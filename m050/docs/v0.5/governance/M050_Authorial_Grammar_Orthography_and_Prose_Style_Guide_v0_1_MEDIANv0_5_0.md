---
title: "MEDIAN v0.5.0 Authorial Grammar, Orthography, and Prose Style Guide"
document_id: M050-AUTHORIAL-GRAMMAR-001
document_version: 0.1
game_target: MEDIAN v0.5.0
document_kind: authorial_grammar_orthography_and_prose_style_guide
authority: active_for_authorial_prose_and_semantic_typography
state: ACTIVE_WORKING_GUIDE
publication_default: internal
created: 2026-08-01
governing_sources:
  - M050_Human_Rulings_Ledger_v0_4_MEDIANv0_5_0.md
  - M050_MSID_Grammar_v0_5_MEDIANv0_5_0.md
  - M050_Governing_Philosophy_and_Architecture_v1_3_MEDIANv0_5_0.md
paired_with:
  - M050_MSID_Grammar_v0_5_MEDIANv0_5_0.md
derived_publication:
  - one-page Phonebook appendix plate
---

# MEDIAN v0.5.0
## Authorial Grammar, Orthography, and Prose Style Guide

**Filename:** `M050_Authorial_Grammar_Orthography_and_Prose_Style_Guide_v0_1_MEDIANv0_5_0.md`

> **MEDIAN's typography carries semantic information. Capitalization, all-caps operators, dots, hyphens, and defined text treatments are not decorative emphasis. Each marks a different relationship between language and the game world.**

---

# I. Status and Relationship to the MSID Grammar

This is a standalone companion to the **MEDIAN Semantic Identifier Grammar**.

The two documents govern adjacent but distinct layers:

| Owner | Governing question |
|---|---|
| **MSID Grammar** | What is the stable semantic address of this game property? |
| **Authorial Grammar** | How does that game property appear in authored prose? |

The Authorial Grammar governs:

- capitalization of Defined Terms;
- all-caps experiential operators;
- prose display of MSIDs;
- Core-Species grammatical usage;
- Hyphen-bound animal-language compounds;
- defined typographic treatments;
- development of future emergent authorial conventions.

The MSID Grammar continues to govern:

- namespace structure;
- valid MSID paths;
- segment construction;
- semantic classes;
- aliases and deprecated paths;
- extraction and registry states.

This guide is **not Book II of the MSID Grammar**. It may evolve through actual writing and layout without forcing an ontology revision whenever a prose convention changes.

The eventual Phonebook appendix receives a one-page derived plate. That plate summarizes this guide; it does not become an independent authority.

---

# II. Core Authorial Doctrine

MEDIAN distinguishes six principal written forms:

| Written form | Meaning | Example |
|---|---|---|
| **Initial Caps** | A Defined Term with stable MEDIAN meaning | Citizen, Place, Body Unit, Exposure |
| **ALL CAPS** | A canonical experiential operator | DWELL, TRAVEL, RISK, MEET, EMBODY |
| **ALL CAPS species operator** | A civilization's characteristic spatial action | JOIN, GATHER, CONNECT |
| **Dot-delimited UpperCamelCase** | A MEDIAN Semantic Identifier | `Away.Crossing.Phase.Planning` |
| **Hyphen-bound compound** | One translated animal-language word rendered through several English elements | After-name, Prior-life Tale |
| *Defined text treatment* | A stable authored-text function, once established | *mechanics-teaching Narrative snippet* |

A seventh grammatical convention governs Core-Species prose:

| Construction | Meaning | Example |
|---|---|---|
| **Bare Core-Species Singular** | One archetypal Core-Species body expresses the characteristic logic of the species | Mouse builds a Manor House. |

---

# III. Initial Caps: Defined Terms

## 1. Rule

A noun or noun phrase receives **Initial Caps** when MEDIAN gives it a stable, defined game meaning that differs from, narrows, or formalizes ordinary English usage.

Examples:

```text
Citizen
Colony
Place
Practice
Project
Role
Mode
Register
View
Body Unit
Exposure
Quiet Equilibrium
Chronicle
Almanac
Home
Away
```

The governing test is not:

> Is this noun important?

The governing test is:

> Could this term receive a definition, MSID, glossary entry, stable cross-document reference, or explicit owner?

If yes, Initial Caps may be warranted.

## 2. Initial Caps are not emphasis

Do not capitalize ordinary prose merely to make it feel weighty.

Prefer:

```text
The party crosses the road during heavy rain.
A familiar route may still become dangerous.
The Colony records the event in its Chronicle.
```

Not:

```text
The Party crosses the Road during Heavy Rain.
A Familiar Route may still become Dangerous.
```

## 3. Defined and ordinary senses may coexist

```text
A Place is a formal Colony category.
This is a quiet place beside the wall.
```

```text
Home is the permanent founding sanctuary.
The Citizen comes home before Night.
```

Where ambiguity is likely, rewrite rather than relying on capitalization alone.

## 4. Multiword Defined Terms

Capitalize the significant elements of a Defined Term:

```text
Body Unit
Quiet Equilibrium
Continuous Run
Community Board
Gathering Place
Prior-life Tale
```

Articles, conjunctions, and internal prepositions remain lowercase unless the canonical term begins with them.

---

# IV. Experiential Operators in ALL CAPS

## 1. Register operators

The five canonical experiential operators are:

```text
Colony       : DWELL
Field        : TRAVEL
Crossing     : RISK
Encounter    : MEET
Embodiment   : EMBODY
```

ALL CAPS identifies the operator through which the player acts. It does not replace the Register noun.

Correct:

```text
Crossing is the Register. The player acts through RISK.
Field carries the party through territory by means of TRAVEL.
```

Incorrect:

```text
RISK is the Register.
Away.RISK.Crossing
Architecture.Register.Risk
```

## 2. Core-Species spatial operators

```text
Mouse        : JOIN
Rabbit       : GATHER
Squirrel     : CONNECT
```

These are canonical spatial and civilizational operators, not general-purpose emphatic verbs.

Correct:

```text
Mouse uses JOIN to extend protected continuity.
A new Rabbit Court must GATHER around shared ground.
Squirrel uses CONNECT to bring a separated Place into the Web.
```

## 3. Ordinary verbs remain ordinary

Do not capitalize every player action.

```text
The player observes the road, chooses a line, commits, and begins the Continuous Run.
```

Not:

```text
The player OBSERVES, CHOOSES, COMMITS, and BEGINS.
```

ALL CAPS is reserved for the canonical operator inventory.

## 4. No all-caps emphasis

Specification prose should not use all caps merely to shout or intensify. Use structure, syntax, bold text, or a defined callout class instead.

---

# V. MSID Display

## 1. Form

A MEDIAN Semantic Identifier is a dot-delimited sequence of UpperCamelCase noun or noun-phrase segments.

```text
Architecture.Scale.BodyUnit
Home.Colony.Practice.GatheringPlace
Away.Crossing.Mouse
Away.Crossing.Phase.ContinuousRun
```

Use inline code styling for MSIDs in authored prose:

```markdown
`Away.Crossing.Phase.Planning`
```

## 2. MSIDs and prose terms are parallel forms

Display punctuation and spaces do not enter the machine-safe segment:

| Canonical prose form | MSID segment |
|---|---|
| Body Unit | `BodyUnit` |
| Quiet Equilibrium | `QuietEquilibrium` |
| Continuous Run | `ContinuousRun` |
| After-name | `AfterName` |
| Prior-life Tale | `PriorLifeTale` |

The prose term and MSID are not competing spellings. Each belongs to a different grammatical environment.

## 3. Do not write prose as a path

Prefer:

```text
The Gathering Place provides access to the Chronicle.
Its MSID is `Home.Colony.Practice.GatheringPlace`.
```

Avoid:

```text
The Home.Colony.Practice.GatheringPlace provides access to Chronicle.
```

MSIDs may function as labels, references, headings, metadata, and diagnostic notation. They should not make ordinary sentences unreadable.

---

# VI. Core-Species Names

## 1. Canonical species forms

The three Core-Species names are Defined Terms:

```text
Mouse
Rabbit
Squirrel
```

Their ordinary plurals are:

```text
Mice
Rabbits
Squirrels
```

Never use **Wood Mouse** or **Wood Mice** in active canon except inside historical quotation or explicit zoological discussion.

## 2. MEDIAN species versus real animals

Initial Caps identify the MEDIAN Core Species or its designed civilization:

```text
Mouse reads safety through continuity.
Rabbit builds Courts.
Squirrel values reachable alternate routes.
```

Lowercase may be used for real-world zoological animals or noncanonical generic reference:

```text
Real-world mice often use covered runs.
The ecological source discusses cottontail rabbits.
```

Do not switch casually between the two.

---

# VII. The Bare Core-Species Singular

## 1. Rule

MEDIAN explicitly permits the **Bare Core-Species Singular**: the Initial-capped singular name of a Core Species may appear without an article when one representative body expresses the characteristic perception, action, spatial logic, or civilizational grammar of the species.

It takes **singular agreement**.

```text
Mouse builds a Manor House.
Rabbit gathers around a shared Court.
Squirrel connects a separated Place.
```

This is a marked house construction, related to the linguistic idea of a **bare generic singular**. It is intentionally available as poetic, naturalist, and doctrinal prose.

## 2. Meaning

```text
Mouse builds a Manor House.
```

means approximately:

```text
The Mouse Core Species, expressed through an archetypal Mouse body, builds Manor Houses in this way.
```

The sentence does not describe one particular runtime Citizen unless context identifies one.

## 3. Bare singular and plural generic are both valid

```text
Squirrel connects a separated Place.
Squirrels connect separated Places.
```

Both are grammatical in MEDIAN authorial prose, but the framing differs:

| Form | Framing |
|---|---|
| **Squirrel connects…** | Archetypal and doctrinal: one representative body expresses the species logic. |
| **Squirrels connect…** | Ordinary plural generalization about members of the species. |

Use the bare singular when bodily perception or species doctrine is foregrounded. Use the plural generic when describing populations, repeated behavior, or ordinary members of the species.

## 4. Individual Citizens remain article-bearing or contextually identified

```text
A Mouse carries one Tool and one Keepsake.
The Mouse at the road edge remains still.
This Mouse returned wounded.
Two Mice constitute one Body Unit.
Six Mice leave Home.
```

## 5. Agreement

The Bare Core-Species Singular always takes singular agreement:

```text
Mouse builds.
Rabbit gathers.
Squirrel connects.
```

Not:

```text
Mouse build.
Rabbit gather.
Squirrel connect.
```

Plural species nouns take plural agreement:

```text
Mice build.
Rabbits gather.
Squirrels connect.
```

## 6. Use with restraint

The construction is permitted, not mandatory. It is strongest in:

- constitutional species doctrine;
- ecological translation;
- architecture and movement descriptions;
- infographic captions;
- naturalist or proverbial Sourcebook voice;
- mechanics-teaching Narrative where the archetypal body matters.

Ordinary explanatory prose may prefer plurals when repeated bare singulars would feel mannered.

---

# VIII. Hyphen-bound Animal-Language Compounds

## 1. Translation premise

A **Hyphen-bound compound** represents one imagined animal-language word whose translated English form requires two or more elements.

The model is the distinctive translation orthography associated with *The Lord of the Rings*: the hyphen marks lexical unity in the source language rather than an ordinary English compound chosen only for convenience.

## 2. Capitalization rule

A Hyphen-bound word receives one initial capital at the beginning of the translated word. Its internal English element remains lowercase.

Correct:

```text
After-name
Prior-life
```

Incorrect:

```text
After-Name
Prior-Life
```

When the Hyphen-bound word modifies or forms part of a separately capitalized Defined Term, that other term keeps its own capitalization:

```text
Prior-life Tale
```

Here:

- `Prior-life` is one Hyphen-bound animal-language word;
- `Tale` is a separate Defined Term;
- therefore **life remains lowercase**.

## 3. MSID mapping

```text
After-name       -> AfterName
Prior-life Tale  -> PriorLifeTale
```

The hyphen remains mandatory in canonical prose. The MSID segment removes punctuation and spaces.

## 4. Controlled use

Not every in-world compound is automatically Hyphen-bound.

A term receives Hyphen-bound status only when the project intentionally treats it as:

- one animal-language lexical unit;
- a culturally meaningful translated compound;
- and a stable canonical form worth preserving.

The guide should maintain a controlled list as such terms emerge.

## 5. Search aliases

An implementation or index may retain common alternate searches:

```yaml
canonical_name: Prior-life Tale
semantic_segment: PriorLifeTale
search_aliases:
  - Prior Life Tale
  - Prior-Life Tale
  - prior-life tale
```

Aliases do not alter canonical orthography.

---

# IX. Defined Text Treatments

## 1. Typography must carry a stable function

Italics, bold text, small caps, inset prose, rule boxes, and other treatments should not acquire semantic meaning casually.

A treatment becomes authorial grammar only when it has:

- a stable function;
- repeated use;
- clear distinction from ordinary emphasis;
- value across multiple sections;
- and practical compatibility with writing, editing, layout, and automated checking.

## 2. Current provisional convention

```yaml
convention: mechanics_teaching_narrative
display_form: italics
status: PROVISIONAL
meaning: >
  A brief in-world Narrative passage that teaches, demonstrates, or reframes
  a mechanic without switching into direct specification voice.
```

Example:

> *Mouse does not cross empty ground. Mouse makes a road from every edge the body can still feel.*

The italics signal a mechanics-teaching Narrative function, not merely emphasis.

This convention remains provisional until repeated Sourcebook use proves that it is both legible and necessary.

## 3. Avoid competing uses

While a defined italic convention is active, do not also use italics indiscriminately for:

- casual emphasis;
- every in-world quotation;
- every Tale;
- every foreign or invented word;
- every caption.

Competing meanings weaken the grammar.

---

# X. Emergent Grammar

This guide is intentionally extensible.

Authorial conventions often become visible only when substantial Sourcebook prose, Narrative, captions, diagrams, and appendix plates exist. New conventions may therefore be recorded without pretending they were known at project inception.

## 1. Convention statuses

| Status | Meaning |
|---|---|
| `OBSERVED` | A recurring pattern has appeared but has not been intentionally adopted. |
| `PROVISIONAL` | The pattern is being used deliberately and tested for stability. |
| `SETTLED` | The pattern has a defined function and is the required house form. |
| `RETIRED` | The pattern was tested and removed from current authorial grammar. |

## 2. Promotion test

A convention may move from `OBSERVED` or `PROVISIONAL` to `SETTLED` only when:

1. its semantic function can be stated in one sentence;
2. it does not duplicate another established treatment;
3. authors can apply it consistently;
4. readers can distinguish it;
5. it survives conversion between Markdown, layout, and Phonebook presentation;
6. automated linting can identify at least its obvious violations;
7. an explicit human ruling adopts it.

## 3. Grammar log

Future revisions should maintain a compact convention ledger:

```yaml
canonical_name:
status:
written_form:
semantic_function:
first_observed:
adopted_by:
conflicts_with:
phonebook_expression:
```

---

# XI. Voice and Density

This guide governs orthography more strictly than literary voice. Nevertheless, several authorial tendencies follow from the grammar.

## 1. Plain activity before formal name

Prefer:

> The party studies the road and commits to one complete passage. This is Crossing, expressed through RISK.

rather than opening with a stack of unexplained Defined Terms and MSIDs.

## 2. Capitalization does not substitute for definition

A reader should not be expected to infer meaning merely because a word is capitalized.

## 3. Defined Terms should earn repetition

Once a term is introduced, use it consistently. Do not rotate among synonyms merely for stylistic variety when the distinction is mechanical.

## 4. Poetic license should remain legible

The Bare Core-Species Singular and Hyphen-bound compounds give MEDIAN a translated, naturalist, slightly mythic register. They should sharpen the world rather than make every sentence conspicuous.

---

# XII. Authoring Examples

## 1. Fully conformed prose

> Mouse builds a Manor House by extending protected continuity. Each new Place must JOIN the inhabited body without exposing the route between them. Two Mice constitute one Body Unit, but each remains a complete Citizen with an individual Tool, Keepsake, wound state, and Tale. The semantic address for the broader scale is `Architecture.Scale.BodyUnit`.

## 2. Crossing prose

> Squirrel connects a separated Place by reading the next reachable anchor. During Crossing, the player acts through RISK. The party enters `Away.Crossing.Phase.Planning`, commits once, and performs one Continuous Run.

## 3. Hyphen-bound prose

> A Citizen may receive an After-name only after meaningful history has made the recognition credible. A newcomer arrives with a Prior-life Tale rather than an empty biography.

## 4. Ordinary plural prose

> Squirrels connect separated Places through redundant routes. Mice build dense domestic interiors. Rabbits gather households around shared Courts.

## 5. Nonconforming version

> The MOUSE BUILD their MANOR-HOUSE by using Join. The Away.Crossing.Planning Phase lets the Player Risk the Highway.

## 6. Corrected version

> Mouse builds a Manor House through JOIN. During Crossing, the player uses RISK to commit the party's plan. The Planning phase is `Away.Crossing.Phase.Planning`.

---

# XIII. Authoring Checklist

Before accepting authored prose, check:

1. Are Defined Terms capitalized consistently?
2. Are ordinary nouns left lowercase?
3. Are only canonical experiential operators in ALL CAPS?
4. Is the Register noun kept distinct from its operator?
5. Are MSIDs dot-delimited UpperCamelCase and shown in code style?
6. Does the Bare Core-Species Singular take singular agreement?
7. Is a plural species noun used when the sentence concerns multiple animals or population behavior?
8. Does every Hyphen-bound form follow its canonical internal casing?
9. Is `Prior-life Tale` written with lowercase **life**?
10. Is typography carrying one defined function rather than casual emphasis?
11. Are provisional conventions marked as provisional in internal documents?
12. Can the sentence be understood without capitalization doing all the explanatory work?

---

# XIV. Machine-checkable Lint Rules

The authoring toolchain should eventually flag:

```text
Architecture.Register.Risk
Away.RISK.Crossing
Architecture.Register.Travel
Away.Travel
Prior-Life Tale
After-Name
Wood Mouse
Wood Mice
```

It should also flag probable agreement errors:

```text
Mouse build
Rabbit gather
Squirrel connect
```

when `Mouse`, `Rabbit`, or `Squirrel` is being used as the Bare Core-Species Singular.

Linting should warn rather than automatically rewrite where context could indicate:

- a direct quotation;
- a historical source;
- lowercase zoological usage;
- a particular named Citizen;
- a heading or visual treatment;
- or an intentional plural construction.

---

# XV. Phonebook Appendix Plate

The Phonebook receives a one-page condensation provisionally titled:

## HOW MEDIAN WRITES

| Meaning | Written form | Example |
|---|---|---|
| Defined game noun | Initial Caps | Citizen, Place, Body Unit |
| Experiential operator | ALL CAPS | DWELL, TRAVEL, RISK |
| Semantic address | Dot-delimited UpperCamelCase | `Away.Crossing.Mouse` |
| Animal-language word | Hyphen-bound | After-name, Prior-life Tale |
| Archetypal Core Species | Bare singular + singular agreement | Mouse builds a Manor House. |
| Stable text function | Defined typography | *mechanics-teaching Narrative* |

Footer doctrine:

> **Typography is part of MEDIAN's semantic system. It tells the reader whether a word is a game concept, an act of play, an ontological address, a translated animal word, or a particular kind of authored voice.**

The plate is generated from this guide and must not introduce independent conventions.

---

# XVI. Current Convention Ledger

| Convention | Status | Owner |
|---|---|---|
| Initial Caps for Defined Terms | `SETTLED` | Authorial Grammar |
| ALL CAPS for experiential operators | `SETTLED` | Authorial Grammar, constrained by P&A |
| Dot-delimited UpperCamelCase MSIDs | `SETTLED` | MSID Grammar |
| Bare Core-Species Singular | `SETTLED` | Authorial Grammar |
| Singular agreement for bare Core-Species names | `SETTLED` | Authorial Grammar |
| Hyphen-bound animal-language compounds | `SETTLED` | Authorial Grammar |
| `Prior-life Tale` exact casing | `SETTLED` | Authorial Grammar |
| Italics for mechanics-teaching Narrative | `PROVISIONAL` | Authorial Grammar |
| One-page Phonebook grammar plate | `SETTLED` as publication architecture | Authorial Grammar / Phonebook |

---

# Change Record

## v0.1 — 2026-08-01

- Established a standalone authorial-grammar owner paired with the MSID Grammar.
- Defined Initial Caps for MEDIAN Defined Terms.
- Reserved ALL CAPS for canonical experiential operators.
- Defined prose display of dot-delimited UpperCamelCase MSIDs.
- Adopted the Bare Core-Species Singular with singular agreement.
- Distinguished bare singular species doctrine from ordinary plural generic prose.
- Established Hyphen-bound animal-language compounds and exact `Prior-life Tale` casing.
- Added an extensible status system for emergent authorial conventions.
- Recorded italics for mechanics-teaching Narrative as provisional.
- Specified the derived one-page Phonebook appendix plate.
