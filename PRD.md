# PRD: kobetriebssystem

**Entwurf, Claude Opus 5.5, 06.11.2026. Entscheiden tut Tristan; was er entschieden hat, steht unter „Entschieden“.**

Diese Datei ist für drei Dinge zuständig: was das Produkt leisten soll, was das erste MVP umfasst und welche
Architekturlücken offen sind (Lückenregister, §9). Regeln stehen weiter in [AGENTS.md](AGENTS.md), Sicherheit in
[SICHERHEIT.md](SICHERHEIT.md), Verteilung in [installation/README.md](installation/README.md), Recherche und Abwägungen
unter [docs/](docs/). Was dort steht, wird hier nicht kopiert, sondern verlinkt.

# An Tristan

Keine offenen Fragen. Deine Antworten vom 06. und 07.11. stehen darunter.

## Entschieden (Tristan, 06. und 07.11.2026)

1. **MVP-Vorgang „Besprechung nachbereiten“** (§6.2): „ja find ich gut“.
2. **MVP ohne Zusatz-Frameworks** (§6, §7): „ja“. **Rakazo ist zurückgestellt**: „rakazo zurück weil keine ahnung wir
   müssen besser wissen wie wir was aufteilen und möglichkeiten durchgehen“. Dauerhaft gilt: eine Sicht auf Produkte und
   Frameworks führen, „aber nicht zu früh annahmen dafür treffen eine konkrete auszuwählen“ (§8, Produktsicht).
3. **Regeln des Lückenregisters** (§9.1): „ok“. Klarstellung: Am 05.11. hat Tristan technische Entscheidungen an die
   Agenten gegeben („I don't make these decisions, you should make them“). Dass Agenten damit Architekturlücken schließen,
   hat er nicht gesagt (06.11.). Die frühere Frage hier unterstellte einen Widerspruch, den es nicht gab; §9.1 Regel 5
   beschreibt die Abgrenzung.
4. **Zwei weitere Lücken** von Tristan: Software auf den Endgeräten (L23) und unvollständiger Kontext (L24).
5. **Testgerät:** Der Laptop ist im MVP das Gerät eines Mitarbeitenden; dort wird das Claude-Plugin geübt (§6.3 Nr. 6):
   „mit dem laptop sollten wa auch trainieren für sen adapter / plugin für claude“.
6. **Zweiter Adapter: Hermes** (§6.3 Nr. 9): „Als beispiel könnten wir im mvp das betriebssystem als adapter statt
   wie angeavht claude vllt eher mit slack verbinden der in slack angebunden ist. Der hermes läuft auf einem server von
   [Name].“ Repo und Zugang fragt Tristan beim Kollegen an. Kurz darauf: „Ah atimmt der hat nur claude. Hm mist ja
   dann installier da vllt hermes? Dann können wir da frei ausprobieren?“ Hermes kommt deshalb zuerst als eigene
   Installation auf den Laptop; Slack und der Server des Kollegen sind der nächste Schritt.
7. **Codex auf dem Laptop:** „Und auf dem laptop ist codex / chatgpt im plus abi dh da können eir auchngut testen den
   adapter“. Damit lassen sich ein dritter Adapter (Codex) und Hermes über den Anbieter `openai-codex` mit diesem Konto
   testen. Ob der Anbieter die Nutzung des Abos durch Drittwerkzeuge erlaubt, ist nicht geprüft.
8. **Mehrere Agenten neben dem persönlichen** (07.11., Vorschlag, keine Entscheidung): „Der hermes oder codex etc ist ja
   der agent eines mitarbeiters gell? Ich würde sagen dass daneben auch noch andere agenten sind … dafür würde ich pi
   agent vorschlagen als harness und pi durable“. Neue Lücke L25; Recherche zu Pi, pi-durable, DeepSeek Harness und
   Harness² in [harness-firmenagenten-2026-11-07.md](docs/architektur/harness-firmenagenten-2026-11-07.md). Messpunkt: Hermes verbrauchte für „hi“ rund 15.000 Tokens.
9. **Wer welchen Harness bekommt** (07.11.): „Ja kannst den mvp machen so … Also pi wegnehmen beim laptop. Das machen wir
   im sandcastle und ist eher für die firmen agenten oder halt deepseek. Für die mitarbeitenden orientieren wir uns an die
   massen tools wie codex und claude ggf etwas von microsoft zb copilot.. aber das auf parkplatz nicht zuviel jez
   reinnehmen.“ Also: Mitarbeitende arbeiten mit verbreiteten Werkzeugen (Claude, Codex); Firmen-Agenten wie der
   Änderungs-Prüfer laufen als Pi in Sandcastle am Mac, schon im MVP. DeepSeek Harness und Copilot liegen auf dem
   Parkplatz (§11). Rakazo bleibt zurückgestellt; die Rakazo-Issues tragen das Label „zurückgestellt“.

## 1. Problem

Firmen wollen KI so einsetzen, wie es der Artikel
[„KI-Betriebssystem 2.0“](https://ai-first.ai/insights/ai-first-ki-betriebssystem-2-0) beschreibt: ein Agent, der
Arbeitsweise, Wissen, Systeme und Regeln der Firma kennt und mit jeder Korrektur besser wird. Der Artikel legt fest, woraus
so ein System besteht. Er sagt kaum, wo etwas läuft, unter wessen Identität und wohin Informationen fließen
([Abgleich §1a und §2](docs/architektur/abgleich-ai-first-2026-11-06.md)). Wer diese Lücken nicht kennt, füllt sie, ohne es
zu merken. Dann bekommt über ein Plugin jeder alles, eine Routine liest mit den Rechten einer Person für alle, oder ein Agent
schreibt eine Regel, die niemand freigegeben hat.

Dazu kommt die Haftung. Wer Agenten für die eigene Firma zusammenstellt, wird nach dem AI Act schnell zum Anbieter (README,
„Warum es dieses Repo gibt“). Je genauer man hinsieht, desto mehr Pflichten kommen dazu: AI Act, ISO/IEC 42001,
Mitbestimmung, Datenschutz. Das Repo muss diese Tiefe sichtbar halten, ohne dass der Einstieg daran scheitert.

## 2. Lösung

Eine Vorlage, mit der eine Firma ihr KI-Betriebssystem nicht leer beginnt: Grundregeln, Ampel, Vorlagen für Skills und
Kontext, Prüffälle, Hooks, Verteilung als Plugin und eine Lernschleife über Pull Requests. Das Repo bleibt laufzeitneutral
([Bericht §10.1](docs/architektur/bericht-2026-11-05.md)). Den Anfang macht ein MVP, das den Kernkreislauf des Artikels mit
vorhandenen Mitteln einmal ganz durchläuft und jede Abkürzung als solche kennzeichnet.

Tristans Vergleichsbild (06.11.): etwas wie ein persönlicher Bot (Grok Bot), aber übertragbar für eine Firma.
Mitarbeitende arbeiten in ihrer gewohnten Umgebung, daneben laufen verschiedene Agenten, und eine gemeinsame
Firmenintelligenz lernt stetig dazu. Daraus folgen zwei Grundsätze:

- **Bausteine statt Plattform.** Firmen sollen nichts Neues als SaaS einkaufen müssen. Das Betriebssystem bleibt Text in
  Git und eine Pipeline, die daraus Pakete für die vorhandene Arbeitsumgebung baut: Plugin für Claude, Regeln und Skills
  für Codex, später Microsoft- oder Google-Umgebungen. Welche Zielformate es dort gibt, ist nicht geprüft (L4). Wo eine
  Umgebung etwas nicht kann, schlägt die Vorlage einen Baustein vor, statt ihn vorauszusetzen.
- **Wenig Frameworks.** Ein Werkzeug kommt erst dazu, wenn eine Lücke es erzwingt (§7). Die Sicht auf den Markt läuft
  weiter, ausgewählt wird spät (§8, Produktsicht).

## 3. Wie wir den Artikel lesen

Herleitung mit Zitaten: [Abgleich §1 und §1a](docs/architektur/abgleich-ai-first-2026-11-06.md). In Kürze:

- **„Ein Agent“ ist eine Definition, kein Prozess.** Alle arbeiten mit derselben Grundlage aus Regeln, Skills und Kontext.
  Jede Person startet aber ihre eigene Sitzung in der Claude-App oder in Claude Code, mit ihren eigenen Konnektoren und
  Rechten. Dazu kommen Läufe in der Cloud für die Automatisierungen.
- **Prüfer und Eval-Agent sind Hilfsläufe mit absichtlich wenig Kontext.** Der Prüfer kennt nur Ergebnis und Kriterien, der
  Eval-Agent nur Skill und Fall. Technisch sind das Unteragenten oder getrennte Läufe derselben Agenten-Software.
- **Hinweg und Rückweg sind getrennt.** Hin: Git → Plugin → Gerät. Zurück: Korrektur → Vorschlag → Ja → Pull Request. Läufe
  im Hintergrund melden sich über Slack. Einen zentralen Agenten, den Mitarbeitende ansprechen, beschreibt der Artikel nicht.

## 3a. Probe von innen: Tristan als ein Mitarbeitender

**Einschätzung Claude Opus 5.5, 06.11.2026.** Tristan arbeitet mit einem eigenen Aufbau, der die Bausteine des Artikels
für eine Person nachbildet (Bild: Folge 33, Folie 16, im privaten Kanal-Repo). Betrachtet man ihn als einen
Mitarbeitenden, sieht man, was die persönliche Ebene schon leistet und wo der Anschluss ans Betriebssystem fehlt.

| Baustein | bei Tristan heute | in der Vorlage | Anschluss fehlt |
|---|---|---|---|
| Grundregeln | eine globale Regeldatei, per Verknüpfung an Claude Code, Codex und Antigravity verteilt | `AGENTS.md` im Plugin | lädt über das Plugin nicht (L2); Vorrang bei Widerspruch (L3) |
| Skills | eigene Sammlung, 84 Skills | `.agents/skills/` je Rolle | Bewährtes über den Beitragsweg (L20) |
| Wissen | persönlicher Wissensgraph, Obsidian-Vault als Eingang, Projekt-Repos | `kontext/` mit Index und Landkarte | Ausschnitt für Agenten ([#22](https://github.com/enving/kobetriebssystem/issues/22), L21); Mail und Chat fehlen (L24) |
| persönliche Anweisungen | Person, Ziele, Grenzen; Startausgabe in jeder Sitzung | `persoenlich/`, künftig `user-kompass/` ([PR #23](https://github.com/enving/kobetriebssystem/pull/23)) | Ort auf dem Gerät (L3) |
| Logbuch | Verlauf im Wissensgraphen und je Repo | Logbuch je Person | Zähler je Muster für den OS-Check (L12) |
| Regeln per Technik | Hooks beim Sitzungsstart, bei jeder Eingabe und vor Werkzeugaufrufen | `system/hooks/` | über Plugin oder Managed Settings (L2) |
| Prüfer | einzelne Abläufe mit unabhängigem Prüf-Agenten | Prüfer im Plugin (§6.3 Nr. 3) | fest in jedem Skill-Lauf (L10) |
| Gesprächseingang | Sprachmemos mit Transkription, Clippings | Kontext-Ernte | Informationsfluss (L7) |
| Automatisierungen | Archon am Mac, Zeitpläne in T3 Code | `automatisierungen/` | Engine, Rückfrage, Fortsetzen (L15) |
| Tools | Mail über lokale Suche, Konnektoren, Mac-Programme | Konnektoren mit den Rechten der Person | L1, L23, L24 |
| Oberfläche | T3 Code, Claude Code, Codex, Vibe | Claude-App, Firmenchat o. Ä. | L4 |

**Was das Betriebssystem aus der Arbeit einer Person bekommt** (Vorschlag): nicht die Gespräche, sondern drei Dinge.

1. **Beitragskandidaten:** verallgemeinerte Korrekturen, bewährte Skills und Regeln, nach dem Ja der Person als PR
   (Beitragsweg, L20).
2. **Zähler:** je Skill und Muster „einmalig“ oder „Regel“, ohne Inhalt und ohne Personenbezug (L12). Daraus sieht das
   Betriebssystem, was bei vielen Personen wiederkehrt.
3. **Ergebnisse, die ohnehin in Firmensysteme gehören:** Issues, Entwürfe, Einträge in den Tools.

**Wie daraus Routinen werden:** Ein Skill, den viele Personen oft nutzen, der alle Prüffälle besteht und kaum noch
korrigiert wird, ist ein Kandidat für eine Routine. Den Vorschlag macht der OS-Check aus den Zählern, einschalten tut die
oder der Prozessverantwortliche (Tor 2 im [Bericht §9](docs/architektur/bericht-2026-11-05.md)). So erkennt das System
Routinen aus dem Gesamtbild, ohne Gespräche mitzulesen. Offen dafür: L12, L13, L15, L21.

## 4. Beteiligte

| Rolle | will | im Repo heute |
|---|---|---|
| Mitarbeitende | Aufgaben abgeben, ohne Skill-Namen oder Git zu kennen; Entwürfe mit „ok“ freigeben | README, „Wie eine Aufgabe läuft“ |
| Prozessverantwortliche | eine Routine einschalten, wenn sie trägt; Freigaben später abbauen | `automatisierungen/_vorlage.md` |
| Bereichsbesitzer | entscheiden, was im Wiki gilt | `kontext/`, README |
| OS-Betreuung | Vorschläge prüfen und mergen, Versionen ausrollen und zurücknehmen | `installation/` |
| IT | Plugin und Sperren auf die Geräte bringen | `installation/README.md` |
| Datenschutz, Betriebsrat | wissen, welche Daten wohin fließen und was protokolliert wird | `SICHERHEIT.md` §3 |
| Rechts- und Compliance-Stelle | Rolle nach AI Act klären, Nachweise prüfen | README, Tabelle zum AI Act |

## 5. User Stories

**MVP** heißt: Das MVP muss es zeigen. „später“ nennt die Lücke aus §9, an der es hängt.

Mitarbeitende

1. Als Mitarbeitende will ich eine Aufgabe in eigenen Worten stellen, damit ich keinen Skill kennen muss. **MVP**
2. Als Mitarbeitende will ich ein Ergebnis, das schon gegen die Kriterien geprüft ist, damit „ok“ oder eine kurze Änderung
   reicht. **MVP**
3. Als Mitarbeitende will ich, dass der Agent fragt statt erfindet, wenn etwas fehlt, damit ich dem Entwurf trauen kann. **MVP**
4. Als Mitarbeitende will ich, dass nichts ohne mich nach außen geht, auch wenn eine Notiz etwas anderes verlangt. **MVP**
5. Als Mitarbeitende will ich, dass meine Korrektur beim nächsten Mal auch bei Kollegen wirkt, ohne dass meine privaten
   Notizen mitwandern. **MVP**
6. Als Mitarbeitende will ich eigene Anweisungen haben, die nur bei mir gelten. **MVP** (eigene Skills: später, L3)
7. Als Mitarbeitende will ich sehen, mit welcher Fassung der Regeln mein Agent gerade arbeitet. **MVP**
8. Als Mitarbeitende ohne Terminal will ich dasselbe in der Claude-App oder im Firmenchat bekommen. später, L4

Prozessverantwortliche

9. Als Prozessverantwortliche will ich eine Routine erst einschalten, wenn ihre Prüffälle bestehen. später, L15
10. Als Prozessverantwortliche will ich Rückfragen einer Routine im Chat beantworten, und die Routine macht danach weiter.
    später, L15
11. Als Prozessverantwortliche will ich die Freigabe abbauen, wenn ein Ablauf trägt, und sie automatisch zurückbekommen,
    wenn er nicht mehr trägt. später, L13
12. Als Prozessverantwortliche will ich sehen, ob alle Routinen gelaufen sind. später, L15

Bereichsbesitzer

13. Als Bereichsbesitzer will ich „Fürs Wiki: …“ sagen, und der Agent pflegt es mit Quelle an der richtigen Stelle ein. später
14. Als Bereichsbesitzer will ich erinnert werden, wenn eine Datei ihr Prüfdatum überschritten hat. später
15. Als Bereichsbesitzer will ich Widersprüche vorgelegt bekommen, statt dass der Agent sie still auflöst. später

OS-Betreuung

16. Als OS-Betreuung will ich jeden Verbesserungsvorschlag als Pull Request mit Prüffall bekommen. **MVP**
17. Als OS-Betreuung will ich, dass vor dem Merge automatisch Struktur, Verweise und Vertraulichkeitsmarker geprüft werden.
    **MVP**
18. Als OS-Betreuung will ich Skills gegen ihre Prüffälle laufen lassen, ohne dass meine eigene Konfiguration das Ergebnis
    verfälscht. **MVP**, teilweise (L11)
19. Als OS-Betreuung will ich eine Version ausrollen und zurücknehmen und sehen, wer welche Version hat. **MVP**, lokal (L5)
20. Als OS-Betreuung will ich wiederkehrende Korrekturen über viele Personen erkennen, ohne Chats zu sammeln. später, L12
21. Als OS-Betreuung will ich wissen, welche Lücken offen sind und welche nur umgangen wurden. **MVP** (§9)

IT

22. Als IT will ich Plugin, Marketplace und Sperren zentral vorgeben, sodass niemand sie abschalten kann. später, L4
23. Als IT will ich je Rolle nur die passenden Skills und Kontexte verteilen. später, L6

Datenschutz, Betriebsrat, Compliance

24. Als Datenschutz will ich wissen, welche personenbezogenen Daten in Entwürfen, Logbuch und Vorschlägen landen. später, L16
25. Als Betriebsrat will ich, dass Zählungen für den OS-Check ohne Personenbezug auskommen. später, L12
26. Als Compliance-Stelle will ich die Spuren aus dem Betrieb (Verlauf, Prüfergebnisse, Logbuch) als Nachweise nutzen können.
    später, L18

## 6. MVP

### 6.1 Beweisfrage

Trägt der Kernkreislauf des Artikels mit Claude Code, einem Plugin aus diesem Repo, Git und einem Prüfskript, ohne ein
weiteres Framework? Und welche Lücken zeigen sich dabei konkret?

Kernkreislauf: Bitte → Agent wählt den Skill → Ergebnis → Prüfer → Entwurf → Mensch korrigiert → Einordnung → Vorschlag mit
Prüffall → Ja → Pull Request → Prüfung → Merge → neue Version → eine zweite Person nutzt in einer frischen Sitzung die
Verbesserung. Das ist der Durchlauf aus [szenarien §4](docs/szenarien.md), auf die kleinste Laufzeit gesetzt.

### 6.2 Vorgang

„Besprechung nachbereiten“: Aus einer Besprechungsnotiz entsteht ein Aufgabenentwurf mit Zuständigkeit, Termin und Quelle.
Nur erfundene Daten, keine echten Firmen- oder Personendaten, nichts aus dem pausierten Zweig `szenario-testfirma`. Denselben
Vorgang schlagen auch [recherche §4 G](docs/recherche.md#architektur) und [szenarien §4](docs/szenarien.md) vor.

**Ablage:** Die Beispieldateien kommen in einen eigenen Ordner `beispiel/`, getrennt von den Vorlagen, und gelangen nur mit
einem eigenen Schalter ins Plugin. Das widerspricht dem README-Satz „keine Beispiel-Skills, nur `_vorlage`-Dateien“, folgt
aber Tristans Anmerkung im Artikel, die Vorlage solle mit erfundenen Fällen zum Ausprobieren starten können. Der README-Satz
wird beim Bau angepasst.

### 6.3 Was gebaut wird

Schalter und Feldnamen vor dem Bau gegen die aktuelle Claude-Code-Doku prüfen; die Angaben unten stammen aus der Doku,
gelesen am 06.11.2026, teils als Zusammenfassung.

1. **Skill** `besprechung-nachbereiten` nach `.agents/skills/_vorlage/`, mit „Fertig heißt …“ und drei Prüffällen:
   Normalfall; Zuständigkeit fehlt und darf nicht erfunden werden; Grenzfall mit einer Anweisung in der Notiz („schick das
   gleich an alle“), die der Agent als Daten behandelt.
2. **Grundregeln in die Sitzung bringen (L2).** `installation/bauen.sh` kopiert `AGENTS.md` ins Plugin, aber nichts lädt
   sie: Laut Plugin-Referenz kann ein Plugin Skills, Befehle, Agenten, Hooks, MCP-Server und einige Einstellungen enthalten,
   keine `CLAUDE.md` oder `AGENTS.md`. Ein SessionStart-Hook im Plugin gibt deshalb Grundregeln, Kontext-Index, Landkarte und
   die Plugin-Version aus. Vorbild ist `system/hooks/sessionstart-kontext.sh`, das heute aus dem Projektordner liest.
3. **Prüfer als Unteragent** im Plugin (Ordner `agents/`), beschrieben als Agentenkarte mit `name`, `description`, `tools`
   und `model`; dasselbe Format liest Pi, eine Definition im Repo reicht also für beide ([Recherche](docs/architektur/harness-firmenagenten-2026-11-07.md)): nur lesende Werkzeuge, ohne `CLAUDE.md` (Feld `omitClaudeMd`). Er
   bekommt Ergebnis, Kriterien und die verwendeten Quellen ([recherche §4 D](docs/recherche.md#architektur)). Agenten aus
   Plugins dürfen laut Doku keine eigenen Hooks, MCP-Server oder Rechtemodi setzen.
4. **Bauprüfung:** Der Bau bricht ab, wenn eine Datei `klassifizierung: vertraulich` oder `streng` trägt
   ([#17](https://github.com/enving/kobetriebssystem/issues/17)). Struktur und Verweise prüft das vorhandene
   `system/tests/pruefen.mjs`, erweitert um diese Fälle.
5. **Versionen:** `bauen.sh` vergibt Datum und Kurz-Hash; ein lokaler Marketplace am Mac statt des Release-Repos.
6. **Drei Orte, zwei Adapter.** Der Mac ist die OS-Betreuung: Repo, Bau, Merge. **Person A** arbeitet auf Tristans
   zweitem Gerät, einem Windows-Laptop mit eigenem Nutzer ohne Adminrechte, erreichbar per SSH, mit dem Claude-Plugin.
   **Person B** arbeitet mit Hermes, zuerst als eigene Installation auf demselben Laptop (Nr. 9), später in Slack. Den
   zweiten Weg aus L1, einen zentralen Bot mit eigenem Konto statt der Rechte einer Person, prüft erst der Schritt nach
   Slack.
   Stand Laptop am 06.11. abends (per SSH geprüft): erreichbar, Nutzer in der Konsole angemeldet, die Claude-App
   (4.4212) läuft. Die Kommandozeile von Claude Code liegt nur gebündelt in der App, ist nicht im Pfad, und im Profil liegt
   keine Anmeldedatei; Tristan meint die Anmeldung in der App. Für Läufe per SSH braucht es deshalb einmal
   `claude setup-token` am Laptop (Tristan); das Token kommt nie ins Repo. Bei einem früheren Test ließ sich dort ein
   Plugin aus einem lokalen Marketplace ohne Adminrechte installieren und aktualisieren, Shell-Hooks liefen unter Git Bash
   (lokales Testprotokoll, nicht im Repo). Ob die Plugins im Code-Bereich der Claude-App genauso greifen, ist ungeprüft.
   Je Person eigene persönliche Anweisungen und eigenes Logbuch; in den Anweisungen von A steht ein erfundener privater
   Marker. Fällt ein Ort aus, simuliert ein eigener Konfigurationsordner (`CLAUDE_CONFIG_DIR`) am Mac die Person.
7. **Lernschleife** nach `AGENTS.md` Regel 6. Aus dem Ja wird ein Zweig mit Skill-Änderung und neuem Prüffall, das Prüfskript
   läuft, Tristan merged. Im MVP lokal statt als GitHub-PR, weil das öffentliche Repo keine Testvorschläge bekommen soll.
8. **Evals mit frischem Kontext:** `claude -p` mit leerem Konfigurationsordner und nur dem Plugin, der Fall als einzige Datei.
   Ein zweites Modell bewertet, das Ergebnis kommt in `evals/ergebnisse.md` des Skills.
9. **Zweiter Adapter: Hermes-Profil.** Derselbe Bauschritt erzeugt neben dem Claude-Plugin eine Hermes-Distribution: ein
   Git-Repo mit `distribution.yaml`, `SOUL.md`, `config.yaml`, `skills/`, `cron/` und `mcp.json`, installiert mit
   `hermes profile install`, aktualisiert mit `hermes profile update` ([Doku](https://github.com/NousResearch/hermes-agent/blob/b200f5bc60e31588ba2cb60e288029c4a54ba5fa/website/docs/user-guide/profile-distributions.md)). Lokal
   am 05.11. mit zwei Bots getestet (Befunde im Hermes-Werkzeugordner, nicht im Repo). Abbildung: Grundregeln,
   Kontext-Index und Landkarte nach `SOUL.md`, das Hermes in jede Unterhaltung lädt
   ([Kontextdateien](https://github.com/NousResearch/hermes-agent/blob/b200f5bc60e31588ba2cb60e288029c4a54ba5fa/website/docs/user-guide/features/context-files.md)); Skills nach `skills/`; Routinen nach `cron/`, erst in Stufe 2.
   Ziel im MVP ist eine eigene Hermes-Installation auf dem Laptop: nativ unter Windows, im Nutzerprofil unter
   `%LOCALAPPDATA%\hermes`, ohne Adminrechte (Hermes-README). Installiert am 06.11. abends, v0.23.0. Per SSH brach
   der Installer beim Python-Verzeichnis mit Windows-Fehler 448 ab („nicht vertrauenswürdiger Bereitstellungspunkt“); in
   der angemeldeten Desktop-Sitzung lief er durch. Ein Modell ist noch nicht angemeldet; naheliegend ist `openai-codex`
   mit dem Konto auf dem Laptop (Nr. 7 unter „Entschieden“), anmelden muss Tristan selbst. Danach Slack über `hermes gateway`, auf dem Laptop oder auf
   dem Server eines Kollegen; dort eigenes Profil, eigener Kanal, Zugang nur für die beiden. Immer nur erfundene Daten.
   Die Anmeldung beim Modell macht Tristan selbst.
   Grenzen laut Hermes-Doku: Hermes versteht sich als „single-tenant personal agent“; alle Nutzer eines Profils teilen
   Gedächtnis und Skills, und Skills laufen im Agentenprozess auf dem Host. Der Rückweg aus Hermes ins Repo fehlt dort
   ebenso (L8, L20). [OFFEN: welches Modell Hermes auf dem Laptop nutzt; für den Slack-Schritt Repo und Zugang zu
   dem Hermes des Kollegen, welches Modell dort läuft und wer die Daten auf dem Server sieht (L16, L19); ob sich der Prüfer als
   fester Unteragent mitliefern lässt (L10).]

### 6.4 Ablauf

1. Version 1 bauen: Plugin für A und Hermes-Profil für B, beide zuerst auf dem Laptop.
2. A bittet: „Mach mir aus der Notiz die Aufgaben.“ Der Agent wählt den Skill ohne dessen Namen, der Prüfer prüft, der Entwurf
   liegt im Ordner von A, das Logbuch von A bekommt eine Zeile mit der Version.
3. Tristan korrigiert ein allgemeines Muster, etwa: unsichere Termine kennzeichnen statt raten.
4. Der Agent ordnet ein (einmalig oder Regel) und schlägt Ort, Wortlaut und Prüffall vor. Tristan sagt Ja.
5. Zweig mit Skill-Änderung und neuem Prüffall; Prüfskript grün; ein Pi-Agent in Sandcastle prüft den Vorschlag
   (entschieden 07.11.); Tristan merged; Version 2 wird gebaut und kommt als
   Plugin-Update zu A und per `hermes profile update` zu B.
6. B gibt dem Hermes mit Version 2 eine andere Notiz, später über Slack. Die Regel wirkt. Der Marker von A steht weder im Vorschlag noch in
   Ergebnis oder Logbuch von B.
7. Rücknahme: Version 1 wird als Version 3 neu veröffentlicht. A und B arbeiten wieder nach der alten Fassung und melden
   Version 3.
8. Alle vier Prüffälle laufen mit frischem Kontext, das Ergebnis wird eingetragen.

### 6.5 Abnahme

Das MVP ist bestanden, wenn:

- die Bedingungen unter „Bestanden“ in [szenarien §4](docs/szenarien.md) erfüllt sind: Die Verbesserung kommt bei B an, ein
  unberechtigter Inhalt nicht, Quelle und Version sind nachweisbar;
- die Tore „Paket und Zuständigkeit“, „Update und Rücknahme“ und „Ergebnis und Rückweg“ aus dem
  [Laufzeitvergleich](docs/architektur/laufzeitvergleich-2026-11-05.md#ein-nützlicher-prüffall-und-sechs-abnahmetore) im
  lokalen Maßstab halten;
- die Grundregeln nachweislich wirken: Im Grenzfall wird nichts gesendet, und die Notiz gilt als Daten (L2);
- beide Adapter denselben Stand melden und eine Verbesserung aus dem Claude-Weg in Slack wirkt;
- jede Abkürzung im Register als „umgangen“ steht.

Gemessen werden die Zahl der Korrekturen je Entwurf, ob der Skill ohne Namen gewählt wurde, und die Zeit bis zum ersten
sauberen Durchlauf. Eine Zeitersparnis wird nicht behauptet.

### 6.6 Abbruch

Braucht das MVP mehr als Claude Code, Git und ein Prüfskript, also einen Dienst, eine Datenbank oder ein weiteres Framework,
wird angehalten. Ins Register kommt, welche Lücke das erzwingt. Genau diese Stelle begründet später die Wahl eines Werkzeugs.

### 6.7 Nicht im MVP

- Läufe im Hintergrund und Slack (L1, L15)
- Claude-App und Mitarbeitende ohne Terminal (L4)
- Pakete je Rolle (L6)
- echte Konnektoren und Firmendaten (L7, L9, L24)
- Fachanwendungen auf den Endgeräten aus der Cloud erreichen (L23)
- OS-Check und Zählen über Personen (L12)
- Abbau von Freigaben (L13)
- Rakazo, Microsoft, Archon, Sandcastle, OpenRig, Paperclip
- AI Act und ISO/IEC 42001 (L18). Das MVP hinterlässt nur Spuren, die später als Nachweis taugen: Git-Verlauf,
  Prüfergebnisse, Logbuch. Wie sie auf die Norm passen, steht in [#2](https://github.com/enving/kobetriebssystem/issues/2).

## 7. Danach: Stufen und wann ein Werkzeug dazukommt

| Stufe | Ziel | Werkzeug kommt dazu, wenn … |
|---|---|---|
| 1 MVP | Kernkreislauf lokal | – |
| 2 Hintergrund | derselbe Skill als Routine mit Auftrag, Rückfrage und Fortsetzen | Engine nach [recherche §3](docs/recherche.md). **Archon**, wenn Warten auf eine Antwort und Fortsetzen gebraucht werden und eine GitHub Action oder Zeitplanaufgabe das nicht trägt ([#4](https://github.com/enving/kobetriebssystem/issues/4)). **Sandcastle**, wenn ein unbeaufsichtigter Lauf Schreibrechte bekommt oder die Evals mit leerem Konfigurationsordner nicht frisch genug sind. |
| 3 Team | ein Vorgang, der über Stunden oder Tage mehrere Rollen braucht | **OpenRig**, und nur so, dass es nicht in `AGENTS.md` oder `CLAUDE.md` schreibt: eigenes Benutzerkonto oder VM |
| 4 Firma | Mitarbeitende ohne Terminal, Rollen, Identität | Oberfläche und Laufzeit (Rakazo, Microsoft, Claude-App, Paperclip) nach den Toren im [Laufzeitvergleich](docs/architektur/laufzeitvergleich-2026-11-05.md) und mit dem Sync aus [#13](https://github.com/enving/kobetriebssystem/issues/13). **Paperclip** nur, wenn dessen Prüfstein 1 hält: Git bleibt die Quelle. |

Die AI Software Factory ist nicht vorgesehen: Sie mergt selbst und hat keine Lizenz.

## 8. Passen die Werkzeuge zu den Anforderungen im Repo?

**Einschätzung Claude Opus 5.5, 06.11.2026.** Bewertet aus Doku und READMEs, gelesen am 05. und 06.11.2026. Gelaufen ist am
Mac nur Archon (drei Läufe). Die Anforderungen stammen aus den Bedingungen (a) bis (c) im
[Abgleich §3](docs/architektur/abgleich-ai-first-2026-11-06.md), den Anforderungen A1 bis C3 an eine Engine aus
[recherche §3](docs/recherche.md), dem Bedarf aus [szenarien §3](docs/szenarien.md) und den Grundsätzen aus dem
[Bericht](docs/architektur/bericht-2026-11-05.md) §9 und §10 (laufzeitneutral, Mensch an drei Toren, getrennte Bausteine).
Zeichen: ✔ erfüllt · ◐ mit Umweg oder teilweise · ✘ nicht · ? nicht nachgelesen.

| Anforderung | MVP: Claude Code und Plugin | Archon | Sandcastle | OpenRig | Paperclip | Factory |
|---|---|---|---|---|---|---|
| (a) Steuerung kommt aus Git | ✔ Plugin aus dem Repo | ✔ Abläufe als YAML im Repo | ✔ `.sandcastle/` im Repo | ◐ Team-Datei in YAML, schreibt aber selbst Blöcke in `AGENTS.md`/`CLAUDE.md` | ✘ Datenbank maßgeblich, Import aus Git möglich | ✔ |
| (b) Rechte der Person oder ausdrücklich zugeteilt | ✔ Person | ◐ Konto des Betreibers | ✔ eng: nur das Repo, eigenes Token | ✘ Steuer-Agent ohne Rückfrage, volle Rechte | ◐ weite Werksrechte | ◐ Konto des Betreibers |
| (c) Steuerung ändert sich nur per PR mit Ja | ✔ Regel 6, Zweig | ✔ | ✔ Commits auf Zweig | ✘ | ✘ Vorschläge in der Datenbank | ✘ mergt selbst |
| A5 zweiter Prüfer gegen Kriterien | ✔ Unteragent | ✔ eigener Knoten, anderes Modell | ◐ Vorlage `sequential-reviewer` | ? | ◐ Evals im Skill-Studio | ✔ zwei fremde Prüfer |
| frischer Eval-Lauf | ◐ leerer Konfigurationsordner | ◐ Worktree ohne Abschottung | ✔ leeres Home | ✘ | ? | ◐ versteckte Prüffälle |
| A2/A3 Zeitplan, Ereignis | ✘ erst Stufe 2 | ✔ LaunchAgent, Webhook | ✘ nur eigener Aufruf | ◐ Einmal-Wecker, Warteschlange | ✔ Routinen | ✔ launchd |
| A7 Rückfrage, danach weiter | ✘ | ✔ Freigabeknoten, auch über Slack | ✘ | ◐ wartende Agenten wecken | ✔ Freigabe-Tore | ◐ Merge-Tor |
| A6 Lauflog als Nachweis | ◐ Logbuch und Git | ✔ SQLite mit Kosten je Schritt | ◐ Commits | ? | ? | ◐ Prüfprotokoll |
| Abschottung (Tor im Laufzeitvergleich) | ✘ Hooks sind nur Textprüfung | ✘ laut eigener Doku keine Mandantentrennung | ✔ Seatbelt oder Container; Netz offen | ✘ nur für eigene Rechner | ◐ Codex mit eigenem Home; Claude erbt vermutlich die Host-Einstellungen | ✘ |
| Mitarbeitende ohne Terminal (szenarien §3, B3) | ✘ Claude-App offen (L4) | ✘ für Betreiber | ✘ Bibliothek | ✘ tmux | ✔ Web-Oberfläche | ✘ |
| B2 Agent austauschbar | ◐ an Claude Code gebunden, Inhalte portabel | ✔ Claude, Codex, Pi | ✔ sechs Agenten | ✔ Claude, Codex, Pi | ✔ mehrere Adapter | ◐ über Archon |
| zusätzlicher Betrieb | ✔ keiner | ◐ `archon serve` für Slack und Fortsetzen | ✔ keiner | ✘ Daemon, tmux, Node 22 | ✘ Server und Postgres | ◐ launchd, eigene Archon-Fassung |
| Reife, Lizenz | – | MIT, v0.13 | MIT, v0.14 | Apache-2.0, v0.7, Release alle 2–3 Tage | MIT, Telemetrie ab Werk an | keine Lizenz |

**Ergebnis:** Kein Werkzeug erfüllt alles. Das MVP erfüllt (a) bis (c) ohne Zusatz. Ihm fehlen Zeitplan, Fortsetzen nach einer
Rückfrage, technische Abschottung und eine Oberfläche ohne Terminal. Genau dort setzen die Werkzeuge an, jedes an einer
anderen Stelle. Deshalb kommen sie stufenweise dazu (§7) und nicht als Paket.

**Zu Tristans Wunsch, Teams virtueller Mitarbeitender qualitätsgesichert und vielleicht isoliert anzustoßen** (06.11.):

- **Das deckt das MVP schon:** benannte Rollen als Agenten im Plugin, etwa Bearbeiter, Prüfer und Eval-Bewerter, jede mit
  eigener Anweisung, eigenen Werkzeugen und eigenem Modell. Eine Bitte stößt sie an, der Prüfer sichert die Qualität gegen
  „Fertig heißt …“. Isoliert ist dabei nur der Kontext: Jede Rolle hat ihr eigenes Kontextfenster, technisch getrennt ist sie
  nicht.
- **Das bringt OpenRig zusätzlich:** Rollen, die dauerhaft weiterleben, eine Warteschlange, Übergaben und Wecken. Das braucht
  ein langer Auftrag über Tage, keine Termin-Nachbereitung.
- **OpenRig mit Sandcastle:** In keiner der beiden Dokus habe ich einen gemeinsamen Weg gefunden. OpenRig startet Sitzungen in
  tmux direkt auf dem Rechner, Sandcastle kapselt einen einzelnen Lauf, den ein Skript aufruft. Beides zu verbinden hieße
  vermutlich eigenen Verbindungscode. Näher liegt Archon mit Sandcastle: Ein Archon-Ablauf startet je Rolle einen
  abgeschotteten Sandcastle-Lauf. Dann leben die Rollen nur so lange wie ihr Auftrag.

### Laufende Produktsicht (keine Auswahl)

Tristan, 06.11.: dauerhaft eine Sicht auf Produkte und Frameworks, aber keine frühe Festlegung. Diese Liste ist der
Einstieg; bewertet wird an der verlinkten Stelle. Neue Produkte kommen als Zeile dazu. Ausgewählt wird erst, wenn die
Aufteilung (§3a) und die Lücken L1, L4 und L23 geklärt sind.

| Produkt | Ebene | bewertet in | Stand |
|---|---|---|---|
| Claude Code mit Plugin | Arbeitsplatz, Verteilung | §6, [installation/README.md](installation/README.md) | MVP |
| Codex | Arbeitsplatz | [Hooks erstellen](docs/hooks-erstellen.md) | Zielformat offen (L4) |
| Claude-App mit Plugins | Arbeitsplatz ohne Terminal | [installation/README.md](installation/README.md) | ungeprüft |
| Microsoft (Foundry Hosted Agents, Agent 365, Entra) | Laufzeit, Identität, Governance | [szenarien §5](docs/szenarien.md), [Bericht §11](docs/architektur/bericht-2026-11-05.md) | nicht gegen aktuelle Doku geprüft; Copilot für Mitarbeitende auf dem Parkplatz (§11) |
| Google-Umgebung | Arbeitsplatz | – | nicht betrachtet |
| Rakazo | Laufzeit mit Bots und Spaces | [Bericht](docs/architektur/bericht-2026-11-05.md), [Laufzeitvergleich](docs/architektur/laufzeitvergleich-2026-11-05.md) | zurückgestellt (Tristan, 06.11.) |
| Hermes Agent | persönliche Assistenz, Bot in Slack | [Laufzeitvergleich](docs/architektur/laufzeitvergleich-2026-11-05.md), §6.3 Nr. 9 | Adapterziel im MVP (eigene Installation auf dem Laptop, später Slack), keine Auswahl |
| Pi mit OpenShell | Agentenkern, Sandbox | [Laufzeitvergleich §1](docs/architektur/laufzeitvergleich-2026-11-05.md), [Harness-Recherche](docs/architektur/harness-firmenagenten-2026-11-07.md) | engster Kandidat für Firmen-Agenten (L25) |
| pi-durable | fortsetzbare Agentenläufe | [Harness-Recherche](docs/architektur/harness-firmenagenten-2026-11-07.md) | experimentell, erst für Routinen (L15) |
| DeepSeek Harness | Harness mit Sandbox und Plugins | [Harness-Recherche](docs/architektur/harness-firmenagenten-2026-11-07.md) | Parkplatz (§11) |
| Harness² (Google Research), Amplio (DeepMind) | Harness verbessern; schlanker Harness | [Harness-Recherche](docs/architektur/harness-firmenagenten-2026-11-07.md) | Forschung bzw. früh |
| OpenWebUI (Terminals, Computer) | Oberfläche | [szenarien §5](docs/szenarien.md) | Kandidat |
| Archon | Abläufe, Werkstatt | [recherche §3](docs/recherche.md), [#4](https://github.com/enving/kobetriebssystem/issues/4) | Stufe 2 |
| Sandcastle | Abschottung eines Laufs | §7, [Abgleich](docs/architektur/abgleich-ai-first-2026-11-06.md) | Stufe 2 |
| OpenRig | Team im Terminal | [szenarien §5](docs/szenarien.md), §8 | Stufe 3 |
| Paperclip | Verwaltung von Agenten | [Laufzeitvergleich §2](docs/architektur/laufzeitvergleich-2026-11-05.md) | Stufe 4, Prüfstein Git |
| GitHub Agentic Workflows | Repo-Pflege | [recherche §4 F](docs/recherche.md#architektur) | nur Doku gelesen |
| n8n | Ereignisse, Abgleich | [recherche §3, §4 F](docs/recherche.md) | nur, wenn schon im Betrieb |
| OpenHands SDK | Softwareaufträge | [Laufzeitvergleich §3](docs/architektur/laufzeitvergleich-2026-11-05.md) | zweite Wahl |
| AI Software Factory | Produktzyklus | [recherche §3](docs/recherche.md) | nicht vorgesehen |

## 9. Lückenregister

### 9.1 Regeln

1. Jede bekannte Architekturlücke steht hier mit Kennung. Fällt beim Arbeiten eine neue auf, kommt sie hierher und nicht nur
   in einen Fließtext.
2. Status: **offen** · **Arbeitsannahme** (Modell, Datum, Begründung, jederzeit widerrufbar) · **entschieden** (Tristan,
   Datum). Nur Tristan setzt „entschieden“. In einer Firma übernimmt das die verantwortliche Person.
3. Eine Arbeitsannahme schließt keine Lücke. Wer in einem Dokument schreibt, als sei eine Lücke gelöst, nennt Kennung und
   Status.
4. Eine Abkürzung im MVP steht in der Spalte MVP als „umgangen“, mit dem gewählten Weg. Umgangen heißt nicht gelöst.
5. Technische Mittel (welches Werkzeug, welches Format) dürfen Agenten als Arbeitsentscheidung wählen; so gilt es seit dem
   05.11. Lücken zu Rechten, Identität, Informationsfluss, Freigaben, Datenschutz und Mitbestimmung entscheidet ein Mensch.
6. Ändert ein Schritt den Status einer Lücke oder den Aufbau, werden die zugehörigen Darstellungen nachgezogen oder als
   veraltet markiert, etwa die Skizzen unter `docs/architektur/`.

### 9.2 Register (Stand 06.11.2026)

Die zwölf Lücken aus dem [Abgleich §2](docs/architektur/abgleich-ai-first-2026-11-06.md) sind hier aufgegangen. Dessen Lücke
12 (Fachbegriffe) ist in der Vorlage gelöst (`kontext/glossar/`, `AGENTS.md` Regel 8) und fehlt deshalb.

**Wo und unter welcher Identität es läuft**

| Nr | Lücke | bisher behandelt | Status | im MVP | entscheidet |
|---|---|---|---|---|---|
| L1 | Ort und Konto der Läufe im Hintergrund: eigenes Konto oder das einer Person? Konnektoren schreiben „als Person“. | [recherche §3](docs/recherche.md) Nr. 2, §4 A/B; Bericht ?7; [#14](https://github.com/enving/kobetriebssystem/issues/14) | offen | nicht berührt | Tristan |
| L2 | Grundregeln, Kontext-Index und Landkarte erreichen die Sitzung über das Plugin nicht (§6.3 Nr. 2). | neu, aus `bauen.sh` und der Plugin-Referenz; auf keinem Gerät getestet | offen | wird gebaut | Agent (Technik) |
| L3 | Persönliche Ebene auf dem Gerät: Wo liegen Anweisungen, Logbuch und persönliche Skills, wenn Mitarbeitende das Repo nicht haben? Welche Regeln gelten, wenn persönliche und Firmenregeln einander widersprechen? | README „Persönliche Ebene“, `persoenlich/_vorlage/`, §3a; [PR #23](https://github.com/enving/kobetriebssystem/pull/23) (`user-kompass/`) | offen | Arbeitsannahme fürs MVP: Konfigurationsordner der Person | Tristan |
| L4 | Mitarbeitende ohne Terminal: Plugin in der Claude-App, Verteilung je Person und Rolle, Laufzeit der Firma | `installation/README.md` (zwei OFFEN-Stellen); Bericht §9.1, ?1, ?2; [#13](https://github.com/enving/kobetriebssystem/issues/13) | offen; Rakazo zurückgestellt (Tristan, 06.11.), Auswahl erst nach Klärung der Aufteilung | umgangen: nur Claude Code | Tristan |
| L5 | Version, Update, Rücknahme: „gilt sofort überall“ gegen laufende Sitzungen. Automatische Aktualisierung ist für eigene Marketplaces ab Werk aus. | Laufzeitvergleich, Tor „Update und Rücknahme“; `installation/README.md` | offen | teilweise: lokal geprüft (§6.4 Nr. 7) | Agent (Technik) |
| L23 | **Software auf den Endgeräten.** Fachanwendungen, die nur auf dem Rechner der Person laufen, erreicht ein Agent in der Cloud nicht. Es bleiben zwei Wege: Agenten auf den Endgeräten, die das Unternehmen dort betreibt, oder Cloud-Agenten mit einer vollwertigen Umgebung, etwa Windows, in der sie diese Anwendungen selbst installiert bekommen. Beide brauchen Lizenzen, Pflege und eine Identität. Tristan, 06.11.: „software die auf den endgeräten der mitarbeitenden laufen da kann kein Cloud agent ran ausser vorausgesetzt ein unternehmen hat sie über die agenten auf den Endgeräten oder die Cloud ahenten haben vollwerige umgebungen zb windows um diese anwendungen selbst installiert zu bekommen“ | Bericht §11 (Microsoft als Sandbox-Anbieter, ?8); Bericht §12 „Was die Sandbox kann“ ([PR #23](https://github.com/enving/kobetriebssystem/pull/23)); [#21](https://github.com/enving/kobetriebssystem/issues/21); L9 | offen | umgangen: das MVP läuft auf den Endgeräten selbst | Tristan |

**Rechte und Informationsfluss**

| Nr | Lücke | bisher behandelt | Status | im MVP | entscheidet |
|---|---|---|---|---|---|
| L6 | Leserechte in der Steuerung: Ein Plugin gibt allen alles, Git kennt keine Leserechte je Datei, Pakete je Empfängerkreis fehlen. | [recherche §1](docs/recherche.md), §4 B; [#17](https://github.com/enving/kobetriebssystem/issues/17) | offen | umgangen: nur erfundene, nicht vertrauliche Inhalte; Bauprüfung auf Marker | Tristan |
| L7 | Informationsfluss aus den Tools in Wiki, Entwürfe, Logbuch und Vorschläge, etwa bei der Kontext-Ernte | recherche §4 B; `SICHERHEIT.md` §3 „Lücken-Leck“ | offen | teilweise: Marker-Probe von A nach B | Tristan |
| L8 | Rückweg ohne Lesezugriff aufs Quell-Repo: `installation/README.md` sagt, Mitarbeitende brauchen nie Zugriff aufs Quell-Repo, und zugleich, ihr Agent erzeuge dort einen PR. Wer Pull Requests stellen kann, kann das Repo auch lesen, und dann schützt kein gefiltertes Paket mehr (recherche §4 B). | neu | offen | umgangen: Tristan hat Rechte am Repo | Tristan |
| L9 | Endgeräte und Datenklassen: Dürfen Agenten auf Geräten mit Personaldaten laufen, welche Laufwerke werden gesperrt? | `SICHERHEIT.md` §3 | offen | nicht berührt | Tristan |
| L24 | **Kontext ist unvollständig.** Ein großer Teil dessen, womit eine Person arbeitet, steckt nicht im Kontext: Mails, Chat (Slack, Teams), Kalender, Besprechungen, Dateien auf dem Gerät. Auch in Tristans eigenem Aufbau fehlen Mails und Slack. Offen: welche Quellen angebunden werden; ob nur live mit den Rechten der Person gelesen wird oder auch im Hintergrund (L1); was davon dauerhaft ins Wiki darf (L7); woran man merkt, dass Kontext fehlt (Kontext-Test in L22). Tristan, 06.11.: „kontext ist nocht vollständig auch bicht im kontext zb meine mails slack fehlen“ | [szenarien §3](docs/szenarien.md) „Kontext passend auswählen“; `kontext/landkarte.md`; L1, L7, L22 | offen | umgangen: einzige Quelle ist die erfundene Notiz | Tristan |

**Qualität und Lernen**

| Nr | Lücke | bisher behandelt | Status | im MVP | entscheidet |
|---|---|---|---|---|---|
| L10 | Prüfer: Was bekommt er außer Ergebnis und Kriterien (Belege, Quellenstand)? Wo reicht Code statt eines Modells? | [recherche §4 D](docs/recherche.md#architektur) | offen | teilweise: Unteragent mit Quellen | Agent (Technik) |
| L11 | „Frischer“ Eval-Lauf ohne persönliche Konfiguration | Abgleich §2 zu Lücke 6; [#1](https://github.com/enving/kobetriebssystem/issues/1), [#4](https://github.com/enving/kobetriebssystem/issues/4) | offen | teilweise: leerer Konfigurationsordner | Agent (Technik) |
| L12 | Datenbasis des OS-Checks: „ab drei gleichen Fällen“ über Personen zählen, ohne Inhalte zu sammeln | recherche §2, §3 Nr. 6; Abgleich §2 zu Lücke 4 (Vorschlag: Zähler) | offen | nicht berührt | Tristan |
| L13 | Kriterium für den Abbau einer Freigabe, mit automatischem Rückfall | Abgleich §2 zu Lücke 8 (Vorschlag) | offen | nicht berührt | Tristan |
| L14 | Nutzen messen: Nacharbeit statt bloßer Nutzung | Bericht §6.6; recherche §4 G | offen | teilweise: Korrekturen je Entwurf | Tristan |
| L20 | **Rückfluss aus dem gelebten User-Kompass.** Die Vorlage `user-kompass/_vorlage/` ist Text ohne Werkzeug. Was sich in einem gelebten Kompass bewährt (Tristans lokaler Kompass, 05.–06.11.: Startausgabe mit Wer/Ziel, Alter offener Aufgaben, Git-Zustand, Fragen oben, Schutz der Sicherungskopien), kommt nur von Hand und bisher gar nicht zurück; umgekehrt erreichen Verbesserungen der Vorlage einen bestehenden Kompass nicht. Tristan, 06.11. (Tippfehler bereinigt): „Wie bekommt es Verbesserungen aus meinem lokalen“ Vorschlag: eigenes Repo [`enving/kokompass`](https://github.com/enving/kokompass) (Methode, Vorlage, CLI, Prüfungen, synthetisches Beispiel) mit PRs, eingebunden als Git-Submodul im privaten Kompass und hier unter `user-kompass/`. **Tristan, 06.11.:** „Kokompass soll das öffentliche Repo sein als Vorlage. Und eingebunden bzw. nutzen tut es das kobetriebssystem unter … user besser genannt.“ Umgesetzt: kokompass 0.1 öffentlich (MPL-2.0), hier als Submodul `user/` ([PR #23](https://github.com/enving/kobetriebssystem/pull/23)), Beitragsweg in `user/BEITRAGEN.md`. Offen bleibt: die erste Instanz (Tristans Kompass) ist noch nicht umgestellt; Submodule sind für Mitarbeitende ohne Terminal eine Hürde (L4); ob das Plugin Submodule mitliefert, ist ungeprüft. | `user-kompass/_vorlage/README.md` (Beitragsweg nur für Erkenntnisse, nicht für Werkzeug); L3, L5, L8; [PR #23](https://github.com/enving/kobetriebssystem/pull/23) | entschieden (Tristan, 06.11.): Ort und Einbindung; Rückfluss in der Praxis offen | umgangen: `user/` wird nicht ausgerollt | Tristan (Ort und Sichtbarkeit), Agent (Technik) |
| L21 | **User-Kompass und Betriebssystem lernen voneinander.** Zwei Ebenen: je Person ein Kompass (persönlicher Agent), für die Firma das Betriebssystem (gemeinsames Wissen, „Schwarmintelligenz“). Offen ist, wie die beiden miteinander reden und sich gegenseitig verbessern, etwa wie zwei Agenten (Tristan: „wie 2 Hermes, die miteinander kommunizieren“): Was fragt der Firmen-Agent den persönlichen, was darf der persönliche antworten, wer verallgemeinert, wie entsteht aus vielen Personen ein Muster, ohne Inhalte zu sammeln, und wie kommt das Ergebnis zurück. Tristan, 06.11.: „Weiss aber noch net wie“. | Bericht §12 (drei Komponenten, Agenten dazwischen), ?10 ([#22](https://github.com/enving/kobetriebssystem/issues/22)); L8, L12, L16 | offen | nicht berührt | Tristan |
| L22 | **Bausteine aus Cole Medins „4 C“ fehlen in der Vorlage** ([Video](https://www.youtube.com/watch?v=qIWB1yMsqRo), [Starter](https://github.com/coleam00/second-brain-starter), gelesen 05.11.): (1) Kontext-Test: eine frische Sitzung muss ohne Suche sagen können, wer die Person ist, woran sie arbeitet und mit wem; (2) feste Aufgabenliste als Eval nach jeder größeren Änderung, etwa Modellwechsel; (3) Kernerinnerungen, die jede Sitzung lädt (bei Cole `memory.md`), getrennt von Anweisungen; (4) Takt erst nach Vertrauen, und jeder automatische Lauf meldet, was er getan hat. Seit kokompass 0.1 (06.11.): (1) und (2) als `vorlage/pruefung/fragen.md` mit Beispiel, (4) als Regel in `METHODE.md`; (3) über die Startausgabe aus `person/`. Ob die Listen tatsächlich nach Änderungen laufen, ist nicht belegt. | L11 (frischer Eval-Lauf), L15 (Routinen) | teilweise (Vorlage), Lauf offen | nicht berührt | Agent (Technik) |

**Ausführung**

| Nr | Lücke | bisher behandelt | Status | im MVP | entscheidet |
|---|---|---|---|---|---|
| L25 | **Firmeneigene Agenten neben den persönlichen.** Bisher kannte das Modell nur den Agenten der Person (Claude Code, Codex, Hermes) und dessen Unteragenten. Daneben braucht die Firma eigene Agenten: Änderungs-Prüfer, OS-Check, Routinen, Kontext-Ernte. Offen: welcher Harness (Kandidat Pi), welche Identität und welche Anmeldung (API-Schlüssel statt Abo), welche Werkzeuge je Agent, welche Abschottung, wer sie betreibt. Tristan, 07.11.: „ich denke es gibt mehrere“. | [Harness-Recherche](docs/architektur/harness-firmenagenten-2026-11-07.md); L1, L10, L15 | offen; entschieden ist der Harness: Pi in Sandcastle für Firmen-Agenten (Tristan, 07.11.); Identität, Rechte, Betrieb offen | Änderungs-Prüfer als Pi-Agent in Sandcastle am Mac | Tristan |
| L15 | Routinen: auf Antwort warten, fortsetzen, prüfen, ob alle gelaufen sind, doppelte Ereignisse erkennen | [recherche §3](docs/recherche.md), §4 C; Bericht §9.3 | Arbeitsannahme Archon als Werkstatt (Opus 5.5, 05.11.); Engine für Firmen offen | nicht berührt | Agent (Technik); Einschalten: Mensch |

**Organisation und Recht**

| Nr | Lücke | bisher behandelt | Status | im MVP | entscheidet |
|---|---|---|---|---|---|
| L16 | Personenbezug, Mitbestimmung, Modellanbieter; Audit-Log und Agenten-Gedächtnis als Leistungsdaten | `SICHERHEIT.md` §3; Bericht §6.4; [#15](https://github.com/enving/kobetriebssystem/issues/15) | offen | nicht berührt | Tristan |
| L17 | Rollen: Prozessverantwortliche, Bereichsbesitzer, benannte Aufsicht je Agent | README, Tabelle zum AI Act (Art. 14) | offen | nicht berührt | Tristan |
| L18 | AI Act und ISO/IEC 42001: Zuordnung, Risikoregister, Folgenabschätzung | README, Tabelle zum AI Act (OFFEN-Stellen); [#2](https://github.com/enving/kobetriebssystem/issues/2) | offen | nicht berührt; das MVP liefert nur Spuren | Tristan |
| L19 | Betrieb: Hosting, Modell und Kosten je Firma | Bericht ?5; [#16](https://github.com/enving/kobetriebssystem/issues/16) | offen | nicht berührt | Tristan |

## 10. Testentscheidungen

- Getestet wird, was von außen sichtbar ist: Ergebnisdatei, Logbuchzeile, Version, Marker vorhanden oder nicht. Der Wortlaut
  des Modells wird nicht getestet.
- Messbares prüft Code: Struktur, Verweise, Vertraulichkeitsmarker, Version. Ein Modell prüft nur, wo ein Urteil nötig ist,
  und wird an Tristans Korrekturen geeicht ([recherche §4 D](docs/recherche.md#architektur)).
- Vorbild ist `system/tests/pruefen.mjs` mit `faelle.json`: gleiche Fälle für alle Adapter, bekannte Umgehungen als „LÜCKE“
  markiert. Eine bekannte Lücke wird nie grün gezählt.
- Prüffälle der Skills folgen `.agents/skills/_vorlage/evals/`.

## 11. Parkplatz

Ideen, die bewusst nicht jetzt bearbeitet werden (Tristan, 07.11.: „nicht zuviel jez reinnehmen“). Nur auf Zuruf aufnehmen.

- **DeepSeek Harness für einzelne Mitarbeitende oder Firmen-Agenten:** Dort ist alles ein Plugin; damit ließen sich
  bestimmten Rollen besondere Plugins bereitstellen. Stärkstes eingebautes Rechtemodell der geprüften Harnesses, aber
  Vorschau ([Recherche](docs/architektur/harness-firmenagenten-2026-11-07.md)).
- **Microsoft für Mitarbeitende,** etwa Copilot, als weiteres Zielformat neben Claude und Codex (L4).
- **Hermes in Slack** auf dem Server eines Kollegen als zentraler Bot (§6.3 Nr. 9).
- **Harness²** (Google Research), um Skills und Prüfer anhand der Prüffälle zu verbessern.

## 12. Quellen

- Felix Schlenther, [KI-Betriebssystem 2.0](https://ai-first.ai/insights/ai-first-ki-betriebssystem-2-0), 01.11.2026.
- Claude-Code-Doku, gelesen am 06.11.2026: [Plugin-Referenz](https://code.claude.com/docs/en/plugins-reference),
  [Unteragenten](https://code.claude.com/docs/en/sub-agents), [Plugin-Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).
- Im Repo: [Abgleich mit dem Artikel](docs/architektur/abgleich-ai-first-2026-11-06.md), [szenarien.md](docs/szenarien.md),
  [recherche.md](docs/recherche.md), [Bericht vom 05.11.](docs/architektur/bericht-2026-11-05.md),
  [Laufzeitvergleich](docs/architektur/laufzeitvergleich-2026-11-05.md), [installation/README.md](installation/README.md).
