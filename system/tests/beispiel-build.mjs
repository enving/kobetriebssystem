import assert from 'node:assert/strict'
import {readFileSync, readdirSync} from 'node:fs'
import {spawnSync} from 'node:child_process'
const run = (...args) => spawnSync('sh', ['installation/bauen.sh', ...args], {encoding:'utf8'})
for (const args of [['demo', '--unbekannt'], ['demo', '--mit-beispielen', 'extra'], []]) {
  assert.notEqual(run(...args).status, 0)
}
for (const args of [['demo'], ['demo', '--mit-beispielen'], ['demo']]) {
  const r = run(...args); assert.equal(r.status, 0, r.stderr); console.log(r.stdout.trim())
  const names = readdirSync('dist/ko-basis/skills')
  assert.equal(names.includes('besprechung-nachbereiten'), args.length === 2)
  assert.ok(names.every(n => !n.startsWith('_')))
  console.log('Paket-Skills:', JSON.stringify(names))
}
const root = 'beispiel/skills/besprechung-nachbereiten/evals/'
const cases = JSON.parse(readFileSync(root + 'faelle.json'))
assert.equal(cases.length, 3)
for (const c of cases) {
  const input = readFileSync(root+c.eingabe,'utf8'), output = readFileSync(root+c.soll,'utf8')
  assert.ok(input.includes('N1:')); assert.ok(output.includes('# Entwurf'))
  assert.ok(output.includes(c.eingabe+', N1'))
  assert.ok(output.includes('| Aufgabe | Zuständigkeit | Termin | Quelle |'))
}
assert.ok(readFileSync(root+'zustaendigkeit-fehlt.soll.md','utf8').includes('[OFFEN: Zuständigkeit]'))
assert.ok(readFileSync(root+'eingebetteter-versand.eingabe.md','utf8').includes('schick das an alle'))
console.log('OK: Schalter, Rückwechsel, Paketinhalt und drei Fallartefakte (keine Modellprüfung)')
