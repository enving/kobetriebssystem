# Ein Entwurf, eine Korrektur, eine neue Prüfung

Dies ist ein ausgearbeitetes Lehrbeispiel mit erfundenen Angaben. Die Ausschnitte sind
erwartete Ergebnisse, keine Protokolle eines vollständigen Live-Rollouts. Die tatsächlichen
früheren Modellläufe stehen beim [Besprechungs-Skill](skills/besprechung-nachbereiten/evals/ergebnisse.md).
Für den Einstieg folge [docs/einstieg.md](../docs/einstieg.md).

## Eingabe → Entwurf → Prüfung

Auftrag: Aus der [Normalfall-Notiz](skills/besprechung-nachbereiten/evals/normalfall.eingabe.md)
die Aufgaben vorbereiten. Die erfundene Teamrolle prüft den Entwurf. Die Notiz ist die einzige
Sachquelle, das Ergebnis erscheint in der Antwort.

Erwarteter Entwurf nach dem [Skill](skills/besprechung-nachbereiten/SKILL.md):

| Aufgabe | Zuständigkeit | Termin | Quelle |
|---|---|---|---|
| Entwurf der Checkliste | Lumo | 12.11.2026 | normalfall.eingabe.md, N1 |

Prüfung: Aufgabe, Zuständigkeit und Termin stehen in N1. Es wurde keine zusätzliche Tätigkeit
erfunden. Der Text bleibt ein Entwurf. Bei fehlender Zuständigkeit hilft der entsprechende
[Gegenfall](skills/besprechung-nachbereiten/evals/zustaendigkeit-fehlt.eingabe.md):
Das erwartete Ergebnis enthält `[OFFEN: Zuständigkeit]`, keine Vermutung.

## Menschliche Korrektur → konkreter Vorschlag

Für die Lernschleife verwenden wir die bereits vorhandene [Korrektur aus Szenario S4](szenarien/S4-lernschleife/korrektur.md).
Sie verlangt Kalenderwochen zusätzlich zu eindeutigen Terminen. Der Vorschlag nennt:

- **Ort:** Abschnitt „Fertig heißt …“ im Besprechungs-Skill der eigenen Firmeninstanz.
- **Wortlaut:** „Bei eindeutigem Datum die Kalenderwoche nach ISO 8601 in Klammern ergänzen;
  bei offenem Datum bleibt auch die Kalenderwoche offen.“
- **Prüffall:** Die andere [Notiz für B](szenarien/S4-lernschleife/notiz-b.eingabe.md) und die
  Erwartungen für `b-version-2` in [S4/faelle.json](szenarien/S4-lernschleife/faelle.json).
- **Freigabestatus:** Vorschlag im Lehrbeispiel; keine tatsächliche Firmenfreigabe.

Antwort der verantwortlichen Rolle im hypothetischen Durchlauf: „Ja zur Regel.“ Erst diese
Freigabe führt zum Änderungsvorschlag im Firmen-Repo. Der PR enthält die verallgemeinerte
Regel und den Prüffall. Persönliche Hinweise aus der Testperson-A-Ebene werden nicht übernommen.
Die zuständige Freigaberegel steht ausschließlich in [AGENTS.md](../AGENTS.md).

## Neue Fassung → Gegenprobe → Rücknahme

Vor der Änderung wird die B-Notiz mit der alten Fassung ausgeführt. Erscheinen dort bereits
Kalenderwochen, ist dieser Fall für den Nachweis der Übertragung ungeeignet. Nach der Änderung
muss die neue Sitzung die Erwartungen aus S4 erfüllen. Beispielsweise lautet der erste Termin
im erwarteten Ergebnis `03.12.2026 (KW 49)` mit Quelle `notiz-b.eingabe.md, N1`.

Die erneute Prüfung umfasst auch die bisherigen Normal-, Lücken- und Versandfälle.
Eine Rücknahme wird als neue Paketversion mit dem vorherigen Inhalt getestet; Versionsnummer
und Inhalt werden gemeinsam geprüft. Eine lokale Transportprobe dafür ist vorhanden:

```sh
python3 system/tests/adapter.py
```

Diese Probe verwendet einen synthetischen Änderungsmarker in einer temporären Kopie. Sie
belegt identische Skilldateien nach Bau, Änderung und Rücknahme sowie das Fernhalten eines
Privatmarkers. Sie beweist keine semantische Kalenderwochen-Regel und keinen echten Clientwechsel.
Der vollständige Nachweis mit frischen Agentensitzungen folgt weiterhin
[Szenario S4](../docs/pruefszenarien.md#s4-lernschleife-über-harness-grenzen).

**Was nach diesem Beispiel vorliegt:** ein nachvollziehbarer Entwurf, eine begründete
Korrektur, ein konkreter Änderungsvorschlag und ein Prüfweg mit Gegenprobe. Ob eine konkrete
Installation die Lernschleife vollständig erfüllt, bleibt an ihre gemessenen Läufe gebunden.
