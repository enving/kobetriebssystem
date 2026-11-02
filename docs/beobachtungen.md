# Beobachtungen aus Vergleichsmaterial

Was in die Vorlage eingeflossen ist (✔) oder offen bleibt:

- ✔ **Repo-Struktur:** `AGENTS.md`, `CLAUDE.md`, `README.md`, `SICHERHEIT.md`, `.agents/skills/`, `automatisierungen/`, `kontext/` (index, landkarte, ein Ordner je Arbeitsgebiet), `installation/`, `plugins/`, `system/`.
- ✔ **AGENTS.md:** `[OFFEN: …]`-Markierung, „Ändere nie still“, Freigabe-Vermerk am Ergebnisort, Lernschleife-Eintrag im Logbuch. Die Regel-Mechanik der Lernschleife liegt besser in einer eigenen Regeldatei (z. B. `.claude/rules/skills.md`) als in AGENTS.md.
- ✔ **Ampel:** Kunden-/Personendaten ins Repo = rot; `main` technisch gesperrt; im Zweifel gelb; Entwürfe in Fremdtools mit Status „KI-Draft“.
- ✔ **Skill:** Ordner mit `SKILL.md` + `evals/` (`evals.json`, `ergebnisse.md`, `files/`). Frontmatter: `name`, langes `description` mit Trigger-Sätzen und Abgrenzung („Ein Objekt, ein Skill“), `metadata.besitzer`, `metadata.nutzt_kontext`.
- ✔ **Kontextdatei:** `beschreibung` + `geprueft` im Kopf, Quelle im Text als „[Ansage Name TT.MM.JJJJ]“, relative Links.
- ✔ **Taktplan** `automatisierungen/takt.md`: Routine / Takt / Auftrag.
- ✔ **Connector-Rechte:** je Tool „Immer erlauben / Nachfragen / Blockieren“.
- **Meldungen per Chat (Vorbild für Routinen):** gebündelt („5 zum Senden, 2 Entscheidungen“) mit Link zum Entwurf; Entscheidungen nummeriert mit Antwortoptionen a/b und Empfehlung, Antwort „1a 2b“ oder „alle wie empfohlen“; „Zu tun für dich“ getrennt.
- **Zeilengrenze** für den Text, den jede Sitzung zuerst lädt (Richtwert ca. 150): wird gemessen und gemeldet. In der Vorlage noch nicht gesetzt.
- **Ablauf:** Auslöser → Agent (liest, erstellt, Prüfer-Agent) → Ergebnis als Entwurf → Mensch; Lernschleife wirkt zurück auf Skill, Kontext, Regeln.
