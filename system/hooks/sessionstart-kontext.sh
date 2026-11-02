#!/bin/sh
# Beispiel SessionStart-Hook (Claude Code): legt den Projektstand beim Start in den Kontext.
# Stdout eines SessionStart-Hooks wird als Kontext übernommen. Dünner Aufrufer: Logik gehört in ein
# eigenes Werkzeug (hier: kontext/index.md), nicht in den Hook. Ein Hook darf nie eine Sitzung
# blockieren – bei jedem Fehler still mit 0 aussteigen.
datei="${CLAUDE_PROJECT_DIR:-.}/kontext/index.md"
[ -f "$datei" ] || exit 0
echo "=== Projektstand (kontext/index.md, erste 40 Zeilen) ==="
head -n 40 "$datei" 2>/dev/null || exit 0
exit 0
