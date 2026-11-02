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
