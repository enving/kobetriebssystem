#!/bin/sh
# Plugin-Kontext vollständig aus dem installierten Paket, unabhängig vom Arbeitsverzeichnis.
# Fehlende Pflichtquellen sichtbar melden; der Sitzungsstart bleibt möglich.
root=${CLAUDE_PLUGIN_ROOT:-}
if [ -z "$root" ]; then
  echo 'FEHLER: CLAUDE_PLUGIN_ROOT fehlt; Plugin-Pflichtquellen können nicht geladen werden.'
  exit 0
fi
for quelle in .claude-plugin/plugin.json AGENTS.md kontext/index.md kontext/landkarte.md; do
  printf '\n=== Pluginquelle: %s ===\n' "$quelle"
  if [ ! -f "$root/$quelle" ] || ! cat "$root/$quelle"; then
    printf '\nFEHLER: Plugin-Pflichtquelle fehlt oder ist nicht lesbar: %s\n' "$quelle"
  fi
done
exit 0
