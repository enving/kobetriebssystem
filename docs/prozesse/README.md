# Prozessentwurf für den OpenWebUI-Versuch

**Entwurf v0.2, GPT-6-astra, 11.11.2026. Zielumfang bestätigt; technische Umsetzung und Betrieb nicht freigegeben.**

[Interaktive Ansicht öffnen](ansicht.html). Drei Kapitel führen durch die acht Detailmodelle:

- **Auftrag bearbeiten:** gemeinsame Grundlagen laden, persönliche Tools nutzen, bei Bedarf einen
  begrenzten Terminalauftrag ausführen und das Ergebnis unabhängig prüfen (P00–P03).
- **Wissen verbessern:** Korrekturen passend einordnen, allgemeine Fähigkeiten vorschlagen und
  das gemeinsame Wiki mit Quellen und fachlichen Besitzern pflegen (P04/P05).
- **Betrieb prüfen:** freigegebene Routinen, Unterbrechungen und reproduzierbare Tests (P06/P07).

## Zielbild und offene Technik

Das Zielbild dieses Versuchs ist ein **gemeinsames Firmenwiki mit Regeln und Skills für alle**.
Bewusst festgelegte persönliche Ergänzungen bleiben getrennt. Vertrauliche Daten bleiben in den
Quellsystemen; notwendige Ergebnisse werden nur im zulässigen Empfängerkreis verarbeitet und abgelegt.
Der Kontextartikel von AI FIRST beschreibt ebenfalls ein Wiki für das gesamte Team und Rechtevergabe
in den angebundenen Tools. Geschützte Rollenpakete aus unserer [PRD L6](../../PRD.md#9-lückenregister)
sind eine weitergehende Anforderung; dieses einfachere Zielbild schließt die allgemeine Lücke nicht.

Gemeinsame Konfiguration bedeutet weder gemeinsamer Gesprächsverlauf noch gemeinsames Tool-Konto.
Ein Rollenprofil beschreibt die Arbeitsweise; die technische Zugriffskontrolle muss vor dem Lesen
oder Handeln greifen. Frontmatter, Dateinamen und Promptregeln allein erzwingen keine Lesesperre.

Zwei Anbindungen bleiben **gleichberechtigte Testvarianten**, keine bereits eingerichteten Wege:

| Variante | Übergabe | Noch nachzuweisen |
|---|---|---|
| A: Tools über OpenWebUI | Die Oberfläche nutzt das persönliche Tool-Konto. Der Worker erhält nur benötigte Daten. | Kontozuordnung, Daten- und Dateitrennung, begrenzte Übergabe |
| B: nutzergebundener Vermittler | Ein vertrauenswürdiger Dienst verbindet den Auftrag mit dem autorisierten Konto; UI und Worker können darüber Tools aufrufen. Composio ist ein möglicher Kandidat. | Authentifizierte Identität, begrenzter Zugriff, Ablehnung fremder Kennungen und Widerruf |

Das Sprachmodell darf keine Nutzerkennung als Berechtigungsnachweis wählen. Ein organisationsweiter
Admin-Schlüssel gehört nicht in die frei verwendbare Worker-Shell. Modellzugang und Tool-Konto sind
verschiedene Identitäten. Die tatsächliche Ausführungsidentität muss auch im Zielsystem geprüft werden.
Eine gültige OAuth-Verbindung kann wiederverwendet werden; eine neue Aufgabe bedeutet nicht automatisch
neue Registrierung. Ob das im Teststack durchgängig funktioniert, bleibt ungetestet.

Einfache Fragen sollen mit dem gemeinsamen Kern beantwortbar sein. Ein Worker wird für benötigte
Datei-/Coding-Arbeit oder ein gesondertes Pflegemandat beauftragt. Die konkrete Mandatsaufteilung bleibt
L25 zugeordnet. Ein frischer Prüflauf bleibt erforderlich; die Hauptunterhaltung wird durch das
Weiterleiten einer Worker-Antwort nicht zum unabhängigen Prüfer. Die bestehende Pi/Sandcastle-Auswahl
für den Änderungs-Prüfer wird hier nicht ersetzt.

## Modelle und eine zuständige Quelle

<!-- modelle:start -->
| Prozess | Quelle | Ansicht |
|---|---|---|
| P00 · Von der Aufgabe zur gemeinsamen Verbesserung | [BPMN](00-gesamtprozess.bpmn) | [Öffnen](ansicht.html#Process_P00) |
| P01 · Auftrag, Kontext und persönliche Tools | [BPMN](01-auftrag-und-tools.bpmn) | [Öffnen](ansicht.html#Process_P01) |
| P02 · Begrenzter Auftrag im Linux-Terminal | [BPMN](02-terminalauftrag.bpmn) | [Öffnen](ansicht.html#Process_P02) |
| P03 · Gegenprüfung und menschliche Entscheidung | [BPMN](03-pruefung-und-mensch.bpmn) | [Öffnen](ansicht.html#Process_P03) |
| P04 · Korrektur, Änderungsvorschlag und Verteilung | [BPMN](04-lernen-und-verteilen.bpmn) | [Öffnen](ansicht.html#Process_P04) |
| P05 · Wissen finden, anreichern und pflegen | [BPMN](05-kontextpflege.bpmn) | [Öffnen](ansicht.html#Process_P05) |
| P06 · Routine, Unterbrechung und Wiederaufnahme | [BPMN](06-routine-und-wiederaufnahme.bpmn) | [Öffnen](ansicht.html#Process_P06) |
| P07 · Reproduzierbarer Test mit fiktiver Firma | [BPMN](07-testbetrieb.bpmn) | [Öffnen](ansicht.html#Process_P07) |
<!-- modelle:ende -->

Die **acht `.bpmn`-Dateien sind die Quelle des Prozessmodells**, einschließlich Schrittdetails,
Kapitelzuordnung und offener Fragen. Der Bauweg erzeugt daraus die selbständige `ansicht.html` und
`pruefung.json`. Die Ansicht enthält alle SVGs und bietet einen Download je Diagramm. Damit stehen
hier 13 statt 21 Dateien; acht separate SVG-Kopien entfallen. Bestehende Exporte in Präsentationen
bleiben eigenständige Snapshots und werden nicht automatisch überschrieben.

BPMN-Bahnen zeigen fachliche Verantwortung, keine nachgewiesenen Container- oder Kontogrenzen.
Die Tool-Verbindung in P01 zeigt den fachlichen Aufruf; ihre technische Platzierung A/B ist offen.
Aufgerufene Aktivitäten verweisen über `calledElement` auf andere Prozessdateien. Alle Modelle tragen
`isExecutable="false"`. Blockierte Unterprozesse dürfen den Gesamtauftrag nicht als erfolgreich
fortsetzen; diese Rückgabestatus müsste eine spätere Laufsteuerung technisch verdrahten. Normale
BPMN-Endereignisse allein leisten das nicht. Zuverlässige Zustellung oder doppelfreie Wirkung ist
hier ebenso wenig nachgewiesen wie Nutzerisolation.

## Bearbeiten und erzeugen

Genutzt wird die vorhandene **Miragon bpmn-cli 0.10.0**
([Originalprojekt](https://github.com/Miragon/bpmn-cli)). Die tatsächlich verwendete Version steht im
Prüfbericht. Beispiel:

```sh
bpmn show docs/prozesse/02-terminalauftrag.bpmn P02_Vertrag
bpmn set docs/prozesse/02-terminalauftrag.bpmn P02_Vertrag name="Arbeitsauftrag und Mandat prüfen"
python3 docs/prozesse/rendern.py
```

Alternativ eine vorhandene CLI in einem ausdrücklich angegebenen Container verwenden:

```sh
python3 docs/prozesse/rendern.py --container <containername>
```

Für zusätzliche SVG-Dateien, etwa für eine Präsentation:

```sh
python3 docs/prozesse/rendern.py --svg-dir /tmp/ko-prozess-export
```

`--container` und `--svg-dir` sind kombinierbar. Ohne Exportoption entstehen keine separaten SVGs.
Das Skript installiert nichts, startet keine Agenten oder Dienste und nutzt `bpmn validate`,
`bpmn diagram` und `bpmn render`. Der Bericht bindet die eingebetteten SVGs, Vorlage und Ansicht an
ihre SHA-256-Prüfsummen. Struktur, erreichbare Enden und Prozessaufrufe werden zusätzlich geprüft.

## Was der Teststack noch beantworten muss

Die konkreten Gegenproben stehen in den bestehenden [OpenWebUI-Prüffällen](../../beispiel/openwebui/fixtures/04-test-cases.md):
Identität und Rechte (E/F/H), sinnvolle Delegation (A/H), frischer Prüfer (C), Lernen ohne private Daten
(G/K), Wiederaufnahme und Versionen (I/J). Zuerst modellfreie Proben, danach wenige echte Modellläufe.
Eine gelesene Codefunktion ist kein erfolgreicher Ende-zu-Ende-Test. Providerfehler werden getrennt
von fachlicher Qualität ausgewiesen. Die bestehenden [Prüfszenarien](../pruefszenarien.md) und das
[PRD-Lückenregister](../../PRD.md#9-lückenregister) bleiben zuständig; es entsteht kein zweites Register.

## Quellen und Geltung

Der Entwurf ersetzt keine Vorgaben aus [AGENTS.md](../../AGENTS.md),
[SICHERHEIT.md](../../SICHERHEIT.md), [Szenarien](../szenarien.md),
[Prüferkarte](../../agents/pruefer.md) oder [Paketverteilung](../../installation/README.md).
Die Herkunft steht an den Prozessschritten. Keine automatische Personenbeobachtung; persönliche
Festlegungen und firmenweites Lernen bleiben gemäß PRD Entscheidung 10 und Prüfszenario S17 getrennt.

Öffentliche Quellen: [AI-FIRST-Architektur](https://ai-first.ai/insights/ai-first-ki-betriebssystem-2-0),
[Kontextpflege](https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst),
[OpenWebUI-OAuth](https://docs.openwebui.com/features/extensibility/mcp/#connecting-an-account),
[OpenWebUI-Subagenten](https://docs.openwebui.com/features/chat-conversations/chat-features/subagents/) und
[Composio-Nutzerzuordnung](https://docs.composio.dev/docs/consumer-agents).
Die im Artikel beschriebene automatische Wiki-Übernahme führt keine neue lokale Freigaberegel ein.

## Prüfstand v0.2

Die aktuelle Struktur- und Layoutprüfung wird in `pruefung.json` erzeugt.
Geprüft am 11.11.2026: acht Modelle, 169 Knoten und 171 Sequenzflüsse; null CLI-Fehler und
Warnungen, keine verdeckten Elemente oder Labels. Alle 179 lokalen Quellenverweise sind auflösbar.
Die Ansicht wurde bei 728 Pixeln hell und 390 Pixeln dunkel geprüft: drei Kapitel, acht Modelle,
169 Schrittdetails, sechs Prozessaufrufe, Zoom und SVG-Download funktionieren ohne Seitenüberlauf.
Der optionale CLI-Export erzeugt acht SVGs mit den Prüfsummen aus dem Bericht und keine SVG-Kopien
im Quellordner. Python-/JavaScript-Syntax, `git diff --check` und Geheimnisscan bestehen.

Die Dokumentationsprüfung ist kein Integrationstest: keine echten Modellantworten, kein OAuth-Login,
keine Mehrnutzer-Abnahme und kein Deployment. Der Teststack wurde durch diese Überarbeitung nicht verändert.
