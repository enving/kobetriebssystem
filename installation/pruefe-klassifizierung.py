#!/usr/bin/env python3
"""Bauprüfung nach PRD §6.3 Nr. 4 auf dem vollständigen Auslieferungspaket."""
import pathlib
import re
import sys


def pruefen(root):
    # Byteprüfung erfasst auch nicht als UTF-8 lesbare Begleitdateien.
    marker = re.compile(
        rb'''(?im)^[ \t]*(?:\xef\xbb\xbf)?["']?klassifizierung["']?[ \t]*:[ \t]*["']?(vertraulich|streng)\b'''
    )
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink im Auslieferungspaket: {path.relative_to(root)}")
        if path.is_file() and marker.search(path.read_bytes()):
            raise ValueError(f"Klassifiziert: {path.relative_to(root)}; Bau verweigert")


if __name__ == "__main__":
    try:
        pruefen(pathlib.Path(sys.argv[1]))
    except (OSError, ValueError) as error:
        print(f"FEHLER: {error}", file=sys.stderr)
        sys.exit(3)
