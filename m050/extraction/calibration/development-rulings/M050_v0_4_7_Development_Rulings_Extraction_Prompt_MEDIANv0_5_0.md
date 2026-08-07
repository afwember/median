# MEDIAN source-bounded atomic extraction

Allowed source: `M050-SRC-047-DEVELOPMENT-RULINGS-001`
Allowed streams: `evidence_game_semantic`, `provenance_evidence`

The input-ordered disposition block-ID set must exactly equal `target_blocks`:
none missing, repeated, or partial.
Use only `SOURCE_BLOCKS`.

Use supplied IDs; never samples, placeholders, or dummy `x`.
Unresolved targets get `review_required`; never abbreviate the target set.

## Approved content/provenance boundary

# MEDIAN v0.5.0 v0.4.7 Development Rulings Content/Provenance Identity Card v0.1

Date: 2026-08-06
Status: `APPROVED`
Lifecycle state: `identity_card_approved`
Author/root of authority: Asa Wember

## Source identity and authority

| Field | Bound value |
|---|---|
| Source ID | `M050-SRC-047-DEVELOPMENT-RULINGS-001` |
| Path | `m050/docs/v0.5/provenance/M050_v0_4_7_Development_Rulings_Ledger_BSA_01_to_11A_Checkpoint_2026_07_30_MEDIANv0_5_0.md` |
| SHA-256 | `34ba0aa443aefe73ee041189998e9afa44521ffe7e7d742d787286f6ae3a2a6b` |
| Source role | `v0_4_7_to_v0_5_working_adaptation_and_disposition_ledger` |
| Disposition | `source_bounded_atomic_extraction_then_content_partition_before_grand_reconciliation` |
| Allowed streams | `evidence_game_semantic`; `provenance_evidence` |
| Compile position | Ordinal 17; next outstanding source after completed v0.4.6 GDD Coverage-Gap Development |

The registered frozen Markdown is the sole extraction source.

## Status and qualification handling

The source declares itself an authoritative working ledger for later
specification authoring and a curated adopted baseline through BSA-11A.
Preserve its explicit adopted, working, exact, tunable, reserved, deprecated,
provisional, example, status, and scope qualifications without resolving them.
Its internal authority and adoption language governs this source only and does
not adjudicate cross-source authority.

## Media and exclusions

The registered Markdown contains no embedded media or media-associated caption.
External sources, repository history, earlier forms, and alternate
representations are excluded.

Document-control furniture, nonsemantic whitespace, source-position comments,
pure structural headings, and table delimiters use the established
source-agnostic dispositions.

## Extraction boundary

Extract only game-semantic and provenance evidence present in the registered
Markdown. Do not import external material, adjudicate cross-source authority,
partition content, or reconcile overlaps during source-bounded extraction.

Source-bounded candidate acceptance is not semantic acceptance, mapping,
reconciliation, canonization, compiled prose, or permission to begin another
source, later compile stage, or Google Sheets work.

## Approval boundary

Asa Wember approved this rebound source identity and extraction boundary.
Approval permits the established Development Rulings-only offline preparation
and representative pilot calibration; provider readiness still requires fresh
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
use `review_required` when necessary. Parent headings are context, never atoms.
Every `exact_source_text` is a byte-for-byte contiguous
target-block substring that occurs exactly once. After JSON decoding it contains actual target-block
characters, never literal backslash Unicode-escape spellings.
No `exact_source_text` may cross an authored semicolon. Split semicolon-delimited
clauses into separate atoms, including coordinated examples in ordinary prose.
Restore an omitted later-clause subject only in `normalized_claim` from its
adjacent coordinated clause. Repeated spans expand through nearest
semicolon-free source boundary. Include interrupting markup or split the atom.

Obey `required_disposition`, `allowed_dispositions`, and `minimum_atoms`;
`no_substantive_claim` requires empty `atoms`. Structural headings, labels, table headers,
delimiters, and document-control metadata carry no substantive atom. Dependent
list items may use necessary explicit subject/status/scope/condition/connective
from indivisible-adjacent lead-in/heading; lead-ins may not import body names,
members, or assertions.

For each substantive table row, cover every nonempty semantic cell. Separate
independent properties, functions, effects, examples, interpretations, stages,
actions, and results. Combine qualifying/indivisible cells; preserve
categorical-mapping endpoints.
Ground each headed cell under its header; never infer a relationship between
adjacent cells. Table spans—cell or whole-row—split at authored semicolons;
none crosses one.
Copy every authored slash into the normalized claim; never replace it with a word unless the source defines that meaning.
Each independent table-cell assertion requires exact source text from its own
cell; never ground a ruling or consequence only in another cell.

Preserve provisional, historical, rejected, example, negative, conditional,
scope, ownership, and authority qualifiers. Use `review_required` instead of
guessing. Never repair source text or invent identifiers, statuses, owners, or
authorities.

## Output check

Return schema-bound JSON only after verifying exactly
`required_target_disposition_count` dispositions. Kind `atoms` requires nonempty
`atoms`; all other kinds require empty `atoms`. Every atom needs bound IDs/stream,
exact source text, normalized claim, and source-faithful kind.
Derive each proposal ID from target block ID plus local atom ordinal;
proposal IDs must remain source-unique.
