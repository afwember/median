# MEDIAN source-bounded atomic extraction

Allowed source: `M050-SRC-PERSONAL-ITEMS-001`
Allowed streams: `evidence_game_semantic`

The disposition block-ID set must exactly equal `target_blocks`: no missing or repeated IDs.
Disposition neither context nor excluded blocks. Use only `SOURCE_BLOCKS`.

Use supplied IDs; invent nothing. Never emit samples, or dummy values such as `x`.
Unresolved targets get `review_required`; never abbreviate the target set.

## Approved content/provenance boundary

# MEDIAN v0.5.0 Personal Items Content/Provenance Identity Card v0.1

Date: 2026-08-05
Status: `APPROVED`
Lifecycle state: `identity_card_approved`
Author/root of authority: Asa Wember

## Source identity and authority

| Field | Bound value |
|---|---|
| Source ID | `M050-SRC-PERSONAL-ITEMS-001` |
| Path | `m050/docs/v0.5/specifications/M050_Personal_Items_Focus_and_Expedition_Equipment_Specification_v1_0_MEDIANv0_5_0.md` |
| SHA-256 | `b29bb2c0b85635fb50c47828ad41d7c406d30a5e4f9928b9f483ad4b3b220455` |
| Source role | `dedicated_items_focus_and_equipment_game_specification` |
| Disposition | `source_bounded_atomic_extraction` |
| Allowed stream | `evidence_game_semantic` only |
| Compile position | Ordinal 11; next outstanding source after completed Guest |

The registered frozen Markdown is the sole extraction source.

## Status and qualification handling

The source declares a complete v0.5 baseline under its source label `BSA-11`
and says it supersedes exploratory development-thread rulings wherever it
speaks directly. It separately marks specified registries, aftermath,
continuous effects, Home Focus conditions, Node Study/Render detail, and final
Supply naming and recipes as deferred, and conditions later edge-case work on
a real authored or implementation requirement. Extraction must preserve the
source's exact complete, baseline, superseding, current, deferred, conditional,
normally, may, negative, illustrative, and unresolved force.

## Media and exclusions

The registered Markdown contains no embedded media or media-associated caption.
Its tables and textual references to interface images or possible future image
generation are ordinary source text, not media.

Alternate representations and external media are excluded. Document-control
furniture, nonsemantic whitespace, source-position comments, pure structural
headings, table delimiters, and the final document marker use the established
source-agnostic dispositions.

## Extraction boundary

Extract only game-semantic evidence present in the registered Personal Items
Markdown. Do not import, consult, summarize, or apply external sources, and do
not adjudicate cross-source authority. The source's own references to other
work remain source-bounded claims in their appropriate chunks.

Source-bounded candidate acceptance is not semantic acceptance, mapping,
reconciliation, canonization, compiled prose, or permission to begin another
source, later compile stage, or Google Sheets work.

## Approval boundary

Asa Wember approved this source identity and extraction boundary. Approval
permits the established Personal Items-only offline preparation and
representative pilot calibration; provider readiness still requires validated
frozen bindings, completed offline and replay gates, sequential review, and
sufficient budget.

## Extraction contract

Separate claims; retain dependent qualifications.
Every `exact_source_text` must be a byte-for-byte contiguous target-block
substring after JSON decoding. Exact spans retain
markup and escaping and must occur exactly once in the block. If claim text is
repeated or nested inside another term, expand the span with adjacent source
text until it is unique. If markup interrupts prose, include it or split the atom.

Obey target constraints. `required_disposition` fixes `kind`; for
`no_substantive_claim`, emit empty `atoms`. `allowed_dispositions` restricts
kind; `minimum_atoms` is a floor. Structural headings, labels, table headers, delimiters, and
document-control metadata carry no substantive atom; never turn a label into a tautological
claim that its section discusses the announced topic. Structural context never
excuses a dependent substantive target from receiving its own disposition.

For every substantive table row, cover every nonempty semantic cell. Ground
independent properties, functions, effects, examples, interpretations, stages,
actions, and results as separate atoms. Combine cells only when one qualifies
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

Return schema-bound JSON only after verifying its disposition count equals
`required_target_disposition_count`. For kind `atoms`, `atoms` must be nonempty;
for every other kind, `atoms` must be empty. Every atom needs supplied source/target block IDs, an
allowed stream, exact source text, concise normalized claim, and source-faithful
claim kind. Derive each proposal ID from target block ID plus local atom ordinal;
proposal IDs must remain source-unique.
