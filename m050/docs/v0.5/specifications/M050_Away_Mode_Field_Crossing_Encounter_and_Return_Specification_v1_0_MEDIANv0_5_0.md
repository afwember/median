<!--@0¶1-->
MEDIAN / SYSTEM SPECIFICATION / v0.5.0

<!--@0¶2-->
THE AWAY LOOP REWORK

<!--@0¶3-->
TRAVEL / RISK / MEET • EXPEDITION, EXPOSURE, AND RETURN

<!--@0¶4-->
A companion architecture to the v0.5 Home Mode, Colony, and DWELL Specification. This document revises the Away material developed in the v0.4.7 decisions log under the governing premise that Home grows the Colony and Away grows, hazards, and changes particular Citizens.

<!--@0¶5-->
| **Document field** | **Specification**                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------- |
| Document version   | 1.0 — initial v0.5 alignment pass                                                             |
| Game-system target | MEDIAN v0.5.0                                                                                 |
| Module             | Away Mode / Field, Crossing, Encounter, Launch, Return, Homecoming                            |
| Precedence         | v0.5 philosophical, Home, and Embodiment specifications lead all conflicting v0.4.7 decisions |
| Status             | Working specification for structured v0.5 revision document                                   |

<!--@0¶6-->
<table>
<tbody>
<tr class="odd">
<td>CANONICAL PREMISE<br />
At Home, a Citizen is one equal share of civic commitment. Away, that same Citizen becomes an individually resolved bearer of capability, history, equipment, Exposure, and consequence.</td>
</tr>
</tbody>
</table>

<!--@1-->
## Source basis

<!--@1¶1-->
  - MEDIAN v0.4.7 — Running Decisions: Register/View distinction, Twin Modes, Launch, Crossing, Field, Nodes, Encounter grammars, Return, Homecoming, outposts, and corridor shape.

<!--@1¶2-->
  - The Home Mode, Colony, and DWELL Specification: equal Home shares, Capacity / Load / Margin, legible expedition absence, Quiet Equilibrium, Home MEET, and successful stillness.

<!--@1¶3-->
  - The Embodiment Register: five-Register topology, Home-only EMBODY, Exposure ebb in sanctuary, and the cycle of danger, return, equilibrium, embodiment, and memory.

<!--@1¶4-->
  - The v0.5 philosophical and manifestation specifications: Home/Away subject split, shared world state, attachment-first stewardship, and the universal preparation–departure–risk–return cycle.

<!--@1#2-->
# 0\. Revision Mandate and Precedence

<!--@1#2¶1-->
This is not a restatement of v0.4.7. It is a governed revision. Where the older log and today’s v0.5 work disagree, v0.5 leads. Useful structures are preserved; contradictory assumptions are explicitly superseded rather than silently carried forward.

<!--@1#2¶2-->
| **v0.4.7 proposition**                          | **v0.5 ruling**                          | **Consequence**                                                                                                                            |
| ----------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Four Registers only; no fifth Register          | Superseded by EMBODY                     | Away retains TRAVEL, RISK, and MEET; Home retains DWELL and EMBODY; MEET remains cross-modal.                                              |
| Encounter verb INTERACT                         | Superseded by MEET                       | A colony may meet wind; an expedition may meet a stranger, a resource, a blockage, or a need.                                              |
| Field can remain Home before anyone crosses     | Superseded by the simulation-scale split | The Mode changes at Launch. TRAVEL on the Home Reach is already Away because particular Citizens are now the crunch subject.               |
| Exposure reserved for contested Encounters      | Superseded                               | Personal Exposure may arise through TRAVEL, RISK, or MEET. Each Register creates it differently.                                           |
| Crossing has no Exposure                        | Superseded                               | Crossing does not use the MEET Exposure procedure, but its bodily danger can add Exposure, wounds, fear, separation, cargo loss, or Tharn. |
| Fixed five Approaches everywhere                | Narrowed                                 | The fixed five remain the provisional grammar of contested Away MEET only. Home MEET uses the v0.5 two-spend-or-refuse structure.          |
| 70/20/10 return Crossing roll                   | Replaced by burden-based return logic    | The return Crossing is elided, abbreviated, or played in full according to time, load, injury, route familiarity, and traffic conditions.  |
| Held Reach carries partial Home state           | Narrowed to refuge                       | An outpost supports Stopover, rest, care, warning, and storage, but not full DWELL, Quiet Equilibrium, or EMBODY.                          |
| Experienced Home workers fare better off-screen | Superseded                               | Home outcome depends on remaining Role Capacity, Places, topology, and Readiness—not personal productivity aptitude.                       |

<!--@1#2¶3-->
<table>
<tbody>
<tr class="odd">
<td>REVISION TEST<br />
No Away rule may weaken the clarity of the v0.5 Home Loop. Departure must create a legible domestic subtraction; return must convert particular consequences back into Colony posture.</td>
</tr>
</tbody>
</table>

<!--@2-->
# 1\. Executive Summary and Canonical Definition

<!--@2¶1-->
Away Mode is the expedition architecture of MEDIAN. It begins when named Citizens leave domestic stewardship and become a particular party committed to distance, risk, opportunity, and return. Its subject is not abstract exploration progress. Its subject is what happens to these friends because they chose to carry the Colony’s need beyond sanctuary.

<!--@2¶2-->
<table>
<tbody>
<tr class="odd">
<td>CANONICAL DEFINITION<br />
Away Mode carries particular Citizens through extended territory, immediate highway danger, and bounded consequential situations. It accumulates material, knowledge, relationships, wounds, Exposure, and memory until Homecoming returns those facts to the Colony.</td>
</tr>
</tbody>
</table>

<!--@2.1-->
## System purposes

<!--@2.1¶1-->
  - Make departure a civic and emotional commitment rather than unit deployment.

<!--@2.1¶2-->
  - Turn Home headcount into individual Away capability without contradicting equal Home value.

<!--@2.1¶3-->
  - Give the highway a distinct RISK grammar that is brief, embodied, and categorically unlike ordinary travel.

<!--@2.1¶4-->
  - Make territory readable through route, time, load, weather, known shelter, and resource relationships.

<!--@2.1¶5-->
  - Concentrate consequential interaction in MEET without making every step an event card.

<!--@2.1¶6-->
  - Allow Exposure to widen outcomes toward courage, distinction, fear, injury, Maiming, Tharn, and loss.

<!--@2.1¶7-->
  - Require the haul, the hurt, and the history to be carried home rather than teleported into storage.

<!--@2.1¶8-->
  - Make Homecoming a playable reintegration of Citizens and Colony, not an inventory summary.

<!--@2.2-->
## Canonical system statement

<!--@2.2¶1-->
DWELL produces a need or ambition. LAUNCH subtracts named Citizens from Colony Capacity. TRAVEL turns geography into distance and burden. RISK turns traffic into immediate bodily commitment. MEET turns a place, Presence, or opportunity into consequence. RETURN carries the changed party back. HOMECOMING converts personal facts into Colony facts. DWELL then restores equilibrium, and EMBODY makes the restored safety felt.

<!--@3-->
# 2\. Register Architecture and Mode Boundaries

<!--@3¶1-->
| **Register** | **Verb** | **Availability** | **Away function**                                                                       |
| ------------ | -------- | ---------------- | --------------------------------------------------------------------------------------- |
| Field        | TRAVEL   | Away             | Carry a party through extended territory, route choices, time, weather, drag, and load. |
| Crossing     | RISK     | Away             | Resolve immediate lane-scale panic, commitment, traffic windows, and bodily hazard.     |
| Encounter    | MEET     | Home and Away    | Stage a bounded consequential circumstance and ask what the Colony or party will do.    |
| Colony       | DWELL    | Home             | Creates the need, loses the departing shares, and receives the return.                  |
| Embodiment   | EMBODY   | Home only        | Becomes available only after return and restored Quiet Equilibrium.                     |

<!--@3.1-->
## Mode-switch doctrine

<!--@3.1¶1-->
Mode is defined by the crunch subject, not by geography or camera. Launch is the outward threshold: once the party commits, particular Citizens become the resolved subject and the game is Away—even while they still traverse the Home Reach toward the road edge. Homecoming is the inward threshold: the game becomes Home only when the Colony has received the returning party and recalculated its civic posture.

<!--@3.1¶2-->
<table>
<tbody>
<tr class="odd">
<td>MODE TEST<br />
Before Launch: “How much Colony capacity is committed?”<br />
After Launch: “Which particular Citizens are carrying this?”<br />
After Homecoming: “What can the Colony now sustain, repair, remember, and permit?”</td>
</tr>
</tbody>
</table>

<!--@3.2-->
## Register/View doctrine retained

<!--@3.2¶1-->
A Register is a mode of attention. A View is a particular presentation within it. Launch and Homecoming are connector Views using MEET’s fixed, consequential attention without becoming separate Registers. Staging, Stopover, and Chronicle are also Views or layers, not new modes.

<!--@4-->
# 3\. Foundational Design Principles

<!--@4¶1-->
**Citizens leave because they belong.** Expeditions are a commitment to sustain, grow, reconnect, or understand the Colony—not a detached hero career.

<!--@4¶2-->
**Launch is subtraction.** The Colony visibly loses the exact named shares, occupancy, and availability that depart.

<!--@4¶3-->
**Away is individually resolved.** Species capability, equipment, wounds, fear memories, relationships, route knowledge, Distinctions, and personal history matter here.

<!--@4¶4-->
**Facts belong to world state.** One injury, one cargo object, one relationship, one route, one clock, and one record are exposed differently by each Register; no parallel versions are created.

<!--@4¶5-->
**Nodes are the meal; cards are the weather.** Field traversal is not a stream of event popups. Most consequence is anchored to places the player chooses to enter.

<!--@4¶6-->
**Crossing is brief because it is terrible.** RISK must remain concentrated, committed, and legible; it must not become a full action game layered over the rest of MEDIAN.

<!--@4¶7-->
**Return is the second half.** Finding or winning something is not possession. The party must carry it through the corridor and across the road.

<!--@4¶8-->
**Home is not a third exposure zone.** While attention is Away, the Colony may change and improvise, but named Citizens are not killed or catastrophically harmed off-screen.

<!--@4¶9-->
**Care is consequence, not optimization.** Tending a returned friend matters even when it is not the statistically superior action.

<!--@4¶10-->
**The player may turn back.** Withdrawal is not failure by default. Choosing what can be safely brought home is a central expedition skill.

<!--@5-->
# 4\. The Complete Expedition Cycle

<!--@5¶1-->
| **Beat**                 | **Register / View**          | **Mechanical subject**                | **Persistent change**                                                           |
| ------------------------ | ---------------------------- | ------------------------------------- | ------------------------------------------------------------------------------- |
| Need or ambition         | DWELL                        | Colony posture                        | A reason to leave becomes legible.                                              |
| Launch                   | MEET — Launch View           | Named volunteers and Home subtraction | Party, purpose, Supplies, and reduced Role margins are committed.               |
| Approach to edge         | TRAVEL — Home Reach          | Particular party                      | Time begins; familiar Home geography becomes a route.                           |
| Staging                  | RISK — Staging View          | Party, load, traffic, chosen edge     | Crossing posture and immediate constraints are set.                             |
| Outbound Crossing        | RISK                         | Bodies in lanes and windows           | Exposure, delay, wound, cargo, fear, separation, or clean passage.              |
| Margin / corridor travel | TRAVEL                       | Party through Reaches                 | Time, load, route knowledge, Conditions, and resource access change.            |
| Node or interruption     | MEET                         | Party in a bounded situation          | Outcome, cargo, relationships, knowledge, and personal consequence.             |
| Decision to return       | TRAVEL                       | Party and remaining day               | Ambition is bounded by what can still be brought home.                          |
| Return route             | TRAVEL                       | Changed and often laden party         | The haul and the hurt affect the route.                                         |
| Return Crossing          | RISK or abbreviated RISK     | Burdened party                        | Final passage reflects accumulated cost.                                        |
| Homecoming               | MEET — Homecoming View       | Returning party ↔ receiving Colony    | Care, stores, Guests, knowledge, absence, and Role availability are integrated. |
| Restored life            | DWELL → EMBODY when eligible | Colony, then available Citizens       | Equilibrium, memory, and embodied sanctuary become possible again.              |

<!--@5.1-->
## Continuity rule

<!--@5.1¶1-->
The cycle should feel continuous. Camera, time scale, and control grammar may change, but there is no conceptual teleport between “mission screen” and “base screen.” The colony remains behind the departing party; the road edge becomes Staging ground; the Margin becomes Field; the returning party physically re-enters Homecoming.

<!--@6-->
# 5\. Expedition Launch — The Outward Bracket

<!--@6¶1-->
Launch is a MEET View in which the Colony’s need is brought into consequential relationship with named Citizens who may answer it. It is not a formation optimizer or hidden-odds comparison screen.

<!--@5.1#2-->
## 5.1 Sources of expedition purpose

<!--@5.1#2¶1-->
| **Source**      | **Examples**                                                       | **Launch consequence**                                                |
| --------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Domestic Need   | Food gap, medicine, salvage, missing tool, route failure           | A shortfall or Project creates urgency and a minimum useful outcome.  |
| Chosen Ambition | New Place, outpost, contact, archive, species route                | The player voluntarily disrupts equilibrium for long-term capability. |
| Promise         | Aid a Guest, revisit a site, return knowledge, mend a relationship | Named relationships or Campaign Memory shape who will go.             |
| World Pressure  | Road work, seasonal window, resource bloom, migration              | Timing changes; waiting may close or worsen the opportunity.          |

<!--@5.2-->
## 5.2 Citizen choice and player authority

<!--@5.2¶1-->
Citizens may volunteer, decline, request preparation, refuse a feared route, insist on accompanying someone, or remain because a Home responsibility cannot be abandoned. These responses express personality and history without creating hidden Home productivity differences. The player selects from the willing and available, but the scene preserves the fiction that Citizens choose to risk themselves because they belong.

<!--@5.3-->
## 5.3 Legible Home subtraction

<!--@5.3¶1-->
Every selected Citizen is removed from their occupied Role and Place. The Launch View previews the exact resulting Capacity / Load / Margin changes. It does not show personal Home aptitude because none exists.

<!--@5.3¶2-->
<table>
<tbody>
<tr class="odd">
<td>EXAMPLE<br />
Taking Sedge removes one Builder share. Builder Margin falls from +1 to 0: the Colony remains maintained but has no spare structural Readiness. Taking Twig as well creates a Gardener shortfall. The player sees the domestic risk before confirming departure.</td>
</tr>
</tbody>
</table>

<!--@5.4-->
## 5.4 Preparation guardrails

<!--@5.4¶1-->
  - No contest status, exact odds, or unrevealed Node content is disclosed at Launch.

<!--@5.4¶2-->
  - Each Citizen receives at most one deliberate Supply choice; standing Tools remain Colony assignments rather than a loadout spreadsheet.

<!--@5.4¶3-->
  - Carry capacity is public at party scale; hidden aptitude numerals remain hidden.

<!--@5.4¶4-->
  - Wounds, descriptive Conditions, fear memories, relationships, species affordances, and known route requirements are visible because they are world facts.

<!--@5.4¶5-->
  - The party faces outward with the Colony visible behind them. The final confirmation hands the game to Away Mode.

<!--@7-->
# 6\. Staging Posts — The Edge Made Legible

<!--@7¶1-->
A Staging Post is improvised and impermanent ground at a Reach edge. It is not a buildable gate, storage building, or progression checkbox. Every Colony and every usable far-side edge has one because every crossing has somewhere animals gather, watch, distribute load, and commit.

<!--@7¶2-->
| **Species** | **Home-side expression**                         | **Far-side expression**               | **RISK emphasis**                                               |
| ----------- | ------------------------------------------------ | ------------------------------------- | --------------------------------------------------------------- |
| Mouse       | Pipe mouth, guardrail base, covered edge run     | Worse cover, improvised debris sleeve | Preserve edge contact; create readable refuges across exposure. |
| Rabbit      | Brush scrape and low launch pocket               | Thin cover, trampled grass pocket     | Hold still, then burst to the next cover commitment.            |
| Squirrel    | Launch branch, post, sign brace, or cable anchor | Lower, shakier, less redundant anchor | Choose a vector and preserve a reachable vertical escape.       |

<!--@7.1-->
## Staging choices are deliberately few

<!--@7.1¶1-->
  - Choose which edge or crossing site to attempt when multiple sides differ in lanes, visibility, elevation, and traffic.

<!--@7.1¶2-->
  - Redistribute one burdensome cargo item or protective Supply.

<!--@7.1¶3-->
  - Read the current traffic pattern and determine whether to wait, proceed, or abandon the crossing.

<!--@7.1¶4-->
  - Set the party’s Crossing posture; then commit. Staging does not become a tactical planning minigame.

<!--@8-->
# 7\. Crossing Register — RISK

<!--@8¶1-->
Crossing is MEDIAN’s immediate bodily danger register. It converts the highway from ecological boundary into lived panic: speed, noise, gaps, fumes, lane width, interrupted sight, and the terrible need to keep moving after commitment.

<!--@8¶2-->
<table>
<tbody>
<tr class="odd">
<td>RISK DEFINITION<br />
Crossing is a brief, real-time or tightly time-stepped sequence in which the party reads traffic windows, commits to transverse movement, and absorbs individual consequences when bodies, load, weather, and timing exceed the available passage.</td>
</tr>
</tbody>
</table>

<!--@7.1#2-->
## 7.1 Crossing is not MEET

<!--@7.1#2¶1-->
RISK has no Approach strip, negotiation round, initiative order, targeting, or tactical positioning grid. Its decisions are spatial and immediate: wait, commit, advance, hold at a refuge, retreat while still possible, protect another Citizen, release cargo, or recover from separation.

<!--@7.2-->
## 7.2 Core Crossing loop

<!--@7.2¶1-->
| **Beat**  | **Player attention**                                                                  | **Possible result**                                                                    |
| --------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Read      | Traffic pulses, lane speeds, vehicle silhouettes, wind, light, refuge positions       | A crossing window becomes intelligible but never perfectly known.                      |
| Commit    | Choose the opening and begin; delay now has a different meaning than delay at Staging | The party enters the road and cannot casually return to planning.                      |
| Traverse  | Move lane to lane or refuge to refuge; keep the party coherent                        | Clean movement, delay, separation, or pressure on the slowest / most burdened Citizen. |
| Intervene | A Citizen may protect another, release cargo, or accept greater personal risk         | Exposure rises around the Citizen who takes responsibility.                            |
| Clear     | Reach the far-side post and account for party, load, Conditions, and time             | The crossing resolves into Field or Homecoming.                                        |

<!--@7.3-->
## 7.3 Consequence ladder

<!--@7.3¶1-->
| **Outcome class**     | **World-state expression**                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| Clean Passage         | Time and cargo preserved; Exposure may still rise slightly under harsh conditions.                         |
| Delayed Passage       | More of the day is spent; later traffic or weather worsens; return margin narrows.                         |
| Scattered / Separated | The party reaches different refuges or sides; regrouping becomes an immediate RISK beat or a bounded MEET. |
| Cargo Loss            | A carried object, food bundle, or Supply is abandoned, scattered, or crushed.                              |
| Shaken / Fear Memory  | A named Condition persists and can affect future volunteering, Crossing posture, or MEET options.          |
| Wound or Maiming      | Physical consequence enters the Citizen record and alters all Registers as the same fact.                  |
| Tharn                 | Acute shutdown interrupts the sequence; rescue or abandonment becomes the only immediate question.         |
| Death                 | Rare, explicit, and visible; never generated by an opaque automatic roll or unattended off-screen state.   |

<!--@7.4-->
## 7.4 Exposure doctrine

<!--@7.4¶1-->
Crossing contributes to personal Exposure but does not use the MEET Exposure procedure. The game derives Crossing Exposure from commitment under pressure: lane time, load, injury, rescue, failed windows, night speed, fumes, and separation. The player sees descriptive state and consequence, not exact hidden numerals.

<!--@7.5-->
## 7.5 Species movement identities

<!--@7.5¶1-->
| **Species** | **Crossing fantasy**                                                                              | **Strength**                                            | **Specific danger**                                                 |
| ----------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------- |
| Mouse       | Make the void readable through edges, debris, shadows, curb lines, pipes, and tiny staged refuges | Low profile, micro-route use, tight cover               | Broad featureless asphalt and lost edge contact.                    |
| Rabbit      | Freeze, then explode across open distance toward immediate concealment                            | Acceleration, cover-to-cover bursts, alarm coordination | A long lane sequence with no safe pause or cover pocket.            |
| Squirrel    | Solve the vector, accelerate linearly, and reach a vertical anchor                                | Direct speed, leap commitment, infrastructure use       | A missing anchor, false landing line, or hesitation in open ground. |

<!--@7.6-->
## 7.6 Return Crossing logic

<!--@7.6¶1-->
The fixed 70/20/10 distribution is retired. Every returning party reaches the far-side Staging Post, and the game evaluates Return Burden from time of day, traffic, route familiarity, load, injury, fear, party cohesion, and weather.

<!--@7.6¶2-->
| **Return Burden** | **Presentation**                                                     | **Design intent**                                                       |
| ----------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Low               | Short cinematic or abbreviated input sequence                        | Relief without pretending the Crossing never existed.                   |
| Moderate          | Compressed Crossing with fewer windows and one decisive intervention | The day’s cost remains legible without full repetition.                 |
| High              | Full manual Crossing from the far-side post                          | The laden, hurt, late, or frightened party must earn the final passage. |

<!--@9-->
# 8\. Field Register — TRAVEL

<!--@9¶1-->
Field Mode carries the party through the road corridor. Its attention is not perpetual discovery; it is reading territory: where things are, which route is possible, what the day permits, what the party carries, and how far sanctuary lies behind or ahead.

<!--@8.1-->
## 8.1 Party representation

<!--@8.1¶1-->
The party travels as one map object so Field remains a route-reading Register rather than a tactical roster game. Individual Citizens remain visible in the party strip because their wounds, Conditions, species affordances, relationships, cargo, and Exposure affect what the party can do.

<!--@8.2-->
## 8.2 Core Field state

<!--@8.2¶1-->
| **State**           | **Function**                                                                                          |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| Route               | Longitudinal path, edge choice, cover line, infrastructure, elevation, and known obstructions.        |
| Time / Light        | Day visibly drains; later conditions alter traffic, weather, predators, visibility, and safe return.  |
| Load                | Cargo affects speed, Crossing burden, available hands, and willingness to press farther.              |
| Weather / Condition | Wind, rain, heat, cold, spume, road work, and sudden acoustic spikes alter travel terms.              |
| Known shelter       | Home, Staging Posts, Held Reaches, natural refuges, and temporary safe stops define achievable range. |
| Party condition     | Wounds, fear, Exposure, cohesion, hunger, separation, and who is carrying what.                       |
| Node knowledge      | Unknown, sighted, studied, depleted, renewable, contested, claimed, marked, or transformed.           |

<!--@8.3-->
## 8.3 Route texture

<!--@8.3¶1-->
The road-edge route is richer and more interrupted; the wall-edge route is quieter and slower. Terrain changes the price and consequence of actions without becoming a positional combat grid. A route is not “best” in the abstract; it is the kind of day the party chooses.

<!--@8.4-->
## 8.4 Home Reach traversal

<!--@8.4¶1-->
After Launch, TRAVEL may begin on the Home Reach as the party walks toward a chosen edge. This is already Away Mode because the party—not the Colony—is the crunch subject. Early campaigns may still meet local contest or opportunity; mature Home ground should increasingly become a quiet, familiar departure walk.

<!--@8.5-->
## 8.5 Turn-back authority

<!--@8.5¶1-->
The player may choose to return whenever the party can still plausibly reach a safe stop. The game should continuously communicate the cost of one more Node, one more Reach, or one more attempt. Withdrawal preserves future lives and is not automatically graded as failure.

<!--@10-->
# 9\. Nodes — Places Before They Become Situations

<!--@10¶1-->
A Node is a meaningful place anchored in Field geography. Passing a known Node remains TRAVEL. Entering it, working it, claiming it, studying it, or confronting what occupies it opens MEET.

<!--@9.1-->
## 9.1 Node families

<!--@9.1¶1-->
| **Family** | **Examples**                                                                | **Primary value**                                                 |
| ---------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Resource   | Wildflower field, seed trap, bramble patch, water, insect bloom             | Food, medicine, fiber, seasonal sustenance.                       |
| Salvage    | Toolbox, vehicle cavity, litter catch, drain grate, construction debris     | Scrap, artifacts, equipment, material transformation.             |
| Shelter    | Pipe, root pocket, tree hollow, culvert ledge, abandoned nest               | Rest, weather protection, temporary care, route extension.        |
| Social     | Guest camp, rat claim, broker, neighboring colony, meeting landmark         | Relationship, recruitment, promise, information, access.          |
| Route      | Bridge anchor, guardrail gap, sign support, drainage path, service crossing | New travel option, shorter leg, safer Crossing, outpost location. |
| Hazard     | Flooded drain, poisoned runoff, hawk line, mowing zone, road-work cut       | Avoidance, warning, repair, sacrifice, changed map state.         |
| Memory     | Lost home remnant, memorial object, old scent line, former colony trace     | Tales, identity, knowledge, Circle work, later EMBODY resonance.  |

<!--@9.2-->
## 9.2 Uncontested Node grammar

<!--@9.2¶1-->
An uncontested Node contains no Presence that must be overcome, bypassed, bought off, or yielded to. It still opens a brief MEET because the party is choosing its relationship to a specific place.

<!--@9.2¶2-->
| **Option**        | **Meaning**                                               | **Constraint**                                                                |
| ----------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| TAKE              | Gather or salvage now                                     | Carry is finite; taking may reduce renewal or leave less for later.           |
| STUDY             | Learn condition, season, yield, route, or hidden property | Consumes time and may expose the party without immediate material gain.       |
| MARK FOR RETURN   | Create scent, sign, route memory, or map knowledge        | Preserves opportunity but leaves it vulnerable to change or another claimant. |
| LEAVE UNDISTURBED | Take nothing and preserve the Node’s current ecology      | Always available; can be husbandry, restraint, or simply the right decision.  |

<!--@9.3-->
## 9.3 Contested Node test

<!--@9.3¶1-->
A Node is contested when a Presence—animal or environmental—must be overcome, got around, bought off, endured, or left. Contest status is normally revealed on arrival, not at Launch. A familiar or Held Node may become uncontested through prior relationship, investment, season, or changed world state.

<!--@9.4-->
## 9.4 Renewable-place doctrine

<!--@9.4¶1-->
Nodes are not factories. They have condition, season, memory, and recovery. A stripped field, repeatedly disturbed cache, or careless salvage site changes. The Colony’s relationship with the corridor is ecological and historical, not only extractive.

<!--@11-->
# 10\. Away MEET — The Consequence Register

<!--@11¶1-->
MEET is the shared Register for bounded consequential situations. In Away Mode, it stages the exact party and allows individual capability, equipment, history, and Exposure to matter. Its grammar differs from Home MEET because its crunch subject differs.

<!--@10.1-->
## 10.1 Contested Approach strip

<!--@10.1¶1-->
|                                             |
| ------------------------------------------- |
| CONTEST • EVADE • PARLEY • YIELD • WITHDRAW |

<!--@10.1¶2-->
The five Approaches remain the provisional taxonomy of contested Away MEET. They are always shown in canonical order and greyed rather than hidden when unavailable. Each carries a short situation-specific line that describes what the action means here without revealing exact odds.

<!--@10.1¶3-->
| **Approach** | **Core relation**                                                       | **Availability rule**                                                                                                     |
| ------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Contest      | Overcome, resist, hold, break, seize, or endure directly                | May be grey when the Presence cannot be fought or held.                                                                   |
| Evade        | Slip past, flee, hide, distract, or use terrain to avoid the Presence   | May be grey when the Presence occupies the desired object and cannot be bypassed.                                         |
| Parley       | Trade, ask, bargain, deceive, persuade, or invoke relationship          | May be grey for weather, machinery, or beings that will not speak.                                                        |
| Yield        | Give ground, cargo, claim, time, or priority to preserve something else | Never removed; makes sacrifice visible.                                                                                   |
| Withdraw     | Leave the Node or situation without pursuing its objective              | Never removed unless the situation has physically closed escape, in which case the Encounter must explicitly explain why. |

<!--@10.2-->
## 10.2 Group result and personal consequence

<!--@10.2¶1-->
The party resolves the shared objective as one body: obtain, escape, persuade, protect, pass, or survive. Individual fate resolves afterward around the Citizens who accepted responsibility, pressed the situation, protected another, carried the critical object, or were already vulnerable. Group success does not immunize individuals; individual harm does not automatically erase group success.

<!--@10.3-->
## 10.3 Encounter rounds and Turns

<!--@10.3¶1-->
A contested Away MEET lasts one to four rounds. The entry Approach establishes the first group result. A clean resolution closes the scene. A costly, partial, or opposed result opens a Turn: a concrete immediate problem produced by the fiction rather than a second universal menu.

<!--@10.3¶2-->
| **Turn type** | **Example**                                                    | **Function**                                                                     |
| ------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Protect       | The hawk turns toward the kit carrier                          | Choose who accepts Exposure to shield another.                                   |
| Recover       | The medicine bundle falls beneath the guardrail                | Decide whether the objective is worth a new risk.                                |
| Rescue        | A Citizen goes tharn or becomes separated                      | Choose who can go back, or Withdraw and accept the cost.                         |
| Press         | The party can force a better group result by staying in danger | A named Citizen deliberately raises personal Exposure.                           |
| Reframe       | New information changes which Approaches remain lit            | A Guest, tool, relationship, or discovered weakness opens or closes possibility. |

<!--@10.4-->
## 10.4 Tharn interrupt

<!--@10.4¶1-->
Tharn is an acute break, not a high damage bar. When a Citizen goes tharn, the scene briefly narrows to that Citizen—sound, breath, pulse, fixation—and returns with changed options. The next Turn is forced toward rescue, protection, withdrawal, or deliberate abandonment. Tharn cannot be cleared by EMBODY; only safety, care, and time can resolve it.

<!--@10.5-->
## 10.5 No tactical positioning

<!--@10.5¶1-->
Scene terrain may alter the terms of an Approach, but the player does not place Citizens into cover squares, assign facing, choose initiative, or target individual enemies. The party remains one body on the front end; individuality appears through choice, Exposure, and consequence on the back end.

<!--@12-->
# 11\. Personal Exposure and Citizen Growth

<!--@12¶1-->
Exposure is the Away economy of possibility. It records how far a Citizen has placed themselves beyond ordinary safety—not as a visible numeric stat, but as an internally tracked pressure expressed through descriptive state, named Conditions, history, and altered outcome tails.

<!--@11.1-->
## 11.1 Sources of Exposure

<!--@11.1¶1-->
| **Register** | **Exposure sources**                                                                                                                         |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| TRAVEL       | Prolonged absence, harsh weather, night movement, hunger, cold, carrying beyond comfort, wild ground, isolation, failed rest.                |
| RISK         | Lane time, missed windows, rescue, separation, load, fumes, injury, panic, committing from a poor Staging Post.                              |
| MEET         | Contest, Press, protecting another, carrying the objective, refusing retreat, being specifically targeted, staying through additional Turns. |

<!--@11.2-->
## 11.2 Display doctrine

<!--@11.2¶1-->
  - No Health numerals, Spirit bars, aptitude pips, or exact Exposure percentages.

<!--@11.2¶2-->
  - Citizen state appears through descriptive bands, posture, voice, animation, named Conditions, and consequence previews.

<!--@11.2¶3-->
  - Public group facts—carry, supplies, time, distance, party size—may use numbers where clarity requires them.

<!--@11.2¶4-->
  - Exact odds remain hidden; availability and stakes are shown.

<!--@11.3-->
## 11.3 Growth and harm

<!--@11.3¶1-->
Away Mode is where Citizens grow because it is where their particular capabilities and choices are resolved. High Exposure widens both tails. A Citizen may earn a Distinction, deepen a relationship, gain route confidence, acquire a Keepsake, or receive an After-name; the same commitment can produce fear memory, wound, Maiming, Tharn, or death. These are not symmetrical reward tables but authored and derived consequences of what actually occurred.

<!--@11.4-->
## 11.4 Exposure ebb

<!--@11.4¶1-->
Exposure begins to ebb when the Citizen returns to credible sanctuary. Dwell, food, shelter, care, familiar company, and time provide the conditions. EMBODY may portray that ebb only after Quiet Equilibrium; it neither accelerates recovery nor cures acute Tharn.

<!--@13-->
# 12\. Field Cards — What Comes to the Party

<!--@13¶1-->
Field cards are occasional interruptions that find the party between Nodes. They open MEET only when the threshold of consequential attention is met. They should remain sparse enough that the corridor is primarily a place the player reads rather than a deck the player endures.

<!--@13¶2-->
| **Card family** | **Function**                                                     | **Example**                                            |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------------ |
| Opportunity     | Risk and reward arrive in the same object and can be declined    | Fresh litter spill, exposed fruit, open service gate.  |
| Condition       | The terms of travel change without a social counterpart          | Spume turns, rain begins, fumes settle, wind rises.    |
| Ambush          | A Presence arrives without being chosen                          | Hawk pass, snake at the edge, sudden machinery onset.  |
| Arrival         | A stranger, messenger, or displaced animal appears between Nodes | Wanderer, warning bearer, lost kit, neighboring scout. |

<!--@13.1-->
## Cadence guardrail

<!--@13.1¶1-->
A typical short expedition should not average several full cards. Known Nodes provide most intentional content; cards punctuate route choice and keep the world active. “Nodes are the meal; cards are the weather” remains the authoring rule.

<!--@13.2-->
## Terrain doctrine

<!--@13.2¶1-->
The card carries the current route terrain and modifies price or consequence, not the menu through tactical positioning. A hawk in open grass is worse than the same hawk at a bramble line; the player chose the route, not a combat square.

<!--@14-->
# 13\. Range, Held Reaches, and Stopovers

<!--@14¶1-->
The older outpost work contains a useful Away principle: range is created by places where a day can safely end. v0.5 narrows those places so they support refuge without becoming alternate Colonies.

<!--@14¶2-->
<table>
<tbody>
<tr class="odd">
<td>OUTPOST RULING<br />
A Held Reach is an Away refuge, not partial Home Mode. It may support Stopover, Rest, low-level Care, Watch, and Storage. It does not support full DWELL, species placement grammar, Nursery, Circle, Quiet Equilibrium, or EMBODY.</td>
</tr>
</tbody>
</table>

<!--@13.1#2-->
## 13.1 Core functions

<!--@13.1#2¶1-->
| **Function**  | **Meaning**                                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| End the day   | Without safe rest, the party must complete the outward and return leg before conditions close.             |
| Mend the hurt | Low-level Care may prevent a forced march home, but serious conditions still require the Colony.           |
| Hold the load | Cargo may be cached and collected later, turning the corridor into a relay rather than a teleport network. |
| Warn          | A stationed Citizen or Guest can telegraph local conditions and send word to Home.                         |

<!--@13.2#2-->
## 13.2 Range doctrine

<!--@13.2#2¶1-->
A party’s reach is determined by travel pace, daylight, load, known refuge, and the chain of safe stops—not by an arbitrary locked-zone gate. Held ground becomes faster because it is known, watched, and less contested. The player builds their own felt fast travel by making the corridor survivable.

<!--@13.3-->
## 13.3 Off-screen protection

<!--@13.3¶1-->
Named stationed Citizens cannot be killed or Maimed off-screen. A serious outpost incident sends a message or opens a waiting situation that requires a future expedition. Minor inconvenience, changed stores, warning failure, or maintenance need may be reported without irreversible personal loss.

<!--@13.4-->
## 13.4 Maintenance without entropy treadmill

<!--@13.4¶1-->
Outposts do not silently decay into nothing. Environmental pressure creates visible Maintenance Need or degraded readiness; neglect may strip conveniences and make the Reach harder, but the claim and basic refuge persist until the player deliberately abandons them or an on-screen MEET decides otherwise.

<!--@15-->
# 14\. Return — The Haul Is Carried Home

<!--@15¶1-->
Return begins when the player turns the party toward a safe destination. It is not a victory transition. The party is now changed by what it found, carried, promised, lost, and suffered; those facts make the route home materially different from the route out.

<!--@14.1-->
## 14.1 Longitudinal return is played

<!--@14.1¶1-->
The party travels Reach by Reach through whatever ground remains wild or held. Familiar and fully safe legs may compress, but unresolved distance is not skipped merely because the objective was achieved. The return journey is where carry, injury, weather, and time become burden.

<!--@14.2-->
## 14.2 Return pressure

<!--@14.2¶1-->
| **Pressure**       | **Effect**                                                                                            |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| Load               | Slower travel, fewer free hands, harsher Crossing burden, more difficult rescue or Evade.             |
| Injury / Condition | Reduced route tolerance, need for shelter, altered volunteering and intervention choices.             |
| Time of day        | Evening rush, night speed, fumes, visibility, predator change, and rising Tharn risk.                 |
| Promises / Guests  | The party may be responsible for someone who does not know the route or cannot move at the same pace. |
| Depleted Supplies  | Fewer ways to protect cargo, treat wounds, or absorb a Field condition.                               |
| Changed route      | Flood, road work, blocked culvert, predator activity, or a Node no longer behaving as expected.       |

<!--@14.3-->
## 14.3 No generic expedition grade

<!--@14.3¶1-->
Legendary / Successful / Hard-Earned / Failed ratings remain deprecated. The return is summarized through derived facts: what was sought, what returned, what it cost, who changed, which Promise remains, and what the Colony can now do. The Chronicle records history rather than awarding a score.

<!--@16-->
# 15\. Homecoming — The Inward Bracket

<!--@16¶1-->
Homecoming is the MEET View that transfers the expedition’s individual facts back into the Colony. It fires after every expedition, but remains cheap and warm by default. A clean return may take seconds; a difficult return expands because care, placement, Guests, absence, or changed capability genuinely require attention.

<!--@16¶2-->
<table>
<tbody>
<tr class="odd">
<td>EMOTIONAL ORDER<br />
recognition → relief → assessment → care → allocation → remembrance</td>
</tr>
</tbody>
</table>

<!--@15.1-->
## 15.1 Homecoming procedure

<!--@15.1¶1-->
1.  Recognition: show who returned, who did not, and the formation’s visible change. The Colony faces inward toward them.

<!--@15.1¶2-->
2.  Assessment: account for wounds, Conditions, Exposure, Tharn, cargo damage, missing Supplies, and immediate needs.

<!--@15.1¶3-->
3.  Care: decide where injured or exhausted Citizens go and which Home Role shares are unavailable at the next Dawn.

<!--@15.1¶4-->
4.  Allocation: place food, salvage, medicine, tools, artifacts, and cached knowledge into Colony stores, Projects, or specific Places.

<!--@15.1¶5-->
5.  Guests and relationships: receive, house, defer, or refuse a Guest; record Promises and changed social facts.

<!--@15.1¶6-->
6.  Knowledge: update routes, Nodes, hazards, warnings, and maps; do not treat knowledge as generic research points.

<!--@15.1¶7-->
7.  Posture restoration: return available Citizens to Roles, recalculate Capacity / Load / Margin, and reveal whether Home is Crisis, Strained, Quiet, or Flourishing.

<!--@15.1¶8-->
8.  Memory seed: preserve a concise derived account when the event matters. Full interpretation may continue later through Teaching, Campaign Memory, or EMBODY.

<!--@15.2-->
## 15.2 Homecoming is not a test

<!--@15.2¶1-->
The player does not roll to deserve the return. Homecoming asks how the Colony receives reality. It cannot retroactively erase expedition consequence, but it can determine whether that consequence becomes cared for, integrated, isolated, wasted, misunderstood, or transformed into future capability.

<!--@15.3-->
## 15.3 Mode shift

<!--@15.3¶1-->
The game returns to Home Mode only when Homecoming is complete and Colony posture is legible. A hard return may reopen DWELL in Strained or Crisis state. EMBODY remains unavailable until Quiet Equilibrium is genuinely restored.

<!--@17-->
# 16\. The Off-Screen Colony Contract

<!--@17¶1-->
|                                                        |
| ------------------------------------------------------ |
| MEDIAN NEVER TAKES A NAMED ANIMAL FROM YOU OFF-SCREEN. |

<!--@17¶2-->
This contract is essential because the game requires departure for growth. A Home that inflicts irreversible personal loss while the player is Away teaches the player not to leave and turns sanctuary into another exposure zone.

<!--@17¶3-->
| **While attention is Away, Home may…**                                                             | **Home may not…**                                                                              |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Advance Projects according to present Citizen-Days.                                                | Kill, Maim, or permanently remove a named Citizen or Guest.                                    |
| Resolve routine matters through existing Capacity and Readiness.                                   | Apply a hidden personal aptitude modifier to decide who “did better.”                          |
| Gain warm or neutral developments: arrival, birth, recovery, found object, ordinary improvisation. | Suffer catastrophic structural loss without an on-screen consequential choice.                 |
| Suffer inconvenience: slower Project, spoiled Perishables, depleted readiness, opened shortfall.   | Create an irreversible outcome solely because the player was attending the required Away loop. |
| Open a waiting Colony situation whose cost or urgency may increase.                                | Resolve that waiting situation against named lives before the player returns.                  |

<!--@17.1-->
## v0.5 correction

<!--@17.1¶1-->
The remaining Colony fares according to Role headcount, Places, topology, Conditions, and Readiness. A named Citizen may be credited in the fiction—“Sedge moved the nursery before the water rose”—but Sedge contributed one Home share, not a hidden superior Builder coefficient.

<!--@18-->
# 17\. Species Identity Across Away Mode

<!--@18¶1-->
JOIN, GATHER, and CONNECT are Home placement identities, but the ecology beneath them should remain bodily legible Away. Species modify available routes, Staging interpretation, movement fantasy, and the situations that feel natural; they do not require three unrelated expedition games.

<!--@18¶2-->
| **Layer**         | **Mouse**                                                                 | **Rabbit**                                                                     | **Squirrel**                                                                            |
| ----------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| TRAVEL            | Reads bases, edges, debris, pipes, leaf litter, and covered micro-routes. | Reads cover distance, brush pockets, sightlines, and burst intervals.          | Reads anchors, vertical escape, overhead lines, branch continuity, and landing vectors. |
| RISK              | Needs the open road made legible by edge or refuge.                       | Freezes, then commits to explosive cover-to-cover movement.                    | Accelerates directly toward a known vertical anchor.                                    |
| NODE preference   | Small cavities, seed traps, drainage, human-object interiors.             | Forage near refuge, brush courts, surface shelter, shared warning.             | Elevated salvage, distributed caches, route anchors, alternate refuges.                 |
| MEET contribution | Infiltration, noticing, small access, concealment, micro-carry solutions. | Warning, acceleration, group alarm, cover knowledge, endurance in open ground. | Route knowledge, vertical access, long reach, cache memory, rapid line commitment.      |
| Specific fear     | Losing edge contact and certainty of being found.                         | Being trapped beyond immediate concealment.                                    | A route ending without another reachable way home.                                      |

<!--@18.1-->
## Mixed parties and Guests

<!--@18.1¶1-->
A Guest does not add a sixth Approach or a generic stat bonus. Guests light existing options, reinterpret terrain, open routes, or make a consequence bearable. Species difference should appear as new possibility inside shared systems.

<!--@19-->
# 18\. Information Architecture and Player Legibility

<!--@19¶1-->
| **View**   | **Must show**                                                                                                | **Must not show**                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| Launch     | Purpose, willing Citizens, Home share removed, resulting margins, one Supply choice, known route constraints | Unrevealed contest, exact odds, hidden aptitude numbers, full inventory optimization. |
| TRAVEL     | Party, route, time/light, load, weather, shelter, known Nodes, descriptive Citizen Conditions                | Tactical spacing, constant event countdowns, invisible return cost.                   |
| RISK       | Lane flow, readable windows, refuges, party cohesion, load burden, immediate descriptive danger              | Approach strip, turn order, enemy health, exact Exposure meter.                       |
| Away MEET  | Fixed scene, exact party, Presence or Node, stakes, lit/grey Approaches, cargo, relevant Conditions          | Positioning grid, initiative, targeting, likelihood labels, Spirit bar.               |
| Homecoming | Who returned, wounds/Conditions, cargo, Guests, knowledge, receiving Places, Role availability, new margins  | Expedition score, celebratory grade, automatic invisible absorption.                  |

<!--@19.1-->
## Advisor voice

<!--@19.1¶1-->
Named Citizen advice remains valuable when the situation makes that Citizen relevant. Advice frames the threatened value or remembered route; it does not reveal hidden odds. The same animal may speak at Launch, in MEET, or at Homecoming because one world fact persists across Registers.

<!--@19.2-->
## Numerical doctrine

<!--@19.2¶1-->
Use figures for public colony and party quantities—Role Capacity, Load, carry, Citizen-Days, stores, route distance, time. Use descriptive bands and named Conditions for personal health, fear, Exposure, and aptitude. No Spirit stat is introduced.

<!--@20-->
# 19\. Balancing Safeguards and Anti-Spiral Rules

<!--@20¶1-->
**Departure cannot be mandatory suicide.** The Launch preview must make Home subtraction and route burden legible enough for an informed decision.

<!--@20¶2-->
**Away content must not erase Home success.** Most expeditions should return something useful, clarifying, or relationship-bearing even when the original objective is not achieved.

<!--@20¶3-->
**Cards remain sparse.** Field remains readable territory; authored Nodes carry most intentional content.

<!--@20¶4-->
**Crossing remains short.** Difficulty should deepen through pressure, route, load, and consequence—not through a long sequence of twitch obstacles.

<!--@20¶5-->
**Withdrawal remains viable.** Yield and Withdraw prevent the game from turning every MEET into all-or-nothing heroics.

<!--@20¶6-->
**Exposure cannot be charged three times.** One risky choice should not automatically add Exposure, wound, lost cargo, and a second compulsory penalty unless the fiction and severity justify it.

<!--@20¶7-->
**Homecoming scales with actual consequence.** Clean return is brief; difficult return earns time. Ceremony is not mandatory after routine forage.

<!--@20¶8-->
**Safe ground compresses.** Known and held routes become faster in felt time so corridor growth does not create repetition.

<!--@20¶9-->
**Outposts are refuge, not maintenance traps.** They may become less capable, but they do not silently vanish into entropy.

<!--@20¶10-->
**No off-screen irreversible personal loss.** Waiting crises may become costlier, not retrospectively fatal.

<!--@21-->
# 20\. Supersession Ledger

<!--@21¶1-->
| **Older decision**                    | **v0.5 status**                             | **Revised canon**                                                                              |
| ------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| V7-3 INTERACT                         | Superseded                                  | MEET is restored and broadened.                                                                |
| V7-23 Exposure only in contested MEET | Superseded                                  | Exposure may accumulate through all Away Registers.                                            |
| V7-27 four-Register Twin Modes        | Superseded in count, preserved in structure | Five Registers: DWELL and EMBODY Home; TRAVEL and RISK Away; MEET cross-modal.                 |
| V7-28 two Encounter grammars          | Preserved and narrowed                      | Contested / uncontested remain Away MEET grammars; Home MEET has its own Colony-scale grammar. |
| V7-29 fixed five                      | Preserved for contested Away MEET           | Always ordered, grey not hide, exits visible.                                                  |
| V7-30 Staging Post                    | Preserved                                   | Improvised threshold ground, never a structure gate.                                           |
| V7-31 Launch → Home Field → Crossing  | Revised                                     | Launch switches to Away; Home Reach traversal is TRAVEL under individual party focus.          |
| V7-33 no off-screen named loss        | Preserved and promoted                      | Core attachment-first contract.                                                                |
| V7-34 experienced Home workers        | Superseded in aptitude                      | Remaining headcount and Readiness decide; names supply voice and history.                      |
| V7-36 Crossing has no Exposure        | Superseded                                  | RISK can produce personal Exposure and consequence without MEET procedure.                     |
| V7-37 Held Reach partial Home         | Superseded                                  | Held Reach is Away refuge with Stopover, not full Home state.                                  |
| V7-38 safe stop returns focus Home    | Revised                                     | Focus may cut away, but the party remains Away; no Quiet Equilibrium or EMBODY at outpost.     |
| V7-40 longitudinal return played      | Preserved                                   | The haul is carried home.                                                                      |
| 70/20/10 crossing distribution        | Superseded                                  | Return Burden decides cinematic, compressed, or full RISK.                                     |
| Expedition Ratings                    | Deprecated                                  | Derived Chronicle facts replace grades.                                                        |

<!--@22-->
# 21\. Open Design Questions for the Structured v0.5 Revision

<!--@22¶1-->
This pass establishes architecture but leaves several tuning and implementation questions deliberately open.

<!--@22¶2-->
| **Question**                     | **Current working position**                                                                        | **Prototype required**                                                  |
| -------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Exact Crossing control model     | Lane-and-window movement with few verbs and species-specific motion; no tactical grid               | One outbound and one high-burden return Crossing for each Core Species. |
| Exposure bands and hidden math   | Descriptive display, shared underlying state across TRAVEL / RISK / MEET                            | A full expedition record from departure to recovery.                    |
| Turn authoring in Away MEET      | Entry Approach, then fiction-specific Protect / Recover / Rescue / Press / Reframe Turns            | One Encounter drawn in Approach, Turn, Tharn, and aftermath states.     |
| Party size and body-unit scaling | Party remains one Field object; individual strip scales by species body-unit rules                  | Mouse, Rabbit, and Squirrel parties at minimum and maximum size.        |
| Return Burden thresholds         | Objective conditions replace fixed percentages                                                      | Compare clean forage, late laden return, and wounded Guest escort.      |
| Field-card cadence               | Sparse; Nodes dominate                                                                              | Ten-day campaign telemetry and late-game held-route comparison.         |
| Outpost scope                    | Stopover, Rest, Care, Watch, Store only                                                             | One multi-leg Special Journey with two Held Reaches.                    |
| Home Reach Field content         | Early contest may taper to quiet familiarity                                                        | Tier I and Tier III outbound walks on the same map.                     |
| Distinction / After-name scope   | Away growth remains primary; high-risk Home MEET may still create history under separate Home rules | Philosophical decision in core progression specification.               |
| Corridor tuning                  | Two Reaches per day remains a provisional working figure                                            | Ancestral-home and Metropolis journey pacing tests.                     |

<!--@23-->
# 22\. Canon Rules, Non-Goals, and Acceptance Tests

<!--@22.1-->
## 22.1 Canon rules

<!--@22.1¶1-->
  - Launch changes the game to Away Mode and visibly subtracts exact named Home shares.

<!--@22.1¶2-->
  - TRAVEL carries a party through extended territory; RISK handles highway-scale immediate danger; MEET stages bounded consequential situations.

<!--@22.1¶3-->
  - Crossing may create personal Exposure and consequence but never uses the Away MEET Approach strip.

<!--@22.1¶4-->
  - Contested Away MEET uses Contest, Evade, Parley, Yield, Withdraw in fixed order; uncontested Node MEET uses Take, Study, Mark for Return, Leave Undisturbed.

<!--@22.1¶5-->
  - The party is one map object in Field and one group subject at the front of MEET; individual consequence resolves afterward.

<!--@22.1¶6-->
  - Exact personal numerals and Spirit are refused.

<!--@22.1¶7-->
  - Return travel is carried, not teleported; return Crossing scales from cinematic to full RISK according to burden.

<!--@22.1¶8-->
  - Homecoming fires after every expedition, scales with what returned, and performs care, allocation, knowledge, Guest, and Role reintegration.

<!--@22.1¶9-->
  - The Colony cannot irreversibly lose a named life off-screen while the player is Away.

<!--@22.1¶10-->
  - EMBODY never appears Away and becomes available only after Homecoming and restored Quiet Equilibrium.

<!--@22.2-->
## 22.2 Non-goals

<!--@22.2¶1-->
  - A hero-RPG mission layer detached from Colony needs and domestic opportunity cost.

<!--@22.2¶2-->
  - A launch spreadsheet comparing hidden success percentages and “best” Citizens.

<!--@22.2¶3-->
  - A full action game inside Crossing, or a tactical combat grid inside MEET.

<!--@22.2¶4-->
  - A constant stream of random cards replacing place-based Field traversal.

<!--@22.2¶5-->
  - Resource Nodes functioning as infinite extraction factories.

<!--@22.2¶6-->
  - An expedition grade, loot rarity ladder, or victory score standing in for history.

<!--@22.2¶7-->
  - Automatic return teleportation after the objective is reached.

<!--@22.2¶8-->
  - Outposts becoming second Colonies, EMBODY locations, or passive resource engines.

<!--@22.2¶9-->
  - Off-screen catastrophe used to force the player to hurry home.

<!--@22.2¶10-->
  - Care, recovery, and attachment reduced to optimal buff processing.

<!--@22.3-->
## 22.3 Acceptance tests

<!--@22.3¶1-->
| **Test**              | **Passing condition**                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Legible subtraction   | Before Launch, the player can name exactly which Home shares leave and how current margins change.                                             |
| No Home aptitude leak | Swapping two healthy willing Citizens in the same Home Role changes no Capacity preview, though Away capability may differ.                    |
| Register distinction  | TRAVEL, RISK, and MEET ask visibly different questions and cannot be mistaken for three skins on one system.                                   |
| Crossing consequence  | A Crossing can alter individual Exposure, cargo, fear, wound, or time without opening an Approach strip.                                       |
| Field readability     | A typical expedition contains long enough stretches of route reading that Nodes remain the meal and cards remain the weather.                  |
| Node ethics           | An uncontested Node can be taken, studied, marked, or preserved, with real future consequences.                                                |
| Away individuality    | Two parties with equal headcount but different Citizens, gear, wounds, relationships, and species affordances behave meaningfully differently. |
| Withdrawal dignity    | Turning back or yielding can preserve Citizens and future possibility without being automatically framed as failure.                           |
| Carried return        | A heavy or wounded party experiences a materially different return from its outbound journey.                                                  |
| Homecoming conversion | Every important Away fact becomes a visible Home fact: Role availability, care need, stores, Place use, Guest, route knowledge, or memory.     |
| Home protection       | A named Citizen cannot die or be Maimed off-screen because the player followed the required Away loop.                                         |
| EMBODY boundary       | A calm Margin or outpost cannot invoke EMBODY; returned Citizens gain access only after the Colony again reaches Quiet Equilibrium.            |

<!--@24-->
# Final System Statement

<!--@24¶1-->
|                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Away Loop succeeds when leaving Home is a legible sacrifice, the highway is a distinct bodily terror, the corridor is a readable ecology, particular Citizens accumulate consequence, and everything found or suffered must be carried back into the Colony that made the journey worth taking. |

<!--@24¶2-->
In v0.5, Home and Away are no longer unequal halves. Dwell establishes the credible sanctuary and collective posture that make departure meaningful. Away makes individual friends answer for distance, risk, and opportunity. Homecoming joins the scales again. Quiet Equilibrium and EMBODY then reveal what their courage preserved.
