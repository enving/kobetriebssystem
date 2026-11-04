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
| 8 | Lernschleife | Datenbasis des OS-Checks unklar (nur PRs? alle Chats?) → festlegen. Personenbezogene Daten in Entwürfen; Checkliste in SICHERHEIT.md. Vorschlag Datenbasis: [recherche §3](recherche.md), Punkt 6. | `automatisierungen/os-check.md`, `SICHERHEIT.md` | ◐ |
| 9 | „So arbeitet…“ | Ist „Agent“ das lokale Claude Code pro Mitarbeiter oder ein zentraler? Szenarien als Tabelle durchgehen (Slack zentral?). | `docs/szenarien.md` | ◐ |

## Abgleich mit dem Vergleichsmaterial (Stand 2026-11-04, Opus 5.5)
Neue Fassung des Vergleichsmaterials geprüft: Abbildungen byteweise gleich, Text bis auf einen Werbesatz gleich. Struktur, Verhaltensregeln, Ampel, Skill-Gerüst mit `evals/` und Kontext-Frontmatter sind in der Vorlage abgebildet. Zwei Lücken:

| # | Stelle | Lücke | Umsetzung | Status |
|---|---|---|---|---|
| 10 | Automatisierungen | `takt.md` ist leer. Das Vergleichsmaterial nennt sechs Routinen: Kontext-Ernte (täglich), Freigaben abarbeiten (stündlich), Termin-Nachbereitung, Podcast-Nachbereitung, Kontext-Pflege (wöchentlich), OS-Check (wöchentlich). Für die Vorlage mindestens Kontext-Ernte, Kontext-Pflege und OS-Check als Beispielaufträge, ausgeschaltet. Engine dafür: [recherche §3](recherche.md) (Bewertung und Test, nicht entschieden). | `automatisierungen/takt.md`, `automatisierungen/_vorlage.md` | ☐ |
| 11 | Agent/Prüfer | Der zweite Agent, der gegen „Fertig heißt …“ prüft, steht nur als Satz in der Skill-Vorlage. Offen: Wie wird er aufgerufen (Subagent, Hook, eigener Lauf), mit welchem Auftrag, und wo landet sein Befund (Logbuch)? | `.agents/skills/_vorlage/SKILL.md`, `AGENTS.md`, `system/` | ☐ |

Offene Fragen: siehe [Übergabe.md](../Übergabe.md).
