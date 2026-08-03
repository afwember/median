# Authorial Grammar source-bounded extraction prompt v0.2

Status: `OFFLINE_TEST_ONLY`  
Provider authority: none  
Allowed source: `M050-SRC-AUTHORIAL-GRAMMAR-001` only  
Allowed stream: `evidence_authorial_rule` only

## Task

Convert the supplied Authorial Grammar target blocks into grounded, atomic authorial-rule proposals. Use only the text inside `SOURCE_BLOCKS`. Do not use background knowledge, prior atoms, other MEDIAN sources, or inferred cross-source authority.

`SOURCE_BLOCKS` contains two separate arrays:

- `context_blocks` provide local headings or examples for interpretation only. Never return a disposition for a context block.
- `target_blocks` are the complete output target set. Return exactly one disposition for every target block, in the supplied order, with no omissions, additions, or duplicates.

The approved identity boundary is:

- Initial Caps for Defined Nouns;
- ALL CAPS for experiential verbs and Core-Species operators;
- prose display, orthography, grammar, semantic typography, convention status, authoring guidance, and authorial lint may be proposed as authorial-rule evidence;
- game mechanics, MSID path validity, operator meaning, source precedence, reconciliation, canonization, and final publication implementation are not owned by this extraction;
- examples and tables retain their local function and do not independently establish game mechanics or ontology;
- `PROVISIONAL`, prospective, derived, example, historical, negative, and context qualifiers must remain explicit; and
- the Phonebook plate is derived and non-independent, not a second authority.

## Atomicity and grounding

Split independent rules into separate atoms. Keep dependent qualifications with the rule they qualify. Copy `exact_source_text` exactly and contiguously from the named target block. Never silently repair or paraphrase the evidence span.

Use `review_required` rather than guessing when ownership, status, scope, example polarity, table structure, or atomic boundaries remain uncertain. Do not create identifiers, statuses, definitions, or authorities absent from the supplied block.

Every disposition must include an `atoms` array. For kind `atoms`, the array must contain one or more atoms. For every other kind, it must be empty. Never use kind `excluded`; exclusions have already been applied offline.

## Output

Return JSON only, conforming to the bound response schema. Every atom must use:

- the supplied source ID;
- its supplied block ID;
- stream `evidence_authorial_rule`;
- a unique proposal ID;
- exact source text;
- a concise normalized authorial claim; and
- an authorial claim kind that describes the source statement without canonizing it.

`SOURCE_BLOCKS` will be inserted mechanically below this line for an authorized request. No source text is embedded in this offline prompt template.
