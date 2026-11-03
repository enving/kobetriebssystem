# kobetriebssystem – Vorlage

Blanke Vorlage für ein KI-Betriebssystem im Unternehmen. Ein Agent erledigt Aufgaben; vier Bausteine sagen ihm *wie* (Skills), *was* (Kontext), *womit* (Tools) und *was erlaubt ist* (Regeln); zwei Schleifen halten alles in Bewegung (Automatisierungen starten ohne Bitte, die Lernschleife macht das System mit jeder Korrektur besser). Alles Steuernde liegt als Textdatei in Git, jede Änderung ist ein Pull Request.

Diese Datei ist die **Navigation** – für Agenten und Menschen. Enthält bewusst keine Firmendaten und keine Beispiel-Skills, nur `_vorlage`-Dateien.

## Wer KI nur Texte schreiben lässt, verpasst das Eigentliche

### Das eigentliche Thema heißt Steuerung, nicht Prompten

Die meisten Beiträge über künstliche Intelligenz drehen sich um Werkzeuge: welche App, welches Modell, welcher Trick für bessere Ergebnisse. Das ist jedoch nur die Oberfläche. Wer KI dauerhaft in seinen Arbeitsalltag einbaut, stellt bald fest, dass sich nicht das Werkzeug verändert, sondern die eigene Position innerhalb der Arbeit.

Nach und nach wandert die Ausführung ab. Recherchieren, formulieren, gestalten, übertragen — das übernimmt zunehmend das System. Was bleibt, ist eine Aufgabe, die vorher kaum jemand ausdrücklich hatte: den Überblick zu behalten.

### Vom Handwerker zum Dirigenten

Ein Vergleich aus der Musik beschreibt das gut. Ein Dirigent spielt kein einziges Instrument. Dennoch entscheidet allein sein Einsatz darüber, ob ein Ensemble zusammenklingt oder jeder Musiker für sich spielt. Die Leistung liegt nicht im eigenen Ton, sondern im Tempo, in der Balance und darin, das Richtige zur richtigen Zeit zu verlangen.

Mit KI verschiebt sich die eigene Rolle in genau diese Richtung. Nicht mehr jede Motion selbst auszuführen, sondern Abläufe zu gliedern, Teilaufgaben zu vergeben, Qualitätsmaßstäbe festzulegen und am Ende zu bewerten, ob das Ergebnis den Ansprüchen genügt — das wird zur Kernkompetenz.

### Ein Beispiel aus dem Alltag: die Kundenpräsentation

Nehmen wir eine Aufgabe, die in vielen Berufen regelmäßig vorkommt: die Vorbereitung einer Präsentation für ein Kundengespräch. Auf den ersten Blick ist das eine einzige Tätigkeit. Bei näherem Hinsehen zerfällt sie in eine Kette ganz unterschiedlicher Schritte:

1. Ziel klären: Was soll das Gegenüber am Ende wissen, wofür entscheiden?
2. Material sammeln: Zahlen, Beispiele, Argumente, Einwände.
3. Dramaturgie festlegen: Reihenfolge, Kernerzählung, roter Faden.
4. Folien bauen: Text, Grafiken, Layout.
5. Qualitätskontrolle: fachlich korrekt? verständlich? auf Zielgruppe zugeschnitten?
6. Übergabe und Nachbereitung: Termin, Feedback, Anpassungen für die nächste Runde.

Wer diese Stationen nie benennt, dessen KI-Einsatz bleibt Zufall. Wer sie dagegen einmal aufgeschrieben hat, kann sie prüfen, sortieren und Schritt für Schritt aus der Hand geben — angefangen bei den Schritten, die am wenigsten Nachdenken verlangen.

### Fachwissen verliert keinen Wert — es wechselt den Einsatzort

Eine verbreitete Sorge lautet: Wenn die Maschine schreibt, wird das eigene Können überflüssig. Das Gegenteil trifft zu. Das Wissen wird knapper und wertvoller, aber es wird an einer anderen Stelle gebraucht — nicht mehr bei der Erzeugung, sondern bei der Bewertung und beim Aufbau des Systems.

Wer gut ist, weiß Antworten auf Fragen dieser Art:

- Wonach beurteilt man, ob eine Recherche vollständig ist?
- Woraus ergibt sich, dass eine Argumentation trägt?
- Welche Fehler entlarven einen Text als austauschbar?
- Wo verläuft die Grenze zwischen kreativem Spielraum und fachlicher Genauigkeit?

Ein System kann nur so gut arbeiten, wie die Person, die es einrichtet, diese Fragen beantworten kann. Automatisierung setzt Urteilsvermögen voraus, sie ersetzt es nicht.

### Erst kartieren, dann automatisieren

Bevor irgendetwas an eine KI übergeben wird, lohnt ein Schritt, der völlig ohne Technik auskommt: die Aufgabe einmal in Ruhe beschreiben. Fünf Fragen genügen:

- Was liegt vor, wenn die Aufgabe beginnt — und wie sieht das fertige Ergebnis konkret aus?
- Durch welche Stationen läuft die Arbeit dazwischen?
- An welchen Punkten wird entschieden, und wer entscheidet?
- Welche Stationen sind reine Routine, welche verlangen Erfahrung?
- Wohin fließt das Ergebnis, und was passiert danach damit?

Das kostet zunächst Zeit und liefert keine sichtbaren Resultate. Es verhindert aber den häufigsten Fehler beim Arbeiten mit KI: viele begonnene, halb fertige und nicht abgestimmte Versuche, deren Verwaltung am Ende mehr Aufwand verursacht als die ursprüngliche Aufgabe selbst.

### Der erste Schritt ist klein

Für den Einstieg genügt eine einzige Übung: eine wiederkehrende Aufgabe auswählen — und nur ihre Stationen auflisten. Nichts automatisieren, nichts optimieren. Wer die Liste einmal vor sich hat, sieht meist sofort, wo sich ein erster, risikofreier Einsatz lohnt: dort, wo die Arbeit gleichförmig ist und das Urteilsvermögen nicht beansprucht wird.

Der Gewinn entsteht selten am ersten Tag. Er entsteht, wenn aus einzelnen Werkstücken allmählich ein System wird, das auch ohne ständige Anleitung läuft.

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
Anleitung: [Hooks erstellen und verlässlich prüfen](docs/hooks-erstellen.md).

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
