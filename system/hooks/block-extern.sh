#!/bin/sh
# Beispiel PreToolUse-Hook (Claude Code): blockt Aktionen nach außen. Nur Gerüst, noch nicht getestet.
# Eingabe: JSON auf stdin. Exit 2 = blockieren.
in=$(cat)
case "$in" in
  *send_message*|*send_email*|*publish*) echo "Gelb: Mensch muss absenden." >&2; exit 2;;
esac
exit 0
