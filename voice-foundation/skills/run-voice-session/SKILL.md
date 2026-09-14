---
name: run-voice-session
description: >
  Use this skill when the user says "Run session 2", "Run the voice session", "Canonical voice",
  "Do my voice reference", or when run-voice-foundation calls for it. It runs a guided,
  one-question-at-a-time interview across a written and a spoken track and appends the voice
  sections to voice_foundation.md, completing it. Assumes Session 1 already wrote that file.
---

Run Session 2 of the Voice Foundation as a guided interview, then append the voice sections to `voice_foundation.md`. This session captures how the agent sounds in writing and out loud. It assumes Session 1 already wrote the mission half of that file, and it does not re-elicit or repeat decision logic. Output structure is in `${CLAUDE_PLUGIN_ROOT}/references/output-schema.md`.

If the mission half does not exist yet, either as a file or earlier in this conversation, run `run-mission-session` first. The voice sections are read together with the mission, and on their own they produce mimicry.

## Interviewer stance

Voice cannot be captured by asking someone to describe their voice. It is captured by collecting real samples and reading the patterns back for confirmation. Weight this session toward evidence over self-report.

## Cadence: one question per turn

Strict rule. One question, one turn, then wait. The parts are your private map, not a script. Name the mode when you ask, and never ask the written and spoken versions of a part in the same turn. After each answer, one short reflection, then one probe or the next single question, never both. Reading a pattern back for confirmation is its own turn.

## When to dig deeper (the probe protocol)

Each part has an extraction target. Hold every answer against it and probe when it falls short. Two signals always trigger a probe here:

- Self-report instead of evidence. If they describe their voice rather than show it, or offer an example they wrote on the spot, redirect to something real they already made. Invented samples corrupt the anchor.
- Abstract or generic answers. Push for the real phrase, the real email, the real line, in their exact words.

Extract patterns from the samples yourself, then read them back for confirmation ("In these three emails you open with the bottom line and never hedge. Is that you, or just these three?"). Confirmed patterns beat claimed ones. Route any answer that is really a decision rule back to the Decision Rules section Session 1 wrote; do not duplicate it in the voice sections.

## Spoken answers must be dictated, not typed

Every question on the spoken track must be answered by voice-to-text, not keyboard. This is the highest-leverage capture rule in the session. A typed spoken answer is not a spoken answer; the moment they type, they compose written prose and the real cadence is gone. Prompt dictation every time you reach a spoken question ("tap the mic and say it the way you'd say it to a client, don't clean it up"). Written questions stay typed. Treat transcription disfluencies as signal; do not tidy them.

## The parts

Ask written and spoken separately in every part. Pull the agent's real emails and a recent conversation before the language and anchor parts; where you have folder access, offer to source samples for them.

- Part 1, Audience and intent. Written and spoken: the specific audience, the feeling to leave, the next action or emotional outcome.
- Part 2, Authority posture. What they lead with and refuse to write; how they open trust and handle pushback, with a real example and the moves they would never use.
- Part 3, Explanation style. A real pasted written trade-off; a spoken trade-off as dialogue; two to three real objection responses in their words.
- Part 4, Language patterns. Real use list, real avoid list, rhythm, and the failure signature (their specific AI tells) for each channel. Get the failure signature concretely: "Show me a sentence that sounds like AI wrote it, not you. What's wrong with it?"
- Part 5, Voice permissions. What AI may do with their voice and what it must never do, scoped to writing and speaking only. What to do when unsure it sounds like them.
- Part 6, Anchors. One real written anchor and one real spoken anchor, both verbatim. A negative example if available.

Extraction targets: for each channel, a specific audience and intent, lead-with and off-limits moves, a real explanation sample, real use and avoid lists, a concrete failure signature, and one real anchor. Objection responses captured in the agent's words.

## Assembly

Append `## Written Voice` through `## Voice Permissions` to the document Session 1 produced, using `${CLAUDE_PLUGIN_ROOT}/references/output-schema.md`. If it exists as a file, open it and append. If it does not, work from the version in the conversation. Do not rewrite or reorder anything Session 1 wrote.

Keep Written Voice and Spoken Voice as two fully separate systems. Paste anchors verbatim, including dictated filler; do not convert spoken cadence into written prose. Build patterns from confirmed observations using the agent's real use and avoid lists. Make the avoid list and failure signature specific, since they are what protect against generic AI output. Scope Voice Permissions to voice only and point back to the AI Boundaries section rather than restating it. Do not invent: leave a bracketed request for any missing anchor rather than fabricating one.

## Confirm it resolved

Before you finish, check that the finished document contains `## AI Boundaries` and at least one `### Failure signature`. If either is missing, the foundation will not pass the check that drafting skills run, and it will refuse to draft. Fix it now rather than letting the agent discover it later.
