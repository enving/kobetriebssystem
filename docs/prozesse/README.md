# Prozessentwurf für den OpenWebUI-Versuch

**Entwurf v0.1, GPT-6.1-sol, 11.11.2026. Keine Betriebs- oder Architekturfreigabe.**

[Interaktive Ansicht öffnen](ansicht.html). Dort lassen sich die acht Prozesse auswählen,
vergrößern und über ihre Schritte lesen. Die BPMN-Dateien sind auch in einem BPMN-Modeler bearbeitbar.

<!-- modelle:start -->
| Prozess | Quelle | Bild |
|---|---|---|
| P00 · Von der Aufgabe zur gemeinsamen Verbesserung | [BPMN](00-gesamtprozess.bpmn) | [SVG](00-gesamtprozess.svg) |
| P01 · Auftrag, Kontext und persönliche Tools | [BPMN](01-auftrag-und-tools.bpmn) | [SVG](01-auftrag-und-tools.svg) |
| P02 · Begrenzter Auftrag im Linux-Terminal | [BPMN](02-terminalauftrag.bpmn) | [SVG](02-terminalauftrag.svg) |
| P03 · Gegenprüfung und menschliche Entscheidung | [BPMN](03-pruefung-und-mensch.bpmn) | [SVG](03-pruefung-und-mensch.svg) |
| P04 · Korrektur, Änderungsvorschlag und Verteilung | [BPMN](04-lernen-und-verteilen.bpmn) | [SVG](04-lernen-und-verteilen.svg) |
| P05 · Wissen finden, anreichern und pflegen | [BPMN](05-kontextpflege.bpmn) | [SVG](05-kontextpflege.svg) |
| P06 · Routine, Unterbrechung und Wiederaufnahme | [BPMN](06-routine-und-wiederaufnahme.bpmn) | [SVG](06-routine-und-wiederaufnahme.svg) |
| P07 · Reproduzierbarer Test mit fiktiver Firma | [BPMN](07-testbetrieb.bpmn) | [SVG](07-testbetrieb.svg) |
<!-- modelle:ende -->

Die **`.bpmn`-Dateien sind die Quelle des Prozessmodells**. SVGs, die HTML-Ansicht und
`pruefung.json` sind daraus erzeugt. Namen, Schrittdetails, Aufrufe und offene Punkte der Ansicht
werden aus BPMN gelesen; sie sind kein zweiter gepflegter Prozessbestand.

Die Übersicht P00 führt in die Details P01–P07: Auftrag und persönliche Tools, Terminalauftrag,
Gegenprüfung, Lernschleife und Verteilung, Kontextpflege, Routinen sowie reproduzierbarer Testbetrieb.
Annahmen und noch nötige Entscheidungen stehen in der Prozessdokumentation, besonders zur
Codex-Rolle, zur Nutzertrennung und zu den Rechten des Prüfers. Die bestehenden Lücken werden
weiter ausschließlich in [PRD §9](../../PRD.md#9-lückenregister) geführt.

## Quellen und Abgrenzung

Das Modell konkretisiert den aktuellen Gesprächsentwurf für einen OpenWebUI-Adapter. Es ersetzt
keine Vorgaben aus [AGENTS.md](../../AGENTS.md), [SICHERHEIT.md](../../SICHERHEIT.md),
[Szenarien](../szenarien.md), [Prüfszenarien](../pruefszenarien.md),
[Prüferkarte](../../agents/pruefer.md) oder [Paketverteilung](../../installation/README.md).
Die Herkunft steht zusätzlich an jedem Prozessschritt. Es enthält nur verallgemeinerte Abläufe.

Öffentliche Ausgangsquellen: [AI-FIRST-Architektur vom 01.11.](https://ai-first.ai/insights/ai-first-ki-betriebssystem-2-0),
[Kontextpflege vom 08.11.](https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst),
[OpenWebUI-OAuth](https://docs.openwebui.com/features/extensibility/mcp/#connecting-an-account) und
[OpenWebUI-Subagenten](https://docs.openwebui.com/features/chat-conversations/chat-features/subagents/).
Die dort teilweise beschriebene automatische Wiki-Übernahme wird nicht als lokale Freigaberegel eingeführt.

Bahnen zeigen **fachliche Verantwortung**. Eine Bahn ist kein eigener Container und kein Nachweis
für Zugriffsrechte. P01 zeigt die direkten persönlichen Tools als eigenen Pool; sein Nachrichtenfluss
führt nicht durch Codex. P02 beschreibt den gesonderten Ausführungsauftrag. Aufgerufene Aktivitäten
verweisen über `calledElement` auf die Prozesskennungen der anderen Dateien. Das sind dokumentarische
Verknüpfungen, keine konfigurierte Workflow-Engine. Alle Prozesse tragen `isExecutable="false"`.

P00 behandelt nur die erfolgreiche Rückkehr eines Unterprozesses als Fortsetzung: Ein blockierendes
oder abbrechendes Ende in einem Detailprozess stoppt den betreffenden Auftrag und meldet seinen Status.
Bei einer späteren ausführbaren Umsetzung sind diese Rückgabestatus technisch zu verdrahten; allein
ein normales BPMN-Endereignis in einer aufgerufenen Datei erzwingt das nicht. Die Modelle behaupten
weder technische Isolation noch zuverlässige Zustellung, frischen Prüferkontext oder doppelfreie Wirkung.
Providerfehler werden als technische Blocker getrennt von fachlicher Qualität ausgewiesen.

## Bearbeiten und erneut erzeugen

Genutzt wurde **Miragon bpmn-cli 0.10.0** aus dem vorhandenen Teststack
([Originalprojekt und CLI-Dokumentation](https://github.com/Miragon/bpmn-cli)).
Die tatsächlich verwendete Version wird in `pruefung.json` festgehalten. Für die Befehle unten
eine vorhandene CLI verwenden; lokale Hilfe: `bpmn guide`.

Beispiel einer Änderung direkt an der Quelle:

```sh
bpmn show docs/prozesse/02-terminalauftrag.bpmn P02_Vertrag
bpmn set docs/prozesse/02-terminalauftrag.bpmn P02_Vertrag name="Arbeitsauftrag und Mandat prüfen"
bpmn layout docs/prozesse/02-terminalauftrag.bpmn
python3 docs/prozesse/rendern.py
```

Alternativ eine bereits vorhandene CLI in einem angegebenen Container verwenden:

```sh
python3 docs/prozesse/rendern.py --container <containername>
```

Das Skript installiert nichts und startet keine Agenten oder Dienste. Es verwendet nur temporäre
Dateien, `bpmn validate`, `bpmn diagram` und `bpmn render`. Der Prüfbericht bindet jedes SVG und die
Ansicht an den SHA-256 der BPMN-Quelle. Zusätzliche Prüfungen kontrollieren unter anderem erreichbare
Enden, beschriftete Verzweigungen, dokumentierte Schritte und auflösbare Prozessaufrufe.
Geprüft wird das Modell, nicht die Funktionsfähigkeit der entworfenen Integration.

## Prüfstand 11.11.2026

Alle acht Modelle bestehen die CLI-Strukturprüfung ohne Fehler oder Warnungen. Die zusätzlichen
Graphprüfungen und 179 lokale Quellenverweise bestehen ebenfalls. Kein Element oder Label überlappt
ein anderes oder wird von einer Kante verdeckt. Verbleibende Kantenkreuzungen stehen getrennt im
Layoutbericht; eine Kreuzung ist keine Zusammenführung des Ablaufs.

Die Ansicht wurde mit 728 Pixeln Breite im hellen und 390 Pixeln im dunklen Erscheinungsbild geprüft:
acht Prozesse auswählbar, alle 169 Schrittdokumentationen erreichbar, sechs Detailprozess-Aufrufe
auflösbar, Zoom und Navigation funktionsfähig, kein horizontaler Seitenüberlauf. Die Begleittexte
verwenden mindestens 14 Pixel; das BPMN-Bild ist gesondert zoombar.

Die Prüfung war eine eigene Modell- und Darstellungsprüfung. Kein echter Mehrnutzerlauf, keine
Modellantwort, keine Connector-Anmeldung und kein Deployment wurden damit getestet.
