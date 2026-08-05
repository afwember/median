# MEDIAN source-bounded atomic extraction

Allowed source: `M050-SRC-GUEST-001`
Allowed streams: `evidence_game_semantic`

The disposition block-ID set must exactly equal `target_blocks`: no missing or repeated IDs.
Context blocks receive none;
excluded blocks are omitted. Use only `SOURCE_BLOCKS`; import nothing else.

Use supplied source/request IDs; invent no IDs or metadata. Never emit samples, or dummy values such as `x`.
For unresolved targets, emit `review_required` dispositions; never abbreviate the target set.

## Approved content/provenance boundary

# MEDIAN v0.5.0 Guest Content/Provenance Identity Card v0.1

Date: 2026-08-04
Status: `APPROVED`
Lifecycle state: `identity_card_approved`
Author/root of authority: Asa Wember

## Source identity and authority

| Field | Bound value |
|---|---|
| Source ID | `M050-SRC-GUEST-001` |
| Path | `m050/docs/v0.5/specifications/M050_Guest_Citizen_Specification_v2_0_MEDIANv0_5_0.md` |
| SHA-256 | `ecedad99eb425c573149c9a1e33bcce0ee89422f76a9e1b25e4f7387af14f15f` |
| Source role | `dedicated_guest_citizen_game_specification` |
| Disposition | `source_bounded_atomic_extraction` |
| Allowed stream | `evidence_game_semantic` only |
| Compile position | Ordinal 10; next outstanding source after completed Population |

The registered frozen Markdown is the sole extraction source.

## Status and qualification handling

The source declares v0.5 Guest architecture and working-roster rules while
separately marking specified implementation values and questions as tunable or
open and its named example Citizens as exemplars rather than mandatory campaign
occupants. Extraction must preserve the source's exact canonical, fixed,
reference, optional, illustrative, exemplary, tunable, open, may, normally,
negative, superseded, and unresolved force.

## Media and exclusions

The registered Markdown contains no embedded image, audio, video, external URL,
repository-media reference, or media-associated caption. HTML and Markdown
tables and textual examples are source text, not media.

All alternate PDF and DOCX representations are excluded. Do not use their
binaries, layout, images, OCR or pixel-contained text, metadata, or text.
Document-control furniture, Contents navigation, nonsemantic whitespace,
source-position comments, pure structural headings, table delimiters, and the
final document marker use the established source-agnostic dispositions.

## Extraction boundary

Extract only game-semantic evidence present in the registered Guest Markdown.
Do not import, consult, summarize, or apply external sources, and do not
adjudicate cross-source authority. The source's own precedence material remains
in its appropriate source chunk and is not duplicated here.

Source-bounded candidate acceptance is not semantic acceptance, mapping,
reconciliation, canonization, compiled prose, or permission to begin another
source, later compile stage, or Google Sheets work.

## Approval boundary

Asa Wember approved this source identity and extraction boundary. Approval
permits the established Guest-only offline preparation and representative pilot
calibration; provider readiness still requires validated frozen bindings,
completed offline and replay gates, sequential review, and sufficient budget.

## Extraction contract

Separate independent claims; keep dependent qualifications with their claims.
Every `exact_source_text` must be a byte-for-byte contiguous target-block
substring after JSON decoding. Exact spans retain
markup and escaping and must occur exactly once in the block. If claim text is
repeated or nested inside another term, expand the span with adjacent source
text until it is unique. If markup interrupts prose, include it or split the atom.

Obey target constraints. `required_disposition` fixes `kind`; for
`no_substantive_claim`, emit empty `atoms`. `allowed_dispositions` restricts
kind; `minimum_atoms` is a floor. Pure structural headings, labels, table headers, delimiters, and
document-control metadata carry no substantive atom; never turn a label into a tautological
claim that its section discusses the announced topic. Structural context never
excuses a dependent substantive target from receiving its own disposition.

For every substantive table row, cover every nonempty semantic cell. Ground
independent properties, functions, effects, examples, interpretations, stages,
actions, and results as separate atoms. Combine cells only when one qualifies
another or the relationship is indivisible. Preserve both endpoints of
categorical mappings.
Ground each headed cell under its header; never infer a relationship between
adjacent cells. Semicolon-separated effects require separate atoms.
Each independent table-cell assertion requires exact source text from its own
cell; never ground a ruling or consequence only in another cell.

Preserve provisional, historical, rejected, example, negative, conditional,
scope, ownership, and authority qualifiers. Use `review_required` instead of
guessing. Never silently repair source text or invent identifiers, statuses,
definitions, owners, or authorities.

## Output check

Return schema-bound JSON only after verifying its disposition count equals
`required_target_disposition_count`. For kind `atoms`, `atoms` must be nonempty;
for every other kind, `atoms` must be empty. Every atom must use supplied source and target block IDs, an
allowed stream, exact source text, a concise normalized claim, and a
source-faithful claim kind. Derive each proposal ID from its target block ID plus
a local atom ordinal so proposal IDs remain unique across the source.
