# Plugin – Verteilung an alle Mitarbeitenden

Ziel: Regeln, Skills, Kontext und Hooks kommen **automatisch und aktuell** auf jedes Gerät, ohne dass jemand etwas kopiert. Das Repo bleibt die Quelle; das Plugin ist ein erzeugtes Paket daraus.
*Einschätzung (Sonnet 5.5, 2026-11-02): Aufbau stimmt mit dem Plugin-/Marketplace-Modell von Claude Code überein, Schlüsselnamen und Update-Verhalten sind vor Einsatz gegen die aktuelle Doku zu prüfen und auf einem echten Gerät zu testen. Ungetestet.*

## Ablauf (Release-Kette)
```
PR im Firmen-Repo ──> Actions: prüfen ──> Review + Merge auf main ──> Actions: Plugin bauen
   ──> Freigabe-Klick (Environment "release") ──> Release-Repo (privat, Marketplace)
   ──> Geräte holen die neue Version beim Start ──> Lernschleife erzeugt neue PRs
```
1. **Quelle** (`kobetriebssystem`-Kopie der Firma): Skills, Kontext, Hooks, `AGENTS.md`. `main` gesperrt, nur PR.
2. **Prüfen bei jedem PR** (`ci-beispiel/plugin-release.yml`, Job `pruefen`): Hook-Syntax, JSON, Probe-Build; ausbaubar um `okf-validate` (kaputte Links, fehlende Quelle/Prüfdatum), Skill-Evals, Scan auf Personen-/Kundendaten und Zugangsdaten.
3. **Bauen** (`bauen.sh`): kopiert Skills (ohne `_vorlage`), Kontext, Regeln und Hooks nach `dist/ko-basis`, erzeugt `plugin.json` und `hooks/hooks.json` (Pfade über `${CLAUDE_PLUGIN_ROOT}`). `dist/` ist erzeugt und nie von Hand zu ändern.
4. **Freigeben**: Job `freigeben` läuft nur nach Merge und erst nach Klick eines Menschen (GitHub Environment mit Pflicht-Reviewer). Version = Datum + Kurz-Hash, als Tag.
5. **Veröffentlichen**: in ein **separates, privates Release-Repo** (`marketplace-beispiel.json` als `.claude-plugin/marketplace.json`). Das Token ist nur für dieses Repo berechtigt. Mitarbeitende brauchen nie Zugriff auf das Quell-Repo (siehe `docs/recherche.md`).

## Auf die Geräte bringen
- **Einmalig durch die IT:** Managed Settings (`managed-settings-beispiel.json`) tragen den Marketplace und `enabledPlugins` ein, sperren fremde Marketplaces (`strictKnownMarketplaces`) und schalten `skip-permissions` ab. Nur so kann eine Person die Hooks nicht abschalten. Verteilung der Datei über das vorhandene Geräte-Management (MDM/Intune/Jamf).
- **Updates:** Marketplace mit automatischer Aktualisierung beim Start. Jede veröffentlichte Version muss die `version` in `plugin.json` erhöhen (macht der Build), sonst sehen Geräte keine Änderung. Bei Rücknahme: letzten Tag erneut als neue Version veröffentlichen, nicht das Release-Repo zurücksetzen.
- **Claude-App (nicht Code):** Plugin über die Organisationsfunktionen der Claude-App bereitstellen, sofern der Tarif es zulässt. [OFFEN: Tarif und Funktionsumfang prüfen.]

## Rollen
Ein Plugin je Zuschnitt: `ko-basis` für alle, `ko-<abteilung>` für Zusatz-Skills. `bauen.sh` baut bisher nur `ko-basis`; Abteilungs-Plugins brauchen einen Ordner je Abteilung im Quell-Repo (z. B. `.agents/skills/<abteilung>/`) und einen weiteren Build-Schritt. [OFFEN: Zuordnung Person → Plugin. Managed Settings gelten gerätweise; je Rolle verschiedene Dateien oder Benutzer-Einstellungen über die Gerätegruppe der IT.]

## Rückweg (Lernschleife)
Korrekturen entstehen auf dem Gerät als Vorschlag („Ja / nein / einmalig“). Bei „Ja“ erzeugt der Agent einen PR gegen das **Quell-Repo**, nie eine Änderung im Plugin selbst (das Plugin ist schreibgeschützt erzeugt). Damit schließt sich die Kette: PR → Prüfung → Merge → Release → alle Geräte.

## Grenzen
- Hooks bleiben Textprüfung, siehe `SICHERHEIT.md`. Das Plugin ersetzt keine Rechte im Dateisystem.
- Personen- und Kundendaten gehören nie ins Plugin: Der Build-Scan muss sie vor der Freigabe stoppen.
- Die Actions-Datei liegt bewusst unter `plugins/ci-beispiel/` und läuft nicht von selbst. Zum Einsatz nach `.github/workflows/` kopieren, Repo-Namen und Secret anpassen.

## Dateien hier
`bauen.sh` · `marketplace-beispiel.json` · `managed-settings-beispiel.json` · `ci-beispiel/plugin-release.yml`
