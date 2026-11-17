# Antwortort und Rechteentzug: Paketprobe S20

Eigene technische Prüfung, GPT-6.1-sol, 17.11.2026. Ausgangspunkt: `9753f44`
(main nach PR #48). Freigabe Rechteprobe, 17.11.: Auftrag zur Probe derselben
Wissensfrage persönlich/öffentlich und anschließendem Rechteentzug.
Keine neue Rechtearchitektur oder Company-Brain-Integration beschlossen.

## Ergebnis

**Die vollständige Rechteprobe ist nicht bestanden.** Der vorhandene Adapter
verteilt statische Pakete. Er bekommt weder einen Antwortort noch eine
Kanalmitgliedschaft als Eingabe. Daraus folgt keine technische Trennung zwischen
persönlichem und öffentlichem Antwortkanal.

Die ausgeführte Teilprobe zeigt:

- Gemeinsames Wissen erreicht beide lokalen Kopien des echten Codex-Pakets.
- Nach `chmod 000` scheitert das erneute Lesen der temporären Quelldatei tatsächlich
  mit `PermissionError`. Der früher verteilte Inhalt bleibt in beiden Kopien lesbar.
  Entzug an der Quelle zieht eine bereits ausgelieferte Datei also nicht zurück.
- Mit `klassifizierung: vertraulich` verweigert der echte Paketbau die neue Quelle
  (Exit 3). Der neue private Marker wird nicht verteilt. Ein nur für den berechtigten
  Kreis verwendbares Paket entsteht ebenfalls nicht. Das ist eine bestehende
  globale Schutzmaßnahme, keine fehlerhafte Freigabe für die Öffentlichkeit.
- Als Gegenprobe wird ausschließlich in der temporären Kopie das Etikett entfernt:
  Dann enthält das neu gebaute Paket den privaten Köder. Der Markerbeobachter
  erkennt den ungeschützten Fall tatsächlich.

Vier Schutz-/Kontrollkriterien und die Sensitivitätskontrolle bestehen; zwei
benötigte Teilfunktionen fehlen. Der Prozess liefert deshalb Exit 3 statt einer
grünen Abnahme. Die letzte Gegenprobe ist ausdrücklich keine produktive Einstellung.

## Wiederholen und Belege

```sh
python3 system/tests/antwortort.py --output docs/pruefungen/antwortort-2026-11-17.json
```

Der Aufruf erzeugt alle Pakete in einem temporären Ordner, stellt die lokalen
Dateirechte vor dem Aufräumen wieder her und verändert keine Installation,
Produktionsdaten, Verbindungen oder Repo-Quelldateien. Kein Modellaufruf und kein
zusätzlicher Dienst. Ohne wirksamen lokalen Rechteentzug bricht die Probe als
technischer Fehler ab; etwa ein überprivilegiertes Konto darf keinen Erfolg vortäuschen.

Die [JSON-Ausgabe](antwortort-2026-11-17.json) enthält Einzelbefunde und SHA-256 der
Fixture und aller beteiligten Bau-/Prüfdateien. Die konkreten [Testdaten](../../beispiel/szenarien/S20-antwortort-und-widerruf/fall.json)
sind vollständig erfunden. Das [Szenario S20](../pruefszenarien.md#s20-antwortort-und-rechteentzug)
bleibt die zuständige Quelle für die spätere vollständige Abnahme.

Zusätzlich bestanden: `node system/tests/pruefen.mjs` (einschließlich 84
Klassifizierungsfällen, Paket-/Rücknahmeprüfung und zehn Symlink-Gegenfällen),
`node system/tests/plugin-start.mjs` und `node system/tests/beispiel-build.mjs`.
Die bereits dokumentierten Hook-Umwege bleiben offen. Python-Syntax, JSON,
Quellhashes, lokale Verweise und Whitespace geprüft; keine unerwartete Abweichung.

## Aussagegrenze und nächster Schritt

Das sind Datei- und Bauzugriffe, **keine Chatantworten**. Die zwei Ablagen sind
Bezeichnungen für mögliche Antwortorte, keine authentifizierten Personen oder
Kanäle. Weder Slack-Mitgliedschaft noch deren Widerruf, ein Fachsystemzugang,
laufender Modellkontext oder ein Quellenbeleg in einer Modellantwort wurden getestet.
Eine allein im Modelltext behauptete Person oder Kanalzuordnung wäre dafür kein Nachweis.

Für die vollständige Probe muss eine vorhandene Clientanbindung den tatsächlichen
Aufrufer und den Antwortort an einen berechtigten Wissenszugriff übergeben. Danach
denselben Fall mit frischem und laufendem Kontext nach realem Mitgliedschaftsentzug
ausführen. Ein statisches Paket bleibt für allgemein freigegebenes Wissen geeignet;
vertrauliche, widerrufbare Quellen benötigen einen tatsächlich geprüften Zugriffsweg.
Welcher Weg gilt, bleibt eine Architekturentscheidung nach PRD und SICHERHEIT.md.

Anregung: Company Brains [Lesefilter](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/brain/memory/read-scope.ts)
und [Mitgliedschaftsabgleich](https://github.com/supermemoryai/company-brain/blob/ef8a45ef3aed97b32599c7d8007edefab6d14e9a/src/brain/slack/channel-membership.ts).
Kein Code daraus übernommen; die eigenen Szenarien und bestehenden Sperren werden weitergenutzt.
