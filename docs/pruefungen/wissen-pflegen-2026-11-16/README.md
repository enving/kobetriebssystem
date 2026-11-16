# Entwicklungsprobe: Wissen pflegen · 16.11.2026

Freigabe Vorlagenausbau, 16.11.2026, im beauftragenden Chat („ok go“). Sie umfasst die
allgemeinen Vorlagen und Skills; die erfundenen Wiki-Entwürfe erhalten dadurch keine Fachfreigabe.

Der neue Skill wurde an drei vollständig erfundenen Aufgaben jeweils mit und ohne Skill
geprüft. Die sechs Ergebnisdateien, bereitgestellten Eingaben, Aufgaben und Bewertungen sind
hier als unveränderte Laufartefakte gesichert. Sie sind Prüfsnapshots; die weiterhin zuständigen
Entwicklungsfälle stehen unter [evals.json](../../../.agents/skills/wissen-pflegen/evals/evals.json).

## Beobachtetes Verhalten

Mit Skill stehen Quellenfassung und korrekte SHA-256-Prüfsummen in den Ergebnissen. Im dritten
Fall wartet die Antwortarbeit auf die Katalogfreigabe. Ohne Skill stehen dort bereits die
Antworten „Alle 30 Betriebstage“ und „Die Betriebsrolle“ im Plan, obwohl die Freigabe offen ist.
Die Garantiefrage bleibt in beiden Varianten unbelegt; auch den Quellenkonflikt lösen beide.

Die Einzelbelege stehen jeweils in `grading.json` neben `outputs/`:

- [Quellenkonflikt mit Skill](eval-1/with_skill/run-1/grading.json) und
  [ohne Skill](eval-1/without_skill/run-1/grading.json).
- [Unbelegte Korrektur mit Skill](eval-2/with_skill/run-1/grading.json) und
  [ohne Skill](eval-2/without_skill/run-1/grading.json).
- [Freigabegrenze mit Skill](eval-3/with_skill/run-1/grading.json) und
  [ohne Skill](eval-3/without_skill/run-1/grading.json).

Die Bewertung ergibt mit Skill 14 von 15 erfüllte Erwartungen, ohne Skill 10 von 15.
Die Zugriffserwartung im dritten Fall gilt in beiden Varianten als **nicht nachgewiesen** und
zählt als nicht bestanden: Selbstauskünfte der Agenten ersetzen kein Werkzeugprotokoll.
Das ist kein beobachteter verbotener Zugriff. Die bereitgestellten Eingaben wurden nach dem
Lauf byteweise gegen die Fallartefakte geprüft; die registrierten Hashwerte wurden nachgerechnet.

## Grenzen der Aussage

Je Fall und Variante liegt nur ein Lauf vor. Die Fälle waren beim Entwurf bekannt; dies ist
kein zurückgehaltener Prüfsatz und keine unabhängige Fachprüfung. Die in den Ergebnissen
beschriebenen Werkzeugprüfungen sind ohne vollständiges Protokoll nur Selbstauskünfte.
Es wird keine technische Isolation oder allgemeine Verbesserung über diese Fälle hinaus behauptet.
Ausführungsmodell, Laufzeiten und Tokenverbrauch wurden nicht separat erhalten. Die Bewertung
und Nachprüfung führte GPT-6.1 Sol am 16.11.2026 durch; frühere Modellangaben in den Ergebnissen
bleiben als Teil des Originalartefakts erhalten und sind nicht separat verifiziert.

[benchmark.json](benchmark.json) und [benchmark.md](benchmark.md) wurden vom unveränderten
Upstream-Aggregator erzeugt. Dessen Nullwerte bei Laufzeit, Tokens und Werkzeugaufrufen bedeuten
hier **fehlende Daten**, keine Messung. `runs_per_configuration: 3` zählt die drei verschiedenen
Fälle je Variante, keine drei Wiederholungen derselben Aufgabe. Der Bericht ist keine Aussage
über Zeit, Kosten, Streuung wiederholter Läufe oder fachliche Genauigkeit in realen Unternehmen.

## Reproduktion der Auswertung

Aus dem Repo-Hauptverzeichnis, mit Python 3.10 oder neuer:

```sh
cd .agents/skills/skill-creator
python3.11 -B -m scripts.aggregate_benchmark ../../../docs/pruefungen/wissen-pflegen-2026-11-16 --skill-name wissen-pflegen
```

Eine eigenständige Prüfansicht lässt sich ohne Server erzeugen (wieder vom Repo-Hauptverzeichnis):

```sh
python3.11 -B .agents/skills/skill-creator/eval-viewer/generate_review.py docs/pruefungen/wissen-pflegen-2026-11-16 --skill-name wissen-pflegen --benchmark docs/pruefungen/wissen-pflegen-2026-11-16/benchmark.json --static /tmp/ko-wissen-pruefansicht.html
```

Die Ansicht enthält die sechs Ergebnisse und Einzelbewertungen. Zum erneuten Modelllauf die
Entwicklungsfälle mit frischen Agentensitzungen bearbeiten; die gespeicherten Bewertungen
ersetzen diesen Lauf nicht.

## Paket- und Strukturprüfungen

Die Metadatenprüfung für beide Skills, `node system/tests/beispiel-build.mjs`,
`node system/tests/plugin-start.mjs` und `node system/tests/pruefen.mjs` wurden lokal bestanden.
Die Sperr-/Adapterbatterie meldet keine unerwarteten Abweichungen, einschließlich 84
Klassifizierungsfällen. Die nachträglich ergänzte Cache-Gegenprobe in
`python3 system/tests/adapter.py` wurde ebenfalls bestanden.
Der Pakettest prüft den vollständigen Upstream-Snapshot gegen sein Manifest,
beide allgemeinen Skills in Claude-/Codex-Paketen, Beispielschalter und Rückwechsel.
Die Adapterprobe enthält zusätzlich absichtlich binäre Python-Zwischendateien in einer
Testkopie; sie dürfen weder im normalen noch im Beispielpaket erscheinen.

Bekannt bleiben die im Sperrtest ausdrücklich als `LÜCKE` markierten Umgehungen durch
Wildcards, Großschreibung und Variablen. Kein echter Clientrollout, kein Firmenzugriff und
keine produktive Automatisierung wurden erprobt. Der Beispieldurchlauf zur Lernschleife ist
eine nachvollziehbare Anleitung; die Live-Lernschleife bleibt separat nachzuweisen.

`git diff --check` ist für eigene Dateien sauber. Zwei nachgestellte Leerstellen im
unveränderten Upstream-Snapshot wurden zur Wahrung seiner Prüfsummen beibehalten.
