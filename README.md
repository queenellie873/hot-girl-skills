# hot girl skills

```
> hot girl skills_
```

open source skills for ur agents, made by the **Hot Girls Code** community.

// steal them, remix them, add urs :)

## what is this

a hot girl is someone who is authentically themselves.

**Hot Girls Code** started as clothing and grew into a community of engineers who break the mold and build dope tech that feels intentional. this is where we trade the skills behind our agents. ([hotgirlsco.de](https://hotgirlsco.de) · IG [@hotgirlsco.de](https://instagram.com/hotgirlsco.de))

// we build for people, not for war.

intentional means no defense tech. no weapons, no military, no surveillance. it means considering who tech often leaves out, and building for them. it means creating technology that actually helps people.

a **skill** is a small instruction file that teaches an AI agent how to do one thing well. it lives in a folder with a `SKILL.md` in it. the top of the file says what the skill does and when to use it, and the rest is the instructions. **Claude Code** reads the description, and when ur request matches, it loads the skill and follows it. u can also run a skill yourself with `/skill-name`.

new to Claude Code? start with the [Claude Code onboarding guide](https://claude.ai/code/artifact/3f8ffc6c-59bd-48e5-8350-b4539dabfc9d).

## the skills

| skill | what it does |
|---|---|
| [agent-orchestrator](skills/agent-orchestrator/) | turns one agent into the lead of a small agent team: writes a brief for each worker, keeps a `STATE.md` state log, checks in, and asks u before anything risky |
| [agent-messaging](skills/agent-messaging/) | a simple protocol for agents to message each other with SendMessage (no typing into each other's tabs), so handoffs stay readable and safe |
| [code-explainer-but-i-have-adhd](skills/code-explainer-but-i-have-adhd/) | explains code in small chunks: tl;dr first, one thing at a time, and a clear next step |

more in [`prompts/`](prompts/) (example `CLAUDE.md` files) and [`teams/`](teams/) (agent team setups).

## install a skill

pick a skill folder and copy it into one of these:

- `~/.claude/skills/` to use it in every project on ur machine
- `.claude/skills/` inside a project to use it (and share it) in just that repo

```bash
git clone https://github.com/queenellie873/hot-girl-skills.git
cp -r hot-girl-skills/skills/code-explainer-but-i-have-adhd ~/.claude/skills/
```

then open Claude Code and ask for something the skill covers, or type `/code-explainer-but-i-have-adhd`. that's it.

// want all of them? `cp -r hot-girl-skills/skills/* ~/.claude/skills/`

## add your skill

fork, add `skills/<your-skill-name>/SKILL.md`, open a PR. there's a blank template in [`templates/SKILL.md`](templates/SKILL.md), and the full steps (plus what reviewers look for) are in [CONTRIBUTING.md](CONTRIBUTING.md).

## safety

skills are instructions an agent will actually follow, so every PR gets read by a human before it's merged. text-only skills are the fast lane. skills with scripts get a closer look (network calls, deleting files, reading credentials, hidden instructions). always read a skill before u install it, from here or anywhere.

## contributors

every skill author gets a spot here. thank u for making the agents smarter and hotter.

<a href="https://github.com/queenellie873/hot-girl-skills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=queenellie873/hot-girl-skills" alt="contributors" />
</a>

- [@queenellie873](https://github.com/queenellie873): agent-orchestrator, agent-messaging, code-explainer-but-i-have-adhd

## license

[MIT](LICENSE)

be bold, be you, be sexy.
