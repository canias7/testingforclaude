import json, sys
for f in ['/tmp/hk.jsonl', '/tmp/hkskill.jsonl']:
    print('== ' + f)
    try:
        lines = open(f).read().splitlines()
    except Exception as e:
        print('missing', e); continue
    for l in lines:
        l = l.strip()
        if not l: continue
        try: d = json.loads(l)
        except Exception: print('BAD', l[:80]); continue
        ti = d.get('tool_input') if isinstance(d.get('tool_input'), dict) else {}
        out = {k: d.get(k) for k in ['hook_event_name','tool_name','mcp_server','source','name','worktree_path','path','file_path','cwd'] if d.get(k) is not None}
        out['ti_keys'] = sorted(ti.keys())
        for k in ['file_path','command','old_string','new_string']:
            if k in ti: out['ti.'+k] = str(ti[k])[:60]
        print(json.dumps(out))
