# Recherche (Stand 2026-11-02, Sonnet 5.5)

## 1. Dateirechte in GitHub/GitLab (Anmerkung 4)
**Befund (Suche, nicht in den Docs selbst nachgeprüft):**
- GitLab: Es gibt Feature-Requests für Lese-Beschränkung auf Ordner ([#454622](https://gitlab.com/gitlab-org/gitlab/-/issues/454622), [ee#308](https://gitlab.com/gitlab-org/gitlab-ee/issues/308)). Foren: Zugriff gilt pro Repository; Workaround getrennte Repos oder Submodul. Push-Regeln pro Pfad: nur Feature-Request ([#25813](https://gitlab.com/gitlab-org/gitlab-ce/issues/25813)).
- GitHub: [CODEOWNERS](https://docs.github.com/de/articles/about-code-owners) regelt, wer Änderungen **freigibt**, nicht wer **lesen** darf. Dass es keine Lese-Rechte pro Datei gibt, ist hier nur *Annahme* (Suche fand nichts Gegenteiliges) → in der GitHub-Doku gegenprüfen.

**Folgerung (Einschätzung, Tristan-Vorgabe 2026-11-02):** Kein Repo je Schutzstufe – das passt vermutlich zu kleinen Firmen, nicht zu gewachsenem Mittelstand. Minimum: **ein zentrales Unternehmens-Repo**; Aufteilung nach Rolle über Plugins/Orchestrierung, Mitarbeitende sehen das Repo evtl. gar nicht. Erst mit der Testfirma prüfen, dann komplexer machen.
**Offen:** GitHub-Doku zu Lese-Rechten prüfen.

## 2. Nicht recherchierbar, nur zu klären
- Datenbasis des OS-Checks festlegen.
- Lokal vs. zentral: im Vergleichsmaterial nicht eindeutig (Chat/Zeitplan/Ereignis; „Claude Code, App, Cloud lesen dieselben Dateien“ spricht für *beides*) → `docs/szenarien.md`.
- Wieviel aus alten Folgen → mit Tristan.
- Hooks, Managed Settings, Pi/OpenCode → nicht recherchiert.

## 3. Engine für die Automatisierungen (Anmerkungen 8, 10, 11; Stand 2026-11-04, Opus 5.5)
**Einordnung:** historischer Vorschlag, keine beschlossene Architektur. Die eigenständige [Architekturprüfung vom 05.11.](#architektur) präzisiert die Rechtefrage, widerspricht dem universellen Ablauf als Auswahlkriterium und ergänzt einen bislang fehlenden Kandidaten.

**Frage:** Was führt die Aufträge in `automatisierungen/` aus, nach Zeitplan oder Ereignis, ohne dass jemand tippt?

**Anforderungen** (Vergleichsmaterial, Abschnitte Automatisierungen und Lernschleife, und diese Vorlage): A1 Auftrag als Textdatei im Repo · A2 Zeitplan · A3 Ereignis · A4 so viel KI wie nötig, Rest Code · A5 zweiter Agent prüft gegen „Fertig heißt …“ · A6 Logbuch je Lauf, der OS-Check sieht, ob alles gelaufen ist · A7 Rückfrage an einen Menschen, danach geht es weiter · A8 Testläufe vor dem Einschalten · B1 zentrale Routine unter eigenem Konto statt mit den Rechten einer Person · B2 an keinen Agenten gebunden · B3 von einer Firma ohne Entwickler betreibbar. Nur für uns als Maintainer: C1 läuft mit Abo statt API-Schlüssel · C2 macht nach leerem Kontingent weiter · C3 erreicht die lokale Simulation der Testfirma auf dem Mac.

### Befunde (Herstellerdoku, Archon zusätzlich lokal; gelesen 04.11.2026)
- **Zeitplanaufgaben in Claude Code** (früher „Routines“, Forschungsvorschau): Zeitplan höchstens stündlich (Cron in UTC), API-Aufruf, GitHub-Ereignisse zu PR, Release und Issue (Claude-GitHub-App am Repo nötig). Läuft in der Anthropic-Cloud, klont die gewählten Repos je Lauf, pusht auf Zweige mit Präfix `claude/`. „Scheduled tasks belong to your individual claude.ai account“; Commits, Slack-Nachrichten und Konnektor-Aktionen erscheinen als diese Person. Verbundene Konnektoren sind standardmäßig dabei, „including writes“. Verbrauch zählt gegen das Abo, am Limit werden Läufe bis zum Reset abgelehnt. Jeder Lauf ist als Sitzung einsehbar; „Succeeded“ heißt nur, dass die Sitzung endete. Der Prompt liegt in der Aufgabe, Skills kommen aus dem geklonten Repo. [Doku](https://code.claude.com/docs/en/routines), [API](https://platform.claude.com/docs/en/api/claude-code/routines-fire)
- **Zeitplanaufgaben in Codex** (App): lokal (Rechner und App müssen laufen) oder im Web; Zeitplan, auf berechtigten Plänen auch Gmail-, Slack- und GitHub-Ereignisse (nur ChatGPT Web/Mobil). Prompt in der Aufgabe. [Doku](https://learn.chatgpt.com/docs/automations?surface=app) (hinterer Teil nur als Zusammenfassung gelesen)
- **GitHub Actions:** `anthropics/claude-code-action` arbeitet mit `prompt` im Automatikmodus, Beispiele mit `schedule` und `workflow_dispatch`; Anmeldung per API-Schlüssel oder `claude_code_oauth_token` aus dem Abo (`claude setup-token`). `openai/codex-action` ist nur mit `OPENAI_API_KEY` dokumentiert. Eigene Runner nur mit privaten Repos, rät GitHub (Forks können über PRs Code darauf ausführen). Zeitgesteuerte Workflows in öffentlichen Repos schaltet GitHub nach 60 Tagen ohne Aktivität ab. [claude-code-action](https://github.com/anthropics/claude-code-action/blob/main/docs/solutions.md), [codex-action](https://learn.chatgpt.com/docs/github-action), [eigene Runner](https://docs.github.com/actions/hosting-your-own-runners/adding-self-hosted-runners), [60 Tage](https://docs.github.com/actions/managing-workflow-runs/disabling-and-enabling-a-workflow)
- **Archon v0.13.2** (installiert, CLI-Hilfe gelesen; das Übrige aus der Doku, die dem Release vorauslaufen kann): Zeitplan per `archon trigger schedule install --config <datei>` als macOS-LaunchAgent (Intervall in Sekunden, nur bei angemeldetem Nutzer; Linux über eigenen Cron). Die Takt-Datei liegt außerhalb des Workflows: „Schedules and event bindings are deployment configuration. They do not belong in workflow YAML.“ Ereignisse per GitHub- oder signiertem Webhook, beides braucht eine erreichbare Adresse. Freigabeknoten, Antwort per CLI (`archon workflow approve`), Web, HTTP oder Slack (Socket Mode ohne öffentliche Adresse, braucht `archon serve`). Anbieter und Modell je Knoten wählbar. Lauflog in SQLite mit Kosten und Tokens je Knoten. Trockenlauf `archon workflow test` mit Fixtures, der laut CLI-Hilfe keinen Anbieter anspricht. [Trigger](https://archon.diy/guides/workflow-triggers/), [Freigaben](https://archon.diy/guides/approval-nodes/), [Slack](https://archon.diy/adapters/slack/)
- **n8n:** Slack-Freigabe für einzelne Werkzeuge eines KI-Agenten und „senden und warten“; Abläufe liegen in der n8n-Datenbank, nicht als Text im Repo. Das Vergleichsmaterial lief in Version 1 auf n8n und wurde umgebaut. [Slack-Knoten](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack)
- **Indiz, kein Beleg:** Im Vergleichsmaterial ist der kürzeste Takt stündlich, und die Ereignis-Routine „Sales“ läuft „werktags dreimal am Tag“. Das passt zu Zeitplanaufgaben mit Mindesttakt eine Stunde und zu Ereignissen, die im Takt abgefragt werden. Welche Engine dort läuft, steht nicht im Text.

### Abgleich (✔ erfüllt · ◐ mit Umweg · ✘ nicht)
| | Zeitplanaufgabe der App (Claude/Codex) | GitHub Actions | Archon am Mac | eigenes Skript (launchd, SQLite, `claude -p`/`codex exec`) | n8n |
|---|---|---|---|---|---|
| A1 Auftrag im Repo | ◐ Einzeiler-Prompt verweist auf die Datei | ✔ | ◐ Workflow im Repo, Takt-Datei außerhalb | ✔ | ✘ Ablauf in der n8n-DB |
| A2 Zeitplan | ✔ ab stündlich, Cloud | ✔ | ✔ Mac muss laufen | ✔ Mac muss laufen | ✔ |
| A3 Ereignis | ◐ GitHub, API; Codex auch Mail/Slack | ◐ GitHub, Fremdes per `repository_dispatch` | ◐ Webhook mit Adresse oder Abfrage | ◐ Abfrage im Takt | ✔ viele Quellen |
| A4 Code + KI | ◐ Code nur, wenn der Agent ihn aufruft | ✔ Schritte vor und nach der KI | ✔ Skript- und KI-Knoten | ✔ | ✔ |
| A5 Prüfer | ◐ Subagent im selben Lauf | ◐ zweiter Job, Codex nur mit API-Schlüssel | ✔ eigener Knoten, anderes Modell | ✔ | ◐ |
| A6 Logbuch, Nachweis | ◐ Sitzungsverlauf, Status sagt nichts über das Ergebnis | ✔ Laufhistorie per API | ✔ SQLite mit Kosten | ◐ selbst bauen | ✔ |
| A7 Rückfrage, dann weiter | ◐ nur als neuer Lauf (Antwort → API-Auslöser) | ◐ Antwort = neues Ereignis | ✔ Freigabeknoten, auch Slack | ◐ asynchron | ✔ senden und warten |
| A8 Testlauf vorab | ◐ „Jetzt ausführen“ | ◐ manuell auf Zweig | ✔ Trockenlauf ohne Anbieter | ◐ | ◐ |
| B1 eigenes Konto | ✘ läuft als die Person | ✔ Secrets, Bot-Konto | ◐ Logins des Mac-Nutzers | ◐ dito | ✔ Zugangsdaten je Knoten |
| B2 nicht gebunden | ✘ je Anbieter ein eigenes Gegenstück | ◐ Claude und Codex, an GitHub gebunden | ✔ Claude, Codex, Pi | ✔ | ◐ eigene KI-Knoten |
| B3 ohne Entwickler | ✔ | ◐ einmal durch die IT | ✘ CLI, vor 1.0 | ✘ | ◐ eigener Server |
| C1 Abo | ✔ | ◐ Claude ja, Codex nein | ✔ | ✔ | ✘ API |
| C2 weiter nach Kontingent | ✘ | ✘ | ✔ (Doku) | ◐ nächster Takt | – |
| C3 lokale Simulation | ✘ | ✘ eigener Runner im öffentlichen Repo: nein | ✔ | ✔ | ◐ Tunnel |

Ohne Test ausgeschlossen: Temporal, Inngest, Trigger.dev, DBOS, Windmill (Server und meist Postgres für wenige Läufe am Tag).

### Einschätzung (Claude Opus 5.5, 2026-11-04; entschieden ist nichts)
1. **Die Vorlage legt einen Ablauf fest, keine Engine.** Keiner der Kandidaten erfüllt alle Zeilen, und das Vergleichsmaterial verlangt, den Agenten wechseln zu können. Gleich bleiben in jeder Engine die Auftragsdatei und fünf Schritte:
   1. Code: Auftrag lesen, `status: freigegeben` und Takt prüfen, sonst abbrechen.
   2. KI: Skill ausführen, nur aus den erlaubten Quellen.
   3. KI mit anderem Modell oder frischem Kontext: gegen „Fertig heißt …“ prüfen.
   4. Code: Logbuchzeile schreiben, Ergebnis als Entwurf, Issue oder Entwurfs-PR ablegen.
   5. Code: höchstens eine Meldung, mit Link.

   Eine neue Routine ist dann eine neue Auftragsdatei und kein neuer Ablauf. Eine Engine, die das nicht mit **einem** Ablauf und der Auftragsdatei als Eingabe abbildet, scheidet aus.
2. **Unter wessen Konto eine Routine läuft, wiegt schwerer als jede Funktion.** Ort (lokal oder Cloud) und Konto (Person oder Dienstkonto) sind zwei getrennte Fragen; die Zeitplanaufgabe der App läuft in der Cloud, aber als Person. Für persönliche Routinen (die eigenen Mails vorsortieren) passt das. Läuft eine zentrale Routine (Kontext-Ernte ins gemeinsame Wiki) unter dem Konto einer Person, landet, was diese Person lesen darf, in einer Ablage für alle: das Rechte-Leck aus Anmerkung 6. **Vorschlag für `SICHERHEIT.md`:** „Eine zentrale Routine läuft unter einem eigenen Konto und liest nur, was alle Leser ihres Ergebnisorts lesen dürfen.“ Prüffall: Kontext-Ernte mit einem Konto, das einen vertraulichen Kanal sieht; der Lauf muss abbrechen oder den Kanal auslassen.
3. **Referenzwege für Firmen:** persönliche Routinen über die Zeitplanfunktion der Agenten-App mit Einzeiler-Prompt, Schreib-Konnektoren abgewählt; zentrale Routinen über GitHub Actions mit eigenem Konto, Nachweis in GitHub (hilft #2). Freigabe vor dem Einschalten als PR, der den Status setzt, mit CODEOWNERS auf `automatisierungen/`. Archon und n8n als Möglichkeit nennen, nicht voraussetzen. n8n taugt als Bote für Ereignisse außerhalb von GitHub (Mail, Kalender → `repository_dispatch` oder API-Auslöser) und für den Abgleich nach SharePoint (Anmerkung 3).
4. **Für uns als Maintainer ist Archon der stärkste Kandidat.** Er deckt genau die Zeilen ab, an denen die Cloud-Wege scheitern: anderes Modell als Prüfer, Rückfrage mit Fortsetzung, Weitermachen nach Kontingent, Trockenlauf, Zugriff auf die lokale Simulation, beide Abos. Belegt ist das nur aus Doku und CLI-Hilfe, nicht aus einem Lauf.
5. **Die Software-Factory auf Archon passt hier nicht.** Sie prüft laufende Software (Nutzerabläufe, Laufzeitprüfung, versteckte Prüffälle gegen ein Programm); dieses Repo enthält Text. Übernehmen lässt sich ihr Muster: Auftrag mit „nie“, versteckte Prüffälle, geschützte Regeldateien.
6. **Lernschleife:** Einordnen, Ja und PR passieren im Chat und brauchen keine Engine. Automatisieren lässt sich der wöchentliche OS-Check. Als Datenbasis (Anmerkung 8) bietet sich die Logbuchzeile aus `AGENTS.md` Regel 6 an („Lernschleife: <Muster> → … einmalig“): ab drei gleichen Mustern ein Vorschlag, höchstens drei je Woche. [OFFEN: Laut `user/vorlage/log.md` (kokompass; bis 05.11.2026 `persoenlich/`) liegt das Logbuch bei der Person, nicht im zentralen Repo. Ein zentraler OS-Check sieht es nur, wenn die Zeilen per PR oder Export zurückfließen.]

### Vorgeschlagener Test (Prüffall für #4)
**OS-Check der Vorlage selbst**, ohne Firmendaten und deshalb im öffentlichen Repo unbedenklich. Code führt `system/tests/pruefen.mjs` aus, prüft Links und Frontmatter, listet die Aufträge mit Status und prüft im Lauflog, ob alle gelaufen sind. KI bündelt die Befunde zu höchstens drei Vorschlägen, ein zweites Modell prüft gegen „Fertig heißt …“, Ergebnis ist ein Entwurfs-Issue plus Logbuchzeile. Einmal als Archon-Workflow am Mac, einmal als GitHub Action. Verglichen werden: Zeilen eigener Code und Konfiguration, Abhängigkeiten, Zeit bis zum ersten sauberen Lauf, Lesbarkeit des Laufprotokolls, Weg der Rückfrage, Fortsetzen nach Abbruch.
**Abbruch für Archon:** Der Ablauf lässt sich nicht als **ein** Workflow mit der Auftragsdatei als Eingabe bauen, oder der erste saubere Lauf dauert länger als zwei Stunden. `archon serve` ist für uns am Mac zulässig, als Voraussetzung der Vorlage nicht. Leistet die Action dasselbe, wird keine Engine eingeführt; Archon wird dann nur für die Testfirma erneut geprüft.

### Fallen
- Zeitplanaufgaben der App: Forschungsvorschau, Takt mindestens stündlich, Zweige `claude/…` per Ruleset begrenzen. [OFFEN: Ob Hooks aus dem Repo (`system/hooks/`) in diesen Läufen greifen, ist nur aus Sekundärquellen bekannt.]
- Archon: Der Takt liegt außerhalb des Repos; `takt.md` bleibt die Quelle, die Trigger-Datei wird daraus erzeugt. `autoResumeOnQuotaReset` ist standardmäßig an. Codex hat über Archon laut Anbietermatrix keine Werkzeugfilter und Hooks ([Matrix](https://archon.diy/reference/provider-capabilities/)). Version vor 1.0.
- GitHub Actions im öffentlichen Repo: 60-Tage-Abschaltung, kein eigener Runner.
- Jede Engine: erst die Prüffälle, dann der Zeitplan, sonst entsteht automatisiert Ausschuss.

<a id="architektur"></a>

## 4. Architekturprüfung: vom lesbaren Wissen zur verlässlichen Arbeit

**Einschätzung: GPT-6-astra, 05.11.2026.** Auf Auftrag, die bisherigen Vorschläge als erste Idee zu behandeln und eine eigene Architekturmeinung zu entwickeln. Gegenprüfung durch Claude Opus 5.5 am 04.11.; die folgenden Schlussfolgerungen liegen in Verantwortung von GPT-6-astra. **Keine neue Regel, Freigabe oder Engine-Entscheidung.** Zuständige verbindliche Quellen bleiben `AGENTS.md`, `SICHERHEIT.md` und die vorhandenen Vorlagen. Eine Übernahme dieser Vorschläge würde dort erfolgen, nicht als zweiter Regelbestand hier.

### Urteil

Die Grundidee trägt: Arbeitswissen und Qualitätsmaßstäbe so zugänglich machen, dass ein Agent Aufgaben selbstständig erledigen kann. Die Trennung von Skills, Kontext, Werkzeugen und Regeln sowie die überprüfbare Lernschleife sind eine gute Grundlage. Das Repository ist bisher jedoch vor allem ein Organisationshandbuch für Agenten. Eine Engine ergänzt Ausführung; verlässliche Arbeit entsteht erst durch klare Zuständigkeit, begrenzte Rechte, überprüfbare Ergebnisse und einen belastbaren Umgang mit Unterbrechungen.

Meine Priorität wäre **ein nützlicher, begrenzter Ablauf mit nachgewiesenen Grenzen**, bevor ein allgemeiner Ausführer oder mehrere gleichartige Implementierungen entstehen. Die Vorlage soll leicht verständlich bleiben. Ihre fehlende Ausführungslogik sollte nicht dadurch kaschiert werden, dass noch mehr Pflichten im Prompt stehen.

### Was tatsächlich geprüft wurde

Referenzstand: `90b280262750ed0dc615a62c7e6f8574cce39ad1`. [Ausführbare Probe](pruefungen/architekturprobe.py), [Rohbefund mit Quell-Hashes](pruefungen/architekturprobe-2026-11-05.json). Der erste Pluginversuch erfolgte am 04.11.; am 05.11. wurden beide lokalen Proben mit dem abgelegten Skript reproduziert.

- **Hook-Batterie:** 44 Adapter/Fall-Kombinationen, 32 `OK`, 12 als bekannt markierte `LÜCKE`, Exit 0. Wildcard, Großschreibung und Variable werden bei jedem der vier Adapter durchgelassen. Das ist das erklärte Verhalten der Testbatterie, kein versteckter Testfehler. Grün bedeutet hier: keine unerwartete Abweichung; es bedeutet nicht: alle verbotenen Zugriffe verhindert. Die Adapter werden mit konstruierten Werkzeugaufrufen getestet, nicht in vier echten Agentensitzungen.
- **Pluginbau:** In einer temporären Kopie wurde genau eine künstliche Kontextdatei mit `klassifizierung: vertraulich` ergänzt. `installation/bauen.sh 0.0.0-probe` lief mit Exit 0 und kopierte sie inhaltlich unverändert ins gemeinsame Plugin. Der Bauschritt besitzt noch keine Auswahl nach Empfängerrechten. Keine realen vertraulichen Daten wurden verteilt; die Probe zeigt eine fehlende Grenze im Gerüst, keinen nachgewiesenen Vorfall.
- **GitHub-Schutz am 05.11.:** `gh api repos/enving/kobetriebssystem/branches/main/protection` liefert PR-Pflicht, 0 erforderliche Freigaben, `require_code_owner_reviews: false`, `required_status_checks: null`, `enforce_admins: true`. `gh api repos/enving/kobetriebssystem/rules/branches/main` liefert `[]`. Im getrackten Stand gibt es keine `.github/`-Dateien. Der Schutz verhindert direkte Pushes; ein unabhängiges Qualitäts- oder menschliches Regeländerungstor ist damit nicht technisch nachgewiesen. Die menschliche Zuständigkeit in `AGENTS.md` gilt trotzdem.
- **Archon lokal:** CLI v0.13.2, Commit `b8d01782`, SQLite. `workflow test --help` sagt ausdrücklich, dass Fixtures keinen Anbieter ansprechen und keinen Lauf anlegen. Damit lässt sich Kontrollfluss prüfen; Live-Rechte, Modellqualität und Wiederaufnahme eines echten Laufs sind dadurch nicht belegt.

### A. Drei Verantwortungsbereiche, auch wenn zunächst alles auf einem Rechner läuft

**Gemeinsame Arbeitsgrundlage:** freigegebene Regeln, Skills, allgemeine Begriffe und veröffentlichbares Firmenwissen. Git ist dafür geeignet. Für eine fachliche Aussage gibt es eine zuständige Quelle; sie muss nicht zwangsläufig Git sein. Wenn ein Prozess bereits verbindlich in SharePoint gepflegt wird, verweist die Vorlage darauf oder erzeugt eine nachvollziehbare, versionierte Ableitung. Eine zusätzliche, manuell gepflegte Wahrheit wäre ein Rückschritt.

**Persönliche Arbeit:** Ein Mensch nutzt einen Agenten in seiner zugelassenen Umgebung. Persönliche Notizen, Rohchats und Präferenzen werden nicht durch Nutzung automatisch Unternehmenswissen. Auch eine zentral gehostete Oberfläche kann im Auftrag dieser Person handeln; „lokal/Cloud“ und „Person/Dienstidentität“ sind verschiedene Achsen. Für Mitarbeitende sollte die vertraute Oberfläche genügen. Git, Pull Requests und Konfiguration sind ein Wartungsweg, kein Pflichtwissen jeder Person.

**Unbeaufsichtigte Arbeit:** Ein konkreter Auftrag erhält Quellen, technische Möglichkeiten, Ergebnisort, Verantwortlichen und einen nachvollziehbaren Zustand. Zeitplan oder Ereignis starten diesen Auftrag. Die Engine führt ihn aus und macht Warten, Fehler und Wiederaufnahme sichtbar. Sie entscheidet weder die fachliche Wahrheit noch die Unternehmensberechtigungen.

Das sind Verantwortungsgrenzen, kein Auftrag zum Bau von drei neuen Diensten. Ein Agent kann innerhalb seines Auftrags frei recherchieren, rechnen und Entwürfe verbessern. Seine Zugriffsmöglichkeiten und Außenwirkungen werden außerhalb seiner eigenen Begründungen begrenzt. Diese Kombination erhält die Stärke guter Modelle, ohne jeden Arbeitsschritt vorzuschreiben. Herstellererfahrungen zu [Harness Engineering](https://openai.com/index/harness-engineering/) und [lang laufender Arbeit](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) unterstützen die Bedeutung einer lesbaren Umgebung und überprüfbarer Übergaben; sie beweisen noch keine Eignung für diesen Firmenfall.

### B. Leserechte allein lösen den Informationsfluss nicht

Der Vorschlag in §3, zentrale Routinen unter einem eigenen Konto laufen zu lassen, ist eine gute Betriebsvereinfachung, aber als Sicherheitskriterium unzureichend. Auch ein Dienstkonto kann zu viel lesen. Umgekehrt kann eine zentral laufende Aufgabe korrekt mit einer eingeschränkten, delegierten Nutzeridentität arbeiten.

Entscheidend sind **Quellen, Zweck, Empfänger und tatsächliche technische Rechte**. Wenn ein Agent aus einem vertraulichen Termin eine allgemeine Anleitung erzeugt, kann schon der Entwurf am gemeinsamen Ergebnisort Informationen offenlegen. „Nur Entwurf“ reduziert die Verbindlichkeit, nicht die Vertraulichkeit.

Für die erste Version empfehle ich deshalb einen einfachen Zuschnitt: Das Basis-Plugin enthält nur Wissen, das alle seine vorgesehenen Empfänger lesen dürfen. Vertrauliche Inhalte bleiben in den berechtigten Quellsystemen bzw. in bereits getrennten, zugelassenen Arbeitsbereichen. Rollen können bei der Auswahl helfen; sie ersetzen keine individuellen Quellrechte. Für zentral geteilte Ergebnisse nur gemeinsam freigegebene Quellen nutzen. Eine weitergehende Freigabe abgeleiteten Wissens ist ein eigener fachlicher Vorgang, keine automatische Folge einer Zusammenfassung.

Eine Markerprüfung beim Bauen wäre ein nützlicher zusätzlicher Test. Sie kann jedoch unbekannt klassifizierte, falsch markierte oder aus vertraulichen Quellen abgeleitete Inhalte nicht zuverlässig erkennen. Ebenso sind Dateirechte, Konnektorrechte und verfügbare Werkzeuge tatsächlich zu testen. Grobe OAuth-Scopes erlauben nicht immer eine Einschränkung auf einen einzelnen Auftrag; diese Einschränkung darf dann nicht behauptet werden. [MCP-Sicherheitsempfehlungen](https://modelcontextprotocol.io/specification/latest/basic/security_best_practices) erläutern zusätzliche Grenzen bei Proxys und Autorisierung.

Ein gemeinsames Repository löst die Leseaufteilung nicht über `CODEOWNERS`: [GitHub vergibt Repository-Rollen](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization). Änderungsfreigaben sind keine Sichtbarkeitsfilter für Dateien. Ein gefiltertes Paket schützt zudem nur, wenn Empfänger nicht zugleich auf das vollständige Quellrepo oder andere Paketvarianten zugreifen können. Vertrauliches wird deshalb nicht zunächst gesammelt und anschließend durch Promptanweisungen versteckt.

### C. Ein gemeinsamer Auftragsrahmen, keine universelle Schrittfolge

Hier widerspreche ich §3 ausdrücklich: „Eine Engine muss jede Routine mit einem Ablauf abbilden“ ist kein sinnvolles Ausschlusskriterium. Ein Wochenbericht, eine Termin-Nachbereitung und die Prüfung einer Änderung dürfen unterschiedliche Abläufe haben. Gemeinsam brauchen sie ein verständliches Ergebnis, eine Zuständigkeit, erlaubte Wirkungen und einen Nachweis. Ob die Engine dafür einen oder mehrere Workflows benötigt, ist nachrangig.

Auch ein eigenes `launchd`-Skript mit SQLite ist nicht automatisch die einfache Lösung. Sobald es Sperren gegen gleichzeitige Läufe, Wiederholungen, wartende Freigaben und unklare Schreibresultate verwaltet, entsteht eine selbst zu wartende Engine. Umgekehrt rechtfertigt ein einzelner Wochenbericht noch kein ausgefeiltes Workflow-System. Zuerst einen Weg tatsächlich benutzen; erst eine zweite reale Aufgabe zeigt, welche Teile sich wiederholen.

Wichtige Fragen vor unbeaufsichtigtem Betrieb: Wird dasselbe Ereignis zweimal verarbeitet? Was passiert bei Abbruch nach dem Schreiben, aber vor der Erfolgsmeldung? Gilt eine Freigabe noch, wenn Entwurf, Empfänger oder Quellenstand geändert wurden? Kann eine neue Sitzung anhand des gespeicherten Ergebnisses korrekt fortsetzen? Ein unklarer Schreibausgang verlangt Abgleich mit dem Zielsystem, nicht blindes Wiederholen. Ein verweigerter Zugriff ist kein Anlass, einen anderen Zugang zu suchen. Für jeden Fehlerfall muss klar sein, ob automatisch wiederholt, begründet gewartet oder beendet wird.

Diese Eigenschaften möglichst aus vorhandenen Plattformen nutzen. Noch keine universelle Auftrags-API, keinen Adapterbaukasten und keine eigene Queue für diese leere Vorlage implementieren.

### D. Prüfung muss am Ergebnis hängen

Ein zweiter Agent ist nützlich, wenn er eine echte Gegenprüfung leisten kann. Nur Ergebnis plus Kriterien reichen für Tatsachenbehauptungen häufig nicht: Der Prüfer benötigt auch die zulässigen Belege, deren Stand und relevante Werkzeugresultate. Ein frischer Kontext reduziert gemeinsame Vorannahmen, ein anderes Modell kann andere Fehler finden; beides garantiert keine Unabhängigkeit oder Richtigkeit.

Messbare Eigenschaften prüft Code: gültige Verweise, vorgeschriebene Felder, erlaubte Dateipfade, eingehaltene Mengen oder unveränderte geschützte Dateien. Inhaltliche Vollständigkeit und Widersprüche können ein Modell benötigen. Fachliche Stichproben kalibrieren dieses Urteil. [Anthropics Evaluationsleitfaden](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) beschreibt diese Kombination und die Grenzen unkalibrierter Modellprüfer.

Ich würde nicht jeden kleinen Entwurf durch zwei Modelle schicken. Die Prüfintensität hängt an Fehlerfolgen und bisheriger Erfahrung mit der Aufgabe. Eine reine Formatierung braucht andere Prüfungen als eine gemeinsame Wissensänderung. Gemessen wird letztlich, wie oft ein Ergebnis ohne fachliche Reparatur verwendbar ist und wie viel menschliche Nacharbeit verbleibt.

Die Gegenprüfung empfiehlt menschlichen Review für alle Änderungen an Evals. Das ist mir zu pauschal. Zu schützen sind besonders Berechtigungen, verpflichtende Prüftore und bestehende Abnahmekriterien gegen eigenmächtige Abschwächung. Zusätzliche Tests und gewöhnliche Verbesserungen können im autorisierten Agentenprozess entstehen. Wer diese Grenzen technisch verwaltet, darf nicht derselbe unbeschränkte Ausführungsweg sein, dessen Ergebnis gerade geprüft wird. `CODEOWNERS` wirkt nur zusammen mit einer entsprechend erzwungenen Review-Regel. Bestehende Projektregeln wurden dafür nicht geändert.

### E. Lernen braucht eine kontrollierte Übergabe

Die Lernschleife ist der wertvollste Teil der Idee, wenn aus einer Korrektur eine überprüfte Verbesserung statt einer weiteren allgemeinen Anweisung entsteht. Zunächst unterscheiden: War die Quelle falsch, fehlte Kontext, war der Skill unklar, war das Werkzeug begrenzt oder war es eine einmalige Präferenz? Sonst wächst `AGENTS.md` bei jedem Fehler, obwohl die Ursache unverändert bleibt.

Persönliche Rohchats müssen dafür nicht zentral gesammelt werden. Ein freigegebener Verbesserungsvorschlag kann den Fehler, einen geeigneten anonymen Prüffall und die betroffene Quelle enthalten. Die in `AGENTS.md` geregelte Zustimmung bleibt maßgeblich. Bei Übernahme wird die zuständige Quelle geändert; vorhandene Prüffälle zeigen, ob anderes Verhalten schlechter wird. Ein Paket sollte seinen Quellstand und seine Version erkennen lassen. Laufende Sitzungen und installierte Plugins übernehmen Änderungen nicht zwingend im selben Augenblick; ein Wechsel oder Rollback muss nachvollziehbar sein.

Die Behauptung „Lernschleife braucht keine Engine“ in §3 gilt für die unmittelbare Korrektur im Chat. Sobald Vorschläge über Sitzungen hinweg gesammelt, geprüft und wieder vorgelegt werden, braucht es einen ausgeführten Ablauf und gespeicherten Stand. Dieser kann auf einem vorhandenen Ticket- oder PR-System beginnen. Eine weitere Aufgabenliste ist dafür nicht nötig.

### F. Auswahl der Ausführung nach der Arbeit

- **Archon:** plausibler lokaler Versuch für einen verantwortlichen Operator, besonders wenn kontrolliertes Warten und Wiederaufnahme gebraucht werden. Die aktuelle [Sicherheitsdoku](https://archon.diy/reference/security/) nennt Ausführung ohne interaktive Werkzeugfreigaben und ausdrücklich keine Mandantentrennung. Die [Anbietermatrix](https://archon.diy/reference/provider-capabilities/) zeigt unter anderem unterschiedliche Unterstützung für Hooks und Werkzeugfilter. Ein Git-Worktree ist keine Sicherheitsgrenze zum übrigen Benutzerkonto. Die Webseite kann dem installierten Release voraus sein. Meine Empfehlung ist daher ein begrenzter Versuch in passender Umgebung, keine Freigabe als Unternehmensplattform und kein Fork.
- **GitHub Actions:** passend für deterministische Repository-Prüfungen und überschaubare, repo-nahe Aufträge. Für diesen Bedarf kann der OS-Check zunächst ganz ohne KI auskommen. Als allgemeiner, verlässlicher Geschäftstakt ist `schedule` ungeeignet: GitHub dokumentiert [Verzögerungen und möglicherweise verworfene Läufe](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule). Ausbleibende Arbeit benötigt dann einen gesonderten Abgleich.
- **GitHub Agentic Workflows (`gh-aw`):** bislang fehlender Kandidat für agentische Repopflege. Markdown wird in Actions übersetzt; ein lesender Agent schlägt Änderungen vor, getrennte Jobs führen zugelassene Schreiboperationen aus. Das [Sicherheitsmuster](https://github.github.com/gh-aw/introduction/architecture/) passt besser als ein Agent mit pauschalem Schreibzugriff. Es löst nicht automatisch Firmenrechte, fachliche Richtigkeit oder sichere Ausgaben. In der aktuellen Doku kann Threat Detection im Standard-Warnmodus trotzdem prüfbare Ausgaben veröffentlichen. [Staged Mode](https://github.github.com/gh-aw/reference/staged-mode/) unterdrückt eingebaute Ausgaben, ist aber keine Sandbox für eigene Skripte oder externe Werkzeuge. Nur Doku geprüft; nicht installiert und kein Lauf gestartet.
- **Vorhandene Unternehmensautomatisierung:** Bei fachlichen Ereignissen aus Mail, Kalender oder ERP ist die bereits betriebene Plattform zuerst zu prüfen. Ein KI-Schritt kann dort einen begrenzten Teil bearbeiten. **Korrektur zur Tabelle in §3:** n8n ist nicht grundsätzlich vom Git-Weg ausgeschlossen; es dokumentiert [Git-basierte Source Control auf Business/Enterprise](https://docs.n8n.io/source-control-environments/). Das macht Export, laufenden Datenbankstand und deklarativen Auftrag noch nicht identisch. Kein Anlass, eine neue Plattform einzuführen, wenn der Betrieb bereits eine passende hat.

Die Software-Factory würde ich hier nicht einführen. Der Grund ist ihr Software-Lebenszyklus, nicht die Tatsache, dass dieses Repo Text enthält. Text lässt sich durchaus auf Quellen, Widersprüche und richtige Zuordnung prüfen. Portables Markdown ist außerdem nur ein Teil der Austauschbarkeit: Werkzeugrechte, Sessions, Ausgabeformate und Tests bleiben an die konkrete Laufzeit gebunden.

### G. Nächster Schritt mit Nutzen und Abbruchpunkt

**Mein Vorschlag:** Einen vorhandenen Arbeitsvorgang über eine ganze Strecke beherrschen, bevor die Vorlage erweitert wird. Für die Pflege dieses Repos ist ein deterministischer OS-Check ein sinnvoller erster Nutzen. Er muss bekannte Sicherheitslücken gesondert anzeigen und darf „keine unerwartete Abweichung“ nicht zu „sicher“ umdeuten. Die Verteilung ausschließlich geeigneter Inhalte und der Schutz wichtiger Prüftore wären die ersten gezielten technischen Verbesserungen. Die dafür nötigen Regel-/Schutzänderungen bleiben gesonderte menschliche Entscheidungen.

Für die Unternehmensidee genügt danach ein eng begrenzter, fiktiver Vorgang als Demonstrator, sobald seine fachlichen Kriterien gewählt sind: beispielsweise aus einer freigegebenen Besprechungsnotiz einen belegten Aufgabenentwurf für genau den passenden Empfängerkreis erstellen. Zuerst interaktiv, dann unverändert im Hintergrund. Das ist ein Vorschlag, keine Reaktivierung der pausierten Testfirma und kein neuer Benchmark. Fehlende Information, ungeeigneter Empfänger und ein doppelter Eingang sind aussagekräftiger als ein großer Funktionsvergleich von Engines.

**Erfolg:** Die Person erhält ein verwendbares Ergebnis mit nachvollziehbaren Quellen und wenigen echten Entscheidungen. Gemessen werden Nacharbeit, Fehlfreigaben, verlorene/doppelte Arbeit und unerledigte Rückfragen. Mehr Skills, Tokens oder Agenten sind kein Erfolgskriterium. Wenn die Routine mehr Pflege oder Prüfaufwand erzeugt, als sie abnimmt, bleibt sie interaktiv oder wird vereinfacht.

**Nicht belegt:** echter Archon-Lauf mit Unterbrechung/Fortsetzung, Produktivfähigkeit von `gh-aw`, Rechtevererbung realer Unternehmenskonnektoren, Ende-zu-Ende-Verteilung auf Mitarbeitergeräten und betrieblicher Nutzen mit echten Anwendern. Die lokalen Proben belegen ausschließlich die oben genannten Grenzen.

## 5. Fortsetzung: Oberfläche und Gesamtbild (05.11., Opus 5.5)
Tristans Skizze, Rakazo als Oberfläche, Gegenprüfung von §4 und fehlende Teile: [architektur/bericht-2026-11-05.md](architektur/bericht-2026-11-05.md).
