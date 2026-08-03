---
title: "MEDIAN v0.5.0 Human Rulings Ledger"
document_id: M050-HUMAN-RULINGS-001
document_version: 0.1
game_target: MEDIAN v0.5.0
document_kind: human_rulings_ledger
authority: highest_for_explicit_human_rulings_recorded_here
state: ACTIVE_INCOMPLETE
publication_default: internal
created: 2026-08-01
supersedes:
  - M050_Human_Rulings_Ledger_Preparation_v0_1_MEDIANv0_5_0.md
---

# MEDIAN v0.5.0
## Human Rulings Ledger

**File:** `M050_Human_Rulings_Ledger_v0_1_MEDIANv0_5_0.md`

> This ledger records decisions made by the designer. It outranks model-authored claims, document self-labels, provisional namespace entries, and inferred precedence within the scope of each ruling.

## 1. Purpose and authority

This document separates actual human decisions from the large body of model-generated specifications, audits, summaries, and proposed terminology produced during development.

A ruling in this ledger may:

- establish game canon;
- correct a mistaken ontology or term;
- define source authority within a scope;
- deprecate a concept;
- establish lineage;
- govern compilation and extraction;
- or establish Sourcebook publication architecture.

This ledger is **active but incomplete**. Version 0.1 records the explicit rulings recoverable from the current corpus-and-namespace thread. BSA-01 through BSA-22 remain settled design history, but their exact human decision carriers must still be ingested rather than replaced by model summaries.

## 2. Admissibility and interpretation

1. A model-written sentence is not a human ruling merely because the designer did not object.
2. Direct corrections, explicit approvals, and unambiguous restatements are admissible.
3. A brief assent such as “Agree” adopts only the clearly presented proposition under discussion.
4. Human rulings outrank document labels such as `CANONICAL`, `SETTLED`, `development-lock`, or `specification`.
5. One section of a document may receive scoped authority without promoting the entire document.
6. Exact human wording is preserved separately from the normalized operational rule.
7. When the exact positive rule remains incomplete, the ledger records the gap instead of completing it by inference.
8. Developmental origin is not the same as current document class.
9. Publication, ontology, and compiler rulings must not be misclassified as gameplay mechanics.

## 3. Ruling classes

| Class | Meaning |
| --- | --- |
| `CANON_RULE` | Establishes a player-facing or persistent game rule. |
| `CORRECTION` | Replaces an erroneous model or document claim. |
| `TERMINOLOGY` | Establishes a canonical name, spelling, hierarchy, or distinction. |
| `AUTHORITY_SCOPE` | Establishes which source or section governs a domain. |
| `DEPRECATION` | Removes a concept or name from active use without requiring an immediate replacement. |
| `LINEAGE` | Establishes development history or parentage. |
| `PROCESS` | Governs compilation, extraction, versioning, file handling, or adjudication. |
| `PUBLICATION_ARCHITECTURE` | Governs Sourcebook organization and presentation depth. |
| `ADVISORY_DIRECTION` | Strong adopted direction that is not yet a complete mechanical rule. |

# 4. Lineage and corpus history

## HR-LIN-001 — Home Loop Rework begins v0.5

- **Date:** 2026-08-01
- **Class:** `LINEAGE`
- **Status:** `SETTLED`
- **Exact statement:** “These are the 4.7 docs before 0.5.0 Home Loop Rework, the first document of what I consider to be 0.5.”
- **Normalized ruling:** The uploaded intended-v0.4.7 documents predate the true v0.5 design generation. Home Loop Rework is the first document the designer considers genuinely v0.5, regardless of inherited filename or internal target labels.
- **Authority effect:** Corrects document genealogy and version classification.
- **Affected sources:** intended-v0.4.7 decisions; spatial review; Home Loop Rework; legacy concordance; future corpus manifest.
- **Semantic scope:** corpus lineage.

## HR-LIN-002 — FourSeven and BSA as contamination barriers

- **Date:** 2026-08-01
- **Class:** `LINEAGE`
- **Status:** `SETTLED`
- **Exact statement:** “Yes they're there as old, but the intention of FourSeven and the BSA (covering different phases of the 0.4.7 docs, along with maybe even one more spec?) was to preserve their learnings so they (047 decisions) didn't contaminate further development with old ideas.”
- **Normalized ruling:** FourSeven and the BSA work were created to salvage useful discoveries from the intended-v0.4.7 phase while preventing obsolete architecture from re-entering later v0.5 development.
- **Authority effect:** Quarantines original v0.4.7 sources after their surviving material is reconciled into current owners.
- **Affected sources:** V6/V7 decisions; FourSeven; BSA audit and ledgers; descendant specifications.
- **Semantic scope:** corpus lineage and source disposition.

## HR-LIN-003 — BSA branches may become dedicated systems

- **Date:** 2026-08-01
- **Class:** `LINEAGE`
- **Status:** `SETTLED`
- **Exact statement:** “Lineagewise, the BSA returns from 0.4.7 as I read them resulted in several massive tangents resulting in dedicated 0.5 Spec Docs -- what's called BSA11 was a fifty round development of entire families of systems.”
- **Normalized ruling:** The BSA was a branch-generating development process. A BSA number records the origin of a question, not the final class, scale, or authority of the system developed from it. BSA-11 became a dedicated family of Personal Item, Tool, Supply, Keepsake, Focus, Launch, Strain, provenance, and loss systems.
- **Authority effect:** Prevents BSA-derived specifications from being downgraded to audit notes.
- **Affected sources:** Personal Items specification; BSA-12–22 consolidation; BSA audit and disposition ledger; corpus manifest.
- **Semantic scope:** corpus lineage and document classification.

# 5. Governing philosophy

## HR-PHIL-001 — Merge the two philosophy generations

- **Date:** 2026-08-01
- **Class:** `AUTHORITY_SCOPE`
- **Status:** `IMPLEMENTED`
- **Exact statement:** “And add to the list please compare the two documents Philosophy Spec 0.5 & Philosophy Architecture and make one. The 0.5 Spec was made early about the difference between 0.4 and a nascent 0.5; the Architecture was made close to the end of the process, about the entire game overall.”
- **Normalized ruling:** The early Philosophical Specification and late Philosophical Architecture are successive generations of one constitutional source and must be merged into one active present-tense philosophy document.
- **Authority effect:** Merges and supersedes the two earlier philosophy documents as active standalone authorities.
- **Affected sources:** early Philosophical Specification; Philosophical Architecture v2.0; `M050_Governing_Philosophy_and_Architecture_v1_0_MEDIANv0_5_0.md`.
- **Semantic scope:** `Philosophy.*`; `Architecture.*` at constitutional level.

## HR-PHIL-002 — Philosophy history belongs in a silent endnote

- **Date:** 2026-08-01
- **Class:** `PUBLICATION_ARCHITECTURE`
- **Status:** `IMPLEMENTED`
- **Exact statement:** “Do this -- end-note it. Keep it out of the body of the ‘present tense’ philosophy doc, for purity, but make it avail of searches for.”
- **Normalized ruling:** The merged philosophy body presents only the current game. Developmental derivation remains searchable in a `STATE: SILENT` endnote omitted from normal publication.
- **Authority effect:** Separates present-tense canon from provenance without destroying searchability.
- **Affected sources:** merged philosophy document; compiler publication states.
- **Semantic scope:** philosophy publication and provenance.

## HR-PHIL-003 — Philosophy and Architecture are distinct domains

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “Agree.”
- **Adopted proposition:** Philosophy and Architecture are distinct top-level Semantic ID domains. Philosophy contains constitutional values and cross-system constraints; Architecture contains structural facts such as Modes, Registers, scales, cycles, and topology. `Conservation of Systems` belongs at `Philosophy.Pillar.ConservationOfSystems`.
- **Normalized ruling:** Use `Philosophy.*` for the game's governing commitments and `Architecture.*` for the structural ontology that realizes them.
- **Authority effect:** Prevents Pillars from being misclassified as structural components.
- **Affected sources:** Semantic ID Grammar; merged philosophy; future Semantic Registry.
- **Semantic scope:** `Philosophy.*`; `Architecture.*`.

# 6. File and version process

## HR-FILE-001 — M050 cleaned-corpus nomenclature

- **Date:** 2026-08-01
- **Class:** `PROCESS`
- **Status:** `SETTLED`
- **Exact statement:** “I want to adopt a new file nomenclature with M050_ as the prefix followed by the content heavy name part of the name at the front, for ease of iPhone reading, and MEDIANv0_5_0 at the end. This will also help keep files clear from pre canon redo.”
- **Normalized ruling:** Cleaned v0.5.0 corpus files use `M050_` first, the content-heavy title next, document version with underscores, and `_MEDIANv0_5_0` at the end.
- **Authority effect:** Establishes the naming convention for canon-redo artifacts.
- **Affected sources:** all new M050 files; future corpus manifest.
- **Semantic scope:** file and build process only.

# 7. Crossing, Highway, and RISK

## HR-CROSS-001 — Crossing is an Away system, not a Register

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `SETTLED`
- **Exact statement:** “Highway is the world manifestation of Crossing:RISK (is there a better verb for Crossing?)”
- **Clarifying statement:** “Verb doesn't enter the namespace. The namespace name is Home.Colony.Practice.Garden, and it's staffed by a Home.Colony.Role.Gardener. All of this happens ‘in DWELL’. In Crossing, it's ‘Away.Crossing.Phase.Observe’ and the act that describes is one of RISK.”
- **Normalized ruling:** Highway is the world manifestation of Crossing. Crossing is an Away system with semantic phases such as `Away.Crossing.Phase.Observe`. Activity in those phases is an expression of the Risk Register and its operator `RISK`; Crossing is not itself a Register and does not require a universal namespace verb.
- **Authority effect:** Supersedes `Crossing Register`, `Away.RISK.Crossing`, and other ontology/operator collapses.
- **Affected sources:** Away; Crossing working specification; provisional namespace; legacy concordance; Semantic ID Grammar.
- **Semantic scope:** `Away.Crossing.*`; `World.*`; `Architecture.Register.*`.

# 8. Home, Chronicle, and recognition

## HR-HOME-001 — Gathering Place, Teacher, and Chronicle are distinct units

- **Date:** 2026-08-01
- **Class:** `CANON_RULE`
- **Status:** `SETTLED`
- **Exact statement:** “Two distinct things. ‘Gathering Place’ (old Story Circle; Circle too rabbity) is a Practice for Teacher Role, and provides diegetic access to the Chronicle, displayed through a View pane.”
- **Normalized ruling:** Gathering Place succeeds Story Circle. It is `Home.Colony.Practice.GatheringPlace`, staffed by `Home.Colony.Role.Teacher`, and provides diegetic access to the Chronicle through a View pane. Gathering Place, Teacher, and Chronicle View are separate semantic units.
- **Authority effect:** Reclassifies Story Circle under current Home ontology and prevents Practice, Role, record, and View from collapsing into one concept.
- **Affected sources:** Home; Overarching; legacy concordance; future Semantic Registry.
- **Semantic scope:** `Home.Colony.Practice.GatheringPlace`; `Home.Colony.Role.Teacher`; Chronicle/View branch pending final path.

## HR-HOME-002 — Place of Pride deprecated

- **Date:** 2026-08-01
- **Class:** `DEPRECATION`
- **Status:** `SETTLED`
- **Exact statement:** “‘Place of Pride’ lets deprecate as a concept for now.”
- **Normalized ruling:** Place of Pride is removed from the active concept inventory until explicitly redesigned.
- **Authority effect:** Deprecates the concept without transferring its prior functions to Gathering Place.
- **Affected sources:** Home; BSA ledgers; Overarching; legacy concordance; provisional namespace.
- **Semantic scope:** Home display and civic-memory concepts.

## HR-MEM-001 — Distinctions and After-names follow meaningful history

- **Date:** 2026-08-01
- **Class:** `CANON_RULE`
- **Status:** `SETTLED`
- **Exact statement:** “Distinction / After-name, yes agree.”
- **Adopted proposition:** Distinctions and After-names may arise from meaningful history at Home or Away and are not restricted to Exposure or contested MEET.
- **Normalized ruling:** A Distinction is a narrow favorable recognition grounded in meaningful events. An After-name is a rarer public recognition of durable life history. Neither requires Away, Exposure, or contested MEET.
- **Authority effect:** Supersedes the old restrictive recognition premise.
- **Affected sources:** FourSeven; Away; BSA memory rulings; merged philosophy; legacy concordance.
- **Semantic scope:** Citizen recognition and memory.

# 9. Language and orthography

## HR-LANG-001 — Hyphen-bound animal-cultural compounds are canonical

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “Full keep and conform fully to Hyphen bound orthography for animal-related concepts which would be ‘one word’ in the squirrel language, explicitly modeled after the theory on Tolkien, explained in an appendix.”
- **Normalized ruling:** Qualifying animal-cultural compounds use canonical Hyphen-bound orthography because they represent one source-language word translated through multiple English elements. The convention is explicitly explained in an appendix using the Tolkien-derived translation model.
- **Authority effect:** Promotes the convention from optional style to canonical orthography.
- **Affected sources:** Appendix Architecture; Semantic Registry; naming banks; all M050 prose.
- **Semantic scope:** language, names, and canonical display forms.

# 10. Outposts, Stopover, and source authority

## HR-AWAY-001 — Latest Outpost work has scoped authority

- **Date:** 2026-08-01
- **Class:** `AUTHORITY_SCOPE`
- **Status:** `SETTLED`
- **Exact statement:** “Latest Outpost work has authority.”
- **Normalized ruling:** The latest Outpost and Stopover treatment controls within that subject, even though its containing document does not receive blanket authority.
- **Authority effect:** Promotes the current Outpost/Stopover section of Overarching Systems within scope.
- **Affected sources:** Overarching Systems; Away; FourSeven; legacy concordance; future corpus manifest.
- **Semantic scope:** Outpost and Stopover.

## HR-AWAY-002 — Stopover remains Away with Muted DWELL presentation

- **Date:** 2026-08-01
- **Class:** `CANON_RULE`
- **Status:** `SETTLED`
- **Exact statement:** “The current ‘Muted DWELL’ look and Away.Encounter.Stopover (a lesser version version of Home.Encounter.Homecoming).”
- **Normalized ruling:** `Away.Encounter.Stopover` remains Away and is a restricted structural analogue of `Home.Encounter.Homecoming`. It may borrow a Muted DWELL presentation, but that presentation does not create Home Mode, DWELL, Residence, civic management, Quiet Equilibrium, or EMBODY.
- **Authority effect:** Settles the mode/presentation distinction and current Stopover identity.
- **Affected sources:** Overarching Systems; Away; FourSeven; Semantic ID Grammar; future Sourcebook.
- **Semantic scope:** `Away.Encounter.Stopover`; `Home.Encounter.Homecoming`.

## HR-AUTH-001 — Overarching Systems is supplementary outside promoted scopes

- **Date:** 2026-08-01
- **Class:** `AUTHORITY_SCOPE`
- **Status:** `SETTLED`
- **Exact statement:** “Agree.”
- **Adopted proposition:** Overarching Systems is supplementary and review-required overall; explicit human rulings may promote individual sections.
- **Normalized ruling:** Overarching Systems has no blanket authority from its self-declared canonical language. Its default status remains supplementary and review-required outside specifically promoted domains.
- **Authority effect:** Constrains source authority while permitting scoped promotions.
- **Affected sources:** Overarching Systems; future Active Corpus and Authority Manifest.
- **Semantic scope:** corpus authority.

# 11. Semantic IDs and ontology

## HR-SEM-001 — Semantic Units belong to MEDIAN

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “Yes the semantic unit is a property of the game, NOT the book.”
- **Normalized ruling:** A Semantic ID identifies a stable property of MEDIAN. Documents, Sourcebook sections, appendices, interfaces, and implementation records may define or reference the unit, but do not create its identity.
- **Authority effect:** Separates game ontology from publication structure.
- **Affected sources:** Semantic ID Grammar; Sourcebook architecture; extraction pipeline; Semantic Registry.
- **Semantic scope:** all semantic branches.

## HR-SEM-002 — Namespace paths identify ontology, not operators

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `SETTLED`
- **Exact statement:** “Verb doesn't enter the namespace. The namespace name is Home.Colony.Practice.Garden, and it's staffed by a Home.Colony.Role.Gardener. All of this happens ‘in DWELL’. In Crossing, it's ‘Away.Crossing.Phase.Observe’ and the act that describes is one of RISK.”
- **Normalized ruling:** Semantic IDs identify defined game objects, classes, phases, processes, and systems. Operators and player verbs remain separate. A verb-shaped word may appear only as the proper name of a semantic object, such as the Observe Phase.
- **Authority effect:** Supersedes paths that insert `DWELL`, `RISK`, or other operators merely because play occurs through them.
- **Affected sources:** provisional namespace; atomic extraction schema; Semantic ID Grammar.
- **Semantic scope:** all semantic branches.

## HR-SEM-003 — Semantic IDs are reader-facing contextual notation

- **Date:** 2026-08-01
- **Class:** `ADVISORY_DIRECTION`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “And this Semantic ID scheme will be such an understanding aid -- it tells the reader EXACTLY how to contextualize what they're currently reading.”
- **Normalized ruling:** Every accepted Semantic ID must explain where the property belongs and what kind of property it is. The hierarchy is an explanatory notation, not merely a database key.
- **Authority effect:** Creates a reader-comprehension acceptance test for the ontology.
- **Affected sources:** Semantic ID Grammar; Sourcebook; future Semantic Registry.
- **Semantic scope:** all semantic branches.

## HR-SEM-004 — Hierarchical rigor is justified by explanatory value

- **Date:** 2026-08-01
- **Class:** `ADVISORY_DIRECTION`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “It alone justifies our rigid hierarchical architecture.”
- **Normalized ruling:** MEDIAN's rigid hierarchy is justified because each Semantic ID can expose mode/domain, governing subject, class, and unit at a glance. A segment that adds no contextual understanding should not be retained.
- **Authority effect:** Establishes a burden of proof for hierarchy depth and new branches.
- **Affected sources:** Semantic ID Grammar; ontology extraction; Sourcebook design.
- **Semantic scope:** architecture of the semantic registry.

## HR-SEM-005 — Register IDs use nouns, not all-caps operators

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `PARTLY_SETTLED`
- **Exact statement:** “This is not quite right -- this should be Architecture.Register.Colony and .Embody (in noun form, not all capped as a verb. Also Embody probably needs a better Noun or VERB).”
- **Normalized ruling:** A Register's Semantic ID uses its noun-form semantic name, not its all-caps operator. `Architecture.Register.Colony` replaces `Architecture.Register.DWELL`. The final noun paired with operator `EMBODY` remains to be confirmed; `Embodiment` is the current working candidate, not yet a final human ruling.
- **Authority effect:** Corrects Register namespace grammar and preserves the unresolved Embodiment naming question.
- **Affected sources:** Semantic ID Grammar; merged philosophy; future Semantic Registry.
- **Semantic scope:** `Architecture.Register.*`.

## HR-SEM-006 — Historical source terminology is not trusted ontology

- **Date:** 2026-08-01
- **Class:** `PROCESS`
- **Status:** `SETTLED`
- **Exact statement:** “With the understanding by the judgement parsing brain that in devo I had no discipline with the term and mixed them up badly.”
- **Normalized ruling:** During extraction and adjudication, legacy uses of Register, Mode, View, Encounter, Phase, system, action, verb, Place, Practice, Project, and related labels are evidence but not authority. Preserve the source wording, then classify the described property by current function, current owners, governing architecture, and human rulings.
- **Authority effect:** Requires literal extraction plus judgmental reclassification rather than mechanical trust in historical labels.
- **Affected sources:** all pre-cleaned specifications; atomic extraction pipeline; Semantic ID Grammar.
- **Semantic scope:** corpus-wide adjudication.

## HR-SEM-007 — Philosophy is not Architecture

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “Agree.”
- **Adopted proposition:** `Philosophy.*` contains constitutional thesis, Pillars, cross-system Principles, and Protections. `Architecture.*` contains Modes, Registers, scales, cycles, and topology. `Conservation of Systems` is `Philosophy.Pillar.ConservationOfSystems`.
- **Normalized ruling:** Philosophy constrains Architecture; Architecture organizes the concrete game ontology. They remain separate top-level Semantic ID domains.
- **Authority effect:** Establishes two primary ontology branches and the location of Conservation of Systems.
- **Affected sources:** Semantic ID Grammar; merged philosophy; future Semantic Registry.
- **Semantic scope:** `Philosophy.*`; `Architecture.*`.

# 12. Sourcebook publication architecture

## HR-SB-001 — Core sections display the unit's Semantic ID

- **Date:** 2026-08-01
- **Class:** `PUBLICATION_ARCHITECTURE`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “These will likely be literal Sourcebook section index ids, at each section.”
- **Later correction:** “Yes the semantic unit is a property of the game, NOT the book.”
- **Normalized ruling:** The Sourcebook may display the game's Semantic ID beneath each core reader-facing heading. The section does not own or create the ID; it presents the semantic unit.
- **Authority effect:** Establishes the relation between ontology and page design.
- **Affected sources:** Sourcebook architecture; Semantic ID Grammar.
- **Semantic scope:** publication use of all semantic units.

## HR-SB-002 — Dual-depth Sourcebook and Phonebook Appendixes

- **Date:** 2026-08-01
- **Class:** `PUBLICATION_ARCHITECTURE`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “The main book presents all of the stuff, but at a tighter, more core level, and each core book section heading is ‘GARDENERS - Home.Colony.Role.Gardeners’, and then in ‘Part 2: the Phonebook Appendixes’ sections are ID'd by their namespace name.”
- **Normalized ruling:** Part I presents each semantic unit in a concise, experiential, reader-facing form. Part II, the working-title Phonebook Appendixes, is organized directly by Semantic ID and may provide in-depth mechanical, eventually tuned, authoring, edge-case, and back-end explanation.
- **Authority effect:** Establishes a dual-depth publication structure over one canon.
- **Affected sources:** Appendix Architecture; Sourcebook TOC; Semantic Registry.
- **Semantic scope:** publication architecture.

## HR-SB-003 — Part I and Part II are views of one rule

- **Date:** 2026-08-01
- **Class:** `PUBLICATION_ARCHITECTURE`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “I actually think this opens up a massive Sourcebook organization opportunity ... with some of the more in-the-weeds and also back-end processes (like Jostle) ... explained in mechanical (eventually tuned) detail.”
- **Normalized ruling:** Core and Phonebook presentations must point to the same semantic unit. Part I may compress; Part II may specify. Neither may create a competing version of the rule.
- **Authority effect:** Prevents appendix mechanics from becoming a second canon.
- **Affected sources:** Sourcebook architecture; appendix plan; compiler cross-reference system.
- **Semantic scope:** all published semantic units.

# 13. Open and incomplete rulings

## OPEN-HOME-001 — Community Board

The designer established that Community Board is distinct from Gathering Place, but has not yet provided its complete positive current function.

- **Current proposal requiring human adjudication:** Community Board is a constructed diegetic display of selected Almanac information in DWELL while the Almanac remains independently accessible.
- **Status:** `OPEN`
- **Do not infer:** Do not merge Community Board into Gathering Place or Chronicle solely from proximity in old sources.

## OPEN-SEM-001 — Noun for the EMBODY Register

- **Settled:** The Semantic ID must use a noun-form Register name and remain separate from all-caps operator `EMBODY`.
- **Working candidate:** `Architecture.Register.Embodiment`.
- **Status:** `OPEN_NAMING`
- **Do not infer:** `Architecture.Register.EMBODY` is rejected; `Architecture.Register.Embodiment` is not yet recorded as an explicit human choice.

# 14. Pending ingestion: BSA-01 through BSA-22

The following settled decision families must be added after exact human statements or clearest direct confirmations are recovered:

- Laws, Sayings, literacy, Chronicle, Tales, Prior-Life Tales, Fear Memory, Distinctions, After-names, and Keepsakes;
- stocks, body units, Carry, Sustenance, Artifacts, and personal slots;
- Places, Practices, Projects, Permissions, recipes, Provisioning, and Civic Projects;
- Tool classes, Supply classes, Focus, Strain, Keepsake effects, and fixed Launch loadout;
- removal of formal Node Study/Knowledge;
- direct world-state discovery;
- continuous corridor and permanent founding Home;
- seasons and weather within existing systems;
- DAWN, Day Bands, and Time Marks;
- Rabbit TRAVEL progress and Crossing acuity;
- Tier recognition and civic proofs;
- Keepsake inheritance or memorial display after Away death.

Until those entries are ingested, their dedicated specifications and accepted decision records remain the positive system carriers. This ledger must not fabricate exact human quotations from later summaries.

# 15. Operational consequences

1. The Active Corpus and Authority Manifest must cite this ledger when classifying Home Loop, FourSeven, BSA descendants, Overarching Systems, and legacy sources.
2. Atomic extraction must preserve source wording and source-declared class separately from adjudicated class.
3. Candidate Semantic IDs are attached during extraction, but become canonical only after cross-source adjudication.
4. Historical documents remain searchable and citable for provenance; they do not originate active gameplay claims after quarantine.
5. Sourcebook sections display Semantic IDs as contextual aids but do not create semantic units.

---

## Change record

### v0.1 — 2026-08-01

- Promoted the preparation schema into an active Human Rulings Ledger.
- Recorded explicit lineage, philosophy, file-naming, Crossing, Home, language, recognition, Outpost, authority, Semantic ID, and Sourcebook rulings from the current thread.
- Preserved exact human wording separately from normalized operational rulings.
- Left Community Board and the noun paired with `EMBODY` explicitly open.
- Deferred BSA-01 through BSA-22 ingestion until exact human decision carriers can be recovered.
