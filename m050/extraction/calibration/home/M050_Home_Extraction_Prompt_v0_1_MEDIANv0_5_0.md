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
with the claim they qualify. Every `exact_source_text` must be a byte-for-byte
contiguous substring selected from its target block after JSON decoding; copy a
source span verbatim rather than reconstructing, cleaning, or reformatting it.
Preserve every literal backslash and every HTML opening and closing tag. Never
render HTML, strip tags, convert tags to Markdown, or change source escaping.
For markup-backed or backslash-escaped claims, copy the whole target block when
that is the safest exact contiguous span. Use `review_required` instead of guessing.
Never silently repair source text or invent identifiers, statuses, definitions,
owners, or authorities.

Pure table-header rows and table-delimiter rows are structural rather than
substantive. Return `no_substantive_claim` with an empty `atoms` array for those
targets; extract claims only from substantive table-body rows. For each
substantive table-body row, preserve the claims and relationships expressed by
all cells; do not extract only the final prose cell or omit a row's categorical
mapping between columns. Before returning a table-body disposition, check every
nonempty cell for coverage. A row is not automatically one atom: when separate
semantic columns independently specify properties, functions, effects,
eligibilities, examples, interpretations, or other claims about the row subject,
create a separate atom for each independent column claim. Keep cells together
only when they jointly form one indivisible relationship or when one cell merely
qualifies another. When columns map a prior category to a reworked
category, at least one grounded mapping atom must name both exact cell values;
naming only the reworked category does not cover the prior-category cell. Do
not fuse all row content into that mapping atom: create separate atoms for each
independent consequence sentence or clause expressed by the remaining cells.
Do not also create a separate atom that merely restates either category already
named by the complete mapping atom. Every prior-to-reworked mapping row must
use one mapping-only atom naming the two categories and one or more separate
consequence-only atoms; never include consequence content in the mapping atom,
even when the row contains only one consequence sentence.

Pure headings, section labels, and topic labels that only announce what follows
do not assert a source claim. Return `no_substantive_claim` for them; never turn
a label into a tautological atom saying that the section discusses its topic.

Before returning, verify that every target block ID appears exactly once, no
context block receives a disposition, every `atoms` disposition has at least
one atom, and every other disposition has an empty `atoms` array. Return JSON
only under the bound response schema. Every atom must use the supplied source
ID, its target block ID, one allowed stream, a unique proposal ID, exact source
text, a concise normalized claim, and a source-faithful claim kind.
