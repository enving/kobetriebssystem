#!/bin/sh
# Baut das Plugin "ko-basis" aus den Quellen des Repos nach dist/ko-basis. Entwurf, nur Gerüst.
# Quelle bleibt das Repo (Skills, Hooks, Kontext); dist/ ist erzeugt und wird nie von Hand geändert.
set -eu
cd "$(dirname "$0")/.."
version="${1:?Aufruf: installation/bauen.sh <version> [--mit-beispielen]}"
if [ "$version" = auto ]; then
  version="$(date -u +%Y.%m.%d)-$(git rev-parse --short HEAD)"
fi
case "$version" in *[!A-Za-z0-9._-]*) echo "Ungültige Version" >&2; exit 2;; esac
beispiele=false
case "${2:-}" in
  '') ;;
  --mit-beispielen) beispiele=true ;;
  *) echo "Unbekannter Schalter: $2" >&2; exit 2 ;;
esac
[ "$#" -le 2 ] || { echo "Zu viele Argumente" >&2; exit 2; }
# Erst in isolierter Kopie bauen; bei Fehler bleibt die letzte Ausgabe unverändert.
staging=$(mktemp -d)
trap 'rm -rf "$staging"' EXIT
trap 'exit 1' HUP INT TERM
out="$staging/ko-basis"
mkdir -p "$out/.claude-plugin" "$out/skills" "$out/hooks" "$out/kontext"

# Skills: _vorlage* nicht ausrollen
for d in .agents/skills/*/; do
  case "$(basename "$d")" in _*) continue;; esac
  cp -R "${d%/}" "$out/skills/"
done
if [ "$beispiele" = true ]; then
  for d in beispiel/skills/*/; do
    [ -f "$d/SKILL.md" ] || { echo "Beispiel-Skill fehlt: $d" >&2; exit 2; }
    name=$(basename "$d")
    [ ! -e "$out/skills/$name" ] || { echo "Doppelter Skill: $name" >&2; exit 2; }
    cp -R "${d%/}" "$out/skills/"
  done
fi
cp -R kontext/. "$out/kontext/"
cp -R agents "$out/agents"
cp AGENTS.md "$out/AGENTS.md"
cp system/hooks/*.sh "$out/hooks/"
cp system/sperren.txt "$out/sperren.txt"   # sperre-pfade.sh sucht ../sperren.txt

cat > "$out/hooks/hooks.json" <<'JSON'
{
  "hooks": {
    "SessionStart": [{"hooks": [{"type": "command", "command": "sh \"${CLAUDE_PLUGIN_ROOT}/hooks/sessionstart-plugin.sh\"", "timeout": 10}]}],
    "PreToolUse": [
      {"matcher": "Read|Edit|Write|Glob|Grep|Bash", "hooks": [{"type": "command", "command": "sh \"${CLAUDE_PLUGIN_ROOT}/hooks/sperre-pfade.sh\""}]},
      {"matcher": ".*", "hooks": [{"type": "command", "command": "sh \"${CLAUDE_PLUGIN_ROOT}/hooks/block-extern.sh\""}]}
    ]
  }
}
JSON
cat > "$out/.claude-plugin/plugin.json" <<JSON
{"name": "ko-basis", "version": "$version", "description": "Betriebssystem: Regeln, Skills, Kontext, Hooks"}
JSON
python3 installation/adapter.py "$staging"
python3 installation/pruefe-klassifizierung.py "$staging"
rm -rf dist
mkdir -p dist
for paket in "$staging"/* "$staging"/.claude-plugin; do mv "$paket" dist/; done
out="dist/ko-basis"
echo "gebaut: $out ($version), Beispiele: $beispiele"
