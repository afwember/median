# MEDIAN v0.5.0 Hardened Compile Process

**Document type:** Plain-language operating manual  
**Audience:** A person or AI task with no prior knowledge of MEDIAN or the recovery work  
**Prepared:** 2026-08-02  
**Current repository:** `/Users/afw/Documents/GitHub/median`  
**Scope:** Assembly of MEDIAN v0.5.0 only  
**Execution authority:** Explanatory. This document does not itself authorize a model call, change a source, or accept an extraction.

---

## 1. What MEDIAN is and what this process is trying to produce

MEDIAN is an atmospheric animal colony-builder set on highway median strips. The current design target is MEDIAN v0.5.0. Its immediate source material is not one finished manuscript. It is a collection of specifications, governing documents, human rulings, developmental bridge documents, publication plans, and one earlier Game Design Document.

The goal is to turn that scattered source set into a coherent, traceable v0.5.0 corpus and then compile readable documents from it.

The process must preserve a chain in both directions:

```text
exact source wording
  → accepted evidence atom
  → MSID mapping
  → reconciliation decision
  → compiled passage

compiled passage
  → reconciliation decision
  → accepted evidence atom
  → exact source wording and location
```

This bidirectional chain matters because no model summary, attractive rewrite, filename, or prior conversational assertion is allowed to become canon merely because it sounds plausible.

The immediate deliverable is therefore **not yet a rewritten GDD**. It is a source-preserving, typed evidence corpus from which the v0.5.0 design can be reconciled, checked against v0.4.6, and compiled.

---

## 2. Why the process was rebuilt

The first extraction work discovered legitimate difficulties:

- PDF and DOCX conversions contain tables, headings, examples, endnotes, and change histories that require different treatment.
- A small number of input tokens can still contain many claim-bearing blocks and generate an oversized response.
- Models can return malformed quotation endpoints, incomplete JSON, compound claims, or semantically incorrect classifications even when much of the answer is useful.
- Provenance and revision-history sections can resemble rules but must not become game canon.
- Tables require row- and cell-aware grounding.
- Different kinds of sources cannot all use the same extraction policy.

Those discoveries justified calibration and stronger validation.

The process later drifted for a different reason. Extraction, MSID assignment, authority judgment, conformance, and cross-document reconciliation began to occur in the same step. Source-specific scripts inherited assumptions from earlier sources. New prompts and schemas accumulated without old ones being clearly retired. Conversational threads became part of the operating state. Filenames and shorthand such as “source 4” were sometimes treated as identity.

The result was recoverable evidence, but not one safe, repeatable pipeline.

The rebuilt process responds by enforcing five separations:

1. **A source is identified from its contents and genealogy, not its filename.**
2. **Extraction records what one source says; it does not decide which source wins.**
3. **MSID mapping happens after evidence acceptance.**
4. **Cross-source authority and conflict decisions happen during reconciliation, not extraction.**
5. **The repository, not conversational memory, defines each authorized job.**

---

## 3. The most important concepts

### 3.1 Source

A source is one frozen Markdown document with a stable source ID, exact repository path, and SHA-256 hash. A source may contain game rules, ontology rules, authorial rules, human decisions, publication instructions, historical evidence, or a mixture.

### 3.2 Source identity card

Before any paid processing, every source must have a content-derived identity card. It records:

- what the document actually contains, section by section;
- where it came from and what predecessor material it incorporates;
- why it exists;
- authority claims made inside the document;
- the human-adjudicated role of the document;
- likely subject owners, without deciding final authority;
- mixed-status, provisional, historical, example, and silent regions;
- allowed output streams;
- material that must be excluded from extraction.

If any of this was inferred from the title alone, the identity gate fails.

### 3.3 Block

A block is a stable structural unit assigned locally before a model is called. Blocks include headings, paragraphs, list items, table rows or cells, callouts, examples, status declarations, endnotes, and change records.

Each block receives an ID and hash. This makes it possible to prove whether every part of the source was processed, excluded for an allowed reason, or held for review.

### 3.4 Chunk

A chunk is a bounded group of blocks sent in one extraction request. A chunk may not break a table row or cross an explicit status, silent, or provenance boundary.

Chunks have two independent limits:

1. input-token ceiling;
2. maximum number of claim-bearing blocks.

The second limit prevents the failure in which a short but example-dense source region produces an enormous response.

### 3.5 Evidence atom

An evidence atom is a small, source-grounded claim. It contains an exact quotation and a normalized statement of what that quotation says. It is testimony from a source, not a final decision about MEDIAN.

### 3.6 MSID

An MSID is a MEDIAN semantic identifier. MSIDs organize claims by subject and semantic role. They are not assigned as final truth during extraction. The MSID Grammar must first be accepted as evidence, converted into a controlled vocabulary, and then used by a separate mapping stage.

### 3.7 Reconciliation

Reconciliation is the first stage in which different sources are compared. It determines agreement, conflict, ownership, status, supersession, aliases, and unresolved human questions.

### 3.8 Baseline

The actual baseline being revised is the **MEDIAN v0.4.6 Game Design Document**. The v0.4.7 developmental ledgers are not baseline audits of that document. They are bridge evidence describing what survived or changed during later development.

---

## 4. Governing principles

### 4.1 Filename is not identity

A filename is a filesystem label. A title and a document's internal claim to be “canonical,” “global,” “adopted,” “locked,” or “overarching” are evidence about the document, not proof of its authority.

Source identity and authority come from:

- actual content;
- development genealogy;
- explicit human rulings;
- section-level scope;
- later reconciliation.

### 4.2 Extraction order is not authority order

The first source processed does not outrank later sources. A dedicated specification does not erase unrelated material in a bridge document merely by remaining silent about it.

### 4.3 Exact wording is immutable evidence

Normalized claims may be corrected, remapped, or superseded. The exact source quotation remains unchanged. If the source itself changes, it becomes a new source version with a new hash.

### 4.4 Absence is not retirement

If a v0.4.6 subject does not appear in the reconciled v0.5.0 corpus, the system may not infer that it was intentionally removed. It becomes a gap or ruling question unless explicit authority explains the change.

### 4.5 Uncertainty remains visible

Ambiguous mappings, unresolved conflicts, provisional rules, invalid identifiers, and human-required questions are retained as explicit states. They are not forced into a false answer so a pipeline can appear complete.

### 4.6 Every transformation is append-only

Accepted records are never edited in place. Corrections produce new records and receipts that point back to the superseded result. Historical results remain addressable.

### 4.7 MEDIAN v0.5.1 is out of scope

All v0.5.1 material lives under `m051/` and must produce a contamination count of zero in every v0.5.0 compile stage.

---

## 5. Recovery Gates versus processing Stages

The process uses two different sequences. They must not be confused.

### Recovery Gates

The five Gates decide whether the machinery and repository are safe enough to proceed.

| Gate | Purpose | Current status |
|---|---|---|
| Gate 1 | Diagnose drift, preserve evidence, and freeze unsafe execution | Complete |
| Gate 2 | Define the desired corpus, source roles, stages, layers, and correction rules | Complete |
| Gate 3 | Decide which completed extractions can be reused | Complete with mandatory migration repairs |
| Gate 4 | Correct source identity, archive drift-era machinery, and clean the active repository | Complete |
| Gate 5 | Implement and prove one guarded extraction system | Not started |

No paid extraction resumes merely because Gates 1–4 contain useful documents. The freeze ends only after Gate 5 passes offline verification and the user explicitly authorizes a paid calibration.

### Processing Stages

The nine Stages describe how source material moves from files to compiled v0.5.0 text. These stages are the long-term operating pipeline. They begin only after the recovery Gates make that pipeline safe.

---

## 6. Current recovery state

### Gate 1: diagnosis

Gate 1 concluded that the evidence was recoverable but the old process could not safely resume. It froze:

- paid extraction;
- new source-specific worker forks;
- modification of accepted candidates in place;
- promotion of dry-run output;
- cross-source reconciliation disguised as extraction;
- execution based only on old prompts, old runbooks, or conversational instructions.

### Gate 2: target architecture

Gate 2 defined:

- the source set and each source's actual role;
- separate evidence streams;
- Stages 0–8;
- Layers E, M, R, and C;
- correction and retry limits;
- work-order requirements;
- acceptance criteria;
- v0.4.6 as the actual revision baseline.

### Gate 3: reuse audit

Four completed legacy extraction sets were audited:

| Source | Legacy chunks | Grounded records | Current disposition |
|---|---:|---:|---|
| Crossing | 11 | 121 | Reuse as Layer E evidence after local migration and review |
| Governing Philosophy and Architecture | 42 | 346 | Reuse as constitutional evidence after compound review |
| MSID Grammar | 30 | 273 | Reuse as ontology evidence; ignore old mappings |
| Human Rulings Ledger | 47 | 173 | Reconstruct deterministically by ruling ID and field |
| **Total** | **130** | **913** | **No wholesale paid re-extraction** |

All 913 exact quotations and cited locations ground against their frozen source. The useful evidence core survives. The old semantic shell—MSID guesses, authority effects, status judgments, conflicts, supersession, and conformance—does not become accepted merely because it was populated.

Home has a 58-chunk dry run but no extraction. Authorial Grammar has a 50-chunk legacy dry run and a rejected calibration response. Both counts are planning evidence from the retired runner and must be recalculated under Gate 5.

### Gate 4: identity and repository cleanup

Gate 4 completed the following work:

- renamed misleading active sources using content-derived identities;
- moved the actual v0.4.6 GDD into `m050/docs/baseline/`;
- archived old extraction controls, prompt versions, schemas, workers, and run directories;
- archived the abandoned Claude compiler and build process;
- preserved pre-migration source snapshots and rename receipts;
- removed empty abandoned active scaffolds;
- reduced live operations material to cost records;
- created two current progress workbooks and one human-readable cost ledger;
- established a frozen corpus manifest and deterministic integrity guard;
- established an active-control index and sole-writer/freeze policy;
- issued a human-readable completion report and machine-readable receipt.

Final path/hash validation, the repository-wide rejected-filename scan, active-control validation, archive seal, and tracker refresh all passed. The process is now paused before Gate 5 design; no extraction runner or provider call is authorized.

### Gate 5: implementation verification

Gate 5 has not begun. It must create one source-independent engine plus declarative source profiles. It must prove the engine offline before any provider call.

---

## 7. Atomic evidence streams

Records are divided by purpose. Sharing a folder does not make records equivalent.

| Stream | What belongs in it | What does not belong in it |
|---|---|---|
| `evidence_game_semantic` | Game identity, mechanics, systems, state, content contracts, and presentation behavior | Final authority decisions or inferred MSIDs |
| `evidence_ontology_grammar` | MSID syntax, identifiers, aliases, semantic classes, and ontology rules | Gameplay that appears only as an example |
| `evidence_authorial_rule` | Canonical language, typography, orthography, prose voice, and lint | Game mechanics or publication schedules |
| `evidence_human_ruling` | Direct human decisions as issued | Automatic flattening into game canon |
| `reconciliation_rule` | Authority, correction, source-scope, conformance, and precedence rules | Independent mechanics |
| `manifestation_rule` | Cross-medium invariants and medium-specific translations | Core rules treated as newly owned by a medium |
| `publication_rule` | Sourcebook, appendix, index, and production architecture | Game canon |
| `provenance_evidence` | Genealogy, history, survivorship, exclusions, and gap evidence | Default current canon |

A mixed document may contribute to several streams, but each contribution must retain its source and section identity.

---

## 8. The four linked record layers

The old process tried to put evidence, mapping, authority, and compilation into one overloaded atom. The hardened process uses four linked layers.

### Layer E: Evidence

Layer E records what the source says.

Required information includes:

- locally assigned evidence ID;
- source ID and source hash;
- block ID and exact location;
- exact source text;
- normalized claim;
- controlled claim kind;
- explicitly declared source status, when present;
- literal identifiers or terminology stated by the source;
- request, response, and chunk receipt IDs.

Layer E contains no inferred final MSID, authority effect, conformance basis, cross-source support, conflict, or supersession.

### Layer M: Mapping

Layer M connects accepted evidence to the controlled MSID vocabulary.

It records:

- mapping ID and version;
- evidence ID;
- zero, one, or more MSID candidates;
- status: `mapped`, `unmapped`, `ambiguous`, `invalid`, or `human_required`;
- rationale tied to accepted ontology evidence;
- mapper identity and review state.

A mapping correction creates a new Layer M record. It never changes Layer E.

### Layer R: Reconciliation

Layer R compares sources and makes or records decisions.

It contains:

- reconciliation ID and version;
- subject or MSID;
- supporting and opposing evidence IDs;
- applicable authority, conformance, and human-ruling evidence;
- adjudicated meaning and status;
- conflict, alias, and supersession links;
- decision type: deterministic, model-proposed, or explicit human ruling;
- review and acceptance receipt.

### Layer C: Compilation

Layer C connects reconciled decisions to published text.

It contains:

- compile ID;
- reconciliation IDs used;
- target document and location;
- rendered text;
- compiler version and input hashes.

This separation allows a mapping or editorial correction without repurchasing or rewriting valid source evidence.

---

## 9. Processing Stages 0–8

## Stage 0: Source freeze and content identity

**Purpose:** Prove that the intended file is being processed and that its role is understood from content.

**Inputs:**

- current source-disposition manifest;
- exact source path and hash;
- approved identity card;
- allowed streams and exclusions;
- v0.5.0 scope restriction.

**Actions:**

- verify path and hash;
- verify source ID and version;
- verify identity-card completeness;
- verify mixed-status boundaries and exclusions;
- reject any work order that relies on filename inference;
- confirm no v0.5.1 input.

**Output:** Frozen source snapshot and Stage 0 receipt.

**Stop conditions:** Any path, hash, role, genealogy, stream, or scope mismatch.

No model is called.

## Stage 1: Structural preparation

**Purpose:** Turn the source into stable blocks and safe chunks.

**Actions:**

- parse headings, paragraphs, lists, tables, callouts, examples, status declarations, endnotes, and change records;
- assign stable block IDs and hashes;
- classify obvious document furniture locally;
- preserve table rows as structural units;
- enforce status, silent, and provenance boundaries;
- generate chunks under both token and claim-block limits;
- select calibration samples;
- estimate request and output sizes;
- project cost without making a call.

**Output:** Block inventory, chunk plan, exclusion plan, calibration selection, prompt-size profile, cost projection, and dry-run receipt.

**Pass condition:** Every source block is structurally accounted for, every chunk is within limits, and the dry run makes zero external calls.

## Stage 2: Source-bounded evidence extraction

**Purpose:** Ask a model what one source says without asking it to compare sources or decide authority.

The model receives only:

- one source identity card;
- owned blocks from that same source;
- the evidence proposal schema;
- the current extraction instructions.

It does not receive:

- atoms from prior documents;
- the complete authority map;
- conformance corrections from other sources;
- final MSID assignments;
- the next document in the queue.

For every block, the response must provide exactly one disposition:

1. one or more proposed evidence atoms;
2. `no_substantive_claim`;
3. an allowed exclusion code;
4. `review_required` with a reason.

This is the block-disposition ledger. Missing or duplicate dispositions cause rejection.

## Stage 3: Deterministic validation and evidence acceptance

**Purpose:** Decide whether proposed evidence is structurally and semantically acceptable as source testimony.

Local validation:

- assigns IDs;
- verifies source and block hashes;
- resolves source locations;
- checks exact quotations;
- prohibits unauthorized cross-block quotations;
- validates schema and controlled enums;
- detects duplicates;
- confirms complete block disposition;
- flags likely compound atoms;
- preserves raw requests, responses, usage, and repair receipts.

Semantic review then examines:

- atomicity;
- correct source meaning;
- provisional, example, historical, tuning, and silent status;
- table-derived claims;
- exclusions and possible omissions;
- every deterministic anomaly.

Accepted Stage 3 records are still source evidence. They do not yet determine final MSIDs or authority.

## Stage 4: MSID vocabulary construction and mapping

**Purpose:** Organize accepted evidence using a controlled semantic vocabulary.

The accepted MSID Grammar evidence is first converted into a versioned vocabulary and validator. Only then is each applicable evidence atom mapped.

Every mapping ends in one explicit state:

- `mapped`;
- `unmapped`;
- `ambiguous`;
- `invalid`;
- `human_required`.

No evidence quotation changes during mapping.

## Stage 5: Authority and conformance reconciliation

**Purpose:** Compare sources and construct the proposed current v0.5.0 design.

This is the first stage allowed to receive multiple sources together. It uses:

- validated Layer E evidence;
- Layer M mappings;
- Human Rulings evidence;
- source identity cards;
- accepted authority and conformance rules.

For each subject, Stage 5 determines:

- agreement and corroboration;
- actual owner and authority scope;
- current status;
- conflict or ambiguity;
- supersession or aliasing;
- terminology corrections;
- need for a new human ruling.

Every substantive claim in the v0.4.7 development ledgers, Cross-System Carryforward, and v0.4.6 GDD Coverage-Gap Development must receive a disposition. Possible outcomes include:

- represented by a current owner;
- corroborating current evidence;
- uniquely surviving and accepted;
- superseded by identified later evidence;
- conflicting and unresolved;
- provisional or deferred;
- diagnostic or process material excluded with reason.

Nothing disappears because a dedicated source is silent.

## Stage 6: v0.4.6 baseline survivorship and gap audit

**Purpose:** Compare the reconciled v0.5.0 target against the actual v0.4.6 GDD.

This happens after reconciliation, not before. The process first determines what v0.5.0 currently says; it then checks what happened to every relevant v0.4.6 subject.

Each baseline subject is classified as:

- covered by current evidence;
- explicitly changed or retired;
- moved or reorganized without loss;
- historical only;
- deferred;
- unresolved and requiring a ruling;
- genuinely absent from the v0.5.0 source set.

An unexplained absence reopens Stage 5. Historical material is never silently restored.

## Stage 7: Manifestation and publication processing

**Purpose:** Handle medium-specific and publication rules without contaminating core semantics.

- The Computer/TTRPG/Card/Mobile framework is extracted later into `manifestation_rule` and reconciled against the settled core.
- The Appendix Architecture and Content Plan is parsed deterministically into `publication_rule`; model extraction is prohibited.
- The exploratory board-game draft is processed only if explicitly selected for the v0.5.0 Sourcebook.
- Market research and visual-augment planning remain references, not atomic compile sources.

## Stage 8: Compilation and bidirectional audit

**Purpose:** Produce human-readable v0.5.0 documents from accepted reconciliation records.

The compiler consumes only pinned, accepted inputs. It emits:

- readable specification or Sourcebook text;
- links from every compiled claim to reconciliation and evidence IDs;
- a reverse disposition for every required reconciled record;
- build receipts with compiler version and input hashes.

The final audit verifies:

- no compiled claim lacks evidence;
- no required accepted record disappears silently;
- no v0.5.1 material entered the build;
- the build is reproducible.

---

## 10. Current document-processing order

This is the intended sequence by processing dependency. Completion status does not confer authority.

| Order | Source | Role | Current extraction status |
|---:|---|---|---|
| 1 | Authorial Grammar, Orthography, and Prose Style Guide | Authorial-rule stream | Rejected calibration only; fresh Gate 5 plan required |
| 2 | Governing Philosophy and Architecture | Constitutional evidence | 42 chunks / 346 grounded legacy records; migrate |
| 3 | Human Rulings Ledger | Human, reconciliation, game, ontology, authorial, and provenance evidence | 47 chunks / 173 grounded legacy records; reconstruct deterministically |
| 4 | MSID Grammar | Ontology evidence | 30 chunks / 273 grounded legacy records; migrate |
| 5 | Home Mode, Colony, and DWELL | Core game evidence | 58-chunk retired dry run only; not extracted |
| 6 | Embodiment and EMBODY | Core game evidence | Not started |
| 7 | Away Mode, Field, Crossing, Encounter, and Return | Core game evidence | Not started |
| 8 | Crossing and RISK | Core game evidence | 11 chunks / 121 grounded legacy records; migrate |
| 9 | Population Growth and Colony Tiers | Core game evidence | Not started |
| 10 | Guest Citizen | Core game evidence | Not started |
| 11 | Personal Items, Focus, and Expedition Equipment | Core game evidence | Not started |
| 12 | Discovery, Time, Movement, and Civic Progression | Core game evidence | Not started |
| 13 | Core Species Traits | Core game evidence | Not started |
| 14 | v0.4.7 Cross-System Attention, Persistence, and World-State Carryforward | Developmental bridge evidence | Not started |
| 15 | Ecological Influences | Subsidiary game evidence | Not started |
| 16 | v0.4.6 GDD Coverage-Gap Development | Late coverage-gap evidence, not a global owner | Not started |
| 17 | v0.4.7 Development Rulings Ledger, BSA-01 to 11A | Mixed bridge and provenance evidence | Not started |
| 18 | v0.4.7 Development Survivorship Review | Mixed bridge and provenance evidence | Not started |
| 19 | MEDIAN v0.4.6 Game Design Document | Actual historical baseline | Deferred to Stage 6 |
| 20 | Computer/TTRPG/Card/Mobile Manifestation Framework | Manifestation rules | Deferred to Stage 7 |
| 21 | Appendix Architecture and Content Plan | Publication rules | Deterministic Stage 7 parse; no model extraction |
| 22 | Board Game Manifestation Initial Draft | Optional exploratory manifestation | Human selection unresolved |
| 23 | Market Position and Comparative Landscape Research | Reference only | No compile extraction |
| 24 | Sourcebook Visual, Narrative, and Infographic Augments Plan | Reference only | No compile extraction |

The authoritative paths, hashes, detailed roles, and dispositions live in the Gate 2 source-disposition YAML. This table is a human-readable guide, not an executable registry.

---

## 11. How one fresh source is processed

The following is the standard operating sequence once Gate 5 exists.

1. **Select one source from the approved order.** The worker cannot select it automatically.
2. **Verify Stage 0.** Confirm path, hash, identity card, role, streams, exclusions, and v0.5.0 scope.
3. **Run Stage 1 offline.** Produce blocks, chunks, exclusions, calibration samples, prompt sizes, density estimates, and a cost projection. External calls must equal zero.
4. **Review the dry run.** Check tables, status boundaries, dense regions, examples, endnotes, and excluded material.
5. **Create a pinned work order.** Default maximum spend is `$0.00`.
6. **Request explicit authorization for one paid calibration.** State provider, model, sample, token limits, maximum spend, and stop conditions.
7. **Run only the calibration sample.** Preserve the complete request, response, provider usage, and cost receipt.
8. **Validate deterministically.** Reject truncation, schema errors, ungrounded quotations, missing block dispositions, duplicates, invalid boundaries, and unauthorized content.
9. **Perform semantic calibration review.** Review every returned atom and every exclusion.
10. **Accept or reject the calibration explicitly.** A parsed response is not automatically accepted.
11. **If accepted, approve a full-document work order.** The prompt and schema remain pinned.
12. **Run synchronously under the cost cap.** Batch remains disabled unless separately chosen after the process has become repetitive and low-risk.
13. **Validate every chunk.** Use preserved responses for zero-cost replay when local code changes.
14. **Review the full document.** Review anomalies, tables, provisional material, exclusions, section edges, and suspected omissions.
15. **Write a new immutable accepted candidate and report.** The worker cannot self-accept.
16. **Update progress and cost records.** Failed and rejected paid calls are recorded too.
17. **Stop before mapping or reconciliation.** Those are later stages.

---

## 12. Work-order contract

Every provider run must begin with one small machine-readable work order containing:

- one source ID;
- exact path and hash;
- identity-card version;
- allowed blocks and output streams;
- prompt, schema, engine, provider, and model versions;
- dry-run receipt;
- calibration selection;
- input-token, output-token, and claim-block limits;
- maximum authorized spend, default `$0.00`;
- retry allowance;
- stop conditions;
- expected output paths.

The worker may not:

- choose another source;
- edit controls;
- change prompt or schema during the work order;
- increase the cost cap;
- accept its own output;
- begin mapping or reconciliation;
- use conversational instructions to broaden scope.

---

## 13. Calibration design

Calibration is not “run the first chunk and see what happens.” The sample must be selected to test the source's known risks.

When present, it includes:

- ordinary prose;
- the densest claim-bearing section;
- a table;
- a mixed-status or provisional region;
- an example or non-normative boundary;
- an endnote, change record, silent region, or excluded region.

Calibration passes only if:

- every input block has exactly one disposition;
- every quotation grounds exactly;
- the response is complete and within limits;
- the schema is valid;
- no other source's content leaked into the request or result;
- every atom passes semantic review;
- every exclusion is justified;
- the cost receipt is present.

One successful easy paragraph is not sufficient calibration for a complex document.

---

## 14. Error correction hierarchy

Always use the least interpretive correction that resolves the defect.

1. **Deterministic local validation or lossless normalization.**
2. **Zero-cost replay of an already-paid raw response.**
3. **Targeted retry of only the failed blocks under the unchanged prompt.**
4. **Global prompt, schema, or engine revision followed by the complete regression suite and replay.**
5. **Explicit human ruling.**

Examples:

| Problem | Correct response | Prohibited shortcut |
|---|---|---|
| Path or hash mismatch | Stop and resolve source identity | Use a similarly named file |
| Wrong source role | Revise the identity card under review | Trust the title |
| Chunk crosses a status or table boundary | Rechunk locally | Ask the model to infer the boundary |
| Output reaches the token ceiling | Reject the whole response and reduce block count | Keep the apparently complete prefix |
| JSON failure | Lossless parser repair only if meaning is unchanged; otherwise retry | Invent missing values |
| Quote not found | Reject the atom or retry the exact block | Substitute similar prose |
| Duplicated quotation prefix | Repair only when exact matching proves the duplicate | Use broad fuzzy trimming |
| Compound atom | Split only when source spans and meanings remain unambiguous | Chop at punctuation |
| Missing block disposition | Reject as incomplete | Assume the block had no claim |
| Wrong MSID | Correct Layer M | Re-extract valid evidence |
| Wrong authority | Correct Layer R with evidence | Rewrite the source atom |
| Cross-source conflict | Preserve unresolved Layer R state or request a human ruling | Delete the inconvenient atom |

### Retry limits

- A work order pins all execution parameters.
- One unchanged-prompt retry is allowed for transport failure or truncation after safe local rechunking.
- A semantic failure that repeats stops the document and opens a process issue.
- Source-specific prompt branches and source-specific worker forks are prohibited.
- A global engine or prompt change must pass the fixed regression corpus before another paid request.

---

## 15. Provider and cost policy

The process is provider-neutral. Anthropic, OpenAI, Gemini, or another provider may be selected when its strengths fit a stage, but provider choice never changes the evidence contract.

Rules:

- Every external request is logged, including failed, rejected, and interrupted requests.
- Provider, service, model identifier, request ID, execution mode, input tokens, cached tokens, output tokens, and exact charge are recorded when available.
- Estimates and caps do not enter confirmed spend.
- Prompt caching may reduce cost but is never a correctness dependency.
- Dry runs, local validation, replay, hashing, and schema checks should do as much iteration as possible at `$0.00`.
- No positive cost cap runs without explicit user approval.
- Calibration is synchronous.
- Batch is opt-in only after the task is proven repetitive and low-risk; it is not the default.

Current cost records:

- provider-neutral entries CSV: `m050/docs/operations/costs/M050_Compile_Cost_Entries_v0_1_MEDIANv0_5_0.csv`;
- human-readable ledger: `m050/extraction/progress/M050_Compile_Cost_Ledger_v0_1_MEDIANv0_5_0.md`.

At the time of this manual, the ledger reports `$10.249100` confirmed spend and a separate `$0.257710` unreconciled modeled upper bound.

---

## 16. Thread and task discipline

An AI task is an operator, not the source of process authority.

Every new task should begin by reading:

1. the current Gate status;
2. the Gate 2 target-process document;
3. the Gate 2 source-disposition manifest;
4. the latest Gate 3 reuse disposition;
5. the progress workbooks;
6. the exact work order, if one exists.

A task should not be told merely “continue source 5.” It should receive an exact source ID, path, hash, authorized stage, allowed actions, cost cap, and stopping condition.

The repository must be sufficient to resume after conversation compaction or thread replacement. If essential operating state exists only in chat, the process is not ready.

Narrative handoff prompts may explain context, but they cannot override machine-readable controls or authorize a broader action.

---

## 17. Archive policy

The active repository should contain only current sources, current evidence, current audits, progress records, and the future Gate 5 machinery.

The archive preserves:

- original PDFs and DOCX files;
- abandoned Claude compiler and build artifacts;
- old prompts and schemas;
- source-specific workers;
- raw provider requests and responses;
- run receipts and replay evidence;
- pre-migration source snapshots;
- prior filenames and concordances;
- rejected and superseded candidates.

Archive material is evidence, not execution authority. A current task may inspect it to understand provenance or reuse a paid response, but it may not treat an archived prompt, runner, registry, or candidate as live merely because it appears complete.

Moves into archive must be recoverable and recorded. Material is deleted only with explicit authority and only when it is truly disposable, such as regenerated previews.

---

## 18. Acceptance criteria

### Source evidence acceptance

- identity card approved;
- source hash verified;
- dry run approved;
- calibration approved;
- every block dispositioned;
- every quotation grounded exactly;
- schema and controlled values valid;
- anomalies resolved or explicitly retained for review;
- raw response and cost receipts present;
- semantic acceptance report complete;
- accepted candidate written immutably.

### Mapping acceptance

- controlled MSID vocabulary version pinned;
- no invalid identifier accepted;
- ambiguous and unmapped evidence remains visible;
- mapping corrections do not alter evidence.

### Reconciliation acceptance

- supporting and conflicting evidence linked;
- authority derived from explicit evidence, not filenames or rhetoric;
- unresolved conflicts remain unresolved;
- human decisions have ruling receipts;
- every substantive bridge and coverage-gap atom has a disposition;
- no source quotation is rewritten.

### Compile acceptance

- every compiled claim traces to accepted reconciliation;
- every required reconciliation record has a compile disposition;
- the v0.4.6 survivorship and gap audit is complete;
- no missing baseline subject is interpreted as retirement without authority;
- v0.5.1 contamination is zero;
- build inputs and versions are pinned and reproducible.

---

## 19. What must never happen again

- Do not infer identity or authority from a filename.
- Do not pass prior-document atoms into source extraction.
- Do not assign final MSIDs during extraction.
- Do not reconcile sources while extracting one source.
- Do not accept a response because it parses.
- Do not accept the prefix of a truncated response.
- Do not repurchase a response when deterministic replay can validate it.
- Do not silently repair an ungrounded quotation.
- Do not broaden a correction rule just to make one example pass.
- Do not create another source-specific worker fork.
- Do not let a task choose its next document.
- Do not let a model raise its own cost cap or accept its own output.
- Do not treat archived controls as current.
- Do not let v0.5.1 material enter the v0.5.0 process.
- Do not let a valid unique developmental rule disappear because a later source is silent.
- Do not interpret absence from v0.5.0 as intentional retirement from v0.4.6.

---

## 20. Exact resumption plan

When work resumes, proceed in this order.

### Design Gate 5 before coding it

1. Specify the Layer E proposal and accepted-evidence schemas.
2. Specify block and chunk records.
3. Specify identity cards and work orders.
4. Specify request, response, replay, repair, acceptance, and cost receipts.
5. Define the global regression corpus from failures already discovered.
6. Define one source-independent engine with declarative profiles.
7. Review the design before implementation.

### Implement Gate 5 offline

1. Build source hashing and identity validation.
2. Build the structural parser and dual-bound chunker.
3. Build prompt rendering from pinned controls.
4. Build deterministic validation and block-disposition accounting.
5. Build preserved-response replay.
6. Build append-only receipts.
7. Run regression fixtures and dry runs with zero external calls.

### Migrate the four reusable sources

1. Preserve all legacy candidates unchanged.
2. Import exact quotations, coordinates, source identity, and legacy IDs into Layer E.
3. Re-derive controlled fields locally.
4. Create retrospective block-disposition ledgers.
5. Review the 123 likely compound records rather than splitting mechanically.
6. Reconstruct Human Rulings from its 41 ruling sections and labeled fields.
7. Stop migration on any new hash, quotation, or coordinate failure.

### First new calibration

After Gate 5 and migration are verified, prepare the next source's identity card and zero-call dry run. Present the calibration sample, provider/model proposal, projected cost, cap, and stop conditions to the user. Make no paid call until the user approves that exact work order.

---

## 21. Where to look in the repository

```text
m050/docs/baseline/
    The actual v0.4.6 GDD baseline.

m050/docs/v0.5/
    Current governance, specification, provenance, and companion sources.

m050/extraction/accepted/
    Active accepted legacy candidates for Crossing, MSID Grammar, and
    Governing Philosophy and Architecture.

m050/extraction/audit/
    Gate 1 diagnosis, Gate 2 target process and source disposition,
    Gate 3 reuse audit, and Gate 4 disposition and completion records.

m050/extraction/control/
    Frozen corpus manifest, sole-writer/freeze policy, and active-control index.

m050/tools/m050_guard.py
    Deterministic frozen-source, accepted-evidence, archive, and version guard.

m050/extraction/progress/
    Progress and Stage Guide workbook, Document Processing Tracker workbook,
    and human-readable cost ledger.

m050/docs/operations/costs/
    Provider-neutral cost-entry CSV.

m050/archive/v0.5.0-orig/
    Historical sources, retired controls, raw runs, original candidates,
    migration snapshots, and receipts. Evidence only; not live authority.

m051/
    Later-version material excluded from the v0.5.0 compile.
```

Provider credentials are out-of-repository support material under
`/Users/afw/Documents/Codex/median-support/`. They are never source material,
never committed, and are not read or used until an explicit provider call is authorized.

The repository safety state was committed and pushed to GitHub on `main` after the Gate 4 reorganization and README update.

---

## 22. Definition of a hardened process

The process is hardened when a fresh operator with no conversational context can:

1. identify the exact authorized source and action from repository controls;
2. prove the source and every processed block by hash;
3. dry-run every structural and budget decision without a model call;
4. make only the explicitly authorized provider request;
5. reject incomplete or ungrounded output deterministically;
6. reuse paid output through replay rather than repurchasing it;
7. preserve uncertainty and conflict instead of hiding them;
8. keep extraction, mapping, reconciliation, baseline audit, and compilation separate;
9. reproduce every accepted result from pinned inputs and receipts;
10. trace every compiled statement back to exact source wording.

That is the standard Gate 5 must demonstrate before routine extraction resumes.
