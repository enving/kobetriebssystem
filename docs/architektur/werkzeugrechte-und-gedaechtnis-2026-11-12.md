# Werkzeugrechte und Gedächtnis des Firmenagenten (12.11.2026)

Betrifft alle Adapter. Einordnung Claude Fable 5.2, 12.11.2026, mit den Überlegungen des Betreibers; nichts davon ist entschieden. Der technische Beleg steht im Repo Open-Source-KI-Stack, `docs/erweiterter-stack-betrieb.md`, Abschnitt „Werkzeugrechte des Firmenagenten“.

## Die Frage

Der Firmenagent soll Werkzeuge nutzen (Ablage, ERP, CRM) und daraus lernen. Zwei Dinge dürfen dabei nicht passieren: Er gibt einer Person etwas heraus, das sie nicht sehen darf, und er schreibt Datensätze in das gemeinsame Wiki, das alle lesen.

Überlegungen des Betreibers:

- Sieht der Agent nur Aufbau und Abläufe, bleibt er vertretbar, berät aber schlechter. Mit Datensätzen berät er besser und schreibt ein besseres Wiki.
- Ob das System hinter dem Agenten pauschal alles sehen darf, ist eine Frage von Datenschutz-Folgenabschätzung, Filter für Personendaten und Schutzstufen an der Quelle. Das ist je Firma zu klären.
- Offen ist, ob die Harnesses (Codex, Claude Code, Pi) das über Jahre sicher halten können.
- Arbeitet der Agent nur mit dem Konto der Person im Chat, fehlt ihm für eigenständige Arbeit Kontext, und er lernt nicht alles.

## Vorschlag: vier Regeln, die nicht am Modell hängen

1. **Rechte hängen am Schlüssel.** Im Auftrag einer Person läuft der Agent mit ihren Verbindungen; das Fachsystem verweigert, was sie nicht sehen darf. Aus eigenem Antrieb läuft er mit einem eigenen Dienstkonto.
2. **Das Dienstkonto zählt als „alle Mitarbeitenden“.** Was ihm freigegeben wird, darf er jeder Person im Unternehmen sagen. Damit muss der Agent nie nachschlagen, welche Rechte die fragende Person hat. Alles darüber hinaus kommt nur über die Rechte der fragenden Person. Wer dem Dienstkonto mehr freigibt (Stufe 2, Datensätze), gibt es damit für alle frei oder muss für diesen Bereich ein zweites, enger genutztes Dienstkonto führen.
3. **Das Wiki speichert Zeiger und Verfahren, keine Daten.** Ein Eintrag sagt, wo etwas liegt und wie man es abfragt („Personalakten liegen im ERP, Modul Personal, Abfrage über …“). Den Inhalt holt der Agent bei jeder Frage frisch, mit den Rechten der fragenden Person. So lernt er aus Datensätzen, ohne sie zu behalten.
4. **Die Sperre sitzt an den Grenzen, nicht im Harness.** Schreibweg ins Wiki nur über Vorschlag und Ja des Bereichsbesitzers; davor eine maschinelle Prüfung auf Personendaten, die die Übernahme blockiert; ein regelmäßiger Suchlauf über das ganze Wiki; ein Protokoll, welcher Lauf mit welchem Konto welches Werkzeug aufrief. Hooks eines Harness sind eine zweite Linie, aber sie wechseln mit dem Harness. Zugangsdaten, Dateirechte und die Merge-Sperre bleiben.

## Was das nicht löst

- Ein manipuliertes Dokument kann einen Lauf fehlleiten. Der Schaden bleibt auf die Rechte des Laufs begrenzt.
- Abgeleitetes Wissen: Aus vielen Datensätzen lässt sich etwas schließen, das einzeln nicht geschützt war. Dafür braucht es die Entscheidung des Bereichsbesitzers, keine Technik.
- Eine Zusammenfassung im Wiki kann Personendaten enthalten, die kein Muster erkennt. Die Prüfung senkt das Risiko, der Besitzer bleibt verantwortlich.
- Wer die Rechte pflegt: das Fachsystem, möglichst über Gruppen. Ein Vermittler wie Composio hält nur die Verbindung und kann einschränken, nie erweitern.

## Offen für die Adapter

- Wie jeder Adapter die Kennung der Person serverseitig an den Agentenlauf gibt. Für Open WebUI mit Open Terminal ist das belegt (siehe Verweis oben).
- Wie die Werkzeugverbindung der Person in den Lauf kommt, ohne dass andere Läufe sie lesen können.
- Prüffall für jeden Adapter: Eine Person ohne Recht fragt nach einer Personalakte; der Agent mit Dienstkonto darf nichts liefern und nichts davon ins Wiki schreiben.
