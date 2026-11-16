---
name: <skill-name>
description: "<Was macht der Skill + wann wählen? Trigger-Sätze der Nutzer. Abgrenzung: Ein Objekt, ein Skill – Nachbar-Skill X für Y. Nie: <harte Grenze>.>"
metadata:
  besitzer: "<verantwortliche Rolle>"
  nutzt_kontext:
    - <bereich>/<datei>.md
---

# <Titel>

**Auslöser:** <woran der Agent erkennt, dass die Aufgabe ansteht>
**Ergebnis:** <was am Ende vorliegt, wo>

## Eingaben und Quellen

- Benötigt: <welche Angaben und Quellen müssen vorliegen?>
- Bei fehlenden Angaben: <welche Teile bleiben möglich, welche einzelne Rückfrage blockiert den Rest?>
- Zuständige Quellen: <Verweise auf Kontext oder Originale; keine kopierten Regeln oder Wertelisten>

## Vorgehen

<Nur fachlich nötige Abhängigkeiten: Was muss vor welchem Schritt feststehen?
Keine Klickfolge festschreiben, die das Werkzeug besser selbst bestimmen kann.>

## Fertig heißt …
Kriterien, die eine prüfende Person, ein Skript oder ein zweiter Agent mit Belegen prüfen kann.
- [ ] <beobachtbares Ergebnis, Fundstelle oder Datei; was würde durchfallen?>
- [ ] <Umgang mit fehlenden oder widersprüchlichen Angaben>

## Grenzen und Abbruch

<Welche fachliche Unsicherheit verhindert das Ergebnis? Wo endet der Auftrag?
Rechte und Freigaben aus den Projektregeln referenzieren, hier nur aufgabenspezifische Grenzen ergänzen.>

## Prüffälle

[evals/evals.json](evals/evals.json): Normalfall, fehlende Information und Grenzfall mit prüfbarer Erwartung.
[evals/ergebnisse.md](evals/ergebnisse.md): tatsächliche Läufe und Grenzen; Solltexte sind kein Testergebnis.

## Stolperfallen
(aus echten Fehlern)

## Beispiele

<Eine kurze Eingabe und das zugehörige Musterergebnis. Größere Dateien unter assets/,
Hintergrundwissen unter references/, wiederholbare Prüfungen unter scripts/; nur bei Bedarf anlegen.>
