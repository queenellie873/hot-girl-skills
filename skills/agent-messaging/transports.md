# Transports

Details for each transport in [SKILL.md](SKILL.md). Try them in order; use the
first that reaches the recipient. Whatever you use, log the
send (SKILL.md section 3).

In the commands below, `<ref>` is the recipient's surface and `<target>` is
its tmux pane. Never copy a ref from an example: look it up.

## a. SendMessage (default)

Use this whenever the recipient is a Claude Code session on this machine or a
subagent. It works across separate sessions, not just subagents, and nobody
types into anyone's terminal.

1. Run `ListAgents`. The first line is **your own address** ("This session is
   <address>"). Every row below starts with another session's address, plus
   whether it is busy or idle.
2. Call SendMessage with that address as `to` and the one-line wire form as
   `message`. Add ` [ref]` after the name only if `ListAgents` shows two rows
   with the same name.
3. The message arrives in the recipient's session on its own, wrapped as
   `<cross-session-message from="<address>">`. To reply, send to that `from`.

```
SendMessage(to: "<worker address>", message: "[from: lead -> to: builder] [type: task] [id: lead-4] [re: -] Build the form from docs/form-spec.md. || reply: type done to lead via SendMessage")
```

Good to know:

- **Give workers your address.** A worker started from a brief has never
  received a message from you, so put your address in its brief or kickoff.
  After that, it replies to the `from` of whatever you send.
- **Waiting without polling.** Send with `notify_when_idle: true` (main
  conversation only, sessions on this machine) to get one notice when the
  recipient next goes idle or exits. You can send it with no `message` to
  subscribe without interrupting. Never loop on `ListAgents` or send "are you
  done?".
- **Delivered is not read.** A session in a different permission mode may hold
  your message for its human's approval, or let it expire. Never treat
  silence as agreement.
- **`@` paths don't attach anything.** Send the text itself.
- If SendMessage or ListAgents is listed as a deferred tool, load it first
  (for example with ToolSearch).

## b. File inbox (when SendMessage can't reach them)

Each agent has one inbox file in the shared project folder:

```
.agents/inbox/<agent>.md
```

Create `.agents/inbox/` if it does not exist. To send, append one entry, never
overwrite:

```
- 2026-10-01 14:05 [from: designer -> to: lead] [type: question] [id: designer-2] [re: lead-3] Should the headlines mention the date or stay evergreen? || reply: answer "date" or "evergreen" with re: designer-2
```

Rules:

- One entry per line, one-line wire form, always append. Nobody edits or
  deletes lines in an inbox, not even its owner: rewriting the file while
  someone else appends can lose a message.
- The recipient reads its inbox at the start of each turn. An idle recipient
  only gets there on its next turn, so tell the human if it is waiting.
- To mark an entry handled, the recipient logs `handled <id>` in its own
  `STATUS.md` (or `STATE.md`) log. Unhandled = ids in the inbox with no
  `handled` line in your log. Match the whole id: `handled lead-1` does not
  cover `lead-10`.

Append from a shell with a quoted heredoc, so apostrophes, quotes and `$` in
the message are safe:

```sh
mkdir -p .agents/inbox
cat >> .agents/inbox/lead.md <<'EOF'
- 2026-10-01 14:05 [from: designer -> to: lead] [type: question] [id: designer-2] [re: lead-3] Don't know the date yet: date or evergreen? || reply: answer with re: designer-2
EOF
```

## c. cmux (backup only)

Typing into a terminal interrupts whoever is typing in that tab, including
the human, and can land in the middle of their message. Grey suggestion text
also looks like typed input on screen. Use cmux or tmux to send only when
SendMessage and the file inbox can't reach the recipient. cmux is still the
right tool for opening, naming and reading tabs.


cmux is a terminal multiplexer for agents. A window holds workspaces, a
workspace holds panes, and a pane holds surfaces (terminal or browser tabs).
Each agent usually runs in its own terminal surface. Targets can be short refs
such as `surface:<n>`, UUIDs, or indexes.

Commands below were checked against `cmux --help` and the per-command `--help`
output. If your version differs, run `cmux guide` and `cmux <command> --help`
before using them.

### Check that cmux is available

```sh
cmux ping                 # succeeds when the cmux app is reachable
cmux identify --json      # your own window / workspace / surface
```

### Find the recipient

```sh
cmux tree                 # all panes and surfaces in the current window, with tab titles
cmux tree --all           # every window
cmux list-pane-surfaces --workspace <workspace> --pane <pane>
```

`cmux tree` marks your own surface with `here`. Match the recipient by its tab
title. It helps if each agent's tab is titled with its agent name; the
orchestrator can set that when it creates the tab
(`cmux rename-tab --surface <ref> "<agent name>"`). If the recipient is in
another workspace, pass `--workspace <workspace>` along with `--surface` on
every command below, and `--window <window>` if it is in another window
(refs are resolved within a window). If you cannot tell which surface belongs to the
recipient, do not guess: use the file inbox.

### Read the screen before sending

```sh
cmux read-screen --surface <ref> --lines 30
```

Only send if the recipient is idle at an empty input prompt. Do not send if
the screen shows:

- the agent still working (for example "esc to interrupt" or a spinner): it
  can raise a permission prompt at any moment,
- a permission or confirmation prompt (for example "Do you want to proceed?",
  numbered Yes/No options, or "Allow" choices),
- a selection menu or dialog,
- text already typed into the input,
- a running command that is reading from the terminal.

Typed text goes straight into whatever has focus in that terminal, so sending
during a prompt can answer it on the agent's behalf. In those cases, use the
file inbox, or wait and read the screen again.

### Send

```sh
cmux send --surface <ref> "[from: lead -> to: builder] [type: task] [id: lead-4] [re: -] Build the form from docs/form-spec.md. || reply: type done to lead"
cmux read-screen --surface <ref> --lines 10
cmux send-key --surface <ref> enter
```

- `cmux send` types text into the terminal surface. It does not press Enter
  unless the text contains `\n` or `\r`; `\t` sends Tab.
- Read the screen again between typing and Enter. Press `enter` only if your
  exact text is sitting in the input box and nothing else (no prompt or menu)
  appeared. If anything changed, do not press Enter: log the send as FAILED,
  use the file inbox, and tell the human there may be stray text in that tab.
- Press Enter once. Never send a second `enter` to "make sure": if a prompt
  appeared in the meantime, the extra Enter would accept its default.
- Use the one-line wire form, starting with `[from:`. Never put `\n`, `\r`, or
  `\t` inside the message, and avoid real newlines: each one would submit a
  partial message.
- Quote the message for the shell. Avoid backticks and `$` inside double
  quotes, or use single quotes.

### Confirm delivery

```sh
cmux read-screen --surface <ref> --lines 10
```

Check that your message appears as submitted input. If it is missing, log the
send as FAILED and use the file inbox. Do not retype or press Enter again.

Always pass `--surface` explicitly. Without it, cmux targets
`$CMUX_SURFACE_ID`, which is your own terminal.

## d. tmux (backup only)

Same warning as cmux: typing into a pane interrupts whoever is using it.

Use when you are inside tmux (`$TMUX` is set) and the recipient runs in a tmux
pane.

```sh
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index} #{pane_title} #{pane_current_command}'
tmux capture-pane -p -t <target> | tail -n 30      # read the screen first
tmux send-keys -t <target> -l "<one-line message>"  # -l types the text literally
tmux capture-pane -p -t <target> | tail -n 5       # check it is in the input box
tmux send-keys -t <target> Enter
```

`<target>` is `session:window.pane`, e.g. `agents:0.2`. Name each agent's pane
when you create it so it can be found by title:
`tmux select-pane -t <target> -T "<agent name>"`. The same screen-check and
single-Enter rules as cmux apply. Use the one-line wire form.
