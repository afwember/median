# MEDIAN GDD Compiler — Naming and Identifier Scheme

**Version 0.3 · 31 July 2026 · RULINGS APPLIED — READY TO FREEZE**

Implements Phase 0 of `MEDIAN_GDD_Compiler_Python_Process_v1.0`. Asa's rulings of
31 July 2026 are incorporated in §4, §5, and §8. Once frozen, source IDs are
permanent and must never be reissued, reused, or renamed, because every atomic
record, conflict, ruling, and migration row is addressed through them.

---

## 1. Governing rules

1. **IDs are independent of filenames.** Filenames may change; IDs may not. The
   manifest binds ID → filename → SHA-256. Identity is the hash, not the name.
2. **IDs are permanent.** A retired or deferred source keeps its ID forever.
   Retired IDs are never recycled for new material.
3. **One ID per document lineage, not per version.** Guest Citizen v1_0 and v2_0
   share the ID `SPEC_GUEST`; the manifest's `version` and `status` columns
   distinguish them.
4. **Record IDs are minted only from sources with disposition `compile`.** This
   is what keeps rule 3 safe — a superseded or deferred version is never
   atomized, so `SPEC_GUEST:0042` can only ever mean one passage.
5. **A source is a container, not a unit of meaning.** Amalgamated specs are not
   split into multiple sources. Granularity is the job of Phase 4 extraction.
6. **ASCII, uppercase, underscore-separated.** No spaces, no hyphens inside an
   ID, no non-ASCII. Safe in filenames, JSON keys, CSV cells, and grep.
7. **Topic token ≤ 8 characters**, chosen for recognition at a glance in a
   conflict packet, not for completeness.

---

## 2. Source ID format

```
<CLASS>_<TOPIC>
```

Class prefixes are drawn from the compiler spec's controlled source classes
(Appendix B2). The topic token is unique within the corpus.

| Prefix | Source class        | Meaning                                                    |
|--------|---------------------|------------------------------------------------------------|
| `BASE` | baseline            | The canonical GDD edition being compiled from.              |
| `SPEC` | detailed_spec       | A v0.5.0 system specification. Primary canon input.         |
| `PASS` | supplementary_pass  | Cross-cutting pass or catch-all over other sources.         |
| `PHIL` | philosophy          | Design philosophy and architecture of intent.               |
| `RSCH` | research            | External or comparative research. Never establishes canon.  |
| `MANI` | manifestation       | Expression of MEDIAN in another medium.                     |
| `APDX` | appendix            | Appendix architecture and content planning.                 |
| `LOG`  | decision_log        | Dated record of decisions or dispositions already taken.    |
| `RULE` | human_ruling        | Ruling issued by Asa during compilation. Highest precedence.|

Three IDs are fixed by the compiler spec's own worked examples and must not be
changed: `SPEC_HOME` and `SPEC_ITEMS` (§3.1) and `PASS_OVER` (§11).

---

## 3. Source disposition

The compiler spec (Appendix B1) carries a boolean `include_in_compile`. The
rulings below need three states, so the manifest replaces that boolean with a
`disposition` field. This is a deliberate extension of the spec.

| Disposition | Normalized | Chunked | Atomized | Meaning |
|---|---|---|---|---|
| `compile` | yes | yes | yes | Canon-eligible input to the v0.5 GDD. |
| `deferred` | yes | no | no | Held out of v0.5; revisited when Sourcebook arrangement begins. |
| `superseded` | no | no | no | Hashed and archived only. |

Everything is hashed and manifested regardless of disposition. Nothing is
deleted, and nothing silently disappears from the accounting.

A separate non-binding `intended_target` column (`body` / `appendix` / `tbd`)
records where a source is expected to land. It is a hint for Phase 10, not an
authority, and it does not affect extraction.

---

## 4. Corpus assignments

### 4.1 Compiled — baseline and specifications

| ID | Document | Ver | Status | Disposition |
|---|---|---|---|---|
| `BASE_046` | MEDIAN_GDD_v0.4.6.md | 0.4.6 | active | compile |
| `SPEC_HOME` | Home Loop Rework Specification | — | active | compile |
| `SPEC_AWAY` | Away Mode Specification | v1.0 | active | compile |
| `SPEC_EMBOD` | Embodiment Register Specification | v2.0 | active | compile |
| `SPEC_CROSS` | Crossing Register Specification | v0.1 | active | compile |
| `SPEC_GUEST` | Guest Citizen Specification | v2.0 | active | compile |
| `SPEC_ITEMS` | Personal Items, Focus and Expedition Equipment | v1.0 | active | compile |
| `SPEC_POP` | Population Growth and Colony Tiers | v1.0 | active | compile |
| `SPEC_ECOL` | Ecological Influences Specification | v1.0 | active | compile |
| `SPEC_SPECIES` | Core Species Traits Specification | v0.1 | active | compile |
| `SPEC_PROG` | Discovery, Time, Movement and Civic Progression | v1.0 | active | compile |

### 4.2 Compiled — passes, rulings, philosophy

| ID | Document | Status | Target |
|---|---|---|---|
| `PASS_OVER` | Overarching Systems Specification v1.0 (CATCHALL_4) | active | body |
| `PASS_047` | FourSeven Decisions Specification v1.0 (CATCHALL_1) | active | body |
| `PASS_BSA` | Baseline Survivorship Audit (CATCHALL_2) | active | body |
| `RULE_BSA` | Baseline Disposition Ledger Checkpoint 2026-07-30 (CATCHALL_3) | active | body |
| `PHIL_ARCH` | Philosophical Architecture v2.0 | active | body |
| `PHIL_SPEC` | Philosophical Specification (v0.5.0) | active | body |

`PASS_BSA` asks and `RULE_BSA` answers. The BSA-nn numbering in the Disposition
Ledger refers back to the Survivorship Audit, so `RULE_BSA` declares a manifest
dependency on `PASS_BSA`. See §8 for the extraction handling both require.

### 4.3 Compiled — appendix material

| ID | Document | Ver | Status | Target |
|---|---|---|---|---|
| `APDX_PLAN` | Appendix Architecture and Content Plan | v1.0 | active | appendix |
| `RSCH_MKT` | Market Position and Comparative Landscape | v1.1 | active | appendix |
| `MANI_SPEC` | Manifestations Specification | — | active | appendix |
| `MANI_BOARD` | Board Game Manifestation Initial Draft | — | provisional | appendix |

### 4.4 Deferred

| ID | Document | Status | Returns at |
|---|---|---|---|
| `SPEC_AUG` | Augments Plan v0.1 | provisional | Sourcebook arrangement |

### 4.5 Superseded

| ID | Document | Ver | Superseded by |
|---|---|---|---|
| `SPEC_GUEST` | Guest Citizen Specification | v1.0 | v2.0 |
| `PHIL_ARCH` | Philosophical Architecture | v1.0 | v2.0 |

**Totals: 21 compiled · 1 deferred · 2 superseded rows · 22 distinct IDs.** The
compiler process specification itself is not a source and receives no ID.

---

## 5. Provisional precedence policy

Frozen at Phase 0 per compiler spec §A5. Human rulings override everything here.

1. Explicit human rulings (`RULE_*`) control absolutely. `RULE_BSA` is the only
   member of this class at Phase 0 and carries top substantive authority.
2. Explicit supersession beats implied supersession.
3. **`PHIL_ARCH` outranks `PHIL_SPEC`.** Philosophical Architecture v2.0 is the
   late-developed overall master and carries the most authority in the
   philosophy class. Philosophical Specification was written for the v0.5
   document earlier and remains canon-eligible, but yields on conflict.
   *(Ruling 5, 31 July 2026.)*
4. **`RSCH_*` and `MANI_*` are canon within their own appendix scope only.**
   Market Position and the two Manifestation documents are appendix material,
   not audit instruments. They are authoritative about comparative position and
   about how MEDIAN expresses itself in another medium. They may not establish
   or alter a core-world mechanic; where one appears to, that is evidence of a
   gap in a `SPEC_*` source, not a grant of authority. *(Ruling 4, revised
   31 July 2026.)*
5. Normative rule beats example.
6. Domain owner beats incidental reference.
7. Compatible specific refinement beats general rule.
8. Date alone does not determine authority.
9. UI does not invent mechanics. SAY does not override STATE.
10. Unresolved conflicts remain unresolved.

---

## 6. Derived identifiers

Every downstream ID is built from a source ID, so the scheme propagates through
the whole build.

| Kind | Format | Example | Notes |
|---|---|---|---|
| Atomic record | `<SOURCE>:<NNNN>` | `SPEC_HOME:0042` | 4 digits, zero-padded, sequential per source. Never renumbered. |
| Chunk | `<SOURCE>:C<NNN>` | `SPEC_HOME:C004` | Sequential in document order. |
| Figure | `FIG-<SOURCE>-<NNN>` | `FIG-SPEC_ECOL-007` | Figure Registry key. |
| Term | `TERM:<CANONICAL>` | `TERM:CITIZEN` | Uppercase canonical form, underscores for spaces. |
| Conflict | `C-<NNNN>` | `C-0017` | Corpus-wide, not per-source. |
| Ruling | `RULING-<YYYY-MM-DD>-<NNN>` | `RULING-2026-08-01-001` | Per compiler spec §11. |
| Section | `GDD-<PP>.<SS>` | `GDD-07.03` | Per compiler spec §8. Frozen at Phase 10. |
| Removal | `<SOURCE>:R<NNNN>` | `SPEC_HOME:R0113` | Lean removal ledger entry. |

**Sequence rule.** Record numbers are assigned in document order at first
extraction and are append-only. Re-running extraction after a prompt change may
add records or mark records superseded; it may not renumber existing ones. Gaps
are expected and acceptable.

---

## 7. Build artifact paths

Filenames inside `build/v0.5/` are generated from source IDs, never from
original document names.

```
build/v0.5/
  sources/raw/SPEC_HOME.docx            immutable copy
  sources/normalized_full/SPEC_HOME.md
  sources/normalized_lean/SPEC_HOME.md
  chunks/SPEC_HOME.jsonl
  records/SPEC_HOME.jsonl
  reports/lean/SPEC_HOME.removals.jsonl
```

Original filenames survive in `manifest.csv` only.

---

## 8. Extraction notes for the two CATCHALL sources

Both were inspected on 31 July 2026 after an initial misclassification. They are
not the same kind of document and must not be extracted the same way.

### `RULE_BSA` — Baseline Disposition Ledger Checkpoint

7,016 words. Self-described as *"Authoritative working ledger for later
specification authoring"* and *"the controlling working record for subsequent
synthesis."* Carries 21 explicit **Adopted** markers across BSA-01 to BSA-11A.

It is a primary canon source and, in several domains, the *only* one. Material
that exists nowhere else in the corpus includes Deep Laws and species dialect,
the literacy scope constraint, the Campaign Memory / Chronicle / Tale three-layer
split, prior-life Tales, fear memory, Distinctions, After-names and Keepsakes,
the Supply and Tool class systems, Provisioning Roles and Dawn ordering, winter
cultivation, Construction Queue concurrency, and the weapon prohibition with its
latent-martial-utility guardrails. Much of this is exactly what `PASS_BSA`
identified as the *"clearest mechanical survivorship gap."* Excluding it would
have compiled a v0.5 GDD with a hole where the material economy should be.

Three handling requirements:

1. **Wording fidelity is SEMANTIC, never EXACT.** The document states it is *"not
   the final polished STATE specification."* It is authoritative on substance and
   provisional on phrasing. No passage may be pasted into the GDD verbatim.
2. **It contains explicit non-STATE blocks.** *"Designer commentary only. Not
   STATE material,"* the Developmental Appendix Note, the Complexity-Drift Watch,
   and the Superseded Note on RENDER must extract at weight `SILENT`, not
   `STATE`. Phase 4 extraction must honour these in-document markers.
3. **Internal supersession applies.** *"Where a later ruling contradicts an
   earlier one, the later ruling controls."* Document order carries authority
   within this source, which is not true of any other source in the corpus.
   Its closing *Provisional and Deferred Items* list (10 entries) should extract
   as `OPEN` records rather than being dropped as back matter.

### `PASS_BSA` — Baseline Survivorship Audit

An audit, not a ruling document. It introduces almost no mechanics. It is
compiled for three things it uniquely provides:

1. **§III** — a complete 38-row section-by-section survivorship ledger of
   v0.4.6 with CLOSED / DECISION REQUIRED / CARRY-FORWARD / DEFER status. This is
   pre-existing Stage 6 accounting and should be loaded as a seed for the
   Migration Ledger rather than re-derived from scratch.
2. **§IV** — 17 explicitly closed changes marked *"should not be reopened."*
   These are negative canon rulings and must survive as records, or the compiler
   will resurrect settled questions.
3. **§VI** — appendix routing calls, which feed Phase 10 alongside `APDX_PLAN`.

Most of its records should carry weight `SILENT` (process and architecture)
rather than `STATE`.

---

## 9. Remaining open items

None blocking. Phase 0 can freeze.
