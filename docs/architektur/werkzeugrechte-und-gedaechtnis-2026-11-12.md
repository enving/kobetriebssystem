# Werkzeugrechte und Gedächtnis des Firmenagenten (12.11.2026)

Betrifft alle Adapter. Einordnung Claude Fable 5.2, 12.11.2026, mit den Überlegungen des Betreibers; nichts davon ist entschieden. Der technische Beleg steht im Repo Open-Source-KI-Stack, `docs/erweiterter-stack-betrieb.md`, Abschnitt „Werkzeugrechte des Firmenagenten“.

## Die Frage

Der Firmenagent soll Werkzeuge nutzen (Ablage, ERP, CRM) und daraus lernen. Zwei Dinge dürfen dabei nicht passieren: Er gibt einer Person etwas heraus, das sie nicht sehen darf, und er schreibt Datensätze in das gemeinsame Wiki, das alle lesen.

Überlegungen des Betreibers:

- Sieht der Agent nur Aufbau und Abläufe, bleibt er vertretbar, berät aber schlechter. Mit Datensätzen berät er besser und schreibt ein besseres Wiki.
- Ob das System hinter dem Agenten pauschal alles sehen darf, ist eine Frage von Datenschutz-Folgenabschätzung, Filter für Personendaten und Schutzstufen an der Quelle. Das ist je Firma zu klären.
- Offen ist, ob die Harnesses (Codex, Claude Code, Pi) das über Jahre sicher halten können.
- Arbeitet der Agent nur mit dem Konto der Person im Chat, fehlt ihm für eigenständige Arbeit Kontext, und er lernt nicht alles.

## Vorschlag (Fassung 13.11.2026): Abteil, Schleuse, Wasserstand

Die erste Fassung vom 12.11. sah ein Dienstkonto vor, das als „alle Mitarbeitenden“ zählt. Einwand des Betreibers: Damit hätte der Agent nur die Rechte der Person mit den wenigsten Rechten; das reicht für einen Firmenagenten nicht. Zweiter Einwand: Eine Textregel oder ein Hook reicht nicht, wenn der Agent Daten sehen darf; schon die Möglichkeit, dass ein Datensatz im Wiki landet, lässt sich in einer Firma kaum abnehmen. Die Fassung unten nimmt beides auf. Sie ist ein Entwurf, gebaut ist davon nur der erste Baustein.

1. **Abteil je Person.** Jeder Lauf im Auftrag einer Person läuft unter einem eigenen Betriebssystemkonto dieser Person. Zwischendateien und Ergebnisse (etwa eine Präsentation aus Personaldaten für die Geschäftsführung) bleiben in ihrem Abteil und haben eine Aufbewahrungsfrist. Im gemeinsamen Bereich des Agenten liegt davon nichts.
2. **Werkzeugschleuse.** Der Agent hält keinen Schlüssel. Er ruft Werkzeuge über einen Dienst außerhalb seines Prozesses auf. Die Schleuse erkennt den Aufrufer am Betriebssystemkonto, also über den Kernel und nicht über Text des Modells, und führt den Aufruf mit der Verbindung genau dieser Person aus. Fragt die Geschäftsführung nach einer Personalakte, bekommt der Lauf sie; fragt jemand ohne Recht, verweigert das Fachsystem. Der Umweg „das Chat-Modell holt die Daten und reicht sie zurück“ entfällt.
3. **Dienstkonto mit breiten Rechten, ohne Hochsensibles.** Für eigenständige Arbeit hat der Agent ein eigenes Konto. Es darf viel lesen, damit er die Firma versteht. Personalakten und Vergleichbares bekommt es nie; die sieht ein Lauf nur im Auftrag einer berechtigten Person.
4. **Wasserstand.** Die Schleuse merkt sich je Lauf, aus welchen Quellen gelesen wurde. Alles, was den Lauf verlässt (Nachricht an eine Person, Datei in ein Abteil, Vorschlag fürs Wiki), geht durch ein Tor. Das Tor fragt beim Fachsystem mit der Verbindung des Empfängers, ob er jede dieser Quellen selbst lesen darf. Wenn nicht, bleibt der Ausgang zu. Das Wiki zählt als Empfänger „alle“: Ein Lauf, der etwas gelesen hat, das nicht alle lesen dürfen, kann nichts ins Wiki schreiben. So darf der Agent mehr wissen als die fragende Person, ohne es ihr sagen zu können.
5. **Nach unten nur über einen Menschen.** Soll aus einem solchen Lauf doch Wissen ins Wiki, gibt der Besitzer des Bereichs einen bereinigten Text frei. Davor läuft eine maschinelle Prüfung auf Personendaten, danach ein regelmäßiger Suchlauf über das ganze Wiki.
6. **Das Wiki speichert Zeiger und Verfahren, keine Daten:** wo etwas liegt und wie man es abfragt. Den Inhalt holt der Agent bei jeder Frage frisch.

Damit hängt nichts am Harness. Codex, Claude Code oder Pi sind austauschbar, auch mit einem Abo-Zugang. Hooks und zentral verwaltete Einstellungen eines Harness bleiben als zweite Linie sinnvoll. Voraussetzung ist, dass der Agentenprozess keinen anderen Ausgang hat: kein Netz außer zur Schleuse, Schreibrechte nur im eigenen Abteil.

Rechte pflegt weiter das Fachsystem, möglichst über Gruppen. Ein Vermittler wie Composio hält nur Verbindungen und kann einschränken, nie erweitern.

## Was das nicht löst

- Ein manipuliertes Dokument kann einen Lauf fehlleiten. Der Schaden bleibt auf die Rechte des Laufs begrenzt.
- Abgeleitetes Wissen: Aus vielen Datensätzen lässt sich etwas schließen, das einzeln nicht geschützt war. Dafür braucht es die Entscheidung des Bereichsbesitzers, keine Technik.
- Eine Zusammenfassung im Wiki kann Personendaten enthalten, die kein Muster erkennt. Die Prüfung senkt das Risiko, der Besitzer bleibt verantwortlich.
- Der Wasserstand ist grob: Ein Lauf, der eine einzige geschützte Quelle gelesen hat, ist für alle anderen Empfänger gesperrt. Läufe müssen deshalb klein geschnitten werden.
- Verdeckte Wege (Dateinamen, Zähler, Zeitpunkte) lassen sich verkleinern, nicht ausschließen.
- Ob ein Fachsystem die Frage „darf Person X Quelle Y lesen“ beantworten kann, ist je System zu prüfen.

## Offen für die Adapter

- Wie jeder Adapter die Kennung der Person serverseitig an den Agentenlauf gibt. Für Open WebUI mit Open Terminal ist das belegt (siehe Verweis oben).
- Wie die Werkzeugverbindung der Person in den Lauf kommt, ohne dass andere Läufe sie lesen können.
- Prüffall für jeden Adapter: Eine Person ohne Recht fragt nach einer Personalakte; der Agent mit Dienstkonto darf nichts liefern und nichts davon ins Wiki schreiben.
