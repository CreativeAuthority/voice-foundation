---
name: run-voice-foundation
description: >
  Use this skill when the user says "run the voice foundation", "run my voice foundation", "set
  up my voice foundation", "build my voice foundation", "start my voice foundation", "set up my
  voice", "let's do the interview", or anything close to those. It orchestrates the two guided sessions and the branded PDF, producing
  voice_foundation.md and a portable operating prompt.
---

Run the full Voice Foundation for an agent. This is the setup that teaches their AI how they think, decide, and communicate, so everything it drafts afterward reflects who they actually are rather than the average of every agent on the internet.

It covers three things, not one: the agent's mission, the decision rules that govern what their AI may and may not do on their behalf, and their written and spoken voice. Voice is the smallest part. Mission and rules are what make the voice mean something, which is why they live in the same document.

Run the parts in order, finishing one before starting the next.

## Before you start: the folder

Check for a connected folder before you ask the first question. Everything saves there, and an agent who answers forty questions and then discovers there is nowhere to put the answers has been badly served.

If no folder is connected, stop and say it plainly in two lines: the foundation is a document that lives on their computer, so Claude needs a folder to save it into, and they add one in the Claude desktop app. Offer to pick it up the moment they have.

If more than one folder is connected, ask which one, once. If exactly one is connected, use it and say which one you are using.

Set expectations in two sentences, not a pitch. This is two guided conversations, not a form. You will ask one question at a time and sometimes dig deeper, the second session uses their real emails and some voice-to-text, and it works best if they answer with real specifics instead of polished language.

Tell them the honest time: each session runs thirty to forty-five minutes if they answer properly. They can stop mid-session and pick it up later.

## Step 1 — Mission and decision rules

Run the `run-mission-session` skill in full. It creates `voice_foundation.md` and writes everything through `## When to Stop and Ask`.

Do not move on until the file is written and the agent has read it back. Ask them to change anything that does not sound like them. Their edits are the point.

## Step 2 — Written and spoken voice

Run the `run-voice-session` skill in full. It appends the voice sections to the same file, completing it.

## Step 3 — Build the PDF

Run the `build-voice-pdf` skill. It reads the finished document plus the interview answers and produces the branded PDF: their own answers laid out with mission and voice side by side, and a portable operating prompt they can paste into any AI, inside this system or out.

Build this only after both sessions are complete, so the operating prompt can carry how they think and how they sound together.

## Step 4 — Use it once, now

Do not end on a file. End on the thing working.

Offer, in one line: "Want to see it? Give me an address or a piece you're working on and I'll draft it in your voice." If they say yes, run `write-in-my-voice` immediately.

This matters more than it looks. An agent who watches their own foundation produce a listing description they would actually send understands what they bought. An agent who ends the session with two files and a PDF has to take it on faith.

## Final summary

Tell them plainly what they have and where it lives:

- `voice_foundation.md` in their folder. Their foundation, theirs to edit any time, and the only file this produces.
- The branded PDF, theirs to keep, with an operating prompt that works in any AI tool including ones outside this system.
- "write this in my voice" as the phrase that puts it to work, any time, in any session.

Then invite them to change anything that does not sound like them, and mean it. The foundation gets sharper every time they correct it.
