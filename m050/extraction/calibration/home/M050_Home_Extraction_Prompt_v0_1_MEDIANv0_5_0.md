# MEDIAN source-bounded atomic extraction

Allowed source: `M050-SRC-HOME-001` only  
Allowed streams: `evidence_game_semantic`

Convert every supplied target block into exactly one grounded disposition.
Context blocks may guide interpretation but never receive dispositions.
Excluded blocks are omitted offline. Use only `SOURCE_BLOCKS`; do not import
other MEDIAN sources, prior atoms, background knowledge, mapping,
reconciliation, canonization, or inferred authority.

## Approved provider-safe content boundary

This source is the dedicated Home and Colony game-semantic specification.
Extract Home-local rules, definitions, procedures, constraints, qualified
reference implementations, examples, non-goals, and acceptance conditions as
source-bounded game-semantic evidence.

Preserve source-declared status and modal force. A label such as `canonical` or
`Canon working specification` remains a source claim rather than automatic
semantic acceptance. Preserve `non-canonical`, reference, provisional,
recommended, normally, may, should, example, negative, conditional, scope, and
ownership qualifiers. Do not assign or validate MSIDs, resolve cross-source
precedence, infer authorial-style rules from typography, or claim that a
recommended interface or reference calculation is implemented.

All embedded-media occurrences and their associated captions or labels are
excluded offline. They are absent from `SOURCE_BLOCKS`. Do not infer, request,
reconstruct, summarize, transcribe, or interpret any image, visual content,
pixel-contained text, alt/title text, caption, label, or external artwork.

## Extraction contract

Split independent claims into separate atoms and keep dependent qualifications
with the claim they qualify. Copy every `exact_source_text` exactly and
contiguously from its target block. Use `review_required` instead of guessing.
Never silently repair source text or invent identifiers, statuses, definitions,
owners, or authorities.

Return JSON only under the bound response schema. `atoms` must be nonempty only
when kind is `atoms`; it must be empty otherwise. Every atom must use the
supplied source ID, its target block ID, one allowed stream, a unique proposal
ID, exact source text, a concise normalized claim, and a source-faithful claim
kind.
