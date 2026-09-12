# Authorial Grammar source-bounded extraction prompt v0.5

Status: `OFFLINE_TEST_ONLY`  
Provider authority: none  
Allowed source: `M050-SRC-AUTHORIAL-GRAMMAR-001` only  
Allowed stream: `evidence_authorial_rule` only

## Task and boundary

Convert every supplied target block into exactly one grounded disposition using only `SOURCE_BLOCKS`. Context blocks guide interpretation but never receive dispositions. Do not import background knowledge, prior atoms, other MEDIAN sources, mapping, reconciliation, canonization, or inferred authority.

Authorial-rule evidence may cover prose display, orthography, grammar, semantic typography, convention status, authoring guidance, and authorial lint. Game mechanics, MSID validity, operator meaning, source precedence, reconciliation, canonization, and publication implementation are outside this extraction. Preserve provisional, prospective, derived, example, historical, negative, conditional, scope, ownership, and authority qualifiers.

## Mandatory target coverage

The response is invalid unless `dispositions` contains exactly `required_target_disposition_count` entries and its block IDs match the supplied `target_blocks` block IDs exactly, with no omission, duplication, or extra ID. Check this correspondence before returning JSON.

Every target remains independently disposition-required even when it is an example body, code fence, list, quotation, or table row governed by a nearby lead-in or pure label. Marking a pure label `no_substantive_claim` never removes or excuses its dependent target body. If a target cannot safely produce grounded atoms, return `review_required`; never omit it.

## Lean structural evidence rules

1. A Markdown table header row and delimiter row are layout metadata. Return `no_substantive_claim` with an empty `atoms` array for both. Substantive table body rows remain eligible and must use their lead-in and header context.
2. A target carrying `required_disposition: no_substantive_claim` is a mechanically identified pure example or polarity label such as `Example:`, `Examples:`, `Prefer:`, `Not:`, `Correct:`, `Incorrect:`, or `Avoid:`. Return exactly that disposition with an empty `atoms` array. Never create an atom merely stating that an example follows.
3. Do not extend rule 2 to a substantive sentence that happens to end in a colon. A sentence such as “Plural species nouns take plural agreement:” states a rule and remains eligible.

These rules are generic and must not be applied only to a named block.

## Atomicity and grounding

Split independent rules into separate atoms and keep dependent qualifications with the claims they qualify. Copy `exact_source_text` exactly and contiguously from the target block. Never repair source text or invent identifiers, statuses, definitions, owners, or authorities. Use `review_required` rather than guessing.

Every disposition must include `atoms`. It must be nonempty only for kind `atoms` and empty otherwise. Never use kind `excluded`; exclusions were applied offline.

## Output

Return JSON only under the bound schema. Every atom must use the supplied source ID and block ID, stream `evidence_authorial_rule`, a unique proposal ID, exact source text, a concise source-faithful normalized claim, and an appropriate authorial claim kind.

`SOURCE_BLOCKS` is inserted mechanically for an authorized request. No source text is embedded in this offline template.
