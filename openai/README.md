# Voice Foundation for ChatGPT and Codex

**Pilot build: not yet a verified public ChatGPT installation.**

This package contains the OpenAI version of Creative Authority's two-session Voice Foundation. The Claude version remains in the repository's original `voice-foundation/` folder.

## What the agent does

Once installed in a supported environment, start a fresh chat and say **Start my voice foundation**. The interview asks one question at a time, follows up on vague answers, and gathers real written and spoken examples. The agent reviews their mission, decision rules and voice before delivery.

The finished foundation produces:

- A branded PDF explaining the mission, decision rules and canonical voice.
- Complete operating instructions to paste into another AI chat.
- A private personalized writing skill containing the entire foundation, with written and spoken voice kept distinct.

The writing skill is generated for the individual agent. Installation and skill-menu discovery must be verified on their host; creating a ZIP is not the same as registering a permanent skill.

## Requirements and pilot installation

The interview is powered by the agent's ChatGPT/Codex account. The package itself needs no separate API key or external service. File delivery needs a supported Work environment with code/file tools and Python 3.10+ with ReportLab. The target customer's account and device must be tested before promising compatibility.

For local Codex authoring/pilot use, clone this repository and add the marketplace at the `openai` directory:

```sh
codex plugin marketplace add /absolute/path/to/voice-foundation/openai
codex plugin add voice-foundation@creative-authority-openai
```

The local marketplace is named `creative-authority-openai` so it can coexist with the Claude marketplace and an existing personal marketplace. After installation, start a fresh task and explicitly select this OpenAI version for the pilot. This is a developer/pilot route, not instructions to put in front of 300 nontechnical agents.

For a managed ChatGPT workspace, an administrator can evaluate importing this GitHub repository with marketplace Path set to `openai`, subject to the workspace's plugin policies. This is not a universal individual-account installation method.

## Website downloads

Run `python3 openai/scripts/package.py` from the repository root to build `openai/dist/voice-foundation-openai-v1.0.0.zip` and its checksum. Upload that ZIP as a GitHub Release asset or to your website's file storage. A button can link directly to the resulting asset URL.

For the intended low-friction experience, the website should link to an actual supported installation/listing page, followed by **Start my voice foundation**. No public listing URL exists in this repository. Public publication requires the OpenAI submission process; do not present a GitHub download as automatic installation.

See [launch checks](LAUNCH-CHECKLIST.md) before distributing widely.

## Development checks

```sh
python3 -m pip install reportlab pypdf
python3 -m unittest discover -s openai/tests -v
python3 openai/scripts/package.py
```

Tests use an explicitly fictional agent. Test answers and private generated skills are excluded from the generic ZIP. The local PDF builder makes no network calls; normal host data handling still applies.

## Official references

- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Skill availability and selection](https://learn.chatgpt.com/docs/build-skills)
- [GitHub workspace marketplace import](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Public plugin submission](https://developers.openai.com/plugins/deploy/submission)

## License

Creative Authority's repository license applies to this package. Bundled fonts retain their separate [font license](plugins/voice-foundation/assets/FONT-LICENSE.txt). Agents own their answers and generated foundations.
