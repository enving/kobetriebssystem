# Prozesse – Markdown-Lesefassung

Automatisch aus den `.bpmn`-Quellen erzeugt durch `rendern.py`.
Dies ist eine Lesefassung des nicht ausführbaren Entwurfs, keine zusätzliche Regelquelle.
Änderungen gehören in BPMN; der nächste Bau aktualisiert diese Datei mit.

[Interaktive Ansicht](ansicht.html) · [Einordnung und Bauweg](README.md)

Die Abschnittsreihenfolge ist keine Ausführungsreihenfolge. Die Übergänge, Verzweigungen
und angehängten Ereignisse bestimmen den modellierten Ablauf. Offene Punkte bleiben offen.

## Verzeichnis

- [P00 · Von der Aufgabe zur gemeinsamen Verbesserung](#p00)
- [P01 · Auftrag, Kontext und persönliche Tools](#p01)
- [P02 · Begrenzter Auftrag im Linux-Terminal](#p02)
- [P03 · Gegenprüfung und menschliche Entscheidung](#p03)
- [P04 · Korrektur, Änderungsvorschlag und Verteilung](#p04)
- [P05 · Wissen finden, anreichern und pflegen](#p05)
- [P06 · Routine, Unterbrechung und Wiederaufnahme](#p06)
- [P07 · Reproduzierbarer Test mit fiktiver Firma](#p07)

## P00

P00 · Von der Aufgabe zur gemeinsamen Verbesserung

Quelle: [00-gesamtprozess.bpmn](00-gesamtprozess.bpmn) · SHA-256: `b3456fa2df166ea299acf61ca5ce7da5a00d3517b093d6e0ae71ed5597e1980e`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Überblick über den Arbeitskreislauf; die aufgerufenen P01–P07 enthalten die Details.
Offen: Tool-Anbindung A/B, Mandat und Isolation des Workers, Träger des frischen Prüflaufs. Zielbild bestätigt; Umsetzung ungetestet.
Quellen: ../szenarien.md ; ../../AGENTS.md ; ../../installation/README.md ; https://ai-first.ai/insights/ai-first-ki-betriebssystem-2-0
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Auftrag bearbeiten
Kurz: Überblick
Zielbild: Gemeinsames Firmenwiki, Regeln und Skills für alle. Persönliche Ergänzungen getrennt; vertrauliche Daten bleiben in den Quellsystemen.
Anbindung: A: persönliche Tools über OpenWebUI. B: nutzergebundener Vermittler für Tool-Aufrufe. Beide Wege sind zu testen; keiner ist bereits ausgewählt.
Grundsatz: Gemeinsam ist die Arbeitsgrundlage, nicht das Tool-Konto oder der Gesprächsverlauf. Identität und Rechte werden außerhalb des Sprachmodells durchgesetzt.

### Schritte und Entscheidungen

#### P00_Start

**Aufgabe liegt vor**

Verantwortung: Mitarbeitende · BPMN-Typ: `startEvent`

Eine Person fragt im Chat. Freigegebene Routinen sind ein zweiter Einstieg nach P06.
Quelle: ../szenarien.md

#### P00_Auftrag

**P01 · Auftrag, Kontext und persönliche Tools**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `callActivity`

Identität und Paketstand binden, benötigte Quellen auswählen, nur im zulässigen Konto lesen. Abbruchfälle bleiben in P01.
Quelle: ../szenarien.md

Aufgerufener Prozess: [P01](#p01).

#### P00_TerminalNoetig

**Terminal-Arbeit nötig?**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `exclusiveGateway`

Ein direkter Tool-Aufruf oder eine belegte Antwort braucht nicht automatisch einen Terminalauftrag.
Quelle: ../szenarien.md

#### P00_Vorbereitet

**Vorbereitung erfolgreich?**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `exclusiveGateway`

Ein blockierendes Ende von P01 darf nicht als vollständiger Arbeitsauftrag an Codex oder den Prüfer weiterlaufen.
Quelle: ../../AGENTS.md

#### P00_Terminal

**P02 · Begrenzten Terminalauftrag bearbeiten**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `callActivity`

Nur mit freigegebenem Mandat und belegter Isolation. Ein blockierter Aufruf liefert einen Status, keinen erfundenen Erfolg.
Quelle: ../../PRD.md

Aufgerufener Prozess: [P02](#p02).

#### P00_Ergebnis

**Zusammenführung**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `exclusiveGateway`

Zusammenführung der Alternativen: Ergebnis ohne Terminal oder Ergebnis eines Terminalauftrags.
Quelle: ../szenarien.md

#### P00_Ausgefuehrt

**Terminal-Ergebnis vorhanden?**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `exclusiveGateway`

BLOCKIERT oder ABBRUCH aus P02 beendet diesen Durchlauf. Nur ein auswertbares Ergebnis geht zur Gegenprüfung.
Quelle: ../../AGENTS.md

#### P00_Pruefen

**P03 · Ergebnis prüfen und vorlegen**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `callActivity`

Gegenprüfung mit zulässigen Quellen und menschliche Entscheidung; Rückgabe enthält ANGENOMMEN, KORREKTUR, OFFEN oder ABBRUCH.
Quelle: ../../agents/pruefer.md

Aufgerufener Prozess: [P03](#p03).

#### P00_Status

**Wie endet der Auftrag?**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `exclusiveGateway`

Der Prüflauf ist keine automatische Versandfreigabe. Offene und abgebrochene Aufträge bleiben als solche sichtbar.
Quelle: ../../AGENTS.md

#### P00_EndeOffen

**Offen oder abgebrochen**

Verantwortung: Mitarbeitende · BPMN-Typ: `endEvent`

Kein fachlich fertiges Ergebnis behaupten; konkreten Blocker und bisherigen Stand nennen.
Quelle: ../../AGENTS.md

#### P00_Korrektur

**P04 · Korrektur passend einordnen**

Verantwortung: Firmenbetrieb / zuständige Quelle · BPMN-Typ: `callActivity`

Nur bei einer bestätigten Korrektur. Persönliches bleibt persönlich; gemeinsame Änderungen gehen über Vorschlag, Prüfung und zulässige Freigabe.
Quelle: ../../AGENTS.md

Aufgerufener Prozess: [P04](#p04).

#### P00_Ende

**Ergebnis und Stand nachvollziehbar**

Verantwortung: Mitarbeitende · BPMN-Typ: `endEvent`

Die Person hat das Ergebnis angenommen oder ihre Korrektur wurde eingeordnet. Gemeinsamer Paketstand ändert sich ausschließlich im Freigabeprozess.
Quelle: ../../AGENTS.md

#### P00_Fortsetzen

**Weiterbearbeitung im Mandat?**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `exclusiveGateway`

Eine Korrektur kann eine begrenzte Überarbeitung auslösen. Quellen, Rechte und verbleibende Laufgrenzen erneut prüfen. Andernfalls ist nur die Korrektur eingeordnet.
Quelle: ../../AGENTS.md

#### P00_Join_Auftrag

**Zusammenführung**

Verantwortung: OpenWebUI / persönlicher Arbeitsagent · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

#### P00_Join_EndeOffen

**Zusammenführung**

Verantwortung: Mitarbeitende · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

#### P00_Join_Ende

**Zusammenführung**

Verantwortung: Mitarbeitende · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P00_Flow_Start_Auftrag` | `P00_Start` | `P00_Join_Auftrag` | — |
| `P00_Flow_Auftrag_Vorbereitet` | `P00_Auftrag` | `P00_Vorbereitet` | — |
| `P00_Flow_TerminalNoetig_Terminal` | `P00_TerminalNoetig` | `P00_Terminal` | ja |
| `P00_Flow_TerminalNoetig_Ergebnis` | `P00_TerminalNoetig` | `P00_Ergebnis` | nein |
| `P00_Flow_Vorbereitet_TerminalNoetig` | `P00_Vorbereitet` | `P00_TerminalNoetig` | ja |
| `P00_Flow_Vorbereitet_EndeOffen` | `P00_Vorbereitet` | `P00_Join_EndeOffen` | nein / blockiert |
| `P00_Flow_Terminal_Ausgefuehrt` | `P00_Terminal` | `P00_Ausgefuehrt` | — |
| `P00_Flow_Ergebnis_Pruefen` | `P00_Ergebnis` | `P00_Pruefen` | — |
| `P00_Flow_Ausgefuehrt_Ergebnis` | `P00_Ausgefuehrt` | `P00_Ergebnis` | ja |
| `P00_Flow_Ausgefuehrt_EndeOffen` | `P00_Ausgefuehrt` | `P00_Join_EndeOffen` | nein / abgebrochen |
| `P00_Flow_Pruefen_Status` | `P00_Pruefen` | `P00_Status` | — |
| `P00_Flow_Status_EndeOffen` | `P00_Status` | `P00_Join_EndeOffen` | OFFEN / BLOCKIERT / ABBRUCH |
| `P00_Flow_Status_Korrektur` | `P00_Status` | `P00_Korrektur` | Korrektur bestätigt |
| `P00_Flow_Status_Ende` | `P00_Status` | `P00_Join_Ende` | angenommen |
| `P00_Flow_Korrektur_Fortsetzen` | `P00_Korrektur` | `P00_Fortsetzen` | — |
| `P00_Flow_Fortsetzen_Auftrag` | `P00_Fortsetzen` | `P00_Join_Auftrag` | ja |
| `P00_Flow_Fortsetzen_Ende` | `P00_Fortsetzen` | `P00_Join_Ende` | nein |
| `P00_Flow_Join_Auftrag_Auftrag` | `P00_Join_Auftrag` | `P00_Auftrag` | — |
| `P00_Flow_Join_EndeOffen_EndeOffen` | `P00_Join_EndeOffen` | `P00_EndeOffen` | — |
| `P00_Flow_Join_Ende_Ende` | `P00_Join_Ende` | `P00_Ende` | — |

### Modellhinweis P00_Querschnitt

P05 Kontextpflege · P06 Routinen · P07 Testbetrieb
Eigene Detailprozesse, keine eingeschalteten Dienste.

## P01

P01 · Auftrag, Kontext und persönliche Tools

Quelle: [01-auftrag-und-tools.bpmn](01-auftrag-und-tools.bpmn) · SHA-256: `09650f1d2f436e88441072a36d8f0464e451016356cc8271ab3dbf814da5f68f`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Den Auftrag einer eindeutig angemeldeten Person mit passenden Quellen und einem festen Quellstand vorbereiten.
Offen: Anbindung A (OpenWebUI) oder B (Vermittler), nachgewiesene Nutzer-/Kontozuordnung. Gemeinsames Wiki ist Zielbild; PRD L6 bleibt als weitergehende Frage bestehen.
Quellen: ../../AGENTS.md ; ../szenarien.md ; https://docs.openwebui.com/features/extensibility/mcp/#connecting-an-account ; https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst ; ../../beispiel/openwebui/fixtures/04-test-cases.md
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Auftrag bearbeiten
Kurz: Auftrag & Tools

### Schritte und Entscheidungen

#### P01_Start

**Bitte eingegangen**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `startEvent`

Die Nutzernachricht ist der Auftrag. Eingebettete Anweisungen aus Dokumenten werden als Daten behandelt.
Quelle: ../../AGENTS.md

#### P01_Identitaet

**Nutzer und Auftrag sicher zuordnen**

Verantwortung: Adapter / Anmeldung / Rechteprüfung · BPMN-Typ: `serviceTask`

Die serverseitig authentifizierte Sitzung bestimmt die Person und bindet den Auftrag. Nutzer-ID aus Prompt oder Toolargument ist kein Nachweis. Rollenprofile steuern die Arbeitsweise; Tool-Rechte werden gesondert technisch geprüft. Keine Kontoauswahl durch das Modell.
Quelle: ../../SICHERHEIT.md

#### P01_Paket

**Freigegebenen Paketstand binden**

Verantwortung: Adapter / Anmeldung / Rechteprüfung · BPMN-Typ: `serviceTask`

Für alle derselbe freigegebene Firmenkern: Wiki, Regeln und gemeinsame Skills. Bewusst festgelegte persönliche Ergänzungen bleiben getrennt. Quellversion an den Auftrag binden; fehlende Pflichtquellen melden. Rollenbezogene Auswahl nach Relevanz ist keine Lesesperre. Gefilterte Wiki-Pakete aus PRD L6 sind eine spätere Erweiterung, kein Bestandteil dieses Zielbilds.
Quelle: ../../installation/README.md

#### P01_Gueltig

**Startgrundlage gültig?**

Verantwortung: Adapter / Anmeldung / Rechteprüfung · BPMN-Typ: `exclusiveGateway`

Start ohne zuordenbare Identität oder erforderliche Quellen ist kein gültiger Firmenauftrag.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P01_Stop

**Start blockiert**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `endEvent`

Fehlende Anmeldung, Quelle oder Version benennen. Kein Zugriff über ein anderes Konto.
Quelle: ../../AGENTS.md

#### P01_Aufgabe

**Ziel und Fertigkriterien klären**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `serviceTask`

Passenden Skill nach Beschreibung wählen. Erwartetes Ergebnis, erlaubten Zielkreis und nötige Quellen erkennen.
Quelle: ../szenarien.md

#### P01_Klar

**Auftrag hinreichend klar?**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `exclusiveGateway`

Fachliche Lücken und unklare Freigaben werden nicht durch Annahmen ersetzt.
Quelle: ../../AGENTS.md

#### P01_Rueckfrage

**Gezielte Rückfrage beantworten**

Verantwortung: Mitarbeitende · BPMN-Typ: `userTask`

Die Person klärt die eine entscheidende offene Angabe oder bricht ab. Der neue Auftrag bleibt an ihre Sitzung gebunden.
Quelle: ../../AGENTS.md

#### P01_Index

**Index und Quellenverweise lesen**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `serviceTask`

Das gemeinsame Wiki ist im Zielbild für das ganze Team lesbar. Index und Verweise erschließen dauerhaftes Arbeitswissen; persönliche Ergänzungen werden nur im jeweiligen Auftrag genutzt. Vertrauliche Live-Daten bleiben in den Quellsystemen und werden nicht als Wiki-Dateien mit Frontmatter-Sperre verteilt.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P01_ToolNoetig

**Live-Quelle nötig?**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `exclusiveGateway`

Mails und laufende Vorgänge bleiben im Quellsystem. Statisches Firmenwissen bleibt in der zuständigen Quelle.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P01_Konto

**Eigenes Tool-Konto und Umfang prüfen**

Verantwortung: Adapter / Anmeldung / Rechteprüfung · BPMN-Typ: `serviceTask`

Vor dem Aufruf die authentifizierte Person ihrem autorisierten Tool-Konto zuordnen. Eine bestehende gültige OAuth-Verbindung kann wiederverwendet werden; bei fehlender oder widerrufener Verbindung muss die Person neu autorisieren. Der Modellzugang ist nicht das Tool-Konto. Ausführung mit delegiertem Nutzerzugriff oder ausdrücklich zulässigem Dienstkonto im Test unterscheiden.
Quelle: https://docs.openwebui.com/features/extensibility/mcp/#connecting-an-account

#### P01_Zugriff

**Zugriff erlaubt?**

Verantwortung: Adapter / Anmeldung / Rechteprüfung · BPMN-Typ: `exclusiveGateway`

Connector beziehungsweise Vermittler und Quellsystem setzen Rechte durch. Nicht nur Tool-Auswahl verstecken: direkte unzulässige Aufrufe, fremde Konto-ID und widerrufene Rechte müssen scheitern. Eine allgemeine Anmeldekennung oder ein Rollenname reicht nicht.
Quelle: ../../SICHERHEIT.md

#### P01_Fehlt

**Zugriff fehlt: offen melden**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `endEvent`

Benennen, welche Quelle nicht gelesen werden konnte, ohne deren gesperrten Inhalt offenzulegen.
Quelle: ../../AGENTS.md

#### P01_Lesen

**Quelle nutzergebunden lesen**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `serviceTask`

Offene Anschlussvarianten: A — OpenWebUI ruft das persönliche Tool auf. B — ein vertrauenswürdiger Vermittler bindet den Tool-Aufruf an den authentifizierten Nutzer und dessen Konto. Der fachliche Datenfluss ist gleich; noch keine Variante ausgewählt oder abgenommen. Composio ist ein möglicher Vermittler, keine Wissensquelle. Nur erforderliche Daten lesen, keine Zugangsdaten an das Modell weitergeben.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P01_Toolfehler

**Tool-Aufruf gescheitert**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `boundaryEvent`

Toolfehler als technischen Blocker zurückgeben, nicht als fehlende Information erfinden. Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

Angehängt an: `P01_Lesen` · unterbricht Aktivität: ja.

Ereignis: `errorEventDefinition` · errorRef=error_toolAufrufGescheitert.

#### P01_Blockiert

**Toolfehler: blockiert**

Verantwortung: Adapter / Anmeldung / Rechteprüfung · BPMN-Typ: `endEvent`

Technischen Blocker an P00 zurückgeben. Keine andere persönliche Verbindung als Umweg verwenden.
Quelle: ../../SICHERHEIT.md

#### P01_Belege

**Belege und Sichtbarkeit festhalten**

Verantwortung: Adapter / Anmeldung / Rechteprüfung · BPMN-Typ: `serviceTask`

Quelle, abgerufener Stand und zulässiger Empfängerkreis begleiten das Ergebnis. Ein abgeleitetes Ergebnis wird nicht automatisch firmenöffentlich.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P01_Zusammen

**Zusammenführung**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `exclusiveGateway`

Quellen aus Wiki und optionalem Live-Aufruf werden für genau diesen Auftrag zusammengestellt.
Quelle: ../szenarien.md

#### P01_PaketAuftrag

**Ergebnis oder Arbeitsauftrag vorbereiten**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `serviceTask`

Einfache Fragen mit dem gemeinsamen Kern und zulässigen Quellen beantworten. Terminal nur für benötigte Datei-/Coding-Arbeit oder einen gesondert erlaubten Pflegeauftrag beauftragen. Notwendige Eingaben, Kriterien, Version und Ausgabeziel übergeben. Ein ständiger Aufruf des Firmenagenten ersetzt das Laden der gemeinsamen Pflichtquellen nicht.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P01_Ende

**Auftrag und zulässige Quellen bereit**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `endEvent`

Rückgabe an P00 mit Version und Herkunft; noch keine Aussage über Ergebnisqualität oder Freigabe.
Quelle: ../szenarien.md

#### P01_Join_Aufgabe

**Zusammenführung**

Verantwortung: OpenWebUI-Agent · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P01_Flow_Start_Identitaet` | `P01_Start` | `P01_Identitaet` | — |
| `P01_Flow_Identitaet_Paket` | `P01_Identitaet` | `P01_Paket` | — |
| `P01_Flow_Paket_Gueltig` | `P01_Paket` | `P01_Gueltig` | — |
| `P01_Flow_Gueltig_Stop` | `P01_Gueltig` | `P01_Stop` | nein |
| `P01_Flow_Gueltig_Aufgabe` | `P01_Gueltig` | `P01_Join_Aufgabe` | ja |
| `P01_Flow_Aufgabe_Klar` | `P01_Aufgabe` | `P01_Klar` | — |
| `P01_Flow_Klar_Rueckfrage` | `P01_Klar` | `P01_Rueckfrage` | nein |
| `P01_Flow_Klar_Index` | `P01_Klar` | `P01_Index` | ja |
| `P01_Flow_Rueckfrage_Aufgabe` | `P01_Rueckfrage` | `P01_Join_Aufgabe` | — |
| `P01_Flow_Index_ToolNoetig` | `P01_Index` | `P01_ToolNoetig` | — |
| `P01_Flow_ToolNoetig_Konto` | `P01_ToolNoetig` | `P01_Konto` | ja |
| `P01_Flow_ToolNoetig_Zusammen` | `P01_ToolNoetig` | `P01_Zusammen` | nein |
| `P01_Flow_Konto_Zugriff` | `P01_Konto` | `P01_Zugriff` | — |
| `P01_Flow_Zugriff_Fehlt` | `P01_Zugriff` | `P01_Fehlt` | nein |
| `P01_Flow_Zugriff_Lesen` | `P01_Zugriff` | `P01_Lesen` | ja |
| `P01_Flow_Lesen_Belege` | `P01_Lesen` | `P01_Belege` | — |
| `P01_Flow_Toolfehler_Blockiert` | `P01_Toolfehler` | `P01_Blockiert` | — |
| `P01_Flow_Belege_Zusammen` | `P01_Belege` | `P01_Zusammen` | — |
| `P01_Flow_Zusammen_PaketAuftrag` | `P01_Zusammen` | `P01_PaketAuftrag` | — |
| `P01_Flow_PaketAuftrag_Ende` | `P01_PaketAuftrag` | `P01_Ende` | — |
| `P01_Flow_Join_Aufgabe_Aufgabe` | `P01_Join_Aufgabe` | `P01_Aufgabe` | — |

### Nachrichten zwischen Beteiligten

| Kennung | Von | Nach | Inhalt |
|---|---|---|---|
| `P01_Message_Aufruf` | `P01_Lesen` (Quelle nutzergebunden lesen) | `P01_Tools` (Persönliche Quellsysteme · z. B. Gmail) | Aufruf als angemeldete Person |
| `P01_Message_Belege` | `P01_Tools` (Persönliche Quellsysteme · z. B. Gmail) | `P01_Belege` (Belege und Sichtbarkeit festhalten) | zulässige Daten + Herkunft |

## P02

P02 · Begrenzter Auftrag im Linux-Terminal

Quelle: [02-terminalauftrag.bpmn](02-terminalauftrag.bpmn) · SHA-256: `ddd30f0db3e7e9d5855cbff205ff68e0f119198388d56dcd7a804b23c189318e`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Codex als beauftragten Ausführer mit technischen Grenzen und überprüfbarer Rückgabe modellieren.
Offen: Fachauftrag oder Betriebssystem-Pflege mit getrenntem Mandat; technische Isolation; Tool-Übergabe A/B. Ein gemeinsam genutztes Home belegt keine Nutzertrennung.
Quellen: ../../PRD.md ; ../../SICHERHEIT.md ; ../pruefszenarien.md ; ../../beispiel/openwebui/fixtures/04-test-cases.md
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Auftrag bearbeiten
Kurz: Terminalauftrag

### Schritte und Entscheidungen

#### P02_Start

**Terminalauftrag empfangen**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `startEvent`

Auftrag aus P01; Rohchat, private Postfächer und Connector-Zugangsdaten gehören nicht automatisch dazu.
Quelle: ../szenarien.md

#### P02_Vertrag

**Mandat und Arbeitsauftrag prüfen**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `scriptTask`

Vertrauenswürdige Laufsteuerung prüft Auftraggeber, Aufgabe, Mandat, Quellversion, erlaubte Eingaben, Schreibbereich, Ausgabeziel und Laufgrenzen. Identität kommt aus der authentifizierten Übergabe, nicht aus Freitext. Fachlicher Worker und Pflege des gemeinsamen Betriebssystems haben getrennte Mandate; deren konkrete Zuteilung bleibt offen.
Quelle: ../../PRD.md

#### P02_Mandat

**Mandat ausdrücklich gedeckt?**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `exclusiveGateway`

Fachliche Bearbeitung und Pflege des gemeinsamen Betriebssystems sind unterschiedliche Rechte. Unentschieden bedeutet nicht freigegeben.
Quelle: ../../PRD.md

#### P02_Warten

**Mandat fehlt: Entscheidung nötig**

Verantwortung: Zuständige Person · BPMN-Typ: `endEvent`

Die zuständige Person muss das Mandat bestimmen. Das Modell dieses Prozesses entscheidet es nicht.
Quelle: ../../PRD.md

#### P02_Raum

**Arbeitsraum passend zum Auftrag zuweisen**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `serviceTask`

Getrennter Bereich je Schutzbedarf. Quellen nur lesbar, Ausgaben gesondert schreibbar; keine fremden Homes, Host-Mounts oder Docker-Sockets. Netz und Prozesse technisch begrenzen.
Quelle: ../../SICHERHEIT.md

#### P02_Isolation

**Grenzen nachgewiesen?**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `exclusiveGateway`

Die Isolation muss vor einem Mehrnutzer- oder Dateigrenzentest belegt sein. Ein Pfadname oder Prompt genügt nicht.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P02_Gesperrt

**Ausführung gesperrt**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `endEvent`

Die technische Voraussetzung fehlt. Kein Fallback auf eine unbeschränkte gemeinsame Shell.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P02_Stand

**Auftrag und Startzustand sichern**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `scriptTask`

Auftragskennung, Quellversionen, Status und Ausgangsdateien festhalten. Wiederholung darf keinen zweiten unabhängigen Auftrag verstecken.
Quelle: ../pruefszenarien.md

#### P02_Codex

**Codex im begrenzten Mandat ausführen**

Verantwortung: Codex im isolierten Arbeitsraum · BPMN-Typ: `serviceTask`

Nur im zugewiesenen Arbeitsraum arbeiten. Variante A erhält benötigte Daten aus OpenWebUI ohne Tool-Zugangsdaten. Variante B erhält einen auf Nutzer und Auftrag begrenzten Vermittlerzugang; vor jedem Abruf Rechte prüfen. Kein organisationsweiter Composio-/Admin-Schlüssel in der Shell. Weitere Tool-Abrufe nur innerhalb des gebundenen Auftrags. Beide Varianten sind ungetestet.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P02_Provider

**Provider- / Laufzeitfehler**

Verantwortung: Codex im isolierten Arbeitsraum · BPMN-Typ: `boundaryEvent`

Providerfehler, Kontingent oder Laufzeitfehler. Keine automatischen Anbieterwechsel und keine Wiederholungs-Endlosschleife. Quelle: ../pruefszenarien.md

Angehängt an: `P02_Codex` · unterbricht Aktivität: ja.

Ereignis: `errorEventDefinition` · errorRef=error_terminalfehler.

#### P02_Abbruch

**Abbruch angefordert**

Verantwortung: Codex im isolierten Arbeitsraum · BPMN-Typ: `boundaryEvent`

Abbruch ist ein eigener Status. Prozessbeendigung und Folgen müssen technisch geprüft werden. Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

Angehängt an: `P02_Codex` · unterbricht Aktivität: ja.

Ereignis: `signalEventDefinition` · signalRef=signal_auftragStoppen.

#### P02_Blockiert

**Blocker und Zwischenstand erfassen**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `scriptTask`

Status BLOCKIERT; keine Annahme über vollständige Ausgaben. Vor einer Wiederaufnahme bereits entstandene Artefakte und Wirkungen prüfen.
Quelle: ../pruefszenarien.md

#### P02_EndeFehler

**Blockiert zurückmelden**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `endEvent`

Fortsetzung nur nach P06 beziehungsweise neu bestätigtem Auftrag; Lauf bleibt als fehlgeschlagen sichtbar.
Quelle: ../pruefszenarien.md

#### P02_Stoppen

**Prozesse stoppen und Zustand erfassen**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `serviceTask`

Abbruch bestätigen, laufende Kindprozesse prüfen, unvollständige Artefakte markieren. Keine Ausgabe als erfolgreich ausgeben.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P02_EndeAbbruch

**Abgebrochen zurückmelden**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `endEvent`

Abbruchstatus samt überprüftem Zwischenstand zurückgeben.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P02_Sammeln

**Artefakte und Nachweise einsammeln**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `scriptTask`

Nur erlaubte Ergebnisdateien, Quellenbezüge, Quellversionen, Dateiveränderungen und Befehlsresultate zurückgeben. Geheimnisse aus Rückgabe und Logs fernhalten.
Quelle: ../pruefszenarien.md

#### P02_Rueckgabe

**Ergebnis zur Prüfung bereit**

Verantwortung: Adapter / Laufsteuerung · BPMN-Typ: `endEvent`

P03 prüft Ergebnis und Nachweise. Ein erfolgreicher Prozess-Exit beweist noch keine fachliche Richtigkeit.
Quelle: ../../agents/pruefer.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P02_Flow_Start_Vertrag` | `P02_Start` | `P02_Vertrag` | — |
| `P02_Flow_Vertrag_Mandat` | `P02_Vertrag` | `P02_Mandat` | — |
| `P02_Flow_Mandat_Warten` | `P02_Mandat` | `P02_Warten` | nein / offen |
| `P02_Flow_Mandat_Raum` | `P02_Mandat` | `P02_Raum` | ja |
| `P02_Flow_Raum_Isolation` | `P02_Raum` | `P02_Isolation` | — |
| `P02_Flow_Isolation_Gesperrt` | `P02_Isolation` | `P02_Gesperrt` | nein |
| `P02_Flow_Isolation_Stand` | `P02_Isolation` | `P02_Stand` | ja |
| `P02_Flow_Stand_Codex` | `P02_Stand` | `P02_Codex` | — |
| `P02_Flow_Codex_Sammeln` | `P02_Codex` | `P02_Sammeln` | — |
| `P02_Flow_Provider_Blockiert` | `P02_Provider` | `P02_Blockiert` | — |
| `P02_Flow_Abbruch_Stoppen` | `P02_Abbruch` | `P02_Stoppen` | — |
| `P02_Flow_Blockiert_EndeFehler` | `P02_Blockiert` | `P02_EndeFehler` | — |
| `P02_Flow_Stoppen_EndeAbbruch` | `P02_Stoppen` | `P02_EndeAbbruch` | — |
| `P02_Flow_Sammeln_Rueckgabe` | `P02_Sammeln` | `P02_Rueckgabe` | — |

## P03

P03 · Gegenprüfung und menschliche Entscheidung

Quelle: [03-pruefung-und-mensch.bpmn](03-pruefung-und-mensch.bpmn) · SHA-256: `5156db640f33e2804bc981a131307edce81af518fd8abf93a3a5e3e7b3bed4f6`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Ein Ergebnis gegen Kriterien und zulässige Belege prüfen, bevor die Person es als verwendbaren Entwurf erhält.
Offen: L10/L25: Träger und Rechte des Prüflaufs. Die Hauptunterhaltung ist kein frischer Kontext; Subagenten erben je nach Laufzeit Werkzeuge und müssen begrenzt werden.
Quellen: ../../agents/pruefer.md ; ../../AGENTS.md ; ../pruefszenarien.md ; https://docs.openwebui.com/features/chat-conversations/chat-features/subagents/
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Auftrag bearbeiten
Kurz: Prüfung & Mensch

### Schritte und Entscheidungen

#### P03_Start

**Ergebnis + Kriterien + Quellen vorliegend**

Verantwortung: Technische Prüfungen · BPMN-Typ: `startEvent`

Gilt für Ergebnisse aus direkten Tools und aus P02. Bewertet wird eine bestimmte Ergebnisfassung.
Quelle: ../../agents/pruefer.md

#### P03_Technik

**Messbare Eigenschaften prüfen**

Verantwortung: Technische Prüfungen · BPMN-Typ: `scriptTask`

Pflichtfelder, gültige Verweise, Dateigrenzen, Ausgabestatus und Unverändertheit geschützter Dateien prüfen. Ein Skripturteil ersetzt keine fachliche Bewertung.
Quelle: ../pruefszenarien.md

#### P03_Daten

**Prüfgrundlage vollständig und zulässig?**

Verantwortung: Technische Prüfungen · BPMN-Typ: `exclusiveGateway`

Der Prüfer darf Ergebnis und Belege bekommen. Fehlende oder gesperrte Quellen dürfen nicht durch mehr Rechte oder Vermutungen ersetzt werden.
Quelle: ../../agents/pruefer.md

#### P03_Offen

**OFFEN: Prüfgrundlage fehlt**

Verantwortung: Technische Prüfungen · BPMN-Typ: `endEvent`

Die fehlende Grundlage nennen. Ein Providerfehler ist ebenfalls kein bestandenes Review.
Quelle: ../../agents/pruefer.md

#### P03_Paket

**Frisches Prüfpaket übergeben**

Verantwortung: Technische Prüfungen · BPMN-Typ: `serviceTask`

Eigener frischer Prüflauf mit Aufgabe, Ergebnisfassung, Kriterien, zulässigen Quellen und Werkzeugresultaten. Keine gesamte Hauptunterhaltung. Dass der Hauptchat einen Worker beauftragt und seine Antwort liest, ist keine unabhängige Prüfung.
Quelle: ../../agents/pruefer.md

#### P03_Review

**Quellen lesen und Kriterien bewerten**

Verantwortung: Frischer Prüflauf / begrenzte Leserechte · BPMN-Typ: `serviceTask`

Frischer Lauf mit nachgewiesen begrenzten Leserechten, ohne Schreib- oder Versandwerkzeuge. Die Pi/Sandcastle-Entscheidung aus PRD L25 für den Änderungs-Prüfer bleibt bestehen; der Träger eines zusätzlichen OpenWebUI-Ergebnisreviews ist offen. Frischer Kontext garantiert keine Richtigkeit.
Quelle: ../../PRD.md

#### P03_Reviewfehler

**Prüfer nicht erreichbar**

Verantwortung: Frischer Prüflauf / begrenzte Leserechte · BPMN-Typ: `boundaryEvent`

Fehlgeschlagener Review ist kein bestandenes oder abgelehntes fachliches Ergebnis. Quelle: ../pruefszenarien.md

Angehängt an: `P03_Review` · unterbricht Aktivität: ja.

Ereignis: `errorEventDefinition` · errorRef=error_prueferfehler.

#### P03_Blockiert

**BLOCKIERT: Prüflauf fehlt**

Verantwortung: Technische Prüfungen · BPMN-Typ: `endEvent`

An P00 melden, dass noch kein auswertbares Prüfurteil vorliegt.
Quelle: ../../agents/pruefer.md

#### P03_Urteil

**Prüfurteil?**

Verantwortung: Frischer Prüflauf / begrenzte Leserechte · BPMN-Typ: `exclusiveGateway`

BESTANDEN je Kriterium ergibt FREIGEBEN; jede Verletzung ergibt ABLEHNEN; fehlende Grundlage ergibt OFFEN. Das ist ein Qualitätsurteil.
Quelle: ../../agents/pruefer.md

#### P03_Mangel

**Belegte Mängel zurückgeben**

Verantwortung: Frischer Prüflauf / begrenzte Leserechte · BPMN-Typ: `serviceTask`

Fundstelle und notwendige Korrektur nennen. Prüfer ändert keine Quelldatei.
Quelle: ../../agents/pruefer.md

#### P03_Reparieren

**Ergebnis im bestehenden Mandat korrigieren**

Verantwortung: Bearbeitender Agent · BPMN-Typ: `serviceTask`

Korrektur bleibt innerhalb von Rechten und Laufbudget. Bei ausgeschöpfter Grenze als Blocker vorlegen; kein endloses Reparieren.
Quelle: ../../AGENTS.md

#### P03_Budget

**Korrektur im Mandat möglich?**

Verantwortung: Bearbeitender Agent · BPMN-Typ: `exclusiveGateway`

Eine neue Quelle, zusätzliche Rechte oder verbrauchtes Budget kann eine neue Entscheidung erfordern.
Quelle: ../../AGENTS.md

#### P03_Vorlegen

**Entwurf mit Belegen und Prüfurteil vorlegen**

Verantwortung: Bearbeitender Agent · BPMN-Typ: `serviceTask`

OFFEN und ABLEHNEN sichtbar lassen. Nur ein bestandenes Ergebnis als fertig geprüft vorlegen.
Quelle: ../../AGENTS.md

#### P03_Mensch

**Ergebnis prüfen und entscheiden**

Verantwortung: Mitarbeitende · BPMN-Typ: `userTask`

Die Person sieht konkrete Ergebnisfassung und wesentliche Quellen; ihre Entscheidung bezieht sich genau auf diesen Stand.
Quelle: ../../AGENTS.md

#### P03_Entscheid

**Entscheidung?**

Verantwortung: Mitarbeitende · BPMN-Typ: `exclusiveGateway`

Annehmen, eine Korrektur verlangen oder abbrechen. Eine Bestätigung der Prüfung ist keine pauschale Erlaubnis für Außenwirkungen.
Quelle: ../../AGENTS.md

#### P03_Lernkandidat

**Korrektur und Ergebnisfassung erfassen**

Verantwortung: Bearbeitender Agent · BPMN-Typ: `serviceTask`

Korrektur mit der betroffenen Ergebnisfassung an P00 zurückgeben. P00 ruft P04 genau einmal auf; hier keine zweite gemeinsame Änderung anlegen.
Quelle: ../../AGENTS.md

#### P03_EndeKorrektur

**Korrektur übergeben**

Verantwortung: Bearbeitender Agent · BPMN-Typ: `endEvent`

Status KORREKTUR an P00; Ergebnisfassung ist noch nicht angenommen. Folgeauftrag bleibt ausdrücklich begrenzt.
Quelle: ../../AGENTS.md

#### P03_Ablehnen

**Abgebrochen**

Verantwortung: Mitarbeitende · BPMN-Typ: `endEvent`

Status ABBRUCH; nichts senden oder veröffentlichen.
Quelle: ../../AGENTS.md

#### P03_Ablage

**Angenommenen Entwurf zulässig ablegen**

Verantwortung: Bearbeitender Agent · BPMN-Typ: `serviceTask`

Nur am für diesen Auftrag freigegebenen Ziel, höchstens im Quellkreis der verarbeiteten Daten. Zustimmung zu einem Entwurf erweitert keine Zugriffsrechte.
Quelle: ../../SICHERHEIT.md

#### P03_Extern

**Außenhandlung gewünscht?**

Verantwortung: Mitarbeitende · BPMN-Typ: `exclusiveGateway`

Senden, Veröffentlichen und Bezahlen bleiben nach AGENTS außerhalb der Agentenbefugnis.
Quelle: ../../AGENTS.md

#### P03_Selbst

**Außenhandlung selbst ausführen**

Verantwortung: Mitarbeitende · BPMN-Typ: `userTask`

Wenn gewünscht, führt der Mensch sie selbst im jeweiligen System aus. Der Agent erhält daraus keine allgemeine Versandfreigabe.
Quelle: ../../AGENTS.md

#### P03_Angenommen

**Angenommen, Status nachvollziehbar**

Verantwortung: Mitarbeitende · BPMN-Typ: `endEvent`

Status ANGENOMMEN an P00. Log und Artefakte bleiben im zulässigen Kreis.
Quelle: ../../AGENTS.md

#### P03_Join_Technik

**Zusammenführung**

Verantwortung: Technische Prüfungen · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

#### P03_Join_Offen

**Zusammenführung**

Verantwortung: Technische Prüfungen · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

#### P03_Join_Angenommen

**Zusammenführung**

Verantwortung: Mitarbeitende · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P03_Flow_Start_Technik` | `P03_Start` | `P03_Join_Technik` | — |
| `P03_Flow_Technik_Daten` | `P03_Technik` | `P03_Daten` | — |
| `P03_Flow_Daten_Offen` | `P03_Daten` | `P03_Join_Offen` | nein |
| `P03_Flow_Daten_Paket` | `P03_Daten` | `P03_Paket` | ja |
| `P03_Flow_Paket_Review` | `P03_Paket` | `P03_Review` | — |
| `P03_Flow_Review_Urteil` | `P03_Review` | `P03_Urteil` | — |
| `P03_Flow_Reviewfehler_Blockiert` | `P03_Reviewfehler` | `P03_Blockiert` | — |
| `P03_Flow_Urteil_Offen` | `P03_Urteil` | `P03_Join_Offen` | OFFEN |
| `P03_Flow_Urteil_Mangel` | `P03_Urteil` | `P03_Mangel` | ABLEHNEN |
| `P03_Flow_Urteil_Vorlegen` | `P03_Urteil` | `P03_Vorlegen` | FREIGEBEN |
| `P03_Flow_Mangel_Reparieren` | `P03_Mangel` | `P03_Reparieren` | — |
| `P03_Flow_Reparieren_Budget` | `P03_Reparieren` | `P03_Budget` | — |
| `P03_Flow_Budget_Technik` | `P03_Budget` | `P03_Join_Technik` | ja |
| `P03_Flow_Budget_Offen` | `P03_Budget` | `P03_Join_Offen` | nein |
| `P03_Flow_Vorlegen_Mensch` | `P03_Vorlegen` | `P03_Mensch` | — |
| `P03_Flow_Mensch_Entscheid` | `P03_Mensch` | `P03_Entscheid` | — |
| `P03_Flow_Entscheid_Lernkandidat` | `P03_Entscheid` | `P03_Lernkandidat` | korrigieren |
| `P03_Flow_Entscheid_Ablehnen` | `P03_Entscheid` | `P03_Ablehnen` | abbrechen |
| `P03_Flow_Entscheid_Ablage` | `P03_Entscheid` | `P03_Ablage` | annehmen |
| `P03_Flow_Lernkandidat_EndeKorrektur` | `P03_Lernkandidat` | `P03_EndeKorrektur` | — |
| `P03_Flow_Ablage_Extern` | `P03_Ablage` | `P03_Extern` | — |
| `P03_Flow_Extern_Selbst` | `P03_Extern` | `P03_Selbst` | ja |
| `P03_Flow_Extern_Angenommen` | `P03_Extern` | `P03_Join_Angenommen` | nein |
| `P03_Flow_Selbst_Angenommen` | `P03_Selbst` | `P03_Join_Angenommen` | — |
| `P03_Flow_Join_Technik_Technik` | `P03_Join_Technik` | `P03_Technik` | — |
| `P03_Flow_Join_Offen_Offen` | `P03_Join_Offen` | `P03_Offen` | — |
| `P03_Flow_Join_Angenommen_Angenommen` | `P03_Join_Angenommen` | `P03_Angenommen` | — |

## P04

P04 · Korrektur, Änderungsvorschlag und Verteilung

Quelle: [04-lernen-und-verteilen.bpmn](04-lernen-und-verteilen.bpmn) · SHA-256: `bc123db4e1c4713ec4acd2a63db9ed28cbc888a5e5f5973dc18f59067ea2bb62`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Passende Korrekturen in die zuständige Quelle zurückführen und eine geprüfte Fassung für berechtigte Sitzungen bereitstellen.
Offen: Technischer Beitragsweg und Wechsel laufender Sitzungen. Ein gemeinsamer Kern ersetzt im allgemeinen System nicht die offenen Fragen L6/L8.
Quellen: ../../AGENTS.md ; ../../installation/README.md ; ../pruefszenarien.md ; ../../PRD.md
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Wissen verbessern
Kurz: Lernen & Verteilung

### Schritte und Entscheidungen

#### P04_Start

**Bestätigte Korrektur liegt vor**

Verantwortung: Arbeitsagent / Vorschlag · BPMN-Typ: `startEvent`

Auch ein Kontext-Hinweis aus P05 kann Material sein. Ein bloß beobachtetes Verhalten ist noch keine neue Firmenregel.
Quelle: ../../AGENTS.md

#### P04_Ursache

**Ursache und Geltungsbereich einordnen**

Verantwortung: Arbeitsagent / Vorschlag · BPMN-Typ: `serviceTask`

Quelle falsch, Kontext fehlt, Skill unklar, Werkzeuggrenze oder einmalige Präferenz? Zuständige vorhandene Quelle suchen, keine zusätzliche Regelkopie schaffen.
Quelle: ../szenarien.md

#### P04_Bereich

**Welcher Geltungsbereich?**

Verantwortung: Arbeitsagent / Vorschlag · BPMN-Typ: `exclusiveGateway`

Im Zweifel einmalig. Persönliche, rollenbezogene und gemeinsame Geltung unterscheiden. Eine Rollen-Anleitung beschreibt Arbeitsweise, nicht automatisch Geheimhaltung. Automatisches Lernen über einzelne Personen ist nach PRD Entscheidung 10/S17 ausgeschlossen.
Quelle: ../../PRD.md

#### P04_Einmalig

**Einmalig, im privaten Vorgang vermerkt**

Verantwortung: Arbeitsagent / Vorschlag · BPMN-Typ: `endEvent`

Kein gemeinsamer Paketwechsel. Der Inhalt bleibt im zulässigen persönlichen Arbeitsbereich.
Quelle: ../../AGENTS.md

#### P04_Persoenlich

**Persönliche Änderung bestätigen**

Verantwortung: Person / zuständiger Besitzer · BPMN-Typ: `userTask`

Nur im persönlichen Bereich und nach Zustimmung der Person pflegen. Firmenregeln bleiben davon unberührt.
Quelle: ../../PRD.md

#### P04_EndePrivat

**Persönlicher Stand angepasst**

Verantwortung: Person / zuständiger Besitzer · BPMN-Typ: `endEvent`

Keine Weitergabe privater Inhalte an andere Personen.
Quelle: ../../PRD.md

#### P04_Vorschlag

**Änderung + Prüffall + Herkunft entwerfen**

Verantwortung: Arbeitsagent / Vorschlag · BPMN-Typ: `serviceTask`

Bewährte Rollen-Anleitung als allgemeine Fähigkeit vorschlagen: Zweck, Kriterien und verallgemeinerter Prüffall. Keine privaten Rohbeispiele oder Personenprofile übernehmen. Bestehende Quelle und fachlichen Besitzer benennen. Eine nützliche persönliche Korrektur wird nicht automatisch firmenweit.
Quelle: ../../PRD.md

#### P04_Sichtbarkeit

**Eignung für den Zielkreis prüfen**

Verantwortung: Prüfung / Repository · BPMN-Typ: `scriptTask`

Keine privaten Rohchats, Kunden-/Personendaten oder Zugangsdaten in gemeinsame beziehungsweise öffentliche Artefakte übernehmen. Automatische Markerprüfung allein ist kein Vollständigkeitsbeweis.
Quelle: ../../SICHERHEIT.md

#### P04_Geeignet

**Vorschlag für Zielkreis geeignet?**

Verantwortung: Prüfung / Repository · BPMN-Typ: `exclusiveGateway`

Eine private Zusammenfassung wird durch Nützlichkeit nicht firmenöffentlich. Bei Zweifel zurück zur Quelle und zum Besitzer.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P04_Zurueck

**Privat belassen oder neu aufbereiten**

Verantwortung: Arbeitsagent / Vorschlag · BPMN-Typ: `endEvent`

Keine Erweiterung des Leser- oder Empfängerkreises.
Quelle: ../../SICHERHEIT.md

#### P04_JaNein

**Zuständige Person entscheidet über Vorschlag**

Verantwortung: Person / zuständiger Besitzer · BPMN-Typ: `userTask`

Die in AGENTS geregelte Zustimmung einholen. Ein Diagramm oder Modellurteil ersetzt dieses Ja nicht.
Quelle: ../../AGENTS.md

#### P04_Ja

**Zustimmung liegt vor?**

Verantwortung: Person / zuständiger Besitzer · BPMN-Typ: `exclusiveGateway`

Nein oder einmalig beendet die gemeinsame Änderung. Zustimmung und zugrunde liegende Fassung festhalten.
Quelle: ../../AGENTS.md

#### P04_Nein

**Nicht übernommen / einmalig**

Verantwortung: Arbeitsagent / Vorschlag · BPMN-Typ: `endEvent`

Entscheidung vermerken; keine gemeinsame Quelle ändern.
Quelle: ../../AGENTS.md

#### P04_Rueckweg

**Zulässiger Beitragsweg vorhanden?**

Verantwortung: Prüfung / Repository · BPMN-Typ: `exclusiveGateway`

Auch bei gemeinsam lesbarem Wiki bleiben Schreib- und Mergebefugnisse getrennt. Nur einen vorhandenen zulässigen Beitragsweg nutzen. PRD L8 bleibt für Konstellationen ohne Repo-Leserecht offen; das gemeinsame Zielbild löst diese allgemeine Lücke nicht.
Quelle: ../../PRD.md

#### P04_Wartet

**Wartet auf Beitragsweg / L8**

Verantwortung: Prüfung / Repository · BPMN-Typ: `endEvent`

Keinen Repository-Zugang oder externen Transport erfinden.
Quelle: ../../PRD.md

#### P04_PR

**Änderung als Pull Request vorlegen**

Verantwortung: Prüfung / Repository · BPMN-Typ: `serviceTask`

Nur die freigegebene, zulässige Änderung an der zuständigen Quelle. Ein PR bleibt ein Vorschlag.
Quelle: ../../installation/README.md

#### P04_Pruefung

**Regression, Quellen und Schutzregeln prüfen**

Verantwortung: Prüfung / Repository · BPMN-Typ: `serviceTask`

Bestehende Evals, Quellenverweise, Klassifizierungs- und Geheimnisprüfungen anwenden. Kriterien und Ampel nicht still lockern.
Quelle: ../pruefszenarien.md

#### P04_Bestanden

**Prüfungen bestanden?**

Verantwortung: Prüfung / Repository · BPMN-Typ: `exclusiveGateway`

Fehler erhalten bisherigen freigegebenen Stand. Reparatur als neuer Vorschlagsstand, keine Umgehung des Prüftors.
Quelle: ../../installation/README.md

#### P04_Fehlgeschlagen

**Änderung abgelehnt, alter Stand gilt**

Verantwortung: Prüfung / Repository · BPMN-Typ: `endEvent`

Befund samt fehlgeschlagenem Prüffall zurückgeben.
Quelle: ../pruefszenarien.md

#### P04_Merge

**Geltende Freigabe und Mergeverfahren anwenden**

Verantwortung: Prüfung / Repository · BPMN-Typ: `serviceTask`

Die zuvor bestätigte Änderung gemäß geltendem Repository-Verfahren und Branchschutz zusammenführen. Zuständige menschliche Freigaben bleiben erhalten; erlaubtes technisches Mergen darf ein Agent übernehmen. Ampel, Sperren und Grundregeln gibt ausschließlich ein Mensch frei. Diese Darstellung verlangt keine zusätzliche pauschale manuelle Mergefreigabe.
Quelle: ../../AGENTS.md

#### P04_Build

**Gemeinsamen Kern versionieren**

Verantwortung: Paketbau / Verteilung · BPMN-Typ: `scriptTask`

Für dieses Zielbild einen gemeinsamen Kern aus freigegebenem Wiki, Regeln und Skills bauen. Persönliche Ergänzungen getrennt halten; vertrauliche Daten bleiben in Quellsystemen. OpenWebUI und Worker beziehen dieselben zuständigen Quellen mit erkennbarer Version. Rollenpakete aus PRD L6 sind keine Voraussetzung dieses Versuchs.
Quelle: ../../installation/README.md

#### P04_Test

**P07 · Neue Fassung und Rücknahme prüfen**

Verantwortung: Paketbau / Verteilung · BPMN-Typ: `callActivity`

In Testumgebung einschließlich frischer Sitzung B ohne privaten Marker von A prüfen. Ein Paketvergleich ist noch kein echter Sitzungsnachweis.
Quelle: ../pruefszenarien.md

Aufgerufener Prozess: [P07](#p07).

#### P04_TestOk

**Bereitstellung abgenommen?**

Verantwortung: Paketbau / Verteilung · BPMN-Typ: `exclusiveGateway`

Ohne erfolgreiche Abnahme kein Wechsel des aktiven gemeinsamen Stands.
Quelle: ../../installation/README.md

#### P04_Release

**Bereitstellung ausdrücklich freigeben**

Verantwortung: Person / zuständiger Besitzer · BPMN-Typ: `userTask`

Die geltende Release-Freigabe anwenden. Der Modellierungsauftrag schaltet keine Verteilung ein.
Quelle: ../../installation/README.md

#### P04_Stand

**Version bereitstellen und Sitzungen zuordnen**

Verantwortung: Paketbau / Verteilung · BPMN-Typ: `serviceTask`

Frische Sitzungen erhalten passende neue Fassung. Bestehende Sitzungen behalten erkennbaren Stand oder wechseln kontrolliert; kein sofortiges Update behaupten.
Quelle: ../../installation/README.md

#### P04_Ende

**Geprüfte Verbesserung bereit**

Verantwortung: Paketbau / Verteilung · BPMN-Typ: `endEvent`

Version, Zielkreis, Prüfnachweis und möglicher Rücknahmestand sind nachvollziehbar.
Quelle: ../../installation/README.md

#### P04_Join_Fehlgeschlagen

**Zusammenführung**

Verantwortung: Prüfung / Repository · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P04_Flow_Start_Ursache` | `P04_Start` | `P04_Ursache` | — |
| `P04_Flow_Ursache_Bereich` | `P04_Ursache` | `P04_Bereich` | — |
| `P04_Flow_Bereich_Einmalig` | `P04_Bereich` | `P04_Einmalig` | einmalig |
| `P04_Flow_Bereich_Persoenlich` | `P04_Bereich` | `P04_Persoenlich` | persönlich |
| `P04_Flow_Bereich_Vorschlag` | `P04_Bereich` | `P04_Vorschlag` | Projekt / Rolle / Firma |
| `P04_Flow_Persoenlich_EndePrivat` | `P04_Persoenlich` | `P04_EndePrivat` | — |
| `P04_Flow_Vorschlag_Sichtbarkeit` | `P04_Vorschlag` | `P04_Sichtbarkeit` | — |
| `P04_Flow_Sichtbarkeit_Geeignet` | `P04_Sichtbarkeit` | `P04_Geeignet` | — |
| `P04_Flow_Geeignet_Zurueck` | `P04_Geeignet` | `P04_Zurueck` | nein / offen |
| `P04_Flow_Geeignet_JaNein` | `P04_Geeignet` | `P04_JaNein` | ja |
| `P04_Flow_JaNein_Ja` | `P04_JaNein` | `P04_Ja` | — |
| `P04_Flow_Ja_Nein` | `P04_Ja` | `P04_Nein` | nein / einmalig |
| `P04_Flow_Ja_Rueckweg` | `P04_Ja` | `P04_Rueckweg` | ja |
| `P04_Flow_Rueckweg_Wartet` | `P04_Rueckweg` | `P04_Wartet` | nein |
| `P04_Flow_Rueckweg_PR` | `P04_Rueckweg` | `P04_PR` | ja |
| `P04_Flow_PR_Pruefung` | `P04_PR` | `P04_Pruefung` | — |
| `P04_Flow_Pruefung_Bestanden` | `P04_Pruefung` | `P04_Bestanden` | — |
| `P04_Flow_Bestanden_Fehlgeschlagen` | `P04_Bestanden` | `P04_Join_Fehlgeschlagen` | nein |
| `P04_Flow_Bestanden_Merge` | `P04_Bestanden` | `P04_Merge` | ja |
| `P04_Flow_Merge_Build` | `P04_Merge` | `P04_Build` | — |
| `P04_Flow_Build_Test` | `P04_Build` | `P04_Test` | — |
| `P04_Flow_Test_TestOk` | `P04_Test` | `P04_TestOk` | — |
| `P04_Flow_TestOk_Fehlgeschlagen` | `P04_TestOk` | `P04_Join_Fehlgeschlagen` | nein |
| `P04_Flow_TestOk_Release` | `P04_TestOk` | `P04_Release` | ja |
| `P04_Flow_Release_Stand` | `P04_Release` | `P04_Stand` | — |
| `P04_Flow_Stand_Ende` | `P04_Stand` | `P04_Ende` | — |
| `P04_Flow_Join_Fehlgeschlagen_Fehlgeschlagen` | `P04_Join_Fehlgeschlagen` | `P04_Fehlgeschlagen` | — |

## P05

P05 · Wissen finden, anreichern und pflegen

Quelle: [05-kontextpflege.bpmn](05-kontextpflege.bpmn) · SHA-256: `5a25b149f1681cd42e9973d276ace7dc98cfcd53a97264fd213151b854165c3b`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Dauerhaftes Wissen mit Herkunft und Besitzer pflegen, ohne persönliche Vorgänge in einen größeren Kreis zu verschieben.
Offen: L1/L7/L12: Identität, Informationsfluss und Logbuch der Routine. Automatische Übernahme unstrittiger Artikel-Ergänzungen wird hier nicht als neue lokale Freigaberegel übernommen.
Quellen: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst ; ../szenarien.md ; ../../PRD.md ; ../../AGENTS.md
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Wissen verbessern
Kurz: Kontextpflege

### Schritte und Entscheidungen

#### P05_Hinweis

**Kontext-Hinweis oder Ansage**

Verantwortung: Kontext-Agent · BPMN-Typ: `startEvent`

Eine Person meldet einen neuen oder widersprüchlichen Fakt. Er bleibt zunächst im berechtigten Vorgang.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Ernte

**Zulässige neue Quellen lesen**

Verantwortung: Kontext-Agent · BPMN-Typ: `serviceTask`

Ein freigegebener Pflegeauftrag liest nur zulässige Quellen mit ausdrücklich zugewiesenem Konto. Ein zeitgesteuerter Lauf übernimmt nicht die Identität des zuletzt aktiven Chatnutzers. Herkunft und Sichtbarkeit jeder Aussage mitführen.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Pflege

**Bestandspflege beauftragt**

Verantwortung: Freigegebener Pflegeauftrag / technische Prüfung · BPMN-Typ: `startEvent`

Eine freigegebene Routine nach P06 oder eine manuelle Beauftragung. Kein fest eingebauter neuer Zeitplan.
Quelle: ../../PRD.md

#### P05_Scan

**Verweise, Metadaten und Fälligkeit prüfen**

Verantwortung: Freigegebener Pflegeauftrag / technische Prüfung · BPMN-Typ: `scriptTask`

Index, Quellen, Besitzer, Prüfdatum, Verweise und verwaiste Einträge prüfen. Bereichsbesitz bedeutet fachliche Verantwortung; Frontmatter und Ordnerstruktur sind keine technischen Leserechte. Das gemeinsame Wiki wird hier für alle gepflegt.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Inhalt

**Widersprüche und doppelte Aussagen finden**

Verantwortung: Kontext-Agent · BPMN-Typ: `serviceTask`

Fachliche Prüfung von Aktualität und Quellenlage. Ein älteres Dokument wird nicht allein wegen einer neueren Fundstelle automatisch falsch.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Merge

**Zusammenführung**

Verantwortung: Kontext-Agent · BPMN-Typ: `exclusiveGateway`

Die folgenden Fragen gelten sowohl für neue Aussagen als auch für Pflegebefunde.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Nutzen

**Dauerhaftes Arbeitswissen?**

Verantwortung: Kontext-Agent · BPMN-Typ: `exclusiveGateway`

Nur Kandidaten, die künftiges Arbeiten verändern, in die gemeinsame Pflege geben. Laufende Vorgänge bleiben im Tool.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Vorgang

**Im Quellsystem belassen**

Verantwortung: Kontext-Agent · BPMN-Typ: `endEvent`

Keine Kopie des operativen Vorgangs in ein allgemeines Wiki.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Kreis

**Zielkreis von Quelle gedeckt?**

Verantwortung: Freigegebener Pflegeauftrag / technische Prüfung · BPMN-Typ: `exclusiveGateway`

Ins gemeinsame Wiki nur Wissen aufnehmen, das für das ganze Team geeignet und freigegeben ist. Private Mailzusammenfassungen bleiben außerhalb, auch wenn sie nützlich sind. Geschützte Informationen verbleiben im Quellsystem; abgeleitete Artefakte bleiben im zulässigen Empfängerkreis.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Privat

**Quelle bleibt im bisherigen Kreis**

Verantwortung: Freigegebener Pflegeauftrag / technische Prüfung · BPMN-Typ: `endEvent`

Privater Kontext-Hinweis gegebenenfalls nur dem berechtigten Besitzer vorlegen; keine Veröffentlichung über Logs oder Index.
Quelle: ../../SICHERHEIT.md

#### P05_Beleg

**Aussage, Quelle und Abhängigkeiten prüfen**

Verantwortung: Kontext-Agent · BPMN-Typ: `serviceTask`

Was gilt jetzt? Wer besitzt den Bereich? Welche Skills oder Dateien bauen darauf auf? Fehlende Belege und widersprüchliche Ansagen offenhalten.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Eindeutig

**Quelle und Geltung geklärt?**

Verantwortung: Kontext-Agent · BPMN-Typ: `exclusiveGateway`

Widersprüche, Grundlagenthemen und fachliche Entscheidungen bleiben beim zuständigen Besitzer.
Quelle: ../../AGENTS.md

#### P05_Besitzer

**Geltende Aussage klären**

Verantwortung: Quellen- / Bereichsbesitzer · BPMN-Typ: `userTask`

Der Besitzer bestätigt oder verwirft eine konkrete Aussage mit Quelle und Datum. Keine still erfundene Zuständigkeit.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Geklaert

**Klärung möglich?**

Verantwortung: Quellen- / Bereichsbesitzer · BPMN-Typ: `exclusiveGateway`

Auch nach einer Rückfrage kann eine Quelle fehlen. Dann bleibt der Kontext-Hinweis offen.
Quelle: ../../AGENTS.md

#### P05_Offen

**Kontext-Lücke sichtbar**

Verantwortung: Kontext-Agent · BPMN-Typ: `endEvent`

Fehlende Grundlage und benötigte Entscheidung vermerken, ohne sie im Wiki als Tatsache darzustellen.
Quelle: ../../AGENTS.md

#### P05_Vorschlag

**Änderung an zuständiger Quelle entwerfen**

Verantwortung: Kontext-Agent · BPMN-Typ: `serviceTask`

Eine aktuelle Aussage je Thema mit Herkunft; veraltete Fassung über Versionierung nachvollziehbar. Abhängige Quellen und betroffene Prüffragen mitprüfen.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Lernen

**P04 · Freigabe und geprüfter Rückweg**

Verantwortung: Freigegebener Pflegeauftrag / technische Prüfung · BPMN-Typ: `callActivity`

Die bestehenden lokalen Freigaberegeln gelten auch für Kontext-Ernte. Der Artikel beschreibt teilweise automatische Übernahme; diese wird hier nicht neu eingeführt.
Quelle: ../../AGENTS.md

Aufgerufener Prozess: [P04](#p04).

#### P05_Ende

**Kandidat geprüft oder bewusst offen**

Verantwortung: Kontext-Agent · BPMN-Typ: `endEvent`

Pflegebefund und Entscheidung bleiben erreichbar. Verteilung eines neuen Stands erfolgt nur nach P04.
Quelle: https://ai-first.ai/insights/wie-unser-kontext-layer-mitwaechst

#### P05_Join_Vorschlag

**Zusammenführung**

Verantwortung: Kontext-Agent · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P05_Flow_Hinweis_Ernte` | `P05_Hinweis` | `P05_Ernte` | — |
| `P05_Flow_Ernte_Merge` | `P05_Ernte` | `P05_Merge` | — |
| `P05_Flow_Pflege_Scan` | `P05_Pflege` | `P05_Scan` | — |
| `P05_Flow_Scan_Inhalt` | `P05_Scan` | `P05_Inhalt` | — |
| `P05_Flow_Inhalt_Merge` | `P05_Inhalt` | `P05_Merge` | — |
| `P05_Flow_Merge_Nutzen` | `P05_Merge` | `P05_Nutzen` | — |
| `P05_Flow_Nutzen_Vorgang` | `P05_Nutzen` | `P05_Vorgang` | nein |
| `P05_Flow_Nutzen_Kreis` | `P05_Nutzen` | `P05_Kreis` | ja |
| `P05_Flow_Kreis_Privat` | `P05_Kreis` | `P05_Privat` | nein / offen |
| `P05_Flow_Kreis_Beleg` | `P05_Kreis` | `P05_Beleg` | ja |
| `P05_Flow_Beleg_Eindeutig` | `P05_Beleg` | `P05_Eindeutig` | — |
| `P05_Flow_Eindeutig_Besitzer` | `P05_Eindeutig` | `P05_Besitzer` | nein |
| `P05_Flow_Eindeutig_Vorschlag` | `P05_Eindeutig` | `P05_Join_Vorschlag` | ja |
| `P05_Flow_Besitzer_Geklaert` | `P05_Besitzer` | `P05_Geklaert` | — |
| `P05_Flow_Geklaert_Offen` | `P05_Geklaert` | `P05_Offen` | nein |
| `P05_Flow_Geklaert_Vorschlag` | `P05_Geklaert` | `P05_Join_Vorschlag` | ja |
| `P05_Flow_Vorschlag_Lernen` | `P05_Vorschlag` | `P05_Lernen` | — |
| `P05_Flow_Lernen_Ende` | `P05_Lernen` | `P05_Ende` | — |
| `P05_Flow_Join_Vorschlag_Vorschlag` | `P05_Join_Vorschlag` | `P05_Vorschlag` | — |

## P06

P06 · Routine, Unterbrechung und Wiederaufnahme

Quelle: [06-routine-und-wiederaufnahme.bpmn](06-routine-und-wiederaufnahme.bpmn) · SHA-256: `9c7eb3c7d3c39dfb8a7a0cd00120c2237853309df05c5bc65bb7dabf3dcf5fa1`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Einen ausdrücklich freigegebenen Hintergrundauftrag nachvollziehbar starten, anhalten und ohne unbemerkte Doppelwirkung fortsetzen.
Offen: L1/L15/L25: Engine, Identität, Nachrichtenzustellung und technische Wiederaufnahme sind offen. Ein Diagramm garantiert weder dauerhafte Ausführung noch Exactly-once-Wirkung.
Quellen: ../pruefszenarien.md ; ../../PRD.md ; ../../AGENTS.md
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Betrieb prüfen
Kurz: Routine & Neustart

### Schritte und Entscheidungen

#### P06_Start

**Auslöser oder Fortsetzung eingegangen**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `startEvent`

Manueller Auftrag, freigegebenes Ereignis oder Zeitplan. Ein Auslöser allein erteilt keine zusätzlichen Rechte.
Quelle: ../../PRD.md

#### P06_Auftrag

**Freigabe, Identität und Grenzen prüfen**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `scriptTask`

Freigabe, Auftragssnapshot, explizites Nutzer- oder Dienstkonto, Quellen, Ziel, Laufgrenzen und zuständige Person prüfen. Ein Zeitplan hat keinen angemeldeten Chatnutzer. Rechte vor Wiederaufnahme erneut prüfen, nicht aus einem alten Profil übernehmen.
Quelle: ../../PRD.md

#### P06_Aktiv

**Auftrag gültig und freigegeben?**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `exclusiveGateway`

Abgelaufene oder deaktivierte Aufträge werden nicht durch eine alte Nachricht wieder aktiviert.
Quelle: ../pruefszenarien.md

#### P06_Inaktiv

**Nicht gestartet**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `endEvent`

Status und fehlende Voraussetzung sichtbar machen; keine neue Routine einschalten.
Quelle: ../../AGENTS.md

#### P06_Schluessel

**Kennung und bisherigen Zustand ermitteln**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `scriptTask`

Ereigniskennung und Auftragssnapshot verwenden; bestehende Läufe und mögliche bereits erfolgte Wirkungen abgleichen.
Quelle: ../pruefszenarien.md

#### P06_Doppelt

**Schon erledigt oder noch laufend?**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `exclusiveGateway`

Eine doppelte Nachricht ist kein neuer unabhängiger Auftrag.
Quelle: ../pruefszenarien.md

#### P06_Alt

**Bisherigen Status zurückgeben**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `endEvent`

Ergebnis oder laufenden Auftrag referenzieren, keinen zweiten Lauf anlegen.
Quelle: ../pruefszenarien.md

#### P06_Checkpoint

**Prüfpunkt und nächste Aktion sichern**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `scriptTask`

Status vor riskanten Schritten sichern. Bei unklarer früherer Wirkung zuerst mit dem Zielsystem abgleichen.
Quelle: ../pruefszenarien.md

#### P06_Arbeiten

**Freigegebenen Teilauftrag ausführen**

Verantwortung: Beauftragter Agent · BPMN-Typ: `serviceTask`

Fachlicher Ablauf nach P01–P03 oder Pflege nach P05. Das geschlossene Browserfenster darf die Zustellung nicht ersetzen.
Quelle: ../../PRD.md

#### P06_Fehler

**Provider / Prozess unterbrochen**

Verantwortung: Beauftragter Agent · BPMN-Typ: `boundaryEvent`

Providerfehler oder Prozessabbruch. Zustand und mögliche Wirkung prüfen. Quelle: ../pruefszenarien.md#s12-routine-mit-rueckfrage

Angehängt an: `P06_Arbeiten` · unterbricht Aktivität: ja.

Ereignis: `errorEventDefinition` · errorRef=error_routineUnterbrochen.

#### P06_Blockiert

**Blocker und sicheren Prüfpunkt melden**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `scriptTask`

Fehlerart und Wiederaufnahmebedingung festhalten. Das Ergebnis gilt nicht als fachlich fehlgeschlagen oder bestanden, solange kein auswertbares Ergebnis vorliegt.
Quelle: ../pruefszenarien.md

#### P06_EndeBlock

**BLOCKIERT, Fortsetzung ausstehend**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `endEvent`

Ein späterer ausdrücklich zulässiger Fortsetzungsversuch startet über den Eingang und prüft den Zustand erneut.
Quelle: ../pruefszenarien.md

#### P06_Rueckfrage

**Entscheidung nötig?**

Verantwortung: Beauftragter Agent · BPMN-Typ: `exclusiveGateway`

Eine unklare Pflichtangabe, Freigabe oder geänderte Quelle kann eine menschliche Entscheidung brauchen.
Quelle: ../../AGENTS.md

#### P06_Melden

**Konkrete Fassung zur Entscheidung zustellen**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `serviceTask`

Zuständiger Person, Ergebnisfassung und Quellenstand zuordnen. Kanal und Zustellung bleiben Implementierungsfragen, keine neue Slack-Pflicht.
Quelle: ../../PRD.md

#### P06_Antwort

**Auf gebundene Entscheidung warten**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `receiveTask`

Wartestatus dauerhaft speichern. Eine verlorene oder alte Antwort ist keine Freigabe.
Quelle: ../pruefszenarien.md

#### P06_Stop

**Stop / Widerruf**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `boundaryEvent`

Stop beendet den wartenden Lauf, ohne ihn automatisch zu wiederholen. Quelle: ../pruefszenarien.md

Angehängt an: `P06_Antwort` · unterbricht Aktivität: ja.

Ereignis: `signalEventDefinition` · signalRef=signal_auftragStoppen.

#### P06_Beenden

**ABGEBROCHEN, Stand erhalten**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `endEvent`

Verbleibende Prozesse und bereits erfolgte Wirkungen prüfen; bei Unsicherheit als offen melden.
Quelle: ../pruefszenarien.md

#### P06_Gueltig

**Person, Fassung und Rechte noch gültig?**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `exclusiveGateway`

Antwort mit Auftragskennung, Ergebnisfassung und aktuellem Quellen-/Rechtestand abgleichen. Eine alte Zustimmung darf keine neue Fassung freigeben.
Quelle: ../pruefszenarien.md

#### P06_Neu

**Neue Entscheidung erforderlich**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `endEvent`

Veraltete Antwort zurückweisen; die zuständige Person bekommt die aktuelle Fassung in einem zulässigen Folgeauftrag.
Quelle: ../pruefszenarien.md

#### P06_Ja

**Zugestimmt?**

Verantwortung: Zuständige Person · BPMN-Typ: `exclusiveGateway`

Ablehnung beendet diesen Lauf. Eine Zustimmung bleibt auf den konkret freigegebenen Schritt begrenzt.
Quelle: ../../AGENTS.md

#### P06_Vereinen

**Zusammenführung**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `exclusiveGateway`

Weiter nur mit ausreichender bestehender Freigabe oder gültiger neuer Entscheidung.
Quelle: ../pruefszenarien.md

#### P06_Wirkung

**Erlaubte Wirkung mit Zustand abgleichen**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `scriptTask`

Vor Schreiben im Zielsystem auf bereits vorhandene Wirkung prüfen; bei unklarem früherem Commit abgleichen statt blind wiederholen. Außenhandlungen bleiben beim Menschen nach P03.
Quelle: ../pruefszenarien.md

#### P06_Fertig

**Ergebnis und tatsächliche Wirkung melden**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `serviceTask`

Auch ein Lauf ohne Änderungen meldet den Status. Inhaltliche Nacharbeit und Betriebskosten bleiben messbar.
Quelle: ../szenarien.md

#### P06_Ende

**Abgeschlossen und nachvollziehbar**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `endEvent`

Auftrag, Version, Ergebnis, Wirkungsbeleg und Logstatus sind verbunden; Daten bleiben im zulässigen Kreis.
Quelle: ../pruefszenarien.md

#### P06_Join_Beenden

**Zusammenführung**

Verantwortung: Laufsteuerung / dauerhafter Auftragsstatus · BPMN-Typ: `exclusiveGateway`

Alternative Eingänge ausdrücklich zusammenführen; keine Synchronisation paralleler Ausführungen.
Quelle: ../szenarien.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P06_Flow_Start_Auftrag` | `P06_Start` | `P06_Auftrag` | — |
| `P06_Flow_Auftrag_Aktiv` | `P06_Auftrag` | `P06_Aktiv` | — |
| `P06_Flow_Aktiv_Inaktiv` | `P06_Aktiv` | `P06_Inaktiv` | nein |
| `P06_Flow_Aktiv_Schluessel` | `P06_Aktiv` | `P06_Schluessel` | ja |
| `P06_Flow_Schluessel_Doppelt` | `P06_Schluessel` | `P06_Doppelt` | — |
| `P06_Flow_Doppelt_Alt` | `P06_Doppelt` | `P06_Alt` | ja |
| `P06_Flow_Doppelt_Checkpoint` | `P06_Doppelt` | `P06_Checkpoint` | nein |
| `P06_Flow_Checkpoint_Arbeiten` | `P06_Checkpoint` | `P06_Arbeiten` | — |
| `P06_Flow_Arbeiten_Rueckfrage` | `P06_Arbeiten` | `P06_Rueckfrage` | — |
| `P06_Flow_Fehler_Blockiert` | `P06_Fehler` | `P06_Blockiert` | — |
| `P06_Flow_Blockiert_EndeBlock` | `P06_Blockiert` | `P06_EndeBlock` | — |
| `P06_Flow_Rueckfrage_Melden` | `P06_Rueckfrage` | `P06_Melden` | ja |
| `P06_Flow_Rueckfrage_Vereinen` | `P06_Rueckfrage` | `P06_Vereinen` | nein |
| `P06_Flow_Melden_Antwort` | `P06_Melden` | `P06_Antwort` | — |
| `P06_Flow_Antwort_Gueltig` | `P06_Antwort` | `P06_Gueltig` | — |
| `P06_Flow_Stop_Beenden` | `P06_Stop` | `P06_Join_Beenden` | — |
| `P06_Flow_Gueltig_Neu` | `P06_Gueltig` | `P06_Neu` | nein |
| `P06_Flow_Gueltig_Ja` | `P06_Gueltig` | `P06_Ja` | ja |
| `P06_Flow_Ja_Beenden` | `P06_Ja` | `P06_Join_Beenden` | nein |
| `P06_Flow_Ja_Vereinen` | `P06_Ja` | `P06_Vereinen` | ja |
| `P06_Flow_Vereinen_Wirkung` | `P06_Vereinen` | `P06_Wirkung` | — |
| `P06_Flow_Wirkung_Fertig` | `P06_Wirkung` | `P06_Fertig` | — |
| `P06_Flow_Fertig_Ende` | `P06_Fertig` | `P06_Ende` | — |
| `P06_Flow_Join_Beenden_Beenden` | `P06_Join_Beenden` | `P06_Beenden` | — |

## P07

P07 · Reproduzierbarer Test mit fiktiver Firma

Quelle: [07-testbetrieb.bpmn](07-testbetrieb.bpmn) · SHA-256: `21c44963fe4d85e281a157dbf1c062c92d5d94620ac2d03e515987584fd1f604`

Entwurf v0.2 | GPT-6-astra | 11.11.2026
Zweck: Die entworfenen Abläufe mit getrennten Testpersonen, festen Eingaben und nachprüfbaren Grenzen erproben, bevor der Adapter freigegeben wird.
Offen: A/B noch ungetestet. Zuerst Identität, Kontobindung und Isolation nachweisen; danach Modellläufe. Providerfehler getrennt von fachlichen Fehlern ausweisen.
Quellen: ../../beispiel/openwebui/fixtures/04-test-cases.md ; ../pruefszenarien.md ; ../../installation/README.md ; ../../SICHERHEIT.md
Lesart: Fachlicher Sollprozess zur Diskussion, keine Betriebsfreigabe. Nicht ausführbar. Bahnen zeigen Verantwortung, keine nachgewiesene technische Isolation.
Kapitel: Betrieb prüfen
Kurz: Testbetrieb

### Schritte und Entscheidungen

#### P07_Start

**Konkreter Teststand vorgesehen**

Verantwortung: Testverantwortliche · BPMN-Typ: `startEvent`

Modellierter Ablauf für spätere Adaptertests; diese Diagrammerstellung selbst führt keine Modelltests aus.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Plan

**Fälle und Sollkriterien vorab festlegen**

Verantwortung: Testverantwortliche · BPMN-Typ: `userTask`

Zunächst modellfreie Identitäts-/Rechteproben nach E/F/H, danach wenige echte Modellläufe nach A/C/G/I/J/K. Varianten A (Tools in OpenWebUI) und B (Vermittler) getrennt erfassen. Nicht durch Testaufbau entscheiden, welcher Weg künftig gilt.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Manifest

**Testmanifest und festen Startstand erfassen**

Verantwortung: Testaufbau / Rechte / Messung · BPMN-Typ: `scriptTask`

Repo-Commit, Paket-/Modellstand, relevante Konfiguration, synthetische Datenversion, Rollen, Quellen und Fallkennungen protokollieren. Keine Zugangsdaten.
Quelle: ../pruefszenarien.md

#### P07_Aufbau

**Getrennte Testkonten und Arbeitsräume aufbauen**

Verantwortung: Testaufbau / Rechte / Messung · BPMN-Typ: `serviceTask`

Zwei fiktive Personen, gemeinsame gültige Grundlagen, getrennte private Quellen und Ausgaben. Persönliche Tools zunächst mit synthetischen Daten simulieren.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Grenzen

**Isolation und Rechte vorab nachweisen**

Verantwortung: Testaufbau / Rechte / Messung · BPMN-Typ: `scriptTask`

Nachweis vor Mehrnutzer-/Terminaltest: getrennte Testkonten, nur synthetische Daten, keine echten Hostdaten. A liest A als Positivkontrolle; B und unautorisierte Aufrufe erreichen A nicht. Fremde Kennung im Prompt/Argument sowie widerrufene Rechte ablehnen. Tool, Arbeitsraum, Cache, Logs und Ausgaben einbeziehen. Quellcode-Lektüre ist noch kein Laufnachweis.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Sicher

**Grenzen belegt?**

Verantwortung: Testaufbau / Rechte / Messung · BPMN-Typ: `exclusiveGateway`

Ohne Isolation keinen Mehrbenutzer- oder Terminalgrenzentest durchführen. Eine gemeinsame Shell ist kein Nachweis.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Sperre

**Test blockiert: Voraussetzung fehlt**

Verantwortung: Testaufbau / Rechte / Messung · BPMN-Typ: `endEvent`

Blocker und nicht ausgeführte Fälle nennen. Ein blockierter Test ist kein bestandener Test.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Normal

**Normalfall und fehlende Quelle durchspielen**

Verantwortung: OpenWebUI und Codex im Test · BPMN-Typ: `serviceTask`

Einfache Wissensfrage gegen Datei-/Coding-Auftrag vergleichen: Kern ohne Worker nutzbar, begrenzter Worker nur bei Bedarf. Persönliche Ergänzungen getrennt. Korrektes und fehlerhaftes Ergebnis mit frischem lesendem Prüfer prüfen. Tool-Konto und im Zielsystem protokollierte Ausführungsidentität prüfen.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Fehler

**Providerfehler und Abbruch simulieren**

Verantwortung: OpenWebUI und Codex im Test · BPMN-Typ: `serviceTask`

Ausschließlich ungefährliche Testunterbrechungen: Limitantwort, fehlende Quelle, Prozessabbruch, alte Zustimmung und doppelte Eingabe. Keine Kontorotation oder Anbieterwechsel durch den Test.
Quelle: ../pruefszenarien.md

#### P07_Update

**Gemeinsame Verbesserung und Rücknahme prüfen**

Verantwortung: OpenWebUI und Codex im Test · BPMN-Typ: `serviceTask`

Sitzung A liefert eine bestätigte allgemeine Korrektur. Frische Sitzung B verwendet freigegebenen neuen Stand ohne privaten Marker von A. Bestehende Chats und Rücknahme gesondert prüfen.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Messung

**Antworten, Status und Spuren erfassen**

Verantwortung: Testaufbau / Rechte / Messung · BPMN-Typ: `scriptTask`

Je Fall Antwort/Artefakt, Quellen und Version, Rechtest, Prüfurteil, menschliche Nacharbeit und tatsächliche Unterbrechung erfassen. Zeit-/Kostenzahlen nur messen, nicht schätzen.
Quelle: ../pruefszenarien.md

#### P07_Ergebnis

**Auswertbares Ergebnis vorhanden?**

Verantwortung: Auswertung / Gegenprobe · BPMN-Typ: `exclusiveGateway`

Provider-/Infrastrukturfehler separat als BLOCKIERT/FEHLER führen. Sie beweisen weder gute noch schlechte fachliche Antwortqualität.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Infra

**Technischen Blocker gesondert ausweisen**

Verantwortung: Auswertung / Gegenprobe · BPMN-Typ: `serviceTask`

Betroffenen Fall und Fehler nennen; keinen bestandenen Lauf aus einem unvollständigen Ergebnis ableiten.
Quelle: ../pruefszenarien.md

#### P07_Qualitaet

**Gegen Sollkriterien und Gegenproben auswerten**

Verantwortung: Auswertung / Gegenprobe · BPMN-Typ: `serviceTask`

Automatisch prüfbare Eigenschaften mit Code, fachliche Aussagen mit Quellen und menschlicher Stichprobe. Saubere Fälle verhindern einen Prüfer, der einfach alles ablehnt.
Quelle: ../pruefszenarien.md

#### P07_Zusammen

**Zusammenführung**

Verantwortung: Auswertung / Gegenprobe · BPMN-Typ: `exclusiveGateway`

Technische Blocker und auswertbare Qualitätsbefunde fließen mit getrennten Status in den Bericht.
Quelle: ../pruefszenarien.md

#### P07_Bericht

**Befund mit Belegen vorlegen**

Verantwortung: Auswertung / Gegenprobe · BPMN-Typ: `serviceTask`

Bestanden, verletzt, offen und nicht ausgeführt unterscheiden. Keine bereits funktionierende Integration aus einem gezeichneten Prozess ableiten.
Quelle: ../../AGENTS.md

#### P07_Entscheidung

**Nächste Entwicklung oder Bereitstellung entscheiden**

Verantwortung: Testverantwortliche · BPMN-Typ: `userTask`

Adapteränderung erst auf Grundlage des Befunds und der geltenden Freigabe. Keine Freigabe durch bloße Existenz dieses Prozessmodells.
Quelle: ../../AGENTS.md

#### P07_Reset

**Teststand kontrolliert zurücksetzen**

Verantwortung: Testaufbau / Rechte / Messung · BPMN-Typ: `serviceTask`

Nur den eigenen Testlauf nach Sichtprüfung und Sicherung zurücksetzen. Gemeinsamen Stack und fremde Arbeit erhalten; benötigte Nachweise behalten.
Quelle: ../../beispiel/openwebui/fixtures/04-test-cases.md

#### P07_Ende

**Befund und wiederholbarer Startstand bereit**

Verantwortung: Testverantwortliche · BPMN-Typ: `endEvent`

Gleiche Eingaben und Startzustände sind wiederherstellbar. Sprachmodellantworten müssen deshalb nicht bytegleich sein.
Quelle: ../pruefszenarien.md

### Übergänge

| Kennung | Von | Nach | Bedingung / Zweig |
|---|---|---|---|
| `P07_Flow_Start_Plan` | `P07_Start` | `P07_Plan` | — |
| `P07_Flow_Plan_Manifest` | `P07_Plan` | `P07_Manifest` | — |
| `P07_Flow_Manifest_Aufbau` | `P07_Manifest` | `P07_Aufbau` | — |
| `P07_Flow_Aufbau_Grenzen` | `P07_Aufbau` | `P07_Grenzen` | — |
| `P07_Flow_Grenzen_Sicher` | `P07_Grenzen` | `P07_Sicher` | — |
| `P07_Flow_Sicher_Sperre` | `P07_Sicher` | `P07_Sperre` | nein |
| `P07_Flow_Sicher_Normal` | `P07_Sicher` | `P07_Normal` | ja |
| `P07_Flow_Normal_Fehler` | `P07_Normal` | `P07_Fehler` | — |
| `P07_Flow_Fehler_Update` | `P07_Fehler` | `P07_Update` | — |
| `P07_Flow_Update_Messung` | `P07_Update` | `P07_Messung` | — |
| `P07_Flow_Messung_Ergebnis` | `P07_Messung` | `P07_Ergebnis` | — |
| `P07_Flow_Ergebnis_Infra` | `P07_Ergebnis` | `P07_Infra` | nein |
| `P07_Flow_Ergebnis_Qualitaet` | `P07_Ergebnis` | `P07_Qualitaet` | ja |
| `P07_Flow_Infra_Zusammen` | `P07_Infra` | `P07_Zusammen` | — |
| `P07_Flow_Qualitaet_Zusammen` | `P07_Qualitaet` | `P07_Zusammen` | — |
| `P07_Flow_Zusammen_Bericht` | `P07_Zusammen` | `P07_Bericht` | — |
| `P07_Flow_Bericht_Entscheidung` | `P07_Bericht` | `P07_Entscheidung` | — |
| `P07_Flow_Entscheidung_Reset` | `P07_Entscheidung` | `P07_Reset` | — |
| `P07_Flow_Reset_Ende` | `P07_Reset` | `P07_Ende` | — |
