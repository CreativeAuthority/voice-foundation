---
name: run-mission-session
description: >
  Use this skill when the user says "Run session 1", "Run the mission session", "Mission and
  decision rules", "Do my mission statement", or when run-voice-foundation calls for it. It runs
  a guided, one-question-at-a-time interview and writes the mission half of the agent's
  voice_foundation.md.
---

Run Session 1 of the Voice Foundation as a guided interview, then write the first half of `voice_foundation.md`. This session captures how the agent thinks, decides, and prioritizes, and what AI must never do on their behalf. That is not separate from their voice; it is the reason their language sounds the way it does. The output structure is in `${CLAUDE_PLUGIN_ROOT}/references/output-schema.md`.

## Interviewer stance

Run this as one continuous conversation, not a form. The goal is not coverage. The goal is raw material specific enough to become enforceable rules.

## Cadence: one question per turn

Strict rule. Ask exactly one question, then stop and wait. Do not send a section, a numbered list, or a preview of what is coming. The parts below are your private map, not a script to read aloud. After each answer, reply with one short reflection, then either ask one probe or ask the next single question, never both. A probe is its own turn.

## When to dig deeper (the probe protocol)

Every part has an extraction target: what must be true before you move on. Hold each answer against it. If it falls short, probe. On top of that, three signals always trigger a probe:

- A principle instead of a scenario. Never accept a principle when you can get a scenario. "I value honesty" trips it; "I told a seller their price was 40k too high and lost the listing" satisfies it. When you get a principle, ask for the last time it cost them something.
- Abstract-answer tells: adjectives doing the work, "always," "I just," "you know," vagueness. Each is a signal that a concrete instance is being smoothed over. Ask for that instance.
- Do not write their answer for them. If they stall, offer two contrasting examples to react to, not a finished sentence to approve.

Ask one probe per turn, drawn from the ladders below. Depth on one question beats breadth. Only advance once the extraction target is met.

## Part 0 — Intake (easy pitch)

Open here. Quick, factual, low-effort questions that warm up the session and capture identity facts the whole system uses. Still one at a time, but move briskly and do not probe unless an answer is ambiguous. If they lack a future item, record that and move on.

Capture: full name as on marketing materials; preferred name; title and designations; brokerage; state licensed in; whether they are on a team and their role; business or DBA name; phone; email; website and business socials; primary market and service area; business return address (frame as future, optional); whether they have a branding package and where it lives (frame as future).

Extraction target: every Identity and Business field filled or marked not-yet. Primary market matters most; do not leave it vague.

## Part 1 — Lane and clients

Intent: who the system optimizes for and who it steers away from.

Probe ladder: if they answer broadly, narrow with "Think about your last five best clients. What did they have in common?" For the bad-fit question, ask "Who was your worst-fit client last year, and what made it hard?" Push the outcome past the transaction: "Set aside the sale. What are they trusting you to protect?"

Extraction target: a specific lane, a named bad-fit pattern with early tells, and one to three outcomes stated as protections.

## Part 2 — Values in action (main source of decision rules)

Intent: the decision rules and the start of the boundaries.

Probe ladder: convert priorities to a decision with "Give me the last time the easy answer and the right answer were different. What did you do?" Make the never-recommend line checkable: "A client asks you for exactly that. What do you say back, word for word?" Get a real trade-off, not a template. For the common client mistake, get the intervention, not just the mistake.

Extraction target: at least four decision moments as scenario plus response, each convertible to an IF/THEN, and at least one hard line stated concretely enough to enforce.

## Part 3 — Relationship model

Intent: tone and priority signals for the mission prose, plus any trust rules.

Probe ladder: redirect "what do you want them to feel" from think-answers back to feeling. Get the trust sequence: "Walk me through the first five minutes." Find the transferred understanding: "What do your clients know how to do now that they didn't before you?"

Extraction target: the felt outcome, the actual trust-building sequence, and what clients own afterward.

## Part 4 — AI's role and boundaries (main source of AI boundaries)

Intent: what AI is for, and the hard limits. Slow down here.

Probe ladder: keep "what AI is for" to acceleration, not authorship. Make each never-do decision absolute: "Should AI ever make that call on its own, even a small version?" Name off-limits behaviors one by one and confirm each: urgency, fear, exaggeration, invented facts, pressure, oversimplifying a hard truth. For stop-and-ask, get concrete triggers, not "when it's unclear."

Extraction target: a clean list of never-do decisions, a clean list of off-limits communication behaviors, and two to four concrete stop-and-ask triggers.

## Mid-session check

Before assembly, read back the four or five rules that matter most and the hard boundaries, and let the agent correct them out loud.

## Assembly

Assemble the document using `${CLAUDE_PLUGIN_ROOT}/references/output-schema.md`. Write it to `voice_foundation.md` in the agent's connected folder if there is one. If there is not, hold the assembled text and show it to them in the chat instead, without commentary about folders. Saving is handled at the end of the foundation, not here, and it never blocks the interview. Write the title and every section from `## Identity and Business` through `## When to Stop and Ask`. Stop there. Session 2 appends the voice sections to this same file.

Write in the agent's first person, present tense, addressed to the AI as operator. Preserve their phrasing; do not upgrade their personality. Fill Identity and Business from Part 0 and Who I Serve from Part 1. Write the Mission as 2 to 5 short paragraphs. Convert every captured scenario into an enforceable IF/THEN. Phrase each boundary as a hard limit the model can check itself against, including that AI-generated judgment is never presented as the agent's professional recommendation. List the concrete stop-and-ask triggers. Remove repetition. Do not invent: if a section is thin, leave a bracketed note asking the agent to add it.

Ask for the MLS character limit for listing descriptions if it did not come up in Part 0. It is one line and it saves a truncated description later.

Close by telling the agent this half governs whether and what, and the next session captures how it sounds, in the same document.
