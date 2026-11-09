---
type: Reference
title: "Rollenprüfung: <Name des Agenten>"
description: "<Ein Satz: was der Agent tut und für wen>"
stand: <TT.MM.JJJJ>
aufsicht: <Rolle der benannten Aufsichtsperson>
freigabe: <Rolle der freigebenden Stelle, Datum>
timestamp: <ISO-Datum>
---

# Rollenprüfung: <Name des Agenten>

Ausfüllen vor dem ersten Einsatz und bei jeder Zweckänderung. Jede Antwort mit Beleg (Datei, Link, Vertrag).
Unklares als `[OFFEN: …]` stehen lassen, nicht raten.

## 1. Zweck

- **Was tut der Agent?** <Aufgabe in einem Satz>
- **Für wen?** <intern: welche Teams | extern: welche Kunden oder Personen>
- **Was tut er ausdrücklich nicht?** <Grenzen>

## 2. Bauweise

| Teil | Angabe |
|---|---|
| Modell und Hersteller | <Modell, Version> |
| Plattform, SDK oder Laufzeit | <z. B. Agenten-SDK des Herstellers, eigene Laufzeit> |
| Eigene Anweisungen, Werkzeuge, Konnektoren | <Liste oder Verweis auf `SKILL.md`> |
| Wer hat gebaut? | <eigenes Team | Dienstleister im Auftrag> |
| Hosting | <eigene Server | Hersteller | Cloud> |

## 3. Rolle nach KI-Verordnung

Unter wessen Namen läuft der Agent? <eigenes Unternehmen | Kunde | Hersteller>

| Frage | Ja/Nein | Folge |
|---|---|---|
| Eigenes System gebaut oder bauen lassen und unter eigenem Namen in Betrieb (auch Eigengebrauch)? | | ja → **Anbieter** (Art. 3 Nr. 3, Nr. 11; nachgelagert nach Nr. 68) |
| Setzt das Unternehmen den Agenten selbst ein? | | ja → zusätzlich **Betreiber** (Art. 3 Nr. 4) |
| Fertiges System eines Dritten mit eigenem Namen versehen oder wesentlich verändert? | | ja und Hochrisiko → Anbieter nach Art. 25 |
| Für einen Kunden gebaut, der ihn unter seinem Namen nutzt? | | ja → Anbieter ist in der Regel der Kunde; Pflichtenteilung im Vertrag |

**Ergebnis Rolle:** <Anbieter | Betreiber | beides>

## 4. Risikoklasse

| Frage | Ja/Nein |
|---|---|
| Verbotene Praxis nach Art. 5? | |
| Zweck aus Anhang III (z. B. Personalauswahl, Kreditwürdigkeit, Risiko und Preis in Lebens- und Krankenversicherung)? | |
| Sicherheitsbauteil eines Produkts nach Anhang I? | |
| Spricht der Agent mit Menschen oder erzeugt er Inhalte für Dritte (Art. 50)? | |

**Ergebnis Risikoklasse:** <verboten | hoch | Transparenzpflicht | gering>

Ändert sich der Zweck später in Richtung Anhang III, wird der Agent nach Art. 25 Abs. 1 Buchst. c zum
Hochrisiko-System. Dann neu prüfen, bevor er weiterläuft.

## 5. Pflichten und wer sie trägt

| Pflicht | Gilt? | Liefert die Plattform | Liefert dieses Repo | Lücke |
|---|---|---|---|---|
| KI-Kompetenz (Art. 4) | ja, immer | | | |
| Hinweis „Sie sprechen mit einer KI“ (Art. 50 Abs. 1) | | | | |
| Kennzeichnung erzeugter Inhalte (Art. 50 Abs. 2) | | | | |
| Protokollierung (Art. 12) | nur Hochrisiko | | | |
| Menschliche Aufsicht (Art. 14) | nur Hochrisiko, intern empfohlen | | Ampel in `AGENTS.md` | |
| Modelldokumentation des Herstellers (Art. 53) angefordert und abgelegt | | | | |
| Datenschutz: AVV, Subprozessoren, Datenstandort | | | | |

## 6. Entscheidung

- **Freigegeben für:** <Zweck, Nutzerkreis>
- **Nicht freigegeben für:** <z. B. jeden Anhang-III-Zweck>
- **Nächste Prüfung:** <Datum oder Auslöser>
