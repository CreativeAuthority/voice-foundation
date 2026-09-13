# content.json format for the Voice Foundation PDF

Build this from the agent's own foundation files and interview answers. Every field is theirs. Do not invent content to fill a gap; leave it out instead.

```json
{
  "biz": "<agent's real-estate brand, from Identity and Business>",
  "date": "<current month and year>",
  "note": "Produced with AI from your own answers. Every idea is yours. Review it, and change any line that does not sound like you.",
  "identity": [
    ["Name", "..."],
    ["Title", "..."],
    ["Brokerage", "..."],
    ["Business", "..."],
    ["State", "..."],
    ["Phone", "..."],
    ["Email", "..."],
    ["Website", "..."],
    ["Primary market", "..."],
    ["Social", "..."]
  ],
  "mission": [
    ["Who do you serve best?", "the agent's answer, cleaned lightly"],
    ["What are they really trusting you to protect?", "..."]
  ],
  "voice": [
    ["Who are you writing to, and what do you want them to feel and do?", "..."],
    ["What tips you off that writing is not you?", "..."]
  ],
  "voice_anchors": [
    ["Written anchor · one-to-one email", "a short real excerpt"],
    ["Spoken anchor · explaining a trade-off", "a short real excerpt"]
  ],
  "prompt": "You are working and writing on behalf of [name]... (full operating prompt as plain text)"
}
```

## Field notes

- `biz`: the agent's real-estate brand or DBA, from the Identity and Business block in voice_foundation.md. Used in the PDF header and the output filename.
- `date`: the current month and year at build time.
- `identity`: pull straight from the Identity and Business block in voice_foundation.md. Keep values short.
- `mission` and `voice`: use the real interview questions with the agent's own answers, lightly cleaned for readability. Keep spoken cadence intact in any dictated material.
- `voice_anchors`: one or two short, real excerpts. Pull from the Anchor sections already in voice_foundation.md.
- `prompt`: write in third person, addressed to the AI. Combine, in this order: who the agent serves, how they think and decide, a NEVER list of hard boundaries, how they sound (written then spoken), the failure signature of tells to avoid, and a short WHAT TO ALWAYS ASK ME FIRST list of two or three questions. This is the portable twin of voice_foundation.md, not a new capture.

## Render

```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/build-voice-pdf/assets/voice_foundation_pdf_builder.py" content.json "<agent folder>/Voice_Foundation_<Business>.pdf"
```

No install step. The builder uses WeasyPrint when it is present and writes a branded, print-ready HTML file beside the target path when it is not. Pass `--html` to force the HTML path.

Fonts: Lora and Poppins are used when installed, with Georgia and Helvetica as fallbacks, so the document is correct either way. The Montserrat wordmark is embedded in the logo image.
