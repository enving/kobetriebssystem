#!/bin/sh
# Baut das Plugin "ko-basis" aus den Quellen des Repos nach dist/ko-basis. Entwurf, nur Gerüst.
# Quelle bleibt das Repo (Skills, Hooks, Kontext); dist/ ist erzeugt und wird nie von Hand geändert.
set -eu
cd "$(dirname "$0")/.."
version="${1:?Aufruf: plugins/bauen.sh <version>}"
out="dist/ko-basis"
rm -rf dist && mkdir -p "$out/.claude-plugin" "$out/skills" "$out/hooks" "$out/kontext"

# Skills: _vorlage* nicht ausrollen
for d in .agents/skills/*/; do
  case "$(basename "$d")" in _*) continue;; esac
  cp -R "$d" "$out/skills/"
done
cp -R kontext/. "$out/kontext/"
cp AGENTS.md "$out/AGENTS.md"
cp system/hooks/*.sh "$out/hooks/"
cp system/sperren.txt "$out/sperren.txt"   # sperre-pfade.sh sucht ../sperren.txt

cat > "$out/hooks/hooks.json" <<'JSON'
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Read|Edit|Write|Glob|Grep|Bash", "hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/sperre-pfade.sh"}]},
      {"matcher": ".*", "hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/block-extern.sh"}]}
    ]
  }
}
JSON
cat > "$out/.claude-plugin/plugin.json" <<JSON
{"name": "ko-basis", "version": "$version", "description": "Betriebssystem: Regeln, Skills, Kontext, Hooks"}
JSON
echo "gebaut: $out ($version)"
