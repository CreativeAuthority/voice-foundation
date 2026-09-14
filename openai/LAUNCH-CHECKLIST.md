# Thursday launch checks

The repository can host both versions. It does not remove the target AI's installation requirements.

## Already checked in the local build

- Generic plugin installed and enabled in the creator's local Codex environment.
- OpenAI manifest and skill validators passed.
- Seven automated tests cover PDF/prompt/skill consistency, evidence requirements, revision preservation, private installation, and collision protection.
- Fictional sample PDF rendered and visually checked.

## Required before calling the ChatGPT experience ready for the audience

- Establish the actual audience environment: ChatGPT browser, desktop, or Codex and relevant account access.
- Obtain a supported install/share/listing URL and test it from an unrelated agent's account.
- Verify website/QR → installation → first interview question, without developer instructions.
- Complete a real interview, including pause/resume and pushback on thin answers.
- Download and review that agent's PDF and portable instructions.
- Verify the personalized skill appears in their menu and works in a separate chat.
- Test a written request and a spoken-script request, with the correct voice selected.
- Establish a fallback path for attendees who cannot install; label its limits accurately.

The biggest remaining uncertainty is customer-account installation and persistence of the personalized skill, not storage of the ZIP on GitHub. Do not promise cross-chat access solely because the agent downloaded a file.

## Website structure

Use two distinct buttons: **Use with Claude** and **Use with ChatGPT**. The Claude path can follow the repository's existing published instructions. The ChatGPT path should use the verified destination above; until it exists, label the OpenAI package as a pilot rather than claiming one-click setup.

A public GitHub Release asset can serve as the download behind a website button. The direct asset URL should be copied from the actual uploaded release, not guessed. Public plugin submission and any required policy attestations are separate from uploading a ZIP.
