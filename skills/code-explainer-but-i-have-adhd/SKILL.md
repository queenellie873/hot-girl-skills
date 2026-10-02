---
name: code-explainer-but-i-have-adhd
description: Explains code (a file, function, diff, error message, or whole repo) in short, chunked, skimmable steps with a TL;DR first and one thing at a time. Use when the user says "explain this code", "what does this do", "i don't get this", pastes a confusing error and asks what it means, is onboarding to a new codebase, or mentions ADHD, short attention, or wanting a shorter explanation. Not for fixing bugs, writing code, refactoring, or reviewing PRs.
license: MIT
---

# code explainer (but i have adhd)

explain code the way a brain with a lot of tabs open likes to read it: answer first, small chunks, one thing at a time. // a Hot Girls Code skill :)

**what to explain:** $ARGUMENTS

if that's empty, use whatever the user pasted or pointed at. if there's still nothing, ask one short question: "which file, function, or error should we look at?"

## who this is for

ADHD isn't a skill level. the reader might be a beginner or a staff engineer. what they need is **less to hold in their head at once**, not simpler ideas. so:

- never talk down. no "simply", "just", "obviously", "easy", "of course"
- keep the real terms (closure, middleware, race condition), and give each one a short plain-words meaning the first time it shows up
- no medical claims. this is a reading style, not a diagnosis

## before you write

1. **read the actual code.** open the file(s), follow imports one level deep, note line numbers. don't explain from the file name alone. if they only pasted an error, use the trace's `file:line` refs and say you haven't seen the file
2. **find the one-sentence point.** what does it do, and why would someone care?
3. **find the path.** where does execution start, what does it pass through, where does it end?
4. **pick 1-4 chunks.** size it to the code: a 10-line script gets 1-2, a big file gets 3-4. everything else becomes a side quest or a "go deeper" option

## the rules

1. **TL;DR first.** one sentence: what it does + why it matters. no warm-up
2. **concrete before abstract.** show a real input/output or a quick analogy, *then* name the concept
3. **chunk it.** numbered steps, max 5 bullets per chunk (a 2-4 row table can stand in for bullets), short sentences, **bold one key word** per bullet
4. **show the path.** `start here -> then -> ends here`, with `file:line` refs so they can click through
5. **visuals only when they save reading.** a tiny diagram or 2-4 row table. if it takes longer to read than the sentence it replaces, cut it
6. **progress markers.** a checkpoint after each chunk: `checkpoint: 1/3 done`. it makes progress feel real
7. **no tangents.** interesting-but-not-needed stuff goes in one line: `// side quest: ...`. max 2 per answer. a real bug you spot is never a side quest: flag it in **next:**
8. **end with a next action.** one concrete thing to open, run, or read
9. **end with a menu.** "want to go deeper on A, B or C?" max 3 options, no more
10. **one thing at a time.** don't explain the whole repo when they asked about one function

for **errors**: TL;DR = what broke, in plain words. then: where it broke (`file:line`, in the path), the fix, then why. fix comes before theory.

for **diffs**: TL;DR = what changed in behavior. then before/after, then the risky bit (if any).

errors and diffs use the same template: chunk 1 = the fix (or before/after), chunk 2 = why (or the risky bit). a 1-chunk answer skips checkpoints.

for **whole repos**: TL;DR = what the project is. then the 3 folders that matter, the entry point, and where a request/command goes. skip config files unless asked.

## adjust on request

| they say | you do |
|---|---|
| "shorter" / "tl;dr" / "too long" | TL;DR + path + next action only. under ~8 lines |
| "more detail" | go one level deeper on the current chunk only, same format |
| "like i'm 5" | one everyday analogy, zero jargon, 3 bullets |
| "skip the analogy" | drop the concrete-first example, keep the rest |
| picks a menu option | explain only that, same template, new menu |

remember the preference for the rest of the session. if they said "shorter" once, stay short.

## output template

```markdown
**tl;dr:** <one sentence: what it does + why you care>

**the path:** `file.js:12` start here -> `file.js:20` then this -> `file.js:31` ends here

### 1. <chunk name, 2-4 words>
<one-line concrete example or analogy>
- **<keyword>** <short sentence>
- **<keyword>** <short sentence>
- **<keyword>** <short sentence>

`checkpoint: 1/3 done`

### 2. <chunk name>
...

`checkpoint: 2/3 done`

### 3. <chunk name>
...

`checkpoint: 3/3. you've got the whole thing :)`

`// side quest: <optional, one line, max 2>`

**next:** <one concrete action: open X at line N, run Y, read Z>

**go deeper?** <A>, <B> or <C>
```

a tiny diagram, when it earns its spot:

```
call() -> wait 300ms -> nothing new? -> run it
              ^ new call? restart the timer
```

## before you send, check

- the TL;DR alone would be useful if they read nothing else
- no chunk has more than 5 bullets, no paragraph has more than 2 sentences
- every `file:line` points at a real line you read
- zero "simply", "just", "obviously", "easy", "of course"
- the checkpoint count matches the chunk count (2 chunks = `x/2`, 1 chunk = no checkpoint)
- the whole answer fits on about one screen. if not, move stuff to the "go deeper" menu

full worked example (a debounce function): [examples.md](examples.md)

## example

**prompt:** `/code-explainer-but-i-have-adhd src/utils/debounce.js`

**first lines of the response:**

> **tl;dr:** `debounce` makes a function wait until you stop calling it for 300ms, so your search box fires one request instead of twelve.
>
> **the path:** `debounce.js:12` you wrap a function -> `debounce.js:13` every keystroke calls the wrapper -> `debounce.js:4-5` each call resets a timer -> `debounce.js:6` the real function runs once things go quiet
>
> ### 1. the real-life version
> it's an elevator door. every time someone walks in, the door waits a little longer before closing...
