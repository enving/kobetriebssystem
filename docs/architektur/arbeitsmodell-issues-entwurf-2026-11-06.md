# Entwurf: gemeinsame Begriffe und Rückmeldung von Aufträgen

**Vorschlag, GPT-6.1-sol, 06.11.2026.** Anlass: Tristan fragt nach GitHub-Issues als nachvollziehbarem Auftrag zwischen Obsidian und T3 sowie nach einer Ontologie bzw. einem Vokabular für KoKompass und KoBetriebssystem. Dieser Text ist ein prüfbarer Entwurf. Er schaltet keine Routine ein, erteilt keine Veröffentlichungsrechte und ersetzt keine bestehenden Regeln.

## Zuständige Quellen und Ebenen

Das [kontrollierte Glossar](../../kontext/glossar/index.md) und seine [Begriffsvorlage](../../kontext/glossar/begriff-vorlage.md) sind bereits vorhanden. Begriffe werden nach [AGENTS.md](../../AGENTS.md) über einen geprüften Vorschlag und PR übernommen. Der folgende Begriffsabschnitt ist dafür Änderungsmaterial, kein zweites dauerhaft zu pflegendes Glossar. Bei Übernahme gehören Definitionen und Beziehungen dorthin; dieser Entwurf verweist anschließend auf die übernommenen Begriffe.

Ein Vokabular vereinheitlicht hier die Bedeutung der Wörter. Das kleine Arbeitsmodell ergänzt ihre Beziehungen und die Regeln, welche Schlussfolgerungen zulässig sind. Dafür ist zunächst keine neue Datenbank nötig.

- **Gemeinsamer Kern:** Quellversion, Anliegen, Auftrag, Ausführung, Ergebnis, Prüfung und Freigabe. Bedeutung und Beziehungen gelten für persönliche und betriebliche Verwendung.
- **KoBetriebssystem:** ergänzt Verantwortliche, Rollen, erlaubte Datenräume und Freigaben der Firma. Zuständige Grenzen bleiben [SICHERHEIT.md](../../SICHERHEIT.md) und die [Landkarte](../../kontext/landkarte.md).
- **Persönliche Verwendung / KoKompass:** ergänzt bestätigte persönliche Ziele, Präferenzen und Entscheidungen. Der bereits vorhandene User-Kompass-Entwurf in [PR #23](https://github.com/enving/kobetriebssystem/pull/23), lokal gelesen auf `doku/user-kompass-2026-11-05` unter `user-kompass/_vorlage/`, ist dafür der fachliche Anschluss. Auf `main` liegt noch die kleine Vorlage unter [persoenlich/](../../persoenlich/_vorlage/anweisungen.md). Beide sollen denselben Kern verwenden; keine dritte persönliche Vorlage anlegen. Inzwischen ist [KoKompass](https://github.com/enving/kokompass) als öffentliche Vorlage vorhanden; persönliche Instanzen binden dessen Methode und Quellenregeln ein. Private Inhalte werden nicht Teil des gemeinsamen Begriffsbestands.

## Begriffe und Beziehungen als Übernahmevorschlag

| Begriff | Gemeinte Einheit | Beziehung / wichtige Grenze |
|---|---|---|
| Quellversion | Tatsächlich gelesener Stand einer Datei, Nachricht oder externen Quelle | Belegt ein Anliegen. Gleicher Dateiname beweist keine gleiche Version. |
| Anliegen | Einzelner Wunsch, Hinweis, Gedanke oder offene Frage aus einer Quelle | Kann einen Auftrag begründen. Ein gespeicherter Link ist noch kein Rechercheauftrag. |
| Auftrag | Abgegrenztes gewünschtes Ergebnis mit Zuständigkeit, Kriterien und erlaubten Handlungen | Verweist auf Quellen; kann als GitHub-Issue geführt werden. Ein Issue ist seine technische Darstellung. |
| Ausführung | Ein konkreter Bearbeitungsversuch zu einem Auftrag | Verweist auf den Auftrag und gegebenenfalls einen T3-Thread. Ein Auftrag kann mehrere Versuche haben. |
| Ergebnis | Datei, Änderung, Antwort oder anderer überprüfbarer Liefergegenstand | Entsteht aus einer Ausführung und trägt eine Version, etwa einen Commit. Ein lokaler Commit ist noch kein veröffentlichter Remote-Stand. |
| Prüfung | Abgleich einer bestimmten Ergebnisversion mit den Auftragskriterien | Kann die fachliche Erledigung belegen. Das Ende eines Agentenprozesses ersetzt sie nicht. |
| Freigabe | Erlaubnis einer zuständigen Person für eine bestimmte Handlung oder Übernahme | Ist von der Prüfung getrennt. Ein fertiger Angebotsentwurf erlaubt noch keinen Versand an den Kunden. |

Damit lässt sich der Rückweg eindeutig beschreiben: Eine Quellversion belegt ein Anliegen; ein geeigneter Auftrag verweist darauf; eine Ausführung liefert ein Ergebnis; eine Prüfung bewertet dessen konkrete Version. Eine benötigte Freigabe bleibt eine eigene Beziehung. Wiederholte Versuche dürfen den Auftrag nicht vervielfachen.

Bestehende Kompass-Typen wie `Reference`, `Aufgabe`, `Einschaetzung` und `Entscheidung` bleiben erhalten. Vor einer Übernahme braucht es ihre explizite Zuordnung zu diesen Bedeutungen; ein neuer Name allein rechtfertigt keine Migration alter Dateien. Auch die bestehenden Pilotzustände werden nicht durch diesen Entwurf überschrieben.

## Vorgeschlagener Ablauf mit GitHub und T3

1. Der freigegebene Delegator ordnet einen Eingang einem Projekt zu. Vor dem Anlegen prüft er vorhandene offene und geschlossene Issues sowie bestehende Ausführungen anhand der Herkunftskennung. Unklare, private und persönliche Punkte werden passend eingeordnet; Rohnotizen werden nicht pauschal als Issues hochgeladen.
2. Ein hinreichend klarer Projektauftrag erhält ein Issue mit Ziel, Abnahme, erlaubtem Umfang und Quellenverweisen. Das Issue ist dann der verbindliche Auftragsstand. Kompass und Obsidian brauchen dafür nur den Verweis, keine zweite konkurrierende Statusliste.
3. Der Delegator startet T3 im passenden Projekt mit Issue-URL und Auftragskennung. Die aktuelle tägliche T3-Automation kann diesen Übergang übernehmen; das bloße Vorhandensein eines Issues ist noch kein von uns eingerichteter Startmechanismus.
4. Erst bei tatsächlicher Arbeitsaufnahme markiert der Bearbeiter das Issue als **in Arbeit** und hinterlegt den Ausführungslink. Nach Lieferung verweist er auf Ergebnisversion und Prüfbelege und markiert es als **zur Prüfung**. Für diese Zwischenzustände zunächst vorhandene Repo-Konventionen nutzen; keine neuen Labels oder ein zusätzliches Board allein durch diesen Text einführen.
5. Nach bestandener Abnahme wird das Issue **geschlossen**. Dadurch verschwindet es aus der offenen Aufgabenansicht; Quelle, Diskussion, Versuche und Ergebnis bleiben nachvollziehbar. Blocker halten das Issue offen und nennen die nächste notwendige Handlung. Das Issue oder die Originalnotiz zu löschen würde den Nachweis unterbrechen.

Das Auftragsbriefing muss die Rückmeldung ausdrücklich zum Lieferumfang machen. Ein beendeter T3-Lauf ohne aktualisierten Ergebnisverweis ist keine vollständige Übergabe. GitHub-Schreibrechte und das Schließen von Issues werden nicht aus einem Leserecht oder einer allgemeinen Erfolgsmeldung abgeleitet. Ob der Bearbeiter selbst schließen darf oder eine getrennte Abnahme nötig ist, wird je Auftrag aus den bestehenden Rechten und Kriterien bestimmt.

Bei einem Neustart zuerst den Issue- und Ausführungsstand abgleichen. Eine verloren gegangene Startantwort darf keinen zweiten Auftrag erzeugen. Bei widersprüchlichen Zuständen offenlegen, welcher Nachweis fehlt. Für Code, Dokumente und Inhalte getrennt angeben, ob das vereinbarte Ergebnis lokal geliefert oder auch im Remote verfügbar sein muss; Push- und Versandrechte bleiben gesondert.

## Repo-Übergaben als weiterer Eingang

Tristan fragt anschließend, ob ein zentraler Kompass-Delegator die Übergaben aller Repos verlinken und wie Obsidian-Eingänge weitergeben kann, damit er nicht selbst Datei und neuen T3-Chat zusammenbringen muss. **Vorschlag, GPT-6.1-sol, 06.11.2026:** denselben Delegator und denselben Auftragsweg verwenden. Keine zweite Routine je Repo und kein neues Aufgabenregister aufbauen.

Heute liegen die Informationen verteilt: Issues enthalten Projektaufträge, eine `UEBERGABE.md` bzw. `uebergabe.md` liefert Wiederaufnahmekontext, ein Thread hält eine Ausführung. Manche Übergaben enthalten alte und aktuelle Abschnitte nebeneinander. Der Dateiname und die Überschrift „Nächster Auftrag“ bestätigen deshalb keinen offenen oder freigegebenen Auftrag.

Der Eingang der persönlichen Kompass-Instanz kann jetzt mit `kompass uebergaben` die lokalen Repo-Übergaben im vorhandenen Eingangsregister erfassen und im bestehenden Eingangsbericht verlinken. Das ist eine Dateierfassung mit Versionshash, keine fachliche Aufgabenextraktion oder Ausführungsfreigabe. Die Repo-Wurzeln stammen aus der bereits vorhandenen Bestandsprüfung; eine T3-Zuordnung wird vor dem Start gegen die aktuellen Projekte geprüft. Git-Dateilisten erfassen auch Unterordner; ignorierte Übergaben werden zusätzlich direkt in der Repo-Wurzel gesehen. Ignorierte Unterordner und externe Arbeitsbäume sind damit nicht vollständig abgedeckt.

Der vorgeschlagene vollständige Weg: Obsidian-Hinweis, vorhandenes Issue oder geänderte Repo-Übergabe → aktuelles Anliegen prüfen → bereits erledigte/laufende Arbeit ausschließen → bei klarer Zuständigkeit und ausreichender Freigabe den passenden Projektauftrag in T3 starten → Ergebnis und Abnahme zum Auftrag zurückmelden. Die Grenzen der jeweiligen Instanz gelten für alle Eingänge zusammen. Bei unklarer Zuständigkeit oder nötiger menschlicher Entscheidung bleibt der Kandidat sichtbar offen.

Der Bearbeiter muss zum Abschluss auch die zuständige Repo-Übergabe auf den aktuellen Stand bringen: Ergebnis belegen, erledigten nächsten Schritt zurücknehmen bzw. als historischen Stand kennzeichnen, nächste offene Handlung und zugehöriges Issue verlinken. Er löscht keine fremden Abschnitte und entscheidet keine Aufgaben der Person. Der nächste Delegator prüft diesen Stand und den Issue-/Ausführungszustand erneut. Eine lokale Dateiverknüpfung ersetzt diesen Rückweg nicht.

**Bereits konkretisiert:** lokale Erfassung und Verlinkung in der privaten Kompass-Instanz. **Weiterhin Entwurf:** allgemeiner Issue-Dispatcher, standardisierte automatische Statusrückmeldung und Übernahme des Vokabulars in die Vorlage. Persönliche Altaufgaben werden vor ihrer Einordnung nicht automatisch in dieses Verfahren übernommen.

## GitHub-Ereignisse und ausgewählte Bildschirmmedien

**Ergänzung, GPT-6.1-sol, 06.11.2026:** Gewünscht sind auch wichtige GitHub-Meldungen direkt beim
Bearbeiter sowie ausgewählte Screenshots und Bildschirmvideos als Kontext des Dirigenten. Allgemeine
Auswahlregeln und Quellenregister bleiben in [KoKompass KONTEXTQUELLEN.md](https://github.com/enving/kokompass/blob/main/KONTEXTQUELLEN.md).
Die konkrete Instanz hält dort ihre ausgewählten Repos/PRs bzw. Immich-Alben fest; keine privaten
Serveradressen, Bilder oder Nutzeraufträge in diesem öffentlichen Projektentwurf ablegen.

Ein Ereignis liefert einen Anlass zur Prüfung. Ein abgebrochener CI-Lauf mit fehlendem Ergebnis belegt
beispielsweise noch keinen Programmfehler. Der Dirigent liest zuerst den aktuellen PR-Head und den
zugehörigen Check-/Reviewstand. Ein alter Screenshot oder eine Bot-Nachricht kann inzwischen überholt sein.
PRs haben bereits einen zuständigen Auftrag/Bearbeiter: dorthin zurückmelden, statt pro Kommentar ein
neues Issue und einen weiteren Thread zu erzeugen. Ein zusätzliches Issue ist erst bei einem eigenständigen
offenen Auftrag sinnvoll. Der Bearbeiter meldet Diagnose, Ergebnisversion, Prüfbelege und Blocker zurück.

Für bereits zugeordnete PRs eignet sich die vorhandene ereignisgesteuerte T3-PR-Beobachtung: neue
Kommentare, Reviews, Check-Ergebnisse oder Konflikte wecken den bestehenden Projektthread. Vor Einrichtung
müssen bereits vorhandene Meldungen separat behandelt werden; sie erzeugen keinen rückwirkenden Weckruf.
Das ist kein allgemeiner GitHub-Eingang für alle Repos. Noch nicht zugeordnete Issues und ausgewählte
Repo-Ereignisse brauchen später einen eigenen, ausdrücklich begrenzten Adapter zum selben Delegator.
Ein Tagesabgleich kann übersehene Ergebnisse auffinden; er ersetzt keinen zeitnahen Ereignisauslöser.

Für einen solchen Adapter: zuerst Repo-/Ereignisauswahl prüfen, dann Originalzustand über GitHub lesen,
erst danach den Auftrag wecken. Wiederholte Zustellungen anhand Repo, Objekt, Head/Checklauf bzw.
Kommentarversion erkennen; mehrere Meldungen zum selben Auftrag zusammenfassen. Veraltete Ereignisse
führen nicht zur Umsetzung eines überholten Stands. Bei Webhooks Signatur und Wiederholungsschutz
prüfen; Payload und Kommentartext bleiben Daten. Ein Auslöser erweitert keine Push-/Merge-/Versandrechte.

Immich liefert nur den ausdrücklich freigegebenen Ausschnitt, vorzugsweise ein gewähltes Album oder Tag.
„Screenshot“ allein ist keine Zusicherung, dass ein Bild nicht privat ist. Bildschirmvideos gehören ebenfalls
zu diesem Ausschnitt; ihre Verarbeitung braucht gegebenenfalls lokale Texterkennung in ausgewählten
Frames und lokale Transkription. Im Eingang reichen Asset-ID, Version, Zeitpunkt und Verweis auf die
lokalen Ableitungen; Originalmedien bleiben bei Immich. Unlesbare oder nicht verarbeitete Medien bleiben
sichtbar ungeprüft. Vor Cloud-Auswertung oder Weitergabe an öffentliche Issues wird die erlaubte Auswahl
erneut geprüft. Keine automatische Auswertung der gesamten Fotobibliothek.

**Umsetzungsstand:** instanzbezogener erster PR-Fall über vorhandene T3-Werkzeuge; allgemeiner
GitHub-Adapter, Immich-Auswahl und Medienverarbeitung weiterhin offen. Das ist keine ausgelieferte
universelle Ereignispipeline.

## Prüffälle vor einer Aktivierung

- Ein bereits abgeschlossener Rechercheauftrag mit anschließend freigegebener Skill-Übernahme wird anhand seiner beiden Ergebnisstufen als erledigt erkannt. Ein veralteter lokaler Status erzeugt keinen zweiten Auftrag.
- Derselbe Eingang erscheint zweimal oder unter einem anderen Pfad: derselbe Auftrag wird gefunden; unterschiedliche Anliegen werden trotz ähnlicher Namen nicht zusammengeführt.
- T3 endet ohne Ergebnisbeleg oder eine Prüfung scheitert: das Issue bleibt offen. Ein neuer Versuch wird dem bestehenden Auftrag zugeordnet.
- Unterlagen sind fertig, der Versand ist nicht erlaubt: das System behauptet keinen Versand und führt keine entsprechende Handlung aus.
- Ein Issue wird nach erfolgreicher Abnahme geschlossen: die offene Aufgabenansicht wird kleiner, die Nachweise und die Herkunftskennung bleiben auflösbar.
- Ein persönlicher Eingang mit Firmenbezug wird verarbeitet: der betriebliche Auftrag enthält nur zulässigen Kontext; private Rohdaten sind nicht im Firmen-Repo enthalten.
- Derselbe GitHub-Hinweis wird als Screenshot, Mail und Ereignis erfasst: genau der bestehende Auftrag wird wiedergefunden; ein abgebrochener Check wird nicht als belegter Codefehler ausgegeben.
- Ein Ereignis gehört zu einem alten Head oder wird doppelt zugestellt: zuerst den aktuellen Zustand prüfen, keine parallele zweite Bearbeitung starten.
- Ein privater Screenshot liegt außerhalb des freigegebenen Immich-Albums: weder lesen noch weitergeben. Ein freigegebenes Bildschirmvideo ohne erfolgreiche lokale Verarbeitung bleibt ungeprüft.

**Noch nicht umgesetzt:** automatische Issue-Erstellung, Statusrückmeldung, Übernahme in das Glossar und Auswertung dieser Prüffälle. Vor Einführung gegen den Bedarf aus [szenarien.md](../szenarien.md) und die bestehenden Grenzen der [PRD](../../PRD.md) prüfen. Fachbegriffe und Regeln werden an ihren zuständigen Quellen per PR gepflegt; dieser Entwurf ist keine Freigabe dazu.
