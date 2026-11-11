# Abgleich mit „KI-Betriebssystem 2.0“: was der Artikel festlegt, was fehlt, welche Werkzeuge passen

**Einschätzung Claude Opus 5.5, 06.11.2026. Entschieden ist nichts.** Grundlage: Felix Schlenther,
[AI FIRST KI-Betriebssystem 2.0](https://ai-first.ai/insights/ai-first-ki-betriebssystem-2-0) (01.11.2026), gelesen über
Tristans Clipping vom 04.11. mit seinen Anmerkungen. Diese Seite wiederholt nichts, was schon an anderer Stelle steht, sie
verweist darauf: Bedarf in [szenarien.md](../szenarien.md), Architekturprüfung in [recherche §4](../recherche.md#architektur),
Ebenen und Arbeitsentscheidungen im [Bericht vom 05.11.](bericht-2026-11-05.md), Abnahmetore im
[Laufzeitvergleich](laufzeitvergleich-2026-11-05.md#ein-nützlicher-prüffall-und-sechs-abnahmetore).

# An Tristan

1. Soll die Architekturbeschreibung schrittweise nach arc42 gegliedert werden (§3)? Oder bleibt es bei datierten Berichten?
2. Soll das Kriterium für den Abbau der Freigabe (§2, Lücke 8, im Register L13) in die Auftragsvorlage? Das ändert
   Freigaberegeln, das entscheidest du.

Die frühere Frage nach dem isolierten Eval-Lauf in Issue #4 ist in die [PRD](../../PRD.md) gewandert (Frage 2 dort): erst
das MVP mit leerem Konfigurationsordner, Sandcastle nur bei Bedarf.

## 1. Was der Artikel festlegt, und wie ich ihn lese

Der Artikel beschreibt eine **logische** Architektur: ein Agent, vier Bausteine (Skills, Kontext, Tools, Regeln), zwei
Schleifen (Automatisierungen, Lernschleife), dazu Prüfer-Agent, Evals, Logbuch, OS-Check und Slack als Rückkanal. Fest steht
auch, wo das Steuernde liegt: als Text in GitHub, jede Änderung als PR, verteilt als Plugin der Claude-App. Diese Bausteine
bildet die Vorlage schon ab (README, Abschnitt „Wegweiser“).

Meine Lesart: Implizit beschreibt der Artikel drei Ebenen.

- **Steuerung:** das Repo mit Grundregeln, Skills und Evals, Wiki samt Index und Landkarte, Aufträgen, Ampel und Hooks.
  Änderungen nur als PR, Regeln gibt nur ein Mensch frei.
- **Ausführung:** mehrere Instanzen derselben Agenten-Definition, nämlich der Chat je Person, Läufe im Hintergrund, der
  Prüfer und der Eval-Lauf. „Ein einziger Agent“ ist eine Rolle, kein Prozess ([szenarien §1](../szenarien.md)).
- **Daten:** die Tools mit ihren eigenen Rechten. Dort bleibt alles Laufende.

Für die Steuerung ist das dasselbe Muster wie GitOps: Der gewünschte Stand liegt in Git, und eine Auslieferung bringt ihn je
Zielsystem in Form. Die Vorlage hat das als Grundsatz „laufzeitneutral, die Pipeline übersetzt je Zielformat“
([Bericht §10.1](bericht-2026-11-05.md)).

## 1a. Wo „der eine Agent“ läuft (Nachtrag 06.11., auf Tristans Frage)

Tristan, 06.11.: „läuft dieser ‚eine agent‘ aus dem artikel wo? … jeder mitarbeitende hat zusätzlich seine eigenen agenten
… wie kommen denn dinge zurück an den agenten von den mitarbeitenden“. Gegenüberstellung, Zitate aus dem Artikel:

| Frage | Der Artikel sagt | Der Artikel sagt nicht | Unsere Lesart (Opus 5.5) |
|---|---|---|---|
| Wo läuft er? | „Claude in der App, Claude Code und unsere Automatisierungen in der Cloud lesen dieselben Dateien.“ | auf welcher Plattform die Automatisierungen laufen | Es gibt keinen zentralen Prozess. Jede Person hat ihre eigene Sitzung, dazu kommen Läufe in der Cloud. |
| Womit startet er? | „Beim Start liest der Agent nur wenige Dateien: unsere Grundregeln, zwei Verzeichnisse unseres Wissens und die persönlichen Anweisungen der Person, für die er arbeitet“ | wo die persönlichen Anweisungen liegen | bei der Person, nicht im Firmen-Repo ([PRD](../../PRD.md) L3) |
| Mit welchen Rechten? | „Jede Person meldet sich dort einmal mit ihrem eigenen Konto an und danach arbeitet der Agent mit genau den Rechten dieser Person.“ | unter welchem Konto die Kontext-Ernte Meetings, Slack und Notion liest | L1 |
| Wie kommt die Steuerung hin? | „Für das Team packen wir alles in ein Plugin für die Claude-App. … nach jeder Änderung aktualisiert es sich von selbst.“ | wie Regeln ohne Repo in die Sitzung kommen; Zuschnitt je Rolle | L2, L4, L5, L6 |
| Wie kommt etwas zurück? | „Sage ich ja, wird daraus ein Änderungsvorschlag in GitHub.“ Fürs Wiki sagen Menschen dem Agenten „Fürs Wiki: …“. | ob Mitarbeitende GitHub-Zugang haben; wo das Logbuch liegt; woher der OS-Check die Korrekturen der Woche nimmt | L8, L12 |
| Wie meldet er sich im Hintergrund? | „erreicht er uns über Slack“; „wir … antworten einfach auf die Slack-Nachricht“ | wie eine Antwort in Slack einen wartenden Lauf fortsetzt | L15 |
| Wer sind die anderen Agenten? | „Ein zweiter, unabhängiger Agent prüft jedes Ergebnis“; „Ein frischer Agent, der nichts außer dem Skill und dem Fall kennt“ | ob das Unteragenten oder eigene Läufe sind | Hilfsläufe derselben Software mit absichtlich wenig Kontext |

**Hat jede Person zusätzlich eigene Agenten?** Ja, in zwei Bedeutungen. Jede Person betreibt ihre eigene Instanz der
gemeinsamen Agenten-Definition. Und es gibt „persönliche und abteilungsspezifische Skills, die nur einzelne für sich nutzen“.

**Haben Mitarbeitende über ihr Claude Code Zugriff auf den Agenten?** Nein, so beschreibt es der Artikel nicht. Sie greifen
nicht auf einen Agenten zu, sie betreiben selbst eine Instanz. Zentral liegt nur das Repo. Zurück fließen Pull Requests,
Einträge in den Tools (Entwürfe, CRM) und Nachrichten in Slack. Ob alle Mitarbeitenden dafür Zugang zu GitHub brauchen, lässt
der Artikel offen; in dieser Vorlage widerspricht es dem gefilterten Paket (L8).

**„Ein Agent“ und trotzdem Prüf- und Eval-Agenten:** Der Artikel nutzt „Agent“ in zwei Bedeutungen. Einmal ist es die eine
Definition, mit der alle arbeiten. Dann sind es Hilfsläufe mit einem bewusst kleinen Kontext. In Claude Code sind das
Unteragenten mit eigenem Kontextfenster oder getrennte Läufe.

## 2. Was der Artikel offen lässt

Der Artikel schweigt fast ganz dazu, **wo** etwas läuft, **unter wessen Identität** es läuft und **wohin Informationen
fließen**. Das sind genau die Stellen, an denen Tristans Anmerkungen nachfragen.

Die zwölf Lücken dieser Seite führt seit dem 06.11. das **Lückenregister der [PRD](../../PRD.md) (§9)**, dort mit Status,
MVP-Bezug und wer entscheidet. Zuordnung: 1 → L1 (Identität der Hintergrundläufe), 2 → L6 (Leserechte in der Steuerung),
3 → L7 (Informationsfluss), 4 → L12 (Datenbasis des OS-Checks), 5 → L15 (Routinen), 6 → L11 (frische Evals), 7 → L5
(Versionen), 8 → L13 (Freigabe abbauen), 9 → L9 (Endgeräte), 10 → L16 (Personenbezug, Mitbestimmung), 11 → L14 (Nutzen
messen). Lücke 12 (Fachbegriffe) ist in der Vorlage gelöst (`kontext/glossar/`, `AGENTS.md` Regel 8).

**Neu gegenüber den vorhandenen Seiten:**

- **Zu 4.** Für „ab drei gleichen Fällen“ braucht es eine Zählung über Personen hinweg. Vorschlag: Der Logbuch-Eintrag mit
  Inhalt bleibt im Arbeitsbereich der Person. Zentral landen nur Skill, Muster-Kennung und „einmalig/Regel“, etwa als Zähler
  an einem Issue. Damit lässt sich zählen, ohne Chats oder Inhalte zu sammeln. Ein Zähler ohne Personenbezug ist auch für die
  Mitbestimmung leichter.
- **Zu 6.** Ein Eval am eigenen Rechner ist nicht frisch: Claude Code lädt die persönliche `CLAUDE.md`, Hooks, Skills und
  Memory mit, und das verfälscht das Ergebnis. Abhilfe ist eine Umgebung ohne persönliche Konfiguration. Sandcastle gibt jedem
  Lauf ein leeres Home und lässt nur das Repo beschreiben; alternativ ein eigener `CLAUDE_CONFIG_DIR`. Die
  `AGENTS.md` des Repos soll dabei mitgelesen werden, denn sie gehört zum geprüften Stand.
- **Zu 8.** Vorschlag für ein Kriterium, Werte sind Platzhalter: Die Freigabe eines Ablaufs entfällt nur, wenn alle Evals
  bestehen und die letzten *n* Läufe ohne inhaltliche Korrektur blieben. Eine inhaltliche Korrektur oder ein fehlgeschlagener
  Eval schaltet die Freigabe automatisch wieder ein. Rot bleibt rot. Den Wechsel beschließt der Prozessverantwortliche per PR
  am Auftrag (`automatisierungen/_vorlage.md`, Feld „Status“). Das ist „human on the loop“ mit Rückfall.

## 3. Wie ich die Architekturbeschreibung ergänzen würde

Vorschlag: **arc42** als Gliederung. Die Vorlage ist frei nutzbar und im deutschsprachigen Raum verbreitet. Bilder nach C4
(Kontext, Container), Entscheidungen als kurze ADRs. Der Artikel füllt davon §5 (Bausteine) und einen Teil von §6 (Abläufe).
Die neue Gliederung verweist auf die vorhandenen Quellen und kopiert sie nicht.

| arc42 | vorhanden | fehlt |
|---|---|---|
| 1 Ziele | README „Warum“, [szenarien §3](../szenarien.md) | – |
| 2 Randbedingungen | README (AI Act), SICHERHEIT | – |
| 3 Kontextabgrenzung | – | Akteure (Mitarbeitende, Prozessverantwortliche, Bereichsbesitzer, OS-Betreuung, Betriebsrat und Datenschutz, Externe) und Nachbarsysteme (Tools, Modellanbieter, Identität) |
| 4 Lösungsstrategie | Bericht §4 und §10.1 | – |
| 5 Bausteine | README „Wegweiser“ (entspricht dem Artikel) | – |
| 6 Abläufe | README „Wie eine Aufgabe läuft“ | Routine wartet auf Antwort; Lernschleife über Sitzungen; Eval-Lauf |
| 7 Verteilung | – | was läuft wo: Gerät, App, Hintergrundlauf, CI, Rakazo oder Microsoft |
| 8 Querschnitt | verstreut: SICHERHEIT, recherche §4 | Identität, Rechte, Datenklassen, Protokoll, Evals an einer Stelle bündeln |
| 9 Entscheidungen | Bericht §9–11 | als ADR-Liste mit Status |
| 10 Qualität | szenarien §3, Abnahmetore im Laufzeitvergleich | – |
| 11 Risiken | SICHERHEIT §3, recherche §4 | – |
| 12 Glossar | `kontext/glossar/` (Firmenbegriffe) | Architekturbegriffe |

Zuerst §7 und §8, weil der Artikel dort schweigt und die Lücken 1–3 dort hingehören. Danach die ADR-Liste aus dem Bericht.

**Was „kompatibel“ heißt:** Eine Ausführungsschicht passt zur Architektur des Artikels, wenn sie drei Bedingungen erfüllt.
(a) Sie liest ihre Anweisungen aus dem Stand in Git oder aus einem daraus erzeugten Paket. (b) Sie arbeitet mit den Rechten
der Person oder mit ausdrücklich zugeteilten Rechten. (c) Änderungen an der Steuerung entstehen bei ihr nur als PR mit
menschlichem Ja.

## 4. Die geprüften Werkzeuge gegen diese drei Bedingungen

Quellen, gelesen am 06.11.2026: [Laufzeitvergleich §2](laufzeitvergleich-2026-11-05.md) für Paperclip;
[Archon](https://github.com/coleam00/Archon) v0.13.2 (hier installiert), [Sandcastle](https://github.com/mattpocock/sandcastle)
v0.14.0 (`docs/guide/`), [AI Software Factory](https://github.com/coleam00/ai-software-factory) (README, ohne Lizenz) und
[OpenRig](https://github.com/mvschwarz/openrig) v0.7.8 (README und `SECURITY.md`).

Die Bewertung je Werkzeug gegen (a) bis (c) und gegen die übrigen Anforderungen im Repo steht seit dem 06.11. in einer
einzigen Tabelle: [PRD §8](../../PRD.md).

Ergebnis: Kompatibel sind **Archon und Sandcastle**, und zwar als Werkzeuge der OS-Betreuung, nicht für Mitarbeitende. Das
deckt sich mit Bericht §9 (Archon als OS-Werkstatt). Neu ist Sandcastle als Antwort auf Lücke 6. Für die Ebene der
Mitarbeitenden bleibt die Frage bei der Oberfläche (Rakazo, Claude-App mit Plugin, Microsoft). Paperclip wäre dort der einzige
der fünf Kandidaten und hängt am Prüfstein 1 aus dem Laufzeitvergleich.

## 5. Vorschlag: nächster Schritt

**Abgelöst am 06.11. durch das MVP in der [PRD](../../PRD.md) §6:** erst der Kernkreislauf mit Claude Code, Plugin, Git und
Prüfskript, Evals mit leerem Konfigurationsordner; Sandcastle und Archon kommen nach §7 dort erst bei nachgewiesenem Bedarf.
Der frühere Vorschlag bleibt zur Nachvollziehbarkeit stehen:

Die Prüfung aus Issue #4 (Archon für Skill-Prüfläufe) um einen Fall erweitern: die drei Evals eines Beispiel-Skills isoliert
in Sandcastle laufen lassen, die Bewertung macht ein zweites Modell, Archon steuert den Ablauf, das Ergebnis landet in
`evals/ergebnisse.md`. Bestanden ist der Fall, wenn die persönliche Konfiguration nachweislich nicht mitläuft und das
Ergebnis aus dem Repo-Stand reproduzierbar ist. Abbruch wie in [recherche §3](../recherche.md): nicht als ein Ablauf
abbildbar, oder mehr als zwei Stunden bis zum ersten sauberen Lauf. Nicht ausgeführt.

**Nicht geprüft:** kein Lauf eines der Werkzeuge in diesem Repo. Die Bewertungen in §4 stützen sich auf Doku und READMEs.
