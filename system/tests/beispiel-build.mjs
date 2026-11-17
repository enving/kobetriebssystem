import assert from 'node:assert/strict'
import {readFileSync, readdirSync} from 'node:fs'
import {spawnSync} from 'node:child_process'
import {createHash} from 'node:crypto'
import {join} from 'node:path'

const files = (root, prefix = '', source = false) => readdirSync(join(root, prefix), {withFileTypes:true})
  .filter(entry => !source || (entry.name !== '__pycache__' && !/\.py[co]$/.test(entry.name)))
  .flatMap(entry => entry.isDirectory()
    ? files(root, join(prefix, entry.name), source)
    : [join(prefix, entry.name)]).sort()
const shippedSkills = ['skill-creator', 'wissen-pflegen']
const upstreamRoot = '.agents/skills/skill-creator'
const upstream = JSON.parse(readFileSync(join(upstreamRoot, 'UPSTREAM.json')))
assert.equal(upstream.license, 'Apache-2.0')
assert.match(upstream.commit, /^[a-f0-9]{40}$/)
assert.deepEqual(files(upstreamRoot, '', true), [...Object.keys(upstream.files), 'UPSTREAM.json'].sort())
for (const [file, sha] of Object.entries(upstream.files)) {
  assert.equal(createHash('sha256').update(readFileSync(join(upstreamRoot, file))).digest('hex'), sha,
    `Upstream-Datei verändert: ${file}`)
}
const run = (...args) => spawnSync('sh', ['installation/bauen.sh', ...args], {encoding:'utf8'})
for (const args of [['demo', '--unbekannt'], ['demo', '--mit-beispielen', 'extra'], []]) {
  assert.notEqual(run(...args).status, 0)
}
for (const args of [['demo'], ['demo', '--mit-beispielen'], ['demo']]) {
  const r = run(...args); assert.equal(r.status, 0, r.stderr); console.log(r.stdout.trim())
  const names = readdirSync('dist/ko-basis/skills')
  assert.equal(names.includes('besprechung-nachbereiten'), args.length === 2)
  assert.ok(names.every(n => !n.startsWith('_')))
  for (const skill of shippedSkills) {
    const source = join('.agents/skills', skill)
    assert.ok(names.includes(skill), `Standard-Skill fehlt: ${skill}`)
    for (const target of [join('dist/ko-basis/skills', skill), join('dist/ko-codex/.agents/skills', skill)]) {
      assert.deepEqual(files(target), files(source, '', true), `Beilagen fehlen oder Zwischendateien enthalten: ${target}`)
      for (const file of files(source, '', true)) {
        assert.deepEqual(readFileSync(join(target, file)), readFileSync(join(source, file)),
          `Paketinhalt weicht ab: ${target}/${file}`)
      }
    }
  }
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
console.log('OK: Upstream-Prüfsummen und vollständige allgemeine Skills in Claude-/Codex-Paketen')
