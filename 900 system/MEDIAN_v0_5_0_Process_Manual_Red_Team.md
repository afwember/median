# Red-Team Review: MEDIAN v0.5.0 Hardened Compile Process Manual

**Target document:** `MEDIAN_v0_5_0_Hardened_Compile_Process_Manual.md` (prepared 2026-08-02)
**Review type:** Conceptual gap analysis — not a copy edit, not an implementation review
**Reviewer stance:** Adversarial. Assumes the process is well-intentioned and looks for where it breaks anyway.

---

## How to read this

The document is internally coherent and the diagnosis in §2 is sound. The separations it enforces (identity from filename, extraction from reconciliation, evidence from mapping) are the right separations, and the error-correction hierarchy in §14 is the strongest part of the design.

The findings below are ordered by how much damage they cause if left unaddressed. Findings 1–4 are structural: they concern things the process needs in order to terminate at all. Findings 5–12 are mechanism gaps — places where a rule is asserted but nothing implements or verifies it. Findings 13–16 are smaller. A closing section lists questions only the author can answer.

---

## 1. The hardest stage is the least engineered

**Gap.** Stage 2 (extraction) receives a work-order contract, dual chunk limits, calibration design, a block-disposition ledger, deterministic validation, retry limits, and a regression corpus. Stage 5 (reconciliation) receives a bulleted list of things it determines.

This is backwards relative to risk. Extraction is the stage that already failed, so it got hardened. But extraction failures are *loud* — a bad quotation doesn't ground, a missing disposition is countable, a truncated response hits a ceiling. Reconciliation failures are *silent*. If Stage 5 never considers an atom, nothing detects it. There is no grounding check for "did this decision account for all relevant evidence," because the relevant set is not enumerable in advance.

**Why it matters.** §19's first-listed fear — "do not let a valid unique developmental rule disappear because a later source is silent" — is guarded almost entirely at Stages 5 and 6, the two least specified stages in the document. The process is most rigorous where the risk is most detectable and least rigorous where the risk is most consequential.

**Suggested resolution.** Stage 5 needs its own version of the Stage 2 apparatus:

- A **bundle contract**: for a given subject, which evidence atoms enter the request, derived by an explicit deterministic rule (MSID match, alias set, term co-occurrence), and a record of the bundle's composition and hash.
- A **completeness argument for bundles**: some mechanical check that an atom mapped to subject X cannot be absent from X's reconciliation bundle. Right now, atom-to-bundle assignment appears to be assumed rather than proven.
- **Per-subject disposition accounting**, mirroring block-disposition accounting: every atom in the bundle gets exactly one disposition, and every mapped atom belongs to at least one bundle.
- Chunk/size limits, calibration, and cost projection for reconciliation requests, since these bundles will be much larger than extraction chunks.
- An **unmapped-atom sweep**: atoms with Layer M status `unmapped` / `ambiguous` / `invalid` are by definition in no subject bundle, so they will silently never be reconciled unless a dedicated pass handles them. The document does not currently have this pass.

---

## 2. Human review capacity is the binding constraint and it is unbudgeted

**Gap.** The process carefully budgets one resource (provider dollars — §15, a cost CSV, a ledger, a `$0.00` default cap) and does not budget the other (human attention). Yet almost every acceptance path routes through a human:

- Stage 3 semantic review: "review every returned atom and every exclusion."
- Stage 5: "every substantive claim ... must receive a disposition."
- Stage 6: every relevant v0.4.6 baseline subject classified.
- §20: "review the 123 likely compound records rather than splitting mechanically," "reconstruct Human Rulings from its 41 ruling sections."
- §14 level 5 and Layer M status `human_required`: the escape hatch from every unresolvable state is a human ruling.

**Scale check from the document's own numbers.** 913 grounded records from 130 chunks ≈ 7 records/chunk, from four sources. There are roughly 15–17 more extractable sources. A plausible corpus is 3,000–4,000 evidence atoms, each requiring mapping review, feeding a reconciliation stage over hundreds of subjects, feeding a baseline audit over the whole v0.4.6 GDD.

At even one minute of genuine attention per atom, Stage 3 alone is 50–65 hours. Stages 4–6 are additive and involve harder judgments.

**Why it matters.** The likeliest failure mode of this process is not a bad extraction. It is abandonment, or — worse — quiet rule-bending under fatigue, which reintroduces exactly the drift §2 describes, but this time inside a system that *looks* rigorous. A process whose safety depends on uniform human diligence across ~4,000 items has an unstated reliability assumption.

**Suggested resolution.**

- Add a **human-effort projection** alongside the cost projection in Stage 1. Estimated review items per source, not just tokens.
- Introduce **risk tiering**. Rigor is currently uniform across all 24 sources, but they are not equally consequential. "Ecological Influences" (subsidiary) and "Governing Philosophy" (constitutional) get the same treatment. Define a reduced-rigor tier — e.g. statistical sampling of atoms rather than 100% review — for sources whose failure modes are low-impact, and reserve exhaustive review for constitutional, ontology, ruling, and core-mechanic sources.
- Define **what a review pass actually is**, so it can be sized: which fields the reviewer checks, what a reviewer is allowed to skim, and what triggers escalation from skim to full read.

---

## 3. No definition of done, and at least one unbounded loop

**Gap.** The document defines acceptance criteria per artifact (§18) but never defines a terminal condition for the corpus. Several rules are individually correct and jointly non-terminating:

- §4.4: absence is not retirement — unexplained absences become open questions.
- §4.5: uncertainty remains visible — unresolved states persist rather than resolving.
- §9 Stage 6: "An unexplained absence reopens Stage 5."

Stage 6 reopening Stage 5 has no iteration bound and no convergence argument. If Stage 5 could not resolve a subject the first time, the second pass has no new information unless a human ruling was issued in between — so the loop terminates only via human rulings, which returns to Finding 2.

**Why it matters.** Compile acceptance (§18) requires "the v0.4.6 survivorship and gap audit is complete." If "complete" means "no unresolved subjects," the compile may never be authorized. If it means "every subject has *a* disposition, including `unresolved`," then say so — and then define how many unresolved subjects a shippable v0.5.0 tolerates, and what a compiled document does at the site of an unresolved subject (omit? emit a marked stub? emit the v0.4.6 text with a flag?).

**Suggested resolution.**

- State the **terminal condition** explicitly: v0.5.0 compiles when every subject has a disposition and the unresolved set is either empty or explicitly accepted by the author as a known-gaps list published with the document.
- Add a **loop bound**: Stage 6 may reopen Stage 5 for a subject at most once without a new human ruling; a second reopening escalates to the rulings queue instead.
- Specify **compile behavior for unresolved subjects**, since it is a design decision, not an error condition.

---

## 4. No staleness or invalidation model

**Gap.** §4.6 establishes append-only records. Append-only tells you that old records survive. It does not tell you *which downstream records became wrong* when a new record supersedes an old one.

The document has at least four invalidation sources and no propagation mechanism for any of them:

1. **A new human ruling** contradicts an earlier accepted Layer R decision. Which reconciliations and compiles are now stale?
2. **A source changes** (§4.3: new version, new hash). All Layer E records point at the old hash. Are they void? Carried forward for unchanged blocks? There is no block-level diff-and-carryforward policy — and these are living design documents, actively developed, so this *will* happen.
3. **The MSID vocabulary is re-versioned** (Stage 4 pins a version). Mappings made under v1 are not automatically valid under v2. Nothing requires re-mapping or asserts compatibility.
4. **A global prompt/schema/engine revision** (§14 level 4). Evidence accepted under prompt v1 now coexists with evidence accepted under prompt v2. §14 prohibits source-specific prompt branches — good — but it silently permits *temporal* prompt drift across the corpus, which is the same comparability problem on a different axis. Is a v1-extracted source still acceptable after a v2 revision, or must it be replayed?

**Why it matters.** Without a dependency graph, the process cannot answer "what needs redoing?" after any change — so in practice either everything gets redone (unaffordable) or nothing does (silent corruption of the traceability claim).

**Suggested resolution.** Every accepted record already pins its inputs (source hash, block hash, prompt version, vocab version, upstream IDs). That is enough to build a dependency edge set. Add:

- A **staleness rule**: a record is stale when any pinned input's current version differs from the pinned one.
- A **dirty-marking pass** that runs after any supersession and reports the affected downstream set.
- A **carryforward policy for source re-freeze**: blocks whose hash is unchanged carry their Layer E records forward with a new provenance link; changed and new blocks re-extract; deleted blocks' atoms move to a superseded state rather than vanishing.
- A **prompt-version policy**: state whether cross-version evidence is comparable, and if the answer is "yes for these change classes, no for those," enumerate the classes.

---

## 5. Immutability is asserted but not enforced

**Gap.** The architecture's guarantees rest on append-only, immutable accepted candidates. Nothing in the document enforces this mechanically. The enforcement is convention plus §19's instruction not to do it.

The primary operator is an AI task with file-write access to the repository. Over enough sessions, an "immutable" file will be overwritten — not maliciously, but by a task that decides a small repair is cleaner than a new record. §16 already anticipates that tasks drift from instructions.

**Suggested resolution.** Cheap, high-value:

- A **manifest of accepted-record hashes**, checked by a script that must pass before any stage runs.
- **Hash-chained receipts** (each receipt includes the hash of its predecessor), so deletion or reordering is detectable rather than invisible.
- Filesystem read-only permissions on `accepted/` and `archive/`, with writes going through an explicit append tool.
- A pre-commit or CI check that fails on modification of any file under an immutable path.

This converts "must never happen" (§19) into "cannot happen silently," which is the difference between a policy and a control.

---

## 6. Under-extraction is invisible

**Gap.** Validation proves the model didn't *invent* text (quotation grounding) and didn't *skip blocks* (disposition accounting). It does not prove the model extracted every claim *within* a block. A block containing three claims that returns one grounded atom passes every check in Stage 3.

This is the classic silent failure mode of extraction pipelines, and the document's fear of losing unique rules makes it especially costly here.

**Suggested resolution.** All cheap relative to the existing budget:

- **Claim-density expectation.** Stage 1 already counts claim-bearing blocks for chunk sizing. Compare projected density to realized atom counts and flag low-yield dense regions for targeted review.
- **Differential double-extraction on a sample.** Re-run 3–5% of chunks under a second model or a second temperature and diff the atom sets. Divergence is a direct measure of extraction recall, and it converts an unknown into a tracked number. Cost is bounded and small.
- **Targeted review sampling** aimed at the lowest-yield blocks rather than uniform review, which pairs well with Finding 2's risk tiering.

---

## 7. Exclusions are a one-way loss channel

**Gap.** Material leaves the pipeline at three points and never returns:

- Stage 1 local classification of "obvious document furniture" — heuristic, applied to PDF/DOCX conversions where structure is unreliable.
- Stage 2 exclusion codes issued by the model.
- Identity-card exclusions defined *before* any extraction (see Finding 8).

Stage 3 requires exclusions to be "justified," but justification is reviewed at issue time only. Nothing later audits the excluded set, and the compile audit (§8, Stage 8) checks only that *accepted* records didn't disappear. Anything excluded early is outside every downstream integrity check.

**Suggested resolution.**

- Retain excluded blocks as **first-class records with reason codes**, not as absences.
- Add an **exclusion audit** to acceptance criteria: sample-review of excluded blocks per source, with the sample weighted toward heuristic (Stage 1 local) exclusions, which are the least trustworthy.
- Report **exclusion rate per source** as a review signal. An anomalous rate is diagnostic before anyone reads a single block.

---

## 8. The identity card is a strong prior injected at the earliest, least-informed moment

**Gap.** §3.2 and §4.1 correctly reject filename inference, but the replacement — a content-derived identity card — is a judgment made once, up front, by reading the document holistically. It then constrains everything downstream: allowed streams, exclusions, mixed-status boundaries, "likely subject owners."

That is precisely the kind of plausible-sounding holistic judgment the process distrusts everywhere else, and it is made at the point of *least* evidence — before a single atom has been extracted. If a card wrongly restricts a stream or excludes a region, extraction cannot surface the error, because the card determined what extraction was allowed to see.

**Suggested resolution.**

- Require identity-card claims to **cite specific block IDs** as support, making the card itself auditable evidence rather than a summary.
- Define a **backflow trigger**: Stage 3 review can challenge the card. If N atoms are flagged as belonging to a disallowed stream, or a region's exclusions look wrong, the card is re-opened, re-versioned, and affected extraction re-run. §14 lists "revise the identity card under review" as a correction but specifies no trigger and no downstream consequence.
- Version cards explicitly and pin the card version in every Layer E record (the document implies this in §12; make it a hard requirement with a staleness consequence per Finding 4).

---

## 9. "The model cannot accept its own output" needs a definition of independence

**Gap.** §12 and §19 forbid self-acceptance, and §11 step 15 says "the worker cannot self-accept." But the document never says *who* accepts. In practice the reviewer will often be another AI task — possibly the same model family, given a similar prompt, looking at the same material.

That is not independence in any meaningful sense; it is the same failure distribution applied twice. The separation is nominal unless the document defines what makes a reviewer independent.

**Suggested resolution.** State the acceptance authority explicitly, per stage. Something like: deterministic checks are machine-accepted; semantic review may be model-performed but must be a different model or a materially different prompt with no access to the extractor's reasoning; final acceptance of a candidate is a human act recorded with a receipt. Whatever the answer, the document should name it, because right now a reasonable operator could satisfy the letter of the rule with two instances of the same model and gain nothing.

---

## 10. The root of authority is unnamed, and the authority rules are themselves extracted evidence

**Gap.** Authority is supposed to emerge from evidence: identity cards, Governing Philosophy (constitutional evidence), Human Rulings, and reconciliation. But Governing Philosophy must itself be extracted and accepted *by this process* before it can govern anything, and if Governing Philosophy conflicts with the Human Rulings Ledger about who owns a subject, the resolution is a human ruling.

So the actual root of trust is the author. That is fine and probably correct — but the document presents authority as emergent from the corpus, which obscures a real structural fact and leaves a genuine ambiguity unresolved.

**Related concrete case:** the processing order puts Human Rulings (3) before MSID Grammar (4), but §4.2 says extraction order is not authority order. If the Rulings Ledger and the MSID Grammar disagree about identifier syntax or a semantic class, the document does not say which wins. This is not hypothetical — a rulings ledger accumulated during development is exactly where such overrides live.

**Suggested resolution.** Add a short **precedence statement**: a named default ordering among evidence classes (e.g. explicit human ruling > constitutional > ontology > dedicated specification > bridge > provenance), with the caveat that precedence is defeasible by explicit scoped statements and that ties escalate to a new ruling. Then state plainly that the author is the root of authority and the process serves that authority rather than substituting for it.

---

## 11. There is no process for *issuing* human rulings

**Gap.** The document consumes rulings extensively (a Rulings Ledger source, `human_required` mapping states, level-5 error correction, "need for a new human ruling" in Stage 5, "requiring a ruling" in Stage 6). It has no production side. Missing:

- Where new rulings are written and in what format.
- How they are versioned and how they relate to the existing 41-ruling ledger — new source version? Append to a separate v0.5.0 rulings file?
- Whether a new ruling can retroactively invalidate accepted Layer R records (Finding 4).
- A **standing queue** of open questions with the author as owner.

**Why it matters.** Rulings are the only termination mechanism in the entire process (Finding 3). The one thing that makes the process finish is the one thing that has no defined workflow. Open decisions are also already accumulating in the manual itself — §10 lists "Board Game Manifestation: human selection unresolved" with no owner, no deadline, and no queue entry.

**Suggested resolution.** A ruling record type (ID, date, question, evidence considered, decision, scope, supersedes), an append-only rulings file for v0.5.0, and an open-questions queue surfaced in the progress workbooks and in §20's resumption plan.

---

## 12. Text normalization is the highest-probability concrete failure and is undefined

**Gap.** The entire evidentiary chain depends on exact quotation matching. The sources are PDF and DOCX conversions (§2). That combination is where quote grounding reliably breaks:

curly vs. straight quotes and apostrophes; en/em dashes vs. hyphens; non-breaking and thin spaces; soft hyphens; ligatures (fi, fl); Unicode normalization form (NFC vs. NFD — visually identical, byte-different); footnote/endnote markers embedded mid-sentence; line-wrap artifacts inside table cells; trailing whitespace.

§14 permits "lossless normalization" without defining it. Undefined normalization is how "silently repair an ungrounded quotation" (§19) happens in practice — not as a violation, but as someone reasonably widening a normalizer until the failing case passes, which is exactly the prohibited "broaden a correction rule just to make one example pass."

**Suggested resolution.** Specify a **canonical normalization spec** as a Gate 5 deliverable: named Unicode form, an explicit character-folding map, a whitespace policy, and a rule that normalization is applied identically at freeze time and validation time, with raw bytes always retained. Then add adversarial fixtures for each of the above to the regression corpus. §20's regression corpus is currently defined as "failures already discovered," which is purely backward-looking; these are known-in-advance failures and should be seeded now.

---

## 13. Two different reproducibility claims are conflated

§18 and §22 claim the build is reproducible from pinned inputs. But model calls are non-deterministic. What is actually reproducible is the compile *from preserved responses via replay* — reproducible-from-receipts. A fresh run from sources would produce a different corpus.

Both properties are fine; only one is being claimed, and the stronger reading is false. Say plainly: "Compilation is deterministic given accepted records. Extraction is not reproducible across fresh model calls; reproducibility is achieved by preserving and replaying raw responses." A future operator who believes the strong claim will draw wrong conclusions when a re-run diverges.

---

## 14. The v0.5.1 contamination check is asserted, not specified

§4.7 requires "a contamination count of zero in every v0.5.0 compile stage." How is it counted? If it is a path allowlist (nothing read outside approved v0.5.0 source paths), say so — that is cheap, deterministic, and sufficient. If it is left undefined, someone will implement it as a semantic scan, which is both expensive and unreliable.

Also unaddressed: the reverse direction. The author knows v0.5.1 material and will issue human rulings informed by it. That is not necessarily wrong, but the document should take a stance — either rulings must cite v0.5.0 evidence only, or v0.5.1-informed rulings are permitted and marked as such.

---

## 15. Gate semantics have slipped

Three inconsistencies that weaken the gate concept:

- Gate 3 is "Complete with mandatory migration repairs." A gate with mandatory outstanding work is not complete. Either the repairs are part of the gate (not complete) or they belong to a later gate (then say which).
- Gate 4 is "In progress; substantially complete" while §6 lists four remaining checks and §20 puts them first in the resumption plan. "Substantially complete" is a status that cannot fail; prefer a checklist with a binary state.
- **Gate numbering does not match execution order.** Gate 3's migration repairs are scheduled in §20 *after* Gate 5 implementation. So the gates are simultaneously being used as sequential phases and as artifact groupings. Pick one. If they are artifact groupings, drop the implication of ordering; if they are phases, move the migration work into Gate 5 or a Gate 6.

---

## 16. The manual will drift from the controls it summarizes

§10 correctly says the Gate 2 YAML is authoritative and this table is a human-readable guide. But nothing keeps them synchronized, and §16's required-reading list for a new task does not include *this manual* — which is odd, since it is the handoff document, and a fresh operator will read it as truth.

Two fixes: (a) have the manual pin the hashes of the control files it summarizes, with a check that fails when they diverge; (b) add the manual to §16's reading list, marked explicitly as orientation-only with no execution authority (consistent with the header on line 8).

---

## Minor / internal consistency

- **Unexplained numbers.** "123 likely compound records" (§20) and "41 ruling sections" (§20) appear for the first time in the resumption plan with no derivation in §6, where the audit results live. A fresh operator cannot verify or reproduce either figure. Move them into §6 with their source.
- **Naming inconsistency.** §6 Gate 3 table says "Crossing"; §10 row 8 says "Crossing and RISK." Presumably the same source. Given that the document's central thesis is that identity must be exact, use the canonical source ID in both places.
- **Cost figures without a total.** §15 reports `$10.249100` confirmed and a `$0.257710` unreconciled upper bound, but there is no projected total for the remaining ~17 sources. That projection materially affects architecture choices (synchronous-only, batch disabled, re-extraction on prompt revision). Add a corpus-level projection with a stated confidence range.
- **"Reference only" sources have no disposition record.** Rows 23–24 are excluded from compile extraction, which is a decision. It should have a ruling receipt like any other decision, or a future operator will re-litigate it.
- **Durability.** "Pushed to GitHub" is the only stated resilience measure, and it covers one repository on one account. If this corpus represents 913+ hand-reviewed records and growing, a second offsite copy is worth one line in §17.

---

## Questions only you can answer

These are not defects — they are choices the document makes implicitly and would be stronger for making explicitly.

1. **Is the rigor proportionate to the stakes?** This process would be appropriate for a regulated corpus with legal traceability requirements. It is being applied to a game design document. The traceability guarantee is real and valuable — but it is being bought with a very large amount of human review time (Finding 2), and the document never states what would be lost by a lighter process. Worth an explicit answer, even if the answer is "yes, deliberately, because I do not trust summaries and this is the point." Risk tiering (Finding 2) is the natural middle path.

2. **What is the minimum viable v0.5.0?** If the full pipeline proves too heavy at Stage 5, what is the fallback? Having no defined reduced path means the fallback will be improvised under pressure, which is how the original drift started (§2). A pre-authorized degraded mode is safer than an unplanned one.

3. **Who is the operator, in practice, and for how long?** §22's definition of hardened is "a fresh operator with no conversational context can..." — which implies operator turnover is expected and frequent (each new AI task is a fresh operator). If so, the repository-as-sole-state requirement in §16 is load-bearing and deserves the enforcement mechanisms in Finding 5, not just the policy.

4. **Does v0.5.1 development continue in parallel?** If yes, sources will change mid-process and Finding 4's carryforward policy moves from "should have" to "blocking."

---

## What is working

Worth preserving explicitly through iteration, because these are the parts that would be easy to lose while fixing the above:

- The five separations in §2 are the correct diagnosis, and §4.2 (extraction order ≠ authority order) is a subtle point most such processes get wrong.
- §14's least-interpretive-correction hierarchy, with the prohibited-shortcut column, is the single best artifact in the document — it encodes judgment in a form that survives handoff.
- §4.4 (absence is not retirement) and §4.5 (uncertainty stays visible) are the right defaults, even though together they create the termination problem in Finding 3.
- The dual chunk limits (token *and* claim-block count) show the design is responding to observed failure rather than to theory.
- Preserving raw responses for zero-cost replay is the correct economic architecture and makes several of the fixes above cheap.
