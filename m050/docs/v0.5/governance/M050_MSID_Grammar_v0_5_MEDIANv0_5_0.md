---
title: "MEDIAN v0.5.0 MSID Grammar"
document_id: M050-SEMANTIC-ID-GRAMMAR-001
document_version: 0.5
game_target: MEDIAN v0.5.0
document_kind: ontology_and_extraction_grammar
authority: active_for_msid_construction_and_adjudication
state: ACTIVE_WORKING_GRAMMAR
publication_default: internal
created: 2026-08-01
revised: 2026-08-01
supersedes: M050_MSID_Grammar_v0_4_MEDIANv0_5_0.md
human_rulings_owner: M050_Human_Rulings_Ledger_v0_4_MEDIANv0_5_0.md
---

# MEDIAN v0.5.0
## MEDIAN Semantic Identifier (MSID) Grammar

**File:** `M050_MSID_Grammar_v0_5_MEDIANv0_5_0.md`

> **An MSID—MEDIAN Semantic Identifier—is the stable ontological address of a property of MEDIAN.**

MSID construction and authored prose are governed by paired documents:

| Document | Scope |
|---|---|
| **MSID Grammar** | Ontological paths, classes, aliases, extraction, and registry state. |
| **Authorial Grammar** | Capitalization, operator typography, species agreement, Hyphen-bound prose, and other semantic text treatments. |

See `M050_Authorial_Grammar_Orthography_and_Prose_Style_Guide_v0_1_MEDIANv0_5_0.md`.


An MSID tells a reader, designer, compiler, or implementation record what kind of game property is under discussion, where it belongs, and what larger system gives it meaning. It is not merely a database key. It is explanatory notation made possible by MEDIAN's rigid hierarchy.


**Canonical abbreviation:** `MSID`. The earlier phrase *Semantic ID* remains a searchable legacy alias, but `SID` is not used as MEDIAN's abbreviation. New schema fields use `msid`, `msid_candidate`, and `msid_status`.

---

## 1. What an MSID belongs to

An MSID belongs to a **game property**, not to:

- the specification that first describes it;
- the Sourcebook section that presents it;
- the appendix entry that explains it in depth;
- the interface that exposes it;
- the manifestation that translates it;
- or the implementation record that realizes it.

Documents declare that they **define, constrain, elaborate, tune, present, revise, supersede, or reference** semantic units. They do not create the unit's identity.

```yaml
msid: Home.Colony.Practice.Garden
canonical_name: Garden
```

A Sourcebook section may display that ID. A Phonebook entry may use it as its direct heading. Both are presentations of the same game property.

---

## 2. Top-level domains are not MSIDs

The first segment of a path is a **Top-Level Domain** or **TLD**. A TLD is a namespace container. It is not, by itself, an MSID.

```text
Home          # namespace only
Away          # namespace only
Architecture  # namespace only
Philosophy    # namespace only
```

A valid MSID contains **at least two segments**.

Incorrect:

```text
Home
Away
Architecture
Philosophy
```

Correct:

```text
Home.Home
Away.Away
Architecture.Mode.Home
Philosophy.Pillar.ConservationOfSystems
```

### 2.1 TLD self-root rule

When the broad concept named by a TLD requires its own MSID, the TLD name is repeated as the second segment:

```text
Home.Home
Away.Away
Architecture.Architecture
Philosophy.Philosophy
```

The first segment identifies the namespace. The second identifies the broad game property within that namespace.

`Home` is therefore not necessarily an MSID. `Home.Home` explicitly is.

### 2.2 The self-root convention stops below the TLD

Below the top level, a branch may simultaneously:

1. identify a Semantic Unit; and
2. serve as the parent of more specific Semantic Units.

The terminal segment is not repeated merely to prove that the branch is a unit.

Correct:

```text
Home.Colony
Home.Colony.Place
Home.Colony.Practice
Home.Colony.Practice.Garden
Home.Colony.Role
Home.Colony.Role.Gardener
Home.Embodiment
```

Incorrect duplication:

```text
Home.Colony.Colony
Home.Colony.Place.Place
Home.Colony.Practice.Practice
Home.Colony.Role.Role
```

A repeated segment below the TLD would be valid only if it identified a genuinely distinct same-named property. It is never added for visual standardization alone.

> **No one-segment MSIDs. Self-root only at the TLD. No empty duplication below it.**

---

## 3. Basic form

MSIDs use dot-delimited UpperCamelCase segments:

```text
<Domain>.<System-or-Subject>.<Class>.<Unit>
```

This is a descriptive pattern, not a mandatory four-segment template. Depth is variable.

Accepted current examples:

```text
Philosophy.Pillar.ConservationOfSystems
Architecture.Mode.Home
Architecture.Register.Colony
Architecture.Register.Field
Architecture.Register.Crossing
Architecture.Register.Encounter
Architecture.Register.Embodiment
Architecture.Scale.BodyUnit
Architecture.Scale.ExpeditionParty
Home.Home
Home.Colony
Home.Colony.Practice.Garden
Home.Colony.Role.Gardener
Home.Colony.Practice.GatheringPlace
Home.Colony.Role.Teacher
Home.Embodiment
Away.Away
Away.Crossing.Phase.Planning
Away.Encounter.Stopover
Home.Encounter.Homecoming
```

Every segment must add meaningful context.

---

## 4. The explanatory-segment rule

Every segment must answer a useful contextual question.

For example:

```text
Home.Colony.Role.Gardener
```

means:

| Segment | Context supplied |
| --- | --- |
| `Home` | The property belongs intrinsically to the Home domain. |
| `Colony` | The property belongs to the Colony branch of Home. |
| `Role` | The property is a civic Role, not a Practice, Place, Project, View, or personal trait. |
| `Gardener` | This is the particular Role being defined. |

A segment that adds no understanding should not exist. If a proposed property cannot receive a clear address, it may be:

- under-defined;
- duplicated;
- assigned to the wrong owner;
- a presentation rather than a semantic unit;
- or not genuinely distinct.

The hierarchy is justified by explanatory value, not by visual neatness.

---

## 5. Noun grammar

MSIDs use **canonical nouns or noun phrases**.

The Authorial Grammar owns the prose display form of those nouns: Initial Caps, spaces, Hyphen-bound compounds, Core-Species agreement, and defined typography. This grammar owns their machine-safe semantic path.

All-caps operators do not become path segments merely because the player acts through them.

Correct:

```text
Architecture.Register.Colony
Architecture.Register.Embodiment
Home.Colony.Practice.Garden
Away.Crossing.Phase.Planning
```

Incorrect:

```text
Architecture.Register.DWELL
Architecture.Register.EMBODY
Away.RISK.Crossing
Home.DWELL.Practice.Garden
```

A word shaped like a verb may appear when it is the proper name of a defined semantic object:

```text
Away.Crossing.Phase.Planning
```

`Planning` names a Phase. It does not establish a universal `PLAN` operator or put every momentary planning action into the ontology.

---

## 6. Registers, substantive branches, and operators are distinct

MEDIAN has five Registers. Each Register has:

1. a noun-form architectural reference under `Architecture.Register.*`;
2. a substantive MSID in the Home or Away ontology; and
3. an all-caps operator through which the player acts.

The architecture entry states the Register's place in the five-Register topology and refers to its substantive branch. It does not become a competing mechanical owner.

| Register | Architectural reference | Substantive MSID | Operator | Mode |
| --- | --- | --- | --- | --- |
| Colony | `Architecture.Register.Colony` | `Home.Colony` | `DWELL` | Home |
| Field | `Architecture.Register.Field` | `Away.Field` | `TRAVEL` | Away |
| Crossing | `Architecture.Register.Crossing` | `Away.Crossing` | `RISK` | Away |
| Encounter | `Architecture.Register.Encounter` | `Home.Encounter` and `Away.Encounter` | `MEET` | Cross-modal |
| Embodiment | `Architecture.Register.Embodiment` | `Home.Embodiment` | `EMBODY` | Home |

`Colony : DWELL`, `Field : TRAVEL`, `Crossing : RISK`, `Encounter : MEET`, and `Embodiment : EMBODY` are settled.

```yaml
msid: Architecture.Register.Crossing
canonical_name: Crossing
substantive_domain: Away.Crossing
operator: RISK
```

```yaml
msid: Away.Crossing
canonical_name: Crossing
architecture_reference: Architecture.Register.Crossing
operator: RISK
world_manifestation: World.Highway
```

An operator never replaces the Register noun in an MSID:

```text
Away.Crossing
Away.Crossing.Phase.Planning
```

not:

```text
Architecture.Register.Risk
Away.RISK.Crossing
```

### 6.1 Crossing is uniquely forked by Core Species

Crossing is a Register, not a generic system operating through a separate Risk Register. Its substantive branch is also a parent for its internal ontology:

```text
Away.Crossing
Away.Crossing.Phase
Away.Crossing.Mouse
Away.Crossing.Rabbit
Away.Crossing.Squirrel
```

The Core-Species branches are not decorative species tags. They exist because Crossing's planning, affordance, movement, and failure grammar forks by Core Species in a way no other Register does.

The Crossing extraction pilot recommends these owner-language phase candidates:

```text
Away.Crossing.Phase.Planning
Away.Crossing.Phase.Commitment
Away.Crossing.Phase.ContinuousRun
Away.Crossing.Phase.Resolution
```

The branch roots are canonical. The exact phase descendants remain provisional until the canonical registry is frozen.

`Away.Crossing.Phase.Observe` is rejected as a phase name. **Observe** is an action inside Planning; the dedicated owner names the phase **Planning**. A future non-Phase Observe unit would require separate evidence that it is independently persistent and addressable.

The human-confirmed species branches must not be flattened into generic `Away.Crossing.Species.*` paths without adjudication.

### 6.2 One Register may have more than one modal branch

Encounter is cross-modal. The architecture entry can therefore refer to both:

```text
Home.Encounter
Away.Encounter
```

A specific Encounter retains the Mode in which it intrinsically exists:

```text
Home.Encounter.Homecoming
Away.Encounter.Stopover
```

Presentation borrowing does not change that identity.
---

## 7. Architectural scales: Body Unit and expedition party

Architecture contains stable scales as well as Modes, Registers, cycles, and topology.

### 7.1 Body Unit

```text
Architecture.Scale.BodyUnit
```

A **Body Unit** is MEDIAN's cross-species equivalency scale. It answers how much general physical and logistical party commitment is present without claiming that bodies, species traits, or Citizens are identical.

```text
1 Rabbit  = 1 Body Unit
1 Squirrel = 1 Body Unit
2 Mice    = 1 Body Unit
```

For body-unit-based systems, one Mouse pair is generally equivalent in scale to one Rabbit or one Squirrel while containing two named Citizens.

Body Unit may govern or normalize:

- ordinary expedition-party scale;
- collective action bandwidth;
- body-unit-based Supply or similar allowances;
- body-unit-based adversity incidence before consequence attaches to actual Citizens;
- other quantities whose owner explicitly declares Body Unit as the counting scale.

Body Unit does **not** imply universal numerical identity. Carry, movement, route use, risk expression, personal items, and other species traits may differ under their dedicated owners.

Two Mice in one Body Unit remain two runtime Citizens. They do not share one Entity ID, one wound, one relationship, one memory, or one personhood. Additional Mouse Citizens do not automatically create extra collective actions, MEET Turns, Crossing activations, Supplies, or duplicated Cargo.

> **Body Unit is an accounting equivalency, not a personhood class.**

### 7.2 Expedition party scale

```text
Architecture.Scale.ExpeditionParty
```

An ordinary expedition has a standard and maximum of **three Body Units**.

A **two-Body-Unit party** is an allowable exception, intended primarily for early play when Colony population is too low to field the full standard party.

```yaml
msid: Architecture.Scale.ExpeditionParty
standard_body_units: 3
ordinary_maximum_body_units: 3
allowable_exception:
  body_units: 2
  primary_context: early_game_low_population
```

“Two to three Body Units” is therefore a valid range only when the asymmetry is preserved: three is the standard and ordinary maximum; two is the exception.

Parties larger than three Body Units require a specific authored exception and do not create permanent ordinary cap progression.

---

## 8. Philosophy and Architecture are distinct TLDs

`Philosophy.*` contains MEDIAN's constitutional commitments: Thesis, Pillars, cross-system Principles, and Protections.

`Architecture.*` contains structural facts: Modes, Registers, scales, cycles, and topology.

```text
Philosophy.Philosophy
Philosophy.Pillar.ConservationOfSystems
Philosophy.Pillar.ConsequenceWithoutDisposability
Philosophy.Pillar.GameLogicPrecedesAttachment
Philosophy.Protection.NoOffscreenPersonalLoss
```

```text
Architecture.Architecture
Architecture.Mode.Home
Architecture.Mode.Away
Architecture.Register.Colony
Architecture.Register.Embodiment
Architecture.Scale.BodyUnit
Architecture.Scale.ExpeditionParty
Architecture.Cycle.HomeAwayReturn
```

Philosophy constrains Architecture. Architecture organizes concrete systems. Concrete systems contain Roles, Practices, Phases, Processes, Conditions, Views, Encounters, and other game properties.

A broad proposition belongs under `Philosophy` only when it can judge or constrain multiple systems. Local doctrines remain with their owning system.

---

## 9. Home and Away exist both architecturally and substantively

`Home` and `Away` are top-level semantic domains. Their architectural status as Modes is separately defined under `Architecture.Mode.*`.

These are related but not duplicate entries:

```text
Architecture.Mode.Home
Home.Home
```

```text
Architecture.Mode.Away
Away.Away
```

### 9.1 Architectural Mode entries

`Architecture.Mode.Home` defines the structural fact that Home is one of MEDIAN's two Modes. Its entry should remain concise and refer to `Home.Home` for the substantive Home domain.

```yaml
msid: Architecture.Mode.Home
canonical_name: Home
substantive_domain: Home.Home
counterpart: Architecture.Mode.Away
```

`Architecture.Mode.Away` does the same for Away.

```yaml
msid: Architecture.Mode.Away
canonical_name: Away
substantive_domain: Away.Away
counterpart: Architecture.Mode.Home
```

### 9.2 Home domain roots

```text
Home.Home
Home.Colony
Home.Embodiment
```

- `Home.Home` defines Home at large: permanent sanctuary, civic continuity, the Home Median, and the broad condition of life and responsibility situated there.
- `Home.Colony` is the substantive MSID of the Colony Register and the parent branch for Colony/DWELL ontology.
- `Home.Embodiment` is the substantive MSID of the Embodiment Register and the parent branch for EMBODY ontology.

```yaml
msid: Home.Colony
architectural_register: Architecture.Register.Colony
operator: DWELL
```

```yaml
msid: Home.Embodiment
architectural_register: Architecture.Register.Embodiment
operator: EMBODY
```

`Home.Colony` is both a valid Semantic Unit and the parent of more specific Colony units. It does not require `Home.Colony.Colony`.

### 9.3 Away Register roots

```text
Away.Away
Away.Field
Away.Crossing
Away.Encounter
```

- `Away.Away` defines Away at large.
- `Away.Field` is the substantive branch of the Field Register.
- `Away.Crossing` is the substantive branch of the Crossing Register and is uniquely forked by Core Species.
- `Away.Encounter` is the Away branch of the cross-modal Encounter Register.

The architecture entries under `Architecture.Register.*` summarize these structural relationships and refer into the substantive branches.

### 9.4 Presentation borrowing does not change domain

Mode and domain identity remain intrinsic. A Stopover remains Away even when it uses a Muted DWELL presentation.

```text
Away.Encounter.Stopover
```

Its borrowed presentation does not turn it into `Home.*` or into the Colony Register.

---

## 10. Top-level domain status

The following TLDs are currently settled by explicit ruling or direct architectural necessity:

```text
Philosophy
Architecture
Home
Away
```

The following remain working candidates to be tested during corpus extraction and the Active Corpus and Authority pass:

```text
World
Citizen
Time
Narrative
```

### 10.1 Narrative TLD proposal

`Narrative` is the current proposed TLD for game properties that turn events and lives into persistent account, memory, recognition, and narrated expression.

If confirmed, its root and likely first-order branches would be:

```text
Narrative.Narrative
Narrative.Memory
Narrative.Record
Narrative.Recognition
Narrative.Expression
```

This branch would potentially subsume the provisional `Memory.*` TLD rather than placing narrative beneath `Architecture`.

The rationale is functional: Chronicle, Tale, Campaign Memory, Distinction, After-name, and related structures do not merely describe architecture. They receive, preserve, select, transform, and present game history.

`Narrative` would not contain example story colonies merely because they are narrated. Worked colonies are authored examples or content objects, not automatically semantic architecture.

Until human confirmation and corpus adjudication, `Narrative.*` remains **provisional** and `Memory.*` must not be frozen as a competing TLD.

---

## 11. Semantic class rule

A class segment states what kind of property the unit is.

Current examples include:

```text
Role
Practice
Place
Project
Phase
Process
Encounter
View
Condition
Pillar
Principle
Protection
Mode
Register
Cycle
Record
Recognition
Expression
```

Classes are not accepted merely because an older document used the word. Their definitions must be established through current architecture and owner specifications.

Example:

```text
Home.Colony.Practice.GatheringPlace
Home.Colony.Role.Teacher
```

Gathering Place is a Practice. Teacher is the Role that staffs it. The Chronicle View pane is another semantic unit and must receive its own adjudicated path rather than being collapsed into either one.

A branch may itself be a semantic class root and a Semantic Unit:

```text
Home.Colony.Role
Home.Colony.Practice
Away.Crossing.Phase
```

Its child units then extend the path without repeating the class name.

---

## 12. Historical terminology adjudication

Development sources used terms such as Register, Mode, View, Encounter, Phase, system, action, verb, Place, Practice, and Project inconsistently. Their labels are evidence of intent, not authoritative ontology.

The extraction doctrine is:

> **Extract literally; classify judgmentally; preserve the difference.**

Every atom that contains a potentially unstable class label should preserve both layers:

```yaml
source_phrase: "Crossing Register"
source_declared_class: Register

adjudicated_class: Register
msid_candidate: Away.Crossing
architecture_reference: Architecture.Register.Crossing
operator: RISK
world_manifestation: World.Highway

adjudication_basis:
  - explicit Human Rulings Ledger correction
  - current Crossing architecture
  - governing philosophy and architecture

confidence: settled
```

The judgment layer uses the following precedence:

1. explicit Human Rulings Ledger entry;
2. current dedicated owner specification within its scope;
3. current Governing Philosophy and Architecture;
4. the behavior, persistence, relationships, and ownership actually described;
5. repeated cross-document usage;
6. the source's own class label.

The source label is deliberately weakest.

---

## 13. Functional classification questions

The adjudicator asks:

1. What persists in game state?
2. What larger system owns this property?
3. What kind of thing is it?
4. Is it a world property, system property, content object, presentation, or relationship of player attention?
5. Does it exist independently of its current interface?
6. Does a later dedicated specification reclassify it?
7. Has the designer explicitly corrected its class, path, name, or owner?
8. Can the statement be split into atoms with one primary semantic subject each?
9. Is the proposed first segment a TLD container rather than a complete ID?
10. Has a repeated segment below the TLD added real meaning, or merely visual symmetry?

Uncertainty remains visible:

```yaml
source_phrase: "Homecoming View"
msid_candidates:
  - Home.Encounter.Homecoming
  - Home.Colony.View.Homecoming
status: review_required
reason: source mixes authored-situation and interface terminology
```

The parser does not choose the tidiest path merely to complete the field.

---

## 14. Canonical names, display names, and aliases

Current structural aliases and rejected paths include:

| Historical or rejected form | Current disposition |
| --- | --- |
| `Architecture.Register.Travel` | Historical alias resolving to `Architecture.Register.Field`. |
| `Away.Travel` | Historical alias resolving to `Away.Field`. |
| `RISK Register` | Prose alias for Crossing Register; `RISK` remains the operator. |
| `Architecture.Register.Risk` | Rejected path. |
| `Away.RISK.Crossing` | Rejected path. |
| `Away.Crossing.Phase.Observe` | Rejected as a Phase name; observation belongs inside `Away.Crossing.Phase.Planning`. |


An MSID uses the canonical semantic name of the unit, converted to UpperCamelCase.

Display titles may differ for readability:

```yaml
msid: Home.Colony.Role.Gardener
canonical_name: Gardener
display_heading: GARDENERS
```

Number is part of the canonical concept name, not a database normalization rule. Singular-versus-plural forms must be decided by the owning semantic unit.

Deprecated and variant names point to one canonical ID:

```yaml
msid: Home.Colony.Practice.GatheringPlace
canonical_name: Gathering Place
deprecated_aliases:
  - Story Circle
```

Aliases never become competing IDs.

---

## 15. Hyphen-bound orthography and machine-safe mapping

Canonical Hyphen-bound prose is owned by the Authorial Grammar.

The governing display rule is:

> A Hyphen-bound animal-language word receives one initial capital at the beginning of the translated word; internal English elements remain lowercase.

```text
After-name
Prior-life Tale
```

`Prior-life Tale` is correct. `Prior-Life Tale` is not. `Tale` remains separately capitalized because it is its own Defined Term.

MSID segments remove punctuation and spaces while preserving the canonical display form in metadata:

```yaml
canonical_name: Prior-life Tale
semantic_segment: PriorLifeTale
search_aliases:
  - Prior Life Tale
  - Prior-Life Tale
  - prior-life tale
```

```yaml
canonical_name: After-name
semantic_segment: AfterName
search_aliases:
  - After name
  - aftername
```

The machine-safe segment does not replace canonical prose orthography.

The MSID Grammar does not decide which future compounds deserve Hyphen-bound status. That is an Authorial-Grammar and human-ruling question.

---

## 16. Documents receive semantic coverage, not one MSID

A document and a semantic unit are different kinds of things.

A broad specification receives a semantic coverage declaration:

```yaml
document_id: SPEC_HOME
defines:
  - Home.Home
  - Home.Colony.*
  - Home.Embodiment.*
references:
  - Architecture.Mode.Home
  - Architecture.Register.Colony
  - Architecture.Register.Embodiment
  - Home.Encounter.*
```

A focused specification may be narrower:

```yaml
document_id: SPEC_CROSSING
defines:
  - Away.Crossing.*
references:
  - Architecture.Mode.Away
  - Architecture.Register.Crossing
  - Away.Away
  - World.Highway.*
  - Citizen.Condition.*
  - Away.Encounter.Stopover
  - Home.Encounter.Homecoming
```

Wildcards describe document coverage. They are not automatically canonical Semantic Units.

A document may relate to a unit through:

```text
defines
constrains
elaborates
tunes
presents
references
revises
supersedes
provides_rationale
```

---

## 17. Atomic extraction lifecycle

MSIDs enter during atomic extraction as provisional classifications.

```yaml
atom_id: ATOM-CROSS-0042
source_id: SPEC_CROSSING
source_location: section 3.1
source_text: "The party studies the current road before commitment."

msid_candidate: Away.Crossing.Phase.Planning
semantic_relation: defines
msid_status: provisional
```

The lifecycle is:

```text
source text
    -> literal atom
    -> candidate MSID
    -> cross-source clustering
    -> authority and contradiction adjudication
    -> canonical MSID
    -> back-propagation into cleaned M050 specifications
    -> Sourcebook and Phonebook presentation
```

The raw historical source remains immutable. Only the adjudicated extraction record and later cleaned specification receive canonical IDs.

TLD self-roots and branch roots are available during extraction as candidate subjects:

```text
Home.Home
Home.Colony
Home.Embodiment
Away.Away
Away.Crossing
```

No atom may be assigned a one-segment candidate such as `Home` or `Away`.

---

## 18. One primary unit per atom

An atom should normally have one primary MSID candidate and zero or more related MSIDs.

```yaml
claim: "The Teacher staffs the Gathering Place."
primary_msid_candidate: Home.Colony.Role.Teacher
related_msids:
  - Home.Colony.Practice.GatheringPlace
relation_type: staffs
```

If a claim cannot be assigned one intelligible primary unit, it may still contain multiple rules and should be split.

A relationship may receive its own semantic unit only when that relationship is independently persistent, addressable, and worth defining—not merely because two units appear in one sentence.

---

## 19. MSIDs do not identify runtime instances

An MSID identifies a stable type, property, system, class, or authored semantic object. It does not absorb the unique identifier of a particular runtime Citizen, Colony, Place, Artifact, Route, or other instantiated entity.

Do not construct:

```text
Home.Colony.Role.Gardener.Bramble#R002
```

That path conflates:

- the semantic definition of the Gardener Role;
- the identity of Bramble;
- and Bramble's current relationship to that Role.

Keep them separate:

```yaml
msid: Home.Colony.Role.Gardener
entity_id: Citizen#R002
display_name: Bramble
relation:
  type: holds_role
  target: Home.Colony.Role.Gardener
```

Readable diagnostic shorthand may combine them without creating a new MSID:

```text
Citizen#R002 -> Home.Colony.Role.Gardener
```

The exact `Entity ID` syntax and registry belong to a later Entity ID Grammar. This specification establishes only the boundary: **instance identity is relational metadata, not a terminal MSID segment.**

---

## 20. Provisional and canonical states

During extraction:

```yaml
msid_candidate: Away.Crossing.Phase.Planning
msid_status: provisional
```

After adjudication:

```yaml
msid: Away.Crossing.Phase.Planning
msid_status: canonical
```

Permitted status values:

```text
provisional
canonical
review_required
deprecated
alias
rejected
```

A candidate may be remapped without altering the source atom. The remap records improved understanding of the game, not a rewrite of history.

---

## 21. Sourcebook and Phonebook use

Part I may present:

```text
GARDENERS
Home.Colony.Role.Gardener
```

Part II may use the ID as the direct heading:

```text
Home.Colony.Role.Gardener
```

The broadest entries may likewise expose the namespace root explicitly:

```text
HOME
Home.Home
```

```text
COLONY
Home.Colony
```

Part I explains the lived and core systemic meaning. Part II may provide complete mechanical detail, tuned values, edge cases, authoring requirements, UI obligations, and related MSIDs.

Both presentations point to one semantic unit. Part I may compress. Part II may specify. Neither may contradict or create a second canon.

The Authorial Grammar supplies a separate one-page Phonebook plate summarizing Initial Caps, operators, MSID display, Hyphen-bound compounds, and the Bare Core-Species Singular. The plate is a derived reader aid and creates no new ontology.

The MSID supplies a persistent “you are here” marker in the game architecture.

---

## 22. Stability and change

An MSID does not change because:

- a specification is renamed;
- a Sourcebook section moves;
- page numbers change;
- the table of contents changes;
- a new manifestation translates the interface;
- or an implementation file is reorganized.

An ID changes only when the ontology itself was wrong: wrong owner, wrong class, wrong domain, conflated units, empty duplication, or a genuine canonical rename.

Every change must preserve the mapping:

```yaml
old_msid: Away.Encounter.Crossing.Observe
new_msid: Away.Crossing.Phase.Planning
change_class: ontology_correction
reason: Crossing is the Away Register branch and Observe is one of its phases
```

The v0.2 root correction should likewise be represented as ontology cleanup where old provisional IDs used empty duplication:

```yaml
old_msid: Home.Colony.Colony
new_msid: Home.Colony
change_class: empty_duplication_removed
reason: Home.Colony is already both a semantic unit and a parent branch
```

---

## 23. Acceptance tests

A candidate MSID passes only when:

1. **Game property:** The unit exists as a property of MEDIAN independent of a document or page.
2. **Minimum depth:** The ID contains at least two segments.
3. **TLD distinction:** The first segment is a namespace root, not a complete one-word ID.
4. **Self-root discipline:** Repetition is used only to identify the broad TLD concept itself, such as `Home.Home`.
5. **No empty duplication:** Repeated segments below the TLD add real meaning or are removed.
6. **Context:** The path tells the reader how to contextualize the unit.
7. **Meaningful hierarchy:** Every segment adds useful classification.
8. **Noun grammar:** The path uses canonical nouns or noun phrases.
9. **Operator separation:** Player operators and Registers are not collapsed into ordinary system paths.
10. **Current ontology:** Historical source labels have been adjudicated rather than trusted automatically.
11. **Single identity:** Aliases and deprecated names resolve to one unit.
12. **Stable owner:** One current source or explicit human ruling owns the positive definition.
13. **Atomic fit:** Extracted claims can identify one primary semantic subject.
14. **Entity boundary:** Runtime instance identifiers are not appended as MSID terminals.
15. **Publication independence:** Reordering the Sourcebook would not invalidate the ID.
16. **Prose boundary:** Canonical display orthography is delegated to the Authorial Grammar rather than encoded ad hoc in MSID paths.
17. **Hyphen mapping:** `Prior-life Tale` maps to `PriorLifeTale` without changing canonical prose casing.

---

## 24. Open grammar decisions

The following remain intentionally open for human adjudication or registry extraction:

1. Final confirmation of `Narrative` as a TLD and the resulting disposition of the provisional `Memory.*` branch.
2. The complete frozen TLD list beyond `Philosophy`, `Architecture`, `Home`, and `Away`.
3. The canonical MSIDs for Almanac, Chronicle, Leadership, and their View panes.
4. Singular-versus-plural final naming for civic Role units where reader-facing headings are collective.
5. The exact syntax and scope of the future Entity ID Grammar.
6. The complete child structure below each Core-Species fork under `Away.Crossing`.
7. The final broader ontology for Core-Species Away traits, including whether `Away.CoreSpecies.*` is the accepted branch.

The following questions are now closed:

- Crossing is one of the five Registers.
- `Away.Crossing` is its substantive MSID.
- `Architecture.Register.Crossing` is its architectural reference.
- `RISK` is Crossing's operator.
- Highway is Crossing's world manifestation.
- Crossing is uniquely forked by Core Species.
- Community Board is the Leadership-associated Practice that provides diegetic Almanac access.
- Gathering Place provides diegetic Chronicle access.
- `Field` is the noun-form Register paired with `TRAVEL`.
- `Architecture.Register.Travel` and `Away.Travel` are historical aliases, not current MSIDs.
- `Embodiment` is the noun-form Register paired with `EMBODY`.
- TLDs are namespace containers rather than one-word MSIDs.
- Every MSID contains at least two segments.
- TLD self-root repetition does not continue below the TLD.
- `Home.Colony` is both an MSID and a parent branch; `Home.Colony.Colony` is not used.
- `Home` and `Away` have both architectural Mode entries and substantive TLD-root entries.
- Runtime instances use separate Entity IDs rather than terminal MSID segments.
- The project abbreviation is `MSID`, not `SID`.
- Body Unit is `Architecture.Scale.BodyUnit`.
- Ordinary expedition scale is `Architecture.Scale.ExpeditionParty`: three Body Units standard and maximum, with a two-unit early-game exception.

These remaining open items do not block atomic extraction. They require provisional MSIDs and visible review status rather than invented certainty.
---

## Change record

### v0.5 — 2026-08-01

- Paired the MSID Grammar with the standalone Authorial Grammar.
- Delegated Initial Caps, operator typography, Core-Species agreement, and defined text treatments to the prose owner.
- Narrowed the MSID Grammar's role in Hyphen-bound orthography to machine-safe mapping.
- Settled `Prior-life Tale` as the canonical prose form and `PriorLifeTale` as the MSID segment.
- Added the derived Phonebook grammar plate relationship.
- Added prose-boundary and Hyphen-mapping acceptance tests.

### v0.4 — 2026-08-01

- Corrected the Field Register throughout: `Architecture.Register.Field`, `Away.Field`, operator `TRAVEL`.
- Replaced the obsolete `Philosophy.Principle.LegibilityPrecedesAttachment` example with `Philosophy.Pillar.GameLogicPrecedesAttachment`.
- Conformed Crossing phases to the dedicated owner's language: Planning, Commitment, Continuous Run, and Resolution.
- Rejected `Away.Crossing.Phase.Observe` as a Phase name while preserving observation as an action inside Planning.
- Added `Architecture.Scale.BodyUnit` and its equal-personhood boundary.
- Added `Architecture.Scale.ExpeditionParty`: three Body Units standard and maximum, with an allowable two-unit early-game exception.
- Added historical aliases for Travel-era and RISK-as-Register terminology.
- Added the unresolved broader Core-Species Away-trait branch to open grammar decisions.

### v0.3 — 2026-08-01

- Adopted **MEDIAN Semantic Identifier (MSID)** as the canonical term and abbreviation; deprecated `SID`.
- Corrected Crossing's ontology: Crossing is one of five Registers, `Away.Crossing` is its substantive MSID, and `RISK` is its operator.
- Replaced the erroneous `Architecture.Register.Risk` model with `Architecture.Register.Crossing`.
- Defined architecture Register entries as concise structural references to substantive Home/Away branches.
- Added Crossing's unique Core-Species fork, including `Away.Crossing.Phase`, `Away.Crossing.Rabbit`, and `Away.Crossing.Squirrel`.
- Closed Community Board as the Leadership-associated Practice that provides diegetic access to Almanac material, mirroring Gathering Place and Chronicle.
- Confirmed `Embodiment : EMBODY`.
- Updated extraction fields from `semantic_id*` to `msid*`.
- Preserved Narrative TLD and Entity ID syntax as open questions.


### v0.2 — 2026-08-01

- Established the Minimum Two-Segment Rule: bare TLDs are namespace containers, not MSIDs.
- Added TLD self-roots such as `Home.Home` and limited self-root repetition to the TLD level.
- Removed empty duplication below the TLD; `Home.Colony` now serves as both Semantic Unit and parent branch.
- Formalized `Architecture.Register.Embodiment` paired with operator `EMBODY`.
- Distinguished `Architecture.Mode.Home` from `Home.Home`, and `Architecture.Mode.Away` from `Away.Away`.
- Defined `Home.Colony` and `Home.Embodiment` as substantive Home branches related to, but not identical with, their Registers.
- Added `Narrative` as a provisional TLD proposal and prevented premature freezing of a competing `Memory.*` TLD.
- Established that runtime instances use separate Entity IDs and relations rather than terminal MSID segments.
- Updated document coverage, extraction, acceptance tests, and open decisions to the revised grammar.

### v0.1 — 2026-08-01

- Established MSIDs as properties of MEDIAN rather than properties of documents or Sourcebook sections.
- Separated noun-form semantic Register names from all-caps operators.
- Initially classified Crossing as an Away system expressed through RISK; this was a v0.1 error superseded by v0.3, which restores Crossing as a Register.
- Distinguished `Philosophy.*` from `Architecture.*` and located Conservation of Systems under `Philosophy.Pillar`.
- Added historical-terminology adjudication for an undisciplined development corpus.
- Defined provisional-ID assignment during atomic extraction and canonicalization after adjudication.
- Established the dual-depth Sourcebook/Phonebook use of one semantic ontology.
