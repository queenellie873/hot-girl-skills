---
name: ask-for-help
description: Writes or rewrites a message that asks someone for their time (feedback on a design or file, a code or doc review, an intro, advice, a meeting) so it's direct, specific, and short. Use when the user says "help me ask X for feedback", "rewrite this ask", "how do i ask for a review/intro", pastes a draft DM or email asking for help, or wants to follow up on an ask that got no reply. Not for writing the work itself or replying to someone else's request. Based on Josh Puckett's "How to Ask for Help".
license: MIT
---

# ask for help

turn "thoughts?" into a message people can actually answer. // a Hot Girls Code skill :)

**the draft or situation:** $ARGUMENTS

if that's empty, use whatever the user pasted. if there's still nothing, ask one short question: "who are you asking, and what do you want from them?"

credit: the five principles come from Josh Puckett's post ["How to Ask for Help"](https://x.com/joshpuckett/status/2104249162556748029). this skill puts them into steps an agent can follow.

## why this matters

the people being asked are busy. in a few seconds they should know what you want, what to look at, and what a useful answer looks like. if they have to work that out, they put it off or never reply.

## the five principles

1. **be direct.** put the ask up front. status updates, apologies and backstory go after it or get cut
2. **be specific.** name exactly what you want. "thoughts?" or "lmk what u think" gets no reply or a vague one. ask the real question, and number them if there's more than one. say what to look at (which screen, section, flow, PR) and who it's for (the user, the audience, the bar it has to clear)
3. **be concise.** cut anything the reader doesn't need to act. one short paragraph of context, max
4. **follow up.** no reply usually means they missed it or forgot. a polite nudge is fine and often welcome. if the message promises a follow-up, say when
5. **follow through.** after someone helps, tell them what you did with it. this happens after the message goes out, so remind the user

## rewrite steps

1. **find the actual ask.** if the draft doesn't have a clear one, work out what the user wants and write it down in one sentence
2. **move it to the top**, or right after a one-line greeting or context line
3. **make it specific:**
   - what exactly should they look at?
   - what question should they answer? turn vague asks into 1-3 concrete questions
   - what form should the answer take? (yes/no, flag + suggested fix, a 30-min call)
   - by when? if the user didn't give a deadline, leave a `[deadline]` placeholder and point it out
4. **make yes easy.** link the file, say how long it'll take them, and be flexible on timing for meetings
5. **cut filler.** over-apologizing ("sorry to bother u!!"), hedging, and anything that doesn't help them act
6. **keep logistics to one line at the end** ("more coming friday", "i'll ping u monday")

match the user's voice and the channel. a slack DM can be lowercase and casual; an email to a stranger probably shouldn't be. don't add formality they didn't ask for.

## follow-ups

if the user is nudging an ask that got no reply: keep it to 1-2 lines, restate the ask (don't just say "bumping this"), and give an easy out ("totally fine if now's not a good time").

## examples

- before: "hey! made some changes to the onboarding flow, would love ur thoughts whenever"
  after: "could u look at the new onboarding flow (link) by thursday? two questions: 1) does step 3 make sense without the tooltip, and 2) would u drop off anywhere? quick gut reactions are perfect, 10 min tops"
- before: "so sorry to bother u, i know ur super busy, but i was wondering if maybe u'd be open to chatting sometime about how u got into dev rel?"
  after: "i'm moving from support into dev rel and would love 20 min of ur advice on how u made the switch. any time next week works for me, i'll work around ur calendar"

## check before u deliver

- can the reader tell what u want from the first sentence or two?
- is there a concrete question they could answer without asking one back?
- is it clear what to look at and what a useful answer looks like?
- is there a deadline or timing signal (or a placeholder for one)?
- is anything left that they don't need?

deliver the rewritten message first. then add a short note: the main changes, any placeholders to fill in, and a reminder to follow through once they reply.
