#!/usr/bin/env python3
"""Regression und Show-me mit ausschließlich erfundenen Dateien, ohne Modellaufruf."""
import pathlib
import shutil
import subprocess
import tempfile

repo = pathlib.Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory(prefix='ko-bau-test-') as tmp:
    root = pathlib.Path(tmp)
    for name in ('installation', 'system', 'kontext', '.agents', 'beispiel'):
        shutil.copytree(repo / name, root / name, symlinks=True)
    shutil.copy2(repo / 'AGENTS.md', root / 'AGENTS.md')

    def build(examples=False):
        return subprocess.run(['sh', 'installation/bauen.sh', '0.0.0-test'] +
                              (['--mit-beispielen'] if examples else []),
                              cwd=root, capture_output=True, text=True, timeout=30)

    targets = ['kontext/erfundene probe.md',
               '.agents/skills/probe/SKILL.md',
               '.agents/skills/probe/beilage.txt',
               'beispiel/skills/probe/SKILL.md',
               'system/hooks/probe.sh', 'AGENTS.md', 'system/sperren.txt']
    count = 0
    for examples in (False, True):
        baseline = build(examples)
        assert baseline.returncode == 0, baseline.stderr
        print(baseline.stdout.strip())
        output = root / 'dist/ko-basis'
        def snapshot():
            return {str(p.relative_to(output)): p.read_bytes()
                    for p in output.rglob('*') if p.is_file()}
        for name in targets:
            path = root / name
            existed = path.exists()
            original = path.read_bytes() if existed else None
            path.parent.mkdir(parents=True, exist_ok=True)
            for marker in ('vertraulich', 'streng', '"VERTRAULICH" # Probe', "'streng'", 'öffentlich', None):
                body = 'ERFUNDENE_PROBE_OHNE_FIRMENDATEN\n'
                if marker is not None:
                    body = f'---\nklassifizierung: {marker}\n---\n' + body
                path.write_text(body)
                before = snapshot()
                result = build(examples)
                blocked = marker not in ('öffentlich', None) and (examples or not name.startswith('beispiel/'))
                assert result.returncode == (3 if blocked else 0), (name, marker, result.stderr)
                if blocked:
                    assert 'Klassifiziert:' in result.stderr and 'Bau verweigert' in result.stderr
                    assert snapshot() == before, 'Verweigerung hat vorherige Ausgabe geändert'
                count += 1
                if name == targets[0] and marker in ('vertraulich', 'öffentlich'):
                    print(f'SHOW-ME Beispiele={examples}, Marker={marker}, Exit={result.returncode}: '
                          + (result.stderr or result.stdout).strip())
            if existed:
                path.write_bytes(original)
            else:
                path.unlink()
                # Den synthetischen Skill nach dem Fall vollständig entfernen.
                if '/skills/probe/' in name:
                    shutil.rmtree(path.parent)
        assert build(examples).returncode == 0
    print(f'OK: {count} Klassifizierungsfälle; normaler Bau und --mit-beispielen')
