# MEDIAN v0.5.0 Authorial Grammar Content/Provenance Identity Card v0.1

Date: 2026-08-03  
Status: `APPROVED`
Lifecycle state: `identity_card_approved`
Author/root of authority: Asa Wember  
Scope: source identity only; source-work, provider, spend, and later-phase authority remain separate

## 1. Source identity

| Field | Bound value |
|---|---|
| Source ID | `M050-SRC-AUTHORIAL-GRAMMAR-001` |
| Label | Authorial Grammar |
| Path | `m050/docs/v0.5/governance/M050_Authorial_Grammar_Orthography_and_Prose_Style_Guide_v0_1_MEDIANv0_5_0.md` |
| SHA-256 | `7d23ef2ccbff0c6594975c03cf405d838a3cc3f712ea6faf942581a72c9284ff` |
| Internal document ID | `M050-AUTHORIAL-GRAMMAR-001` |
| Internal version | `0.1` |
| Internal state | `ACTIVE_WORKING_GUIDE` |
| Internal authority label | `active_for_authorial_prose_and_semantic_typography` |
| Gate 2 content role | `authorial_grammar` |
| Gate 2 disposition | `source_bounded_atomic_extraction` |
| Allowed output stream | `evidence_authorial_rule` only |
| Gate 2 exclusions | `document_furniture`, `change_record` |
| Current compile state | Active source; C0001 and C0002 accepted, C0003 frozen for recalibration pilot |

The path, hash, source ID, disposition, stream, and exclusions above agree across the frozen corpus manifest and Gate 2 disposition. Approval of this identity card settles the source boundary only; it does not authorize a source run, provider call, spend, or later phase.

## 2. Control bindings

The active extraction configuration binds this exact card, its approval receipt,
the Authorial Grammar block manifest, and the Gate 2 disposition by hash. Root
`AGENTS.md` governs lifecycle and mandate; the canonical compile state and source
processing order govern mutable status and sequence. This card intentionally
does not duplicate their changing values.

## 3. Reason for existence and content role

Authorial Grammar exists because MEDIAN separates stable semantic addressing from authored presentation. The MSID Grammar owns what a game property's stable semantic address is; Authorial Grammar owns how that property appears in prose. This separation permits prose, typography, writing, and layout conventions to develop without treating every authorial change as an ontology revision.

The source defines or constrains:

- Initial Caps for Defined Nouns;
- ALL CAPS for experiential verbs and Core-Species operators;
- authored display of MSIDs;
- Core-Species naming and the Bare Core-Species Singular;
- Hyphen-bound animal-language compounds;
- stable and provisional text treatments;
- the lifecycle for emergent authorial conventions;
- voice, density, examples, authoring checks, and prospective lint behavior; and
- a derived one-page Phonebook appendix plate that summarizes rather than replaces the guide.

The extractable identity is therefore authorial rule evidence. The source is not a general game-mechanics owner, an ontology owner, a human-ruling ledger, or an independent publication-architecture stream.

## 4. Genealogy and provenance

This is the first identified standalone version of the guide. Its front matter does not name a superseded Authorial Grammar artifact, and no standalone predecessor is present in the registered corpus. The source records `created: 2026-08-01`. Current repository history first contains the file in commit `d294d4c528f98dd0790804b0b305a053a90af17e` (`Checkpoint MEDIAN v0.5 compile reorganization`, committed 2026-08-02). That repository commit proves current inclusion, not the date or completeness of pre-repository authoring history.

The direct decision provenance is the Human Rulings authorial-language group, especially:

- `HR-LANG-001`: Hyphen-bound animal-cultural compounds;
- `HR-LANG-002`: standalone Authorial Grammar ownership;
- `HR-LANG-003`: Initial Caps, ALL CAPS, and MSID display;
- `HR-LANG-004`: Bare Core-Species Singular and agreement;
- `HR-LANG-005`: Hyphen-bound internal lowercase and `Prior-life Tale`;
- `HR-LANG-006`: emergent grammar and provisional mechanics-teaching Narrative italics; and
- `HR-LANG-007`: the derived Phonebook grammar plate.

The source names Human Rulings, MSID Grammar, and Governing Philosophy and Architecture as governing sources and pairs itself with MSID Grammar. These are provenance and ownership relationships, not permission to place their prose or atoms in an Authorial Grammar provider payload.

### Bound related sources

| Relationship | Path | SHA-256 |
|---|---|---|
| Human decision provenance and later conformance authority | `m050/docs/v0.5/governance/M050_Human_Rulings_Ledger_v0_4_MEDIANv0_5_0.md` | `27d74381e86f64bb76f56daec9034dcf06913d18034821d8a97c20571a41e50f` |
| Paired ontology/MSID owner | `m050/docs/v0.5/governance/M050_MSID_Grammar_v0_5_MEDIANv0_5_0.md` | `9ca2e250720f7ea3acc4e74c7921cbf6f22686155077c78ef445557ac5f742b4` |
| Constraining constitutional/operator doctrine | `m050/docs/v0.5/governance/M050_Governing_Philosophy_and_Architecture_v1_3_MEDIANv0_5_0.md` | `b3f60389260625bed27e9fd71b8aa9f26211cea8098699ee0778cbfece1c09da` |

## 5. Authority boundary

The source's internal authority and active-state labels are evidence about intended scope; they do not grant blanket canonical authority by self-description. Candidate authorial rules remain source evidence until the later controlled evidence lifecycle accepts them.

Within this source:

- Authorial Grammar is the candidate owner of prose capitalization, orthography, grammatical house forms, semantic typography, authorial convention statuses, and authored display rules.
- Human Rulings remains the higher human-decision authority. After extraction and local validation, the source candidate must undergo the separately required conformance review against applicable active Human Rulings authorial evidence before source-bounded candidate acceptance.
- MSID Grammar owns MSID ontology, path validity, namespaces, segment construction, semantic classes, aliases, deprecated paths, and registry/extraction states. Authorial Grammar may own only how MSIDs are displayed and integrated into prose.
- Governing Philosophy and Architecture and dedicated system owners constrain the inventory and substantive meaning of Registers, experiential operators, species operators, mechanics, and game concepts. Authorial Grammar owns their written treatment, not their game-semantic truth.
- Appendix/Phonebook controls own final publication implementation. The guide owns the rule that its one-page plate is derived and non-independent, but it cannot emit `publication_rule` records under the current Gate 2 stream allowlist.
- Examples, checklists, and lint patterns support or operationalize authorial rules. They do not independently settle game mechanics or ontology.

Provider extraction, if separately authorized later, must expose extractable content from this source only. Human Rulings, MSID Grammar, P&A, prior atoms, and other-source prose remain outside the extraction payload.

## 6. Section-level content and candidate ownership

| Region | Actual content | Candidate owner and handling |
|---|---|---|
| Front matter, title, filename, separators | Identity, internal authority/state, relationships, and document furniture | Bind identity/provenance deterministically; exclude document furniture from atoms. Internal labels remain scoped evidence, not self-ratifying authority. |
| Opening typography doctrine | Typography as semantic information rather than decoration | Authorial Grammar; eligible for `evidence_authorial_rule`. |
| I. Status and Relationship to the MSID Grammar | Boundary between semantic address and authored display; guide scope; paired and derived artifacts | Authorial Grammar owns prose/display boundary; MSID Grammar owns ontology; Phonebook plate is derived only. |
| II. Core Authorial Doctrine | Six written forms plus the Bare Core-Species Singular | Authorial Grammar owns written-form classification; referenced game concepts retain their substantive owners. |
| III. Initial Caps | Defined-Term test, non-emphasis rule, ordinary/defined coexistence, multiword casing | Authorial Grammar; eligible authorial rules. |
| IV. Experiential Operators in ALL CAPS | Register/operator presentation, species operators, ordinary verbs, no ALL-CAPS emphasis | Authorial Grammar owns casing and prose distinction; P&A, Human Rulings, and system owners constrain operator identity and meaning. Do not emit game-semantic ownership from this section. |
| V. MSID Display | Dot-delimited UpperCamelCase display, inline-code styling, prose/MSID mapping, readability | Authorial Grammar owns display in prose; MSID Grammar owns path and segment validity. |
| VI. Core-Species Names | Canonical singular/plural forms, retired Wood Mouse usage, canonical-vs-zoological casing | Authorial Grammar owns prose form; historical quotation and zoological contexts remain qualifiers. |
| VII. Bare Core-Species Singular | Marked construction, meaning, plural boundary, article-bearing individuals, agreement, restraint | Authorial Grammar; eligible authorial rules with all usage qualifiers preserved. |
| VIII. Hyphen-bound Animal-Language Compounds | Translation premise, casing, MSID mapping, controlled adoption, search aliases | Authorial Grammar owns canonical prose orthography; MSID Grammar owns machine-safe segment validity; aliases are implementation/index aids, not alternate canon. |
| IX. Defined Text Treatments | Stability test, provisional italics convention, competing-use constraint | Authorial Grammar; stability criteria are active guidance, while mechanics-teaching Narrative italics remains explicitly `PROVISIONAL`. |
| X. Emergent Grammar | Extensibility, statuses, promotion test, future grammar-log fields | Authorial Grammar owns the convention lifecycle. No observed/provisional convention becomes settled without explicit human adoption. |
| XI. Voice and Density | Plain activity before formal name, definitions, term consistency, legible poetic license | Authorial Grammar; eligible authorial guidance. |
| XII. Authoring Examples | Conforming, nonconforming, and corrected examples | Supporting and regression evidence for nearby rules; examples do not independently create mechanics or ontology. |
| XIII. Authoring Checklist | Twelve acceptance checks | Operational authorial-rule evidence; checklist form and dependencies must be preserved. |
| XIV. Machine-checkable Lint Rules | Prospective flags and warnings, including context-sensitive exceptions | Authorial lint requirements and examples; “should eventually” is prospective and must not be recast as proof of an implemented tool. |
| XV. Phonebook Appendix Plate | Proposed one-page condensation, table, and footer doctrine | Authorial Grammar owns derivation/non-independence and wording guidance. Final publication implementation is outside the allowed stream and remains with Appendix/Phonebook controls. |
| XVI. Current Convention Ledger | Settled/provisional statuses and owner labels | Preserve record-level status and joint-owner qualifiers. Self-recorded `SETTLED` status remains source evidence subject to Human Rulings conformance. |
| Change Record | v0.1 development summary | Exclude from atomic extraction under Gate 2; retain as deterministic provenance/document history. |

## 7. Mixed, provisional, prospective, and derived regions

1. **Whole-document state:** `ACTIVE_WORKING_GUIDE`. This describes the source as a working guide; it does not erase record-level status distinctions.
2. **Mechanics-teaching Narrative italics:** explicitly `PROVISIONAL`. It may be extracted only with that qualifier and must never be normalized to settled or mandatory.
3. **Emergent conventions:** `OBSERVED`, `PROVISIONAL`, `SETTLED`, and `RETIRED` are lifecycle values. A lifecycle definition is not evidence that an unnamed convention currently occupies that state.
4. **Machine-checkable linting:** prospective (`should eventually flag`). It establishes intended lint behavior, not current implementation or validation capability.
5. **Controlled Hyphen-bound list and grammar log:** future-maintenance structures. Empty or illustrative templates do not establish additional canonical terms.
6. **Phonebook grammar plate:** settled as a derived publication architecture in the source ledger, but still non-independent and `publication_only` for media/publication disposition.
7. **Examples and code/YAML fragments:** examples, mappings, tests, or templates must retain their local function and must not be flattened into unsupported independent rules.

## 8. Exclusions and non-extractable material

Gate 2 requires exclusion of:

- `document_furniture`: YAML delimiters and purely bibliographic/front-matter fields when they do not carry a substantive identity or authority qualifier; duplicate title and filename display; thematic separators; and structural heading text considered apart from its governed content; and
- `change_record`: the complete final `# Change Record` region, retained as provenance rather than authorial-rule atoms.

These category decisions do not yet constitute block-level extraction dispositions. Exact block accounting belongs to the later offline phase after this card is reviewed and author-approved.

The following must also remain outside this source's extraction stream:

- game-mechanical claims inferred from examples;
- ontology/path-validity claims owned by MSID Grammar;
- cross-source authority or reconciliation conclusions;
- final Phonebook layout/publication records;
- implied conventions inferred from typography without an explicit stable function; and
- alternate search forms treated as canonical orthography.

## 9. Tables, figures, captions, and media references

The source contains Markdown tables, fenced examples, block quotations, and a proposed appendix-plate table. These are structural text evidence, not embedded visual media, and require table-aware preservation during later offline planning.

No embedded image, figure, audio, video, or external media asset appears in the bound source. The only publication/media reference is the planned one-page Phonebook appendix plate. Its terminal identity-stage disposition is `publication_only`: the source may establish that the plate is derived and non-independent, but the plate is not an embedded artifact and cannot enter a provider request as external material.

## 10. Predecessor and coverage warnings

- No standalone Authorial Grammar predecessor is identified. This card makes no claim that v0.1 captures every earlier prose convention or authoring discussion.
- The Human Rulings group supplies direct decision provenance but is an active, incomplete ledger. Its incompleteness must not be filled with model inference.
- The current source contains examples and summarized operator/MSID statements that cross ownership boundaries. Source extraction alone cannot prove their cross-source conformance.
- The source's self-recorded convention ledger and change record are not substitutes for the mandatory post-extraction Human Rulings conformance gate.
- Repository history proves inclusion from the reorganization commit onward; it does not establish complete pre-repository genealogy.

## 11. Approval resolution

Asa Wember approved the source identity and section-level ownership boundaries.
The allowed stream remains `evidence_authorial_rule`; the Change Record remains
excluded; provisional, prospective, example, table, lint, and publication-only
material retain the qualifications stated above. Post-extraction conformance
against applicable Human Rulings authorial evidence remains mandatory before
source-bounded candidate acceptance.

## 12. Current transition boundary

This approved artifact settles source identity only. It does not itself authorize
source work, provider/model calls, retries, spending, Google Sheets interaction,
Layer E semantic review or acceptance, mapping, reconciliation, canonization,
compiled prose, or work on another source. Those permissions remain governed by
the root contract and canonical compile state.
