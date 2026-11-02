// Beispiel-Erweiterung für Pi (pi-coding-agent): dieselben zwei Sperren wie block-extern.sh und sperre-pfade.sh.
// Ablage: .pi/extensions/sperre.js (Projekt, erst nach Vertrauen) oder ~/.pi/agent/extensions/ (global).
// Grenze wie bei den Shell-Hooks: reine Textprüfung, ersetzt keine Rechte im Dateisystem.
import { readFileSync } from "node:fs"
import { join } from "node:path"

export function pruefe(toolName, input, verzeichnis) {
  if (/send_message|send_email|publish/.test(toolName)) return "Gelb: Mensch muss absenden."
  let muster = []
  for (const p of ["sperren.txt", join("system", "sperren.txt")]) {
    try {
      muster = readFileSync(join(verzeichnis, p), "utf8").split(/\r?\n/).filter((l) => l.trim() && !l.trim().startsWith("#"))
      break
    } catch {}
  }
  const ziel = Object.values(input ?? {}).filter((v) => typeof v === "string").join("\n").replaceAll("\\", "/")
  const treffer = muster.find((m) => ziel.includes(m))
  return treffer ? `Gesperrter Pfad (${treffer}). Mensch fragen.` : null
}

export default function (pi) {
  pi.on("tool_call", async (event) => {
    const grund = pruefe(event.toolName, event.input, process.cwd())
    if (grund) return { block: true, reason: grund }
  })
}
