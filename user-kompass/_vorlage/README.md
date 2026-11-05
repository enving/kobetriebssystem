# User-Kompass

Der Kompass einer Person: ihre Anweisungen, Ziele, Grenzen, ihr Logbuch und ihre Beitragsliste. Er gehört der
Person und darf unordentlich sein. Menschen verfolgen mehrere Ziele gleichzeitig, und das ist kein Fehler, den ein
Agent beheben muss. Architektur und Begründung stehen in
[Architektur §12](../../docs/architektur/bericht-2026-11-05.md).

## Was hier liegt

| Datei | Inhalt | Verlässt den User-Kompass? |
|---|---|---|
| `anweisungen.md` | Rolle, Stil, Ziele, Grenzen; oben offene Fragen des Agenten an die Person | nein |
| `logbuch.md` | Was der Agent für die Person getan hat, mit Beleg | nein, höchstens als verallgemeinerte Zeile |
| `beitraege.md` | Kandidaten für Verbesserungen am Betriebssystem | nur verallgemeinert, per PR, nach Ja |
| `privat/` | Was kein Agent außerhalb der Person liest (per Hook gesperrt, [Beispiel](../../system/hooks/settings-beispiel.json)) | nie |

Die Vorlage ist bewusst klein. Wer mehr braucht (Knoten für Entscheidungen, Gespräche, Ideen, Quellen), legt
weitere Ordner an. Wichtig ist nur eine Trennung: **Beleg** (was war), **Einschätzung** (was ein Agent meint,
mit Modell und Datum) und **Entscheidung** (was die Person gesagt hat, als Zitat mit Datum). Ein Agent
entscheidet nichts für die Person und leitet keine Richtung aus Belegen ab.

## Der Beitragsweg: vom User-Kompass ins Betriebssystem

1. **Bemerken.** Der Agent sieht ein Muster, etwa eine Korrektur, die dreimal kam, ein Skill, der sich bewährt,
   oder eine Regel, die fehlt. Er trägt es in `beitraege.md` ein, mit Beleg, der bei der Person bleibt.
2. **Verallgemeinern.** Er formuliert ohne Personen-, Kunden- und Gesundheitsdaten, ohne Namen und ohne
   Einzelfall, sodass es für eine Rolle gilt und nicht für diese Person.
3. **Vorlegen.** Die Person sagt Ja, nein oder einmalig (Grundregel 6 in [AGENTS.md](../../AGENTS.md)).
4. **PR ans Betriebssystem** mit Prüffall. Pipeline und Mensch-Tor wie bei jeder Änderung am Kern.
5. **Zurück.** Die übernommene Fassung kommt über die normale Verteilung wieder bei allen an, auch bei der Person
   selbst. Die eigene Kopie in `beitraege.md` wird auf „übernommen“ gesetzt, nicht doppelt gepflegt.

## Was nicht hochgeht

Ziele, Grenzen, Gesundheit, Familie, Geld, Bewerbungen, Rohgespräche und alles unter `privat/`. Ein Bot in der
Agenten-Laufzeit liest den User-Kompass nicht im Ganzen, sondern bekommt nur, was die Person ihm ausdrücklich gibt.
