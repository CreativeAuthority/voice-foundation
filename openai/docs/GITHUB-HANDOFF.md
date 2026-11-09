# GitHub handoff

Repository: https://github.com/CreativeAuthority/voice-foundation

The OpenAI version lives in the `openai/` folder. The Claude plugin in `voice-foundation/` and the Claude marketplace in `.claude-plugin/` are separate and aren't changed by OpenAI work.

## Release 1.0.4

This is the version submitted for OpenAI review on October 2, 2026. The ZIP built from this source has the same contents as the submitted ZIP. Submission records, portal IDs, and test transcripts are kept outside the repository.

The earlier pilot branch, `openai-voice-foundation-pilot` (v1.0.0), is superseded. Its pull request was closed without merging, because the branch predates the September 13, 2026 change to `main` and would have reverted it.

## Keep these out of the repository

- `dist/`: rebuild it with `scripts/package.py`.
- `output/` and any customer foundation files.
- `submission/`: portal records and account details.
