Alle Angaben sind erfunden.

# Korrektur zum Entwurf von A

Gibt der Mensch, nachdem A den Entwurf zu `notiz-a.eingabe.md` gesehen hat:

> „Bei uns stehen Termine immer zusätzlich mit Kalenderwoche, also ‚13.11.2026 (KW 46)‘. Das gilt für alle, nicht nur
> für mich.“

Erwartete Einordnung nach AGENTS.md Regel 6: Regel, nicht einmalig. Erwarteter Vorschlag: eine Zeile in „Fertig heißt …“
des Skills `besprechung-nachbereiten` (Kalenderwoche nach ISO 8601 in Klammern hinter dem Datum, nur bei eindeutigem
Datum) und ein neuer Prüffall dazu.

Warum diese Korrektur: Version 1 verlangt schon, unsichere Termine erkennbar zu lassen. Eine Korrektur, die der Skill schon
enthält, zeigt keine Übertragung. Die Kalenderwoche schreibt ein Modell nicht von sich aus; ob das stimmt, prüft der Fall
`b-version-1-gegenprobe`.
