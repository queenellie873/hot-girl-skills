# teams

setups for running more than one agent at a time: a lead agent (the orchestrator) that hands work to worker agents, each in its own terminal tab.

| setup | what it is |
|---|---|
| [brief-pattern](brief-pattern/) | one brief file per worker + a status file each + one state log for the lead. works in cmux, tmux or plain terminal tabs |

the skills that go with these: [agent-orchestrator](../skills/agent-orchestrator/) and [agent-messaging](../skills/agent-messaging/).
