# Delivery and skill registration

Read [data contract](data-contract.md). Use one confirmed foundation.json as source for all deliverables. Never save personal data inside this shared plugin or its cache. Each skill carries its own scripts and assets. From this references directory, `../scripts/build_foundation.py` is the builder. Resolve `<skill-root>` as the directory containing this skill’s SKILL.md, never a sibling skill or a shared plugin parent.

## Build

Attempt the build first using the host’s available Python 3 (3.8 or newer). ReportLab is optional. Never run an install command before attempting the build. If PDF generation fails, the builder preserves all other deliverables and writes branded Voice_Foundation.html beside the intended PDF path. It has a Command-P / Ctrl-P Save as PDF banner hidden when printing. Offer the actual HTML link and print instruction; never call HTML a finished PDF. The builder never calls a model, remote server, or uploads answers. Resolve the actual plugin path from this SKILL.md rather than assuming a machine-specific location.

Run:

```
python3 <skill-root>/scripts/build_foundation.py <private-foundation.json> --output <user-workspace>/Voice-Foundation-Deliverables
```

The output parent may exist; the version-specific delivery directory must be new. The script refuses to overwrite an earlier revision. It validates the data and emits one version directory containing:

- Voice_Foundation.pdf (or self-contained print-ready Voice_Foundation.html): explanations plus the complete mission, decision rules, separate written/spoken references, and the portable instructions.
- voice_foundation.md: one complete readable foundation.
- operating-instructions.txt: the full portable prompt, including that same foundation.
- a private skill folder and its ZIP, with the complete foundation as a bundled reference and menu metadata.
- a private personalized plugin folder and ZIP for hosts that distribute skills through plugins.
- foundation.json and delivery.json, for private revision and verification.

The script checks structure and evidence links, not whether the agent's beliefs are wise or a sentence truly matches their style. You still review the content. Missing evidence/review means finish the interview; never fill fields simply to bypass validation.

Open the actual PDF or HTML and render/inspect pages with available PDF tools. Check the complete sections, exact anchors, no clipping, and readable page breaks. Read the generated skill and bundled reference. For a spoken script or long URL, do not alter source text merely to fit a layout.

## Register the private skill

This step is part of delivery. Discover the host's supported skill-creation or skill-installation capability and use it with the generated skill directory/archive and UI name. Use the built-in skill creator where available; do not invent a tool name or API. In local Codex, a supported personal location is `~/.agents/skills/<generated-skill-name>/`; installation must follow filesystem permissions. Do not put personal skills into shared repos or the public plugin. If updating, confirm the existing skill belongs to the same agent_id before replacing its bundled reference; preserve the prior revision.

For a confirmed local Codex host, the bundled helper performs the file installation with collision checks:

```
python3 <skill-root>/scripts/install_personal_skill.py <generated-version-directory> --skills-dir <actual-user-home>/.agents/skills
```

Use `--update` only for a reviewed later revision of the same agent. The helper keeps a backup outside skill discovery and records `installed_files_pending_discovery`; this is deliberately not a claim of menu availability. Use normal host approval handling if that directory is outside the writable workspace. Never route a remote/cloud installation into an arbitrary local directory just to claim success.

For a host requiring plugin installation, offer the private generated plugin through its supported local/private install flow. Never publish or share an agent's personalized plugin publicly. The public Voice Foundation installer contains only generic workflows.

Verify registration using the host's skill list/menu or a fresh conversation with the skill explicitly selected. Verify the bundled agent_id/revision, not merely a folder's existence. Update delivery.json installation status only after evidence. If unavailable, deliver the private ZIP and explain the one remaining installation action; call it “created, ready to install,” not “installed.” Do not claim menu availability from archive creation.

ChatGPT uses @ selection; Codex uses $ selection. The familiar spoken trigger is “Write this in my voice.” Implicit skill matching depends on the host; explicit selection is the reliable alternative. If more than one foundation is installed, choose the correct person/business rather than guessing.

## No Python/file tools

Do not lose the completed interview because the host lacks execution tools. Present the full canonical foundation and portable operating prompt in the conversation as equal usable delivery paths. If file creation is available but Python is absent, create self-contained print-ready HTML using the branding and print rules above directly, plus the reviewed JSON and skill files. If files cannot be created, explain that downloadable documents and skill registration remain pending; supply a copyable checkpoint for Work. Never direct a nontechnical buyer to install Python or libraries.

## Finish

Present two equal choices: the foundation document (PDF or printable HTML), and the complete portable operating prompt for a project’s custom instructions. Also give the private writing skill ZIP. Neither document nor prompt is a fallback. In ChatGPT, if direct skill registration is unavailable, explain the tested manual path: Skills → Create → Upload from your computer → select my-writing-skill.zip, then open a fresh chat and select that personal skill. Creating the ZIP alone is “created, ready to install.” Only claim installation after verifying host discovery and the bundled identity/revision. Cloud updates must preserve the previous source/export before editing, and never claim host backup behavior without evidence. Explain actual installation status in one plain sentence. Offer to test a real piece with the foundation and use the resulting corrections if the agent wants to save them. The PDF and prompt are usable even when installation is pending, but do not report the full requested delivery complete until the skill is registered or the remaining host limitation is clearly identified.
