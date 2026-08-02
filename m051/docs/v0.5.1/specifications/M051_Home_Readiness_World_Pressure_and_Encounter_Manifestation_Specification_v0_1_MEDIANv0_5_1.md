---
title: "MEDIAN v0.5.1 Home Readiness, World Pressure, and Encounter Manifestation Specification"
document_id: M051-HOME-READINESS-WORLD-PRESSURE-001
document_version: 0.1
game_target: MEDIAN v0.5.1
document_kind: additive_home_system_development_specification
authority: active_for_v0_5_1_development_only
state: ACTIVE_DEVELOPMENT
publication_default: internal
created: 2026-08-01
inherits_locked_baseline: MEDIAN v0.5.0
does_not_reopen:
  - MEDIAN v0.5.0 Atomic Extraction
  - MEDIAN v0.5.0 governing architecture
  - MEDIAN v0.5.0 dedicated-owner adjudication
primary_predecessor:
  - M050_Home_Colony_and_DWELL_Specification_v1_0_MEDIANv0_5_0.docx
governing_v0_5_0_sources:
  - M050_Governing_Philosophy_and_Architecture_v1_3_MEDIANv0_5_0.md
  - M050_Human_Rulings_Ledger_v0_4_MEDIANv0_5_0.md
  - M050_MSID_Grammar_v0_5_MEDIANv0_5_0.md
  - M050_Authorial_Grammar_Orthography_and_Prose_Style_Guide_v0_1_MEDIANv0_5_0.md
development_question: >
  Make Colony Readiness, Load, World Pressure, and Colony Encounter
  manifestation specific enough that implementation and authoring do not guess.
---

# MEDIAN v0.5.1
## Home Readiness, World Pressure, and Encounter Manifestation

**Filename:** `M051_Home_Readiness_World_Pressure_and_Encounter_Manifestation_Specification_v0_1_MEDIANv0_5_1.md`

> **MEDIAN v0.5.0 is locked. This document begins additive v0.5.1 development. It may clarify, extend, and tune Home systems, but it may not retroactively alter the meaning of the v0.5.0 corpus or its Atomic Extraction.**

---

# 0. Revision Mandate

The v0.5.0 Home specification establishes the correct architecture:

```text
Citizens hold Roles.
Roles sustain Practices.
Practices inhabit Places.
Places and circumstances create contextual Load.
Role Capacity meeting Load produces Readiness.
Shortfall becomes vulnerability.
MEET turns vulnerability into a situated choice.
```

That architecture is retained without revision.

The remaining problem is specificity. The existing owner identifies the sources of Load, the reference Roles, Margin bands, the Deficiency Ledger, and the Home Encounter grammar, but it does not yet provide a sufficiently complete authoring and implementation model for:

- the canonical Load families;
- which Role answers each family;
- which material channels may modify or answer it;
- how much Capacity or material is normally required;
- what happens when the Colony does not maintain it;
- how the weakness changes Colony Encounter content;
- the ontology of World Pressure;
- the difference between simulated world state and authored special event;
- biome, Season, Day Band, and event variation;
- the exact route from world circumstance to Encounter flavor.

This document begins that work.

It is not a replacement Home specification. It is the first v0.5.1 deepening pass under the locked v0.5.0 owner.

---

# 1. Locked v0.5.0 Baseline

The following are inherited and not reopened.

## 1.1 Home resolves the Colony

At Home, the crunch subject is the Colony. Each present Citizen assigned to a Role contributes one equal unit of Role Capacity. Personal aptitude does not modify ordinary Home output.

```text
1 assigned present Citizen = 1 Capacity in that Role
```

Roles are current civic responsibilities, not classes, skills, or permanent careers.

## 1.2 Load is contextual

A Role is not deficient merely because it exists and is unstaffed.

```text
Role Margin = Role Capacity - Current Role Load
```

Load arises from actual conditions:

- population and households;
- settlement extent;
- Season and forecast;
- active Projects;
- current Conditions;
- Expedition absence;
- species topology and spatial alignment.

A Role with no current contextual demand may be `N/A`.

## 1.3 Adequate maintenance can succeed completely

Routine obligations do not create automatic decay when covered. A functioning Colony can pass ordinary Dawns without deterioration, compulsory clicking, or manufactured crisis.

## 1.4 Shortfall is vulnerability before it is damage

A negative Margin enters the Deficiency Ledger. It changes the Colony's exposure to a relevant problem but does not automatically inflict daily damage.

## 1.5 Home MEET is normally the transaction

A fitting Colony Encounter applies the Big and Small relevant Weaknesses and normally offers:

1. protect the primary stake through one meaningful spend;
2. protect or redirect the secondary stake through a different spend;
3. spend neither and accept the compounded consequence.

The system does not additionally charge the same deficiency through automatic decay, event frequency, worse choices, and a mandatory repair queue unless a deliberately major event justifies every layer.

## 1.6 Species topology changes manifestation

Mouse JOIN, Rabbit GATHER, and Squirrel CONNECT change settlement form, Load geometry, resilience, threatened Places, and the route by which failure spreads.

## 1.7 Stability is an achieved state

Quiet Equilibrium is a real success plateau. The Colony is not paid a bonus for stability; stability creates the time and attention in which attachment-forward life becomes perceptible.

---

# 2. The Three Distinct Things Currently Called Pressure

v0.5.1 must separate three related concepts.

## 2.1 Load

**Load** is the current civic demand placed upon a Role.

```text
Building Load
Care Load
Watch Load
```

Load is answered primarily by Role Capacity.

## 2.2 Deficiency Pressure

**Deficiency Pressure** is the obscured systemic likelihood that one or more negative Role Margins will be tested through a shortage-shaped Colony Encounter.

It is generated by:

- number of deficient Roles;
- depth of deficit;
- persistence;
- cooldown and recent manifestation history.

Deficiency Pressure governs **how often internal thinness seeks a transaction**.

## 2.3 World Pressure

**World Pressure** is a persistent or event-like condition originating outside the Colony's Role allocation.

Examples include:

- heavy wind;
- prolonged rain;
- freeze and thaw;
- drought;
- predator activity;
- human mowing or maintenance;
- migration;
- traffic disruption;
- smoke, fire, spill, or crash;
- unusual ecological abundance or scarcity.

World Pressure governs **what the world is currently doing to the corridor**.

## 2.4 Relationship

```text
World Pressure supplies the circumstance.
Load determines what the Colony must sustain.
Margin determines how prepared the Colony is.
Weakness determines what is at stake.
MEET determines what the player must choose.
```

World Pressure is not simply another name for Deficiency Pressure.

A well-prepared Colony may absorb World Pressure silently. A poorly prepared Colony may generate a shortage-driven Encounter even under ordinary world conditions. A severe external event may open MEET even when every Role has nonnegative Margin; in that case Relative Vulnerability shapes the event without increasing deficiency-generated frequency.

---

# 3. Canonical Load Families

v0.5.1 adopts eight Role-aligned Load families as its working Home taxonomy.

The family is named for the civic obligation, not merely for the corresponding stock or Place.

| Load family | Primary Role | What the Load measures |
|---|---|---|
| **Building Load** | Builder | Structural extent, upkeep, drainage, access, route anchors, coverings, retaining earth, and physical resilience. |
| **Care Load** | Caretaker | Household coordination, dependents, Stores, preservation, relocation, crowding, and ordinary domestic continuity. |
| **Watch Load** | Watchkeeper | Observation, warning, exposed edges, route oversight, forecast interpretation, and early detection. |
| **Leadership Load** | Leader | Coordination, mobilization, fairness, dispute, uneven sacrifice, founding, and Colony-scale decisions. |
| **Cultivation Load** | Gardener | Managed food sources, green-season yield, soil and plant health, harvest transition, and seasonal reserve preparation. |
| **Craft Load** | Crafter | Tool maintenance, material conversion, prepared components, ordinary fabrication, and Supply preparation. |
| **Health Load** | Healer | Current patients, treatment readiness, recovery, illness exposure, rehabilitation, and post-Exposure burden. |
| **Teaching Load** | Teacher | Knowledge transmission, lessons, newcomer integration, shared explanation, cultural continuity, grief, and memory-bearing work. |

These families do not require eight Citizens at all times. Contextual demand and the `N/A` state remain mandatory.

## 3.1 Cross-Role demand tags

Some obligations should not become ninth or tenth Load families merely because several Roles participate.

The following are **cross-Role demand tags**:

```text
Provisioning
Evacuation
Founding
Recovery
Seasonal Transition
Newcomer Integration
Memorial Work
Emergency Mobilization
```

A tag selects or modifies several Load families.

Example:

```text
Winter Provisioning
  Cultivation Load
  Care Load
  Craft Load
  Leadership Load
```

Provisioning is therefore an authored relationship among existing Roles, not a new Provisioner Role or universal Provisioning meter.

---

# 4. Load Is Measured in Capacity, Not Paid as a Resource Tax

The original development prompt asks which resource addresses each Load and how much. The governing answer is:

> **Role Capacity addresses routine Load. Materials do not purchase exemption from civic responsibility.**

## 4.1 Primary conversion

```text
1 Citizen assigned to a Role = 1 Capacity
1 ordinary Load unit = 1 Capacity demand
Margin = Capacity - Load
```

The Capacity-to-Load relationship remains integer-based unless later prototype work proves a narrow need for half-step display. v0.5.1 should not default to decimals.

## 4.2 Routine coverage

When Capacity meets routine Load:

- no additional stock is consumed merely because the Role exists;
- the Practice is understood to perform hundreds of ordinary acts;
- diffuse strain is absorbed;
- the relevant Condition does not decline from passage of time alone.

Universal systems still operate. Sustenance is consumed at Dawn under its own rule. That is not an additional Care or Cultivation tax.

## 4.3 What materials actually do

Existing materials may:

- enable a Project;
- reduce future Load;
- provide a prepared asset;
- lower an Encounter cost;
- protect one stake during MEET;
- transform a severe consequence;
- restore a Condition after a genuinely meaningful loss.

They do not replace Citizens as the heavy-lifting source of Home Capacity.

---

# 5. Resource Channels by Load Family

MEDIAN v0.5.1 uses the locked stock set:

```text
Perishable Sustenance
Durable Sustenance
Flexible Scrap
Rigid Scrap
```

Supplies remain bounded authored consumables:

```text
Binding
Remedy
Distraction
Device
```

There is no separate Medical Stores stock.

| Load family | Routine answer | Relevant stock or Supply channels | Typical material purpose |
|---|---|---|---|
| Building Load | Builder Capacity | Flexible Scrap, Rigid Scrap, Binding, Device | Reinforcement, patching, bracing, drainage, splints for structures, route stabilization. |
| Care Load | Caretaker Capacity | Perishable Sustenance, Durable Sustenance, Flexible Scrap, Binding | Preservation, containers, relocation, household protection, emergency distribution. |
| Watch Load | Watchkeeper Capacity | Device, Distraction, occasionally Flexible Scrap | Markers, alarms, warning aids, decoys, temporary observation positions. |
| Leadership Load | Leader Capacity | Normally no stock; may spend civic attention, Project time, or accept Cohesion/Resolve consequence | Mobilization, coordination, evacuation order, dispute settlement, allocation of sacrifice. |
| Cultivation Load | Gardener Capacity | Perishable Sustenance, Durable Sustenance, Flexible Scrap, Rigid Scrap | Seed and reserve handling, supports, beds, irrigation, protection, harvest and preservation preparation. |
| Craft Load | Crafter Capacity | Flexible Scrap, Rigid Scrap; any Supply recipe allowed by its owner | Tool upkeep, component preparation, conversion of recovered material, emergency substitution. |
| Health Load | Healer Capacity | Sustenance for significant treatment; Remedy; Binding; Rigid Scrap for splints or adaptive devices | Treatment, stabilization, rehabilitation, illness response. |
| Teaching Load | Teacher Capacity | Normally no stock; may require Place, recovered knowledge, memorial material, or Project time | Lessons, integration, records, rites, memorials, cultural continuity. |

## 5.1 No false materialization

Leadership and Teaching must not acquire generic currencies merely so every row has a spend.

Their principal costs are:

- Capacity;
- attention;
- time;
- interrupted Projects;
- Cohesion or Resolve consequence;
- the availability of an appropriate Place;
- specific authored objects or knowledge.

## 5.2 No separate healing stock

Significant treatment may consume ordinary Sustenance. A Remedy may use Sustenance and Flexible Scrap in its recipe. Splints and adaptive devices may require Rigid Scrap. Routine recovery remains primarily a function of time, Healer coverage, Patient Load, and a suitable Place.

---

# 6. Working Cost Grammar

This section begins v0.5.1 tuning. It does not alter the locked v0.5.0 resource ontology.

## 6.1 Routine obligation

```text
Cost: 1 Capacity per 1 Load
Additional stock cost: 0
```

Routine obligation is paid by staffing the Role.

## 6.2 Forecast preparation

A preparation Project normally costs:

```text
1-4 Citizen-Days
0-2 units of relevant existing stock
no more than two stock types in one recipe
```

The exact Project determines the amount.

Preparation may:

- reduce one named incoming Pressure by one intensity step;
- convert an ordinary Encounter into silent success;
- reduce one option cost;
- protect a specific Place or household;
- supply one prepared asset.

Preparation does not grant permanent universal immunity.

## 6.3 Ordinary Colony Encounter spend

The default ordinary response should ask for **one meaningful cost channel**, normally:

```text
1 unit of one relevant stock
or
1 available positive Role Margin committed through the next Dawn
or
1 Citizen-Day of current Project progress interrupted or redirected
or
1 prepared asset consumed
or
one bounded Cohesion / Resolve consequence accepted
```

A choice may combine fiction and presentation around the cost, but should not hide multiple mechanical charges inside one button.

## 6.4 Major response

A major response may require:

```text
2 total stock units
or
1 stock unit plus 1 nonmaterial opportunity cost
or
2 distinct nonmaterial opportunity costs
```

This should protect a correspondingly major stake.

## 6.5 Exceptional event

An exceptional authored event may exceed the ordinary grammar, but it must identify itself as exceptional and must not redefine the everyday cost baseline.

## 6.6 Refusal

Refusal spends no immediate resource. It accepts a compound result affecting the primary and secondary stakes.

Refusal must remain a legitimate strategic answer when the Colony chooses to preserve scarce reserves for a greater known Pressure.

---

# 7. Margin, Shortfall, and Consequence

The inherited Margin bands remain:

| Margin | State | v0.5.1 interpretation |
|---:|---|---|
| +2 or more | **Reserve** | Meaningful slack; can absorb absence, preparation, substitution, or ordinary external Pressure. |
| +1 | **Ready** | One useful share of readiness; a forecast event may be handled silently. |
| 0 | **Covered** | Stable but brittle; routine obligation is met, but added Pressure has no buffer. |
| -1 | **Thin** | One share unsupported; no automatic damage, but a relevant transaction becomes likelier and more expensive. |
| -2 or worse | **Exposed** | Deep or persistent shortfall; severe manifestations become eligible and Pressure rises faster. |
| N/A | **No current demand** | The Role does not enter deficiency count. |

## 7.1 Consequence ladder

Failure to maintain a Load family should proceed through a restrained ladder.

### A. Latent vulnerability

- warning appears;
- Margin is visibly Thin or Exposed;
- no automatic damage;
- future relevant MEET becomes more likely.

### B. Cost escalation

When a fitting Encounter occurs:

- the relevant protective option may require a higher spend;
- the secondary stake may become harder to redirect;
- silent absorption may no longer be available.

### C. Global Condition consequence

The refusal or failed protection may reduce or worsen:

- Structural Condition;
- Stores;
- Cohesion / Resolve;
- Health posture;
- seasonal preparedness;
- general availability.

### D. Transformative local consequence

Used sparingly:

- a Place becomes unusable;
- a household is displaced;
- a route or node closes;
- a Place is renamed or recontextualized;
- a focused restoration Project becomes necessary;
- a specific Citizen becomes a patient or bears a visible injury.

## 7.2 Load-family consequence channels

| Weak Load family | Primary consequence channel | Common collateral channel |
|---|---|---|
| Building | Structural Condition, access, Place usability | Stores, displacement, injury |
| Care | Stores, household protection, displacement | Cohesion, Health |
| Watch | Late warning, lost preparation window, route exposure | Structural loss, injury, Stores |
| Leadership | Cohesion / Resolve, mobilization delay, uneven sacrifice | Project interruption, displacement |
| Cultivation | Perishable yield, Durable reserve, seasonal preparedness | Cohesion, Care burden |
| Craft | Tool and component availability, higher material cost | Structural Condition, Expedition preparation |
| Health | Patient burden, recovery delay, illness spread | Care burden, availability |
| Teaching | Integration, knowledge continuity, grief, identity strain | Leadership burden, Cohesion |

## 7.3 No automatic one-to-one punishment

A Building shortfall does not always cause building damage. It makes structural stakes available and changes how a fitting event manifests.

The same Builder weakness may appear as:

- a roofline at risk under Heavy Winds;
- a soft retaining edge under Flash Flood;
- frozen access under a Cold Snap;
- insufficient bracing during human mowing;
- costly expansion during a chosen Project.

---

# 8. World Pressure Ontology

## 8.1 Definition

> **World Pressure is an externally originating corridor condition that may change Load, test Readiness, alter ordinary life, or supply the circumstance for MEET.**

World Pressure is broader than weather.

## 8.2 Pressure families

v0.5.1 begins with six working families.

| World Pressure family | Examples |
|---|---|
| **Atmospheric** | Wind, rain, hail, humidity, smoke, heat, sudden cold. |
| **Hydrological and Ground** | Flood, saturation, washout, drought, erosion, freeze-thaw, ice, blocked drainage. |
| **Biological** | Predator activity, disease ecology, insect abundance, migration, invasive growth, forage cycle. |
| **Human Corridor** | Mowing, maintenance, roadwork, salting, pesticide, litter removal, drainage work, traffic diversion. |
| **Traffic and Mechanical** | Unusual traffic density, crash, vibration, debris throw, idling, lane closure, vehicle fire. |
| **Exceptional Event** | Major storm, spill, fire, mass displacement, construction project, unusual arrival, corridor-scale disturbance. |

Seasonal ecology is expressed as a profile across these families rather than a seventh universal Pressure.

Social and civic problems are not normally World Pressure. Newcomer strain, grief, dispute, and uneven sacrifice are internal Colony circumstances, though an external event may cause them.

## 8.3 Pressure record

A tracked World Pressure should be representable by:

```yaml
pressure_family:
canonical_name:
intensity:
duration:
forecastability:
spatial_footprint:
affected_load_families:
biome_expression:
season_expression:
day_band_expression:
special_event_status:
recent_manifestations:
```

## 8.4 Intensity

Use a small qualitative scale:

| Intensity | Meaning |
|---|---|
| **Background** | Part of ordinary environmental life; usually absorbed by routine Load. |
| **Present** | Meaningfully changes one or more current Loads or ordinary presentation. |
| **Severe** | Can open MEET, deepen consequences, or affect several Load families. |
| **Exceptional** | Authored corridor event that may override normal frequency safeguards. |

Exact hidden numbers may exist in implementation, but the player-facing grammar remains qualitative.

## 8.5 Duration

World Pressure may be:

```text
Momentary
Day-bound
Multi-Dawn
Seasonal
Persistent until changed
```

Duration should change content and Load, not merely repeat the same event card.

---

# 9. Is World Pressure Perpetually Simulated?

The answer is **yes in continuity, no in computational or attentional burden**.

## 9.1 Continuous world-state doctrine

The corridor has one persistent world state. Weather, Season, traffic, human activity, and ecological cycles do not cease to exist when the player looks elsewhere.

## 9.2 Banded adjudication

Home does not require minute-by-minute simulation.

World Pressure normally updates at:

- DAWN;
- a Day Band transition when materially relevant;
- the start or end of a forecast event;
- a special-event trigger;
- a meaningful player-caused state change.

The interface surfaces only meaningful changes.

## 9.3 Not purely uninfluenceable

The player usually cannot prevent:

- rain;
- wind;
- winter;
- traffic;
- mowing schedules;
- predator movement.

The player can influence:

- forecast quality;
- preparation;
- settlement exposure;
- route redundancy;
- Stores;
- Role Margin;
- Place support;
- evacuation readiness;
- which stakes are protected;
- how quickly the Colony recovers.

> **World Pressure is exogenous in origin and mediated in consequence.**

Some pressures are partially influenceable. The Colony may alter drainage, remove attractants, create warning lines, establish cover, negotiate with a Guest, or abandon an exposed Place. Such acts change the relationship to Pressure rather than switching the world off.

---

# 10. Variation by Biome, Season, Day Band, and Special Event

## 10.1 Biome

Biome establishes:

- baseline Pressure distribution;
- available shelter and material;
- ordinary drainage and soil behavior;
- predator and competitor palette;
- vegetation rhythm;
- human-maintenance pattern;
- visual and acoustic Encounter vocabulary.

Biome should not create a separate Home engine. It supplies different inputs to the shared Pressure and Load model.

Example:

| Biome trait | Likely Pressure emphasis |
|---|---|
| Dry exposed median | Heat, drought, wind, sparse cover, mowing visibility |
| Wet low median | Saturation, flash flood, mold, soft ground, drainage work |
| Wooded broad median | Falling limbs, predator cover, leaf accumulation, shade, fire risk |
| Urban engineered median | Vibration, debris, human maintenance, runoff, artificial heat, lighting |
| Cold northern corridor | Freeze-thaw, snow load, salt, reduced green yield, winter access |

## 10.2 Season

Season changes:

- frequency;
- duration;
- forecast horizon;
- affected Load families;
- normal resource flow;
- sensory and Narrative presentation.

Example:

| Season | Typical Home emphasis |
|---|---|
| Spring | Saturation, washout, growth, planting, migration, repair after winter |
| Summer | Heat, drought, storms, high traffic, cultivation, predator activity |
| Autumn | Harvest, preservation, leaf and drainage burden, cooling, migration |
| Winter | Durable reserve, cold, ice, snow load, reduced access, illness and recovery |

Season is not a universal penalty. A prepared Colony can coast through ordinary seasonal days.

## 10.3 Day Band

Day Band modifies a Pressure when the difference is materially legible.

| Day Band | Common modifiers |
|---|---|
| Morning | Dew, cold start, first traffic surge, fresh tracks, early warning |
| Midday | Heat, visibility, human work, traffic density, drying |
| Evening | Cooling, commuter traffic, household return, predator transition |
| Night | Reduced human work, darkness, cold, altered predator activity, sound carrying |

Day Band should usually change:

- warning quality;
- who is present;
- presentation;
- traffic and predator activity;
- immediate option costs.

It should not add a universal Night penalty.

## 10.4 Special events

A special event is a bounded authored change to ordinary Pressure state.

Examples:

- road resurfacing begins;
- a storm remnant stalls over the corridor;
- a crash spills material or fire;
- a mowing crew enters the median;
- a mass migration crosses;
- an unusual freeze arrives after green growth;
- a new human barrier changes drainage;
- a Guest population arrives under distress.

Special events may:

- create new temporary Loads;
- change a Pressure family to Severe or Exceptional;
- alter spatial footprint;
- create a multi-stage situation;
- persist as a Condition or Project after MEET.

They must still use existing systems wherever possible.

---

# 11. From World State to Colony Encounter

A Colony Encounter is not generic flavor attached after the calculation. Its fiction is generated from the same state that creates the choice.

## 11.1 Manifestation pipeline

```text
1. World state establishes plausible Pressure families.
2. Deficiency Pressure or external severity establishes whether MEET is due.
3. The selected Encounter family defines the relevant Role mask.
4. Big and Small Weakness select primary and collateral stakes.
5. Species topology selects threatened geometry and failure spread.
6. Biome, Season, and Day Band select sensory and situational expression.
7. Current Places and Conditions select the exact tableau.
8. Named Role holders provide advice, disagreement, fear, or practical framing.
9. Campaign history adds callbacks without changing hidden productivity.
10. Two spends and one refusal resolve the transaction.
11. Consequences return to global Conditions, Stores, Projects, availability, or rare local loss.
```

## 11.2 What each layer contributes

| Layer | Authoring contribution |
|---|---|
| World Pressure | What is happening |
| Encounter family | What kind of problem this is |
| Big Weakness | What the Colony is least able to protect |
| Small Weakness | What else is endangered or complicates the response |
| Species topology | Where it happens and how it spreads |
| Biome | Material and environmental vocabulary |
| Season | Timing, expectedness, and resource context |
| Day Band | Light, sound, activity, and warning conditions |
| Places | Exact threatened location |
| Role holders | Human-scale—or animal-scale—voice and advice |
| Campaign Memory | Why this manifestation belongs to this Colony |
| Choice grammar | What the player must sacrifice or accept |

## 11.3 Flavor rule

> **Colony Encounter flavor is state-derived recombination, not random decorative text.**

The same Heavy Winds family should not merely swap species names. It should threaten different geometry, expose different weak Roles, require different credible resources, and foreground different ordinary lives.

---

# 12. Weakness-Shaped Encounter Examples

## 12.1 Heavy Winds: Builder + Caretaker weakness

**World state**

```text
Atmospheric Pressure: Heavy Winds / Severe
Season: Autumn
Day Band: Evening
```

**Mouse expression**

The joined roofline above the pantry chambers flexes as pressure finds a recently extended seam. The Manor House protects the Colony from open exposure, but one poor join can carry movement through connected rooms.

**Primary stake**

Structural Condition and the integrity of the joined roofline.

**Secondary stake**

Stores and households beneath it.

**Choices**

1. Spend Rigid Scrap or a prepared Binding and interrupt one Builder Project to brace the seam.
2. Commit Caretaker reserve through the next Dawn and move households and Stores inward, accepting controlled structural strain.
3. Spend neither; suffer compounded Structural and Stores consequence, with possible displacement.

## 12.2 Heavy Winds: Watchkeeper + Leader weakness

The wind itself is unchanged. The manifestation changes because warning and mobilization are thin.

The Colony learns too late that one exposed edge is failing. A known weak Place could have been emptied or braced, but households have not agreed which Court or chamber will accept them.

The primary stake becomes timing. The secondary stake becomes fair mobilization.

## 12.3 Flash Flood: species topology

**Mouse**

Water enters through one failed protected portal and threatens continuity through connected interior passages.

**Rabbit**

The Court's common ground becomes the collection basin; the question is which households remain neighbors when the center cannot be used.

**Squirrel**

One low route and its caches are cut off; redundancy determines whether the Web reroutes or fragments.

The Pressure family is shared. JOIN, GATHER, and CONNECT write different failure geometry.

## 12.4 Human maintenance

A mowing crew or drainage team is not weather.

It may affect:

- Watch Load through forecast and warning;
- Building Load through access and cover;
- Care Load through evacuation and Stores movement;
- Leadership Load through coordinated sacrifice;
- Teaching Load if records, memorials, or culturally important Places must be moved;
- species topology through the particular way the settlement occupies space.

This family is crucial because it makes the highway corridor a human-maintained environment rather than generic wilderness.

---

# 13. Colony Encounter Authoring Matrix

Every reusable Encounter family should eventually declare:

```yaml
encounter_family:
world_pressure_families:
required_context:
eligible_roles:
common_big_weaknesses:
common_small_weaknesses:
biome_variants:
season_variants:
day_band_variants:
species_manifestations:
primary_stake_types:
secondary_stake_types:
ordinary_cost_channels:
major_cost_channels:
refusal_consequences:
silent_success_conditions:
cooldown_category:
persistence_behavior:
```

## 13.1 Minimum authoring standard

A complete family needs:

- at least three credible Big Weakness manifestations;
- at least three credible Small Weakness complications;
- a distinct Mouse, Rabbit, and Squirrel spatial expression;
- at least two biome or seasonal variants;
- one silent-success presentation;
- one ordinary three-choice transaction;
- one severe but noncatastrophic manifestation;
- a cooldown and repetition rule.

## 13.2 Repetition protection

A family should remember:

- recently threatened Places;
- recent Big and Small Weakness pairings;
- recent costs;
- recent consequences;
- whether the Colony prepared successfully;
- whether the event remains unresolved.

The director should prefer variation without inventing irrelevant Roles.

---

# 14. Information Architecture

The player should see:

- current Role Capacity;
- current Role Load;
- qualitative Margin;
- named Role occupants;
- current Conditions;
- current Stores;
- Season;
- forecast World Pressures;
- known special events;
- broad consequence previews;
- the posture change caused by an Expedition departure.

The player should not see:

- exact Deficiency Pressure score;
- exact next trigger;
- hidden Big and Small Weakness ranking;
- full probability tables;
- every future manifestation;
- internal cooldown arithmetic.

## 14.1 Dawn ledger

The Dawn ledger should add one compact World Pressure section:

```text
WORLD
Cold rain continues through Midday.
Low ground remains saturated.
Human drainage work is forecast in two Dawns.

READINESS
Building: COVERED
Care: THIN
Watch: READY
Leadership: COVERED

INTERPRETATION
The Colony is stable, but Stores movement and household shelter are lightly attended.
```

After the ledger is read, the interface quiets.

---

# 15. Development Decisions Settled in v0.1

This first v0.5.1 document adopts the following development propositions:

1. Load, Deficiency Pressure, and World Pressure are distinct.
2. Eight working Load families map to the eight established Home Roles.
3. Routine Load is answered by Capacity, not by recurring material tax.
4. Existing stocks and Supplies modify preparedness, Projects, Encounter costs, and recovery; they do not replace Citizens.
5. World Pressure is broader than weather.
6. World Pressure is continuously true but banded in adjudication.
7. World Pressure is exogenous in origin and mediated in consequence.
8. Biome, Season, Day Band, and special events modify shared Pressure families rather than create parallel Home engines.
9. Colony Encounter flavor is generated through state-derived recombination.
10. The same World Pressure must produce materially different manifestations through Weakness profile and species topology.
11. v0.5.0 Atomic Extraction must not use this v0.5.1 document to reinterpret the locked corpus.

---

# 16. Open v0.5.1 Decisions

The following remain to be developed and tested.

## 16.1 Load tuning

- Exact Load formulas by population, Place count, extent, and Tier.
- Whether any Load source requires threshold steps rather than linear addition.
- How low-population Colonies receive Gentle Loads and substitution.
- Whether mixed Guest residency alters Load through body count, Place requirements, or authored support tags.

## 16.2 Cost tuning

- Confirm the `1-4 Citizen-Day` preparation range.
- Confirm ordinary one-channel and major two-channel Encounter costs.
- Establish stock-unit expectations by Tier.
- Establish when positive Margin can be committed as a spend and how long it remains unavailable.
- Confirm the current status and name of Cohesion / Resolve.

## 16.3 Pressure tuning

- Exact intensity transition rules.
- Forecast reliability.
- Multi-Dawn persistence and escalation.
- Biome profiles.
- special-event frequency.
- interactions with current Conditions.
- whether traffic and human maintenance require separate subfamilies.

## 16.4 Encounter content

- Full family list.
- Role masks.
- species manifestations.
- biome and seasonal variants.
- cooldown categories.
- silent-success text.
- aftermath and persistence rules.

## 16.5 MSIDs

Candidate branches for later adjudication:

```text
Home.Colony.Load
Home.Colony.Load.Building
Home.Colony.Load.Care
Home.Colony.Load.Watch
Home.Colony.Load.Leadership
Home.Colony.Load.Cultivation
Home.Colony.Load.Craft
Home.Colony.Load.Health
Home.Colony.Load.Teaching

Home.Colony.Readiness
Home.Colony.Margin
Home.Colony.Deficiency

World.Pressure
World.Pressure.Atmospheric
World.Pressure.Hydrological
World.Pressure.Biological
World.Pressure.HumanCorridor
World.Pressure.Traffic
World.Pressure.ExceptionalEvent
```

The `World` top-level domain remains unadjudicated in the v0.5.0 grammar. These are v0.5.1 candidates only.

---

# 17. v0.5.0 Atomic Extraction Boundary

This document is not evidence for what v0.5.0 already meant.

During the locked v0.5.0 Atomic Extraction:

- extract the v0.5.0 Home owner literally;
- preserve its actual Load sources, Role rules, Margin bands, and open tuning;
- do not import the eight-family taxonomy unless the source itself supports the claim;
- do not import v0.5.1 cost bands;
- do not use the new World Pressure ontology to close v0.5.0 namespace questions;
- record this document only as a future-development descendant after v0.5.0 extraction is complete.

---

# 18. Acceptance Tests for the Completed v0.5.1 Pass

| Test | Passing condition |
|---|---|
| Complete Load map | Every recurring Home obligation belongs to one primary Load family or an explicit cross-Role tag. |
| No false resource tax | Routine covered Load does not consume arbitrary material each Dawn. |
| Legible answer | The player can tell which Role, Place, preparation, or stock channel can improve a vulnerable posture. |
| Exact enough to author | An Encounter writer can determine eligible Roles, stakes, costs, and consequences without inventing system rules. |
| World is more than weather | Human maintenance, traffic, biological activity, and exceptional corridor events use the same Pressure framework. |
| No parallel biome engines | Biomes change profiles and manifestations without replacing the Home system. |
| Day Band restraint | Time of day changes relevant activity and presentation without imposing a universal Night penalty. |
| Silent success | Readiness can absorb forecast Pressure without opening MEET. |
| Weakness specificity | The same Pressure family changes materially under different Big and Small Weaknesses. |
| Species specificity | Mouse, Rabbit, and Squirrel manifestations differ in threatened geometry and failure propagation. |
| No double charge | A shortfall normally transacts through one clear Encounter rather than stacked automatic penalties. |
| Recovery | A strained Colony has a clear route back to Quiet Equilibrium. |
| v0.5.0 lock | No v0.5.1 proposition is retroactively used to alter v0.5.0 Atomic Extraction. |

---

# Appendix A — Original Deferred Development Prompt

> Next, a short but deep dive on the systems of Home Mode. Colony readiness—what are all the types of Load? What Roles address them? What “resource” addresses them and how much? What are consequences for not maintaining them? How do they affect the Colony Encounter flavor?
>
> What are the World Pressures, how do they manifest, how do they vary by biome, Season, time of day, and special events? Are they just perpetually tracked simulated Conditions that are uninfluenceable—essentially “weather”? How do they affect Colony Encounter flavor?
>
> Let’s be specific and not leave this to guesswork in the compiling.

---

# Change Record

## v0.1 — 2026-08-01

- Opened the first MEDIAN v0.5.1 systems document after the explicit v0.5.0 lock.
- Preserved the v0.5.0 Home architecture without reopening it.
- Distinguished Load, Deficiency Pressure, and World Pressure.
- Proposed eight Role-aligned Load families.
- Established Capacity as the primary answer to routine Load.
- Mapped existing stocks and Supplies to preparation, response, and recovery without creating new currencies.
- Added a working cost grammar for preparation and Colony Encounters.
- Defined six working World Pressure families.
- Defined banded persistent simulation and the doctrine that World Pressure is exogenous in origin and mediated in consequence.
- Defined biome, Season, Day Band, and special-event variation.
- Formalized the Colony Encounter manifestation pipeline.
- Added authoring matrices, examples, development decisions, open questions, and acceptance tests.
- Preserved a hard boundary preventing v0.5.1 from affecting v0.5.0 Atomic Extraction.
