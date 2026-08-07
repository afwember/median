# MEDIAN source-bounded atomic extraction

Allowed source: `M050-SRC-047-SURVIVORSHIP-REVIEW-001`
Allowed streams: `evidence_game_semantic`, `provenance_evidence`

The input-ordered disposition block-ID set must exactly equal `target_blocks`:
none missing, repeated, or partial.
Use only `SOURCE_BLOCKS`.

Use supplied IDs; never samples, placeholders, or dummy `x`.
Unresolved targets get `review_required`; never abbreviate the target set.

## Approved content/provenance boundary

# MEDIAN v0.5.0 v0.4.7 Development Survivorship Review Content/Provenance Identity Card v0.1

Date: 2026-08-07
Status: `APPROVED`
Lifecycle state: `identity_card_approved`
Author/root of authority: Asa Wember

## Source identity and authority

| Field | Bound value |
|---|---|
| Source ID | `M050-SRC-047-SURVIVORSHIP-REVIEW-001` |
| Path | `m050/docs/v0.5/provenance/M050_v0_4_7_Development_Survivorship_Review_v0_1_MEDIANv0_5_0.md` |
| SHA-256 | `cd32434225e48618689f73f697ec21c17514514f3bea28ea0de552318a58257b` |
| Source role | `v0_4_7_decision_development_survivorship_and_adaptation_review` |
| Disposition | `source_bounded_atomic_extraction_then_content_partition_before_grand_reconciliation` |
| Allowed streams | `evidence_game_semantic`; `provenance_evidence` |
| Compile position | Ordinal 18; next outstanding source after completed v0.4.7 Development Rulings |

The registered frozen Markdown is the sole extraction source.

## Status and qualification handling

The source declares itself a model-authored survivorship audit identifying
baseline material as `CLOSED`, `DECISION REQUIRED`, `CARRY-FORWARD REVIEW`, or
`DEFER`, with recommendations and architecture-blocker assessments. Preserve
those statuses, audit claims, recommendations, historical comparisons, and
unresolved qualifications as source-bounded evidence without treating them as
authorial rulings or adjudicating their cross-source authority.

## Media and exclusions

The registered Markdown contains no embedded media or media-associated caption.
External sources, artwork, repository history, earlier forms, and alternate
representations are excluded.

Document-control furniture, nonsemantic whitespace, source-position comments,
pure structural headings, and table delimiters use the established
source-agnostic dispositions.

## Extraction boundary

Extract only game-semantic and provenance evidence present in the registered
Markdown. Do not import its named external sources, determine cross-source
ownership, apply asserted precedence, or perform the proposed content partition
or reconciliation during source-bounded extraction.

Source-bounded candidate acceptance is not semantic acceptance, mapping,
reconciliation, canonization, compiled prose, or permission to begin another
source, later compile stage, or Google Sheets work.

## Approval boundary

Asa Wember approved this source identity and extraction boundary. Approval
permits the established Development Survivorship Review-only offline preparation
and representative pilot calibration; provider readiness still requires
validated frozen bindings, completed offline and replay gates, sequential
review, and sufficient budget.

## Extraction contract

Separate claims only when each remains independently grounded and self-contained.
Exact spans uniquely ground core assertions. Preserve coordinated subjects or effects in one atom
when they share a predicate, subject, condition, or relationship;
split only at a contiguous subject-predicate span. A subject or
label alone never grounds an imported predicate. Anchor each normalized claim in `exact_source_text`.
For self-containment, if bound context names a pronoun, anaphora, or subjectless prefix's referent,
substitute it in `normalized_claim`. Headings supply only status or scope.
Never paraphrase, gloss, define, compare, infer, or complete implied meaning;
use `review_required`. Parent headings are context, never atoms.
Every `exact_source_text` is a byte-for-byte contiguous
target-block substring that occurs exactly once. JSON-decoded, it contains actual target-block
characters, never literal backslash Unicode-escape spellings.
No `exact_source_text` may cross an authored semicolon. Split semicolon-delimited
clauses into separate atoms, including coordinated examples in ordinary prose.
Restore an omitted later-clause subject only in `normalized_claim` from its
adjacent coordinated clause. Repeated spans expand through nearest
semicolon-free source boundary. Include interrupting markup or split the atom.

Obey `required_disposition`, `allowed_dispositions`, and `minimum_atoms`;
`no_substantive_claim` requires empty `atoms`. Headings, labels, table headers,
delimiters, and document-control metadata carry no substantive atom. Dependent
list items use minimum unambiguously-adjacent governing
subject/status/scope/condition/connective, grammatically agreeing with targets;
lead-ins cannot import body names,
members, or assertions.

For substantive table rows, cover every nonempty semantic cell. Separate
properties, functions, effects, examples, interpretations, stages,
actions, and results. Combine qualifying/indivisible cells; preserve
categorical-mapping endpoints.
Ground each headed cell under its header; never infer a relationship between
adjacent cells. Table spans—cell or whole-row—split at authored semicolons;
none crosses one.
Copy every authored slash into the normalized claim; never replace it with a word unless the source defines that meaning.
Each independent table-cell assertion requires exact source text from its own
cell; never ground a ruling or consequence only in another cell.

Process/audit/publication → `provenance_evidence`; game claims → `evidence_game_semantic`.
Preserve provisional, historical, rejected, example, negative, conditional,
scope, ownership, and authority qualifiers. Use `review_required` instead of
guessing. Never repair source text or invent identifiers, statuses, owners, or
authorities.

## Output check

Return schema-bound JSON only after verifying exactly
`required_target_disposition_count` dispositions. Kind `atoms` requires nonempty
`atoms`; all other kinds require empty `atoms`. Every atom needs IDs/stream,
exact source text, normalized claim, and source-faithful kind.
Derive each proposal ID from target block ID plus local atom ordinal;
proposal IDs must remain source-unique.
