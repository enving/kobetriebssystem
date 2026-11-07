# Hermes, Rakazo und ein kleinerer Unterbau für KoBetriebssystem

**Bedarf zuerst (06.11.2026):** [Rückkehr zum AI-FIRST-Gedanken und zum gemeinsamen Lernen](../szenarien.md). Die technische Shortlist unten ist keine Auswahlentscheidung; zuerst ist der dort beschriebene fachliche Durchlauf zu klären.

Einschätzung und Recherche: GPT-6.1-sol, 05.11.2026. Zwei gleichzeitige Recherche-Agenten derselben Modellfamilie; tragende Befunde zusätzlich an Originalquellen geprüft. Die unabhängige Gegenprobe mit Claude Sonnet 5.5 scheiterte am API-Limit. Technischer Vorschlag, keine Auswahlentscheidung Tristans und keine neue Betriebsregel.

## Empfehlung

**KoBetriebssystem bleibt die laufzeitneutrale Betriebsführung. Für ausführende Agenten ist Pi mit OpenShell der engste neue Prüfkandidat. Vor dem Eigenbau einer Verwaltungsoberfläche sollte Paperclip geprüft werden.** Rakazo bleibt der nähere fertige Arbeitsplatz, Hermes ein Kandidat für persönliche Assistenz. Ein Wechsel zu Hermes allein schließt die Firmenlücken nicht.

Pi ist als austauschbarer Agentenkern sinnvoll. „Pi und alles andere selbst bauen“ würde allerdings Identitäten, Arbeitsaufträge, Freigabezustände, Laufhistorie, Wiederaufnahme und Verwaltung wieder zu unserer Aufgabe machen. Dafür gibt es bereits Bausteine. Die Kombination Paperclip → OpenShell → Pi ist hier **eine Architekturhypothese**, keine nachgewiesene fertige Integration. Für einen ersten Pi-Lauf braucht es Paperclip noch nicht.

## Ausgangspunkt aus den vorhandenen Ordnern

Gelesen: `README.md`, `AGENTS.md`, `kontext/index.md`, `kontext/landkarte.md`, `installation/README.md`, `installation/werkzeuge.md`, `system/hooks/pi-sperre.js`, `docs/recherche.md`, Architekturbericht §9–11 und die lokale Übergabe. Ergänzend die bestehenden Befunde in den Werkzeugordnern Hermes/Rakazo und die gezielten Kompass-Verweise.

Die erklärte Richtung: Firmenvorlage, zuerst selbst nutzen; Mensch beaufsichtigt und kann stoppen; wichtige Entscheidungen bleiben bei Menschen; Komponenten möglichst getrennt; Regeln und Skills werden zentral gepflegt; Rakazo ist Kandidat. Kontextschicht und Ontologie werden durch diesen Vergleich nicht wieder aufgemacht.

Im Repo existiert bereits eine Pi-Erweiterung mit Werkzeug-Sperrprüfung. Ihr eigener Kommentar benennt die Grenze: Textprüfung ersetzt keine Dateisystemrechte. Der vorhandene Pluginbau erzeugt ein Claude-Code-Paket; eine geprüfte Pi-/OpenShell-Verteilung entsteht daraus noch nicht. Neue Komponenten sollen diese fachlichen Quellen verwenden, keine zweite Regelablage begründen.

## Vergleich nach Verantwortung

Legende: „vorhanden“ bedeutet in Code/Dokumentation gefunden; keine Aussage über einen bestandenen Betriebtest.

| Baustein | Was er übernimmt | Passung | Was offen bleibt |
|---|---|---|---|
| Hermes | Persönlicher Agent, Chat-Gateways, Zeitpläne, Profile, Lernfunktionen | Eigene Assistenz in einem Vertrauenskreis | Firmenrechte und gegenseitige Abschottung; reproduzierbarer Rollout; geprüfter Rückweg |
| Rakazo | Gemeinsamer Arbeitsplatz, Spaces, Bot-Computer, Freigaben, Routinen und Audit | Fertige Oberfläche für Menschen und Bots | Zentraler rollenbasierter Git-Ausrollweg; Identitätszuordnung; alle Zugriffswege prüfen |
| Pi | Agentenschleife, Modelle, Werkzeuge, Erweiterungen, SDK/RPC und Sessions | Kleiner austauschbarer Ausführungskern | Hat selbst keine Sandbox und keine Firmenadministration |
| OpenShell | Sandbox, Datei-/Prozess-/Netzregeln, Zugangsdatenvermittlung, Gateway und Workspace-Rechte | Sicherheitsunterbau für den ganzen Pi-Prozess | Fachliche Aufgabensteuerung, Ergebnisprüfung und Anschluss an unsere Freigaben |
| Paperclip | Agentenverwaltung, Aufgaben, Ziele, Budgets, Freigaben und verschiedene Laufzeitadapter | Kandidat für die fehlende Verwaltungsoberfläche | Git als Pflegequelle durchsetzen; konkrete Sandbox-Anbindung; Rechte und Abbruch im Betrieb prüfen |
| OpenHands SDK | Agent, Remote-Agent-Server, Workspaces, Ereignisse und Bestätigungsrichtlinien | Alternative für die Software-Werkstatt | Allgemeiner Firmenarbeitsplatz und fachlicher Rollout bleiben Zusatzarbeit |

### Hermes gegen Rakazo, konkret

Hermes beschreibt sich ausdrücklich als persönlicher Einzelmandant. Ein Docker-Terminalbackend begrenzt Shell- und Dateiwerkzeuge; der Python-Prozess, MCP und Erweiterungen sind dadurch nicht mit eingeschlossen. Für den gesamten Agenten ist eine gesonderte Prozessisolation vorgesehen. Profile sind kein Nachweis gegeneinander gehärteter Mandanten. [Hermes-Sicherheitsmodell](https://github.com/NousResearch/hermes-agent/blob/e76fbd80be65ea5c1b89831f8d7aaedb713f5cac/SECURITY.md)

Die Profil-Distribution ist ein vorhandener Hinweg für Konfiguration und Skills. **Korrektur zur bisherigen Einschätzung:** Git-Ref-Pinning, SHA-Lockfile, Signaturen und Update-Dry-run werden noch als geplant beschrieben. Der Installer klont den Defaultbranch; beim Update bleibt die lokale Konfiguration standardmäßig erhalten. Außerdem hält `hermes pause` neue Arbeit an und beendet laufende Arbeit nicht. Das genügt nicht als allgemeiner sofortiger Notaus. [Distribution](https://github.com/NousResearch/hermes-agent/blob/e76fbd80be65ea5c1b89831f8d7aaedb713f5cac/website/docs/user-guide/profile-distributions.md), [Installer](https://github.com/NousResearch/hermes-agent/blob/e76fbd80be65ea5c1b89831f8d7aaedb713f5cac/hermes_cli/profile_distribution.py), [Pause](https://github.com/NousResearch/hermes-agent/blob/e76fbd80be65ea5c1b89831f8d7aaedb713f5cac/hermes_cli/subcommands/pause.py)

Bei Rakazo läuft Pi im API-/Worker-Prozess, außerhalb des Bot-Computers. Team-Bots teilen dessen Dateisystem; Private Computer bieten einen anderen Zuschnitt. Aktuell gibt es getrennte Chrome-Profile je Bot. Das trennt Cookies funktional, schützt sie aber nicht vor einem anderen Bot mit Shellzugriff auf denselben Computer. Optionale stdio-MCP-Prozesse laufen mit den Rechten von API/Worker, ebenfalls außerhalb des Bot-Computers. [Computerlaufzeit](https://github.com/elie222/rakazo/blob/045f6b747d79677ba55773dc27d5b08ffb497ee8/docs/computer-runtime.md), [Integrationen](https://github.com/elie222/rakazo/blob/045f6b747d79677ba55773dc27d5b08ffb497ee8/docs/self-host-integrations.md)

Rakazo hat Organisationsrollen und einen eigenständigen Auditlog; die Aussage „keine Teamverwaltung“ wäre zu pauschal. Zusätzliche OIDC-Scopes sind konfigurierbar, automatische Gruppen→Space-Zuordnung wurde nicht gefunden. Fleet-Werkzeuge ersetzen keinen zentralen Ausrollweg. **Korrektur zum Architekturbericht:** „fast vollständig“ war für eine Firmenlaufzeit zu stark; Spaces, SSO und Freigaben sind Teilfunktionen, keine Abnahme für den Unternehmenseinsatz. [Konten](https://github.com/elie222/rakazo/blob/045f6b747d79677ba55773dc27d5b08ffb497ee8/docs/self-host-accounts.md), [Audit](https://github.com/elie222/rakazo/blob/045f6b747d79677ba55773dc27d5b08ffb497ee8/docs/self-host-audit-log.md), [Fleet](https://github.com/elie222/rakazo/blob/045f6b747d79677ba55773dc27d5b08ffb497ee8/docs/fleet-management.md)

## Die neuen Prüfkandidaten

### 1. Pi plus OpenShell: vorhandener Weg statt eigener Sandbox

Pi bringt bereits SDK, JSONL-RPC, Erweiterungen und persistente Sitzungen mit. Git-Commits und genaue npm-Versionen lassen sich für Pakete festpinnen. Unsere Arbeit wäre damit die Einbindung dieser Funktionen, keine neue Agentenschleife. [SDK](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/sdk.md), [RPC](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/rpc.md)

Pi dokumentiert ausdrücklich mehrere Isolationswege. Bei OpenShell läuft der ganze Pi-Prozess einschließlich Erweiterungen in der Sandbox. Die Gondolin-Erweiterung lässt dagegen Pi auf dem Host und leitet ausgewählte Werkzeuge in eine VM; weitere Erweiterungswerkzeuge können weiter auf dem Host arbeiten. Für unsere Grenze ist der vollständige Prozess leichter nachzuvollziehen. [Pi v1.5.0: Containerization](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/containerization.md)

OpenShell bietet Netz-, Datei- und Prozessregeln sowie Vermittlung von Provider-Zugangsdaten. Das Gateway unterstützt OIDC, unter anderem Entra/Keycloak, Rollen und Workspace-Mitgliedschaften. Ein Plattformadmin darf über Workspace-Grenzen hinweg zugreifen; das Rollenmodell muss also passend konfiguriert und getestet werden. Der Pi-Start ist bereits dokumentiert: `openshell sandbox create --name pi-probe --from pi -- pi`. Das ist ein Dokumentationsbeispiel und wurde hier nicht ausgeführt. [OpenShell](https://github.com/NVIDIA/OpenShell), [Authentifizierung v0.1.7](https://github.com/NVIDIA/OpenShell/blob/v0.1.7/docs/how-it-works/gateways/authentication.mdx)

**Zwei konkrete Fallen:** Netzfreigabe für einen Host ist keine Freigabeprüfung einzelner Schreiboperationen; die dokumentierte L7-Prüfung steht standardmäßig auf `audit` und braucht `enforcement: enforce`, wenn sie blockieren soll. Pi kann fehlende konfigurierte Pakete beim Start überspringen und weiterlaufen. Pflichtregeln müssen daher vor dem Workerstart auf Vollständigkeit und Quellstand geprüft werden; ein fehlendes Schutzpaket muss den Start verhindern. Das ist ein vorgeschlagener Abnahmefall, noch keine eingebaute Sperre. [OpenShell-Sicherheitskonfiguration](https://github.com/NVIDIA/OpenShell/blob/v0.1.7/docs/security/best-practices.mdx), [Pi-Pakete](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/packages.md)

OpenShell ist ein junges 0.1.x-Projekt. Die konkrete Mac-/Colima-Kombination und Ressourcenlast wurden nicht getestet. Die dokumentierte Architektur trägt die Auswahl für eine Probe, keine Freigabe als Firmeninfrastruktur.

### 2. Paperclip: vor einem eigenen Manager prüfen

Paperclip hat einen konkreten Pi-Adapter mit Skill-Auswahl und lokalen beziehungsweise entfernten Ausführungszielen. Der aktuelle Agenten-Konfigurationsvertrag umfasst Skill-Versionpins, Werkzeugprofile, Berechtigungen und Wiederherstellen von Revisionen. Das trifft mehrere der heutigen Lücken direkt. [Pi-Adapter](https://github.com/paperclipai/paperclip/blob/d3713d827f70ddba63a323e57c562384dbd648ba/packages/adapters/pi-local/src/server/execute.ts), [Konfigurationsvertrag](https://github.com/paperclipai/paperclip/blob/d3713d827f70ddba63a323e57c562384dbd648ba/doc/agent-configuration-yaml.md)

**Der Widerspruch zu unserem Git-Ansatz:** Paperclip erklärt seine Datenbank und Ressourcendienste zur maßgeblichen Laufzeitquelle. YAML im Editor ist noch kein GitOps-Ausrollweg. Unser Repo müsste freigegebene Versionen über einen kleinen Abgleich bereitstellen und Abweichungen erkennen; Regeln dürfen nicht unbemerkt in Repo und Oberfläche unabhängig gepflegt werden. Ob diese Integration klein bleibt, ist die entscheidende Probe.

Ausführung kann lokal, über SSH oder Sandbox erfolgen. Der vorhandene Kubernetes-Provider ist **Alpha**. Seine Standard-Netzrichtlinie kann FQDNs nicht eng ausdrücken; eine FQDN-Freigabe öffnet für diesen Lauf öffentliches IPv4-TCP auf 80/443. Cilium kann genauer filtern. „Sandbox unterstützt“ allein ist deshalb kein ausreichender Befund. [Ausführungsziele](https://github.com/paperclipai/paperclip/blob/d3713d827f70ddba63a323e57c562384dbd648ba/packages/adapter-utils/src/execution-target.ts), [Kubernetes-Provider](https://github.com/paperclipai/paperclip/blob/d3713d827f70ddba63a323e57c562384dbd648ba/packages/plugins/sandbox-providers/kubernetes/README.md)

**Releasegrenze:** geprüftes `main` ist `d3713d82`; neueste über die API gefundene Veröffentlichung ist `v2026.1023.0` vom 24.10. Dort existieren Pi-Adapter und Kubernetes-Provider, die gelesene neue YAML-Dokumentation dagegen nicht. Die gesamte heutige Funktionsmatrix ist daher keine Zusage für dieses Release. Einen veröffentlichten Stand vor dem Pilot festpinnen und dessen APIs erneut abgleichen. [Release](https://github.com/paperclipai/paperclip/releases/tag/v2026.1023.0)

#### Nachtrag 06.11.2026 (Claude Opus 5.5): Doku über das README hinaus gelesen

Stand `master` `7e3caa7b`, nur Doku gelesen, nichts installiert.

**Neue Tatsachen zum Git-Widerspruch.** Es gibt eine herstellerneutrale Paketspezifikation `agentcompanies/v1-draft`: Firma, Team, Agent, Projekt und Aufgabe als Markdown mit YAML-Frontmatter (`COMPANY.md`, `TEAM.md`, `AGENTS.md`, `PROJECT.md`, `TASK.md`), Skills bleiben `SKILL.md`. Grundsätze laut Spezifikation: „Markdown is canonical“, Git-Repos sind gültige Paketbehälter, fremde Verweise an feste Commits gebunden; Paperclip-eigene Felder (Adapter, Rechte, Budgets, Routinen-Auslöser) liegen getrennt in `.paperclip.yaml`. Wiederkehrende Aufgaben werden beim Import zu Routinen. Das ist ein **Import- und Exportformat**, kein laufender Abgleich: Für die Laufzeit bleiben Datenbank und Ressourcendienste maßgeblich. Skills aus Git werden mit vollem Commit-SHA und Wiederherstellungsrezept gespeichert, Läufe pinnen Skill-Versionen. ([Spezifikation](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/docs/companies/companies-spec.md), [Skill-Speicher](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/doc/skill-package-storage.md), [Konfigurations-YAML](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/doc/agent-configuration-yaml.md))

**Rechte und Sichtbarkeit.** Arbeit ist standardmäßig für die ganze Firma sichtbar; private Aufgaben und Projekte mit benannten Beteiligten gibt es, Audit-Logs bleiben firmenweit (nur Kennungen). Ein neuer Standard-Agent erhält ab Werk weitreichende Rechte: Agenten-Konfiguration lesen und ändern, Skills anlegen, Werkzeug-Verbindungen verwalten, Aufgaben zuweisen, `canCreateAgents: true`. Die Vorgabe `low_trust_review` begrenzt Agenten, die feindliche Eingaben lesen; laut eigener Doku ist das „containment, not privacy“. Die Doku erwähnt eine „EE“, in der Richtlinien bearbeitet werden können, die der Community Edition fehlen; welche Funktionen nur dort liegen, ist nicht geprüft. ([Rechtevorgaben](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/doc/agent-permission-defaults.md), [Vertrauensstufen](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/doc/LOW-TRUST-PRESETS.md), [Private Aufgaben](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/doc/ISSUE-PRIVACY.md))

**Agenten-Anbindung.** `codex_local` gibt jedem Agenten ein eigenes `CODEX_HOME` und verlinkt die ChatGPT-Abo-Anmeldung des Hosts; ein Host-API-Schlüssel wird ausgeblendet. `claude_local` arbeitet mit Abo-Login, `CLAUDE_CODE_OAUTH_TOKEN` oder API-Schlüssel und startet standardmäßig mit `dangerouslySkipPermissions: true`. Eine eigene Claude-Konfiguration je Agent ist nur für Sandbox-Ziele beschrieben (dorthin werden `settings.json` und `CLAUDE.md` des Hosts bereinigt hochgeladen). Für lokale Läufe folgt daraus vermutlich, dass Hooks, Skills und globale Anweisungen der Person mitlaufen; das ist nicht ausdrücklich dokumentiert und muss im Test geprüft werden. ([Claude-Adapter](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/docs/adapters/claude-local.md), [Codex-Adapter](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/docs/adapters/codex-local.md))

**Betrieb.** Ohne `DATABASE_URL` startet ein eingebettetes PostgreSQL 18. Betriebsarten `local_trusted` (ohne Login, nur localhost) und `authenticated` mit Bindung an `loopback`, `lan` oder `tailnet`. Telemetrie standardmäßig an. Schema-Migration 0423 in rund acht Monaten Projektlaufzeit, 6.458 offene Issues (GitHub-API, 06.11.). Zum Ausprobieren gibt es `npx paperclipai test-drive` (eigener temporärer Datenordner, kein Dienst); laut README mit API-Schlüssel. ([Betriebsarten](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/doc/DEPLOYMENT-MODES.md), [Datenbank](https://github.com/paperclipai/paperclip/blob/7e3caa7bac3f2c1a560158b28ec42381a153dfff/doc/DATABASE.md))

**Einschätzung (Claude Opus 5.5, 06.11.2026), Entscheidung: Tristan.** Gegen den Bedarf in [szenarien.md §3](../szenarien.md) deckt Paperclip laut Doku die meisten Zeilen ab, besser als die übrigen geprüften Kandidaten: Arbeit übergeben, gepinnte gemeinsame Skills, Zusammenarbeit mit Zuständigkeit und Freigaben, Routinen. Für „gemeinsam besser werden“ gibt es `skills:suggest-changes` mit Zustimmung, also Vorschlag → Freigabe → neue Version, aber in der Datenbank statt als PR. Drei Prüfsteine entscheiden:

1. **Git bleibt Quelle?** Lässt sich ein `agentcompanies`-Paket aus diesem Repo erneut importieren, ohne in der Oberfläche freigegebene Änderungen stillschweigend zu überschreiben, und lassen sich Abweichungen erkennen? Das ist das Tor „Update und Rücknahme“ oben.
2. **Enge Rechte ohne Bezahlversion?** Die Werksrechte eines Standard-Agenten sind für eine Firma zu weit. Ist ein enger Zuschnitt in der Community Edition möglich?
3. **Betreibbar?** Datenbank-Server, hohe Änderungsrate, eigener Abbruch im April 2026 (Kompass).

**Günstiger Schritt ohne Festlegung (Vorschlag):** Die Dateistruktur dieses Repos so ausrichten, dass sie als `agentcompanies/v1`-Paket lesbar ist. `AGENTS.md` und `SKILL.md` sind schon da, es fehlen etwa `COMPANY.md`/`TEAM.md` und eine Abbildung der Automatisierungen als wiederkehrende `TASK.md`. Dann bleibt KoBetriebssystem laufzeitneutral, und Paperclip wäre eine austauschbare Laufzeit, die das Repo importiert. Vorher prüfen, ob die Spezifikation nach `v1-draft` stabil wird. Ein `test-drive` lohnt erst, wenn die Bedarfsklärung eine Verwaltungsoberfläche verlangt; Abnahme wäre dann der Durchlauf aus [szenarien.md §4](../szenarien.md) plus die sechs Tore unten. Abbruch: Re-Import überschreibt freigegebene Änderungen ohne Hinweis, enge Rechte nur in der EE, oder die Einrichtung dauert länger als zwei Stunden.

### 3. OpenHands SDK: zweite Wahl für Softwareaufträge

Das modulare SDK trennt Agent, Tools, Agent-Server und Workspace; es bietet entfernte Ausführung und Bestätigungsrichtlinien. Der Agent-Server verwendet standardmäßig lokale Ausführung; Docker je Gespräch und API-Schlüsselauthentifizierung müssen passend eingeschaltet werden. [Server-Konfiguration](https://github.com/OpenHands/software-agent-sdk/blob/232d0b05fa5cd798c9c827d1a1c1aafa541757ad/openhands-agent-server/openhands/agent_server/README.md) Das kann für die OS-Werkstatt weniger Eigenbau als Pi bedeuten. Für allgemeine Büroarbeit liefert die Softwareausrichtung aber nicht automatisch passende Fachprozesse. Das SDK unter MIT ist vom gesamten OpenHands-Produkt mit gegebenenfalls anderen Unternehmensfunktionen zu unterscheiden. [SDK](https://github.com/OpenHands/software-agent-sdk), [Bestätigungsrichtlinien](https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/security/confirmation_policy.py)

### Weitere Ansätze, mit geringerem Vertiefungsgrad

- **Dify:** näher an einer Plattform für KI-Apps und modellierte Abläufe. Die aktuelle Lizenz ergänzt Apache-2.0 um Bedingungen für Mehrmandantenbetrieb; ein Tenant ist dort ein Workspace. Für eine mehrfach ausrollbare Vorlage keine ungeprüfte Standardbasis. Das ist die Wiedergabe der Lizenzbedingung, keine rechtliche Einordnung eines konkreten Geschäftsmodells. [Lizenz](https://github.com/langgenius/dify/blob/main/LICENSE)
- **OpenClaw:** ein persönliches Gateway ist keine Abkürzung zur gegenseitigen Abschottung unterschiedlicher Nutzer. Das eigene Sicherheitsmodell beschreibt diese Grenze ausdrücklich. [Sicherheitsmodell](https://github.com/openclaw/openclaw/blob/main/SECURITY.md)
- **LangGraph:** geeigneter Baustein für langlebige Abläufe mit gespeichertem Zustand und menschlicher Unterbrechung; ersetzt keine Sandbox oder Firmenverwaltung. Erst vertiefen, wenn ein konkreter Ablauf die vorhandene Steuerung überfordert. [Originaldoku](https://docs.langchain.com/oss/python/langgraph/overview)
- **Vorhandene Automation und GitHub:** deterministische Prüfungen bleiben Code. Repo-Aufträge können bei den vorhandenen Werkzeugen beginnen; die bestehenden Abgrenzungen in [Recherche §4](../recherche.md#architektur) bleiben relevant. Kein Anlass, für einen simplen Prüflauf einen allgemeinen autonomen Agenten zu bauen.

## Was wir selbst bauen würden

Ein schmaler Adapter statt einer neuen Plattform: Er liest den freigegebenen Quellstand, erstellt den erlaubten Zuschnitt für einen Agenten, startet einen begrenzten Auftrag und verknüpft Ergebnis und Nachweis. Er erfasst mindestens Quell-Commit, Paket-/Policy-Version, Identität, Lauf-ID und Ergebnisort. Die genaue Datenform wird erst bei einer Implementierung festgelegt; dieser Bericht ist kein zweites Konfigurationsschema.

Zurück kommen ein Ergebnis oder ein Verbesserungsvorschlag mit zulässigen Belegen. Der Agent ändert seine zentralen Regeln nicht selbst. Die vorhandenen Freigaben und PR-Prüfungen bleiben zuständig. Firmenkontext und personenbezogene Rohchats werden nicht als Teil der allgemeinen Vorlage verteilt.

Für den ersten Versuch genügen ein Ausführungsweg, ein schreibgeschützt bereitgestelltes Paket und ein Ergebnisort. Einen neuen Scheduler, eine Chat-Oberfläche, eigene Secrets-Verwaltung, ein Rollenverzeichnis oder ein allgemeines Workflow-Framework würde ich dafür nicht bauen. Die Komponenten können klare Grenzen haben, ohne sofort eine ganze Microservice-Landschaft zu betreiben.

**Stärkster Einwand gegen meinen Vorschlag:** Jede zusätzliche Verbindung erzeugt Wartungsarbeit. Wenn Paperclips Sandbox-Weg bereits genügt, wäre OpenShell daneben doppelte Steuerung. Wenn ein begrenzter Pi-Auftrag mit vorhandener Auftragsverwaltung genügt, wäre Paperclip zu viel. Deshalb beide erst getrennt prüfen und nur bei nachgewiesenem Nutzen verbinden. Es gibt hier keinen Beleg, dass die Kombination schon weniger Pflege als Rakazo kostet.

## Ein nützlicher Prüffall und sechs Abnahmetore

Vorschlag: Ein Agent prüft einen festgelegten Stand dieses öffentlichen Vorlagen-Repos und erstellt ausschließlich einen lokalen Befundbericht zu Struktur, Links und bekannten Grenzen. Keine private Wissensablage, keine fremde Firma, kein Senden und keine erneute Aktivierung bereits erledigter Aufträge. Anschließend derselbe Auftrag mit einem zweiten Agenten und einem anderen freigegebenen Skill-Zuschnitt.

| Tor | Versuch | Bestanden erst wenn |
|---|---|---|
| Paket und Zuständigkeit | Agent A bekommt Skill A; B bekommt Skill B; benötigtes Paket einmal weglassen | Sichtbare und erreichbare Ressourcen passen zum Zuschnitt; fehlendes Pflichtpaket verhindert Start; Quell-Hash steht im Nachweis |
| Abschottung | A versucht B-Datei, Hostpfad und nicht freigegebenen Netzhost zu erreichen | Alle negativen Zugriffe werden technisch blockiert und protokolliert; Erweiterungen/MCP werden einbezogen |
| Freigabe | Schreibversuch ohne Recht sowie Pause vor einem erlaubnispflichtigen Schritt | Kein Seiteneffekt vor einer berechtigten Freigabe; Entscheidung bleibt nach Neustart erhalten |
| Stop und Wiederaufnahme | Aktiven Lauf mit Kindprozess stoppen, danach Worker neu starten | Vorab festgelegte Abbruchgrenze eingehalten; keine weiterlaufenden Prozesse; kein zweiter Seiteneffekt beim Wiederaufnehmen |
| Update und Rücknahme | Paket v1 → v2 → v1; laufende Sitzung beobachten | Neue und laufende Sitzungen haben eindeutigen Stand; Rücknahme ist messbar; keine unbemerkte Mischkonfiguration |
| Ergebnis und Rückweg | Bekannten Fehler sowie vertraulichen Testmarker einfügen | Befund erkennt Fehler, Marker verlässt seinen erlaubten Ergebnisort nicht; nur zulässiger Vorschlag geht ins zentrale Review |

Abbruchkriterium: Erfordert diese begrenzte Probe einen dauerhaften großen Fork, mehrere doppelte Verwaltungsdienste oder einen eigenen kompletten Manager, wird der Aufbau vereinfacht. Zuerst wird ein fertiger Weg gegen diese Tore geprüft. Keine Aufwandsschätzung in Tagen ohne Umsetzungsprobe.

## Quellenstand, Lizenzen und Grenzen

Hermes: lokal `b200f5bc`, Upstream `e76fbd80`; Rakazo: lokal `eaca269c`, Upstream `045f6b74`. Pi: `d9af3d73`, Release v1.5.0; OpenShell: `71da34fc`, Release v0.1.7; OpenHands SDK: `232d0b05`, neueste gefundene Veröffentlichung v1.60.1; Paperclip: `d3713d82`, Release v2026.1023.0. Diese Stände wurden am 05.11.2026 ermittelt; lokale Installationen können älter sein. Kein vollständiger Versionsdiff. Pi, Hermes, Paperclip und OpenHands SDK nennen MIT; Rakazo und OpenShell Apache-2.0. Dify trägt Zusatzbedingungen. Modellanbieter und Konnektoren haben eigene Nutzungsbedingungen; kein Abonnement wurde als kostenlose Firmenlaufzeit vorausgesetzt.

**Nicht geprüft:** Modellqualität, Kosten, Installationsaufwand, Ressourcenlast, echte zweite Nutzer, Identitätsentzug, tatsächlicher Abbruch, Crash-Replay, produktiver Git-Abgleich oder Ende-zu-Ende-Verbindung zwischen Paperclip und OpenShell. Aus Selfhosting folgt weder europäische Datenverarbeitung aller Konnektoren noch rechtliche Konformität. Dieser Bericht enthält keine Rechtsbewertung; die gesetzlichen Abschnitte der README wurden nicht erneut geprüft.
