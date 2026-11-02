# Übergabe (Stand 2026-11-02)

## Was das hier ist
Blanke Vorlage für ein KI-Betriebssystem – für **organisch gewachsene größere Mittelständler**, nicht für kleine Firmen. Bewusst Minimum, Plug-and-Play; Komplexität kommt erst durch Erkenntnisse aus dem Test.
Keine Beispielfirma, keine Beispiel-Skills (nur `_vorlage`-Dateien).

## Offene Fragen
1. **Kontext-Layer:** Was aus den Digitalalchemisten-Folgen zum Kontextlayer übernehmbar ist? Fundstellen im Kompass (`~/Documents/Dev/kompass`): `ideen/folge-16-kolibri-kontextlayer.md`, `ideen/folge-17-ki-wiki-konzern.md` (neun Konzern-Fragen: Rechte, Datenschutz, Betriebsrat, Freigabe …), `aufgaben/folge-wiki-je-rechteschicht-grenzen.md`, `aufgaben/serie-kontextlayer-harness-je-folge.md`, `entscheidungen/kontextlayer-zwei-wege-palantir.md` (Leck-Quote als Messgröße). Noch nicht ausgewertet.
2. **Aufteilung nach Rolle:** Ein zentrales Repo, Aufteilung über Plugins/Orchestrierung, Mitarbeitende sehen das Repo evtl. nicht? Wie genau, ist offen. Lese-Rechte pro Datei gibt es nach bisheriger Suche nicht (siehe `docs/recherche.md`, GitHub-Doku noch zu prüfen).
3. **Lokal oder zentral:** Meint „Agent“ das lokale Claude Code je Mitarbeiter oder einen zentralen Agenten? Szenariotabelle: `docs/szenarien.md`.
4. **Logbuch:** Wo liegt es? Im Vergleichsmaterial scheinbar in einem externen Tool, nicht im Repo; bei uns Ebene Mitarbeiter?
5. **OS-Check:** Welche Datenbasis (nur PRs, Logbücher, alle Chats)? Festlegen.
6. **Datenschutz:** Kontaktdaten externer Personen in Entwürfen und Logbuch; Checkliste in `SICHERHEIT.md`.
7. **Leck über Kontext-Lücken:** Gelangen Tool-Infos über Kontext/Skills an Unberechtigte? Mit kobench testen.
8. **Endgeräte und Hooks:** Hooks zur Pfad-/Laufwerkssperre und Klassifizierung sind als Entwurf angelegt (`system/`, `SICHERHEIT.md`); ungetestet auf echten Geräten. Offen: Daten auf Endgeräten? Betriebsvereinbarung, Managed Settings, Pi Agent und OpenCode prüfen.
9. **Prompt-Bibliothek:** RAF-Schema-Grundsätze nachtragen; Rückfluss per PR, rollenbasierte Verteilung.
10. **Zeilengrenze** für den Start-Kontext (Richtwert ca. 150 Zeilen) übernehmen?

## To-do
- [ ] **Test-Branch** (z. B. `test-quinlan`, Quinlan Labs oder andere Testfirma aus dem Kompass): Kontext, ein bis zwei Skills mit Evals, eine Routine anlegen; testen, Erkenntnisse zurück in die Vorlage. Hinweis: Sichtbarkeit gibt es nur je Repo, nicht je Branch – privat nur über ein privates Repo/Fork.
- [ ] Fragen 1–10 abarbeiten, Antworten in `docs/` festhalten.
- [ ] Standard-Routinen als Aufträge erwägen: Kontext-Ernte, Kontext-Pflege, OS-Check (hier bewusst nicht vorgegeben).
- [ ] Prüfprogramm `system/` (Links, Quelle, Prüfdatum, fällige Dateien); Hooks in `system/hooks/` auf echten Geräten testen.

## Redlines
Keine Kundennamen/Kennzahlen von Auftraggebern in Außentexte. Keine Herkunftsangaben zum Vergleichsmaterial in die Vorlage schreiben.
