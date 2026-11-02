#!/bin/sh
# Beispiel Stop-Hook (Claude Code): mahnt eine Übergabe an, wenn das Kontextfenster voll wird.
# Eingabe: JSON auf stdin (transcript_path, stop_hook_active, session_id).
# Ausgabe {"decision":"block","reason":…} zwingt den Agenten, vor dem Stopp noch zu handeln.
# Schutz gegen Endlosschleife: stop_hook_active beachten; je Sitzung nur einmal mahnen.
# Grobe Schätzung statt Tokenzählung: Größe des Transkripts in Bytes (~4 Bytes je Token).
SCHWELLE_BYTES="${KONTEXT_SCHWELLE_BYTES:-1200000}"
in=$(cat)
case "$in" in *'"stop_hook_active":true'*|*'"stop_hook_active": true'*) exit 0;; esac
t=$(printf '%s' "$in" | sed -n 's/.*"transcript_path" *: *"\([^"]*\)".*/\1/p')
s=$(printf '%s' "$in" | sed -n 's/.*"session_id" *: *"\([^"]*\)".*/\1/p')
[ -f "$t" ] || exit 0
merker="${TMPDIR:-/tmp}/kontextmahnung-${s:-x}"
[ -f "$merker" ] && exit 0
[ "$(wc -c < "$t")" -ge "$SCHWELLE_BYTES" ] || exit 0
: > "$merker"
echo '{"decision":"block","reason":"Kontextfenster wird voll. Schreibe jetzt eine kurze Übergabe (Stand, offene Punkte, Entscheidungen, Fallen) ins Logbuch und sage dem Menschen, dass er /clear tippen kann."}'
exit 0
