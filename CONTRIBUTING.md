# contributing

thank u for being here :) adding a skill takes about 5 minutes.

## the rules

- **one skill per PR.** one folder: `skills/<skill-name>/SKILL.md`, plus optional supporting files.
- **name it right.** folder name = the `name:` line. lowercase letters, numbers and dashes, max 64 characters.
- **write a real description.** it's how the agent decides when to use ur skill, so say *what* it does and *when* to use it. max 1024 characters.
- **test it.** run it with an agent at least one time before u open the PR.
- **show a before and after (if it applies).** paste what the agent did without ur skill, then with it. a short snippet is plenty. this is the fastest way to get approved.
- **say which agent(s) u tested with** in the PR (Claude Code, Codex, Cursor, etc.).
- **include an example of when it triggers**: a prompt that should make the agent reach for ur skill.
- **nothing private.** no API keys, tokens, passwords, emails, addresses, private URLs or other people's names.
- **only share what's yours to share.** if u adapted someone else's skill, credit them and make sure their license allows it.
- **no skills built for weapons, military or surveillance tech.** we'll close those PRs.

## the format

```markdown
---
name: your-skill-name
description: what it does and when to use it.
---

# your skill name

instructions for the agent: steps, rules, examples.
```

that's the minimum. optional extras that work in Claude Code (from the [official skills docs](https://code.claude.com/docs/en/skills)):

- supporting files next to `SKILL.md` (`reference.md`, `examples.md`, `scripts/helper.py`). link them from `SKILL.md` so the agent knows they exist.
- `$ARGUMENTS` in the body gets replaced with whatever the user types after `/your-skill-name`.
- heads up: `$` followed by a digit (`$1`, `$300`) also gets replaced, by an argument. write `\$300` or "300 dollars". the skill check catches this.
- keep `SKILL.md` under 500 lines. move long reference stuff into other files.
- for skills that also work outside Claude Code (claude.ai, the API), stick to these frontmatter fields: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.

there's a blank template in [`templates/SKILL.md`](templates/SKILL.md).

## how to open a PR

```bash
# fork on GitHub first, then:
git clone https://github.com/<you>/hot-girl-skills.git
cd hot-girl-skills
git checkout -b add-my-skill
mkdir -p skills/my-skill && cp templates/SKILL.md skills/my-skill/SKILL.md
# write ur skill, test it (cp -r skills/my-skill ~/.claude/skills/), then:
python3 scripts/check_skills.py
git add skills/my-skill && git commit -m "add my-skill"
git push -u origin add-my-skill
```

then open a pull request and fill in the checklist.

## how review works

skills are instructions agents will follow, sometimes with real permissions on someone's machine. so a human reads every PR before it's merged. for now, [@queenellie873](https://github.com/queenellie873) reviews and merges every PR.

**fast lane: text-only skills.** just a `SKILL.md` (and maybe other markdown). these can get merged the same day, even live at an event.

**closer look: anything that runs code.** scripts, `!` shell commands in the skill, `allowed-tools`, or hooks. reviewers check for:

- network calls (`curl`, `fetch`, `requests`, webhooks): where is data going?
- deleting or overwriting files (`rm`, `git reset --hard`, `--force`)
- reading credentials (`.env`, `~/.ssh`, `~/.aws`, keychains, tokens, browser data)
- `allowed-tools` that pre-approve risky commands
- obfuscated code (base64 blobs, minified scripts, downloads that get executed)

**hidden instructions.** reviewers also read the text for prompt injection: lines telling the agent to ignore the user, skip asking for permission, send data somewhere, or do something unrelated to the skill. that includes HTML comments, zero-width characters and text inside "examples".

PRs that do any of this on purpose get closed. honest mistakes get a friendly comment.

## code of conduct

be kind, be generous with credit, assume good intent. we're here to build and have fun. harassment of any kind isn't welcome, and maintainers can remove content or people that make this space worse.
