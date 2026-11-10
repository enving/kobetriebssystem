# Szenarien und Bedarf für KoBetriebssystem (Entwurf)

**Einordnung, GPT-6.1-sol, 06.11.2026:** Zurück zum Bedarf aus Felix Schlenthers AI-FIRST-Artikeln und Tristans Einwand gegen isolierte Wissensinseln. Diese Seite beschreibt eine zu prüfende Anforderungshypothese, keine neue Betriebsregel und keine Auswahl einer Laufzeit. Zuständige Verhaltensregeln bleiben [AGENTS.md](../AGENTS.md), technische Grenzen [SICHERHEIT.md](../SICHERHEIT.md), Verteilung [installation/README.md](../installation/README.md), kritische Architekturfragen [recherche §4](recherche.md#architektur).

# An Tristan

1. Welcher erste echte Vorgang soll die Verbindung aus gemeinsamer Fähigkeit und übernommener Verbesserung zeigen? Die Prioritätsfrage wurde im Chat gestellt; eine Auswahl ist noch offen. Vorschlag (Opus 5.5, 06.11.): „Besprechung nachbereiten“ als MVP, siehe [PRD §6](../PRD.md).

## 1. Der gemeinsame Gedanke

Felix beschreibt im März Fähigkeiten, Kontext, Governance und Feedback als gemeinsam gepflegte Systembausteine, aus denen sich Ausführende je Aufgabe bedienen. In der November-Fassung liegt das Steuernde als Text in Git; Korrekturen werden zu geprüften Vorschlägen für gemeinsam verwendete Dateien. Das ist seine dokumentierte Vorgehensweise, kein Nachweis allgemeiner Überlegenheit gegenüber anderen Architekturen. [Fünf Bausteine, 08.03.2026](https://ai-first.ai/insights/die-5-bausteine-unseres-ki-betriebssystems), [Version 2, 01.11.2026](https://ai-first.ai/insights/ai-first-ki-betriebssystem-2-0)

**Unsere Ableitung:** KoBetriebssystem soll Fähigkeiten und Verbesserungen wiederverwendbar machen. Wie viele Agentenprozesse laufen oder wie deren Fenster aussehen, entscheidet diese Frage nicht. Ein gemeinsamer fachlicher Ausgangsstand kann in vielen getrennten Sitzungen verwendet werden. Die Formulierung eines einzigen Agenten im Artikel erzwingt keinen einzigen Serverprozess für alle Mitarbeitenden.

In der letzten Recherche sind wir zu schnell von diesem Bedarf zur Verwaltung benannter Bots und zu Plattformkombinationen gesprungen. Die Erkenntnisse bleiben nützlich; die dortige Empfehlung Pi/OpenShell plus Prüfung von Paperclip ist aber kein nächster Schritt unabhängig vom hier geklärten Bedarf.

## 2. Zusammenarbeit, Gedächtnis und Lernen unterscheiden

| Ebene | Was gemeinsam sein sollte | Was daraus nicht folgt |
|---|---|---|
| Firmenweite Fähigkeiten | Freigegebene Skills, allgemeine Regeln, Prüffälle und Verweise aus den zuständigen Quellen | Alle Mitarbeitenden dürfen dieselben Fach- oder Personaldaten lesen |
| Abteilungs-/Projektwissen | Ein gemeinsam nutzbarer aktueller Arbeitsstand im berechtigten Kreis | Alle Rohchats oder persönlichen Vorlieben werden Firmenwissen |
| Zusammenarbeit an einem Auftrag | Benannte Zuständigkeit, gemeinsame zulässige Artefakte, Status, Nachrichten und ein definierter Übergabepunkt | Alle Beteiligten benötigen denselben Rechner oder uneingeschränkte gegenseitige Shellrechte |
| Persönlicher Kontext | Rolle, bestätigte Präferenzen und private Vorgänge der Person | Persönliche Korrekturen werden ohne Entscheidung zu Firmenregeln |
| Gemeinsame Verbesserung | Geeignete Korrektur → Vorschlag → zuständige Freigabe und Prüfung → neuer gemeinsamer Quellstand | Ein langes Chatgedächtnis oder ein geteiltes Laufwerk verbessert automatisch alle Ausführungen |

**Arbeitsräume dürfen getrennt sein und trotzdem zusammenarbeiten.** Im gleichen berechtigten Projekt kann ein gemeinsamer Aufgabenstand verwendet werden. Zwischen unterschiedlichen Berechtigungskreisen werden gezielt erlaubte Ergebnisse übergeben. Neue allgemeine Erkenntnisse nehmen den geprüften Rückweg in die zuständige Quelle. Der Bedarf ist dieser Zusammenhang; die genaue technische Umsetzung bleibt offen.

**Lernen heißt hier:** Die wiederverwendbaren Dateien und gegebenenfalls fachlichen Prüfungen werden verbessert. Eine Nachricht an einen anderen Bot ist zunächst Kommunikation. Ein gespeicherter Chat ist zunächst Gedächtnis. Beides kann Material für eine Verbesserung liefern, ersetzt aber deren Einordnung, Freigabe und Bereitstellung nicht. Es wird kein Training von Modellgewichten vorausgesetzt.

## 3. Was eine passende Lösung im Alltag leisten müsste

Die folgenden Punkte sind Vorschläge für die Abnahme, keine zusätzlich geltenden Regeln:

| Bedarf | Beobachtbares Ergebnis |
|---|---|
| Einfach Arbeit übergeben | Eine Person formuliert eine Aufgabe; sie muss keinen Spezialbot und keinen Skill-Namen kennen. Ergebnis, offene Entscheidung und laufende Arbeit sind erreichbar. |
| Gemeinsame Fähigkeiten verwenden | Zwei neue Sitzungen wählen für passende Aufgaben den gleichen freigegebenen Skill-Stand; persönliche und bereichsspezifische Ergänzungen bleiben möglich. |
| Kontext passend auswählen | Jede Ausführung kann zeigen, welche Quellen und Versionen sie verwendet hat; fehlender Zugriff wird sichtbar. Ein großer gemeinsamer Kontextdump ist keine Voraussetzung. |
| An einem Auftrag zusammenarbeiten | Beteiligte sehen den zulässigen Arbeitsstand und können eindeutig übernehmen. Bei Delegation geht weder Ergebnis noch Zuständigkeit verloren. Ein zweiter Agent ist nur dort nötig, wo er erkennbaren Nutzen bringt. |
| Gemeinsam besser werden | Eine bestätigte allgemeine Korrektur wirkt in einer frischen berechtigten Sitzung; die privaten Ausgangsdaten tauchen dort nicht auf. |
| Ohne offenen Browser weiterarbeiten | Eine freigegebene Routine kann laufen, auf eine Entscheidung warten und danach nachvollziehbar fortsetzen. Abbruch und Wiederholung haben überprüfbare Folgen. |
| Betreibbar bleiben | Pflegeaufwand, fachliche Nacharbeit und ausgebliebene/doppelte Arbeit sind erkennbar. Die Erweiterung spart im realen Vorgang mehr Aufwand, als sie verursacht. |

Technische Sicherheits-, Rollout- und Wiederanlaufprüfungen stehen bereits im [Laufzeitvergleich](architektur/laufzeitvergleich-2026-11-05.md#ein-nützlicher-prüffall-und-sechs-abnahmetore). Sie bleiben relevant, belegen allein aber noch keinen guten gemeinsamen Arbeitsprozess. Die bisherigen Aussagen im Artikel über sofort überall gültige Updates und reibungslose Portabilität übernehmen wir nicht als technische Zusage; Installation, bestehende Sitzungen und Rechte müssen im Zielsystem geprüft werden.

## 4. Ein aussagekräftiger Durchlauf

**Vorschlag, noch nicht ausgeführt:** Zwei getrennte Sitzungen A und B verwenden denselben freigegebenen Skill für die Nachbereitung einer Besprechung mit synthetischen Daten.

1. A erstellt einen Aufgabenentwurf mit Zuständigkeiten, Terminen und Quellen. Eine absichtlich unklare Zuständigkeit darf nicht erfunden werden.
2. Der Mensch korrigiert ein allgemeines Muster, etwa wie unsichere Terminangaben im Entwurf gekennzeichnet werden sollen. Zunächst wird geprüft, ob das einmalig, persönlich, projektspezifisch oder tatsächlich allgemeingültig ist.
3. Für eine allgemeine Änderung entsteht ein Vorschlag an der vorhandenen Skill-/Kontextquelle mit geeignetem Prüffall. Die im Repo vorhandene Lernschleife entscheidet über die Übernahme; die Demo gibt sich keine eigenen Freigaberechte.
4. B startet frisch mit anderem synthetischem Inhalt und der freigegebenen neuen Version. Sie berücksichtigt die Änderung ohne Zugriff auf As private Notiz oder Gesprächshistorie. Ein Marker aus As privatem Bereich darf nicht in Bs Ergebnis vorkommen.
5. Separat kann B einen zulässigen Teil desselben Projektauftrags übernehmen. Das prüft Zusammenarbeit, nicht die allgemeine Lernschleife.

**Bestanden:** Die bestätigte Verbesserung kommt bei B an, ein unberechtigter Inhalt nicht; Quelle und Version sind nachweisbar. Beim Delegieren gibt es genau einen nachvollziehbaren Auftrag und ein übernehmbares Ergebnis. Vergleich mit dem bisher interaktiven Vorgehen: weniger erneute Erklärung und fachliche Reparatur. Noch keine Zahlen für Zeitersparnis behauptet.

**Noch offen:** Welcher erste echte Vorgang den synthetischen Durchlauf ersetzen soll. Zur Auswahl stehen derzeit ein interaktiver Arbeitsassistent, ein längerer gemeinsamer Auftrag oder eine wiederkehrende Hintergrundroutine. Diese Priorisierung ist keine Folge der vorhandenen Werkzeuge und noch nicht entschieden.

## 5. Wo die zuletzt genannten Werkzeuge einzuordnen sind

### OpenWebUI und Terminals

Die aktuelle OpenWebUI-Doku beschreibt mehr als Chat: Subagenten und Hintergrundarbeit sind vorhanden. Terminals stellt Arbeitsräume je Person und Richtlinie bereit, optional enger je Chat oder Automation. **Daraus folgt keine automatische gemeinsame Lernschleife.** Unterschiedliche Räume können denselben freigegebenen Skill-Stand bekommen und über geeignete Projektartefakte zusammenarbeiten; genau diese Verbindung wäre zu belegen. Für produktiven Einsatz nennt Terminals ausdrücklich eine Enterprise-Lizenz. Ein synthetisches Prüfset liegt unter [`beispiel/openwebui/`](../beispiel/openwebui/README.md); tatsächliche Modell-, Mehrbenutzer- und Terminalprüfungen sind damit noch nicht belegt, und es wird keine Lizenz vorausgesetzt. [Subagenten](https://docs.openwebui.com/features/chat-conversations/chat-features/subagents/), [Terminals](https://docs.openwebui.com/features/open-terminal/terminals/)

Open WebUI Computer ist ein anderer Baustein: Der vorhandene Gateway macht einen Computer-Workspace als Modell wählbar, synchronisiert aber weder Nutzer noch Wissensbasis, Tools oder Prompts. Gateway-Aufträge laufen ohne einzelne Werkzeugbestätigungen. Computer beschreibt sich als gemeinsamer Vertrauensbereich, nicht als Isolation unterschiedlicher Nutzer. Deshalb kein stiller Ersatz für die Berechtigungs- und Freigabeanforderungen. [Gateway](https://docs.openwebui.com/ecosystem/computer/automate/open-webui/), [Sicherheitsmodell](https://docs.openwebui.com/ecosystem/computer/phone-and-remote/security/)

### OpenRig und das verlinkte Video

Gesichtet: englische Untertitel und acht über das Video verteilte Standbilder, zusätzlich die offizielle Repo-/Sicherheitsdoku; keine Installation und kein eigener Agententeam-Test. Die Bildabdeckung des rund zwanzigminütigen Videos ist begrenzt.

Im Video werden eine Auftragsqueue und Übergaben erläutert (ab 07:54), ein gemeinsamer Arbeitsordner als Gedächtnis (ab 09:06), Wecken wartender Agenten (ab 11:50) und teilbare Team-Konfigurationen (ab 14:19). Bei 07:32 begründet der Autor selbst eine Hierarchie, bei 10:52 bezeichnet er das ganze Team für den einzelnen Bug als überdimensioniert. Die Aussage „Agenten arbeiten nicht in Hierarchien“ wird durch dieses Video somit nicht gestützt. [Video mit Einstieg bei 07:32](https://www.youtube.com/watch?v=qccsfUnrQ9w&t=452s)

Das passt zu Zusammenarbeit über längere Aufträge. Die Übertragung einer allgemeinen fachlichen Korrektur auf alle berechtigten Arbeitsassistenten wird damit noch nicht demonstriert. Ein RigBundle verteilt die Team-Konfiguration; aus dieser Funktion allein folgt kein kontrollierter Verbesserungsprozess. OpenRig ist laut eigener Sicherheitsdoku für eigene Maschinen und vertrauenswürdige private Netze gedacht und verändert auch Harness-Konfigurationen und Hooks. [Repo](https://github.com/mvschwarz/openrig), [Sicherheitsmodell](https://github.com/mvschwarz/openrig/blob/main/SECURITY.md)

### Paperclip und Microsoft

Paperclip bleibt eine Alternative für Aufgaben- und Agentenverwaltung. Unsere Kritik sollte am tatsächlichen Mehraufwand der Aufgabe ansetzen: Braucht dieser Vorgang wirklich dauerhafte benannte Agenten und eine Hierarchie? Eine generelle Aussage über die natürliche Arbeitsweise aller Agenten ist hier nicht belegt. Die technische Recherche steht im [Vergleich](architektur/laufzeitvergleich-2026-11-05.md#2-paperclip-vor-einem-eigenen-manager-prüfen); daraus wurde keine Pflicht für KoBetriebssystem.

Microsoft liefert passende Teilfunktionen: Foundry Hosted Agents betreibt eigenen Agentencode einschließlich Zustand und Sitzungen auf Microsoft-Infrastruktur. Agent 365 verwaltet und beaufsichtigt Agenten. Das ist eine Alternative für Ausführung und Administration; es beweist noch keinen gemeinsamen fachlichen Lernprozess. Bei einer vermittelten Anbindung müssen Identitäten und Sitzungen korrekt zugeordnet werden; ein gemeinsamer API-Zugang ist dafür keine hinreichende Lösung. [Hosted Agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents), [Sitzungen je Nutzer](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/isolate-sessions-per-user), [Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/overview)

**Folge für die Auswahl, GPT-6.1-sol, 06.11.2026:** Zuerst den gemeinsamen fachlichen Durchlauf nachweisen. OpenWebUI ist dafür eine zu prüfende Oberfläche, OpenRig eine zu prüfende Zusammenarbeitsschicht. Pi, OpenShell, Paperclip und Microsoft bleiben mögliche technische Mittel. Es wird keine Kombination aus allen Bausteinen vorausgesetzt. Vor der Auswahl muss klar sein, welcher vorhandene Weg die benötigte Strecke mit dem geringsten zusätzlichen Betrieb tatsächlich trägt.

## 6. Frühere Ortsvarianten

Die ursprüngliche Tabelle bleibt als historische Skizze erhalten. Sie ist keine Funktionsprüfung der genannten Produkte und keine Zusage zu Rechten oder Datenhaltung.


| | A Lokal (Claude Code je Mitarbeiter) | B Zentral (Cloud-Agent, z. B. Slack) | C Gemischt |
|---|---|---|---|
| Rechte | erbt die des Nutzers (Shell/Konnektoren) | explizit vergeben, Dienstkonto | je Aufgabe |
| Eigene Skills/Prompts | ja, `persoenlich/` | nur zentrale | beides |
| Logbuch | beim Mitarbeiter | zentral | geteilt |
| Datenschutz/Endgerät | Daten lokal → klären | Daten in Cloud → AVV | ? |
| Automatisierung | persönliche Routinen über die Zeitplanfunktion der App (läuft in der Cloud, aber als Person) | gut (Zeitplan/Ereignis) | Routinen zentral |
| Konto einer Routine | Person: passt für persönliche Routinen | eigenes Konto: Pflicht für zentrale Routinen (Rechte-Leck, [recherche §3](recherche.md)) | je Auftrag festlegen |
| Offen | | | |
