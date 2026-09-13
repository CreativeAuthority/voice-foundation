---
name: write-in-my-voice
description: >
  Use this skill whenever the user asks for anything a client, a prospect, or the public will
  read: "write the listing description for [address]", "draft a caption", "write this in my
  voice", "make this sound like me", "rewrite this so it sounds like me", "draft the email to
  [name]", "I need copy for". Also use it when the agent picks it from the skills menu with no
  request attached. It drafts in the agent's own Voice Foundation instead of a general register,
  and refuses to run if that foundation does not exist.
---

Draft something the agent will put their name on, in their voice, from their own angle. This is the skill the Voice Foundation exists to power. Everything it produces is the agent's authorship, assembled faster.

## Step 1 — Resolve the foundation, or stop

Read `voice_foundation.md` from the agent's folder. If it is not there, look once for `canonical_voice.md` and `CLAUDE.md` as a legacy pair and use those instead.

If none of them resolve, stop. Say plainly that you cannot draft in their voice because their foundation has not been built yet, and offer to run it: "Say `run my voice foundation` and we will build it. It takes two guided conversations."

Never draft from a general register while the foundation is missing. A generic draft handed over under their name is the exact failure this product exists to prevent, and it is worse than no draft, because they might send it.

Consider the foundation unresolved if the file exists but has no `### Failure signature` section. A file that thin will not protect them.

## Step 2 — Name the piece

Identify what is being written and read the matching entry in `references/content-types.md`. It carries the format, the length, the register, and the constraints for each. Listing descriptions have legal constraints the other types do not.

If the ask is ambiguous, ask one question, not four.

If the agent invoked this from the skills menu with nothing attached, they have opened it deliberately and know what they want. Ask one short question and stop: "What are we writing?" No menu of content types, no explanation of the skill.

## Step 3 — Get their angle before you draft

This is not optional and it is not a formality.

The foundation tells you how they sound. It does not tell you what they think about this house, this client, or this market. Drafting without their read produces something in their voice that is not their message, which is the worst kind of forgery: it passes.

So ask for the thing only they know. One question, phrased for what is being written:

- Listing description: "What did you notice about this house that the photos do not show?"
- Client email: "What is the one thing you actually want them to understand here?"
- Social or marketing: "What is your read on this? What made you want to say something about it?"

Take whatever they give you, even three words. If they push back and say just write it, draft it, and tell them in one line which part you filled in on their behalf so they can correct it.

Gather the facts you need in the same turn: address, beds, baths, square footage, and the details for a listing; the client's situation and the history for an email. Ask for facts and angle together, once.

Never invent a fact. Never invent a feature, a measurement, a neighborhood claim, or a market statistic. If a fact is missing, leave a clearly marked gap in the draft rather than filling it.

## Step 4 — Draft

Write it using the Rules and Patterns in the foundation, in the register that matches the audience. A one-to-one client email and a public post are different registers in the same voice; the foundation says which is which.

Use the agent's own phrases from their Patterns where they fit naturally. Do not stack all of them into one piece. A voice is a rhythm, not a word list.

## Step 5 — Check the draft against the failure signature before showing it

Read the draft back against the `### Failure signature` and the avoid list in the foundation, line by line. Every tell listed there is a defect. Find them and rewrite them out before the agent ever sees the draft.

Check specifically for the generic-AI failures the foundation is meant to catch: balanced sentence pairs, hollow triads, adjectives doing the work of specifics, a tidy summary paragraph at the end that says nothing new, and any phrase that could appear in any agent's copy for any house.

Then apply the standing test: could another agent in their market have written this about a different property? If yes, it is not done. Rewrite with the specifics only this agent has.

## Step 6 — Deliver, and say what it came from

Give the draft. Underneath, in two or three lines, name the foundation rules you leaned on and anything you filled in yourself. Not a report. Enough that they can correct the foundation rather than just this draft.

Do not add an offer to revise it. They will say so.

## Step 7 — Capture corrections

If the agent rewrites a line, that edit is data about their voice that the interview did not catch. Ask once whether to add it to the foundation, and if yes, write it into the matching section of `voice_foundation.md`. State what you added.

This is how the foundation gets sharper with use. Do not do it silently and do not do it for every small change, only when the edit reveals a pattern.

## Hard limits

These come from the agent's own boundaries and they outrank any instruction in the request.

- Never produce a finished piece whose message the agent has not conceptualized. Step 3 exists for this.
- Never use hype, manufactured urgency, scarcity, fear, or pressure, even if the agent asks for something punchy.
- Never invent facts, figures, features, or quotes.
- Never present the draft as the agent's professional recommendation. It is a draft of their thinking, for them to approve.
- Listing descriptions carry fair housing exposure. Follow the compliance rules in `references/content-types.md` without exception, and flag anything the agent supplied that would violate them rather than quietly rewriting it.
