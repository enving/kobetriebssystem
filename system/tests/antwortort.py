#!/usr/bin/env python3
"""S20: reale Paketgrenzen prüfen, keine Chat- oder Mitgliedschaftssimulation.

Exit 0: alle gemessenen Teilkriterien erfüllt; 3: Schutzfunktion fehlt;
1: technischer Fehler. Die vollständige Chat-Abnahme bleibt separat offen.
"""
import argparse
import hashlib
import json
import pathlib
import shutil
import stat
import subprocess
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
FALL = pathlib.Path('beispiel/szenarien/S20-antwortort-und-widerruf/fall.json')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def probe():
    fall = json.loads((REPO / FALL).read_text())
    for kind in ('gemeinsam', 'vertraulich'):
        assert fall[kind]['marker'].strip() and fall[kind]['marker'] in fall[kind]['text']
    assert fall['gemeinsam']['marker'] != fall['vertraulich']['marker']
    results = []

    def record(name, passed, evidence):
        results.append({'fall': name, 'bestanden': passed, 'beleg': evidence})

    with tempfile.TemporaryDirectory(prefix='ko-antwortort-') as tmp:
        root = pathlib.Path(tmp) / 'repo'
        root.mkdir()
        for name in ('installation', 'system', 'kontext', '.agents', 'beispiel', 'agents'):
            shutil.copytree(REPO / name, root / name,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '*.pyo'))
        shutil.copy2(REPO / 'AGENTS.md', root / 'AGENTS.md')
        source = root / fall['datei']
        assert not source.exists(), 'Probe darf keine vorhandene Quelldatei ersetzen'
        source.write_text(fall['gemeinsam']['text'])

        def build(version):
            return subprocess.run(['sh', 'installation/bauen.sh', version], cwd=root,
                                  text=True, capture_output=True, timeout=60)

        built = build('s20-gemeinsam')
        if built.returncode != 0:
            raise RuntimeError(built.stdout + built.stderr)
        # Zwei Ablagen desselben echten Codex-Pakets, KEINE getrennten Chatidentitäten.
        copies = {}
        for surface in ('persoenliche-nachricht', 'oeffentlicher-kanal'):
            target = pathlib.Path(tmp) / surface
            shutil.copytree(root / 'dist/ko-codex', target)
            copies[surface] = target / fall['datei']
            record('gemeinsam-' + surface,
                   fall['gemeinsam']['marker'] in copies[surface].read_text(),
                   {'paket': 'ko-codex', 'marker': fall['gemeinsam']['marker']})

        # Echte lokale Rechteänderung nur an der temporären Quelldatei. Der gelesene
        # Inhalt wird nicht aus einem Test-Dictionary mit erfundenen Rechten bezogen.
        mode = stat.S_IMODE(source.stat().st_mode)
        try:
            source.chmod(0)
            try:
                source.read_bytes()
                denied = False
            except PermissionError:
                denied = True
            if not denied:
                raise RuntimeError('Quelldatei bleibt trotz chmod 000 lesbar; '
                                   'Widerrufsprobe unter diesem Konto nicht belastbar')
            record('quelle-nach-rechteentzug', True, {'direktes_lesen': 'PermissionError'})
            retained = {surface: fall['gemeinsam']['marker'] in path.read_text()
                        for surface, path in copies.items()}
            record('verteilte-kopie-nach-rechteentzug', not any(retained.values()),
                   {'alter_marker_weiter_lesbar': retained,
                    'grenze': 'Dateirechte entzogen, keine Slack-Mitgliedschaft getestet'})
        finally:
            source.chmod(mode)

        # Die bestehende Klassifizierungssperre darf weder umgangen noch durch eine
        # neue, nur für diese Probe gebaute Berechtigungslogik ersetzt werden.
        source.write_text(fall['vertraulich']['text'])
        assert fall['vertraulich']['marker'] in source.read_text()
        classified = build('s20-vertraulich')
        blocked = classified.returncode == 3 and 'Klassifiziert:' in classified.stderr
        if not blocked:
            raise RuntimeError('Klassifizierungsgegenprobe unerwartet: '
                               + classified.stdout + classified.stderr)
        # Das tatsächliche Bauartefakt prüfen, nicht nur die vor dem zweiten Bau
        # abgelegten Kopien. Ein fehlgeschlagener Bau darf nichts Neues ausliefern.
        fresh = fall['vertraulich']['marker'] in (root / 'dist/ko-codex' / fall['datei']).read_text()
        record('vertraulich-oeffentlich-nicht-ausgeliefert', not fresh,
               {'bau_exit': classified.returncode, 'schutzebene': 'globaler Bauabbruch',
                'keine_aussage_ueber': 'Ausgangskontrolle in einem Chat'})
        record('vertraulich-nur-persoenlich-verfuegbar', fresh,
               {'bau_exit': classified.returncode,
                'quelle_lokal_lesbar': True,
                'grenze': 'Bau verweigert auch ein Paket für den berechtigten Kreis; '
                          'Antwortort und Mitgliedschaft sind keine Bauparameter'})

        # Sensitivitätskontrolle ausschließlich in der wegwerfbaren Testkopie:
        # Ohne vorhandenes Klassifizierungsetikett muss der private Köder tatsächlich
        # im neu gebauten Paket auftauchen, sonst könnte die Probe blind sein.
        source.write_text(fall['vertraulich']['text'].split('---\n', 2)[2])
        unprotected = build('s20-gegenprobe-ohne-etikett')
        if unprotected.returncode != 0:
            raise RuntimeError(unprotected.stdout + unprotected.stderr)
        exposed = fall['vertraulich']['marker'] in (root / 'dist/ko-codex' / fall['datei']).read_text()
        record('gegenprobe-ohne-klassifizierung', exposed,
               {'privater_koeder_im_paket': exposed, 'nur_temporaere_testkopie': True})

    return {
        'szenario': 'S20', 'frage': fall['frage'],
        'pruefebene': 'Paketbau, Dateikopien und lokale Quelldateirechte',
        'quellen_sha256': {str(p): digest(REPO / p) for p in (
            FALL, pathlib.Path('installation/bauen.sh'), pathlib.Path('installation/adapter.py'),
            pathlib.Path('installation/pruefe-klassifizierung.py'),
            pathlib.Path('system/tests/antwortort.py'))},
        'faelle': results,
        'gesamt_bestanden': all(r['bestanden'] for r in results),
        'nicht_geprueft': ['Chatantworten und Umschreibungen', 'reale getrennte Identitäten',
                          'Slack-Mitgliedschaft und deren Widerruf', 'Modellkontext und Logs',
                          'lebende Fachsystemverbindungen'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=pathlib.Path, help='JSON-Ergebnis zusätzlich hier ablegen')
    args = parser.parse_args()
    result = probe()
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')
    return 0 if result['gesamt_bestanden'] else 3


if __name__ == '__main__':
    raise SystemExit(main())
