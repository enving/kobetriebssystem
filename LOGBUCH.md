# Logbuch (Belege), Claude Sonnet 5.5, 2026-11-03

- ISO-42001-PDF lokal mit `doc_to_markdown.py --no-images` umgewandelt (72 Seiten, 2366 Zeilen), abgelegt als `normen-lokal/iso-42001-2026-08.md`; `git check-ignore -v` bestätigt Ignorierung, `git ls-files normen-lokal` = 0. PR #3 (gemergt) brachte die Regel nach `main`.
- `main` auf `ecc5baa` gezogen und gepusht; Testbatterie `system/tests/pruefen.mjs` in temporärem Worktree: „keine unerwarteten Abweichungen", je Adapter 3 bekannte Lücken (Wildcard, Großschreibung, Variable).
- Issues angelegt: #1 (Tests für Prompts/Skills), #2 (ISO 42001), #4 (Archon, 30 Minuten). Repo `enving/kobetriebssystem` ist öffentlich (`gh repo view`).
- Archon/Neon: Herstellerseiten über Hilfsagenten gelesen (Archon README und archon.diy: v0.13.2, MIT, SQLite/Postgres, `autoResumeOnQuotaReset` Standard an; Neon: MCP „nur Entwicklung/Test", `neon_superuser`-Falle). Nichts installiert oder ausgeführt.
- Kompass: Nachtrag in `einschaetzungen/mistral-2026-09-29-archon.md`, Commit `ddf46d7`; `kompass vorwissen` Commit `1b348c6` (`werkzeuge/vorwissen.py`, `test_vorwissen.py`, `werkzeuge/kompass`). `python3 -m unittest test_vorwissen`: 6 Tests grün.
- Hook: `~/.claude/hooks/kompass-vorwissen.sh`, in `~/.claude/settings.json` unter `UserPromptSubmit`; Aufruf mit Test-JSON liefert den Archon-Knoten, „ok go" liefert nichts. In einer frischen Sitzung nicht beobachtet.
- Messung zur Suche (vier Umschreibungen, keine belastbare Zahl): „Orchestrierung von Coding-Agenten mit YAML Abläufen" findet den Archon-Knoten nicht an erster Stelle; Kompass hat 450 Knoten, etwa 156.000 Wörter.

# Logbuch (Belege), Claude Sonnet 5.5, 2026-11-05 · Folge 33

- Excalidraw-Renderer des Skills schlug fehl (`Page.wait_for_function` Timeout); Ursache per Playwright-Konsole: `https://esm.sh/@braintree/sanitize-url@6.0.2/es2022/dist/constants.mjs` → 404.
- Skizzen `docs/architektur/skizze-tristan-2026-11-05.excalidraw` und `skizze-v4-2026-11-05.excalidraw` per Einmalskript in SVG-Formen und Textboxen umgesetzt; Kanal-Repo Commit `f47f1f6` (F06, F07 in Folge 33). `deck_bauen.py`: 8 Folien; `deck.py pruefen --profil intern`: 0 Fehler, 1 Warnung (F02 „ai-first“, schon vorher). Folienbilder angesehen (F06 Fußzeile geschnitten → Maßstab 1,05; F07 OFFEN-Block → Maßstab 0,75).

# Logbuch (Belege), Claude Haiku 5.5, 2026-11-10 · OpenWebUI-Testfälle

- `fixtures/04-test-cases.md` (außerhalb des Repos, `/Users/macenving/.local/share/kobetriebssystem-openwebui-test/`) um Fälle L (Werkzeuge und Schreibrechte), M (Persistenz über Neustart) und N (Browser-Automation) ergänzt; A–K unverändert. Nicht ausgeführt: Open Terminal ist laut Übergabe nicht verbunden.
- `git status` am 10.11. (Branch `docs/openwebui-testfaelle`, HEAD `f1751bd`): keine eigenen Repo-Änderungen; `git log @{u}..` leer.
- `gh repo view enving/kobetriebssystem --json visibility`: PUBLIC (10.11.).
- `UEBERGABE.md` im Repo: neuer Kopf vom 10.11. vorangestellt; alter 09.11.-Kopf als historisch markiert, nichts gelöscht.
