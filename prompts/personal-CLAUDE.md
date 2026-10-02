<!--
  a starter ~/.claude/CLAUDE.md from Hot Girls Code. copy it, then make it urs.
  - this file loads into every Claude Code session on ur machine.
  - html comments like this one are stripped before Claude reads the file, so leave urself notes here.
  - keep it short (under ~200 lines) and concrete: "run pnpm test" beats "test ur changes".
  - the stack section is a filled-in example. swap in ur own.
-->

# working with me

## communication
- Keep replies short. Lead with the answer or result, then the reason.
- When you need a decision from me, ask one question at a time. Give 2-4 options and mark the one you recommend.
- If something is unclear and you can check it yourself in under a minute (read a file, run a command), check it instead of asking.

## ask before you act
- Ask me before any action that is hard to undo or visible to other people: `git push`, deploying, deleting files or branches, sending messages or emails, opening PRs or issues, or making anything public.
- Never put secrets (API keys, tokens, passwords, `.env` values) in code, commits, logs, or messages. If you find one, stop and tell me.
- Stay in scope. If you notice something else worth fixing, list it at the end of your reply instead of changing it.

## before you say "done"
- Prove it works where it runs: run the tests, the command, or open the page. Reading the code is not proof.
- If anything failed or you skipped a step, say so plainly in your final message, with the error output.

## my stack
<!-- example values: replace with yours -->
- Language: TypeScript, strict mode. Framework: Next.js (App Router).
- Package manager: pnpm. Never use npm or yarn in this setup.
- Install: `pnpm install`
- Dev server: `pnpm dev` (http://localhost:3000)
- Tests: `pnpm test`. Run them before you say a change is done.
- Lint and types: `pnpm lint && pnpm typecheck`

## code style
- Match the style of the file you are editing: naming, comment density, and patterns.
- Prefer small, focused changes. Don't refactor unrelated code.
