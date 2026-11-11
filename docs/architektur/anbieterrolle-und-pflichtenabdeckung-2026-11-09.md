---
type: Reference
title: Anbieterrolle bei selbst gebauten Agenten und welche Pflichten Plattform und Betriebsschicht abdecken
description: Wer mit dem Agenten-SDK eines Modellherstellers einen Agenten für einen festen Zweck baut und unter eigenem Namen einsetzt, ist nach der KI-Verordnung Anbieter dieses KI-Systems. Daraus folgen eine Rollenprüfung je Agent, ISO/IEC 42001 als Rahmen für den laufenden Ablauf und Auswahlkriterien für Agentenplattformen.
timestamp: 2026-11-09T10:00:00+01:00
---

# Anbieterrolle bei selbst gebauten Agenten und welche Pflichten Plattform und Betriebsschicht abdecken

**Einschätzung Claude Opus 5.5, 09.11.2026. Keine Rechtsberatung, kein Konformitätsnachweis.** Ergänzt den
README-Abschnitt [„Warum es dieses Repo gibt“](../../README.md#warum-es-dieses-repo-gibt-betrieb-haftung-eu-ai-act)
und die Lücke [PRD](../../PRD.md) L18. Artikelangaben sind gegen den Verordnungstext zu prüfen, bevor sie in eine
Freigabe eingehen.

## Die Frage

Ein Unternehmen baut Agenten mit dem SDK eines Modellherstellers, zum Beispiel dem Mistral Agents SDK. Der Hersteller
liefert Modell, Laufzeit, Werkzeuge und auf Wunsch das Hosting. Bleibt das Unternehmen damit Betreiber, weil es „im
Framework des Herstellers“ bleibt, oder wird es Anbieter?

## Einordnung

**Drei Ebenen, drei Anbieter.**

| Ebene | Anbieter | Wird das Unternehmen durch Agentenbau Anbieter? |
|---|---|---|
| Allzweckmodell | Hersteller | Nein. Anweisungen, Werkzeuge und Konnektoren ändern das Modell nicht. |
| Agentenplattform und SDK | Hersteller | Nein, das ist Werkzeug. |
| Der Agent (Modell, Anweisungen, Werkzeuge, Konnektoren, Zweck) | wer ihn baut oder bauen lässt und unter eigenem Namen einsetzt | **Ja, in aller Regel.** |

**Das SDK verschiebt die Rolle nicht.** Art. 3 Nr. 3 fragt, wer ein KI-System entwickelt oder entwickeln lässt und es
unter eigenem Namen in Verkehr bringt oder in Betrieb nimmt. Inbetriebnahme umfasst den Eigengebrauch; verkauft werden
muss nichts. Mit wessen Bibliothek gebaut wird, spielt keine Rolle. Die Verordnung kennt für diesen Fall den
nachgelagerten Anbieter, der ein fremdes Allzweckmodell in sein System einbaut, und verpflichtet Modellanbieter, solche
Anbieter mit Informationen zu versorgen (Art. 53). Auch Hosting beim Hersteller ändert daran nichts.

**Art. 25 ist hier nicht der Prüfweg.** Art. 25 regelt, wann jemand ein *fremdes, fertiges* System so verändert, dass er
Anbieter wird, und betrifft Hochrisiko-Fälle. Wer mit dem SDK baut, verändert kein fremdes System, er baut ein eigenes.
Relevant bleibt Art. 25 Abs. 1 Buchst. c: Bekommt ein allgemeiner Agent einen Zweck aus Anhang III, wird er hochriskant.

**Die Rolle hängt am Namen.**
- Eigener Agent für das eigene Unternehmen: Anbieter und Betreiber zugleich.
- Dienstleister baut für ein Unternehmen, das den Agenten unter eigenem Namen nutzt: Anbieter ist in der Regel das
  Unternehmen („entwickeln lässt“). Im Vertrag regeln, wer welche Dokumentation liefert.
- Agent unter eigenem Namen an mehrere Kunden: Anbieter; die Kunden sind Betreiber.

**Die Last entscheidet die Risikoklasse.**
- Geringes Risiko (Recherche, Entwürfe, Wissensassistent): vor allem Art. 50 Abs. 1 (Hinweis, dass man mit einer KI
  spricht), Art. 50 Abs. 2 (Kennzeichnung erzeugter Inhalte, soweit technisch machbar), Art. 4 (KI-Kompetenz).
- Hochrisiko durch Zweck, etwa Bewerbungen vorsortieren oder Risiko und Preis in Lebens- und Krankenversicherung: die
  Anbieterpflichten aus der README-Tabelle (Art. 9–17, 72), dazu Konformitätsbewertung und Registrierung.

## Was daraus für den Betrieb folgt

Ein Unternehmen, das Agenten selbst baut, wird mit jedem Agenten erneut Anbieter. Jede neue Aufgabe oder Zweckänderung
kann einen Hochrisiko-Fall auslösen. Das ist eine dauernde Tätigkeit und braucht einen festen Ablauf.

**Rollenprüfung je Agent als fester Schritt.** Vor dem ersten Einsatz und bei jeder Zweckänderung: Zweck, Name, unter
dem der Agent läuft, Rolle (Anbieter, Betreiber, beides), Risikoklasse, Anhang-III-Prüfung. Ergebnis im Inventar.
Vorlage: [`ki-inventar/`](../../ki-inventar/README.md), mit erfundenem Beispiel (L18).

**ISO/IEC 42001 als Rahmen für den Ablauf.** Das KI-Managementsystem verlangt ein Inventar der KI-Systeme, Risiko- und
Folgenabschätzung, Zuständigkeiten, Lieferantensteuerung, Überwachung und Verbesserung. Das passt zu einem Unternehmen,
das laufend Anbieter wird. Die Norm ersetzt keine Konformitätsbewertung nach KI-VO; sie ist aber der naheliegende
Rahmen für ein Qualitätsmanagementsystem nach Art. 17, falls ein Agent hochriskant wird.

**Plattformen danach auswählen, welche Pflichten sie operativ abdecken.** Eine Agentenplattform führt Agenten aus. Für
die Auswahl zählt zusätzlich, welche Pflicht sie dem Unternehmen abnimmt und welche bei der Betriebsschicht bleibt:

| Pflicht | Was die Plattform liefern sollte | Was dieses Repo heute beiträgt |
|---|---|---|
| Protokollierung (Art. 12) | Laufprotokolle je Sitzung, exportierbar, mit Aufbewahrungsfrist | Git-Verlauf für Steuerndes; Laufprotokolle offen |
| Menschliche Aufsicht (Art. 14) | Freigabe vor Werkzeugaufrufen, Abbruch, Rollenrechte | Ampel in `AGENTS.md` |
| Transparenz (Art. 50) | KI-Hinweis im Dialog, Kennzeichnung erzeugter Inhalte | [OFFEN] |
| Dokumentation (Art. 11, 53) | Modelldokumentation des Herstellers, versionierte Agentendefinitionen | `SKILL.md`, versioniert |
| Robustheit und Sicherheit (Art. 15) | Leitplanken, Sandbox, Geheimnisverwaltung, Evals | Sperren in `system/`, Evals vor Automatisierung |
| Datenschutz (DSGVO Art. 28, 44 ff.) | AVV, Liste der Subprozessoren, Datenstandort | [OFFEN: Anbieterprüfung] |
| Beobachtung nach dem Einsatz (Art. 72) | Vorfallmeldung, Auswertung | Lernschleife, `docs/beobachtungen.md` |

Was die Plattform liefert, muss die Betriebsschicht nicht nachbauen; was sie nicht liefert, bleibt als Lücke sichtbar.
Hersteller-Agentenplattformen nennen Bausteine wie Freigaben, Leitplanken und Sitzungsprotokolle. Ob Protokolle
exportierbar sind, wie lange sie aufbewahrt werden und welche Subprozessoren beteiligt sind, ist je Plattform zu prüfen
und hier noch nicht geprüft.

## Offen

- Plattformvergleich anhand der Tabelle oben, sobald eine Laufzeit für Firmenagenten feststeht.
- Abgleich der README-Tabelle mit ISO/IEC 42001 (dort schon als OFFEN geführt).
