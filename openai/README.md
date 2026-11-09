# Voice Foundation for ChatGPT and Codex

Release 1.0.4, submitted for OpenAI review on October 2, 2026. Not published.

A skills-only Creative Authority plugin for real estate agents: start or resume a reviewed mission/voice interview, write with a completed foundation, and update enduring preferences. Each interview/delivery skill contains its own scripts, fonts and references so imports do not depend on a shared plugin folder.

## Deliverables

The reviewed foundation produces a PDF (or printable HTML when the PDF engine is unavailable), Markdown, complete portable instructions, source JSON, and a private personalized writing skill. The document and portable prompt are equally usable options. A generated skill is “created, ready to install” until host discovery is verified. No separate API key or Creative Authority service is required. File generation uses the host's code/file tools; without them the workflow supplies copyable foundation and checkpoint text. Customers are not asked to install Python or libraries.

The generic package contains no customer foundations. The bundled Python helpers do not make network calls or add telemetry. Host processing and storage follow the user's ChatGPT/Codex environment and settings.

## Build and check the package

This folder holds the source for release 1.0.4. Built ZIPs, submission records, and interview output aren't kept in the repository.

To build the four release ZIPs into `dist/`, run:

```
python3 scripts/package.py
```

To run the offline package checks and the test suite, run:

```
python3 scripts/check_package.py
python3 -m unittest discover -s tests
```

`dist/voice-foundation-chatgpt-v1.0.4.zip` is the combined package for the OpenAI plugin portal. The three single-skill ZIPs are for manual upload through ChatGPT Skills.

Do not distribute older ZIPs as the current release. The locally installed personal plugin is separate from this editable source; editing source does not update an installed copy. Never package the private `output/` or `Voice-Foundation-Deliverables/` directories for public distribution.
