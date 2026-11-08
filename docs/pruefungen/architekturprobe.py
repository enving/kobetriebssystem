#!/usr/bin/env python3
"""Beobachtungsprobe zur Architektur-Recherche, kein Sicherheits-Freigabetest.

Aufruf aus beliebigem Verzeichnis: python3 docs/pruefungen/architekturprobe.py
Der Pluginbau läuft ausschließlich in einer neuen temporären Kopie. Diese bleibt
zur Nachprüfung erhalten. Es werden weder Agenten noch Konnektoren gestartet.
"""
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone


def main():
    repo = pathlib.Path(__file__).resolve().parents[2]
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="ko-architekturprobe-"))
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z", "installation", "system", "kontext", ".agents", "beispiel", "AGENTS.md"],
        cwd=repo,
    ).decode().split("\0")
    for relative in filter(None, tracked):
        source, target = repo / relative, scratch / relative
        if source.is_symlink():
            raise RuntimeError(f"Keine externen Symlink-Ziele in die Probe übernehmen: {relative}")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    hooks = subprocess.run(
        ["node", "system/tests/pruefen.mjs"], cwd=scratch,
        capture_output=True, text=True, timeout=60,
    )
    sentinel = scratch / "kontext" / "interne-probe.md"
    sentinel.write_text(
        "---\nklassifizierung: vertraulich\n---\nSYNTHETISCHE_PROBE_KEINE_FIRMENDATEN\n",
        encoding="utf-8",
    )
    build = subprocess.run(
        ["sh", "installation/bauen.sh", "0.0.0-probe"], cwd=scratch,
        capture_output=True, text=True, timeout=60,
    )
    shipped = scratch / "dist/ko-basis/kontext/interne-probe.md"
    refused = (build.returncode == 3 and not shipped.exists()
               and "Klassifiziert: kontext/interne-probe.md; Bau verweigert" in build.stderr)
    result = {
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "repo_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip(),
        "source": "Dateien aus dem Arbeitsbaum; Auswahl über git ls-files",
        "source_sha256": {
            path: hashlib.sha256((repo / path).read_bytes()).hexdigest()
            for path in filter(None, tracked)
        },
        "hook_probe": {
            "exit_code": hooks.returncode,
            "ok": sum(line.startswith("OK ") for line in hooks.stdout.splitlines()),
            "known_gaps": sum(line.startswith("LÜCKE ") for line in hooks.stdout.splitlines()),
            "stdout": hooks.stdout, "stderr": hooks.stderr,
        },
        "plugin_probe": {
            "exit_code": build.returncode,
            "classified_synthetic_file_shipped": shipped.exists(),
            "classified_build_refused": refused,
            "content_unchanged": shipped.exists() and shipped.read_bytes() == sentinel.read_bytes(),
            "stdout": build.stdout, "stderr": build.stderr,
        },
        "limits": "Adapter-Simulation und Pluginbau; kein Live-Agent, keine echte Zugriffskontrolle, keine Firmendaten.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"Temporäre Kopie zur Nachprüfung: {scratch}", file=sys.stderr)
    return 0 if hooks.returncode == 0 and refused else 1


if __name__ == "__main__":
    raise SystemExit(main())
