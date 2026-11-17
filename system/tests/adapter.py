#!/usr/bin/env python3
"""Lokale Paket-/Update-/Rücknahmeprobe; keine Agentensitzung oder Installation."""
import json
import pathlib
import shutil
import subprocess
import tempfile

repo = pathlib.Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory(prefix='ko-adapter-') as tmp:
    root = pathlib.Path(tmp) / 'repo'
    root.mkdir()
    for name in ('installation', 'system', 'kontext', '.agents', 'beispiel', 'agents'):
        shutil.copytree(repo / name, root / name)
    shutil.copy2(repo / 'AGENTS.md', root / 'AGENTS.md')
    # Auch nach Ausführung der Python-Skillwerkzeuge bleiben alle Pakete quelltextrein.
    for folder in ('.agents/skills/skill-creator', 'beispiel/skills/besprechung-nachbereiten'):
        cache = root / folder / '__pycache__'
        cache.mkdir(exist_ok=True)
        (cache / 'probe.pyc').write_bytes(b'\xa7\r\r\nPYTHON_CACHE_TEST')
        (root / folder / 'probe.pyo').write_bytes(b'\xa7\r\r\nPYTHON_CACHE_TEST')
    (root / 'person-a-privat.md').write_text('PRIVAT_SYNTHETISCH_8291')
    skill = root / 'beispiel/skills/besprechung-nachbereiten/SKILL.md'
    original = skill.read_text()
    packages = ('ko-basis', 'ko-codex', 'ko-pi')
    def build(version, examples=True):
        args = ['sh', 'installation/bauen.sh', version]
        if examples: args.append('--mit-beispielen')
        p = subprocess.run(args, cwd=root, text=True, capture_output=True, timeout=30)
        assert p.returncode == 0, p.stderr
        for name in packages:
            assert json.loads((root/'dist'/name/'version.json').read_text())['version'] == version
        assert not any(p.name == '__pycache__' or p.suffix in ('.pyc', '.pyo')
                       for p in (root/'dist').rglob('*'))
        return root/'dist'
    def skills(dist):
        return [dist / n / folder / 'besprechung-nachbereiten/SKILL.md'
                for n, folder in [('ko-basis','skills'), ('ko-codex','.agents/skills')]]
    for version, body in [('1-test', original), ('2-test', original+'\nERFUNDENE_REGEL_V2\n'), ('3-test', original)]:
        skill.write_text(body)
        dist = build(version)
        marketplace = json.loads((dist/'.claude-plugin/marketplace.json').read_text())
        assert marketplace['plugins'] == [{'name': 'ko-basis', 'source': './ko-basis'}]
        assert all(p.read_text() == body for p in skills(dist))
        assert all('PRIVAT_SYNTHETISCH_8291' not in p.read_text() for p in dist.rglob('*') if p.is_file())
        claude = (dist/'ko-basis/agents/pruefer.md').read_text()
        pi = (dist/'ko-pi/.pi/agents/pruefer.md').read_text()
        assert 'tools: Read, Grep, Glob' in claude and 'omitClaudeMd: true' in claude
        assert 'tools: read, grep, find, ls' in pi and 'model:' not in pi
        assert claude.split('---',2)[2] == pi.split('---',2)[2]
        print('OK:', version, 'drei Paketversionen gleich; zwei Skillkopien identisch; Privatmarker fehlt')
    dist = build('4-ohne-beispiele', False)
    assert not any(p.exists() for p in skills(dist))
    # Externe Inhalte dürfen auch ohne Klassifizierungsmarker nicht über Links hinein.
    external = pathlib.Path(tmp) / 'extern'
    external.mkdir()
    (external / 'inhalt.txt').write_text('EXTERN_SYNTHETISCH_4831')
    before = {str(p.relative_to(dist)): p.read_bytes() for p in dist.rglob('*') if p.is_file()}
    link_cases = 0
    for folder, examples in [('.agents/skills/wissen-pflegen', False),
                             ('.agents/skills/wissen-pflegen', True),
                             ('beispiel/skills/besprechung-nachbereiten', True)]:
        for target in (external / 'inhalt.txt', external, external / 'fehlt.txt'):
            link = root / folder / 'extern'
            link.symlink_to(target)
            args = ['sh', 'installation/bauen.sh', '5-link-verweigert']
            if examples: args.append('--mit-beispielen')
            refused = subprocess.run(args, cwd=root, capture_output=True, text=True, timeout=30)
            assert refused.returncode == 3 and 'Symlink' in refused.stderr, refused.stderr
            assert before == {str(p.relative_to(dist)): p.read_bytes() for p in dist.rglob('*') if p.is_file()}
            link.unlink()
            link_cases += 1
    # copytree folgt selbst mit symlinks=True einem verknüpften Wurzelverzeichnis.
    link = root / '.agents/skills/verknuepft'
    link.symlink_to(root / '.agents/skills/wissen-pflegen', target_is_directory=True)
    refused = subprocess.run(['sh', 'installation/bauen.sh', '5-wurzel-verweigert'],
                             cwd=root, capture_output=True, text=True, timeout=30)
    assert refused.returncode == 3 and 'Symlink' in refused.stderr, refused.stderr
    assert before == {str(p.relative_to(dist)): p.read_bytes() for p in dist.rglob('*') if p.is_file()}
    link.unlink()
    print('OK:', link_cases + 1, 'Symlink-Gegenfälle verweigert; alle bisherigen Pakete unverändert')
    # A marker in the newly shipped card must prevent every output from being replaced.
    before = {str(p.relative_to(dist)): p.read_bytes() for p in dist.rglob('*') if p.is_file()}
    with (root/'agents/pruefer.md').open('a') as f: f.write('\nklassifizierung: streng\n')
    refused = subprocess.run(['sh','installation/bauen.sh','5-verweigert'],cwd=root,capture_output=True,text=True)
    assert refused.returncode == 3, refused.stderr
    assert before == {str(p.relative_to(dist)): p.read_bytes() for p in dist.rglob('*') if p.is_file()}
    print('OK: Rückwechsel ohne Beispiele und klassifizierte Karte verweigert alle Pakete unverändert')
print('PASS: Paketbau, Update und Rücknahme; keine Live-Lernschleife nachgewiesen')
