# Record-to-Presentation Asset Pipeline

## Deterministic Baselines, Optional Model Realizations, and Memory

**Artifact class:** Developmental Source
**Version:** 0.1
**Date:** August 8, 2026
**Status:** Exploratory and non-authoritative
**Scope:** MEDIAN m051 and later Sourcebook development
**Related Source:**
`m051/prose/M051_Source_Landscape_Voice_Tolkien_Adams_and_Landscape_Orientation_v0_1.md`

This Source develops a conceptual in-game asset pipeline for MEDIAN. It
describes how the imagined game may turn authoritative play into narrative and
imagery while preserving deterministic operation when model services are
unavailable. It is intended for eventual Sourcebook treatment, not software
implementation. Terms such as `Moment Brief`, `renderer`, `pipeline`, and
`engine` describe game-design functions rather than required files, schemas,
services, prompts, or code.

This Source is not a finished Spec and does not amend the locked m050
architecture. Its companion atomic document is a derivative review form. This
prose document remains the canonical home of the idea until later authorial
review, reconciliation, and promotion.

---

# 1. One Pipeline, Two Channels, Two Realizations

## 1.1 Core proposition

MEDIAN appears to require two in-game asset channels:

- **Narrative**, which turns action and state into experienced language; and
- **Imagery**, which turns action and state into experienced pictures.

Each channel requires:

- a deterministic **Baseline** realization that is always available; and
- an optional **Model-assisted** realization that can enrich the result without
  becoming necessary for play.

These should not become four independent pipelines. They should share one
deterministic projection of the relevant Record facts and world state.

The conceptual architecture is:

```text
PLAYER ACTION
      |
      v
THE RECORD
authoritative facts
      |
      v
MOMENT BRIEF
derived presentation truth
      |
      +-----------------------+
      |                       |
      v                       v
NARRATIVE                  IMAGERY
      |                       |
      +-- Baseline             +-- Baseline
      |   deterministic        |   deterministic
      |                       |
      +-- Model-assisted       +-- Model-assisted
              \               /
               v             v
              EXPERIENCED MOMENT
                      |
                      v
               MEMORIES GATEWAY
                |      |      |
                v      v      v
             Memory   Tale  Chronicle
```

The Record gives the event integrity. A shared presentation projection gives
the outputs consistency. Narrative and imagery give the event experience. The
Memories architecture gives selected experience duration.

## 1.2 Conservation of Representation

The Record remains the sole factual authority. Narrative and image outputs do
not independently decide what happened.

The narrative passage and image should be parallel interpretations of the same
bounded moment rather than a serial chain in which prose invents details and
the image then treats those details as facts. A selected passage may help guide
the image's mood or emphasis, but the image must remain bound to the shared
presentation truth.

This prevents four common failures:

- prose and image depicting different participants or consequences;
- an image inheriting an attractive but unsupported literary embellishment;
- a later Memory contradicting the passage the player experienced; and
- model output becoming a second carrier of world state.

## 1.3 Deterministic baseline doctrine

The deterministic realization is not a degraded emergency mode. It is the
complete, reliable baseline expression of the system.

The imagined game should remain narratively and visually coherent when:

- no model service is enabled;
- a player declines external generation;
- a network is unavailable;
- generation exceeds its deadline;
- a generated result fails validation; or
- generation cost is not justified by the moment.

Model-assisted output may add variation, fluidity, composition, and literary or
illustrative richness. It may not hold essential information or gate continued
play.

---

# 2. The Moment Brief

## 2.1 Conceptual function

`Moment Brief` is a provisional name for the bounded presentation truth derived
from the Record and current world state. It is a conceptual handoff, not a
requirement for a particular technical artifact.

The Moment Brief answers:

- What actually happened or may still happen?
- Who is present?
- Where and when is the moment occurring?
- What can the participating animals perceive?
- Which established histories, relationships, possessions, and Conditions are
  relevant?
- What remains hidden or unresolved?
- What narratorial tempo follows from the actual state?
- What deserves attachment-focused emphasis?
- When must the result be ready?
- Is the resulting experience eligible to enter Memories?

## 2.2 Possible contents

A Moment Brief may conceptually bind:

- the originating event and Record revision;
- actual participants and their current Conditions;
- location, route, Place, Node, or Colony context;
- time, season, weather, light, sound, and visibility;
- carried Tools, Supplies, Keepsakes, or found objects;
- the action attempted;
- the resolved consequence, or explicitly bounded unresolved branches;
- known world state and immediately perceivable terrain;
- relevant Citizen, relationship, Place, and object history;
- species-oriented selective attention;
- required facts;
- prohibited inferences;
- intended presentation deadline; and
- possible Memory, Tale, or Chronicle relevance.

The Moment Brief should be only as large as the moment requires. It should not
become a second summary of the whole campaign.

## 2.3 Authority boundary

The Moment Brief derives from authority and carries no independent authority.
If it conflicts with the Record, the Record controls. If it contains an
unresolved branch, no branch becomes historical truth until play resolves and
the Record commits that outcome.

---

# 3. Narrative Channel

## 3.1 Deterministic narrative Baseline

A deterministic narrative engine can be literary without pretending to be an
unbounded author. It may combine three controlled functions.

### Sentence planning

The engine selects an authored event structure appropriate to the moment, such
as:

- orientation -> action -> consequence;
- pressure -> commitment -> escape;
- discovery -> attention -> changed understanding;
- departure -> absence -> Homecoming;
- injury -> assistance -> remaining distance; or
- vista -> significant feature -> next possibility.

### Authored clause families

MEDIAN may maintain bounded prose fragments tied to truthful conditions. A
clause about rain, exposure, a broken route, a known Place, or a Citizen's
established relationship is eligible only when its conditions are present.

Representative fragments might include:

> The road had gone pale beneath the rain.

> There was no cover close enough to divide the distance.

> The seam beneath the wall was the only part of the world that held still.

> The next anchor ended in open air.

These fragments are examples of an authoring method, not adopted final prose.

### Controlled realization

The engine may assemble its selected structure and clauses while controlling:

- names and pronouns;
- singular and plural agreement;
- species-oriented selective attention;
- tense;
- sentence rhythm;
- repetition;
- established vocabulary; and
- stable variation derived from the event.

The result should be reproducible from the same event and narrative version. A
deterministic passage establishes the truth-bearing presentation against which
optional model output can be judged.

## 3.2 Model-assisted narrative

The language model should not be asked to inspect the entire raw Record and
decide which facts matter. The deterministic narrative function first bounds
the moment. The language model then realizes those authorized facts in the
requested Landscape Voice.

A model-assisted passage should be constrained by:

- the Moment Brief;
- established voice and terminology;
- permitted knowledge;
- prohibited inference;
- approximate length;
- desired narratorial orientation; and
- the requirement not to add facts.

The result is eligible to replace the Baseline passage only if it arrives
before the presentation deadline and remains consistent with the bounded
moment. Unknown names, invented objects, hidden information, premature
outcomes, unsupported emotions, or mechanical contradictions invalidate it.

## 3.3 Landscape Voice

Landscape Voice is a principal narrative realization of this pipeline. It can
render slow spatial attention after a Crossing, compressed perception during
flight, exhaustion during return, or stillness at Home without changing the
facts beneath those modes.

The voice changes attention and tempo, not truth. It remains authoritative
about situated perception and restrained about interpretation.

---

# 4. Imagery Channel

## 4.1 Deterministic imagery Baseline

The deterministic visual baseline should depict the actual moment through
repeatable composition rather than attempting to manufacture a unique painting
for every event.

Where the imagined game already renders its world, an event still may be
composed from:

- a camera orientation appropriate to the moment;
- actual location and terrain state;
- Citizen presence, pose, and Condition;
- significant Tools, Supplies, objects, or hazards;
- time, weather, and light;
- foreground occlusion and animal-scale viewpoint;
- framing suited to Landscape Voice, Encounter, Memory, mailing, or Chronicle;
  and
- a restrained visual treatment appropriate to the event's pace.

Where a reusable world render is unavailable, the same doctrine can be
expressed through layered two-dimensional assets:

```text
location plate
+ terrain-state overlay
+ Citizen portrait or pose
+ action silhouette
+ significant object
+ weather and light
+ foreground occlusion
+ animal-height crop
+ final color treatment
```

The result may resemble a diorama, story plate, naturalist view, portrait, map
detail, or commemorative frame. Its purpose is truthful immediacy rather than
unlimited novelty.

## 4.2 Model-assisted imagery

Model-assisted imagery may use image-to-image generation, but the most recently
generated illustration should not become the sole canonical visual reference.
Repeatedly transforming the last image risks accumulating errors in Citizen
identity, architecture, object count, terrain, and composition.

Visual continuity should instead be re-anchored from stable sources such as:

- Citizen reference sheets;
- location or Colony reference plates;
- the current deterministic composition;
- material, palette, and style guidance;
- relevant object references; and
- the shared Moment Brief.

The prior generated image may contribute continuity, but it must not carry
visual truth by itself.

## 4.3 Art direction

The Moment Brief can produce a bounded art direction directly. An optional
language-model art-direction pass may improve composition and phrasing, but it
should preserve required and prohibited facts.

A conceptual art direction might state:

```text
View: low animal-height landscape
Focus: one Citizen supporting an injured companion
Location: east Margin beside the wrecked sedan Node
Weather and light: late-afternoon rain
Required: two named Citizens; raspberry hedge behind; route ahead visible
Prohibited: visible predator; additional Citizens; human presence
```

The image model realizes the bounded direction. It does not decide what
happened. The resulting illustration remains a presentation of state rather
than state itself.

---

# 5. Predictive Preparation

## 5.1 Use player deliberation as preparation time

Model generation may occur before an asset is needed when the possible results
are already bounded. An Encounter that presents three options creates a natural
preparation interval while the player deliberates.

```text
ENCOUNTER OFFERS A / B / C
            |
            v
THREE PROVISIONAL MOMENT BRIEFS
            |
            v
CANDIDATE PRESENTATIONS PREPARED
            |
            v
PLAYER CHOOSES B
            |
            v
B RESOLVES INTO THE RECORD
            |
            v
B MAY BE EXPERIENCED AND REMEMBERED

A AND C ARE DISCARDED
```

Unused branches are speculative assets, not alternate histories. They must not
enter the Record, Memories, Tales, or Chronicle.

## 5.2 Fully bounded outcomes

If each option completely determines its consequence, the game may prepare all
candidate passages while the player considers the choice. Multiple short
narrative candidates may be produced together when that reduces latency and
preserves a shared voice.

After selection, the chosen candidate must still match the committed outcome.
Only that candidate becomes eligible for presentation or memory.

## 5.3 Outcomes with unresolved variables

If an option still requires a roll, hidden discovery, variable injury,
resource calculation, or another unresolved consequence, the game should not
pre-author a falsely complete result.

It may instead prepare:

- a branch-specific orientation;
- the attempted action;
- a narrative or visual structure with unresolved consequence held open; and
- a deterministic completion once the result enters the Record.

Prediction must not become predictive fiction.

## 5.4 Asymmetric preparation by medium

Narrative candidates are comparatively small and may be practical to prepare
for several bounded options. Full model-generated images are slower and more
expensive.

A conservative visual approach is:

1. Prepare one shared establishing image when the Party enters the Node.
2. Prepare deterministic compositions for all available options.
3. Prepare candidate narrative passages during deliberation.
4. Commission the expensive model-assisted image after selection.
5. Use the deterministic selected image or establishing view immediately.
6. Allow the later illustration to serve Memory, Tale, mailing, Colony view, or
   Chronicle if it remains useful and valid.

This keeps rich illustration outside the critical path while preserving
immediate continuity.

---

# 6. Deadlines, Fallback, and Experienced Truth

## 6.1 Presentation deadline

Every asset request has an experiential deadline. If model output has not
arrived and validated by that point, the deterministic Baseline appears. The
game never waits for optional enrichment.

## 6.2 Late output

A late model result does not silently replace what the player already
experienced. It may:

- be discarded;
- appear later as an explicitly framed retelling;
- illustrate a subsequent Tale or Chronicle entry;
- appear in a mailing or Colony display; or
- become part of a later commemorative view.

If the later rendering changes perspective, it should be presented as later
interpretation rather than retroactive replacement.

## 6.3 Validation failure

An invalid model output is simply unavailable. The Baseline remains complete.
Failure does not trigger another player-facing system or alter the Record.

---

# 7. Memory and Persistence

## 7.1 Experience before preservation

The player first encounters the selected passage or image as part of ongoing
play. Only the resolved, selected moment then becomes eligible for the existing
Memories process.

## 7.2 Provenance

A preserved experience should remain traceable to:

- the Record facts that produced it;
- the participants and Place;
- the selected outcome;
- the narrative or image realization class; and
- the exact passage or image the player experienced.

This provenance does not make narration or imagery authoritative. It ensures
that later interpretation cannot quietly detach from the event.

## 7.3 Levels of duration

Not every presented moment deserves permanent civic history. Existing salience
distinctions remain:

- a moment may remain an immediate or personal Memory;
- it may contribute to a Citizen Tale or Item Tale; or
- it may qualify for the Chronicle when it crosses a civic threshold.

Landscape Voice can make an event vivid without declaring it historically
important.

---

# 8. Sourcebook Appendix Treatment

## 8.1 Purpose

The conceptual pipeline should receive approximately one or two appendix pages
in the future Sourcebook. The appendix should explain how one authoritative
event becomes several truthful forms without presenting a software design.

## 8.2 Proposed page one — From Record to Representation

The first page should center the principal flow:

```text
Player Action -> The Record -> Moment Brief
                                  |
                    +-------------+-------------+
                    |                           |
             Narrative Channel           Imagery Channel
              Baseline / Model           Baseline / Model
                    |                           |
                    +-------------+-------------+
                                  |
                          Experienced Moment
                                  |
                          Memories Gateway
                                  |
                    Memory / Tale / Chronicle
```

Required Baseline paths should use heavy continuous lines. Optional
model-assisted paths should use lighter or dashed lines. The graphic should
make clear that optional generation rejoins the same experiential and memory
path rather than forming another authority.

A smaller inset should show predictive preparation:

```text
A / B / C prepared -> player selects B -> Record commits B
                                         |
                                         v
                              B presented and eligible

A and C discarded
```

## 8.3 Proposed page two — One Moment, Four Renderings

The second page should show one concrete MEDIAN event in four forms:

1. Narrative Baseline
2. Narrative Model
3. Image Baseline
4. Image Model

A compact human-readable Moment Brief should accompany them so the reader can
see that all four outputs describe the same underlying event.

Representative brief:

> Rabbit party emerges onto the east Margin after rain. Clover supports
> injured Marrow. The wrecked sedan is behind them; a raspberry thicket is
> ahead. Late afternoon. No predator is currently visible.

The page should demonstrate expressive difference without factual divergence.

---

# 9. Sourcebook Output Badges

## 9.1 Purpose

Whenever the Sourcebook depicts a hypothetical output from these in-game
systems, the output should carry a small, consistent corner badge. The badge
lets later pages use examples without repeatedly explaining how the example was
realized.

The badge is Sourcebook editorial metadata. It is not necessarily an interface
element shown to the player in the imagined game.

## 9.2 Two-axis convention

Each badge encodes:

1. **Channel:** Narrative or Image
2. **Realization:** Baseline or Model

Preferred full labels are:

```text
NARRATIVE
BASELINE
```

```text
NARRATIVE
MODEL
```

```text
IMAGE
BASELINE
```

```text
IMAGE
MODEL
```

Compact diagram codes may be:

- `N.B` — Narrative Baseline
- `N.M` — Narrative Model
- `I.B` — Image Baseline
- `I.M` — Image Model

`Baseline` means deterministic, locally available, and model-independent.
`Model` means model-assisted realization. It does not mean more authoritative,
more canonical, or necessarily better.

## 9.3 Visual convention

All four badges should share one geometry so they visibly belong to the same
conserved system.

- Channel may be supported by a quotation-mark or frame icon.
- Realization may use restrained color differentiation.
- Baseline should use a neutral structural color.
- Model may use a restrained accent.
- Text labels or codes must remain present so the distinction survives
  grayscale and supports accessibility.
- Placement should remain consistent, preferably upper-right with a fixed safe
  inset.
- The badge must not obscure meaningful prose or image content.

## 9.4 Separate production provenance

The output badge describes the hypothetical in-game realization being
demonstrated. It does not describe how the Sourcebook example itself was
produced.

An `IMAGE / MODEL` example could be manually assembled for explanatory clarity.
An `IMAGE / BASELINE` example could be illustrated using a production model.
Actual Sourcebook art provenance belongs in the production manifest or credits,
not in the in-game output badge.

---

# 10. Conservation of System

This proposal conserves system by deriving multiple expressive capabilities
from one bounded interpretation of existing authority.

It reuses:

- the Record for truth;
- existing world state for context;
- Landscape Voice for situated narration;
- deterministic presentation for reliable operation;
- optional models for enrichment;
- existing transitions for presentation timing; and
- Memories, Tales, and Chronicle for duration.

It should not create:

- separate narrative and image authorities;
- model-only game information;
- a second Record;
- a parallel Memories system;
- alternate histories from unused predictive branches; or
- a requirement that generation complete before play continues.

The architecture does not minimize MEDIAN's artistic ambition. It finds the
smallest common structure capable of multiplying that ambition safely.

---

# 11. Unresolved Development Questions

This Source deliberately leaves open:

- the eventual accepted name for the Moment Brief;
- the exact categories of moments that merit presentation assets;
- how many deterministic sentence and composition families are sufficient;
- how narratorial tempo is derived from state;
- how model output is substantively validated in the imagined game;
- which outputs may be prepared speculatively under different cost settings;
- whether an establishing image persists across several outcomes;
- how an explicitly later retelling differs from the experienced passage;
- how repetition is managed over a long campaign;
- how the pipeline changes across desktop, mobile, tabletop, and card
  manifestations;
- the final graphic design of the four output badges; and
- the final location and pagination of the Sourcebook appendix.

These are development questions rather than instructions to elaborate
additional machinery in advance.
