// Beispiel-Plugin für OpenCode: dieselben zwei Sperren wie block-extern.sh und sperre-pfade.sh.
// Ablage: .opencode/plugins/sperre.js (Projekt) oder ~/.config/opencode/plugins/ (global).
// Liest system/sperren.txt aus dem Projektordner (Muster = Teilstring des Pfades/Kommandos).
// Grenze wie bei den Shell-Hooks: reine Textprüfung, ersetzt keine Rechte im Dateisystem.
import { readFileSync } from "node:fs"
import { join } from "node:path"

export const Sperre = async ({ directory }) => {
  const muster = () => {
    for (const p of ["sperren.txt", join("system", "sperren.txt")]) {
      try {
        return readFileSync(join(directory, p), "utf8").split(/\r?\n/).filter((l) => l.trim() && !l.trim().startsWith("#"))
      } catch {}
    }
    return []
  }
  return {
    "tool.execute.before": async (input, output) => {
      if (/send_message|send_email|publish/.test(input.tool)) throw new Error("Gelb: Mensch muss absenden.")
      const ziel = Object.values(output.args ?? {}).filter((v) => typeof v === "string").join("\n").replaceAll("\\", "/")
      for (const m of muster()) if (ziel.includes(m)) throw new Error(`Gesperrter Pfad (${m}). Mensch fragen.`)
    },
  }
}
