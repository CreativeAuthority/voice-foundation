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

## Before you start

Do not check for a folder. Do not ask where anything will be saved. Start the interview.

Where the document lands is the last step, not the first, and it is handled in Step 3. An agent who just paid for this should be answering the first question within thirty seconds of asking for it.

Set expectations in two sentences, not a pitch. This is two guided conversations, not a form. You will ask one question at a time and sometimes dig deeper, the second session uses their real emails and some voice-to-text, and it works best if they answer with real specifics instead of polished language.

Tell them the honest time: each session runs thirty to forty-five minutes if they answer properly. They can stop mid-session and pick it up later.

## Step 1 — Mission and decision rules

Run the `run-mission-session` skill in full. It creates `voice_foundation.md` and writes everything through `## When to Stop and Ask`.

Do not move on until the file is written and the agent has read it back. Ask them to change anything that does not sound like them. Their edits are the point.

## Step 2 — Written and spoken voice

Run the `run-voice-session` skill in full. It appends the voice sections to the same file, completing it.

## Step 3 — Put it to work, two ways

The document exists. Now make it usable. There are two ways, they are both complete, and the agent picks. Present them in about four lines total, no preamble, no explaining of mechanisms.

**The file.** If a folder is connected, write `voice_foundation.md` into it and say which folder. From then on "write this in my voice" finds it on its own, in any session, with nothing to remember. If no folder is connected, say that connecting one in the desktop app makes it automatic, and offer to write the file the moment they do.

**The prompt.** Show them their operating prompt, in full, in the chat, ready to copy. Tell them they can paste it into the custom instructions of a Claude project and everything they write in that project comes out in their voice, on their laptop or their phone, with no setup on any computer. The same prompt works in ChatGPT or anything else they use.

Do not rank them and do not call either one a fallback. The file is less to remember. The prompt goes more places. Most agents will end up using both.

If they take the prompt route and later ask for a draft, `write-in-my-voice` will ask them to paste the document once. Say that in one sentence now so it is not a surprise later.

## Step 4 — Build the PDF

Run the `build-voice-pdf` skill. It reads the finished document plus the interview answers and produces the branded PDF: their own answers laid out with mission and voice side by side, and a portable operating prompt they can paste into any AI, inside this system or out.

Build this only after both sessions are complete, so the operating prompt can carry how they think and how they sound together.

## Step 5 — Use it once, now

Do not end on a file. End on the thing working.

Offer, in one line: "Want to see it? Give me an address or a piece you're working on and I'll draft it in your voice." If they say yes, run `write-in-my-voice` immediately.

This matters more than it looks. An agent who watches their own foundation produce a listing description they would actually send understands what they bought. An agent who ends the session with two files and a PDF has to take it on faith.

## Final summary

Tell them plainly what they have and where it lives:

- `voice_foundation.md`, their foundation. Theirs to edit any time, and the only file this produces.
- The branded PDF, theirs to keep, with an operating prompt that works in any AI tool including ones outside this system.
- "write this in my voice" as the phrase that puts it to work, any time, in any session.

Then invite them to change anything that does not sound like them, and mean it. The foundation gets sharper every time they correct it.
