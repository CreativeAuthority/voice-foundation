# Reviewed foundation data contract

Create UTF-8 `foundation.json` in the agent's private workspace. The builder uses the same source for all exports. Required fields below are a schema guide, not ready-made answers. Strings contain the agent's language or confirmed interpretations. Arrays of text must contain meaningful content, not placeholders.

- `schema_version`: 1.
- `agent_id`: a stable, random canonical lowercase UUID for this person/business.
- `revision`: positive integer, starting at 1. Increment for reviewed updates.
- `date`: actual review date, YYYY-MM-DD.
- `demo`: false for a real agent. True only for clearly labeled synthetic product tests.
- `identity`: object with `name`, `business`, `market`; optional confirmed signature fields (brokerage, license state, title, email, phone, website, MLS limit). Capture `team_membership` (yes/no in the agent’s terms) and, if applicable, `team_role` as separate identity fields from their brokerage role. Unknown optional fields may be omitted.
- `profile`: `best_fit`, `poor_fit`, `protected_outcomes`, `trust_sequence`, each text.
- `mission`: array of two to five first-person paragraphs.
- `decision_rules`: at least four objects `{trigger, response, evidence_ids}`. The renderer adds IF and THEN; write trigger and response as clauses. Cite four distinct `decision_scenario` or clearly labeled `prospective_policy` evidence records across the set. Avoid generic virtues disguised as rules.
- `ai_boundaries`: nonempty array of specific hard limits the agent supplied/confirmed.
- `stop_and_ask`: at least two concrete triggers supplied/confirmed by the agent.
- `written` and `spoken`: objects each containing `audience`, `intent`, `rhythm` (text); `rules`, `use`, `avoid`, `failure_signature` (nonempty text arrays); `evidence_ids` (source IDs); and `anchor` (see below).
- `spoken.objections`: at least two `{objection, response, evidence_ids}` objects. Preserve their actual response; label proposed future responses explicitly.
- `anchor`: `{text, source, evidence_id}`. `text` must equal the linked evidence's text character-for-character. Link `written_sample` for written and `spoken_sample` for spoken. The source is an honest label, e.g. “Agent-pasted client email, client names redacted” or “Agent-provided transcript of a consultation.” Do not claim an improvised AI draft is evidence.
- `voice_permissions`: `may`, `never`, `uncertain`, each a nonempty array of text.
- `evidence`: array of `{id, kind, text, source, confirmed}`. Unique stable ID; kind is `answer`, `decision_scenario`, `prospective_policy`, `written_sample`, `spoken_sample`, or `correction`; exact agent text; source label; confirmed boolean. A correction also has `supersedes`, the ID of retained prior evidence; never overwrite the earlier quote. Only confirmed evidence belongs in the final source. Keep unconfirmed material in the interview checkpoint.
- `provenance`: object with `mission`, `profile`, `ai_boundaries`, `stop_and_ask`, `voice_permissions`, each a nonempty array of evidence IDs. Channel evidence links cover rules, rhythm and failure signatures; individual decision rules and objections carry their own evidence links.
- `review`: `{mission_confirmed: true, voice_confirmed: true, final_confirmed: true, open_gaps: [], confirmation_quote: "...", evidence_ids: ["..."]}`. Quote the agent's actual final accuracy confirmation; it must occur in the referenced evidence. Set these values only after their content review.

The builder checks counts, required content, unique IDs, provenance, verbatim anchors and completion flags. It cannot assess the meaning or truth of a quote. Before generating, the interviewer must verify that rules really follow from their cited evidence, prospective policies are labeled, and review flags reflect actual user turns.

Partial interviews can use this shape with gaps, but they will not pass final delivery. Save them as drafts/checkpoints, not as a completed `foundation.json`. Never manufacture evidence or approval to make a validator pass.
