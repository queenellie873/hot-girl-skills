# the brief pattern

how Hot Girls Code runs an agent team, e.g. for planning an event: one lead agent, a handful of workers, and u approving the important stuff.

```
project/
├── STATE.md              <- the lead's state log (source of truth)
├── DESIGNER-BRIEF.md     <- what this worker builds, rules, first move
├── BUILDER-BRIEF.md
├── work/
│   ├── designer/
│   │   └── STATUS.md     <- done / next / NEEDS HUMAN / log
│   └── builder/
│       └── STATUS.md
└── .agents/inbox/        <- fallback message inboxes (agent-messaging)
```

## how it runs

1. **u give the lead a goal.** `/agent-orchestrator plan our meetup`
2. **the lead writes one brief per worker** (see [example-worker-brief.md](example-worker-brief.md)) and opens a tab for each one.
3. **each worker starts with** "read X-BRIEF.md in this folder and follow it." it says hi in one line and asks u its first decision.
4. **workers keep their `STATUS.md` current.** the lead rolls them up into `STATE.md`, with anything blocked on u at the top under NEEDS HUMAN.
5. **agents message each other** with the [agent-messaging](../../skills/agent-messaging/) envelope, so u can read every handoff on screen.

## why it works

- **briefs are files**, so a worker can restart, or a new one can pick up, without losing context.
- **decisions go to u one at a time**, multiple choice, with a recommendation. fast to answer from ur phone.
- **hard rules live in every brief**: no pushing, publishing, sending or spending without ur explicit OK, and no secrets.
