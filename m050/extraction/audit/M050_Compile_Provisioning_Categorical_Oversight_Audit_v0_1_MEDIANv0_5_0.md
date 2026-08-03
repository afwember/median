# MEDIAN v0.5.0 Compile Provisioning Categorical Oversight Audit

Date: 2026-08-03

Status: amendment audit complete; execution remains paused

## Purpose

This audit asks a broader question than whether the omitted pilot paragraph was restored: could a cold successor task still perform the correct-looking work under a categorically incomplete model of the compile? Each category below is checked against repository controls rather than task memory.

## Findings

| Control category | Risk found | Amendment disposition | Enforced by |
|---|---|---|---|
| Corpus boundary | Four legacy sources could be mistaken for the complete corpus. | Already corrected and retained: 24 registered, 22 compile scope, 4 legacy seed, 18 outstanding = 14 pre-reconciliation + 4 later or conditional. | Gate 2 disposition, source-state matrix, v0.11 index, guard |
| Source ordering | Gate 2 matrix position could be mistaken for execution order; the intended order lived only in the tracker. | Corrected. The tracker sequence is now a separate, hash-bound 24-source control cross-checked against Gate 2 state and disposition. | Processing-order JSON and regression tests |
| Source selection authority | A task could begin from the next filename without an explicit source transition. | Corrected. Selection and every subsequent authority receipt remain author-specific and source-specific. | Protocol, state gate, root override |
| Content/provenance identity | Atomization could begin before the source’s actual contents, genealogy, mixed regions, and authority limits were understood. | Corrected. A reviewed, author-approved identity card now precedes offline extraction preparation. | Protocol and readiness gate |
| Disposition and timing | Deterministic, deferred, conditional, optional, and excluded sources could be forced through the ordinary provider path. | Corrected. Each Gate 2 disposition follows its own timing and execution path; excluded companions never atomize. | Protocol and readiness gate |
| Output streams and partitioning | Mixed sources could be flattened into one game-semantic stream. | Corrected. Stream routing is frozen and must be complete; multi-stream records retain record-level routing. | Protocol, readiness gate, pilot bindings |
| Structural and media accounting | Figures, captions, visual-only evidence, tables, or intentional exclusions could disappear outside text-block counts. | Corrected. Complete structural accounting and an explicit terminal disposition for every embedded media reference are required. | Protocol and readiness gate |
| Prompt source isolation | Another source’s prose or accepted atoms could become extractable context and contaminate provenance. | Corrected. Extractable provider payload is limited to exactly one source. | Source-only firewall and tests |
| Source-specific higher-authority conformance | Authorial Grammar could reach candidate acceptance without the historical post-extraction comparison against applicable Human Rulings authorial evidence. | Recovered from the retired processing-order control. The comparison is now mandatory before source-candidate acceptance, but Human Rulings content remains outside the provider prompt and the comparison cannot perform Layer E acceptance. | Processing order, protocol, root override |
| Offline calibration | A provider call could substitute for parser, chunker, schema, and fake-response development. | Corrected. Complete offline development and regression testing precede any bounded pilot authority. | Protocol and state machine |
| Representative pilot coverage | One easy paragraph could falsely validate a structurally heterogeneous source. | Corrected. Pilot material must cover the highest-risk regimes; materially different regimes require separate pilots. | Protocol |
| Configuration binding | A successful pilot could be reused after prompt, engine, validator, normalization, model, or scope drift. | Corrected. Release binds the full execution configuration; drift invalidates it absent an explicit replay-compatibility receipt. | Calibration module and tests |
| Spending and provider authority | General permission could be read as authority for retries or the full source. | Corrected. Pilot and source-run receipts are separate, call-limited, source-bound, and cost-capped with costs rounded up to the cent. | Protocol and calibration module |
| Execution cadence | “Full-source release” could silently become a batch or parallel run. | Corrected. The default is one call followed by extraction-quality review; any batch or parallel cadence requires separate author approval. | Protocol, source-run gate, tests |
| Continuous calibration | Pilot acceptance could be interpreted as proof that later chunks need no inspection. | Corrected. Philosophy/Architecture is the controlling precedent: defects discovered anywhere halt calls, revoke the release, and return the affected method to calibration. | Protocol, state machine, staged-execution gate |
| Immutable capture and replay | Rejected responses or accepted prior chunks could be edited in place while repairing a run. | Existing control confirmed. Requests, raw responses, validation, reviews, and receipts remain append-only; reuse requires binding-compatible replay. | Technical contract, capture/receipt tests, protocol |
| Whole-document coverage | Mechanically valid chunks could be promoted without detecting cross-chunk omissions, table loss, or fragments. | Corrected. A whole-document coverage and extraction-quality gate is mandatory. | Protocol and state machine |
| Acceptance-layer separation | “Source accepted” could be mistaken for semantic acceptance, canonization, or reconciliation. | Corrected. The terminal atomization state is `source_extraction_candidate_accepted`; Layer E and later stages remain separately gated. | Protocol, v0.11 index, state machine |
| Cross-source handoff | Success or write authority on one source could carry into the next source or another task. | Corrected. Every source resets; one repository writer exists; a successor starts read-only until explicit transfer. | Root override, protocol, write-authority policy |
| Downstream stage boundary | Atomization could implicitly start semantic review, mapping, reconciliation, or compiled prose. | Existing prohibition reconfirmed and carried forward. | v0.11 transition boundary and guard |
| External progress systems | Updating Google Sheets could resume as an assumed progress requirement. | Existing pause reconfirmed. No Google Sheets interaction occurs unless the author later reauthorizes a smaller-footprint method. | v0.11 transition boundary and root override |

## Historical calibration interpretation

Crossing is a clear example of pilot, full-run, and table-repair separation, but it was the lighter precedent. Philosophy/Architecture required 53 paid calls across 42 chunks plus offline replays, targeted retries, control changes, and continuing inspection. The operative rule is therefore continuous, defect-driven calibration throughout a source—not merely a small pilot before a bulk run.

Across Crossing, Philosophy/Architecture, MSID Grammar, and Human Rulings, the retained ledger records 152 controlled paid calls. These are evidence for the method, not reusable authority for any future source.

## Remaining intentional uncertainties

This amendment does not predesign Authorial Grammar’s identity card, parser profile, pilot chunks, prompt, or cost. Doing so would cross the current read-only boundary and repeat the mistake of treating a source as generic. It also does not authorize later-layer review or settle conditional-source selection. Those decisions remain future, source-bound transitions.

## Conclusion

No additional category currently permits execution to outrun authority or source understanding. The next controlled activity remains: push and verify this amendment, rerun the successor cold start read-only, explicitly transfer repository authority if its report is correct, and only then draft the Authorial Grammar identity card.
