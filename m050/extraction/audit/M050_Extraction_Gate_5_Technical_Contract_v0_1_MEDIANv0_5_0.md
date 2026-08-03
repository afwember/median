# MEDIAN v0.5.0 Extraction — Gate 5 Technical Contract

**Status:** Approved for offline implementation
**Date:** 2026-08-02
**Scope:** Offline implementation and verification of the guarded processing foundation
**Execution authority:** This proposal authorizes no provider call, corpus extraction, Layer M mapping, Layer R adjudication, or Layer C compilation.

**Author approval basis:** After conversational review of scope, review tiers, artifact classes, and transitions, the author directed Codex to proceed, use the dedicated Mac Mini resources needed, and bring the system into the best state for future operations. Provider use remains separately gated.

## 1. Gate 5 decision boundary

Gate 5 will build and prove the complete guarded foundation while initially production-enabling only source preparation, evidence extraction, and Layer E migration.

Gate 5 includes contracts and offline controls for Layers M, R, and C because omissions in later stages are harder to detect and more consequential than malformed extraction output. It does not authorize those stages to operate on the corpus. Production mapping, reconciliation, and compilation require later, explicit work orders after Layer E is stable.

The intended boundary is:

1. specify the complete machine-readable contracts;
2. implement one source-independent offline engine;
3. pass the regression corpus with zero provider calls;
4. replay preserved legacy responses and migrate reusable evidence locally;
5. prepare one fresh-source calibration work order;
6. stop for explicit author approval before the first provider call.

## 2. Authority and non-negotiable constraints

Asa Wember is the author and root of design authority. Codex is the sole repository operator while explicitly authorized. The active write-authority and freeze policy remains controlling.

The following constraints apply throughout Gate 5:

- The 33 files in the frozen v0.5.0 source inventory are immutable.
- The six protected accepted-evidence artifacts and the sealed archive are immutable.
- `m051/` is prohibited as an input to every v0.5.0 operation.
- No source identity, role, or authority may be inferred from a filename.
- Extraction records one source's testimony; it does not perform mapping or reconciliation.
- Accepted records are append-only. Corrections create superseding records and receipts.
- One engine serves all sources. Source differences are declarative profiles, not worker forks.
- A parsed or valid model response cannot accept itself.
- A provider call requires a positive-cost work order and explicit author approval.
- A failed integrity guard is a hard stop; expected hashes may not be updated to make a failure pass.

## 3. Implementation shape

The implementation will be a small Python command-line package using repository files as the authoritative state. It will not depend on an opaque database or conversational state.

Machine-readable contracts will use JSON Schema 2020-12. Immutable collections will use JSON or JSONL with ordered hash manifests. Human-readable reports will use Markdown. Derived indexes may be regenerated from authoritative records and are never themselves authority.

The engine will expose narrow commands rather than one unrestricted runner. Proposed command families are:

- `guard`: verify frozen and immutable state;
- `profile`: validate a source identity card;
- `block`: create a structural block manifest;
- `plan`: create chunks, exclusions, calibration samples, and cost projections;
- `render`: render a request without sending it;
- `capture`: record an externally returned response and provider receipt;
- `replay`: re-run local parsing and validation against a preserved response;
- `validate`: perform schema, grounding, disposition, and isolation checks;
- `review`: create risk-tiered review bundles and record dispositions;
- `accept`: append an accepted Layer E record set after authority checks;
- `stale`: calculate downstream invalidation from dependency edges;
- `bundle`: construct deterministic future reconciliation bundles and orphan reports;
- `report`: produce progress, cost, coverage, and known-gap reports.

Provider adapters will be isolated behind `capture`. Offline commands must not import credentials, initialize a provider client, or have a network side effect.

### 3.1 Runtime and dependency contract

MEDIAN will use a repository-local `.venv`; it will not execute from the mutable global environment.

The initial supported runtime is:

- macOS on Apple Silicon (`arm64`);
- CPython `>=3.12,<3.13`;
- a `.venv` created from the Mini's `/opt/anaconda3/bin/python3.12` interpreter;
- direct dependencies declared in `pyproject.toml`;
- exact transitive versions captured in a reviewed lock file;
- provider SDKs installed as optional extras, not as dependencies of the offline core.

The Apple `/usr/bin/python3` installation is prohibited for Gate 5 because it is Python 3.9.6 and is operating-system managed. The global Anaconda environment is a bootstrap source, not the project environment. The Codex bundled Python and document libraries may be used to render or inspect ancillary artifacts, but they are app-versioned resources and are not execution authority for MEDIAN.

The offline core should minimize dependencies. The anticipated direct set is:

- `jsonschema` for JSON Schema 2020-12 validation;
- `PyYAML` only where current authoritative YAML controls must be read;
- `pytest` as a development/test dependency.

Command parsing, hashing, canonical serialization, filesystem operations, state transitions, and receipts should use the Python standard library unless a third-party dependency gives a clear correctness benefit. `pydantic`, `typer`, `rich`, tokenizers, and provider SDKs are not assumed core dependencies. A tokenizer may be added as a provider-specific optional extra after its estimate-versus-provider behavior is tested.

Provider extras will be isolated, for example `provider-openai` and `provider-anthropic`. Installing an SDK does not authorize its use. Offline tests must pass in an environment where no provider extra is installed.

Before implementation, an environment preflight will record without exposing secrets:

- OS, architecture, Python implementation/version, and executable;
- virtual-environment status;
- installed direct dependency versions;
- schema and lock-file agreement;
- import isolation between offline core and provider adapters;
- whether expected credential *paths* exist and have private permissions, without reading their contents;
- a zero-network smoke test and repository guard result.

The bootstrap process must be scripted and idempotent. It may create or update only the ignored `.venv` and package caches. Any network installation will be disclosed before execution; no global package, base Conda environment, system Python, or shell profile will be modified.

## 4. Artifact model

Gate 5 will define schemas for the following artifacts before runner code is considered complete.

### 4.1 Control artifacts

- **Source identity card:** versioned, content-derived, and supported by cited block IDs. It records genealogy, roles, allowed streams, mixed-status regions, and proposed exclusions. It is a revisable hypothesis, not an irreversible classification.
- **Source profile:** only declarative parsing information that cannot be derived generically, such as known table conventions or explicit status markers. It cannot contain semantic conclusions, prompt branches, or authority outcomes.
- **Block manifest:** every structural block, its ordinal, type, raw hash, boundaries, parent section, status markers, and claim-density indicators.
- **Chunk plan:** ordered block membership, dual token/claim-bearing limits, boundary proofs, prompt-size estimates, and calibration selection.
- **Work order:** one source, exact hashes and versions, allowed blocks and streams, prompt/schema/engine/provider/model pins, spend cap, retry allowance, stop conditions, and expected outputs.

### 4.2 Capture and evidence artifacts

- **Rendered request:** the exact payload prepared for a provider, whether or not it is sent.
- **Raw response:** the exact returned bytes and provider metadata, never edited after capture.
- **Request/cost receipt:** request ID, timestamps, model, token use, caching, confirmed or estimated charge, and terminal disposition.
- **Proposal record:** model-proposed atoms and block dispositions. Proposal records are never accepted evidence.
- **Block-disposition ledger:** exactly one terminal disposition for every eligible block: one or more proposed atoms, `no_substantive_claim`, an allowed exclusion, or `review_required`.
- **Exclusion record:** block ID and hash, exclusion stage, controlled reason, decision source, reviewer, and review state. Exclusion is a disposition, not disappearance.
- **Validation report:** all deterministic checks, normalization events, anomalies, and pass/fail results.
- **Review bundle and receipt:** risk tier, membership hash, reviewer independence, findings, sampling method, and disposition.
- **Layer E candidate:** accepted-evidence-shaped records awaiting acceptance authority.
- **Layer E acceptance receipt:** candidate hash, controlling reports, accepting authority, and predecessor receipt hash.

### 4.3 Later-layer foundation artifacts

- **Layer M record:** evidence-to-MSID mapping with `mapped`, `unmapped`, `ambiguous`, `invalid`, or `human_required` status.
- **Reconciliation bundle manifest:** deterministic membership for one subject, membership hash, inclusion reasons, alias/term supplements, and size profile.
- **Layer R record:** subject disposition with supporting, opposing, authority, and ruling evidence.
- **Layer C record:** compiled wording and bidirectional evidence chain.
- **Dependency edge:** typed upstream/downstream relation used to calculate staleness.
- **Open-question record:** unresolved question, evidence set, owner, risk, and status.
- **Human-ruling record:** ruling ID, date, question, evidence considered, exact author decision, normalized decision, scope, affected subjects, and supersession links.

## 5. State machines

Every artifact family has its own state machine. Work orders and individual requests are separate so a successful request cannot imply an accepted work order or accepted evidence.

### 5.1 Work-order states

```text
draft
  -> offline_verified
  -> awaiting_authorization
  -> authorized
  -> active
  -> closed
```

Terminal alternatives are `rejected`, `failed_cost`, `failed_integrity`, and `cancelled`.

Only the author may move a positive-cost work order from `awaiting_authorization` to `authorized`. Authorization applies only to the exact pinned work order and expires when its allowed calls or spend are exhausted.

### 5.2 Individual-request states

```text
rendered
  -> verified
  -> authorized_for_send
  -> sent
  -> response_captured
  -> locally_processed
  -> dispositioned
```

Exceptional states are `not_sent`, `transport_failed`, `cost_blocked`, `truncated`, `invalid_response`, and `retry_authorized`. A retry is a new request linked to its predecessor; it never overwrites the earlier request or response.

### 5.3 Evidence states

```text
proposed
  -> mechanically_valid | mechanically_rejected
  -> semantic_review_pending
  -> reviewed
  -> accepted | rejected | human_required
  -> superseded | stale
```

Deterministic validation may move a proposal to `mechanically_valid`; it cannot move it to `accepted`. Acceptance requires the review receipt appropriate to the record's risk tier. Supersession and staleness retain the original record and append a new disposition.

### 5.4 Other artifact states

- Identity cards: `draft -> reviewed -> approved -> challenged -> superseded`.
- Mappings: `proposed -> validated -> reviewed -> accepted`, with `human_required`, `rejected`, `stale`, and `superseded` alternatives. Mapping lifecycle is distinct from semantic status (`mapped`, `unmapped`, `ambiguous`, `invalid`, or `human_required`).
- Reconciliation bundles: `constructed -> completeness_verified -> sealed -> reviewed -> accepted`, with `human_required`, `rejected`, `stale`, and `superseded` alternatives.
- Open questions: `open -> prepared -> presented -> answered -> encoded -> closed`; `deferred` remains visible and may return to `prepared`.
- Human rulings: `drafted_by_codex -> author_confirmed -> recorded -> effective -> superseded`. Only the author can confirm substance.
- Compile records: `drafted -> mechanically_validated -> editorially_reviewed -> accepted -> published`, with `human_required`, `rejected`, `stale`, and `superseded` alternatives.

Every transition produces an immutable receipt containing the artifact hash, prior state, new state, reason, authority, tool version, timestamp, and predecessor-receipt hash.

All operational cost caps and totals use nonnegative integer cents. If a provider reports a fractional-cent decimal charge, the exact reported decimal is preserved as audit metadata and the operational charge is rounded upward to the next whole cent. Binary floating-point values are not used for authorization or accounting.

## 6. Stable identity and content addressing

The engine, not a model, assigns identifiers.

- Source IDs come from the accepted source-disposition manifest.
- Block IDs combine source ID, structural ordinal, and a raw-block-hash prefix. The complete hash remains in the manifest.
- Request, response, candidate, bundle, and receipt IDs are derived from canonical serialized content hashes.
- Evidence IDs are derived locally from source hash, block ID, exact raw source span, normalized claim, controlled claim kind, and stream.
- A changed normalized claim creates a different evidence record. It never overwrites the earlier one.

Canonical JSON serialization must be deterministic: UTF-8, sorted object keys, no insignificant whitespace, and a specified treatment of decimals and timestamps. IDs cannot depend on filesystem modification time, model ordering, or thread state.

## 7. Text normalization and quotation grounding

Three text views will be kept distinct:

1. **Raw view:** exact source bytes and exact decoded source text. This is the evidentiary authority.
2. **Structural view:** UTF-8 decoded strictly, line endings represented as LF, and Unicode normalized to NFC for parsing. Raw offsets remain recoverable.
3. **Locator view:** a conservative comparison-only view that may normalize Unicode spacing, remove soft hyphens, expand common presentation ligatures, normalize typographic quotation marks, and classify dash variants.

The locator view may help locate a proposal, but it never becomes evidence. Acceptance requires a unique, contiguous raw source span inside the cited block. The engine stores that exact raw substring, not a model-rewritten quotation. Every locator transformation is listed in the validation report. Multiple possible raw matches, a cross-block match, or a non-contiguous reconstruction is rejected for review.

Whitespace collapse cannot cross paragraph, list-item, table-cell, or block boundaries. Table line-wrap handling belongs to structural parsing and must retain row/cell coordinates. Footnote markers are retained unless an explicit, globally tested normalization rule identifies a presentation-only marker.

The normalization specification is versioned. It may not be broadened inside a work order to rescue a failing quotation.

## 8. Structural preparation and completeness

Every source is parsed into headings, paragraphs, list items, table rows/cells, callouts, examples, status declarations, endnotes, and change records where present.

Every block must receive one structural disposition before a chunk plan passes. Chunks must obey:

- a maximum estimated input-token count;
- a maximum claim-bearing-block count;
- no table-row break;
- no status, silent, provenance, or source-region boundary crossing;
- stable, ordered membership recorded by block ID and hash.

Claim-density indicators are estimates, not exclusions. After extraction, projected density is compared with realized atoms. Low-yield dense blocks enter targeted review even when their one required block disposition is present.

Identity-card or Stage 1 exclusions remain visible in the exclusion ledger. An anomalous exclusion rate, a challenged stream restriction, or repeated evidence outside the card's expectation reopens and versions the identity card. Affected descendants are marked stale.

## 9. Review and acceptance model

Deterministic controls apply to every record. Human attention is exhaustive for high-risk decisions and exception-driven or sampled for routine grounded evidence.

### Tier 1 — author decision required

This tier includes:

- new human rulings;
- cross-source conflicts and authority decisions;
- unresolved or design-changing ambiguity;
- rejected, provisional, or historical material proposed for normative use;
- any request to alter a frozen source or controlling scope.

Codex prepares the evidence bundle and question. Only the author decides the substance.

### Tier 2 — exhaustive independent semantic review and bundle approval

This tier includes:

- constitutional and ontology rules;
- human-ruling reconstruction;
- numerical mechanics and tables;
- negations, exceptions, prohibitions, and supersession language;
- bridge-only and coverage-gap evidence;
- unique uncorroborated claims;
- likely compound records;
- anomalous exclusions, low-yield blocks, and model disagreements.

Every record receives semantic review, but approval occurs at a coherent section or subject bundle rather than atom by atom. The extractor may not be the semantic accepter. A separate review prompt or model may assist, but Codex records the review and the author receives a bundle-level digest; any substantive uncertainty escalates to Tier 1.

### Tier 3 — deterministic acceptance with risk-weighted sampling

Routine, grounded, non-conflicting evidence receives all deterministic checks. Codex may accept a batch after the fixed sample and all anomaly queues pass. The source report records sample selection and results.

The initial sampling rule is five percent of eligible chunks, rounded up, with a minimum of three when available: one deterministic random sample from a pinned seed, one highest-density sample, and one highest-exclusion or boundary-risk sample. Calibration material is reviewed exhaustively and is not counted toward this sample.

After provider calls are authorized, a differential extraction sample may use a second model or materially independent prompt. Its exact rate, cost, and model require a work order; Gate 5 does not silently spend for independence.

## 10. Review independence

Independence is functional, not merely a second invocation.

- Mechanical validation is accepted only by deterministic code.
- The extraction model cannot semantically accept its proposals.
- A semantic review model must use a materially different task prompt, see the source and proposal but not hidden extractor reasoning, and record its model/prompt identity.
- Codex may adjudicate whether deterministic and semantic review requirements are satisfied, but may not invent an author ruling.
- Tier 1 substance is accepted only from the author.

## 11. Dependency and staleness model

Every accepted artifact records its pinned inputs and typed dependency edges:

```text
source -> block -> evidence -> mapping -> reconciliation -> compile
identity card ------^          |             ^
prompt/schema/engine^          |             |
MSID vocabulary ---------------^             |
human ruling ---------------------------------^
```

A local staleness pass walks descendants after every supersession.

- Frozen-source mutation is an integrity failure, not ordinary staleness.
- A versioned identity-card change stales affected block plans, proposals, and evidence decisions.
- A changed block would stale its evidence; unchanged block hashes may carry forward only with an explicit provenance receipt. This path exists for a formally authorized re-freeze, not normal v0.5.0 work.
- An MSID-vocabulary change stales affected mappings and descendants, not Layer E quotations.
- A human ruling stales affected reconciliation and compile records.
- A semantic prompt/schema change requires a compatibility receipt. Compatible changes preserve accepted evidence; incompatible changes mark affected evidence for replay, review, or targeted re-extraction.
- Local renderer or validator fixes may use zero-cost replay, but any changed acceptance outcome creates a new record and receipt.

The staleness report is deterministic and may not delete or silently reactivate anything.

## 12. Human rulings and termination

New rulings are stored separately from the frozen 41-ruling historical ledger. The author may issue a ruling conversationally; Codex must present the proposed repository wording and then append the approved record.

An open-question record moves through `open`, `prepared`, `answered`, `encoded`, and `closed`, with `deferred` as an explicit nonterminal state. Encoding a ruling creates dependency edges and runs staleness propagation.

The corpus definition of done is:

> Every source block, evidence proposal, accepted evidence record, mapping, reconciliation subject, baseline subject, and required compile input has exactly one explicit current disposition. Any unresolved remainder appears in a known-gaps list that the author has explicitly accepted.

Stage 6 may reopen Stage 5 only when it identifies new evidence or a previously unrepresented subject. A repeated unresolved question without new evidence goes to the human-question queue rather than circulating indefinitely.

Unresolved normative wording is omitted unless the author approves clearly marked provisional language. The system does not invent a resolution and does not automatically restore v0.4.6 text.

## 13. Reconciliation completeness foundation

Even though production reconciliation is not authorized by Gate 5, its completeness machinery must pass offline tests.

For each subject, a deterministic bundle builder will include:

- every Layer M record mapped to that subject;
- records mapped to accepted aliases or parent/child subjects under explicit vocabulary rules;
- supplemental term-co-occurrence candidates, marked as supplemental rather than silently promoted;
- applicable human-ruling, authority, conformance, and source-identity evidence.

Each bundle records ordered membership, inclusion reason, source distribution, token/claim size, and a membership hash. Every applicable atom receives exactly one disposition within each required bundle. Every mapped atom must enter at least one bundle.

Separate sweeps report:

- mapped atoms in no bundle;
- `unmapped`, `ambiguous`, `invalid`, and `human_required` atoms;
- bundle members without dispositions;
- evidence referenced by no current downstream record;
- bridge and coverage-gap atoms without reconciliation outcomes.

Model-assisted reconciliation will later require its own calibration, size limits, cost projection, and author-approved work order.

## 14. Immutability and append-only enforcement

Immutability will be enforced through controls rather than convention alone:

- accepted artifacts and raw captures are added to ordered hash manifests;
- transition and acceptance receipts form predecessor-hash chains;
- the guard verifies all protected hashes before any command that can append state;
- an append writer refuses an existing target path;
- CI or an equivalent repository check rejects modification or deletion of protected paths;
- tests prove that overwrite, receipt reordering, missing predecessors, and manifest divergence fail closed.

Filesystem read-only flags may be added later as defense in depth, but Git-reproducible manifests and fail-closed writers are the required mechanism.

## 15. Provider and cost isolation

The engine is offline by default. Provider execution is a deliberately separate adapter invoked only with an authorized work-order ID.

Before a call, the adapter must verify:

1. repository guard pass;
2. work-order hash and state;
3. exact source, identity-card, block-plan, prompt, schema, engine, provider, and model versions;
4. remaining allowed calls and spend;
5. absence of `m051/` and unregistered input paths;
6. exact rendered-request hash.

The adapter captures the raw response and usage receipt before parsing. Network, authentication, rate-limit, truncation, and cost failures receive explicit terminal dispositions. One unchanged-prompt retry may occur only when the work order grants it. Batch execution remains disabled.

## 16. Regression corpus

All offline fixtures must pass before legacy migration or a calibration proposal. Fixtures will cover at least:

- UTF-8, NFC/NFD, curly quotes, apostrophes, dash variants, non-breaking and thin spaces, soft hyphens, and ligatures;
- ambiguous normalized matches and prohibited cross-block quotations;
- tables, lists, footnotes, examples, silent/provenance boundaries, and section edges;
- claim-dense chunks and token/claim-limit enforcement;
- missing, duplicate, and contradictory block dispositions;
- truncated and malformed responses;
- duplicated quotation prefixes and prohibited fuzzy repair;
- multi-claim under-extraction and low-yield detection;
- exclusion-rate anomalies and identity-card challenges;
- source/context leakage and `m051/` path contamination;
- immutable-file mutation, append overwrite, broken receipt chains, and stale descendants;
- reconciliation orphans, ambiguous mappings, missing bundle dispositions, and bundle-hash changes;
- deterministic replay producing identical validated output from pinned raw responses.

Every fixture records the failure it prevents and the expected fail/pass outcome. Tests must not access a provider or credential file.

## 17. Implementation sequence

Gate 5 will proceed in reviewable slices:

1. **Runtime preflight and bootstrap:** record the Mini baseline, add project metadata and a reviewed lock, create the local `.venv`, prove offline/provider import isolation, and document exact reproduction commands.
2. **Contract and schemas:** finalize this contract and machine-readable schemas.
3. **Deterministic core:** canonical serialization, hashing, guard integration, blocks, normalization, chunk plans, work orders, state receipts, and append-only writer.
4. **Validation and review:** proposal parsing, grounding, disposition completeness, exclusions, density checks, risk tiers, and review bundles.
5. **Dependency and later-stage foundation:** staleness graph, ruling/question records, Layer M/R/C schemas, reconciliation bundle builder, and orphan sweeps.
6. **Regression suite:** adversarial fixtures and fail-closed tests, all offline.
7. **Legacy replay and migration:** migrate the 913 grounded records without editing legacy artifacts; reconstruct Human Rulings deterministically; build retrospective block/exclusion ledgers; review the 123 compound flags and other risk queues.
8. **Fresh-source zero-call plan:** select the next approved source, issue its identity card and dry run, project provider cost and human effort, and render the proposed calibration request.
9. **Hard stop:** present the exact provider/model, request, sample, maximum cost, retry allowance, and stop conditions to the author.

No slice may silently broaden the next slice's authority.

## 18. Gate 5 pass criteria

Gate 5 passes only when:

1. the environment preflight passes from the documented local `.venv` on the Mini;
2. direct dependencies and exact locked versions agree, with provider dependencies absent from the offline-core test environment;
3. every artifact named in this contract has a validated schema or explicit deterministic format;
4. all state transitions and acceptance authorities are enforced;
5. offline commands cannot initialize provider access;
6. the full regression corpus passes with zero provider calls;
7. frozen-source, immutable-artifact, append-only, receipt-chain, and `m051/` controls fail closed under adversarial tests;
8. replay of preserved raw responses is deterministic;
9. the 913 reusable legacy records have a complete migration disposition, with no quotation or coordinate failure hidden;
10. Human Rulings reconstruction accounts for all 41 ruling sections and labeled fields;
11. retrospective block and exclusion ledgers account for the four legacy sources;
12. review-risk and human-effort reports are produced;
13. dependency/staleness and reconciliation-completeness fixtures pass;
14. one fresh calibration is fully rendered and costed but not sent;
15. the repository guard passes and the working state is documented;
16. the author reviews the Gate 5 completion report and separately decides whether to authorize the first provider call.

Passing Gate 5 proves that the machinery is safe enough to request a calibration. It does not itself authorize that calibration or declare later processing stages complete.
