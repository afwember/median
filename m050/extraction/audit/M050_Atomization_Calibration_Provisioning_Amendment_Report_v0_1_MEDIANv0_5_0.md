# MEDIAN v0.5.0 Atomization Calibration Provisioning Amendment Report

Date: 2026-08-03

Status: append-only correction prepared; execution remains paused

## Omission

The v0.10 handoff correctly restored the complete 22-source compile boundary, but it reduced the future execution method to “one bounded source transition at a time.” That controls corpus scope without controlling how a source earns release.

The omitted method was the core quality mechanism used on the first four legacy sources: offline dry-run development, one frozen representative pilot, one cost-capped model call, local mechanical validation, substantive source comparison, rejection and offline iteration until perfect-for-release, separate full-source authorization, stoppable chunk execution, and whole-document review.

The omission could have allowed Compile B to select the right source while using an uncalibrated prompt or treating a generic warning to “check first” as sufficient control.

## Evidence and correction

The thread export, cost ledger, and acceptance reports show 152 controlled paid calls across the four preserved sources: Crossing 22, Philosophy/Architecture 53, MSID Grammar 31, and Human Rulings 46. Crossing’s seven calibration/comparison calls preceded twelve full-run calls and three table retests. Philosophy/Architecture was substantially heavier and required continuing semantic inspection, repeated stop/replay/retry cycles, and evolving deterministic controls throughout its 42 chunks. The method was therefore not “one pilot, then trust the run”; it was continuous defect-driven calibration through whole-document acceptance.

The amendment therefore:

- makes calibration reset for every source;
- defines perfect-for-release with mechanical and semantic criteria;
- binds acceptance to the exact source, pilot chunk, prompt, schema, chunker, model, and effort;
- separates pilot-call and full-source authorizations;
- revokes execution after any defect;
- requires a whole-document gate; and
- prevents authorization from transferring to the next source.

## Categorical audit additions

A broader audit found and corrected five adjacent category-level risks:

- Gate 2 identity approval now precedes offline extraction preparation.
- Source-bounded extraction-candidate acceptance is explicitly separated from later Layer E semantic acceptance and canonization.
- Pilot binding now includes identity, profile, engine, validator, normalization, exclusion, disposition, and stream-routing controls.
- deterministic-only, non-atomic, multi-stream, and embedded-media paths receive explicit disposition-specific treatment.
- sequential one-call/review and a one-source extractable-content firewall are the defaults; another-source context and implicit batching are prohibited.
- the external recovery bundle was scanned for stranded standalone controls; the only missing live obligation found was Authorial Grammar's post-extraction/pre-candidate conformance review against applicable Human Rulings authorial evidence, with Human Rulings material excluded from the provider prompt.

The intended 24-source order was recovered from the current Document Processing Tracker and promoted into a machine-readable control so a successor task does not infer order from filenames or task recency. The processing-order artifact is separately bound to the tracker sequence and the Gate 2 disposition authority, and identifies Authorial Grammar as the next outstanding source.

The complete category-by-category results are retained in `M050_Compile_Provisioning_Categorical_Oversight_Audit_v0_1_MEDIANv0_5_0.md`. The archive comparison and non-restoration decisions are retained in `M050_Post_Cleanup_External_Archive_Recovery_Scan_v0_1_MEDIANv0_5_0.md`.

No atomization, provider call, Google Sheets interaction, semantic review, acceptance, mapping, reconciliation, or compiled prose was performed by this amendment.
