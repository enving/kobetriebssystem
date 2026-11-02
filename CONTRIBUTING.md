# Mitmachen – Verbesserungen zurück in die Vorlage

Diese Vorlage steht unter der **Mozilla Public License 2.0** (`LICENSE`). Wer sie in einem Unternehmen einsetzt und weiterentwickelt, soll Verbesserungen, die *der Vorlage* nützen, per Pull Request hierher zurückgeben.

## Was zurück gehört
Alles, was nicht an ein bestimmtes Unternehmen gebunden ist:
- bessere Grundregeln, Ampel, Lernschleife, Sicherheitsvorgaben (`AGENTS.md`, `SICHERHEIT.md`, `system/`)
- neue oder verbesserte Hooks, Skripte, Rollout- und Release-Werkzeuge
- allgemeine Skill-Vorlagen, Prüffall-Muster, Glossar-Begriffe, Fehlerkorrekturen in der Doku

## Was bei euch bleibt
Firmendaten, Kunden- und Personendaten, eigene Skills, Kontext, Automatisierungen, Landkarte. **Nie** in einen PR an dieses Repo.

## So geht's
1. Änderung im eigenen Fork von allem Firmenspezifischen trennen (eigener Zweig, nur die allgemeinen Dateien).
2. Prüfen: Steht irgendwo ein Firmenname, Kundenname, eine interne URL, ein Zugang? Dann raus.
3. Pull Request gegen `main`. Kurz beschreiben: *was* wurde besser und *wie wurde es geprüft*.

## Was die Lizenz verlangt – und was nicht
- MPL-2.0 ist eine Copyleft-Lizenz auf **Dateiebene**: Wer eine Datei dieser Vorlage ändert und die Ergebnisse **weitergibt** (z. B. an Kunden, Töchter, Dritte), muss diese geänderten Dateien unter MPL-2.0 und im Quelltext verfügbar machen. Eigene, neue Dateien dürfen privat bleiben.
- Die Lizenz **erzwingt keinen Pull Request** hierher und greift nicht bei rein interner Nutzung. Der Rückfluss an dieses Repo ist eine ausdrückliche Bitte und Erwartung des Projekts, keine Lizenzpflicht.
