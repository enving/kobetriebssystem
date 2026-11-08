// Testbatterie für alle Adapter. Aufruf: node system/tests/pruefen.mjs [pfad-zu-sh]
// Prüft: Shell-Hooks (Claude-Code-Datenform), OpenCode-Plugin, Pi-Erweiterung gegen dieselben Fälle.
// Ausgabe je Fall: OK | FEHLER | LÜCKE (erwartet, bekannt) | NEU-GESCHLOSSEN (Lücke ist nicht mehr da).
import { readFileSync, mkdtempSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { join, dirname } from "node:path"
import { spawnSync } from "node:child_process"
import { fileURLToPath, pathToFileURL } from "node:url"

const hier = dirname(fileURLToPath(import.meta.url))
const hooks = join(hier, "..", "hooks")
const sh = process.argv[2] || "sh"
const { faelle } = JSON.parse(readFileSync(join(hier, "faelle.json"), "utf8"))
const proj = mkdtempSync(join(tmpdir(), "sperre-"))
writeFileSync(join(proj, "sperren.txt"), "geheim-ordner\n")

const gross = (t) => ({ read: "Read", glob: "Glob", bash: "Bash" })[t] || t
const claudeJson = (f) => JSON.stringify({ tool_name: gross(f.tool), tool_input: f.tool === "bash" ? { command: f.befehl } : f.pfad ? (f.tool === "glob" ? { pattern: f.pfad } : { file_path: f.pfad }) : {} })
// Codex hat kein eigenes Lese-Werkzeug: Lesen/Suchen laufen als Bash-Befehl (tool_name "Bash", tool_input.command).
const codexJson = (f) => JSON.stringify({ hook_event_name: "PreToolUse", tool_name: f.tool === "send_message" ? "mcp__x__send_message" : "Bash", tool_input: f.tool === "send_message" ? {} : { command: f.tool === "bash" ? f.befehl : (f.tool === "glob" ? "dir " : "type ") + f.pfad } })
const args = (f) => (f.tool === "bash" ? { command: f.befehl } : f.pfad ? { filePath: f.pfad } : {})

const shell = async (f, json) => {
  for (const s of ["block-extern.sh", "sperre-pfade.sh"]) {
    const r = spawnSync(sh, [join(hooks, s)], { input: json(f), env: { ...process.env, SPERRLISTE: join(proj, "sperren.txt") }, encoding: "utf8" })
    if (r.status === 2) return "block"
    if (r.error || r.status !== 0) return "fehler:" + (r.error?.message || r.status)
  }
  return "ok"
}

const adapter = {
  "sh (Claude Code)": (f) => shell(f, claudeJson),
  "sh (Codex)": (f) => shell(f, codexJson),
  "opencode": async (f) => {
    const { Sperre } = await import(pathToFileURL(join(hooks, "opencode-sperre.js")))
    const h = (await Sperre({ directory: proj }))["tool.execute.before"]
    try { await h({ tool: f.tool }, { args: args(f) }); return "ok" } catch { return "block" }
  },
  "pi": async (f) => {
    const { pruefe } = await import(pathToFileURL(join(hooks, "pi-sperre.js")))
    return pruefe(f.tool, args(f), proj) ? "block" : "ok"
  },
}

let fehler = 0
for (const [name, fn] of Object.entries(adapter)) {
  console.log(`\n== ${name}`)
  for (const f of faelle) {
    const ist = await fn(f)
    let urteil
    if (ist.startsWith("fehler")) { urteil = "FEHLER(" + ist + ")"; fehler++ }
    else if (f.luecke) urteil = ist === "block" ? "NEU-GESCHLOSSEN" : "LÜCKE"
    else if (ist === f.erwartet) urteil = "OK"
    else { urteil = "FEHLER"; fehler++ }
    console.log(`${urteil.padEnd(16)} ${f.id.padEnd(20)} erwartet=${f.erwartet} ist=${ist}`)
  }
}
const bau = spawnSync("python3", [join(hier, "klassifizierung.py")], { encoding: "utf8", timeout: 120000 })
console.log(bau.stdout)
if (bau.status !== 0 || bau.error) {
  console.error(bau.stderr || bau.error)
  fehler++
}
console.log(fehler ? `\n${fehler} unerwartete Abweichung(en)` : "\nkeine unerwarteten Abweichungen")
process.exit(fehler ? 1 : 0)
