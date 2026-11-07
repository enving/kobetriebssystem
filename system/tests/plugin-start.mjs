import assert from 'node:assert/strict'
import {mkdtempSync, cpSync, readFileSync, rmSync, writeFileSync} from 'node:fs'
import {tmpdir} from 'node:os'
import {join, resolve} from 'node:path'
import {spawnSync} from 'node:child_process'
const repo = resolve(import.meta.dirname, '../..')
const temp = mkdtempSync(join(tmpdir(), 'plugin-test-'))
const root = join(temp, 'Plugin mit Leerzeichen')
try {
  assert.equal(spawnSync('sh', ['installation/bauen.sh', '26.0-test'], {cwd: repo}).status, 0)
  cpSync(join(repo, 'dist/ko-basis'), root, {recursive:true})
  const hooks = JSON.parse(readFileSync(join(root, 'hooks/hooks.json'))).hooks
  const run = (command, input = '{}', extra = {}) => spawnSync('sh', ['-c', command], {cwd: temp, env:{...process.env, CLAUDE_PLUGIN_ROOT:root, ...extra}, input, encoding:'utf8'})
  const command = hooks.SessionStart[0].hooks[0].command
  const result = run(command)
  assert.equal(result.status, 0)
  for (const file of ['AGENTS.md', 'kontext/index.md', 'kontext/landkarte.md']) {
    assert.ok(result.stdout.includes(readFileSync(join(repo, file), 'utf8')))
  }
  assert.ok(result.stdout.includes(readFileSync(join(root, '.claude-plugin/plugin.json'), 'utf8')))
  assert.ok(result.stdout.includes('26.0-test'))
  for (const file of ['AGENTS.md', 'kontext/index.md', 'kontext/landkarte.md', '.claude-plugin/plugin.json']) {
    const path = join(root, file), original = readFileSync(path)
    rmSync(path)
    const missing = run(command)
    assert.equal(missing.status, 0)
    assert.ok(missing.stdout.includes(`FEHLER: Plugin-Pflichtquelle fehlt oder ist nicht lesbar: ${file}`))
    writeFileSync(path, original)
  }
  assert.ok(run('sh ' + JSON.stringify(join(root, 'hooks/sessionstart-plugin.sh')), '{}', {CLAUDE_PLUGIN_ROOT:''}).stdout.includes('FEHLER: CLAUDE_PLUGIN_ROOT fehlt'))
  writeFileSync(join(root, 'sperren.txt'), 'test-geheim\n')
  for (const [i, input] of [[0, '{"tool_name":"Read","tool_input":{"file_path":"test-geheim"}}'], [1, '{"tool_name":"send_email"}']]) {
    assert.equal(run(hooks.PreToolUse[i].hooks[0].command, input).status, 2)
    assert.equal(run(hooks.PreToolUse[i].hooks[0].command).status, 0)
  }
  console.log('OK: Pluginstart, Quellen, Version, Fehlermeldungen und Sperrhooks')
} finally { rmSync(temp, {recursive:true, force:true}) }
