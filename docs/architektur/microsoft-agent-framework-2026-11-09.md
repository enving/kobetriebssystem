# Microsoft Agent Framework für KoBetriebssystem

> **Vermerk 10.11.2026:** Hermes als MVP-Adapter gestrichen ([PRD](../../PRD.md), „Entschieden“ Nr. 6). Dieses Dokument bleibt als damaliger Befund unverändert.

**Recherche und Einschätzung Claude Opus 5.5, 09.11.2026.** Anlass: Tristan will das Framework als eigenes MVP, „because
it's big and it's probably interesting for also our requirements for ISO 42001“ ([PRD](../../PRD.md) „Entschieden“ Nr. 11).
Gelesen: GitHub-API, README und Beispiele im Repo am Stand
[`924a6e5`](https://github.com/microsoft/agent-framework/tree/924a6e50ec0336f3c965ee8b1151c54085888b6e). Nichts installiert,
kein Modelllauf. Den Umfang des MVP führt [PRD §6b](../../PRD.md#6b-mvp-2-microsoft-agent-framework).

## Was es ist (Beleg)

- Open-Source-Bibliothek von Microsoft für Agenten und Abläufe mit mehreren Agenten, in Python und .NET; Go liegt in einem
  eigenen Repo. Lizenz MIT. Repo seit 28.04.2025; am 09.11.2026 rund 14.600 Sterne und 905 offene Issues. Stabile Versionen
  kommen etwa wöchentlich, zuletzt python-1.25.0 (07.11.2026) und dotnet-1.28.0 (06.11.2026).
- Nachfolger von Semantic Kernel und AutoGen; das README verlinkt Umstiegsanleitungen für beide.
- Bausteine laut [README](https://github.com/microsoft/agent-framework/blob/924a6e50ec0336f3c965ee8b1151c54085888b6e/README.md):
  mehrere Modellanbieter, Middleware, Abläufe als Graph mit Checkpoints, Streaming, menschlicher Freigabe und Zurückspulen,
  Hosting in Azure AI Foundry, OpenTelemetry, Agenten als YAML-Datei, Skills, eine Entwickleroberfläche (DevUI).
- [`create_harness_agent`](https://github.com/microsoft/agent-framework/tree/924a6e50ec0336f3c965ee8b1151c54085888b6e/python/samples/02-agents/harness)
  baut einen fertigen Agenten: Werkzeugschleife, Verlauf nach jedem Modellaufruf, Kontextverdichtung, Aufgabenliste,
  Plan- und Ausführungsmodus, Dateigedächtnis je Sitzung, Skills aus Dateien, Shell-Werkzeug, Werkzeugfreigabe mit
  Dauerregeln und heuristischer Selbstfreigabe (ab Werk an) und OpenTelemetry. Jede Funktion lässt sich abschalten.
- [Skills](https://github.com/microsoft/agent-framework/blob/924a6e50ec0336f3c965ee8b1151c54085888b6e/docs/decisions/0030-agent-skills-design.md):
  Namen und Beschreibungen stehen im Systemprompt, den Inhalt holt das Modell schrittweise über bis zu drei Werkzeuge.
  Ob unsere `SKILL.md` unverändert passen, ist ungeprüft.
- [FIDES](https://github.com/microsoft/agent-framework/tree/924a6e50ec0336f3c965ee8b1151c54085888b6e/python/samples/02-agents/security),
  als experimentell gekennzeichnet: Abwehr eingeschleuster Anweisungen nach Costa et al. 2025
  ([arXiv 2505.23643](https://arxiv.org/abs/2505.23643)). Inhalte tragen Labels für Vertrauenswürdigkeit und Vertraulichkeit.
  Eine Middleware verfolgt die Labels und blendet nicht vertrauenswürdige Inhalte aus, eine zweite blockiert Werkzeugaufrufe,
  die gegen die Richtlinie verstoßen, oder verlangt eine Freigabe. Ein eigenes Label bindet Personendaten an Mandant und
  Person und lässt sie nur zu passenden Zielen fließen. MCP-Werkzeuge können automatisch gelabelt werden. Die Beispiele
  setzen Azure AI Foundry voraus.

## Was das für unsere Anforderungen heißt (Einschätzung)

| Anforderung | Was das Framework bietet | Grenze |
|---|---|---|
| Steuerung aus Git ([Abgleich §3](abgleich-ai-first-2026-11-06.md)) | Agenten als YAML, Skills aus Dateien | eigener Adapter nötig, wie für Hermes und Pi |
| Leitplanken im Code (L26, S16 bis S19) | Middleware vor jedem Werkzeugaufruf; FIDES-Labels für Vertrauliches und Personendaten | FIDES ist experimentell und wirkt nur auf gelabelte Inhalte |
| Freigaben und Rechte (L6, L25, L27, S15) | Werkzeugfreigaben mit Dauerregeln; an Personen gebundene Richtlinien | kein Rollenmodell einer Firma; Identität aus Azure oder selbst gebaut; Selbstfreigabe ab Werk an |
| Routine mit Rückfrage und Fortsetzen (L15, S12) | Abläufe mit Checkpoints und menschlicher Freigabe; Erweiterung für dauerhafte Läufe | genau eine Wirkung bei doppelten Ereignissen selbst prüfen |
| Nachweise (L18, ISO/IEC 42001) | Traces über OpenTelemetry, Freigaben, Checkpoints | Rohstoff, kein Managementsystem; Zuordnung zur Norm in [#2](https://github.com/enving/kobetriebssystem/issues/2) |
| Lernen nach Rolle (S17) | Dateigedächtnis je Sitzung, abschaltbar | prüfen, was gespeichert wird |
| Betrieb (L19) | Bibliothek im eigenen Prozess, optional Hosting in Foundry | wöchentliche Versionen und 905 offene Issues bedeuten Pflegeaufwand |
| Mitarbeitende ohne Terminal (L4) | DevUI für Entwicklung | kein Arbeitsplatz für Mitarbeitende |

**Einordnung:** Für Mitarbeitende ändert das Framework nichts; dort bleiben Claude und Codex (PRD „Entschieden“ Nr. 9). Für
Firmen-Agenten ist es neben Pi der Kandidat, der Leitplanken nicht nur als Text, sondern als Code und Label mitbringt. Ob das
hält, zeigt erst S19; ein Versprechen im README ersetzt keine Messung.

## Nicht geprüft

Hosting in Foundry, Agent 365 und Entra stehen nicht im MVP 2 und wurden nicht gegen die aktuelle Doku geprüft.
