---
type: Reference
title: "Rollenprüfung: Wissensassistent (erfundenes Beispiel)"
description: "Interner Agent der erfundenen Musterfirma, beantwortet Fragen der Mitarbeitenden aus freigegebenen Handbüchern."
stand: 09.11.2026
aufsicht: Teamleitung Wissensmanagement
freigabe: Rechts- und Compliance-Stelle, 09.11.2026
timestamp: 2026-11-09T11:00:00+01:00
---

# Rollenprüfung: Wissensassistent (erfundenes Beispiel)

Ausgefüllt nach [`ki-inventar/_rollenpruefung-vorlage.md`](../../ki-inventar/_rollenpruefung-vorlage.md). Firma,
Rollen und Angaben sind erfunden.

## 1. Zweck

- **Was tut der Agent?** Beantwortet Fragen zu internen Abläufen aus dem freigegebenen Handbuch und nennt die Fundstelle.
- **Für wen?** Intern, alle Mitarbeitenden der Musterfirma.
- **Was tut er ausdrücklich nicht?** Keine Personalfragen zu einzelnen Beschäftigten, keine Bewertung von Personen,
  kein Versand nach außen.

## 2. Bauweise

| Teil | Angabe |
|---|---|
| Modell und Hersteller | Allzweckmodell eines europäischen Herstellers |
| Plattform, SDK oder Laufzeit | Agenten-SDK des Herstellers |
| Eigene Anweisungen, Werkzeuge, Konnektoren | Anweisung, ein Suchwerkzeug als eigene Funktion, Konnektor zum Handbuch-Archiv |
| Wer hat gebaut? | eigenes Team |
| Hosting | beim Hersteller |

## 3. Rolle nach KI-Verordnung

Unter wessen Namen läuft der Agent? Musterfirma.

| Frage | Ja/Nein | Folge |
|---|---|---|
| Eigenes System gebaut und unter eigenem Namen in Betrieb (auch Eigengebrauch)? | ja | Anbieter |
| Setzt das Unternehmen den Agenten selbst ein? | ja | zusätzlich Betreiber |
| Fertiges System eines Dritten verändert? | nein | – |
| Für einen Kunden gebaut? | nein | – |

**Ergebnis Rolle:** Anbieter und Betreiber.

## 4. Risikoklasse

| Frage | Ja/Nein |
|---|---|
| Verbotene Praxis nach Art. 5? | nein |
| Zweck aus Anhang III? | nein, Personalfragen sind ausgeschlossen |
| Sicherheitsbauteil nach Anhang I? | nein |
| Spricht mit Menschen oder erzeugt Inhalte für Dritte? | spricht mit Mitarbeitenden; keine Inhalte für Dritte |

**Ergebnis Risikoklasse:** gering. Der Hinweis nach Art. 50 Abs. 1 kann entfallen, wenn offensichtlich ist, dass eine
KI antwortet; die Musterfirma zeigt ihn trotzdem an, weil er nichts kostet.

## 5. Pflichten und wer sie trägt

| Pflicht | Gilt? | Liefert die Plattform | Liefert dieses Repo | Lücke |
|---|---|---|---|---|
| KI-Kompetenz (Art. 4) | ja | – | Grundregeln, Schulungsnachweis | [OFFEN: Schulungsnachweis] |
| Hinweis „Sie sprechen mit einer KI“ | freiwillig | Anzeige im Chatfenster | – | – |
| Kennzeichnung erzeugter Inhalte | nein, nur intern | – | – | – |
| Protokollierung | nicht Pflicht | Sitzungsprotokolle | Git-Verlauf für Anweisungen | Aufbewahrungsfrist klären |
| Menschliche Aufsicht | empfohlen | Freigabe vor Werkzeugaufrufen | Ampel in `AGENTS.md` | – |
| Modelldokumentation des Herstellers | ja | angefordert | abgelegt unter `kontext/` | – |
| Datenschutz | ja | AVV, Subprozessorliste | – | Subprozessoren prüfen |

## 6. Entscheidung

- **Freigegeben für:** Handbuchfragen der Mitarbeitenden.
- **Nicht freigegeben für:** Fragen zu einzelnen Beschäftigten, Bewerbungen, Leistungsbewertung (Anhang III).
- **Nächste Prüfung:** bei jedem neuen Konnektor, spätestens nach zwölf Monaten.
