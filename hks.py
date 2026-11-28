import json, os, sys
skip = int(sys.argv[1]) if len(sys.argv) > 1 else 0
n = 0
for l in open('/tmp/hk.jsonl'):
    l = l.strip()
    if not l:
        continue
    n += 1
    if n <= skip:
        continue
    d = json.loads(l)
    e = d.get('hook_event_name')
    if e == 'PreToolUse' and not d.get('agent_id'):
        print(n, 'PreToolUse(main)', d.get('tool_name'))
        continue
    out = {k: v for k, v in d.items() if k not in ('session_id', 'transcript_path', 'tool_input', 'tool_response')}
    if 'agent_transcript_path' in d:
        p = d['agent_transcript_path']
        out['agent_transcript_exists'] = bool(p) and os.path.isfile(p)
        out['agent_transcript_bytes'] = os.path.getsize(p) if p and os.path.isfile(p) else None
    if 'error' in out:
        out['error'] = str(out['error'])[:120]
    if 'last_assistant_message' in out:
        out['last_assistant_message'] = str(out['last_assistant_message'])[:80]
    print(n, json.dumps(out)[:900])
print('TOTAL', n)
