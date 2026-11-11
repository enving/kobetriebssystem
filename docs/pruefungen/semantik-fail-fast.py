"""Probe ohne Netz oder Push: Fehler muss den folgenden Marker verhindern."""
import pathlib
import subprocess
import sys
import tempfile

with tempfile.TemporaryDirectory() as directory:
    marker = pathlib.Path(directory) / 'push-marker'
    code = (
        'import pathlib, subprocess, sys\n'
        'subprocess.run([sys.executable, "-c", '
        '\'raise AssertionError("absichtliche Probe")\'], check=True)\n'
        f'pathlib.Path({str(marker)!r}).touch()\n'
    )
    result = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
    assert result.returncode == 1, result.returncode
    assert 'AssertionError: absichtliche Probe' in result.stderr
    assert 'CalledProcessError' in result.stderr
    assert not marker.exists(), 'Nachfolgender Marker wurde erreicht'
    print('Innere Assertion: Exit 1; aufrufender Prozess: Exit 1')
    print('CalledProcessError beobachtet; nachfolgender Marker unerreichbar')
    print('Keine Netz- oder Pushhandlung Bestandteil der Probe')
