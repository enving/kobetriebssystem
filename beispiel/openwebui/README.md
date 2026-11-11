# OpenWebUI-Prüfset

Dieses Prüfset enthält ausschließlich synthetische Daten. Es ist für einen manuellen Lauf in einer OpenWebUI-Testinstanz vorbereitet. Es wurden damit noch keine Modellantworten erzeugt oder bewertet; Provider-Zugangsdaten und echte Personen- oder Unternehmensdaten gehören nicht in dieses Verzeichnis.

## Dateien

- `system-prompt.md`: begrenzter Prüfauftrag für die Testinstanz.
- `fixtures/01-meeting-notes.md`: mehrdeutige Besprechungsnotizen.
- `fixtures/02-approved-shared-rule.md`: freigegebene synthetische Regel.
- `fixtures/03-review-proposal.md`: absichtlich widersprüchlicher Änderungsvorschlag.
- `fixtures/04-test-cases.md`: Prüffälle A–K und ihre Bestehenskriterien.

## Durchführung

Die Testfälle setzen einen OpenWebUI-Testaufbau mit synthetischen Dateien voraus. Für Modellprüfungen muss ein Provider in der Testinstanz eingerichtet sein. Datei- und Terminalprüfungen benötigen zusätzlich eine Sandbox mit schreibgeschützten Fixtures und einem getrennten Ausgabeverzeichnis; die Fallbeschreibung allein stellt diese Isolation nicht her.

Die Reihenfolge und das Ergebnis jedes Laufs in einer lokalen Testnotiz festhalten: Modell und Konfiguration, Fall-ID, verwendete Dateien, Antwort, Soll/Ist, Befund. Keine Schlüssel, persönlichen Daten oder privaten Marker in dieses Repo schreiben. Produkt- und Sicherheitsannahmen stehen gesammelt in [Szenarien §5](../../docs/szenarien.md#5-wo-die-zuletzt-genannten-werkzeuge-einzuordnen-sind), nicht in diesem Prüfset.
