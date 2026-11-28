---
name: hk
description: Hook test skill. Use only when invoked as /hk.
hooks:
  PreToolUse:
    - matcher: Bash
      hooks:
        - type: command
          command: "cat >> /tmp/hkskill.jsonl; echo >> /tmp/hkskill.jsonl"
          once: true
---
Reply with exactly: HK skill loaded. Do not run any tools.
