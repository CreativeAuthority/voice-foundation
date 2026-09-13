---
name: start-here
description: >
  The front door. Use this whenever the user opens Voice Foundation without naming an action, or
  says anything like "help", "hi", "what can you do", "what now", "where do I start", "I'm new",
  "what's next", or "menu". Also use it when they describe what they want in their own words but
  do not know the command. When in doubt, start here.
---

Get the agent to the right next step in one short exchange. Never present a menu of everything. Look at what exists, then say the one thing that comes next.

## First, look

Check the agent's connected folder for `voice_foundation.md`.

If no folder is connected, that is the only problem worth solving right now. Tell them their foundation is a document that lives on their own computer, so Claude needs a folder to save it into, and they add one in the Claude desktop app. Then stop. Do not start the interview.

## If the foundation does not exist yet

They have just bought this and installed it. Say what it is and what happens next, in about four lines, in plain language. No feature list.

Something close to: this is two guided conversations that teach your AI how you think, decide, and sound. When it is done you will have your foundation document, a branded PDF with a prompt you can paste into any AI, and the ability to say "write in my voice" and get something you would actually send. Each conversation runs thirty to forty-five minutes and you can stop and come back.

Then ask one question: ready to start now, or want to know more first?

If ready, run `run-voice-foundation`.

## If the foundation exists and is complete

Do not re-explain the product. Ask what they are working on, and route:

- Anything a client or the public will read, a listing description, a caption, an email, a post: run `write-in-my-voice`.
- They want to change how they sound: open `voice_foundation.md`, make the edit they describe in the right section, and read the changed lines back to them.
- They want the PDF again, or a fresh one after edits: run `build-voice-pdf`.
- Their business changed, new market, new lane, new focus: offer to re-run the mission session only, keeping the voice sections.

## If the foundation exists but is half built

Session 1 ran and Session 2 did not, or the file is missing `### Failure signature`. Say where they stopped and offer to pick it up. Do not restart from the beginning and do not re-ask what they already answered.

## If they ask what else this does

Answer honestly and briefly. This builds the foundation and drafts in their voice. The full Creative Authority System is where the rest lives: the morning briefing, the sphere and referral engine, buyer and seller workflows. Mention it once, only when asked, and do not pitch it. Their foundation carries over to it unchanged.

## Tone

They are a working agent, not a user. Short sentences, no exclamation points, no enthusiasm about the software. Answer, route, get out of the way.
