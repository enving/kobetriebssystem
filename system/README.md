# system/
Anleitung zu Ereignissen, Installation und Prüfung: [Hooks erstellen](../docs/hooks-erstellen.md).

- `sperren.txt` – Pfad-Sperrliste (leer, an die Firma anpassen)
- `hooks/` – `block-extern.sh`, `sperre-pfade.sh`, `sessionstart-kontext.sh`, `stop-kontextmahnung.sh`, `opencode-sperre.js`, `pi-sperre.js`, `codex-hooks.json`, `settings-beispiel.json` (Entwürfe, siehe SICHERHEIT.md)
- geplant: Prüfprogramm für `kontext/` (kaputte Links, fehlende Quelle/Prüfdatum, fällige Dateien; z. B. `okf-validate.mjs`)
- `tests/` – `faelle.json` + `pruefen.mjs`: gleiche Testfälle gegen alle Adapter (`node system/tests/pruefen.mjs [pfad-zu-sh]`); bekannte Umgehungen sind als Lücke markiert
