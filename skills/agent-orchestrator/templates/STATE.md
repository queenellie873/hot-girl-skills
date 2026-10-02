# STATE: <project name>

Source of truth for this project. Owned by the lead. Workers write their own STATUS.md; the lead rolls them up here.
Rules: update after every meaningful event, before replying to the human. Never delete history. Absolute dates only (YYYY-MM-DD). Names are lowercase.

## NEEDS HUMAN

<!-- Blocking items only. Check the box and move to Decisions log when answered. -->
- [ ] YYYY-MM-DD lead: <question> options: a) <option>, b) <option> recommend: a

## Goal

<1 to 3 sentences: what we are making and for whom.>
Deadline: YYYY-MM-DD
Constraints: <budget, tools, anything off-limits>

## Agents

| name | surface/id | brief | status file | status | last update |
|------|------------|-------|-------------|--------|-------------|
| lead | <e.g. cmux surface:1> | this file | this file | working | YYYY-MM-DD HH:MM |
| <name> | <e.g. cmux surface:2, tmux work:1, subagent, this session> | [<NAME>-BRIEF.md](<NAME>-BRIEF.md) | work/<name>/STATUS.md | not started | YYYY-MM-DD HH:MM |

<!-- status: not started | waiting on human | working | blocked | done -->

## Decisions log

<!-- For approvals of specific actions, quote the human's exact words. -->
- YYYY-MM-DD <who>: <decision> (<why, in a few words>)

## Done

- YYYY-MM-DD <name>: <what finished> -> <file or result>

## Next

- <name>: <next concrete step>

## Log

<!-- Append-only. One line per event. Never edit old lines. Message events: sent <id> <type> -> <to> via <transport>: <summary> / recv <id> <type> <- <from> via <transport>: <summary> / handled <id> -->
- YYYY-MM-DD HH:MM lead: state log created
