import subprocess,json,pathlib,tempfile,os,hashlib,sys
r=pathlib.Path(__file__).resolve().parents[4]; e=r/'beispiel/skills/besprechung-nachbereiten/evals'; out=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else e/'codex-neulauf'; out.mkdir(exist_ok=False)
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=r,text=True).strip()
cli_version=subprocess.check_output(['codex','--version'],text=True).strip()
base=['codex','--no-daemon','-a','never','exec','--ignore-user-config','--ignore-rules','--ephemeral','--skip-git-repo-check','--json','-m','gpt-6.1-sol','-s','read-only','-c','project_doc_max_bytes=0','-c','web_search="disabled"','--enable','skip_host_skill_discovery']
for f in ['hooks','plugins','memories','shell_tool','unified_exec','multi_agent','apps','skill_search','shell_snapshot']:
 base += ['--disable',f]
env={k:v for k,v in os.environ.items() if k not in ['OPENAI_API_KEY','CODEX_API_KEY'] and not k.startswith('CODEX_')};
for case in json.loads((e/'faelle.json').read_text()):
 id=case['id']; prompt='AGENTS.md (öffentliche Grundregeln):\n'+(r/'AGENTS.md').read_text()+'\nSKILL.md:\n'+(e.parent/'SKILL.md').read_text()+'\n'+case['prompt']+'\nNotiz '+case['eingabe']+':\n'+(e/case['eingabe']).read_text()
 (out/(id+'.prompt.txt')).write_text(prompt)
 with tempfile.TemporaryDirectory(prefix='semantik25-') as work:
  cmd=base+['-C',work,'-']; p=subprocess.run(cmd,input=prompt,text=True,capture_output=True,env=env)
 (out/(id+'.jsonl')).write_text(p.stdout.replace(str(pathlib.Path.home()), '<HOME>')); (out/(id+'.stderr.txt')).write_text(p.stderr.replace(str(pathlib.Path.home()), '<HOME>'))
 meta={'source_commit':commit,'model':'gpt-6.1-sol','cli':cli_version,'exit_code':p.returncode,'prompt_bytes':len(prompt.encode()),'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'command':base+['-C','<leerer temporärer Ordner>','-']}
 (out/(id+'.meta.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
 print(id, 'Exit', p.returncode, flush=True)
 p.check_returncode()
 if any(s in (p.stdout+p.stderr).lower() for s in ['usage limit','rate limit','limit reached']): raise RuntimeError('Limit: STOP')
 events=[json.loads(line) for line in p.stdout.splitlines()]
 assert any(x.get('type')=='turn.completed' for x in events), 'Kein abgeschlossener Lauf'
 answers=[x['item']['text'] for x in events if x.get('item',{}).get('type')=='agent_message']
 assert len(answers)==1, 'Keine eindeutige Antwort'
 (out/(id+'.antwort.md')).write_text(answers[0]+'\n')
