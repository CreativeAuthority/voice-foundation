---
name: build-voice-pdf
description: >
  Use this skill when the user says "Build my voice foundation PDF", "Generate the voice PDF",
  "Make the client PDF", or when run-voice-foundation calls for it. It assembles the agent's
  interview answers and foundation files into a Creative Authority branded PDF with a portable
  operating prompt. Run only after both foundation sessions are complete.
---

Produce the client-facing, Creative Authority branded PDF for an agent whose voice foundation is complete. The two markdown files face the AI; this PDF faces the person. It gives the agent clarity on how they work and communicate, and a portable operating prompt they can paste into any AI, inside the system or out.

## Prerequisites

The agent's folder must already contain a complete `voice_foundation.md`, with both the mission sections and the voice sections written. If the voice sections are missing, stop and run `run-voice-session` first.

## What the PDF contains

1. The basics, from the Identity and Business block.
2. The Q&A from both sessions, in the agent's own answers, lightly cleaned, with written and spoken voice anchors as pull quotes.
3. One paste-ready operating prompt that combines mission, decision rules, and voice, ending with a short WHAT TO ALWAYS ASK ME FIRST list.

The operating prompt is not an appendix. It is one of the two ways this product actually gets used: pasted into a Claude project's custom instructions, or into any other AI, it carries the agent's voice everywhere without a file or a folder. Write it so it stands completely on its own, readable by a model that has never seen the foundation document, and put the failure signature inside it rather than referring to it.

## Steps

1. Read `voice_foundation.md` and the interview answers from this foundation.
2. Build a `content.json` matching the shape in `references/content-format.md`. Populate every field from the agent's real material. For the operating prompt, write it in third person addressed to the AI ("You are working on behalf of [name]"), combining the mission, the hard boundaries, the written and spoken voice essentials, the failure signature, and two or three clarifying questions to always ask first. Do not invent; if something is thin, leave it out.
3. Render with the bundled builder. Run it exactly as written, with no install step first:

   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/build-voice-pdf/assets/voice_foundation_pdf_builder.py" content.json "<agent folder>/Voice_Foundation_<AgentBusiness>.pdf"`

   The builder runs offline and defaults to the bundled wordmark, so no logo argument is needed. It uses the Creative Authority palette with Lora and Poppins, falling back to Georgia and Helvetica when those are not installed.

4. Read what the builder printed, and handle the two cases.

   `WROTE` means the PDF rendered. Confirm the page count and that the operating-prompt panel is whole, then tell the agent where it is.

   `WROTE_HTML` means the PDF engine is not installed on this machine, so the builder produced a fully branded HTML version instead. This is a normal outcome, not a failure, and it is the right moment to be matter-of-fact rather than apologetic. Tell the agent their foundation document is ready, that it opens in their browser, and that Command-P then Save as PDF gives them the PDF. The file itself carries a bar at the top saying the same thing, and that bar does not appear in the saved PDF.

   Only if the agent specifically wants the builder to produce PDFs directly, offer the install once: `pip install weasyprint --break-system-packages`. Do not run it unasked, do not run it before step 3, and do not troubleshoot a failed install past one attempt. The HTML path produces the same document and nobody's deliverable should wait on a toolchain.

## Never block on the renderer

The PDF is the thing the agent paid for and can hold. Whatever happens with the rendering engine, they end this step with a finished branded document in their folder. If both paths somehow fail, write the operating prompt into a plain markdown file and hand them that, then say plainly what did not render.

## Branding note

The PDF is always branded to Creative Authority, since Creative Authority is the producer, regardless of the agent's own business. The bundled logo in `assets/` is the wordmark. Do not substitute the agent's brand here.

## Honesty line

Include the standard note: produced with AI from the agent's own answers, every idea is theirs, review and change anything that is not them.
