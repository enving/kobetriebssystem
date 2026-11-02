# Werkzeug-Matrix: Claude Code, OpenCode, Pi, Codex

Stand 2026-11-02. Getestet auf Windows 11 (Build 26200, Nutzer ohne Admin) und macOS. Versionen: Claude Code 2.1.309, OpenCode 1.19.5, Pi 0.73.1.
Belegstufen: **live** = im echten Programm erlebt · **Skript** = Skript direkt aufgerufen, nicht durchs Programm · **Doku** = nur aus Hersteller-Doku gelesen · **offen** = nicht geprüft.

| | Claude Code | OpenCode | Pi |
|---|---|---|---|
| Blockieren vor Werkzeugaufruf | `PreToolUse`-Hook, Exit 2 (Skript; **offen** live) | Plugin `tool.execute.before`, Fehler werfen (**live**: Lesen von gesperrtem Pfad scheiterte, Modell meldete die Sperre) | Erweiterung `tool_call`, `{block:true}` (Doku; Prüffunktion per Skript) |
| Ablage Projekt / Person | Plugin (`--plugin-dir`, Marketplace), `.claude/settings.json` | `.opencode/plugins/`, `~/.config/opencode/plugins/` (live für Projekt) | `.pi/extensions/` (erst nach Projekt-Vertrauen), `~/.pi/agent/extensions/` |
| Installation ohne Admin | Marketplace + Install + Update (**live**, lokaler Ordner; Git-Quelle **offen**) | `npm install -g opencode-ai` (**live**); Plugin als Datei (**live**) | npm-Paket; Installation **offen** |
| Firmenebene, vom Nutzer nicht änderbar | Managed Settings (**offen**, Pfad unter Windows ungeprüft) | Managed Config `%ProgramData%\opencode` bzw. `/etc/opencode`, `/Library/Application Support/opencode` (Doku, Admin nötig; **offen** live) | In den geprüften Doku-Dateien nicht gefunden (**offen**); Erweiterungen laufen mit vollen Rechten des Nutzers |
| Regelwerk `AGENTS.md` | über `CLAUDE.md` → `@AGENTS.md` | liest `AGENTS.md` (**live**) | **offen** |
| Hooks unter Windows | `sh` über Git for Windows (Skript **live**; durch Programm **offen**) | JavaScript, ohne Shell | JavaScript, ohne Shell |
| Gratis-Modell zum Testen | nein (Anmeldung/Schlüssel nötig) | ja, `opencode/*-free` (**live**) | nein (Schlüssel nötig) |

## Codex (OpenAI), Version 0.166.0-alpha.5.1 (Windows-Desktop-App mit eingebautem CLI)
Quelle für die Hook-Aussagen: developers.openai.com/codex/hooks (gelesen 2026-11-02).
- **Anmeldung:** über ChatGPT-Konto (`codex login status` → "Logged in using ChatGPT"). Günstige Modelle laut Modell-Cache der App: `gpt-5.6-luna` (älter, schnell), `gpt-6-luna` (schnell, günstig); wir nehmen `gpt-5.6-luna` mit `model_reasoning_effort=low`.
- **Hook-Ereignis zum Blockieren:** `PreToolUse`. Deckt Bash, Dateiänderungen über `apply_patch`, MCP-Aufrufe und andere lokale Funktionen ab. **Es gibt kein eigenes Lese-Werkzeug:** Lesen läuft als Shell-Befehl (`tool_name: "Bash"`, `tool_input.command`). Die Pfadsperre muss deshalb den Befehlstext prüfen, nicht ein Pfad-Feld.
- **Blockieren:** Exit 2 mit Grund auf stderr, oder JSON `permissionDecision: "deny"`. Die Datenform entspricht der von Claude Code, `block-extern.sh` und `sperre-pfade.sh` laufen unverändert (Skript, Testbatterie: gleiche Ergebnisse wie bei Claude Code).
- **Ablage:** `~/.codex/hooks.json`, `~/.codex/config.toml`, `<repo>/.codex/hooks.json`, `<repo>/.codex/config.toml`; auch in Plugins (`hooks/hooks.json`). Windows-Befehl über `commandWindows`.
- **Falle (Doku):** Nicht verwaltete Hooks müssen erst geprüft und vertraut werden (`/hooks`), sonst laufen sie nicht. Verbindlich nur als **verwaltete Hooks** (System, MDM, Cloud, `requirements.toml`), die der Nutzer nicht abschalten kann. `--dangerously-bypass-hook-trust` umgeht die Vertrauensprüfung (nur für Tests).
- **Live auf dem Laptop gelernt (Belege):**
  - `codex exec` liest Standardeingabe mit, wenn sie offen ist, und hängt dann ohne Ausgabe. Abhilfe: Standardeingabe aus leerer Datei.
  - `--ignore-user-config` entfernt auch die Windows-Sandbox-Einstellung; danach lehnt Codex Shell-Befehle mit "blocked by policy" ab.
  - Die Windows-Sandbox (`elevated`: "timed out connecting runner pipe-in"; `unelevated`: Exit `0xC0000142`) startet **nicht in einer SSH-Sitzung**. Codex-Tests mit Shell-Befehlen brauchen eine angemeldete Desktop-Sitzung.
  - Codex las `AGENTS.md` im Projekt von selbst und hielt sich an die "vorgeschriebenen Kontextdateien".
- **Offen:** Hook im echten Lauf (blockiert er? und: läuft er ohne Vertrauen nicht?), verwaltete Hooks per `requirements.toml` unter Windows, Plugin-Weg. Ein Lauf mit abgeschalteter Sandbox wurde von der Sicherheitsprüfung abgelehnt und deshalb nicht gemacht.

## Testbatterie (`system/tests/pruefen.mjs`)
Dieselben 11 Fälle laufen gegen alle Adapter (Claude Code, Codex, OpenCode, Pi), auf macOS und auf dem Windows-Laptop. **Ergebnis: identisch.** 8 Fälle wie erwartet (senden, Lesen erlaubt/gesperrt, Windows-Backslash, Glob, `bash` direkt, `cd`, harmlos). 3 Umgehungen sind **nicht** abgefangen:
- Wildcard (`geheim-o*\a.txt`), Groß-/Kleinschreibung (`GEHEIM-ORDNER`, Windows ist case-insensitiv), Variablen (`%A%%B%`).

## Live-Beleg der Lücke (OpenCode, Windows)
1. Nur Plugin aktiv: `powershell Get-Content geheim-o*/a.txt` → **Inhalt kam durch** (Sperre umgangen).
2. Zusätzlich Dateisystem-Sperre (`icacls … /deny test:(OI)(CI)(R)`) → derselbe Befehl **scheiterte** ("ItemNotFound"). Gegenprobe danach zurückgenommen, Datei wieder lesbar.

**Folgerung (Einschätzung, Sonnet 5.5, 2026-11-02):** Die Hooks aller drei Werkzeuge sind Textfilter. Verbindliche Sperren gehören ins Dateisystem; Hooks sind zweite Linie. Das gilt unabhängig vom Werkzeug.

## Offen
- Claude Code live: Hook blockiert im echten Lauf; Managed-Settings-Pfad und -Schlüssel unter Windows; Marketplace aus Git (echtes Update-Verhalten).
- OpenCode: Managed Config mit `plugin`-Eintrag erzwingt das Plugin wirklich (Admin nötig).
- Pi: Installation, Erweiterung im echten Lauf, Firmenebene.
- Dateischutz per ACL als Standard in der Vorlage beschreiben (`SICHERHEIT.md`).
