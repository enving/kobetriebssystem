# Sicherheit (Vorlage)

## 1. Security by Instruction
Ampel in `AGENTS.md`. Wirkt nur, solange der Agent sie befolgt.

## 2. Security by Design (Technik erzwingt)
- **Rechte nur im jeweiligen Tool**, nie im Agenten. Agent erbt die Rechte der Person (Shell, Konnektoren); ein Cloud-Agent bekommt Rechte explizit.
- **Connector-Tools** in der Claude-App einzeln auf *Immer erlauben / Nachfragen / Blockieren* stellen.
- **Repo:** `main` gesperrt, Änderungen nur per PR; keine Kunden-/Personendaten im Repo.
- **Hooks** (`system/hooks/`, Entwurf, Verdrahtung in `settings-beispiel.json`):
  - `block-extern.sh`: stoppt Senden/Veröffentlichen/Zahlen, auch wenn der Agent sich irrt oder eine Mail ihn austricksen will.
  - `sperre-pfade.sh`: blockt Pfade aus `system/sperren.txt` (Laufwerke wie SharePoint/Nextcloud, Bereiche mit Personal-/Studierendendaten) und Dateien, deren Kopf `klassifizierung: vertraulich|streng` trägt.
  - Verteilung an alle Geräte: Plugin bzw. Managed Settings der Organisation, sonst kann jede Person den Hook abschalten.
  - **Grenze (Einschätzung, Sonnet 5.5, 2026-11-02):** Hooks prüfen Text. Bash-Umwege (Variablen, `cd`, Symlinks) fängt `sperre-pfade.sh` nicht sicher. Zuerst im Dateisystem/Rechtekonzept sperren, Hook als zweite Linie. Auf echten Geräten ungetestet; Ablehnungstests liegen nur als Skriptlauf vor.

## 3. Vor dem Rollout klären
- [ ] **Daten auf Endgeräten?** Personen-, Studierenden-, Vertragsdaten: entscheidet, ob Claude Code dort überhaupt laufen darf.
- [ ] **Laufwerke/Pfade:** welche sperren, wie (Rechte, `permissions.deny`, Hook `sperren.txt`)? Gilt auch für synchronisierte Ordner.
- [ ] **Datenklassifizierung:** hat die Firma eine? Dann Metadaten nutzen (Marker, Etikett), damit klassifizierte Dokumente für den Agenten unlesbar sind – wohl die sauberste Variante. Prüfen, ob ein Hook das leisten kann (Dateiattribute statt Kopfzeile).
- [ ] **Verhalten der Mitarbeitenden:** `skip-permissions` abschalten (Managed Settings, `disableBypassPermissionsMode` prüfen), Startverzeichnis (Claude Code im falschen Ordner = zu viele Rechte), Betriebsvereinbarung.
- [ ] **Unternehmensrichtlinien:** Managed Settings / Teams-Funktionen; Vergleich Pi Agent, OpenCode.
- [ ] **Rollen:** IT nutzt selbst Claude Code – Ausnahmen oder abgestufte Sperrlisten je Rolle?
- [ ] **Lücken-Leck:** enthält Kontext/Skill Infos aus Tools, die die Person dort nicht sehen darf? Mit kobench testen.
- [ ] **Personenbezogene Daten** in Entwürfen und Logbuch: Rechtsgrundlage, Information der Betroffenen, Löschfristen, Auftragsverarbeiter der genutzten KI-Dienste.
