# MEDIAN v0.5.0 Authorial Grammar Offline Dry-Run Report v0.1

Date: 2026-08-03  
State reached: `offline_dry_run`  
Source: `M050-SRC-AUTHORIAL-GRAMMAR-001`  
Provider calls: **0**  
Accounted cost: **0 cents**  
Google Sheets interactions: **0**  
Pilot state: **not frozen**

## Authority and source binding

Asa Wember approved the Authorial Grammar content/provenance identity card at SHA-256 `983ca763a907d3465c14215bed7f165f712b903567b5bbe54f6e50f6717e10b4` and then instructed the normal next transition to proceed. This report covers offline preparation only.

The source remained byte-identical at SHA-256 `7d23ef2ccbff0c6594975c03cf405d838a3cc3f712ea6faf942581a72c9284ff`. Only `evidence_authorial_rule` is allowed. Prompt-extractable content is restricted to this source ID; foreign evidence count is zero.

## Complete structural parse

The deterministic parser preserved the complete source byte-for-text after conservative structural normalization and produced:

| Measure | Count |
|---|---:|
| Total blocks | 590 |
| Paragraphs | 126 |
| Headings | 61 |
| List items | 75 |
| Table rows | 51 |
| Fenced-code blocks | 38 |
| Whitespace blocks | 239 |
| Initially claim-bearing blocks | 252 |
| Initial estimated claims | 300 |

The approved offline disposition policy accounts for all 590 blocks exactly once:

| Disposition | Count |
|---|---:|
| Eligible | 228 |
| Context only | 82 |
| Excluded | 280 |

Excluded material includes front/document furniture, separators and whitespace, and the complete 14-block Change Record region. Thirteen fenced inventories or semantically operative examples are eligible; the remaining fenced examples/templates are context-only. The `status: PROVISIONAL` record is eligible and carries an explicit status marker.

The planned Phonebook appendix plate is the only media/publication reference. It has terminal disposition `publication_only`; no embedded image, figure, audio, video, or external media asset exists in the source.

## Rejected offline methods and corrections

### Generic dual-limit plan rejected

The first no-write planning comparison used the existing token/claim planner. It split by claim count and isolated the `PROVISIONAL` YAML record into a 62-token, zero-claim chunk. This lost the surrounding Defined Text Treatments section needed to interpret the provisional status. No plan artifact from this attempt was promoted.

The corrected isolated deterministic planner packs complete Markdown level-one sections without changing the frozen engine. At limits of 1,800 estimated input tokens and 60 claim-bearing blocks, it creates five chunks with estimates:

| Chunk | Estimated tokens | Claim-bearing blocks |
|---:|---:|---:|
| 1 | 877 | 50 |
| 2 | 1,360 | 47 |
| 3 | 1,179 | 43 |
| 4 | 1,334 | 52 |
| 5 | 1,055 | 60 |

Every source block occurs exactly once. The provisional record remains with the complete Defined Text Treatments section. Excluded blocks remain structurally accounted for but must be mechanically omitted from any provider payload.

### Review-required structural-block gap rejected

The frozen generic proposal validator requires dispositions only for blocks already labeled claim-bearing. Used alone, that would make fenced examples and YAML impossible to disposition, including the source's only explicit provisional record. The offline disposition policy therefore promotes thirteen named semantic fenced blocks to eligible and accounts for every other fenced block as context-only. The isolated offline contract tests require explicit handling of the promoted blocks without changing the frozen engine or introducing a provider worker.

## Prompt and response-contract dry run

The offline prompt template:

- contains no source text;
- permits only the Authorial Grammar source ID and `evidence_authorial_rule` stream;
- incorporates the approved terminology “Defined Nouns” and “experiential verbs and Core-Species operators”;
- prohibits other-source evidence, background knowledge, ontology/path adjudication, mechanics ownership, reconciliation, canonization, and final publication implementation;
- requires exact contiguous grounding and one disposition per presented eligible/review-required block; and
- requires explicit preservation of provisional, prospective, derived, example, historical, negative, and context qualifiers.

The response schema fixes the source ID and stream, constrains block-ID form, refuses uncontrolled fields, and requires atoms only for an `atoms` disposition.

## Fake and malformed-response evidence

A synthetic valid response was exercised against the eligible provisional YAML block. It passed:

- JSON Schema validation;
- explicit block disposition validation;
- exact source grounding;
- source/profile allowlist validation; and
- preservation of `PROVISIONAL` in the normalized claim.

Malformed variants failed closed for:

- `evidence_game_semantic` in place of the allowed stream;
- a foreign Human Rulings source ID;
- loss of the `PROVISIONAL` qualifier;
- invented, ungrounded exact-source text; and
- attempted use of an excluded Change Record block.

These are offline synthetic tests. They are not provider responses, atom candidates, semantic review, or acceptance.

## Hash-bound offline artifacts

| Artifact | SHA-256 |
|---|---|
| Offline disposition policy | `904a25bba3e96a18be67bd7a58a78f0692ace38a48a8bf8287ae94087bad3c92` |
| Block manifest | `cf1d0291cf7cb9fb3d959cb45f3477d69f5987d7d93c4f79b89dfe743eea0cca` |
| Section-aware chunk plan | `ef3aa26a3c2020a52ee452a6706dd83604e5d3145af56380df64155da8a5adb2` |
| Complete block-disposition ledger | `a365b4260d8cb7820742e4ab879c3d6336f643989139c700401ee887cf960b6c` |
| Offline readiness profile | `82cde773092c761d2e2b2556473513a68fa3ef396cfe07b07ef3926a4d22880b` |
| Prompt template v0.1 | `3833be2222cf0e2506cb7c44c4f1909865b46355c9cb998c21feab51ece077a3` |
| Response schema v0.1 | `f5bf0ac439b11f975216ee0ac7e59e4886079efcf4f0ed2e3fb5627826b160a7` |
| Offline profile builder | `ff71acb9779c20b52e1c5f678362de5bca190299d2428b822ab16e945bcf441e` |
| Section-aware planner tool | `b1ca85a93f2e0c12938b5f1f0c6740158f795fc2f525576f8b80b55b1463c9cd` |
| Authorial offline regression tests | `81f7e7031d917b1dd03b2380da7b74a4d567c0754df43e4bf09f75747d67b609` |
| Source-pilot request renderer | `69a196c0f553362079caef189be9f8526b07eb85481e9f0e114165ff4f6270b5` |
| Source-pilot response validator | `caace05225dd4e9e5ef32c04ceef8b8611813a0d92646abe6fc9efda3bc7dbf5` |

## Representative-pilot regimes identified during offline dry run

No pilot chunk has been selected or frozen. The following risk regimes require explicit consideration at the next transition:

1. **Tables, inventories, examples, and cross-owner syntax:** chunks 2–3 contain Initial Caps, experiential verbs/Core-Species operators, MSID display, Core-Species grammar, and Hyphen-bound mappings. They test table and fenced-inventory handling plus the boundary between authored display and external ontology/mechanics ownership.
2. **Status and example polarity:** chunk 4 contains the sole `PROVISIONAL` convention, the emergent-status lifecycle, voice rules, and conforming/nonconforming examples. It tests status preservation and prevents negative examples from becoming positive rules.
3. **Checklist, lint, derived publication, and exclusions:** chunk 5 contains the authoring checklist, prospective lint rules, derived Phonebook plate, current convention ledger, and excluded Change Record. It tests prospective/derived qualifiers, table status, and terminal exclusion behavior.

The follow-on pilot-freeze preparation rendered one bounded candidate for each regime and recorded the exact requests and bindings in `M050_Authorial_Grammar_Pilot_Freeze_Proposal_v0_1_MEDIANv0_5_0.json`. That proposal does not advance the machine state because its author-approved cost-cap field remains unset.

## Transition boundary

Offline dry-run preparation is complete. The source has **not** advanced to `pilot_frozen`. Asa Wember confirmed `claude-sonnet-5` with low effort for atomic extraction and reserved `gpt-5.6-sol` for the later post-extraction phase, without activating that phase. Three exact candidate requests exist, but their authorized provider-call limits remain zero. No cost cap is approved, no provider request is authorized, and no full-source activity is authorized.
