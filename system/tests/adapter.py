#!/usr/bin/env python3
"""Lokale Paket-/Update-/Rücknahmeprobe; keine Agentensitzung oder Installation."""
import json
import pathlib
import shutil
import subprocess
import tempfile

repo = pathlib.Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory(prefix='ko-adapter-') as tmp:
    root = pathlib.Path(tmp)
    for name in ('installation', 'system', 'kontext', '.agents', 'beispiel', 'agents'):
        shutil.copytree(repo / name, root / name)
    shutil.copy2(repo / 'AGENTS.md', root / 'AGENTS.md')
    (root / 'person-a-privat.md').write_text('PRIVAT_SYNTHETISCH_8291')
    skill = root / 'beispiel/skills/besprechung-nachbereiten/SKILL.md'
    original = skill.read_text()
    packages = ('ko-basis', 'ko-hermes', 'ko-codex', 'ko-pi')
    def build(version, examples=True):
        args = ['sh', 'installation/bauen.sh', version]
        if examples: args.append('--mit-beispielen')
        p = subprocess.run(args, cwd=root, text=True, capture_output=True, timeout=30)
        assert p.returncode == 0, p.stderr
        for name in packages:
            assert json.loads((root/'dist'/name/'version.json').read_text())['version'] == version
        return root/'dist'
    def skills(dist):
        return [dist / n / folder / 'besprechung-nachbereiten/SKILL.md'
                for n, folder in [('ko-basis','skills'), ('ko-hermes','skills'), ('ko-codex','.agents/skills')]]
    for version, body in [('1-test', original), ('2-test', original+'\nERFUNDENE_REGEL_V2\n'), ('3-test', original)]:
        skill.write_text(body)
        dist = build(version)
        marketplace = json.loads((dist/'.claude-plugin/marketplace.json').read_text())
        assert marketplace['plugins'] == [{'name': 'ko-basis', 'source': './ko-basis'}]
        assert all(p.read_text() == body for p in skills(dist))
        assert all('PRIVAT_SYNTHETISCH_8291' not in p.read_text() for p in dist.rglob('*') if p.is_file())
        for source in ('AGENTS.md', 'kontext/index.md', 'kontext/landkarte.md'):
            assert (root/source).read_text() in (dist/'ko-hermes/SOUL.md').read_text()
        assert (dist/'ko-hermes/config.yaml').read_text().strip() == '{}'
        assert not list((dist/'ko-hermes/cron').iterdir())
        assert json.loads((dist/'ko-hermes/mcp.json').read_text()) == {}
        claude = (dist/'ko-basis/agents/pruefer.md').read_text()
        pi = (dist/'ko-pi/.pi/agents/pruefer.md').read_text()
        assert 'tools: Read, Grep, Glob' in claude and 'omitClaudeMd: true' in claude
        assert 'tools: read, grep, find, ls' in pi and 'model:' not in pi
        assert claude.split('---',2)[2] == pi.split('---',2)[2]
        print('OK:', version, 'vier Paketversionen gleich; drei Skillkopien identisch; Privatmarker fehlt')
    dist = build('4-ohne-beispiele', False)
    assert not any(p.exists() for p in skills(dist))
    # A marker in the newly shipped card must prevent every output from being replaced.
    before = {str(p.relative_to(dist)): p.read_bytes() for p in dist.rglob('*') if p.is_file()}
    with (root/'agents/pruefer.md').open('a') as f: f.write('\nklassifizierung: streng\n')
    refused = subprocess.run(['sh','installation/bauen.sh','5-verweigert'],cwd=root,capture_output=True,text=True)
    assert refused.returncode == 3, refused.stderr
    assert before == {str(p.relative_to(dist)): p.read_bytes() for p in dist.rglob('*') if p.is_file()}
    print('OK: Rückwechsel ohne Beispiele und klassifizierte Karte verweigert alle Pakete unverändert')
print('PASS: Paketbau, Update und Rücknahme; keine Live-Lernschleife nachgewiesen')
