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
6. **Lernschleife:** Einordnen, Ja und PR passieren im Chat und brauchen keine Engine. Automatisieren lässt sich der wöchentliche OS-Check. Als Datenbasis (Anmerkung 8) bietet sich die Logbuchzeile aus `AGENTS.md` Regel 6 an („Lernschleife: <Muster> → … einmalig“): ab drei gleichen Mustern ein Vorschlag, höchstens drei je Woche. [OFFEN: Laut `persoenlich/_vorlage/logbuch.md` liegt das Logbuch bei der Person, nicht im zentralen Repo. Ein zentraler OS-Check sieht es nur, wenn die Zeilen per PR oder Export zurückfließen.]

### Vorgeschlagener Test (Prüffall für #4)
**OS-Check der Vorlage selbst**, ohne Firmendaten und deshalb im öffentlichen Repo unbedenklich. Code führt `system/tests/pruefen.mjs` aus, prüft Links und Frontmatter, listet die Aufträge mit Status und prüft im Lauflog, ob alle gelaufen sind. KI bündelt die Befunde zu höchstens drei Vorschlägen, ein zweites Modell prüft gegen „Fertig heißt …“, Ergebnis ist ein Entwurfs-Issue plus Logbuchzeile. Einmal als Archon-Workflow am Mac, einmal als GitHub Action. Verglichen werden: Zeilen eigener Code und Konfiguration, Abhängigkeiten, Zeit bis zum ersten sauberen Lauf, Lesbarkeit des Laufprotokolls, Weg der Rückfrage, Fortsetzen nach Abbruch.
**Abbruch für Archon:** Der Ablauf lässt sich nicht als **ein** Workflow mit der Auftragsdatei als Eingabe bauen, oder der erste saubere Lauf dauert länger als zwei Stunden. `archon serve` ist für uns am Mac zulässig, als Voraussetzung der Vorlage nicht. Leistet die Action dasselbe, wird keine Engine eingeführt; Archon wird dann nur für die Testfirma erneut geprüft.

### Fallen
- Zeitplanaufgaben der App: Forschungsvorschau, Takt mindestens stündlich, Zweige `claude/…` per Ruleset begrenzen. [OFFEN: Ob Hooks aus dem Repo (`system/hooks/`) in diesen Läufen greifen, ist nur aus Sekundärquellen bekannt.]
- Archon: Der Takt liegt außerhalb des Repos; `takt.md` bleibt die Quelle, die Trigger-Datei wird daraus erzeugt. `autoResumeOnQuotaReset` ist standardmäßig an. Codex hat über Archon laut Anbietermatrix keine Werkzeugfilter und Hooks ([Matrix](https://archon.diy/reference/provider-capabilities/)). Version vor 1.0.
- GitHub Actions im öffentlichen Repo: 60-Tage-Abschaltung, kein eigener Runner.
- Jede Engine: erst die Prüffälle, dann der Zeitplan, sonst entsteht automatisiert Ausschuss.
