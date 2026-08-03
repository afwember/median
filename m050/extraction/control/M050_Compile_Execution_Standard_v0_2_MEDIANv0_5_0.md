# MEDIAN v0.5.0 Compile Execution Standard v0.2

Date: 2026-08-03
Status: active efficiency and calibrated-quantization amendment; safety lifecycle preserved

Supersedes `M050_Compile_Execution_Standard_v0_1_MEDIANv0_5_0.md`. The
predecessor remains historical evidence.

## Operating objective

The extraction system exists to convert each in-scope Spec Doc into complete, grounded atomic proposals without reinventing the worker for every source. Rigor belongs at decisions and defects. Routine, already-authorized chunk traffic must remain mechanically guarded but operationally light.

## One machine, declarative sources

`m050/tools/m050_extraction_machine_v0_1.py` is the provider-eligible chunk controller. Source differences belong in one hash-bound configuration plus its manifest, disposition ledger, chunk plan, prompt, and response schema. New source-specific provider workers are prohibited unless a source structure is first proved impossible to express declaratively.

The approved processing order and source-state matrix select the source. `STATUS.md` reports state but is not parsed as execution authority.

After the selected source's identity card is approved, `scaffold` performs the
repeatable zero-call onboarding work: it parses the source, drafts conservative
block dispositions, plans heading- and table-aware chunks, generates the
source-bound prompt and response schema, and writes a provider-disabled
configuration. All outputs remain review drafts. Source-specific disposition
review, representative pilot selection, and pilot calibration remain required,
but new plumbing does not.

## Calibrated chunk quantization

Source block manifests describe evidence structure and never prescribe or
preserve a chunk count. Chunk count is always a generated result.

Calibration determines an acceptable number of provider-eligible target blocks
per chunk from observed output behavior, including atom density and the bound
output allowance. Once that quantization is selected, the generic `replan`
workflow re-apportions the complete source—not only the failed region—while
preserving source order, indivisible tables, repeated heading context, approved
dispositions, and input limits. The resulting number of chunks may increase or
decrease freely.

The re-apportioned plan and configuration require offline preparation, fake and
malformed-response validation, a newly frozen representative pilot, and exact
one-call author authorization. A prior pilot or source-run release does not
transfer across a changed chunk binding.

## Call lifecycle

1. `prepare` resolves a configured chunk and writes one immutable call packet containing its payload, provider request, bindings, pricing, and conservative cache-miss cost ceiling.
2. `send` requires both a source-bound lifecycle receipt and an active money-only spend envelope. The lifecycle receipt binds the exact ordered chunk IDs and matching call limit. It preserves one raw response and one compact outcome.
3. The controller appends `call_captured` to the source run ledger and blocks another call.
4. Mechanical validation and substantive source comparison occur before `review passed` may be appended.
5. Only a terminal `review_passed` event permits the next sequential call. A defect, ambiguity, cache failure, transport uncertainty, or failed review halts the run.

Pilot acceptance still does not release a source. Identity approval, pilot acceptance, full-source release, whole-document acceptance, and source advance remain separate authorial decisions.

## Spend envelope

- The normal operating envelope is cumulative provider spend, proposed in $2.00 increments, with machine scope `provider_spend_only`.
- It is source-agnostic money authority only. It never selects a source, releases a pilot or full-source run, changes cadence, forgives a defect, or advances a lifecycle state.
- Before every call, the controller requires enough unspent balance to cover the exact packet's conservative cache-miss ceiling. A possible cache hit is never used to justify authority.
- After a response, exact provider usage is debited. Human-facing cost is rounded upward to the next cent; exact cost remains in the machine record.
- The envelope has no shift, day, timer, or inferred renewal. Execution halts when the remaining balance cannot cover the next call and resumes only after Asa Wember grants another explicit increment.

## Claude prompt caching

- Claude Sonnet requests use explicit one-hour caching because sequential substantive review can exceed five minutes.
- The cache boundary follows the stable system policy and bound response-schema contract. Source/chunk payload, request IDs, timestamps, status reporting, and cost data remain after the boundary.
- Configuration, prompt, schema, and ordering must be byte-stable across a source run. Any semantic configuration change invalidates the run and returns it to calibration.
- The first response must report cache creation or a cache read. Zero creation and zero read is a machine defect and halts the run rather than silently proceeding uncached.
- Cost records preserve uncached input, five-minute creation, one-hour creation, cache reads, output, exact cost, and rounded-up display cost.

## Lean evidence policy

Historical R1–R6 evidence remains immutable. Prospectively, the ordinary durable footprint is exactly three artifacts per routine provider attempt, plus one ledger append:

- one execution configuration per source;
- one call packet, one raw response, and one compact outcome per provider attempt;
- one append-only, hash-chained JSONL run ledger per source;
- one whole-source candidate and one acceptance report after completion.

The run ledger carries call capture, validation summary, exact cost, cache telemetry, and review transition. Separate files for each routine freeze/capture/cost/review transition are prohibited unless an anomaly cannot be represented safely in the compact outcome and ledger.

## Proportionate verification

- Offline development uses focused unit, fixture, render, replay, and validator tests.
- Every provider response receives complete mechanical validation and substantive source comparison before the next call.
- The complete repository guard runs before control/code checkpoints, before a provider-enabled configuration is released, at whole-source acceptance, and before commit/push.
- Routine append-only runtime capture does not rerun the entire repository suite; its packet, spend, source, cache, response, and prior-review gates are the applicable preflight.

## Reporting

User-facing updates report only a decision, defect, spend-envelope exhaustion, source milestone, or completion. Internal validation remains thorough without narrating every hash read, test invocation, or staging operation.

## Current boundary

Authorial Grammar Pilot 001-R6 is accepted. The generic machine and its cached request layout are offline work only. Provider calls, the full-source run, and a cumulative spend envelope remain unauthorized until separate exact receipts are created.
