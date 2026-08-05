# MEDIAN source-bounded atomic extraction

Allowed source: `M050-SRC-DISCOVERY-TIME-PROGRESSION-001`
Allowed streams: `evidence_game_semantic`

The input-ordered disposition block-ID set must exactly equal `target_blocks`:
none missing, repeated, or partial.
Disposition neither context nor excluded blocks. Use only `SOURCE_BLOCKS`.

Use only supplied IDs; never samples, placeholders, or dummy `x`.
Unresolved targets get `review_required`; never abbreviate the target set.

## Approved content/provenance boundary

# MEDIAN v0.5.0 Discovery, Time, Movement, and Civic Progression Content/Provenance Identity Card v0.1

Date: 2026-08-05
Status: `APPROVED`
Lifecycle state: `identity_card_approved`
Author/root of authority: Asa Wember

## Source identity and authority

| Field | Bound value |
|---|---|
| Source ID | `M050-SRC-DISCOVERY-TIME-PROGRESSION-001` |
| Path | `m050/docs/v0.5/specifications/M050_Discovery_Time_Movement_and_Civic_Progression_Specification_v1_0_MEDIANv0_5_0.md` |
| SHA-256 | `4ee2dea9e73c8e0194a9a250d1447e2d3b06202f02ae9c318c64fa501e2a30f8` |
| Source role | `scoped_discovery_time_movement_and_progression_game_specification` |
| Disposition | `source_bounded_atomic_extraction` |
| Allowed stream | `evidence_game_semantic` only |
| Compile position | Ordinal 12; next outstanding source after completed Personal Items |

The registered frozen Markdown is the sole extraction source.

## Status and qualification handling

The source declares BSA-12 through BSA-22 complete for MEDIAN v0.5 and leads
over earlier assumptions where it speaks directly, while leaving population
thresholds and Tier identities controlled elsewhere unless explicitly restated.
It defers specified registries, tuning, recipes, daughter-colony detail, and
memorial presentation, and conditions further edge-case work on a real authored
or implementation requirement. Extraction must preserve this complete,
superseding, qualified, deferred, conditional, negative, and illustrative force.

## Media and exclusions

The registered Markdown contains no embedded media or media-associated caption.
Its tables and textual references are ordinary source text, not media.

Alternate representations and external media are excluded. Document-control
furniture, nonsemantic whitespace, source-position comments, pure structural
headings, table delimiters, and the final document marker use the established
source-agnostic dispositions.

## Extraction boundary

Extract only game-semantic evidence present in the registered Markdown. Do not
import, consult, summarize, or apply external sources, and do not adjudicate
cross-source authority. The source's own references to other work remain
source-bounded claims in their appropriate chunks.

Source-bounded candidate acceptance is not semantic acceptance, mapping,
reconciliation, canonization, compiled prose, or permission to begin another
source, later compile stage, or Google Sheets work.

## Approval boundary

Asa Wember approved this source identity and extraction boundary. Approval
permits the established Discovery-only offline preparation and representative
pilot calibration; provider readiness still requires validated frozen bindings,
completed offline and replay gates, sequential review, and sufficient budget.

## Extraction contract

Separate claims. Exact spans uniquely ground core assertions. Keep a coordinated subject list with its shared predicate in one atom
unless each split atom has a contiguous span containing both its subject and predicate. A subject or label alone never grounds an
imported predicate. Normalized claims may add explicit, unambiguous qualifiers from the
target block or its supplied `parent_heading`; other context never supplies qualifiers or exact text. A parent heading may qualify
its body but is not an atom. Every `exact_source_text` is
a byte-for-byte contiguous target-block substring that occurs exactly once. After JSON decoding it contains actual target-block
characters, never literal backslash Unicode-escape spellings.
Expand repeated or nested terms with adjacent text until unique.
Include interrupting markup or split the atom.

Obey `required_disposition`, `allowed_dispositions`, and `minimum_atoms`;
`no_substantive_claim` requires empty `atoms`. Structural headings, labels, table headers,
delimiters, and document-control metadata carry no substantive atom. Never make
a label a tautological topic claim or use structural context to omit a
dependent substantive target.

For each substantive table row, cover every nonempty semantic cell. Separate
independent properties, functions, effects, examples, interpretations, stages,
actions, and results. Combine cells only when one qualifies
another or the relationship is indivisible. Preserve both endpoints of
categorical mappings.
Ground each headed cell under its header; never infer a relationship between
adjacent cells. No exact span crosses a semicolon; each side gets its own atom.
Copy every authored slash into the normalized claim; never replace it with a word unless the source defines that meaning.
Each independent table-cell assertion requires exact source text from its own
cell; never ground a ruling or consequence only in another cell.

Preserve provisional, historical, rejected, example, negative, conditional,
scope, ownership, and authority qualifiers. Use `review_required` instead of
guessing. Never repair source text or invent identifiers, statuses, definitions,
owners, or authorities.

## Output check

Return schema-bound JSON only after verifying exactly
`required_target_disposition_count` dispositions. Kind `atoms` requires nonempty
`atoms`; all other kinds require empty `atoms`. Every atom needs supplied source/target block IDs, an
allowed stream, exact source text, concise normalized claim, and source-faithful
claim kind. Derive each proposal ID from target block ID plus local atom ordinal;
proposal IDs must remain source-unique.
