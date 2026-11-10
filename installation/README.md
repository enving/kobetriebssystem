# Installation – Verteilung an alle Mitarbeitenden

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
3. **Bauen** (`bauen.sh`): kopiert Skills (ohne `_vorlage`), Kontext, Regeln und Hooks nach `dist/ko-basis`, erzeugt `plugin.json` und `hooks/hooks.json` (Pfade über `${CLAUDE_PLUGIN_ROOT}`). `dist/` ist erzeugt und nie von Hand zu ändern. SessionStart gibt die vollständigen Pflichtquellen und `plugin.json` (einschließlich Version) aus `CLAUDE_PLUGIN_ROOT` aus. Fehlende Quellen erscheinen als `FEHLER` im Kontext; der Start bleibt möglich.
4. **Freigeben**: Job `freigeben` läuft nur nach Merge und erst nach Klick eines Menschen (GitHub Environment mit Pflicht-Reviewer). Version = Datum + Kurz-Hash, als Tag.
5. **Veröffentlichen**: in ein **separates, privates Release-Repo** (`marketplace-beispiel.json` als `.claude-plugin/marketplace.json`). Das Token ist nur für dieses Repo berechtigt. Mitarbeitende brauchen nie Zugriff auf das Quell-Repo (siehe `docs/recherche.md`).

## Auf die Geräte bringen
- **Einmalig durch die IT:** Managed Settings (`managed-settings-beispiel.json`) tragen den Marketplace und `enabledPlugins` ein, sperren fremde Marketplaces (`strictKnownMarketplaces`) und schalten `skip-permissions` ab. Nur so kann eine Person die Hooks nicht abschalten. Verteilung der Datei über das vorhandene Geräte-Management (MDM/Intune/Jamf).
- **Updates:** Automatische Aktualisierung ist für eigene Marketplaces ab Werk aus; eine Person oder ein Admin schaltet sie ein, dann läuft sie nach dem Start einer Sitzung ([Doku](https://code.claude.com/docs/en/plugin-marketplaces), gelesen 06.11.2026; korrigiert die frühere Angabe „beim Start“). [OFFEN: mit welchem Schlüssel Managed Settings sie für alle einschalten; laufende Sitzungen behalten ihren Stand, [PRD](../PRD.md) L5.] Jede veröffentlichte Version muss die `version` in `plugin.json` erhöhen (macht der Build), sonst sehen Geräte keine Änderung. Bei Rücknahme: letzten Tag erneut als neue Version veröffentlichen, nicht das Release-Repo zurücksetzen.
- **Claude-App (nicht Code):** Plugin über die Organisationsfunktionen der Claude-App bereitstellen, sofern der Tarif es zulässt. [OFFEN: Tarif und Funktionsumfang prüfen.]

## Rollen
`bauen.sh` erzeugt Claude- und Codex-Pakete sowie die abgeleitete Pi-Prüferkarte
(siehe unten „Lokale MVP-Paketkette“). Ein verwalteter Codex-Rollout bleibt separat zu prüfen.
Unterstützte Richtlinien, Vertrauensmodell und
offene Abnahmefälle: [Managed Hooks für den Unternehmensrollout](../docs/hooks-erstellen.md#6-managed-hooks-für-den-unternehmensrollout).

Ein Plugin je Zuschnitt: `ko-basis` für alle, `ko-<abteilung>` für Zusatz-Skills. `bauen.sh` baut bisher nur `ko-basis`; Abteilungs-Plugins brauchen einen Ordner je Abteilung im Quell-Repo (z. B. `.agents/skills/<abteilung>/`) und einen weiteren Build-Schritt. [OFFEN: Zuordnung Person → Plugin. Managed Settings gelten gerätweise; je Rolle verschiedene Dateien oder Benutzer-Einstellungen über die Gerätegruppe der IT.]

## Rückweg (Lernschleife)
Korrekturen entstehen auf dem Gerät als Vorschlag („Ja / nein / einmalig“). Bei „Ja“ erzeugt der Agent einen PR gegen das **Quell-Repo**, nie eine Änderung im Plugin selbst (das Plugin ist schreibgeschützt erzeugt). Damit schließt sich die Kette: PR → Prüfung → Merge → Release → alle Geräte. [OFFEN: Das widerspricht Schritt 5 („Mitarbeitende brauchen nie Zugriff auf das Quell-Repo“): Wer dort einen PR stellen kann, kann es auch lesen. Rückweg ohne Lesezugriff ungeklärt, [PRD](../PRD.md) L8.]

## Grenzen
- Hooks bleiben Textprüfung, siehe `SICHERHEIT.md`. Das Plugin ersetzt keine Rechte im Dateisystem.
- Personen- und Kundendaten gehören nie ins Plugin: Der Build-Scan muss sie vor der Freigabe stoppen.
- Die Actions-Datei liegt bewusst unter `installation/ci-beispiel/` und läuft nicht von selbst. Zum Einsatz nach `.github/workflows/` kopieren, Repo-Namen und Secret anpassen.

## Dateien hier
`bauen.sh` · `marketplace-beispiel.json` · `managed-settings-beispiel.json` · `ci-beispiel/plugin-release.yml`

Lokaler Regressionstest: `node system/tests/plugin-start.mjs`. Prüft erzeugte Hook-Befehle aus fremdem Arbeitsverzeichnis mit Leerzeichen im Pluginpfad, vollständige Quellen, Version und fehlende Pflichtquellen. Kein Nachweis für die Darstellung oder Ausführung in einem echten Claude-Code-Client; Installation und Rollout bleiben ungeprüft.

### Bauprüfung und reproduzierbarer Nachweis (#17)

Die Marker-Abnahme steht in [PRD §6.3 Nr. 4](../PRD.md#63-was-gebaut-wird).
`bauen.sh` benötigt jetzt Python 3 und prüft das fertig zusammengestellte Paket in
einer temporären Kopie vor der Ausgabe. Bei Verweigerung (Exit 3) bleibt eine
vorherige `dist/`-Ausgabe unverändert; sie ist kein Ergebnis des verweigerten Baus.
Lesefehler und Symlinks im Paket verweigern den Bau ebenfalls. Dies ist eine
Markerprüfung, keine Erkennung unmarkierter sensibler Inhalte oder Rollenfreigabe.

Show-me und Regression: `python3 system/tests/klassifizierung.py`.
Die Ausgabe zeigt denselben erfundenen Kontext mit vertraulichem Marker (Exit 3,
„Bau verweigert“) und öffentlichem Marker (Exit 0, „gebaut“), jeweils normal und
mit `--mit-beispielen`. Alle Testdateien liegen in einer automatisch entfernten
Temporärkopie. Die vollständige Batterie startet mit `node system/tests/pruefen.mjs`.

Lernschleife: Kopieren ohne Markerprüfung → übernommen (08.11.2026, #17).
Prüffall: `system/tests/klassifizierung.py` prüft beide gesperrten Marker,
öffentliche und fehlende Marker in Kontext, Skills samt Beilagen, Regeln, Hooks
und Sperrliste. Nicht ausgewählte Beispiele beeinflussen den normalen Bau nicht.
Die [Architekturprobe](../docs/pruefungen/architekturprobe.py) muss die tatsächliche
Verweigerung erkennen und `classified_synthetic_file_shipped: false` melden.

Geprüft am 08.11.2026 (lokal, synthetisch):

- `python3 system/tests/klassifizierung.py`: 84 Fälle bestanden.
- `node system/tests/pruefen.mjs`: keine unerwarteten Abweichungen; 32 Hook-Fälle
  bestanden, 12 bestehende Hook-Lücken bleiben ausdrücklich offen.
- `node system/tests/beispiel-build.mjs`: Schalter, Paketinhalt, Rückwechsel und Fallartefakte bestanden.
- `node system/tests/plugin-start.mjs`: Pluginstart-Regression bestanden.
- `python3 docs/pruefungen/architekturprobe.py`: Exit 0; Pluginbau Exit 3,
  `classified_build_refused: true`, `classified_synthetic_file_shipped: false`.
- `sh -n installation/bauen.sh` und `git diff --check`: bestanden.

Keine realen Modellaufrufe, Geräteinstallation oder Anmeldung geprüft.
Der historische Architekturbericht vom 05.11. bleibt als damaliger Befund erhalten.

### Lokaler MVP-Bau: zwei Adapter und Prüferkarte (#25)

Hermes ist als MVP-Adapter seit dem 10.11.2026 gestrichen; `bauen.sh` erzeugt kein `ko-hermes` mehr.

`sh installation/bauen.sh auto --mit-beispielen` erzeugt aus denselben Quellen:

- `dist/ko-basis`: Claude-Plugin einschließlich `agents/pruefer.md`.
- `dist/ko-codex`: Projektpaket mit AGENTS.md, `.agents/skills/` und Kontext.
- `dist/ko-pi`: abgeleitete Prüferkarte für die Pi-Beispielerweiterung subagent;
  kein installierter Dienst und keine automatisch geladene Erweiterung.
- `dist/.claude-plugin/marketplace.json`: lokaler Marketplace nur für ko-basis.

`auto` setzt UTC-Datum und Quell-Kurz-Hash als Version; eine ausdrückliche Version
bleibt möglich. Alle drei Pakete erhalten dieselbe `version.json`. Lokaler Marketplace:
`claude plugin marketplace add ./dist` (hier nicht installiert). Das Codex-Verzeichnis dient als Projektwurzel,
kein verwalteter globaler Rollout. Persönliche Konfiguration wird nie hineinkopiert.
Die Markerprüfung läuft über sämtliche erzeugten Pakete vor Ersetzen von dist.

Die fachliche Prüferdefinition liegt ausschließlich in `agents/pruefer.md`.
Claude erhält Read/Grep/Glob und model inherit; Pi bekommt die entsprechenden
read/grep/find/ls und lässt model weg, um das Sitzungsmodell zu behalten.
omitClaudeMd ist eine Claude-Einstellung; der Pi-Treiber muss seine Ressourcen
weiterhin ausdrücklich begrenzen. Die Karte allein bietet keine Sandbox.
Übergeben werden Ergebnis, Kriterien und Quellen. Eine automatische Einbindung
in jeden Skill-Lauf ist damit noch nicht belegt (L10).

`python3 system/tests/adapter.py` zeigt Version 1, die erfundene Änderung in Version 2
und die ursprünglichen Skillbytes unter neuer Version 3. Beide Adapter bekommen
identische Skills; der private synthetische Marker einer Person fehlt überall.
Rückwechsel ohne Beispiele und Abbruch bei klassifizierter Prüferkarte werden geprüft.
Dies ist ein Paket-/Transportnachweis, kein echter Lernschleifen- oder Modelllauf.
Die Testbatterie `node system/tests/pruefen.mjs` führt die Probe mit aus.

Quellen der Feldabbildung, gelesen 08.11.2026:
[Claude-Unteragenten](https://code.claude.com/docs/en/sub-agents),
[Pi-Beispielparser](https://github.com/earendil-works/pi/blob/085c84e98e7f4c950f2be606466fff4f75d8fe7c/packages/coding-agent/examples/extensions/subagent/agents.ts),
[Codex-Skills](https://developers.openai.com/codex/skills) und
[AGENTS.md](https://developers.openai.com/codex/guides/agents-md).

Lernschleife: Gleiche Quellen allein garantieren keinen gleichen Paketstand.
Prüffall: Adapterprobe vergleicht Versionen und Skillbytes vor Update, nach Update
und nach Rücknahme; ein fremder privater Marker darf in keinem Paket erscheinen.
