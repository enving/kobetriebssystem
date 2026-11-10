# Harness für firmeneigene Agenten: Pi, pi-durable, DeepSeek Harness, Harness², DeepAgents

> **Vermerk 10.11.2026:** Hermes als MVP-Adapter gestrichen ([PRD](../../PRD.md), „Entschieden“ Nr. 6). Dieses Dokument bleibt als damaliger Befund unverändert.

**Recherche und Einschätzung Claude Opus 5.5, 07.11.2026.** **Entschieden (Tristan, 07.11.):** Firmen-Agenten wie der
Änderungs-Prüfer laufen als Pi in Sandcastle, schon im MVP; Mitarbeitende nutzen verbreitete Werkzeuge (Claude, Codex);
DeepSeek Harness und Copilot liegen auf dem Parkplatz ([PRD](../../PRD.md) „Entschieden“ Nr. 9, §11). Nur Doku, READMEs und Quelltext gelesen,
nichts installiert. Anlass: Neben dem persönlichen Agenten jeder Person (Claude Code, Codex, Hermes) braucht das
Betriebssystem eigene Agenten der Firma, etwa einen Prüfer, den OS-Check und Routinen. Dafür war ein schlanker Harness
gefragt, bei dem sich genau einstellen lässt, was der Agent darf. Lücke: [PRD](../../PRD.md) L25.

**Nachprüfung GPT-6.1-sol, 07.11.2026:** Die vier ausdrücklich gewünschten Projekte an ihren Originalquellen
abgeglichen; Quellenstände unten. Weiterhin kein Modelllauf und kein Leistungstest. Pi Durable ist eine eigene
Bibliothek im Pi-Monorepo, kein Schalter, der die Coding-CLI nachträglich dauerhaft macht. Dans `disler/durable-pi`
ist eine darauf aufgebaute Beispielanwendung und wird davon getrennt betrachtet.

**Umfang:** Dieser Bericht und seine nächsten Prüfschritte gehören zur technischen Projektarbeit in
KoBetriebssystem. Die Auswertung der Videos und ihre Aufbereitung für eine Folge sind ein eigenständiger Kanalauftrag.

## Zwei Arten von Prüfer

Beim Prüfer lohnt eine Unterscheidung, weil sie über Ort und Identität entscheidet (Einschätzung):

- **Ergebnis-Prüfer:** prüft einen Entwurf gegen „Fertig heißt …“, bevor die Person ihn sieht. Er braucht die Quellen, die
  die Person sehen darf, und läuft deshalb bei der Person, mit ihren Rechten (Unteragent oder lokaler Lauf).
- **Änderungs-Prüfer:** prüft einen Verbesserungsvorschlag an das Betriebssystem (Skill-Änderung und Prüffall), bevor ein
  Mensch merged. Er braucht nur das Repo, keine Personendaten, und ist damit der erste echte Firmen-Agent.

Für beide passt dieselbe Agentenkarte mit `name`, `description`, `tools` und `model`. Dieses Format nutzen
Claude-Code-Unteragenten und das Pi-Beispiel `subagent` in ähnlicher Form. Eine gemeinsame fachliche Definition ist ein
Ausgangspunkt; Gleichheit von Werkzeugnamen, Modellkennungen und wirksamen Rechten muss der jeweilige Adapter prüfen.

## Kandidaten

| | Rechte genau einstellbar | ohne Bildschirm | nach Abbruch fortsetzen | Windows | Grundlast | Reife |
|---|---|---|---|---|---|---|
| [Pi](https://github.com/earendil-works/pi) (MIT) | Werkzeugauswahl, Erweiterungen; keine eigene Betriebssystemgrenze. MCP gesondert filtern oder deaktivieren | `-p`, `--mode json`, `--mode rpc`, SDK | gespeicherten Gesprächskontext fortsetzen; kein Nachweis dauerhafter Werkzeug-/Auftragszustände wie bei pi-durable | CLI dokumentiert | nicht gemessen; standardmäßig read, bash, edit, write | Releases vorhanden; konkret gewählten Stand pinnen |
| [pi-durable](https://github.com/earendil-works/pi/tree/main/packages/durable) (MIT) | Werkzeuge und Hooks je Unterhaltung; eine eigene Umgebung ist nicht automatisch eine Sandbox | Bibliothek; Host-Anwendung nötig | ja: gespeicherte Tasks, `resume()`, deduplizierte Eingabe über `requestId`, `sleepUntil`; externe Seiteneffekte gesondert absichern | hier nicht betrieblich geprüft | nicht gemessen; abhängig von Registry, Werkzeugen und Prompt | experimentell, API ändert sich ohne Ankündigung |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (MIT) | Sandbox-Modi für Dateieffekte, Freigaben und Plugins. Netzwerk und Prozesssicht außerhalb dieser Modi; Windows teils nur teilweise durchgesetzt | `dsh headless`, SDK, ACP, Zeitplan | Gespräche fortsetzbar; gleichwertige Absturz-/Replay-Garantie hier nicht belegt | Backends dokumentiert, nicht getestet | nicht gemessen; verschiedene Profile | Developer Preview, kein Sicherheitsaudit |
| [Harness²](https://github.com/google-research/harness2) (Apache-2.0) | – | Stapellauf | – | nein | – | Forschungswerkzeug: verbessert Prompts, Skills und Unteragenten eines bestehenden Harness anhand von Benchmarks; kein Betriebs-Harness |
| [DeepAgents](https://github.com/langchain-ai/deepagents) (MIT) | Regeln für eingebaute Dateiwerkzeuge; eigene Werkzeuge, MCP und Shell gesondert begrenzen | Python-SDK, eigene Host-Anwendung | LangGraph-Checkpointer und Freigabe-Unterbrechungen; dauerhafte Speicherung konfigurieren, externe Effekte absichern | hier nicht geprüft | nicht gemessen; eingebaute Dateiwerkzeuge und Unteragenten beachten | Quellstand 0.7.34, Paket als Beta klassifiziert; siehe Vertiefung unten |
| [Amplio](https://github.com/google-deepmind/amplio) (Google DeepMind) | keine Allowlist in der Doku gefunden | `amplio headless run/resume` | ja | offen | unbekannt | früh, kein Release |

Separater Befund: Hermes Agent v0.23.0 verbrauchte laut Betreiber auf einem Testgerät für „hi“ rund 15.000 Tokens
(07.11.2026). Das ist keine Vergleichsmessung: Modell, Konfiguration, Tokenzählung und Auftrag wurden für die anderen
Kandidaten nicht gleich gehalten. Die früheren Pi-/DeepSeek-Schätzungen sind deshalb entfernt.

Pi und DeepSeek Harness laden `AGENTS.md` sowie Skills aus `.agents/skills` nach dem Agent-Skills-Muster. Bei DeepAgents
werden die Quellen im SDK ausdrücklich angegeben (siehe unten). Die
Sperr-Erweiterung [`system/hooks/pi-sperre.js`](../../system/hooks/pi-sperre.js) passt zu Pi.

**Anmeldung:** Für firmeneigene Agenten API-Schlüssel. Anthropic beschreibt die Abo-Anmeldung als gedacht für Claude Code
und die eigenen Apps; wer Produkte oder Dienste baut, soll API-Schlüssel nutzen
([Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)). Die Bedingungen für ChatGPT/Codex sind nicht
geprüft.

## Einschätzung

1. **Pi ist der engste Kandidat für Firmen-Agenten.** Er läuft ohne Bildschirm und ist über SDK/RPC einbindbar;
   Windows ist dokumentiert. Grundlast und Kartenübertragbarkeit sind zu prüfen. Die Werkzeugauswahl begrenzt das
   Modellangebot; MCP, verschachtelte Aufrufe und Erweiterungen müssen mitgeprüft werden. Es fehlen eine eingebaute
   Sandbox und Pfadgrenzen. Erweiterungen laufen mit vollen Rechten. Sobald ein Firmen-Agent schreibt oder fremde Inhalte liest, braucht er eine
   Abschottung außen herum (OpenShell, Container oder Sandcastle, siehe [Laufzeitvergleich](laufzeitvergleich-2026-11-05.md)).
2. **pi-durable** löst genau das Fortsetzen von Routinen (L15), ist aber experimentell. Erst nehmen, wenn eine Routine es
   braucht, und Version festpinnen.
3. **DeepSeek Harness** als Alternative für einen Arbeitsplatz mit Oberfläche und konfigurierbaren Plugins prüfen.
   Es bringt eigene Sandbox-/Freigabebausteine mit; eine stärkere Gesamtabschottung als bei Pi mit externer Sandbox ist
   daraus nicht belegt. Developer Preview und die zusätzliche Cordis-Integration sind Betriebsaufwand.
4. **Harness²** ist kein Ausführer, könnte aber später helfen, Skills und Prüfer anhand der Prüffälle zu verbessern.

**Vorschlag fürs MVP:** Der Ergebnis-Prüfer bleibt Unteragent in der Sitzung der Person. Der Änderungs-Prüfer läuft als
Pi-Agent am Mac, ohne Bildschirm, mit `read,grep,find,ls`, ohne MCP und ohne ungeprüfte Erweiterungen, mit begrenztem
Dateizugriff, API-Schlüssel und einem anderen Modell als der Bearbeiter. Das wäre ein Harness mehr als bisher geplant;
Tristan hat am 07.11. zugestimmt, mit Sandcastle als Abschottung.

## Weiterer Prüfkandidat: DeepAgents

Auftrag vom 07.11.2026: Zusätzlich zu den bereits betrachteten Ansätzen
[LangChains DeepAgents](https://github.com/langchain-ai/deepagents) für die Firmen-Agenten ansehen.
Arbeitsauftrag und Status: [Issue #27](https://github.com/enving/kobetriebssystem/issues/27).
Die beschlossene MVP-Auswahl Pi in Sandcastle bleibt bestehen.

**Vertiefung GPT-6.1-sol, 07.11.2026:** Originaldoku und Python-Quelltext am unten festgehaltenen Commit gelesen.
Keine Installation, kein Modelllauf, kein Absturz- oder Isolationstest. Die Befunde beschreiben dokumentierte und
im Quelltext erkennbare Mechanismen; ihre Wirkung in unserem Betrieb ist noch zu prüfen.

### Einordnung und Betrieb

DeepAgents ist ein Ausführungs-Harness auf LangChain/LangGraph. LangGraph liefert gespeicherten Laufzustand und
Unterbrechungen für Freigaben. Damit überschneidet es sich mit Pi plus Pi Durable; Harness² bleibt die getrennte
Verbesserungswerkstatt. Das SDK kann im eigenen Prozess oder Container laufen, ohne zusätzliche LangSmith-SaaS-Pflicht.
Das Python-Paket hat trotzdem `langsmith` als Bibliotheksabhängigkeit. Modellanbieter und Sandbox sind gesonderte
Betriebsentscheidungen. [SDK-Betrieb](https://docs.langchain.com/oss/python/deepagents/overview#self-host-with-the-sdk),
[Paketmanifest](https://github.com/langchain-ai/deepagents/blob/9c5d330893e0580ece0422511248d1048373cd7f/libs/deepagents/pyproject.toml).

### Rechte und Abschottung

`tools=` ergänzt eingebaute Werkzeuge. Eine kurze Liste erzeugt daher keinen nur lesenden Prüfer. Im geprüften
Quellstand lassen sich Dateiwerkzeuge über eine eigene `FilesystemMiddleware(tools=[...])` tatsächlich entfernen;
ein Harness-Profil kann außerdem den automatisch ergänzten allgemeinen Unteragenten deaktivieren. Jede verbleibende
Unteragenten-Konfiguration braucht dieselbe Rechteprüfung.
[Agent-Aufbau](https://github.com/langchain-ai/deepagents/blob/9c5d330893e0580ece0422511248d1048373cd7f/libs/deepagents/deepagents/graph.py).

`permissions=` begrenzt eingebaute Dateiwerkzeuge. Die erste passende Regel gilt; ohne Treffer ist der Zugriff erlaubt.
Für unseren Prüfer wären erlaubte Lesepfade und eine abschließende Sperre für alles Übrige nötig. Eigene Werkzeuge,
MCP, direkte Backend-Aufrufe und Shell-Ausführung erhalten dadurch keine gleichwertige Grenze. Eigene Regeln eines
Unteragenten ersetzen die geerbten Regeln vollständig. Für Sandbox-Backends erklärt die Doku diese Dateiregeln
ausdrücklich für nicht anwendbar.
[Dateiregeln und Geltungsbereich](https://docs.langchain.com/oss/python/deepagents/permissions).

`FilesystemBackend(root_dir=..., virtual_mode=True)` begrenzt Dateipfade, bietet aber keine Prozess- oder
Netzwerkisolation. **Quellenwiderspruch:** Die abgerufene Backend-Doku nennt `virtual_mode=False` als Standard;
der geprüfte Quelltext setzt bereits `True`. Für eine Probe den Wert ausdrücklich setzen. `LocalShellBackend`
führt Befehle auf dem Host aus. Eine äußere Sandbox bleibt nötig; DeepAgents in Sandcastle ist hier nicht nachgewiesen.
[Backend-Doku](https://docs.langchain.com/oss/python/deepagents/backends),
[geprüfte Implementierung](https://github.com/langchain-ai/deepagents/blob/9c5d330893e0580ece0422511248d1048373cd7f/libs/deepagents/deepagents/backends/filesystem.py).

### Freigabe, Neustart und doppelte Ereignisse

`interrupt_on` kann vor Werkzeugaufrufen anhalten und Freigabe, Änderung oder Ablehnung abwarten. Dafür braucht es
einen Checkpointer; fortgesetzt wird mit `Command(resume=...)` und derselben `thread_id`. Für einen Prozessneustart
braucht es dauerhafte Speicherung, etwa SQLite oder PostgreSQL. Das häufig gezeigte `MemorySaver`/`InMemorySaver`
verliert seinen Zustand beim Neustart.
[Freigaben](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop),
[Speicherung](https://docs.langchain.com/oss/python/langgraph/persistence).

Eine `thread_id` ist kein Beleg für die Entdoppelung eingehender Aufträge. Wiederholte Ausführung nach Absturz kann
externe Wirkungen wiederholen. Die Anwendung braucht eine dauerhaft gespeicherte Ereigniskennung und Werkzeuge,
bei denen Wiederholungen dieselbe Wirkung haben oder vom Zielsystem erkannt werden. Freigabeidentität und Bindung
an Vorschlag/Quellversion gehören ebenfalls in unseren Adapter.
[Wiederholung und externe Wirkungen](https://docs.langchain.com/oss/python/langgraph/fault-tolerance#retry-boundaries-and-idempotency).

### Vorhandene Regeln und Skills

Im SDK lassen sich vorhandene Regeldateien über `memory=[...]` und Skill-Ordner über `skills=[...]` einbinden;
`SKILL.md` folgt dem Agent-Skills-Format. Das ersetzt keine Prüfung unserer Werkzeugnamen, Hooks und Rollenrechte.
Im geprüften Memory-Lader werden fehlende Dateien übersprungen und bereits geladene Inhalte aus dem Zustand
wiederverwendet. Deshalb muss der Adapter Pflichtquellen und deren Hashes vor dem Start und beim Fortsetzen prüfen.
Für die Probe Firmenregeln und Skills nur lesbar einbinden, damit Änderungen weiter über den vorhandenen PR-Weg laufen.
[Skills](https://docs.langchain.com/oss/python/deepagents/skills),
[Memory-Lader](https://github.com/langchain-ai/deepagents/blob/9c5d330893e0580ece0422511248d1048373cd7f/libs/deepagents/deepagents/middleware/memory.py).

**Einschätzung:** Für den begrenzten Änderungs-Prüfer ergibt sich aus der Recherche kein Anlass, die MVP-Auswahl
zu ersetzen. DeepAgents wird interessanter, wenn ein konkreter Ablauf gespeicherten Zustand, mehrere Unteragenten
und Freigaben gemeinsam braucht. Dafür sind eine Python-Host-Anwendung, Backend-/Werkzeugadapter, Freigabezugang,
Ereignisverwaltung und Betrieb der Zustandsablage einzurichten. Python-, Paket- und Abhängigkeitsstände sowie
Repo-Commit und Freigabeversion müssen festgehalten werden. Umfang des Adaptercodes, Tokenkosten und Laufzeit
sind ungemessen; „weniger Aufwand als Pi Durable“ ist bisher nicht belegt.

### Gegenprobe für denselben Firmen-Prüfer

Offen, keine Testergebnisse: Den oben beschriebenen Pi-Prüfer-Auftrag mit gleichem Modell, Quell-Commit,
erfundenem Vorschlag, bekannten Fehlern und Budget wiederholen. Zusätzlich muss die Probe zeigen:

1. Effektiv verfügbare Werkzeuge erfassen; Schreiben, fremde Pfade und Ausweichen über Unteragenten scheitern.
2. Fehlende Pflichtregel stoppt vor dem Modellaufruf; geladene Regel- und Skill-Versionen sind nachweisbar.
3. An einer harmlosen Freigabe anhalten, Prozess beenden und mit dauerhaftem Speicher fortsetzen;
   Ablehnung und eine Freigabe zur falschen Vorschlagsversion dürfen nichts ausführen.
4. Dasselbe Ereignis zweimal zustellen und einen Absturz nach einer simulierten externen Wirkung auslösen;
   die Wirkung darf nur einmal entstehen.
5. Ohne LangSmith-Dienst starten; Netzwerkziele erfassen, Quellenzugriff begrenzen und Rückkehr zu den
   festgehaltenen Paket-/Repo-Versionen prüfen.

Die Recherchepunkte aus Issue #27 sind damit eingeordnet. Laufzeitprüfung, Identität und Anmeldung bleiben offen;
das Issue und das PRD-Lückenregister werden dadurch nicht geschlossen.

## Welche Lücken das tatsächlich betrifft

Zuordnung und Vorschlag: GPT-6.1-sol, 07.11.2026. Keine Lücke wird durch diese Doku als geschlossen markiert.

| Bedarf | Geeigneter Ansatz | Verbleibende Arbeit |
|---|---|---|
| Regeln und passender Kontext gelangen in die Sitzung (L2, L3) | Pi-Adapter lädt vorhandene Quellen; DeepSeek-Profile als Alternative | Vorrang persönlicher/Firmenregeln klären; Quellenstand und tatsächlich geladene Ressourcen nachweisen |
| Ergebnis-/Änderungsprüfung (L10, L11, L25) | begrenzter Pi-Lauf; frische Ressourcen statt geerbter persönlicher Sitzung | Quellen und Kriterien übergeben, erlaubte Zugriffe begrenzen, bekannte Fehler erkennen; deterministische Prüfungen bleiben Code |
| Hintergrundarbeit wartet und setzt nach Neustart fort (L15) | pi-durable mit persistenter Speicherung und eigener Host-Anwendung | Auslöser, Identität, Freigabezustand, Stop, doppelte Ereignisse und externe Seiteneffekte prüfen |
| Gemeinsame Skills werden besser (L20, L21, L22) | Harness² als isolierte Verbesserungswerkstatt | eigene Prüffälle anbinden; Änderung als Vorschlag prüfen und freigeben; persönliche Erkenntnisse zulässig verallgemeinern |
| Versionen verteilen und zurücknehmen (L5) | Pi-Pakete unterstützen feste Git-/npm-Stände | Pflichtpaket muss nachweislich vorhanden sein; Pi läuft bei fehlgeschlagener Paketinstallation laut Doku weiter. Ausrollnachweis und Rücknahme selbst prüfen |
| Kontext aus Mail/Chat und Software am Endgerät (L23, L24) | vorhandene Konnektoren/CLIs bzw. Gerätedienst an den gewählten Harness anbinden | keiner der vier liefert dadurch automatisch vollständigen Kontext oder Zugriff auf lokale Fachanwendungen |
| Firmenrechte und inhaltsarme Zähler (L6, L12, L16, L17) | gesonderte fachliche und technische Grenze | Werkzeugauswahl ist kein Rollenmodell; dauerhafte Speicherung ist kein Nachweis zulässiger Datennutzung |

Für **KoKompass** wäre Pi ein weiterer austauschbarer Nutzer der Methode und CLI. Das Gedächtnis und seine
Pflegequelle bleiben beim Kompass. Für **KoBetriebssystem** passt Pi zu begrenzten Firmenaufträgen; pi-durable
ergänzt bei belegtem Bedarf deren Laufzustand. DeepSeek ist ein alternativer Ausführungsunterbau. Harness² arbeitet
auf einer anderen Ebene: Es verändert einen bestehenden Harness, mit festen Modellgewichten, über
Propose–Probe–Compose und aufbewahrte Lernergebnisse. Das ist kein Training der Modellgewichte und keine fertige
Firmenlaufzeit. Sein Standardaufbau nutzt OpenCode oder Codex, nicht Pi; eine Pi-Verbindung wäre zusätzliche Arbeit.

## Konkrete Gegenprobe vor einer Auswahl

Erst denselben begrenzten Prüfer-Auftrag mit Pi und DeepSeek vergleichen: identisches Modell, identische erlaubte
Quellen, derselbe Quell-Commit, dieselben Erfolgskriterien und ein festgelegtes Kostenlimit. Konfiguration und
Paketversionen erfassen. Einen bekannten fachlichen Fehler einbauen, einen fehlenden Pflichtkontext erkennen lassen
und fremde Testdaten technisch unzugänglich halten. Messen: gefundene/übersehene Fehler, unbelegte Aussagen,
Nacharbeit, Tokenverbrauch, Kosten und Laufzeit. Es gibt hier noch keine Ergebnisse dieses Versuchs.

Pi Durable anschließend an **einem** wartenden Auftrag prüfen: Prozess während eines Werkzeugaufrufs beenden,
Speicher erneut öffnen, doppelte Eingabe schicken und eine noch ausstehende menschliche Freigabe wiederherstellen.
`requestId` verhindert doppelte Aufnahme derselben Eingabe; es garantiert keine einmalige externe Wirkung. Nur als
`replay: "safe"` deklarierte Werkzeuge werden nach Unterbrechung erneut ausgeführt. Andere liefern `interrupted`;
auch sichere Werkzeuge brauchen für externe Effekte eigene Idempotenz.

Harness² getrennt an einer kopierten Skill-Fassung untersuchen. Verbesserungs- und zurückgehaltene Prüffälle trennen,
Modell und Budget festhalten, keine Produktionsregeln automatisch übernehmen. Das Repo dokumentiert offenen
Netzzugriff und beim Codex-Ausführer abgeschaltete Sandbox; Prüfkriterien und Antworten dürfen darüber nicht erreichbar
sein. Ein Benchmarkgewinn aus dem Paper ersetzt keinen Nachweis an den eigenen Aufgaben.

## Quellenstand der Nachprüfung

GitHub-HEADs am 07.11.2026 ermittelt; Doku-/Quellvergleich, keine installierten Versionen. Die vorhandene Tabelle ist
ein Recherche-Snapshot, kein zweiter Konfigurationsstandard.

- **Pi/Pi Durable:** `085c84e98e7f4c950f2be606466fff4f75d8fe7c`;
  [SDK](https://github.com/earendil-works/pi/blob/085c84e98e7f4c950f2be606466fff4f75d8fe7c/packages/coding-agent/docs/sdk.md),
  [CLI und MCP-Werkzeugauswahl](https://github.com/earendil-works/pi/blob/085c84e98e7f4c950f2be606466fff4f75d8fe7c/packages/coding-agent/docs/cli.md),
  [Sicherheitsgrenzen](https://github.com/earendil-works/pi/blob/085c84e98e7f4c950f2be606466fff4f75d8fe7c/packages/coding-agent/docs/security.md),
  [Pakete](https://github.com/earendil-works/pi/blob/085c84e98e7f4c950f2be606466fff4f75d8fe7c/packages/coding-agent/docs/packages.md),
  [Durable-Vertrag](https://github.com/earendil-works/pi/blob/085c84e98e7f4c950f2be606466fff4f75d8fe7c/packages/durable/README.md).
- **DeepSeek Harness:** `fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159`;
  [Architektur](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/docs/architecture.md),
  [Sandbox-Vertrag](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/docs/subsystems/sandbox.md),
  [Sicherheitsstatus](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/SAFETY.md).
- **Harness²:** `6868817518876de8fd170c6a8354daca273b6191`;
  [Aufbau](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/README.md),
  [Experimente und Netzzugriff](https://github.com/google-research/harness2/blob/6868817518876de8fd170c6a8354daca273b6191/docs/EXPERIMENTS.md).
- **Dans Beispielanwendung:** `37165c619573dbaf425463038bbffecfe576beec`;
  [durable-pi, On-Call-Demo](https://github.com/disler/durable-pi/blob/37165c619573dbaf425463038bbffecfe576beec/README.md).
  Das Beispiel beschreibt Log-Auslöser, Klassifikation, Agent und Freigabe vor Deployment. Nicht lokal ausgeführt;
  Kosten- und Zeitangaben des Autors wurden nicht als eigene Messwerte übernommen.
- **DeepAgents (Python):** `9c5d330893e0580ece0422511248d1048373cd7f`, Manifestversion `0.7.34`, Python `>=3.11,<4.0`, MIT,
  Beta-Klassifikation. Commit per GitHub-API ermittelt; die oben verlinkten Implementierungen und das Manifest wurden
  von diesem Stand gelesen. Online-Doku am 07.11.2026 abgerufen; sie ist nicht an diesen Commit gebunden.
  Kein installiertes Paket und keine Zusage, dass der Manifeststand einem veröffentlichten Release entspricht.
