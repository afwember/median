# MEDIAN v0.5.0 Reconciliation Manual-Triage Plan

## Purpose

Before model-assisted reconciliation begins, use direct human authorial knowledge to remove obviously obsolete, administrative, out-of-scope, or otherwise nonparticipating atoms from the active reconciliation workload. The purpose is to reserve GPT-5.6 judgment for genuine semantic relationships, conflicts, and uncertainties.

This is a bounded operation within reconciliation, not a new permanent phase. It should reduce model work and process complexity rather than introduce another supervisory layer.

## Governing distinction

Accepted extraction candidates preserve what each frozen source says. They are evidence, not final canon, and must remain unchanged.

Manual “purging” therefore means excluding an atom from active v0.5.0 reconciliation. It does not mean deleting the atom from its accepted extraction candidate. This preserves the complete source record, makes human decisions reversible, and prevents any need to repeat extraction.

Atomization was a useful prerequisite for this work. Before extraction, review could only reject whole documents or sections and could easily discard an important statement embedded in obsolete material. The extracted atom is now the appropriate unit for authorial triage.

## Minimal implementation

Create one source-agnostic local Python review program after atomic extraction has completed and the Compile Worker has formally Stopped down.

The program reads accepted candidate JSONL files directly and presents atoms in source order. For each atom it displays:

- source ID and human-readable source name;
- source location, block, or chunk provenance;
- exact source text as the primary review material;
- normalized claim as secondary material when available;
- claim kind or existing semantic class; and
- preceding and following atoms from the same source block on request.

The initial interface should require no model call and use single-key decisions without requiring Enter:

- `Y` — retain for reconciliation;
- `N` — authorially exclude from active v0.5.0 reconciliation;
- `?` — uncertain and specifically eligible for GPT-5.6 review;
- `U` — undo the preceding decision; and
- `Q` — save and quit.

The program must save after every decision or small bounded group, resume exactly where review stopped, and report source-level and corpus-level progress.

### Optional exclusion reason

If the added keystroke proves useful rather than burdensome, an `N` decision may record one compact reason:

- `O` — obsolete or superseded;
- `A` — administrative or provenance-only rather than game content;
- `S` — outside MEDIAN v0.5.0 scope;
- `D` — true duplicate; or
- `X` — other authorial exclusion.

These are audit reasons, not a new game taxonomy. They must not expand into a classification system.

## Canonical representation

Maintain exactly one canonical human-disposition record with one current row per reviewed atom. Git supplies its history. Do not generate or preserve a second filtered copy of the atom corpus.

At reconciliation-call time, the deterministic caller combines:

```text
accepted atoms + canonical human dispositions -> permitted GPT-5.6 payload
```

The permitted payload is transient. Accepted extraction remains the sole source-evidence representation; the human-disposition record is the sole authority for manual reconciliation eligibility.

The review program should be the sole writer of the human-disposition record. The reconciliation caller and guard should consume it directly.

## Group review and deterministic reduction

Reviewing approximately ten thousand atoms strictly one by one could require substantial human time:

- three seconds per atom: roughly eight hours;
- five seconds per atom: roughly fourteen hours; and
- ten seconds per atom: roughly twenty-eight hours.

The program should therefore support cautious group presentation without automatic semantic deletion:

- present all atoms from one source block together;
- group exact normalized-text duplicates into one review unit while retaining every provenance link;
- permit whole-block exclusion only after displaying the exact atom count and boundaries;
- queue metadata and document-control claims together for rapid review;
- queue explicit supersession and historical-comparison claims together; and
- permit immediate drill-down whenever a group contains mixed material.

Deterministic grouping proposes review units. It does not decide authority.

Cross-source duplicates should ordinarily be consolidated for presentation rather than deleted. Agreement across sources may be useful reconciliation evidence. A later model payload may transmit one compact claim with its complete supporting source-ID list instead of retransmitting identical wording.

## Permitted model-free operations

The local program may perform:

- exact-text and normalized-text equivalence detection;
- whitespace, punctuation, and capitalization normalization;
- consolidation of repeated provenance references;
- grouping by source, block, and source order;
- identification of legacy atoms that already contain MSID candidates or semantic status;
- display queues based on existing claim kinds; and
- deterministic coverage accounting proving that every atom has a human or model disposition.

Existing claim-kind labels are advisory only. The corpus contains heterogeneous claim-kind vocabularies, and extraction labels are not semantic-authority decisions. Examples, non-goals, negative rules, acceptance tests, and similar classes may contain important constraints and must not be automatically excluded.

## Possible second authorial operation

After the first `Y` / `N` / `?` pass, measure how much GPT-5.6 work remains before adding further machinery.

If the remaining workload justifies it, add one additional authorial disposition:

- `C` — directly confirmed as current MEDIAN v0.5.0 authority.

A confirmed atom becomes an authoritative reconciliation anchor. GPT-5.6 need not decide whether it survives, but may still identify related, supporting, or conflicting atoms around it.

Do not add this operation speculatively. Add it only if the first-pass measurement shows that direct human confirmation would eliminate a substantial additional body of model judgment.

## Expected cost effect

The preliminary untriaged estimate for disciplined GPT-5.6 Sol reconciliation is approximately $40–$70 at standard API rates, with a conservative authorization ceiling of $100.

Approximate planning ranges after manual reduction are:

| Workflow | Estimated GPT-5.6 Sol standard API cost |
|---|---:|
| No manual triage | $40–$70 |
| `Y` / `N` / `?` review plus deterministic grouping | $25–$45 |
| Substantial authorial exclusion and direct rulings | $15–$35 |
| Reduced workload using Batch or Flex rates | Potentially about $10–$25 |

Savings will not be perfectly linear because the surviving material will contain the hardest conflicts and may require more reasoning per atom. Nevertheless, removing an obsolete atom before reconciliation prevents it from being reread during mapping, comparison, retries, and final verification.

## Conservation of System evaluation

This proposal is justified under Conservation of System only if it remains small:

- one source-agnostic review program;
- one canonical human-disposition representation;
- no new agent or supervisory role;
- no persistent filtered corpus;
- no new semantic taxonomy;
- no automatic authority decisions; and
- direct replacement of model relevance decisions with human authorial decisions.

The mechanism transforms canonical evidence into bounded reconciliation eligibility and enforces complete disposition coverage. It therefore performs a necessary function. If it grows into a collection of passes, ledgers, taxonomies, or derived corpora, it has violated its purpose.

## Recommended phase-boundary sequence

1. Complete lossless atomic extraction of the compile-scope corpus.
2. Complete the formal Worker Stopdown.
3. Retool the active phase profile for reconciliation in discussion with the author.
4. Implement and test the single source-agnostic manual-review program.
5. Pilot it on one representative source or bounded source section.
6. Inspect the pilot output and human review burden before releasing corpus-wide use.
7. Conduct the authorial `Y` / `N` / `?` sweep, using cautious block-level batching.
8. Measure the retained, excluded, and uncertain populations.
9. Decide whether direct `C` confirmation is justified by the measured workload.
10. Design the smallest GPT-5.6 reconciliation packets around only the surviving relationships and uncertainties.

The intended result is not to ask GPT-5.6 to understand everything. It is to ask GPT-5.6 only about relationships, conflicts, and uncertainties that genuinely require model judgment.
