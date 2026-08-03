---
title: "MEDIAN v0.5.0 Human Rulings Ledger"
document_id: M050-HUMAN-RULINGS-001
document_version: 0.4
game_target: MEDIAN v0.5.0
document_kind: human_rulings_ledger
authority: highest_for_explicit_human_rulings_recorded_here
state: ACTIVE_INCOMPLETE
publication_default: internal
created: 2026-08-01
revised: 2026-08-01
supersedes:
  - M050_Human_Rulings_Ledger_v0_3_MEDIANv0_5_0.md
  - M050_Human_Rulings_Ledger_v0_2_MEDIANv0_5_0.md
  - M050_Human_Rulings_Ledger_v0_1_MEDIANv0_5_0.md
  - M050_Human_Rulings_Ledger_Preparation_v0_1_MEDIANv0_5_0.md
---

# MEDIAN v0.5.0
## Human Rulings Ledger

**File:** `M050_Human_Rulings_Ledger_v0_4_MEDIANv0_5_0.md`

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

This ledger is **active but incomplete**. Version 0.4 records the explicit rulings recoverable from the current corpus, namespace, authority, Crossing-pilot, and authorial-grammar threads. BSA-01 through BSA-22 remain settled design history, but their exact human decision carriers must still be ingested rather than replaced by model summaries.

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
- **Adopted proposition:** Philosophy and Architecture are distinct top-level MSID domains. Philosophy contains constitutional values and cross-system constraints; Architecture contains structural facts such as Modes, Registers, scales, cycles, and topology. `Conservation of Systems` belongs at `Philosophy.Pillar.ConservationOfSystems`.
- **Normalized ruling:** Use `Philosophy.*` for the game's governing commitments and `Architecture.*` for the structural ontology that realizes them.
- **Authority effect:** Prevents Pillars from being misclassified as structural components.
- **Affected sources:** MSID Grammar; merged philosophy; future Semantic Registry.
- **Semantic scope:** `Philosophy.*`; `Architecture.*`.

## HR-PHIL-004 — Game Logic Precedes Attachment is the eighth Pillar

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `SETTLED`
- **Exact statement:** “a tweak on Philosophy.Principles.LegibilityPreceedArtachmenr is actually a late added Pillar. And it should have been GamelogicPreceedsAttachment which is the pillar that if the Player is worried about colony mechanics, they don't have the headspace to fully appreciate Attachment-forward aspects, so all Attachment-forward systems must have a gane mechanic aspect.”
- **Normalized ruling:** The constitutional unit is `Philosophy.Pillar.GameLogicPrecedesAttachment`. Legibility remains the first link in the attachment chain rather than a separate Pillar or Principle. A substantial or repeatable attachment-forward system must perform genuine Game Logic work so that the player's mechanical concerns can become understood and stable enough to release attention toward Attachment.
- **Authority effect:** Supersedes `Philosophy.Principle.LegibilityPrecedesAttachment` and any framing that treats attachment systems as mechanically exempt.
- **Affected sources:** Governing Philosophy and Architecture; MSID Grammar; Embodiment; Sourcebook.
- **Semantic scope:** `Philosophy.Pillar.GameLogicPrecedesAttachment`.

## HR-ARCH-001 — The five Registers include Field, not Travel

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `SETTLED`
- **Exact statement:** “Canonical Registers are Colony, Field, Crossing, Encounter, and Embodiment -- not Travel. TRAVEL is Field Register verb.”
- **Normalized ruling:** MEDIAN's five Registers are Colony, Field, Crossing, Encounter, and Embodiment. Field's architectural MSID is `Architecture.Register.Field`, its substantive MSID is `Away.Field`, and its operator is `TRAVEL`. `Architecture.Register.Travel` and `Away.Travel` are superseded terminology.
- **Authority effect:** Corrects the Register table and all current MSID examples.
- **Affected sources:** Governing Philosophy and Architecture; MSID Grammar; Away; FourSeven; Active-Owner Conformance Directive; future registry.
- **Semantic scope:** `Architecture.Register.Field`; `Away.Field`.

## HR-ARCH-002 — Body Unit is MEDIAN's cross-species equivalency scale

- **Date:** 2026-08-01
- **Class:** `CANON_RULE`
- **Status:** `SETTLED`
- **Exact statement:** “the Body-Unit principle (basically Mouse has general numeric equivalency the other two with the individual 2x Citizen count) needs to be detailed somewhere in Phil or Arch and it's not as of now.”
- **Normalized ruling:** Body Unit is an architectural scale at `Architecture.Scale.BodyUnit`. One Rabbit, one Squirrel, or two Mice constitute one Body Unit. Where MEDIAN compares general expedition footprint, collective action bandwidth, or another explicitly body-unit-based quantity, one Mouse pair is generally equivalent to one Rabbit or one Squirrel while containing twice the number of named Citizens.
- **Equal-personhood rule:** Two Mice in one Body Unit remain two complete equal Citizens. Each retains individual identity, personal items where their owners allow them, relationships, wounds, adversity, memory, Tale, recovery, and death. Body-unit equivalency is never half-personhood.
- **Boundary:** Body Unit does not make every species number identical. Dedicated owners may define species-specific Carry, movement, risk expression, and other traits. Additional Mouse Citizens do not automatically double collective party actions, Supplies, Cargo, MEET Turns, or Crossing activations.
- **Authority effect:** Places the Body-Unit principle in Architecture rather than leaving it as an isolated logistics rule.
- **Affected sources:** Governing Philosophy and Architecture; MSID Grammar; Core Species Traits; Away; Crossing; Population; future registry.
- **Semantic scope:** `Architecture.Scale.BodyUnit`.

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

## HR-FILE-002 — Canonical M050 filenames become the permanent current names

- **Date:** 2026-08-01
- **Class:** `PROCESS`
- **Status:** `SETTLED`
- **Exact statement:** “Then we use those new names forever onward.”
- **Normalized ruling:** After the approved filename-only repository migration, the canonical `M050_` filename is the only current filename used by live references. A legacy filename may remain only in Git history, `legacy_filename` metadata, migration ledgers, or explicit provenance.
- **Authority effect:** Separates permanent source identity from obsolete working filenames and prevents reintroduction of mixed nomenclature.
- **Affected sources:** Active Corpus and Authority Manifest v0.2; File Nomenclature Migration Ledger; repository links, indexes, scripts, and future documents.
- **Semantic scope:** file and build process only.

# 7. Crossing, Highway, and RISK

## HR-CROSS-001 — Crossing is a Register; RISK is its operator

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `SETTLED`
- **Exact statement:** “HR-CROSS-001 is wrong. Crossing is a Register, one of five. Its verb is RISK. It's SID is Away.Crossing, and it contains such systems as Away.Crossing.Phase and also Away.Crossing.Rabbit and Away.Crossing.Squirrel because Crossing is forked by Core Species in a way no other Regusters are.”
- **Terminology normalization:** “SID” in the exact statement is now canonically abbreviated `MSID`, for **MEDIAN Semantic Identifier**.
- **Normalized ruling:** Crossing is one of MEDIAN's five Registers. Its all-caps operator is `RISK`. Its substantive MSID is `Away.Crossing`; Highway is its world manifestation. `Away.Crossing` is both a defined semantic unit and the parent branch for Crossing's internal ontology, including `Away.Crossing.Phase` and Core-Species forks such as `Away.Crossing.Rabbit` and `Away.Crossing.Squirrel`. Crossing is uniquely species-forked among the Registers.
- **Architecture relation:** `Architecture.Register.Crossing` may summarize Crossing's structural status and refer to `Away.Crossing`; it is not a competing mechanical owner.
- **Prior ledger error:** v0.1 incorrectly normalized Crossing as a non-Register system expressed through a separate Risk Register. That normalization is superseded.
- **Authority effect:** Restores the source specification's Register class; supersedes `Architecture.Register.Risk`, the claim that Crossing is not a Register, and paths such as `Away.RISK.Crossing`.
- **Affected sources:** Away; Crossing specification; provisional namespace; legacy concordance; MSID Grammar; merged philosophy's Register table.
- **Semantic scope:** `Away.Crossing.*`; `Architecture.Register.Crossing`; `World.*`.

## HR-AWAY-003 — Ordinary expeditions use three Body Units with a two-unit early-game exception

- **Date:** 2026-08-01
- **Class:** `CANON_RULE`
- **Status:** `SETTLED`
- **Exact statement:** “Body unit is three as a standard and maximum with an allowable exception of two body units, primarily to be untilized in early game when population is quite low.”
- **Normalized ruling:** An ordinary expedition is built to a standard and maximum of three Body Units. A two-Body-Unit expedition is an allowable exception, intended primarily for early play when the Colony's population is too low to field the full standard party.
- **Interpretive consequence:** “Three Body Units” in Crossing and Core Species Traits describes the standard full party and ordinary maximum; it does not prohibit the explicit two-unit exception. “Two to three Body Units” remains accurate only when the distinction between exception and standard is preserved.
- **Boundary:** Parties larger than three Body Units are not ordinary expedition parties. Any larger formation must be a specific authored exception rather than permanent cap progression.
- **Authority effect:** Reconciles the Crossing/Core Traits fixed-three wording with the prior two-to-three expedition range.
- **Affected sources:** Crossing; Core Species Traits; Away; BSA disposition records; Crossing Atomic Extraction Pilot; Governing Philosophy and Architecture.
- **Semantic scope:** `Architecture.Scale.ExpeditionParty`; `Architecture.Scale.BodyUnit`.

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

## HR-HOME-003 — Community Board is the Leadership Practice for the Almanac

- **Date:** 2026-08-01
- **Class:** `CANON_RULE`
- **Status:** `SETTLED`
- **Exact statement:** “OPEN-HOME-001 - the Community Board is an example of the third kind of Practice associated with Leadership. It's the diegetic source for Almanac material (current game & conditions) mirroring the Gathering Place as a diegetic source for Chronicle (history).”
- **Normalized ruling:** Community Board is `Home.Colony.Practice.CommunityBoard`, an example of the third kind of Practice and associated with Leadership. It provides diegetic access to Almanac material concerning the current game state and present conditions. It mirrors `Home.Colony.Practice.GatheringPlace`, which provides diegetic access to the Chronicle as history.
- **Authority effect:** Closes `OPEN-HOME-001`; establishes Community Board's positive function without merging Almanac and Chronicle or Community Board and Gathering Place.
- **Affected sources:** Home; Overarching Systems; legacy concordance; MSID Grammar; future Semantic Registry and Sourcebook.
- **Semantic scope:** `Home.Colony.Practice.CommunityBoard`; Leadership branch pending exact MSID; Almanac and Chronicle branches pending exact MSIDs.

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


## HR-LANG-002 — MEDIAN uses a standalone Authorial Grammar

- **Date:** 2026-08-01
- **Class:** `AUTHORING_PROCESS`
- **Status:** `SETTLED`
- **Exact statement:** “I want to add an explicit prose style guide.”
- **Normalized ruling:** Authorial prose, capitalization, orthography, species agreement, and semantic typography are owned by a standalone `M050_Authorial_Grammar_Orthography_and_Prose_Style_Guide`, paired with but not embedded as Book II of the MSID Grammar.
- **Authority effect:** Separates prose evolution from ontology revision while keeping the two grammars coordinated.
- **Affected sources:** Authorial Grammar; MSID Grammar; Active Corpus and Authority Manifest v0.2; Sourcebook; Phonebook.
- **Semantic scope:** authorial process and prose presentation.

## HR-LANG-003 — Defined Terms use Initial Caps; experiential operators use ALL CAPS

- **Date:** 2026-08-01
- **Class:** `ORTHOGRAPHY`
- **Status:** `SETTLED`
- **Exact statement:** “Significant nouns in the game have initial caps, experiential VERBS are all caps, MSID is Thing.Thing dot separated.”
- **Normalized ruling:** Stable MEDIAN Defined Terms use Initial Caps. Canonical experiential operators use ALL CAPS. MSIDs use dot-delimited UpperCamelCase segments and are normally presented in code style.
- **Interpretive boundary:** Initial Caps mark defined meaning, not mere importance. ALL CAPS is reserved for the operator inventory and is not general emphasis.
- **Authority effect:** Establishes the primary semantic typography of MEDIAN prose.
- **Affected sources:** all active specifications; Sourcebook; Phonebook; future authoring lint.
- **Semantic scope:** authorial orthography.

## HR-LANG-004 — Bare Core-Species Singular is permitted

- **Date:** 2026-08-01
- **Class:** `AUTHORIAL_GRAMMAR`
- **Status:** `SETTLED`
- **Exact statements:**
  - “Species can be referred to by nonplairalized forms ex ‘Mouse builds a Manor House’ means as ‘The Mouse core species builds Manor Houses’.”
  - “Squirrel connects a separated Place” and “Squirrels connect separated Places.” Both are valid.
  - “My mistake -- that should have been ‘builds’ present tense in the Mouse sentence.”
- **Normalized ruling:** MEDIAN permits the Initial-capped singular Core-Species name without an article when one archetypal body expresses that species' characteristic perception, action, spatial logic, or civilizational grammar. This **Bare Core-Species Singular** takes singular agreement: `Mouse builds`, `Rabbit gathers`, `Squirrel connects`.
- **Plural boundary:** `Mice build`, `Rabbits gather`, and `Squirrels connect` remain valid ordinary plural generics.
- **Authority effect:** Adopts a narrow marked house construction without making it mandatory throughout the manuscript.
- **Affected sources:** Authorial Grammar; Ecology; P&A species doctrine; Home; Away; Sourcebook captions and prose.
- **Semantic scope:** Core-Species authorial grammar.

## HR-LANG-005 — Hyphen-bound internal elements remain lowercase

- **Date:** 2026-08-01
- **Class:** `ORTHOGRAPHY`
- **Status:** `SETTLED`
- **Exact statement:** “‘Prior-life Tale’ needs a lower case L in life. This is lifted directly from Lord of the Rings as a two-word hyphenated compound with the first word Capitalized and the second word not.”
- **Normalized ruling:** A Hyphen-bound animal-language word receives one initial capital at the beginning of the translated word; internal English elements remain lowercase. The canonical form is `Prior-life Tale`, not `Prior-Life Tale`. `Tale` is separately capitalized as a Defined Term.
- **MSID mapping:** `Prior-life Tale` maps to the machine-safe segment `PriorLifeTale`.
- **Authority effect:** Clarifies the canonical internal casing of Hyphen-bound compounds.
- **Affected sources:** Authorial Grammar; MSID Grammar; Chronicle and Tale materials; Sourcebook and Phonebook.
- **Semantic scope:** canonical names and display orthography.

## HR-LANG-006 — Authorial grammar may emerge through repeated practice

- **Date:** 2026-08-01
- **Class:** `AUTHORING_PROCESS`
- **Status:** `SETTLED`
- **Exact statement:** “This can develop if more emergent grammar comes to light later (for example mechanics-teaching Narrative snippets are italicized).”
- **Normalized ruling:** The Authorial Grammar is extensible. New conventions are tracked as `OBSERVED`, `PROVISIONAL`, `SETTLED`, or `RETIRED` and require explicit human adoption before becoming mandatory.
- **Current provisional example:** Italics may identify mechanics-teaching Narrative snippets, provided the treatment does not also carry several competing meanings.
- **Authority effect:** Permits genuine manuscript practice to reveal stable grammar without canonizing every local layout choice.
- **Affected sources:** Authorial Grammar; Sourcebook authoring; Narrative presentation; Phonebook.
- **Semantic scope:** authorial process and typography.

## HR-LANG-007 — The Phonebook receives a derived grammar plate

- **Date:** 2026-08-01
- **Class:** `PUBLICATION_ARCHITECTURE`
- **Status:** `SETTLED`
- **Exact statement:** “this will guide our authoring process and then could be a single plate appendix in the Phoneboox appendixes”
- **Normalized ruling:** The complete Authorial Grammar remains the active internal owner. The Phonebook appendixes receive a one-page derived plate summarizing the reader-facing conventions.
- **Authority effect:** Prevents the appendix plate from becoming a second independent style owner.
- **Affected sources:** Authorial Grammar; Appendix Architecture; Phonebook.
- **Semantic scope:** publication architecture.

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
- **Affected sources:** Overarching Systems; Away; FourSeven; MSID Grammar; future Sourcebook.
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

## HR-AUTH-002 — Ecology is an active subsidiary owner, not an unattended biological authority

- **Date:** 2026-08-01
- **Class:** `AUTHORITY_SCOPE`
- **Status:** `SETTLED`
- **Exact statement:** “Yes that's good. Ecology was a layer I didn't fully engage with because I was afraid of letting its biological-strict considerations get into the spec without rogorous evaluation. I think we include as a subsidiary document.”
- **Adopted proposition:** Ecological Influences is active within a narrow translation scope: qualitative bodily priors, perceptions of safety and movement, ecology-versus-civilization boundaries, and privileged-camera doctrine. Dedicated system owners determine mechanical expression.
- **Normalized ruling:** Ecology is an `ACTIVE_SUBSIDIARY_OWNER`. It may define the ecological premises MEDIAN deliberately translates and constrain affected systems, but it may not automatically import biologically strict conclusions, tuned modifiers, or system mechanics without rigorous evaluation and adoption by the appropriate owner.
- **Authority effect:** Includes Ecology in the active corpus while preventing biological literalism from silently entering canon.
- **Affected sources:** Ecological Influences; Active Corpus and Authority Manifest; Home; Away; Crossing; Embodiment; Core Species Traits.
- **Semantic scope:** ecological translation and source authority.

# 11. MSIDs and ontology

## HR-SEM-001 — Semantic Units belong to MEDIAN

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “Yes the semantic unit is a property of the game, NOT the book.”
- **Normalized ruling:** An MSID identifies a stable property of MEDIAN. Documents, Sourcebook sections, appendices, interfaces, and implementation records may define or reference the unit, but do not create its identity.
- **Authority effect:** Separates game ontology from publication structure.
- **Affected sources:** MSID Grammar; Sourcebook architecture; extraction pipeline; Semantic Registry.
- **Semantic scope:** all semantic branches.

## HR-SEM-002 — Namespace paths identify ontology, not operators

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `SETTLED`
- **Exact statement:** “Verb doesn't enter the namespace. The namespace name is Home.Colony.Practice.Garden, and it's staffed by a Home.Colony.Role.Gardener. All of this happens ‘in DWELL’. In Crossing, it's ‘Away.Crossing.Phase.Observe’ and the act that describes is one of RISK.”
- **Normalized ruling:** MSIDs identify defined game objects, classes, phases, processes, and systems. Operators and player verbs remain separate. A verb-shaped word may appear only as the proper name of a semantic object, such as the Observe Phase.
- **Authority effect:** Supersedes paths that insert `DWELL`, `RISK`, or other operators merely because play occurs through them.
- **Affected sources:** provisional namespace; atomic extraction schema; MSID Grammar.
- **Semantic scope:** all semantic branches.

## HR-SEM-003 — MSIDs are reader-facing contextual notation

- **Date:** 2026-08-01
- **Class:** `ADVISORY_DIRECTION`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “And this Semantic ID scheme will be such an understanding aid -- it tells the reader EXACTLY how to contextualize what they're currently reading.”
- **Normalized ruling:** Every accepted MSID must explain where the property belongs and what kind of property it is. The hierarchy is an explanatory notation, not merely a database key.
- **Authority effect:** Creates a reader-comprehension acceptance test for the ontology.
- **Affected sources:** MSID Grammar; Sourcebook; future Semantic Registry.
- **Semantic scope:** all semantic branches.

## HR-SEM-004 — Hierarchical rigor is justified by explanatory value

- **Date:** 2026-08-01
- **Class:** `ADVISORY_DIRECTION`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “It alone justifies our rigid hierarchical architecture.”
- **Normalized ruling:** MEDIAN's rigid hierarchy is justified because each MSID can expose mode/domain, governing subject, class, and unit at a glance. A segment that adds no contextual understanding should not be retained.
- **Authority effect:** Establishes a burden of proof for hierarchy depth and new branches.
- **Affected sources:** MSID Grammar; ontology extraction; Sourcebook design.
- **Semantic scope:** architecture of the semantic registry.

## HR-SEM-005 — Register MSIDs use nouns; Embodiment pairs with EMBODY

- **Date:** 2026-08-01
- **Class:** `CORRECTION`
- **Status:** `SETTLED`
- **Exact statement:** “This is not quite right -- this should be Architecture.Register.Colony and .Embody (in noun form, not all capped as a verb. Also Embody probably needs a better Noun or VERB).”
- **Closing statement:** “let's formalize Embodiment:EMBODY”
- **Normalized ruling:** Register entries use noun-form semantic names, while all-caps operators remain separate. `Architecture.Register.Colony` pairs with `DWELL`; `Architecture.Register.Embodiment` and the substantive branch `Home.Embodiment` pair with `EMBODY`.
- **Authority effect:** Corrects operator-shaped Register paths and closes the Embodiment naming question.
- **Affected sources:** MSID Grammar; merged philosophy; future Semantic Registry.
- **Semantic scope:** `Architecture.Register.*`; `Home.Embodiment`.

## HR-SEM-006 — Historical source terminology is not trusted ontology

- **Date:** 2026-08-01
- **Class:** `PROCESS`
- **Status:** `SETTLED`
- **Exact statement:** “With the understanding by the judgement parsing brain that in devo I had no discipline with the term and mixed them up badly.”
- **Normalized ruling:** During extraction and adjudication, legacy uses of Register, Mode, View, Encounter, Phase, system, action, verb, Place, Practice, Project, and related labels are evidence but not authority. Preserve the source wording, then classify the described property by current function, current owners, governing architecture, and human rulings.
- **Authority effect:** Requires literal extraction plus judgmental reclassification rather than mechanical trust in historical labels.
- **Affected sources:** all pre-cleaned specifications; atomic extraction pipeline; MSID Grammar.
- **Semantic scope:** corpus-wide adjudication.

## HR-SEM-007 — Philosophy is not Architecture

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “Agree.”
- **Adopted proposition:** `Philosophy.*` contains constitutional thesis, Pillars, cross-system Principles, and Protections. `Architecture.*` contains Modes, Registers, scales, cycles, and topology. `Conservation of Systems` is `Philosophy.Pillar.ConservationOfSystems`.
- **Normalized ruling:** Philosophy constrains Architecture; Architecture organizes the concrete game ontology. They remain separate top-level Semantic ID domains.
- **Authority effect:** Establishes two primary ontology branches and the location of Conservation of Systems.
- **Affected sources:** MSID Grammar; merged philosophy; future Semantic Registry.
- **Semantic scope:** `Philosophy.*`; `Architecture.*`.

## HR-SEM-008 — TLDs are containers; root concepts self-root once

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “For me it was mainly to avoid one word TLD. I don't understand Home as necessarily a SID but Home.Home is explicitly so.”
- **Closing statement:** “Drop the convention below TLD so Home.Home stays but Home.Colony.Colony loses the dupe?”
- **Normalized ruling:** A bare Top-Level Domain is a namespace container, not an MSID. Every MSID contains at least two segments. When the broad root concept requires an MSID, it self-roots once, as in `Home.Home`. The repetition convention stops below the TLD; `Home.Colony` is both a valid MSID and a parent branch, while `Home.Colony.Colony` is rejected as empty duplication.
- **Authority effect:** Establishes the Minimum Two-Segment Rule, TLD self-rooting, and branch-as-unit behavior.
- **Affected sources:** MSID Grammar; future Semantic Registry; extraction validators.
- **Semantic scope:** all MSID branches.

## HR-SEM-009 — Runtime instances are not terminal MSID segments

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact question:** “should the Grammar to include a terminal entry that's one single distinct instance, ie Home.Colony.Role.Gardener.Bramble#R002”
- **Adopted disposition:** Runtime entities use separate Entity IDs and relations rather than extending the semantic path.
- **Normalized ruling:** An MSID identifies stable game ontology. A particular Citizen, Colony, Place, Artifact, Route, or other runtime instance receives a separate Entity ID and may be linked to an MSID by a relation such as `holds_role`.
- **Authority effect:** Prevents type ontology and campaign-instance identity from being conflated.
- **Affected sources:** MSID Grammar; extraction schema; future Entity ID Grammar.
- **Semantic scope:** MSID/entity boundary.

## HR-SEM-010 — MEDIAN Semantic Identifier is abbreviated MSID

- **Date:** 2026-08-01
- **Class:** `TERMINOLOGY`
- **Status:** `SETTLED`
- **Exact statement:** “Added just now: Semantic ID abbreviated as MSID (Median Semantic Identifier) (it's a short word that's more unique than SID)”
- **Normalized ruling:** The canonical term is **MEDIAN Semantic Identifier**, abbreviated **MSID**. `SID` is not used as the project abbreviation. Earlier prose saying “Semantic ID” remains intelligible as a legacy term, but new specifications, schemas, and publication references use `MSID`.
- **Authority effect:** Renames the project-specific identifier notation and its short form.
- **Affected sources:** MSID Grammar; Human Rulings Ledger; compiler fields; Sourcebook; Semantic Registry.
- **Semantic scope:** corpus-wide terminology.

# 12. Sourcebook publication architecture

## HR-SB-001 — Core sections display the unit's MSID

- **Date:** 2026-08-01
- **Class:** `PUBLICATION_ARCHITECTURE`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “These will likely be literal Sourcebook section index ids, at each section.”
- **Later correction:** “Yes the semantic unit is a property of the game, NOT the book.”
- **Normalized ruling:** The Sourcebook may display the game's MSID beneath each core reader-facing heading. The section does not own or create the ID; it presents the semantic unit.
- **Authority effect:** Establishes the relation between ontology and page design.
- **Affected sources:** Sourcebook architecture; MSID Grammar.
- **Semantic scope:** publication use of all semantic units.

## HR-SB-002 — Dual-depth Sourcebook and Phonebook Appendixes

- **Date:** 2026-08-01
- **Class:** `PUBLICATION_ARCHITECTURE`
- **Status:** `SETTLED_DIRECTION`
- **Exact statement:** “The main book presents all of the stuff, but at a tighter, more core level, and each core book section heading is ‘GARDENERS - Home.Colony.Role.Gardeners’, and then in ‘Part 2: the Phonebook Appendixes’ sections are ID'd by their namespace name.”
- **Normalized ruling:** Part I presents each semantic unit in a concise, experiential, reader-facing form. Part II, the working-title Phonebook Appendixes, is organized directly by MSID and may provide in-depth mechanical, eventually tuned, authoring, edge-case, and back-end explanation.
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

## OPEN-SEM-002 — Narrative as a Top-Level Domain

The designer proposed a `Narrative` TLD as a possible home for Memory, Records, recognition, and narrativized expression, but did not yet explicitly choose it over a child of Architecture or another ontology.

- **Status:** `OPEN_ARCHITECTURE`
- **Do not infer:** Do not freeze `Narrative.*` or a competing `Memory.*` TLD until explicitly adjudicated.

## OPEN-SEM-003 — Entity ID grammar

The boundary is settled: runtime instances do not become terminal MSID segments. The exact syntax, prefixes, uniqueness rules, and campaign scope of Entity IDs remain to be designed.

- **Status:** `OPEN_GRAMMAR`
- **Do not infer:** The illustrative form `Citizen#R002` is not yet a frozen identifier standard.
# 14. Pending ingestion: BSA-01 through BSA-22

The following settled decision families must be added after exact human statements or clearest direct confirmations are recovered:

- Laws, Sayings, literacy, Chronicle, Tales, Prior-Life Tales, Fear Memory, Distinctions, After-names, and Keepsakes;
- stocks, Carry, Sustenance, Artifacts, and personal slots;
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
3. Candidate MSIDs are attached during extraction, but become canonical only after cross-source adjudication.
4. Historical documents remain searchable and citable for provenance; they do not originate active gameplay claims after quarantine.
5. Sourcebook sections display MSIDs as contextual aids but do not create semantic units.

---

## Change record

### v0.4 — 2026-08-01

- Established the standalone Authorial Grammar as the scoped owner of prose and semantic typography.
- Adopted Initial Caps for Defined Terms and ALL CAPS for experiential operators.
- Adopted the Bare Core-Species Singular with singular agreement.
- Settled exact `Prior-life Tale` casing and Hyphen-bound internal lowercase.
- Established an extensible status lifecycle for emergent authorial conventions.
- Recorded mechanics-teaching Narrative italics as provisional.
- Established the one-page Phonebook grammar plate as a derived publication artifact.

### v0.3 — 2026-08-01

- Recorded `GameLogicPrecedesAttachment` as the eighth Pillar and retired `LegibilityPrecedesAttachment` as an independent Principle.
- Recorded Field, not Travel, as the Register paired with operator `TRAVEL`.
- Established `Architecture.Scale.BodyUnit` and its equal-personhood boundary.
- Settled ordinary expedition scale: three Body Units is the standard and maximum; two is an allowable early-game exception.
- Reconciled the fixed-three and two-to-three source statements without flattening the exception into a second standard.
- Recorded Ecology as an active subsidiary owner with guarded biological authority.
- Recorded the permanent-current-name rule for the approved M050 nomenclature migration.

### v0.2 — 2026-08-01

- Corrected `HR-CROSS-001`: Crossing is one of five Registers, its operator is `RISK`, its substantive MSID is `Away.Crossing`, and Highway is its world manifestation.
- Recorded Crossing's unique Core-Species fork and child branches such as `Away.Crossing.Phase`, `Away.Crossing.Rabbit`, and `Away.Crossing.Squirrel`.
- Closed `OPEN-HOME-001`: Community Board is the Leadership-associated Practice providing diegetic access to Almanac material, parallel to Gathering Place and Chronicle.
- Closed `OPEN-SEM-001` by formalizing `Embodiment : EMBODY`.
- Added the Minimum Two-Segment and TLD self-root rulings.
- Established the MSID/entity boundary.
- Adopted **MEDIAN Semantic Identifier (MSID)** as the canonical project term and abbreviation.
- Left the Narrative TLD and exact Entity ID grammar visibly open.

### v0.1 — 2026-08-01

- Promoted the preparation schema into an active Human Rulings Ledger.
- Recorded explicit lineage, philosophy, file-naming, Crossing, Home, language, recognition, Outpost, authority, MSID, and Sourcebook rulings from the current thread.
- Preserved exact human wording separately from normalized operational rulings.
- Initially left Community Board and the noun paired with `EMBODY` open; both were closed in v0.2.
- Deferred BSA-01 through BSA-22 ingestion until exact human decision carriers can be recovered.
