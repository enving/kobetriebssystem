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
python3.11 -B -m scripts.aggregate_benchmark ../../../docs/pruefungen/wissen-pflegen-2026-11-16 --skill-name wissen-pflegen --skill-path .agents/skills/wissen-pflegen
```

Das reproduziert Einzelwerte und Zusammenfassung. Erzeugungszeitpunkt, ergänzte Modellhinweise
und die Hinweise unter `notes` sind Metadaten des gesicherten Berichts und werden dabei
nicht identisch neu erzeugt. Für einen Vergleich den Befehl in einer Testkopie ausführen.

Eine eigenständige Prüfansicht lässt sich ohne Server erzeugen (wieder vom Repo-Hauptverzeichnis):

```sh
python3.11 -B .agents/skills/skill-creator/eval-viewer/generate_review.py docs/pruefungen/wissen-pflegen-2026-11-16 --skill-name wissen-pflegen --benchmark docs/pruefungen/wissen-pflegen-2026-11-16/benchmark.json --static /tmp/ko-wissen-pruefansicht.html
```

Die Ansicht enthält die sechs Ergebnisse und Einzelbewertungen. Zum erneuten Modelllauf die
Entwicklungsfälle mit frischen Agentensitzungen bearbeiten; die gespeicherten Bewertungen
ersetzen diesen Lauf nicht.

Die zuständigen Metadaten liegen jeweils unter `eval-N/eval_metadata.json`. Die am 17.11.
ergänzten gleichnamigen Dateien in `run-1/` sind daraus bytegleich abgeleitete Prüfsnapshots:
Der unveränderte Upstream-Viewer sucht nur im Laufordner und dessen direktem Elternordner.
Ohne diese Snapshots fehlen ihm die Aufgabe und Fallkennung. Sie sind keine zweite
Pflegequelle; bei einer neuen Probe werden sie aus den jeweiligen Fallmetadaten erzeugt.

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

## Unabhängiger technischer Review · 17.11.2026

Prüfer: GPT-6.1 Sol in einer neuen Sitzung. Geprüft wurde der Vorlagenausbau von
[PR #48](https://github.com/enving/kobetriebssystem/pull/48) bei `79de3de` gegen Auftrag,
Repo-Anweisungen, PRD, vorhandene Übergabe, Diff, Bau-/Adaptercode und alle sechs
Entwicklungsartefakte. Lastannahme: lokaler Paketbau durch die OS-Betreuung.
Der Review ist eine Gegenprüfung vorhandener Belege, keine unabhängige Fachabnahme
und kein neuer Modellvergleich mit zurückgehaltenen Aufgaben. Keine Company-Brain-Integration.

### Befunde und Behebung

1. **Hoch: Externer Inhalt konnte durch Skill-Symlinks ins Paket gelangen.** Die neue
   `shutil.copytree`-Verwendung folgte symbolischen Links. In einer temporären Testkopie
   endete der Bau bei `79de3de` mit Exit 0 und enthielt eine externe, ausschließlich
   synthetische Datei als normale Datei in Claude- und Codex-Paketen. Damit konnte die
   bestehende Symlink-Prüfung sie nicht mehr erkennen. Die Kopie erhält nun Symlinks;
   die bestehende Klassifizierungsprüfung läuft zusätzlich vor der Adaptererzeugung.
   Verknüpfte Skill-Wurzelordner werden unmittelbar abgewiesen. Ohne diese Änderung
   könnten unbeabsichtigt externe Inhalte verteilt werden.
2. **Mittel: Der Bericht war aus dem ausgelieferten Wissens-Skill nicht erreichbar.**
   `evals/ergebnisse.md` verwies relativ auf einen nicht ausgelieferten `docs/`-Ordner.
   Der Link zeigt jetzt auf den veröffentlichten, unveränderlichen Stand dieser
   Entwicklungsprobe im Quell-Repo. Die Berichtsdateien werden dadurch nicht mitverteilt.
3. **Mittel: Die Dokumentation begrenzte die Wirkung der CLI-Proben zu stark.**
   `run_eval.py` legt eine vorübergehende Befehlsdatei unter `.claude/commands/` an,
   gegebenenfalls im übergeordneten Projekt. Der gestartete Client wird dadurch nicht
   auf die Testdaten beschränkt. `docs/skills.md` beschreibt jetzt diesen tatsächlichen
   Ablauf und verweist auf die weiterhin offene Trennung frischer Läufe in PRD L11.
   Der unveränderte Upstream-Code wurde nicht als isolierte Laufzeit ausgegeben.
4. **Mittel: Der Viewer fand Aufgaben und Fallkennungen nicht.** Er suchte nicht am
   vorhandenen Ort `eval-N/eval_metadata.json`; alle sechs Läufe erschienen mit
   `(No prompt found)` und ohne Fallkennung. Abgeleitete Metadatensnapshots im Laufordner
   beheben die Darstellung. Die ursprünglichen Aufgaben, Ergebnisse und Bewertungen
   bleiben unverändert; der Upstream-Snapshot bleibt identisch.

### Tatsächliche Gegenprüfung

- `python3 -B system/tests/adapter.py`: bestanden; zehn neue Symlink-Gegenfälle
  (Datei, Verzeichnis, defekter Link, Skill-Wurzel; allgemeine und Beispiel-Skills).
  Jeder verweigerte Bau erhält sämtliche vorherigen Paketdateien bytegleich.
  Derselbe neue Test schlägt mit dem ursprünglichen `bauen.sh` aus `79de3de` am ersten
  Symlink-Fall fehl. Die Python-Cache-Gegenprobe bleibt bestanden.
- `node system/tests/beispiel-build.mjs` und `node system/tests/plugin-start.mjs`:
  bestanden. `node system/tests/pruefen.mjs`: keine unerwarteten Abweichungen,
  84 Klassifizierungsfälle bestanden; zwölf als `LÜCKE` ausgegebene Adapterfälle
  bleiben bekannte Umgehungen, keine bestandenen Sperrprüfungen.
- Beide Skills mit `python3.11 -B .../scripts/quick_validate.py` geprüft: gültig.
  `sh -n installation/bauen.sh` und `git diff --check` der Reviewänderungen: sauber.
- Alle Einzelbewertungen gegen die Ergebnistexte und die erfundenen Originalquellen
  abgeglichen. Aufgabentexte, Erwartungslisten, Eingabesnapshots, registrierte SHA-256
  und Summen stimmen. Die bisherigen 14/15 und 10/15 bleiben unverändert.
- Den Upstream unabhängig von GitHub am im Manifest fixierten Commit abgerufen:
  alle 18 Dateien und SHA-256 stimmen mit `UPSTREAM.json` überein.
- Aggregator in einer temporären Kopie erneut ausgeführt: Einzelwerte und Zusammenfassung
  identisch; ergänzte Berichtsmetadaten wie oben getrennt behandelt. Die statische
  Prüfansicht enthält nun alle sechs richtigen Aufgaben und Fallkennungen. Alle sechs
  Metadatensnapshots stimmen byteweise mit ihrer Fallquelle überein. Lokale Links im
  ausgelieferten Wissens-Skill erreichen in Claude- und Codex-Paketen vorhandene Ziele;
  der externe Berichtslink wurde am fixierten GitHub-Stand nachgeschlagen.

### Grenzen und Rückgabe

Die Bewertung des dritten Falls bleibt in beiden Varianten beim Dateizugriff
**nicht nachgewiesen**. Weder der heutige Artefaktabgleich noch die neue lokale Bauprüfung
rekonstruieren historische Werkzeugaufrufe. Die drei Fälle waren bekannt, je Variante
liegt nur ein Lauf vor. Ausführungsmodell und persönlicher Kontexteinfluss sind nicht
unabhängig rekonstruierbar; Zeit, Tokens und Kosten bleiben ungemessen. Nullwerte und
die Streuung über verschiedene Aufgaben belegen weder Effizienz noch Wiederholbarkeit.
Die beschriebenen Prozessprüfungen der ursprünglichen Agenten bleiben Selbstauskünfte.

Kein echter Clientrollout, keine Fachsystemrechte, kein Widerrufstest, keine produktive
Routine und keine vollständige Live-Lernschleife geprüft. Die Baukorrektur schließt den
reproduzierten Kopierfehler; sie ist keine technische Rechtegarantie. Die offene
Clientprüfung zu [#26](https://github.com/enving/kobetriebssystem/issues/26), der Rückweg
aus [#28](https://github.com/enving/kobetriebssystem/issues/28) und die automatische
Skillprüfung aus [#1](https://github.com/enving/kobetriebssystem/issues/1) werden durch
diesen Review nicht abgeschlossen. Keine Architektur- oder Zuständigkeitsänderung,
daher keine neue Darstellung erforderlich.

**Urteil (GPT-6.1 Sol, 17.11.2026):** Die vier Befunde sind behoben; nach den belegten
Prüfungen bereit für die Parent-Abnahme. Keine Merge- oder Fachfreigabe erteilt.

**Lerneintrag:** Ein Cache-Ausschluss mit geänderter Kopierfunktion ließ die bestehende
Symlink-Grenze ungetestet. Die Gegenprobe muss auch externe und defekte Verknüpfungen
sowie unveränderte Altpakete bei Abbruch erfassen. Zusätzlich Paketlinks am Zielort und
den Viewer mit seinen tatsächlichen Metadatenpfaden prüfen; Quellbaum-Vollständigkeit
allein deckt diese Fehler nicht auf. CLI-Nebenwirkungen aus dem Code abgleichen, bevor
die Dokumentation einen engen Wirkungsumfang behauptet.
