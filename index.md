Diese strukturierte und nach **Funktionsbereichen** gruppierte Übersicht macht sofort deutlich, welcher Ordner oder welche Datei zu welchem Zweck und Themenbereich gehört:


| Funktionsbereich                 | Element (Ordner / Datei)                       | Typ                | Zweck & Zugehörigkeit                                              |
| -------------------------------- | ---------------------------------------------- | ------------------ | ------------------------------------------------------------------- |
| **1. Steuerung & Governance**    | `AGENTS.md`                                    | Regelwerk          | Übergreifende Grundregeln für das Verhalten aller Agenten         |
|                                  | `CLAUDE codex etc. .md`                        | Modell-Guide       | Spezifische Wegweiser und Instruktionen für das primäre LLM       |
|                                  | `README.md`                                    | Dokumentation      | Zentrale Einstiegs- und Funktionsübersicht für das Team           |
|                                  | `SICHERHEIT.md`                                | Richtlinie         | Vorgaben zu Datenschutz, Zugriffsschutz und Compliance              |
| **2. Agenten & Workflows**       | `.agents/skills/`                              | Modul-Verzeichnis  | Sammlung modularer Fähigkeiten und Funktionserweiterungen          |
|                                  | `automatisierungen/`                           | Workflow-Ordner    | Strukturierte Einzelaufträge und Abläufe pro Routine              |
| **3. Wissensbasis (`kontext/`)** | `index.md`                                     | Inhaltsverzeichnis | Zentraler Einstieg in die interne Dokumentation                     |
|                                  | `landkarte.md`                                 | Referenz           | Übersicht und Verknüpfung zu Daten außerhalb des Repositories    |
|                                  | `[Fachbereiche]/` *(admin, firma, sales etc.)* | Domänen-Wissen    | Fachspezifische Ablagen für organisatorische und operative Inhalte |
| **4. Plattform & System**        | `installation/`                                | Rollout            | Betriebssystem als Plugin bauen, prüfen, an alle Geräte verteilen  |
|                                  | `plugins/`                                     | Schnittstelle      | Externe, zusätzliche Plugins für die Agenten-App                   |
|                                  | `system/`                                      | Kontroll-Ebene     | Prüfprogramme, Validierungsskripte und automatisierte Sperren      |
| **5. User-Kompass**              | `user-kompass/<name>/`                         | Mitarbeiter-Ebene  | Eigene Anweisungen, Ziele, Logbuch, Beiträge; fließen nur verallgemeinert per PR zurück |
|                                  | `prompts/`                                     | Bibliothek         | Gemeinsame Prompt-Bibliothek, rollenbasiert verteilt              |
| **6. Doku**                      | `Übergabe.md`                                  | Stand              | Offene Fragen, nächste Schritte, Test-Branch                       |
|                                  | `docs/`                                        | Entwurf            | Anmerkungen, Recherche, Szenarien, Beobachtungen |
|                                  | `automatisierungen/takt.md`                    | Taktplan           | Welche Routine wann läuft, Auftrag je Routine                      |
