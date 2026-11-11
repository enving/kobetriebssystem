#!/usr/bin/env python3
"""Erzeugte Adapter aus dem bereits zusammengestellten Plugin; keine Nutzerprofile."""
import json
import pathlib
import shutil
import sys

root = pathlib.Path(sys.argv[1])
plugin = root / 'ko-basis'
version = json.loads((plugin / '.claude-plugin/plugin.json').read_text())['version']
for name in ('ko-basis', 'ko-codex', 'ko-pi'):
    target = root / name
    target.mkdir(exist_ok=True)
    (target / 'version.json').write_text(json.dumps({'version': version}, ensure_ascii=False) + '\n')

marketplace = root / '.claude-plugin'
marketplace.mkdir()
(marketplace / 'marketplace.json').write_text(json.dumps({
    'name': 'ko-lokal', 'owner': {'name': 'OS-Betreuung'},
    'plugins': [{'name': 'ko-basis', 'source': './ko-basis'}]
}, ensure_ascii=False) + '\n')
codex = root / 'ko-codex'
(codex / 'AGENTS.md').write_text((plugin / 'AGENTS.md').read_text() + '\n\nPaketversion: ' + version + '\n')
(codex / '.agents').mkdir()
shutil.copytree(plugin / 'skills', codex / '.agents/skills')
shutil.copytree(plugin / 'kontext', codex / 'kontext')

# Pi example subagent extension uses lowercase tool names and an omitted model to inherit.
# This is a card for that extension, not an installed or automatically running agent.
pi = root / 'ko-pi/.pi/agents'
pi.mkdir(parents=True)
card = (plugin / 'agents/pruefer.md').read_text()
assert 'tools: Read, Grep, Glob\n' in card and 'model: inherit\n' in card and 'omitClaudeMd: true\n' in card, 'Prüferkarte: Adapterabbildung prüfen'
card = card.replace('tools: Read, Grep, Glob', 'tools: read, grep, find, ls')
card = card.replace('model: inherit\n', '').replace('omitClaudeMd: true\n', '')
(pi / 'pruefer.md').write_text(card)
