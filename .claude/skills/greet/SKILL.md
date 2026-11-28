---
name: greet
description: Greets someone by name
argument-hint: [name]
arguments: [name]
---
Greet the person. NAME_VAR=$name FIRST_ARG=$ARGUMENTS[0] SKILL_DIR=${CLAUDE_SKILL_DIR}
YEAR_NOW=!`date +%Y`
Reply with one line that repeats NAME_VAR, FIRST_ARG, SKILL_DIR and YEAR_NOW exactly as given above.
