#!/bin/sh
# PreToolUse-Hook (Claude Code): blockt Zugriffe auf gesperrte Pfade und klassifizierte Dateien.
# Eingabe: JSON auf stdin. Exit 2 = blockieren (Meldung an stderr geht an den Agenten).
# Grenze: reine Textprüfung. Ein Bash-Umweg (Variablen, cd, Symlinks) wird nicht sicher erkannt –
# die Sperre ersetzt keine Rechte im Dateisystem. Dort zuerst sperren.
dir=$(dirname "$0")
liste="${SPERRLISTE:-$dir/../sperren.txt}"
in=$(cat)
# Zeichenfolge aus Pfad-/Kommando-Feldern (grob, ohne JSON-Parser)
ziele=$(printf '%s' "$in" | grep -oE '"(file_path|path|command|pattern)" *: *"[^"]*"' | sed -E 's/^"[^"]*" *: *"//; s/"$//')
[ -z "$ziele" ] && exit 0

# 1. Pfad-Sperrliste
if [ -f "$liste" ]; then
  grep -vE '^[[:space:]]*(#|$)' "$liste" | while IFS= read -r muster; do
    printf '%s\n' "$ziele" | grep -qF -- "$muster" && { echo "Gesperrter Pfad ($muster). Mensch fragen." >&2; exit 3; }
  done
  [ $? -eq 3 ] && exit 2
fi

# 2. Klassifizierung per Metadaten: Kopfzeile "klassifizierung: vertraulich|streng"
printf '%s\n' "$ziele" | while IFS= read -r f; do
  [ -f "$f" ] && head -c 2000 "$f" 2>/dev/null | grep -qiE 'klassifizierung: *(vertraulich|streng)' && { echo "Klassifiziert ($f). Nicht für Agenten freigegeben." >&2; exit 3; }
done
[ $? -eq 3 ] && exit 2
exit 0
