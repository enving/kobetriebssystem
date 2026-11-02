# kobetriebssystem – Vorlage

Blanke Vorlage für ein KI-Betriebssystem im Unternehmen. Ein Agent erledigt Aufgaben; vier Bausteine sagen ihm *wie* (Skills), *was* (Kontext), *womit* (Tools) und *was erlaubt ist* (Regeln); zwei Schleifen halten alles in Bewegung (Automatisierungen starten ohne Bitte, die Lernschleife macht das System mit jeder Korrektur besser). Alles Steuernde liegt als Textdatei in Git, jede Änderung ist ein Pull Request.

Diese Datei ist die **Navigation** – für Agenten und Menschen. Enthält bewusst keine Firmendaten und keine Beispiel-Skills, nur `_vorlage`-Dateien.

## Für Agenten: Lesereihenfolge
1. **Beim Start nur:** `AGENTS.md` → `kontext/index.md` → `kontext/landkarte.md` → `persoenlich/<ich>/anweisungen.md`.
2. **Danach bei Bedarf:** passenden Skill wählen (Beschreibung im Kopf der `SKILL.md`), dessen `nutzt_kontext`-Dateien lesen, Landkarte für Systeme außerhalb des Repos.
3. **Nie** alles lesen. Je weniger am Anfang geladen wird, desto besser bleibt der Agent bei der Aufgabe.

## Wie eine Aufgabe läuft
Auslöser (Bitte im Chat, Zeitplan oder Ereignis) → Agent erkennt die Aufgabe → zieht Skill, Kontext, Regeln, Tools → Prüf-Agent prüft gegen die Kriterien des Skills → Ergebnis liegt als **Entwurf** bereit oder der Agent stellt die eine Frage, die er nicht selbst entscheiden darf → Mensch prüft, ändert, sendet selbst → jede Änderung des Menschen startet die Lernschleife.

## Wegweiser: wozu was dient

### Steuerung (Wurzel)
| Datei | Zweck | Wer ändert |
|---|---|---|
| `AGENTS.md` | Grundregeln für jeden Agenten: Verhalten, Ampel, Lernschleife | nur Mensch, per PR |
| `CLAUDE.md` | Wegweiser für das primäre Modell; verweist auf `AGENTS.md` (andere Modelle: gleiche Datei unter eigenem Namen) | Mensch |
| `SICHERHEIT.md` | Technische Sperren, Datenschutz, Checkliste vor dem Rollout | Mensch |
| `Übergabe.md` | Stand, offene Fragen, nächste Schritte der Vorlage selbst | wer an der Vorlage arbeitet |
| `index.md` | Tabellen-Überblick über alle Ordner | bei Strukturänderung |

### Skills – *wie wir arbeiten* (`.agents/skills/`)
Ein Ordner je wiederkehrender Aufgabe: `SKILL.md` (Auslöser, Ergebnis, „Fertig heißt …“, Stolperfallen) und `evals/` (Prüffälle: Normalfall, fehlende Info, Grenzfall; Ergebnisse je Testlauf). Ein Skill beschreibt Ziel und Kriterien, nicht Schritte, und verweist auf Kontextdateien statt Preise oder Regeln zu kopieren. Neuer Skill: `_vorlage/` kopieren. Erst wenn alle Prüffälle bestanden sind, darf er als Automatisierung laufen. Jede Korrektur wird ein neuer Prüffall.

### Kontext – *was wir wissen* (`kontext/`)
Wiki für Dauerhaftes (Angebot, Prozesse, Stimme). Ein Ordner je Arbeitsgebiet mit einem Besitzer. Regeln je Datei: eine Aussage = eine Quelle, ein Prüfdatum, nur was *jetzt* gilt. Der Agent pflegt ein, Menschen sagen ihm, was gilt.
- `index.md` – Verzeichnis (eine Zeile je Bereich/Datei), zuerst lesen.
- `landkarte.md` – *wo Daten außerhalb des Repos liegen* und was der Agent dort nie tun darf. Laufende Arbeit (Mails, Kunden, Projekte) bleibt in den Tools und wird live mit den Rechten der Person gelesen.
- `glossar/` – kontrolliertes Vokabular: neue Begriffe per PR, von Agenten und Menschen geschärft.
- `_vorlage-bereich/_vorlage.md` – Dateivorlage; `log.md` – Änderungslog.

### Automatisierungen – *ohne uns* (`automatisierungen/`)
Ein Auftrag je Routine als Textdatei: Auslöser, Skill, erlaubte Quellen, Ergebnisort, „Nie“. `takt.md` ist der Taktplan. Eingeschaltet wird erst nach sauberen Testläufen und Freigabe des Verantwortlichen. Vorher den Prozess oft genug selbst mit KI durchlaufen, sonst entsteht automatisiert Ausschuss. Rückfragen kommen per Chat an die Person.

### Regeln – *was erlaubt ist*
`AGENTS.md` (Ampel, Security by Instruction) und `system/` (Security by Design). Rot gilt immer, gelb nach Rückfrage, grün selbst.

### Tools – *womit*
Keine Ordner im Repo. Tools hängen über Konnektoren an der Person; Rechte werden nur im Tool vergeben. Was der Agent dort darf/nie darf: `kontext/landkarte.md`. Alles Nach-außen-Gehende bereitet der Agent nur vor.

### Persönliche Ebene (`persoenlich/`) und Prompts (`prompts/`)
- `persoenlich/_vorlage/` – Anweisungen (Rolle, Ziele, Stil) und Logbuch einer Person. Gehört der Person; fließt nur per PR ins zentrale Wissen zurück.
- `prompts/` – gemeinsame Prompt-Bibliothek, rollenbasiert verteilt.

### Plattform (`installation/`, `plugins/`, `system/`)
- `installation/` – wie dieses Betriebssystem selbst als Plugin gebaut, per GitHub Actions geprüft und an alle Geräte verteilt und aktualisiert wird (Rollen, Managed Settings).
- `plugins/` – externe, zusätzliche Plugins für die Agenten-App (Konnektoren u. Ä.), die das Betriebssystem ergänzen.
- `system/` – Prüfprogramme und Sperren: `sperren.txt` (Pfad-Sperrliste), `hooks/` (Senden stoppen, Pfade/klassifizierte Dateien sperren, Beispielkonfiguration).

### Doku (`docs/`)
`anmerkungen.md` (Anmerkungen → Umsetzung), `recherche.md`, `szenarien.md` (lokal vs. zentral), `beobachtungen.md`.

## Lernschleife in einem Satz
Der Agent selbst lernt nichts; besser werden die Dateien, die er liest. Korrektur einordnen (einmalig oder Regel) → bei Regel Vorschlag mit Ort, Wortlaut, Prüffall → Ja vom Menschen → PR. Nichts ändert sich still.

## Wer darf was
| | lesen | ändern |
|---|---|---|
| Agent | im Rahmen der Person | nur per PR-Vorschlag; Kontext nach Anweisung der Besitzer |
| Besitzer eines Bereichs | ja | entscheidet, was gilt |
| Ampel, Sperren, Grundregeln | alle | nur ein Mensch |

## Status
Entwurf. Nächste Schritte und offene Fragen: [Übergabe.md](Übergabe.md).

## Lizenz und Mitmachen
Mozilla Public License 2.0 (`LICENSE`). Verbesserungen, die nicht firmenspezifisch sind, bitte als Pull Request zurückgeben – Details in `CONTRIBUTING.md`.
