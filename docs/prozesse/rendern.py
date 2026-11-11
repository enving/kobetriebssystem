#!/usr/bin/env python3
"""BPMN-Quellen mit vorhandener bpmn-cli prüfen und als lokale Ansicht rendern."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
NS = {'b': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}
FLOW_NODES = {'startEvent', 'endEvent', 'boundaryEvent', 'intermediateCatchEvent',
              'intermediateThrowEvent', 'task', 'userTask', 'serviceTask', 'scriptTask',
              'sendTask', 'receiveTask', 'manualTask', 'businessRuleTask', 'callActivity',
              'subProcess', 'exclusiveGateway', 'parallelGateway', 'inclusiveGateway',
              'eventBasedGateway', 'complexGateway'}

# Ein einziger Treiber für lokale CLI und ausdrücklich angegebenen Container.
DRIVER = r'''
import base64,json,pathlib,shutil,subprocess,sys,tempfile
payload=json.load(sys.stdin)
exe=shutil.which('bpmn') or str(pathlib.Path.home()/'.local/bin/bpmn')
def run(args):
 p=subprocess.run([exe,*args],capture_output=True,text=True)
 if p.returncode:
  raise RuntimeError('bpmn '+ ' '.join(args)+': '+p.stdout+p.stderr)
 return p.stdout
version=run(['--version']).strip()
output=[]
with tempfile.TemporaryDirectory(prefix='ko-bpmn-render-') as tmp:
 for item in payload:
  if pathlib.Path(item['file']).name!=item['file']: raise ValueError('Nur Dateinamen erlaubt')
  p=pathlib.Path(tmp)/item['file']; p.write_bytes(base64.b64decode(item['xml']))
  validation=json.loads(run(['validate',str(p),'--json']))
  diagram=json.loads(run(['diagram',str(p),'--json']))
  svg=p.with_suffix('.svg'); run(['render',str(p),'-o',str(svg)])
  # Keine flüchtigen Containerpfade im versionierten Prüfbericht.
  def clean(v):
   if isinstance(v,str): return v.replace(str(p),item['file'])
   if isinstance(v,list): return [clean(x) for x in v]
   if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
   return v
  output.append({'file':item['file'],'validation':clean(validation),'diagram':clean(diagram),
                 'svg':base64.b64encode(svg.read_bytes()).decode()})
print(json.dumps({'cliVersion':version,'models':output}))
'''


def local_model(path):
    root = ET.fromstring(path.read_bytes())
    process = root.find('b:process', NS)
    assert process is not None, f'{path.name}: Prozess fehlt'
    assert process.get('isExecutable') == 'false', f'{path.name}: ausführbar'
    nodes = {e.get('id'): e for e in process if e.tag.split('}')[-1] in FLOW_NODES}
    flows = list(process.findall('b:sequenceFlow', NS))
    outgoing = {id: [] for id in nodes}
    incoming = {id: [] for id in nodes}
    for f in flows:
        a, b = f.get('sourceRef'), f.get('targetRef')
        assert a in nodes and b in nodes, f'{path.name}: ungültige Kante {f.get("id")}'
        outgoing[a].append((b, f.get('name', '')))
        incoming[b].append(a)
    starts = [id for id, e in nodes.items() if e.tag.endswith('}startEvent')]
    ends = [id for id, e in nodes.items() if e.tag.endswith('}endEvent')]
    assert starts and ends, f'{path.name}: Start oder Ende fehlt'
    # Fehler-/Abbruchereignisse werden über ihre Aktivität erreichbar.
    boundary = {id: e.get('attachedToRef') for id, e in nodes.items() if e.tag.endswith('}boundaryEvent')}
    def walk(seed, reverse=False):
        seen, stack = set(), list(seed)
        while stack:
            id = stack.pop()
            if id in seen: continue
            seen.add(id)
            stack.extend(incoming[id] if reverse else [x[0] for x in outgoing[id]])
            if not reverse: stack.extend(b for b, host in boundary.items() if host == id)
        return seen
    assert set(nodes) == walk(starts), f'{path.name}: unerreichbare Knoten {set(nodes)-walk(starts)}'
    assert set(nodes) == walk(ends, True), f'{path.name}: kein Weg zum Ende {set(nodes)-walk(ends,True)}'
    lane_by_node = {}
    for lane in process.findall('.//b:lane', NS):
        for ref in lane.findall('b:flowNodeRef', NS): lane_by_node[ref.text] = lane.get('name', '')
    entries, calls = [], []
    for id, e in nodes.items():
        kind = e.tag.split('}')[-1]
        doc = (e.findtext('b:documentation', '', NS)).strip()
        assert doc and 'Quelle:' in doc, f'{path.name}: undokumentierter Schritt {id}'
        assert id in lane_by_node, f'{path.name}: Bahn fehlt {id}'
        if kind == 'exclusiveGateway' and len(outgoing[id]) > 1:
            assert all(label for _, label in outgoing[id]), f'{path.name}: unbeschriftete Verzweigung {id}'
        call = e.get('calledElement')
        if call: calls.append(call)
        entries.append({'id': id, 'name': e.get('name', ''), 'kind': kind, 'doc': doc,
                        'lane': lane_by_node[id], 'call': call, 'next': outgoing[id]})
    return {'file': path.name, 'id': process.get('id'), 'name': process.get('name'),
            'doc': process.findtext('b:documentation', '', NS), 'nodes': entries,
            'calls': calls, 'nodeCount': len(nodes), 'flowCount': len(flows),
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--container', help='Vorhandener Container mit Python und bpmn-cli')
    args = parser.parse_args()
    paths = sorted(HERE.glob('*.bpmn'))
    assert paths, 'Keine BPMN-Quellen'
    models = [local_model(p) for p in paths]
    ids = {m['id'] for m in models}
    assert len(ids) == len(models), 'Doppelte Prozesskennung'
    for m in models:
        assert set(m['calls']) <= ids, f'{m["file"]}: unbekannter Prozessaufruf'
    payload = [{'file': p.name, 'xml': base64.b64encode(p.read_bytes()).decode()} for p in paths]
    cmd = ['docker', 'exec', '-i', args.container, 'python3', '-c', DRIVER] if args.container else [sys.executable, '-c', DRIVER]
    proc = subprocess.run(cmd, input=json.dumps(payload), capture_output=True, text=True)
    if proc.returncode:
        raise RuntimeError(proc.stdout + proc.stderr)
    result = json.loads(proc.stdout)
    reports = []
    svgs = []
    for m, rendered in zip(models, result['models'], strict=True):
        assert m['file'] == rendered['file'], 'Falsche Ergebniszuordnung'
        state = rendered['validation']['state']
        assert state['errors'] == 0 and state['warnings'] == 0, f'{m["file"]}: {rendered["validation"]}'
        critical = ('through', 'overlaps', 'frameIntrusion', 'frameOverlap', 'labelClash',
                    'labelOnLine', 'labelOutsideFrame', 'labelOnTitle', 'missing',
                    'outsideLane', 'outsidePool', 'outsideSub', 'detachedEdge', 'failed')
        problems = {k: rendered['diagram']['counts'][k] for k in critical if rendered['diagram']['counts'][k]}
        assert not problems, f'{m["file"]}: verdeckte Elemente oder Beschriftungen: {problems}'
        svg = base64.b64decode(rendered['svg']).decode()
        ET.fromstring(svg)
        svgs.append(svg)
        m['svg'] = svg
        reports.append({'file': m['file'], 'sha256': m['sha256'], 'svgSha256': hashlib.sha256(svg.encode()).hexdigest(), 'nodeCount': m['nodeCount'],
                        'flowCount': m['flowCount'], 'validation': rendered['validation'],
                        'diagram': rendered['diagram']})
    # Erst nach allen Prüfungen die abgeleiteten Dateien ersetzen.
    template = (HERE/'ansicht-vorlage.html').read_text()
    assert template.count('/*__MODELS__*/[]') == 1, 'Datenplatzhalter fehlt'
    data = json.dumps(models, ensure_ascii=False).replace('</', '<\\/')
    html = template.replace('/*__MODELS__*/[]', data)
    readme = (HERE/'README.md').read_text()
    begin, end = '<!-- modelle:start -->', '<!-- modelle:ende -->'
    assert readme.count(begin) == readme.count(end) == 1, 'Modellverzeichnis fehlt'
    links = ['| Prozess | Quelle | Bild |', '|---|---|---|']
    for m in models:
        links.append(f'| {m["name"]} | [BPMN]({m["file"]}) | [SVG]({Path(m["file"]).with_suffix(".svg")}) |')
    readme = readme.split(begin)[0]+begin+'\n'+'\n'.join(links)+'\n'+end+readme.split(end)[1]
    for p, svg in zip(paths, svgs, strict=True): p.with_suffix('.svg').write_text(svg)
    (HERE/'ansicht.html').write_text(html)
    report = {'scope': 'Prozessmodell, kein Integrationstest', 'cliVersion': result['cliVersion'],
              'source': '*.bpmn', 'structuralChecks': 'bestanden',
              'viewerSha256': hashlib.sha256(html.encode()).hexdigest(),
              'rendererSha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'templateSha256': hashlib.sha256(template.encode()).hexdigest(), 'models': reports}
    (HERE/'pruefung.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    (HERE/'README.md').write_text(readme)
    print(f'{len(models)} Modelle: 0 CLI-Fehler, 0 CLI-Warnungen; Struktur und Aufrufe geprüft.')
    print(f'{sum(m["nodeCount"] for m in models)} Knoten, {sum(m["flowCount"] for m in models)} Sequenzflüsse; Ansicht und SVGs erzeugt.')


if __name__ == '__main__':
    main()
