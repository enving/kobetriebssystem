# Von der Vorlage zum ersten geprüften Entwurf

Beginne mit einer wiederkehrenden Aufgabe und erfundenen Eingaben. Für diesen Durchlauf brauchst
du einen Agenten, der lokale Markdown-Dateien lesen kann. Für die Paketprüfung zusätzlich Git,
Python 3, Node.js und eine POSIX-Shell. Ein Firmenrollout ist ein eigener Schritt.

## 1. Aufgabe und Verantwortung festlegen

Im eigenen Arbeitsbereich kurz notieren: Wer braucht welches Ergebnis, welche Rolle prüft es,
welche Quelle darf gelesen werden und wo landet der Entwurf? Keine echten Firmendaten in diese
öffentliche Vorlage übernehmen. Der [Beispieldurchlauf](../beispiel/durchlauf.md) verwendet nur
erfundene Besprechungsnotizen.

**Fertig:** Ein Satz beschreibt Aufgabe und Ergebnis; eine zuständige Rolle ist benannt.

## 2. Quelle auffindbar machen

Für die Beispielaufgabe reicht die angegebene lokale Notiz. Bei einer eigenen Aufgabe beschreibt
die [Landkarte](../kontext/landkarte.md) den Zugang zum erlaubten Quellsystem. Dauerwissen bekommt
eine Seite nach der [Kontextvorlage](../kontext/_vorlage-bereich/_vorlage.md) und einen relativen
Link im [Index](../kontext/index.md). Bestehende Quellen bleiben an ihrem erlaubten Ort.

**Fertig:** Eine neue Sitzung findet die Quelle und kann sagen, wer für ihren Inhalt zuständig ist.
Fehlender Zugriff bleibt ein benannter Blocker.

## 3. Passenden Skill wählen

Für die Übung verwende [besprechung-nachbereiten](../beispiel/skills/besprechung-nachbereiten/SKILL.md).
Für eine andere Aufgabe lässt du `skill-creator` die [Skill-Vorlage](../.agents/skills/_vorlage/SKILL.md)
ausfüllen. Für den Aufbau eines belegten Wikis verwende `wissen-pflegen`.
[Herkunft, Werkzeuge und Grenzen](skills.md).

**Fertig:** Eingaben, erwartetes Ergebnis, fehlende Angaben und Abbruchbedingungen sind beschrieben.

## 4. Mit einer erfundenen Eingabe ausführen und prüfen

Bitte den Agenten:

> Lies den Beispiel-Skill „besprechung-nachbereiten“. Erstelle aus
> `beispiel/skills/besprechung-nachbereiten/evals/normalfall.eingabe.md` einen Aufgabenentwurf.
> Nutze ausschließlich diese Notiz als Sachquelle und gib das Ergebnis hier aus.

Vergleiche mit dem [Sollentwurf](../beispiel/skills/besprechung-nachbereiten/evals/normalfall.soll.md).
Wiederhole mit der fehlenden Zuständigkeit und der eingebetteten Versandaufforderung aus
[den Prüffällen](../beispiel/skills/besprechung-nachbereiten/evals/faelle.json).

**Fertig:** Jede Angabe hat eine Fundstelle; fehlende Angaben bleiben offen. Ergebnis und beobachtete
Fehler stehen mit Modell und Datum im Prüfbericht. Ein ähnlicher Solltext allein reicht als Beleg nicht.

## 5. Korrektur bis zur erneuten Prüfung verfolgen

Der [Beispieldurchlauf](../beispiel/durchlauf.md) zeigt einen konkreten Änderungsvorschlag mit
Prüffall. Für echte Änderungen gilt die [Lernschleife](../README.md#die-lernschleife-wie-das-system-mit-jeder-korrektur-besser-wird).

**Fertig:** Vorschlag, Freigabestatus und Prüfung sind auffindbar. Ein freigegebener neuer Stand
wird in einer frischen Sitzung geprüft; ein nicht freigegebener Vorschlag bleibt ein Vorschlag.

## 6. Das Paket lokal prüfen

Im Quell-Repo:

```sh
sh installation/bauen.sh 0.1-einstieg --mit-beispielen
node system/tests/beispiel-build.mjs
node system/tests/plugin-start.mjs
```

Die beiden Prüfprogramme bauen weitere Testversionen; `dist/` ist danach deren letzte Ausgabe.
Der normale Bau ohne `--mit-beispielen` enthält die zwei allgemeinen Skills, aber keinen
Besprechungs-Skill. Der [Pakettest](../system/tests/beispiel-build.mjs) prüft auch diesen Rückwechsel.
Er überschreibt nur das erzeugte `dist/`, nicht die Quellen.

**Fertig:** Die Prüfungen enden ohne Fehler und die benötigten Skills samt Beilagen liegen im Paket.
Das belegt Paketinhalt und Startbefehle. Installation im echten Client, persönliche Zugriffsrechte,
Versionswechsel laufender Sitzungen und Unternehmensfreigabe müssen separat geprüft werden.
[Verteilung und bekannte Grenzen](../installation/README.md).

Eine Routine wird erst danach nach der [Routinevorlage](../automatisierungen/_vorlage.md)
vorbereitet und freigegeben. Dieser Einstieg schaltet keine Automatisierung ein.
