# Anmerkungen → Umsetzung

Status: ☐ offen · ◐ Gerüst da · ☑ erledigt

| # | Stelle | Anmerkung | Umsetzung | Status |
|---|---|---|---|---|
| 1 | GitHub | Prompt-Bibliothek (RAF-Schema), gemeinsam pflegbar, ggf. Sync nach SharePoint; Prompts/Skills fließen per PR zurück, werden nur an passende Rollen verteilt; Wissen aus Chats → LLM-Wiki; Agent recherchiert und hinterlässt Notizen; Grundregeln: was nie geteilt wird. Test im Branch mit Testfirma (siehe Übergabe.md). | `prompts/`, `AGENTS.md` | ◐ |
| 2 | Agent | „Drei Dinge“ (2. Agent, Logbuch, Slack) fürs Betriebssystem eher überflüssig. Wichtiger: **zwei Ebenen** zentral vs. Mitarbeiter (Logbuch, Prompts, Skills); Verhältnis unklar. Im Vergleichsmaterial liegen Berichte evtl. in einem externen Tool – das Logbuch ist dort also evtl. gar nicht im Repo. Zentraler „Single Point of Truth“ meist unrealistisch → saubere Aufteilung. Rechte erben über Shell des Nutzers; Cloud-Agent bekommt Rechte explizit. | `persoenlich/`, `docs/szenarien.md` | ◐ |
| 3 | Skills | Erinnert an Ontologie: Agenten notieren Fachbegriffe, klären mit Nutzer, PR → kontrolliertes Vokabular + Regeln zur Nutzung → Wissensgraph. Sync einzelner Ordner nach SharePoint via n8n/Power Automate. | `kontext/glossar/` | ◐ |
| 4 | Evals | Beispielfälle/Testdaten gehören in den Test-Branch, nicht in die blanke Vorlage. **Recherche:** Rechte pro Datei in GitHub/GitLab (CODEOWNERS, getrennte Repos, Branch-Schutz, kleine DB als Kompromiss?). | `.agents/skills/*/evals/`, [recherche §1](recherche.md) | ◐ |
| 5 | Kontext | Was aus den Digitalalchemisten-Folgen zum Kontextlayer übernehmbar ist: Fundstellen im Kompass in Übergabe.md, Vorschlag steht noch aus. | `kontext/`, `Übergabe.md` | ◐ |
| 6 | Tools | Lücken in Skills/Kontext können Tool-Infos an Unberechtigte bringen. Wie technisch ausgeschlossen? Mit kobench testen. | `SICHERHEIT.md` | ☐ |
| 7 | Regeln/Hook | Beispiel-Hooks ins Repo, per Plugin verteilen. Daten auf Endgeräten? Laufwerke sperren, Datenklassifizierung per Metadaten, Betriebsvereinbarung, skip-permissions, Startpfad, Managed Settings; Pi/OpenCode prüfen. | `system/`, `SICHERHEIT.md` | ◐ |
| 8 | Lernschleife | Datenbasis des OS-Checks unklar (nur PRs? alle Chats?) → festlegen. Personenbezogene Daten in Entwürfen; Checkliste in SICHERHEIT.md. | `automatisierungen/os-check.md`, `SICHERHEIT.md` | ◐ |
| 9 | „So arbeitet…“ | Ist „Agent“ das lokale Claude Code pro Mitarbeiter oder ein zentraler? Szenarien als Tabelle durchgehen (Slack zentral?). | `docs/szenarien.md` | ◐ |

Offene Fragen: siehe [Übergabe.md](../Übergabe.md).
