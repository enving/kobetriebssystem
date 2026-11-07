# Erfundene Beispiele

Der Skill unter `skills/besprechung-nachbereiten/` folgt der Skill-Vorlage des Repos. Seine drei Fälle enthalten ausschließlich erfundene Daten. Die `.soll.md`-Dateien zeigen erwartete Entwürfe; den tatsächlichen Prüfstatus nennt `evals/ergebnisse.md`.

Bau ohne Beispiele: `sh installation/bauen.sh 0.1-demo`

Bau mit Beispielen: `sh installation/bauen.sh 0.1-demo --mit-beispielen`

Jeder Bau ersetzt `dist/`. Nur der zweite Aufruf kopiert Beispiel-Skills nach `dist/ko-basis/skills/`. Keine Installation oder Verteilung ist Teil dieses Beispiels.
