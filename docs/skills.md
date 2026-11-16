# Skills erstellen und Wissen pflegen

Das Standardpaket enthält zwei allgemeine Arbeitsfähigkeiten:

- [skill-creator](../.agents/skills/skill-creator/SKILL.md): einen wiederkehrenden Ablauf
  als Skill beschreiben, mit Aufgaben ausprobieren, gegen einen Lauf ohne Skill vergleichen
  und nach Rückmeldung verbessern. Beispiel: „Mach aus dieser Arbeitsanweisung einen Skill.“
- [wissen-pflegen](../.agents/skills/wissen-pflegen/SKILL.md): einen Wissensbestand aus
  erlaubten Quellen aufbauen oder aktualisieren. Beispiel: „Baue daraus Antworten auf die
  Fragen unserer Werkstattplanung, mit Fundstellen und sichtbaren Lücken.“

`skill-creator` ist ein unveränderter Snapshot aus `anthropics/skills`, einschließlich
Skripten, Prüfansicht und Apache-2.0-Lizenz. Revision und Prüfsummen stehen ausschließlich in
[UPSTREAM.json](../.agents/skills/skill-creator/UPSTREAM.json); die Originalmethode wird hier
nicht nochmals beschrieben. Ein Update ersetzt den Snapshot nach einem geprüften Diff,
aktualisiert das Manifest und läuft durch die Paketprüfung. Kein automatischer Download beim Bau.

Die übrigen Dateien dieses Repos behalten ihre jeweilige Lizenz; der Snapshot steht unter
[seiner eigenen Lizenz](../.agents/skills/skill-creator/LICENSE.txt).

## Anwendung in dieser Vorlage

Eigene Skills beginnen mit [.agents/skills/_vorlage/](../.agents/skills/_vorlage/SKILL.md).
Sie liegt nur im Quell-Repo und wird nicht als ausführbarer Skill verteilt. Das Format der
neuen Prüffälle folgt den [Schemas des Skill Creator](../.agents/skills/skill-creator/references/schemas.md).
Das bestehende Besprechungsbeispiel behält sein bereits genutztes `faelle.json`-Format.

Allgemeine Rechte und die Lernschleife stehen in [AGENTS.md](../AGENTS.md).
Ein mitgelieferter Skill erlaubt weder Veröffentlichungen noch Änderungen an diesen Rechten.
Lokale Anpassungen am Unternehmensprozess gehören in den betreffenden eigenen Skill oder
die zuständige Kontextquelle, nicht in eine bearbeitete Kopie der Upstream-Methode.

Die Skripte des Skill Creator brauchen Python 3.10 oder neuer; die Metadatenprüfung braucht
zusätzlich PyYAML. Mit Python 3.9 scheitert die Prüfansicht bereits beim Laden ihrer Typangaben.
Verwendet bei mehreren Installationen ausdrücklich den passenden Interpreter, zum Beispiel
`python3.11`. Modellaufrufe zur Beschreibungssuche setzen die Claude-CLI voraus. Diese Teile werden
durch das Paket weder installiert noch automatisch ausgeführt. In anderen Agentenumgebungen
können die vorhandenen Unteragenten für die inhaltlichen Proben verwendet werden; die
CLI-spezifische Beschreibungssuche bleibt dann ungeprüft. Probeläufe verändern nur ihre
eigenen Ergebnisordner und erhalten ausschließlich die dafür freigegebenen Testdaten.

`wissen-pflegen` verallgemeinert die Methode eines freigegebenen Wiki-Auftrags:
Fragen vor Seiten, präzise Fundstellen, sichtbarer Quellenabgleich, getrennte Prüfung
und anschließende Pflege. Fachliche Rechtslisten, konkrete Prüfgewichte, private Quellen
und projektgebundene Freigaben wurden nicht übernommen. Das ist eine öffentliche Methode,
kein veröffentlichtes Fachwiki.

Der [Prüfbericht](pruefungen/wissen-pflegen-2026-11-16/README.md) enthält die tatsächlichen
Entwicklungsproben mit und ohne Skill sowie die Grenzen des Nachweises.
