# MEDIAN v0.5.0 Game Design Document

## Provisional First Draft

**Status:** Provisionally complete first draft. The seven-Part MEDIAN v0.5.0
GDD has been developed through direct authorial review. Its current status and
next bounded revision are recorded in canonical compile state and derived
`STATUS.md`.

This document is the sole active provisional first draft of the MEDIAN v0.5.0
Game Design Document. It establishes the coherent conceptual design of a
theoretical game and the reader-facing order of its concept book. Final canon,
compiled prose, editorial refinement, and later conceptual tuning remain
separate authorial concerns.

## Front Matter

- Title page
- Brief reader note
- Contents

# 0. THE FOUNDING ESCAPE

The GDD opens in the exhausted founding party's flight through Reach 4, then
returns to the last calm hours of the ancestral Colony. The Founding Escape is
told here as an uninterrupted literary narrative, following animal-scale
experience from Home's destruction through the Crossings to the discovery of
promising ground in Reach 5. It ends when the party chooses to make Home there.

Chapter 6.2 specifies the player control, Registers, RISK, transitions, and
persistent state enacted by this narrative.

# PART I — WHAT MEDIAN IS: SANCTUARY AND EXPOSURE

## 1.1 A Civilization Where Nobody Else Would Call Home

### The game in one breath

- Animal-colony base-building on active highway median strips
- One permanent Home
- A small population of named Citizens
- Expeditions undertaken for material, civic, relational, and personal reasons
- Consequences carried back into the Colony

### The central dramatic promise

- Sanctuary → Exposure → Consequence → Return → Memory
- Home as the condition that makes departure and return meaningful

### What the player does

- Build and tend a Colony
- Understand its needs and ordinary life
- Prepare and send particular Citizens Away
- Cross, travel, meet, choose, and endure
- Return with materials, relationships, injuries, obligations, and memories
- Inhabit the changed Home again

### Creative lineage

- *Watership Down* — emotional and dramaturgical foundation
- *Age of Empires* — legible civic growth and the transformation of a settlement
- *Mouse Guard* — animal-scale material and visual imagination
- A lifetime spent looking at highway median strips through car and bus windows,
  imagining the overlooked land between roads as inhabited territory
- A compact boundary between influence and borrowed fiction or wholesale
  mechanics

### Creative boundaries

- Colony stewardship, attachment, and consequence leading play
- Road Crossings treated as brief animal-scale bodily thresholds
- Every Citizen remaining named and historically continuous
- Animal bodies and ecology shaping material culture
- Territorial exploration returning meaning to the permanent founding Home
- Sentiment arising through credible Game Logic

## 1.2 The attachment-forward base builder

`Philosophy.Pillar.AttachmentForward`

### What attachment means

Attachment begins when imagined people, places, objects, and histories acquire
durable emotional reality. A work can invite it through legibility, contact,
care, identity, shared history, credible danger, and return, while leaving the
player free to decide what matters rather than demanding or declaring
attachment on their behalf.

The human propensity to form such attachments appears in long-lived fandoms
around worlds such as Middle-earth and *Star Trek*, remembered Pokémon
companions, and personally built *Animal Crossing* towns. These examples
demonstrate attachment behavior; they are not additional creative influences on
MEDIAN.

Attachment-forward design asks what a game enables the player to know, value,
remember, and find worthy of protection. It points the whole design toward
particularity: a Citizen becomes known, a settlement becomes historically
specific, and a Place or object acquires meaning through what happened there
and who was present.

MEDIAN treats Home as an inhabited social protagonist. Production, survival,
construction, and exploration serve one continuing Colony rather than
consuming or replacing it. Its four anchors of attachment are **Home, Citizen,
Place or object, and Memory**.

> **Legibility → competence → stability → attention → attachment**

A comprehensible Colony permits competent stewardship. Competence can produce
Quiet Equilibrium, releasing attention toward ordinary life and EMBODY. That
attachment then gives weight to departure, Exposure, consequence, Homecoming,
and the changed life that returns.

Cozy and attachment-forward describe different dimensions. Cozy is an
experiential condition; attachment-forward is a design direction. MEDIAN's
quiet belongs to particular lives and follows credible Game Logic.

> **MEDIAN earns its cozy.**

Appendix I gives the complete attachment-forward philosophy, its general
manifestations across systems and media, its relationship to cozy experience,
and its design protections and acceptance test.

## 1.3 Global pillars and governing doctrines

The first seven sections are player-facing pillars. The final two are governing
design doctrines that protect those pillars across the whole design.

### One permanent, attachment-forward Home

- Home as the permanent emotional and mechanical center
- Improvement, inhabitation, damage, repair, and memory without replacement
- Corridor growth accumulating around the founding Home rather than making it
  obsolete

### Every Citizen is known

- Every Citizen named, distinguishable, and historically continuous
- Population remaining small enough for every name to count
- Core and Guest origins sharing equal personhood and Citizenship

### Home can become enough

- Successful stillness as a valid state of play
- Growth supporting ordinary life rather than perpetuating itself
- Quiet made mechanically credible
- Peaceful continuation through care, craft, relationship, hospitality, memory,
  and chosen exploration
- No required expansion, domination, or terminal victory state

### Home grows the Colony; Away changes Citizens; Return changes both

- Home developing collective capability and continuity
- Away developing and endangering particular Citizens
- Return making collective and personal change answer one another
- These as centers of attention rather than exclusive jurisdictions

### Consequence and continuity

- Danger changing lives before erasing them
- Harm, Maiming, Distinctions, relationships, and memory carrying consequence
  Home
- Death remaining possible without becoming routine inventory loss

### One persistent world across two Modes and five Registers

- Colony, Embodiment, Field, Crossing, and Encounter acting upon one world
- Facts and consequences remaining continuous across Registers
- Transitions changing attention and expression rather than partitioning
  reality

### Lived in the world, legible in the ledger

- Important state perceptible in the world and available in functional form
- Atmosphere never excusing obscurity
- Clarity about known facts without eliminating uncertainty or suspense

### Conservation of Systems — governing doctrine

- New meaning arising through context, combination, permission, species
  expression, manifestation, and memory before new meters or subsystems
- A small reusable grammar protecting player attention
- Mechanical restraint supporting expressive variety

### Game Logic opens Attachment Space — governing doctrine

- Legibility enabling competence
- Competence enabling stability
- Stability releasing attention
- Released attention making attachment possible
- Repeatable attachment-forward systems performing genuine game work while
  permitting individual quiet moments to remain non-instrumental

## 1.4 One Persistent World: Two Modes, Five Registers

### One persistent world

- No disconnected minigames
- A Citizen, Place, object, Node, wound, promise, or memory remaining the same
  fact across every form of play
- Registers altering scale, pace, subject, and attention rather than reality
- Actions and consequences persisting through transitions
- Open situations remaining attached to the Citizens, Places, or Nodes where
  they exist until changed, resolved, or overtaken

### Mode, Register, operator, and view

- **Mode** — where primary life and responsibility are currently situated
- **Register** — the structural form of play
- **Operator** — the characteristic action through which the player engages a
  Register
- **View or camera** — a manifestation of a Register rather than the Register
  itself
- Interface decisions not changing game ontology

### Home and Away: Inward and Outward

- Home Mode gathering responsibility Inward toward the permanent Colony
- Away Mode extending responsibility Outward through particular Citizens
- Modes as centers of attention rather than exclusive jurisdictions
- Home able to concern an individual and Away able to change the Colony and
  Corridor

### Operationally exclusive, informationally permeable

- One Mode holding active player operation at a time
- Launch transferring active operation from Home to Away
- Homecoming returning active operation from Away to Home
- An active expedition keeping Away operational until its Homecoming completes
- Home information remaining inspectable through the Almanac, Roster, Project
  progress, and other established lenses while ordinary DWELL commitments remain
  suspended
- The Away party moving, resting, engaging Nodes, and making decisions only
  through direct player operation
- Home continuing through its established Roles, Practices, Projects, passive
  production, Civic Balance, Pressure, and world-time checks while operation is
  Away
- A consequential Home situation able to interrupt through cross-modal MEET and
  return attention afterward to the party's persistent Field position
- One active expedition at a time in v0.5

### The five-Register topology

| Mode | Register | Operator | Primary relationship |
|---|---|---|---|
| Home | Colony | **DWELL** | Understand, build, arrange, and sustain collective life. |
| Home | Embodiment | **EMBODY** | Experience ordinary life made possible by sanctuary. |
| Away | Field | **TRAVEL** | Carry particular lives through distance and changing territory. |
| Away | Crossing | **RISK** | Commit bodies, paths, burdens, and timing to immediate danger. |
| Home or Away | Encounter | **MEET** | Present an applicable situational decision matrix through focused choice and aftermath. |

### The Colony Register — DWELL

- The Colony Register as the primary form of Home play, attending to the Colony
  as a collective body
- DWELL engaging the player in understanding, building, arranging, and
  sustaining collective life
- Places, Practices, Roles, Projects, Resources, Readiness, and situated
  conditions forming its principal working material
- Named Citizens remaining visible and individually accounted for while being
  resolved through Body-Unit-normalized civic commitments rather than personal
  capability profiles
- An elevated, freely navigable operational view making the Colony's
  relationships and current posture legible without defining the Register by
  its camera
- Routine information remaining native to DWELL rather than seizing attention
  through a separate scene
- Sustained functioning in DWELL establishing or restoring Quiet Equilibrium
  and opening the potential for EMBODY
- EMBODY becoming available because the Colony can release attention from
  urgent stewardship rather than triggering automatically or functioning as a
  reward currency
- MEET bringing a consequential situation into focus when it requires direct
  attention, while Launch carries named Citizens from Home into Away
- Homecoming returning material, bodily, relational, civic, and remembered
  consequences to the Colony Register
- DWELL as stewardship rather than factory maximization or perpetual crisis
  prevention
- Detailed Home systems deferred to Part III

### The Field Register — TRAVEL

- The Field Register as the primary form of Away movement through extended
  territory
- TRAVEL carrying a particular party of named Citizens through Reaches,
  Margins, Nodes, and changing conditions
- Distance, time, load, shelter, Nodes, and the changing condition of the party
  and world as its principal working material
- The party never becoming an abstract expedition marker; the same Citizens
  who left Home remain physically and historically present
- A characteristic presentation following the party through terrain at animal
  scale while keeping the ground ahead, available shelter, and carried burden
  legible
- Traversal, observation, ordinary discovery, and changing environmental
  information remaining native to the Field without demanding a separate scene
- Engagement with a Node, animal, or group opening MEET when it becomes
  consequential and requires focused choice
- Reaching a Roadway threshold moving the party into RISK, with a completed
  Crossing returning it to the continuous Field on the other side
- Return using the same geography and accounting for elapsed time, changed
  conditions, injuries, companions, and Cargo rather than teleporting the
  outcome Home
- Field play as neither a mission-selection map, generic open world, tactical
  combat layer, nor stream of compulsory event cards
- Detailed movement, time, personal states, Cargo, and return procedures deferred to
  the later Away chapters

### The Crossing Register — RISK

- The Crossing Register as the concentrated Away threshold where human-scale
  traffic becomes immediate bodily danger
- RISK belonging specifically to Crossing rather than serving as a universal
  resolution system for every dangerous action
- Uniquely among the five Registers, Crossing changing its fundamental play
  experience according to Core Species rather than merely modifying odds,
  speed, or presentation
- **Crossing examining animal biology through the lens of movement under
  hazard:** each Core Species confronting the same traffic simulation through
  its own body, perception, and locomotion

| Core Species | Crossing experience |
|---|---|
| **Rabbit** | Read the broad traffic pattern, choose an opening, and commit to one complete sprint. |
| **Mouse** | Read pavement-scale terrain and link meaningful waypoints into one continuous scurry. |
| **Squirrel** | Plot a flowing trajectory through moving traffic with limited planned redirection. |

- The three experiences retaining a common contour: **Plan → Commit →
  Continuous Run → Resolve**
- After commitment, the party executing the Crossing continuously, without the
  Roadway pausing for turns or repeated strategic revision
- The party following one global plan and receiving a global passage result,
  while bodily adversity may attach to particular Citizens
- Day Band, traffic condition, River Spume, weather, party composition, and
  carried burden entering RISK from the shared world
- A closer camera, heightened sound, altered pacing, and denser information
  expressing a change of attention rather than entry into a disconnected
  minigame
- A completed Crossing returning the party to the Field on the other side,
  while a sufficiently consequential result may instead open MEET
- Crossing outcomes remaining attached to the party through subsequent TRAVEL,
  the return Crossing, and Homecoming
- RISK as neither an arcade road-crossing game nor a turn-based tactical
  Encounter
- Detailed planning and resolution rules deferred to the dedicated Crossing
  chapters

### The Encounter Register — MEET

- **The Encounter Register uses MEET to present focused situational choice and
  consequential state transition.**
- Encounter is cross-modal: MEET may arise during DWELL or TRAVEL, from RISK
  aftermath, or through a systemic transition.
- MEET does not imply danger, opposition, or a separate event space. It focuses
  a situation already present in the persistent world.
- Routine activity remains within its owning Register until it crosses the
  decision or state-transition threshold.
- Choice Events use MEET without forming a separate system. Launch, Rest, and
  Homecoming use dedicated systemic forms.
- A simple Field example is: **TRAVEL → engage a consequential Node → MEET →
  consequence → return to TRAVEL.**
- Chapter 1.5 defines the complete MEET contract.

### The Embodiment Register — EMBODY

- The Embodiment Register as MEDIAN's second Home Register and principal
  positive destination
- EMBODY as optional and Home-only, becoming available through Quiet
  Equilibrium
- A temporary descent from Colony-scale stewardship into the lived physical
  scale of a present and available Citizen
- Particular moments of activity, motion, repose, relationship, play, and sensory
  attention making sanctuary materially felt
- A closer and more intimate presentation expressing animal-scale Presence
  without making camera proximity sufficient to create EMBODY
- No required failure state, punitive pressure, or exclusive economic output
- EMBODY as neither a general close-camera mode, Away traversal layer,
  trauma-clearing minigame, nor additional production channel
- Consequential MEETs not occurring inside EMBODY; urgent situations end
  eligibility and return attention to the appropriate Register
- EMBODY experiences able to deepen attachment or enter memory without every
  ordinary moment requiring instrumental justification
- EMBODY recurring whenever its conditions are met rather than serving as a
  terminal reward or post-expedition epilogue
- Detailed experience families, species expression, and eligibility rules
  deferred to Part III

### Continuous transitions

- Transitions as emotional and attentional beats rather than neutral loading
  screens
- Borrowed visual composition not changing Register identity
- What is open to the player not necessarily open or exposed within the world
- Manifestations translating interface and camera while preserving dramatic
  function

### The Home–Away–Return cycle

- Home → Launch → Away [RISK / TRAVEL / MEET] → Return → Homecoming → Home
- A dramatic circuit rather than a mandatory screen sequence
- RISK, TRAVEL, and MEET recurring or appearing in situational order
- Launch, Return, and Homecoming as transitions or procedures rather than
  additional Registers
- Homecoming reintegrating material, bodily, relational, civic, and remembered
  outcomes
- The changed Home becoming the ground of the next choice

## 1.5 MEET: The Situational Decision Matrix

**MEET is MEDIAN's universal presentation for focused situational choice and
consequential state transition.** It brings together the relevant participants,
place, known facts, stakes, and available responses when the player needs to
decide what happens next or attend to an important change becoming true.

A MEET may concern danger, work, care, opportunity, arrival, rest, ceremony,
conversation, or aftermath. It focuses a situation within the same Colony,
Field, Citizens, objects, relationships, and history. Opposition is one
possible circumstance among many.

DWELL, TRAVEL, RISK, relationships, Items, environmental conditions, or
Campaign state supply and resolve the subject. MEET makes the choice or
transition legible, while the systems that own the affected facts apply and
retain its consequences.

### When play becomes MEET

Most MEETs use the **decision threshold**:

1. **A specific situation:** the subject, participants, and physical or civic
   setting are known.
2. **A meaningful decision:** the player has at least two materially different
   responses, including refusal, endurance, or withdrawal when those are
   credible.
3. **A consequential distinction:** choosing among those responses changes
   what happens, what is spent, what is protected, what becomes possible, or
   what persists afterward.

A narrower class uses the **state-transition threshold**:

- A bounded transition changing or reconciling several important persistent
  facts at once
- Those changes benefiting from presentation through the participating
  Citizens, Places, objects, and consequences together
- The player able to review, acknowledge, or make limited allocations without
  needing a branching decision to justify the MEET

**Homecoming** is the clearest state-transition MEET. It physically receives
the returning party, applies bodily consequences, transfers Cargo, restores
civic availability, updates relationships and Campaign Memory, and returns
play to Home. It warrants focused presentation even when nothing remains
undecided.

Routine information and state changes remain in the Register that produces
them. A Resource total changing, rain beginning, a Node entering view, a
Project completing, or a Citizen becoming available does not alone create
MEET. The state-transition threshold is not a generic notification or cutscene
format.

Routine actions also remain native to their Register. MEET begins when the
player benefits from seeing the situation's participants, choices, costs, and
stakes together before committing, or from seeing a consequential transition
reconcile the world as one event.

### Chosen and arriving situations

MEET may begin in either direction:

- **The player attends:** engaging a consequential Node, opening a known Colony
  situation, preparing to Launch, choosing to Rest, or addressing an available
  relationship.
- **The situation calls:** World Pressure reaches the Colony, another animal or
  group intercepts the party, an authored event matures, or completed RISK
  creates a decision on the far side.

An urgent situation never ambushes the player inside EMBODY. It ends EMBODY
eligibility and returns attention to the appropriate Register before MEET
opens.

### What a MEET shows

Before the player commits, MEET makes these elements legible:

- The physical or civic setting and current time
- The situation's subject and relevant participants
- Known facts, including meaningful uncertainty
- What is sought, threatened, offered, or changing
- The materially distinct responses available now
- The requirements and immediate costs of each response
- The likely direction of consequence without exposing exact hidden odds
- What refusal, endurance, delay, or withdrawal means when applicable

Tharn is the defined exception to consequence preview. Chapter 5.6 governs its
causes and resolution; MEET never names, highlights, or forecasts its
possibility before it occurs.

The same Place, Node, Citizens, objects, weather, and damage remain visually
recognizable. MEET focuses the existing world rather than replacing it with a
generic event backdrop or fixed portrait lineup.

A state-transition MEET instead foregrounds what has changed, which persistent
facts are being reconciled, and any limited allocations or acknowledgments
still available.

### Subject, participants, and stakes

Every MEET has one clear **subject**: the particular situation now receiving
the player's attention. Its subject may be a threatened Place, an encountered
animal or group, a contested Resource, a social exchange, a returning party,
or any other situated matter that crosses a MEET threshold.

A MEET ordinarily presents **one to three active stakes**, ordered by their
importance to the present situation. A stake is something the current response
can protect, spend, gain, lose, change, or leave unresolved. Other persistent
facts continue to inform resolution while the display reserves stake status
for the present decision's central concerns. State-transition MEETs may
reconcile many facts by grouping them into a small number of intelligible
concerns.

Participants appear at the scale the situation requires:

| Scale | Participant presented |
|---|---|
| **Colony** | The Colony collectively when a civic situation is broadly shared |
| **Place or group** | The affected household, Practice, family, or other situated group |
| **Citizen** | A named Citizen when their body, relationship, possession, or history materially matters |
| **Away party** | The present expedition as a group, with only materially involved members called out |
| **Transition** | The Citizens, goods, injuries, and relationships crossing between states |

Named Citizens are not added as decorative witnesses. Core Citizens remain
fractional player characters within the Colony or party rather than autonomous
agents who may independently refuse the player's command. Non-Citizen animals
and groups retain their own aims and agency, but their presence does not by
itself imply conflict.

### Presentation in the world

MEET keeps the world itself prominent. Its interface clarifies the current
situation through the visible scene:

- The Place, Node, terrain, participants, and visible condition occupying most
  of the presentation
- Short in-world labels identifying only facts and participants needed to read
  the situation
- A compact response matrix paired with a concise statement of subject and
  stakes
- A contextual summary gathering the known facts that materially constrain the
  decision
- Relevant Citizens remaining visible as members of the Colony or party rather
  than becoming a generic portrait lineup
- Character speech or narration interpreting the situation without replacing
  mechanical clarity
- Interface ornament, meters, and labels remaining subordinate to the scene

After provisional selection, the chosen response expands in place to reveal
its applicable expressions. Tools, Supplies, Keepsakes, relationships, and
Signatures do not require a separate general inventory grid. If another Round
follows, the same scene persists while changed facts replace the response set
and contextual summary. Focus is expressed through framing, animation, action,
speech, and resolution language rather than a character-selection step or
meter.

Dedicated forms preserve this grammar while presenting what they actually do.
A Homecoming MEET, for example, presents reconciliation concerns and limited
allocations rather than disguising them as competing tactical responses.

### Available and unavailable responses

- Each MEET presenting a response set authored for that situation rather than
  every theoretical action
- A response that is relevant but presently unavailable remaining visible when
  understanding its absence matters
- An unavailable response stating the concrete reason: missing capability,
  insufficient Resource, absent participant, physical impossibility, or prior
  consequence
- Irrelevant responses remaining absent rather than filling the interface with
  disabled choices
- Refusal, endurance, or withdrawal appearing only when physically and
  situationally credible

This allows a particular MEET form to establish its own named response families
without forcing those responses into Homecoming, Launch, Home Pressure, or
every other situation.

A contested Away MEET is the defined exception. It always shows its five
response families in canonical order so their positions and absences remain
legible. An inactive family is greyed and gives a concise reason grounded only
in facts the party can know. Chapter 5.5 defines that fixed display and its
contextual actions.

### From response to commitment

1. **Frame.** MEET establishes the situation, participants, facts, and stakes.
2. **Select.** The player provisionally chooses a response.
3. **Express.** Only the Resources, civic commitments, Tools, Supplies,
   Keepsakes, relationships, Signatures, or other capabilities able to affect
   that response become available.
4. **Commit.** The player confirms the complete response after seeing its
   immediate costs and likely direction.
5. **Focus.** The committed response determines which Citizen the Round
   follows when one is applicable.
6. **Resolve.** The owning systems determine the shared result, individual
   consequences, and persistent aftermath.

A state-transition MEET may shorten this sequence to **Frame → Reconcile →
Allocate if applicable → Continue**.

### Responses and expressions

A **response** is what the Colony or party attempts. An **expression** is the
Tool, Supply, Keepsake, relationship, Guest Signature, or other capability
through which that response becomes possible or changes.

- The player provisionally selecting a response before choosing an expression
- The player remaining free to return to the response matrix before final
  Commit
- Relevant expressions therefore informing the final option choice without
  filling the initial matrix with inventory
- Each expression stating exactly what it changes: availability, cost,
  protected stake, likely result, or consequence
- No expression providing an unspecified bonus or guaranteeing success

### Tools, Supplies, and Keepsakes

Tools, Supplies, and Keepsakes ordinarily change how an existing response is
carried out. The authored response remains the top-level choice.

- A provisional response revealing every Tool, Supply, or Keepsake that can credibly
  affect it
- Several relevant Items appearing as alternatives rather than stacking
- At most one active item expression—one Tool, Supply, or actively committed
  Keepsake—being used in a Round
- A Tool supplying its full contextual effect before any resulting hazard is
  applied
- A used Tool entering hazard only when the situation actually threatens it
- A Supply applying its stated effect and being consumed upon Commit
- A Keepsake able to inform a response through recognition without becoming
  the active item; offering, using, surrendering, or placing it at stake making
  it the active item instead
- Carry Tools remaining standing equipment unless their capacity or Cargo is
  specifically at stake
- The player able to return after seeing these expressions and select a
  different response

### Guest Signatures and choice

A Guest's species affordance is expressed mechanically through its
**Signature**. Unlike an ordinary Tool, a Signature may affect the response
matrix itself.

A relevant Signature may:

- Reveal information that changes how the available responses are understood
- Open a response that the party could not otherwise attempt
- Make an unavailable response available
- Change a response's immediate cost, protected stake, or likely consequence
- Provide a distinct means of carrying out an otherwise shared response

The Signature appears only when its defined bodily, ecological, social, or
spatial circumstances are present. It neither grants general aptitude nor adds
an extra action. A Signature may coexist with one active Tool or Supply when
both credibly contribute, but each retains its authored effect; they do not
combine into a generic stacked bonus.

### Multiple Rounds

Most MEETs resolve in one **Round**. A situation may continue for up to four
Rounds when one response changes the circumstances and leaves them open.

Each Round follows **Frame → Select → Express → Commit → Focus → Resolve**.

After Resolve:

- A closed situation proceeding to aftermath
- A changed situation presenting its new facts, stakes, and contextual
  responses in another Round
- Spent Resources and Supplies, Tool hazard, injuries, changed relationships,
  and other consequences remaining true
- The player unable to reset the situation or repeat the same unchanged attempt
- Withdrawal, endurance, or refusal remaining available in later Rounds only
  when still credible
- A Round not automatically equaling a Day Band, with the owning situation
  determining elapsed time

A situation requiring more than four Rounds resolves into aftermath or becomes
a new linked situation rather than extending one decision interface
indefinitely.

### Focus

**Focus identifies whose life the current Round follows.** The Colony or party
still chooses and resolves the response collectively.

The committed response establishes an eligible Focus set from any Citizen who
is directly identified by its required action, Guest Signature, active Tool or
Supply, applicable Keepsake, relationship, or authored circumstance. One
eligible Citizen takes Focus. When several Citizens qualify, the system selects
one of them at random.

- Focus resolving after Commit so that it cannot steer the player's choice
- Every causally involved Citizen remaining present even when another receives
  Focus
- Focus governing camera, animation, principal speech or action, resolution
  language, and possible Tale attribution
- Focus never being selected directly or rerolled
- Focus never changing response availability, success, aptitude, consequence
  targeting, or Exposure by itself
- The MEET's framing able to concern one Citizen while another takes Focus for
  a particular Round
- Focus able to move naturally to another Citizen in a later Round
- A Round remaining collective when nothing identifies an eligible Citizen
- A Focused action entering a Tale only when the underlying event independently
  warrants memory
- No Focus meter, bonus, progression, or additional action

### Resolution and aftermath

MEET resolves through the facts and rules owned by its particular situation.
Commit guarantees the stated action and its immediate cost. Known
circumstances, the chosen response, and its committed expressions establish as
much of the outcome as they can; bounded hidden variation answers any genuine
uncertainty that remains.

Resolution proceeds from the shared undertaking to its particular
consequences:

1. Apply the committed response, costs, civic commitments, and expressions.
2. Resolve what the Colony or party collectively achieves, prevents, accepts,
   or leaves unfinished.
3. Attach particular consequences to the Citizens, objects, relationships,
   Places, or other facts causally involved.
4. Return every changed fact to the system that owns and persists it.
5. Present the resulting world state and any immediate continuation.

A result may be mixed. One stake may be protected while another is lost, an
objective may be achieved at a cost, or withdrawal may preserve the party while
leaving the subject unresolved. Group success does not protect every
participant from consequence, and individual harm does not automatically erase
the shared result.

Resolution never adds an unrelated surprise penalty. Afterward, the player is
shown what changed and why without receiving a generic success, failure, score,
or expedition grade. The event enters Campaign Memory only when what happened
independently warrants remembrance.

### Choice Events

**Choice Events are authored situations presented through MEET. Systemic and
state-transition MEETs complete the larger form.**

A Choice Event is authored content that supplies a bounded situation to the
Encounter Register. It defines:

- The world-state eligibility and means by which the situation arrives
- Its subject, participants, and one to three active stakes
- Its contextual response set and any meaningful unavailable responses
- The facts and expressions that can alter those responses
- Its possible resolutions, costs, and persistent aftermath
- Any continuation or Campaign Memory hooks that the outcome warrants

MEET supplies the shared presentation, commitment, Focus, resolution, and
aftermath grammar through which that content is played. Choice Events do not
form a separate event system or Register.

Launch, Rest, Homecoming, and other systemic MEET forms are not Choice Events
unless an authored situation specifically modifies them. Their subject and
procedure arise from the transition or system they already serve.

### MEET design relationships

MEET situations have three useful design relationships:

- **Systemic forms:** Launch, Rest, and Homecoming use dedicated procedures
  because they conduct recurring transitions.
- **Situated decisions:** Home Pressure, Nodes, encountered animals, Field
  Cards, RISK aftermath, relationships, and other owning systems may supply a
  particular condition that crosses a MEET threshold.
- **Choice Events:** authored situations enter through whichever Home or Away
  context owns them and use MEET to present and resolve their content.

These relationships organize design and authoring beneath the player-facing
level. Each MEET names and presents its actual subject—such as heavy winds, a
berry bush, or a Homecoming.

# PART II — THE CORRIDOR WORLD

Part II establishes the physical and perceptual reality in which the game
occurs before explaining what the player builds or governs. The Corridor is not
merely a map or backdrop: it is active human infrastructure inhabited at animal
scale. Its spaces mean different things to different bodies, its conditions
change over time, and much of it must be discovered before it can be
understood.

The Part proceeds from world to geography, biome, habitation, and change.
Chapter 2.1 supplies the establishing view; Chapters 2.2–2.5 bring its spatial,
environmental, ecological, temporal, and consequential layers into focus.

## 2.1 A World at Animal Scale

### Nobody's destination, somebody's home

- Human leftover space becoming animal homeland, sanctuary, and polity
- The median protected enough for settlement but never detached from exposure
- Nobody's destination becoming a place whose inhabitants choose to remain

### The highway is an environment

- Active traffic, noise, heat, runoff, salt, wind, barriers, and maintenance
- The road as terrain, climate, resource edge, ecological organizer, and danger
- Human scale as vast, mostly indifferent, and only partly legible
- The Highway remaining an active and maintained human system rather than an
  abandoned or post-human ruin

### Civilization in the seams

- Animal civilization arising from bodies, ecological needs, and inherited
  practices
- Soil, vegetation, drainage, debris, and scavenged material understood through
  their affordances
- Animals inhabiting and reinterpreting human infrastructure according to
  their own scale and needs rather than reproducing miniature human industry

### One Corridor, many Reaches

- The Colony situated within a continuous world rather than an isolated level
- Reaches, Roadways, Margins, and Outposts introduced as related parts of the
  Corridor
- Detailed spatial definitions deferred to Chapter 2.2

### Three ways of inhabiting the same ground

- Mouse safety understood through enclosure and belonging
- Rabbit safety understood through neighborhood and company
- Squirrel safety understood through routes and reach
- Three core species inhabiting different experiential worlds within the same
  physical landscape
- Other animal peoples existing beyond the three civic foundations

### Partial understanding, language, and folklore

- Animals understanding the human world through observation, inherited
  explanation, and culturally accumulated language
- Giants as part of the animals' partial understanding of human-scale phenomena
- Laws and Sayings as cultural interpretations rather than objective cosmology
- Fuller treatment of culture, records, and memory deferred to their later home

Throughout Chapter 2.1, sanctuary remains distinct from perfect safety, peril
from combat fantasy, animal civilization from miniature human industrialism,
and quiet from emptiness.

## 2.2 The Shape of the Corridor

### The Highway in cross-section

- **Sound Wall ‖ Margin | Main Roadway | Median | Main Roadway | Margin ‖ Sound Wall**
- The Highway as the complete physical setting and the two Main Roadways as its
  continuous lateral traffic bands
- Smaller roads able to cut across the Median at longitudinal Reach borders
- The Sound Walls as hard lateral world boundaries rather than playable zones
- Shoulders, road edges, drainage, vegetation, and other features situated
  within the playable bands

This simple section contains a lived gradient on either side. The Median
interior gives way to verge, shoulder, drainage, exposed Staging ground, and the
Main Roadway. Beyond it, the Roadway-side Margin receives the strongest River
Spume and most volatile material opportunity; mixed ground occupies the middle;
and the Sound-Wall-side Margin more readily traps moisture, vegetation, shelter,
and debris. The ground at the wall's base remains playable while the wall
itself ends the world laterally.

- Local geometry able to narrow, widen, flood, harden, obscure, or interrupt
  these tendencies while preserving the cross-sectional relationship
- A smaller Reach-border road creating a compressed Roadway edge, moving
  surface, and far-side refuge inside longitudinal Median travel
- The cross-section remaining physically continuous rather than dividing The
  Highway into abstract zones or separate maps

### From Corridor to Reach to Median

- The Corridor as the continuous longitudinal organization of The Highway
- A Reach as one comprehensible segment of the Corridor
- The Median as the central habitat band continuing through successive Reaches,
  with a smaller road able to interrupt it at a Reach border
- Each Reach also containing its corresponding Roadways and Margins
- The Corridor continuing beyond the presently known or represented Reaches

### The Colony and the Home Median

- The Colony, or its eventual proper name, as the permanent civic settlement
- The Colony occupying a particular median informally called the Home Median
- Home Median as geographic shorthand rather than the Colony's name
- Home used alone reserved for the Mode
- No separate Home Reach term

### Along the Corridor and across a Roadway

- Longitudinal travel through a Reach and between Reaches
- Upcorridor and downcorridor as the primary directions
- A smaller Reach-border road sometimes requiring a Crossing during
  longitudinal travel between adjacent Reaches
- Transverse movement between Median and Margin crossing a Main Roadway
- Main and Reach-border roads using the same RISK procedure and species grammar
- Road width, traffic, visibility, weather, and physical setting determining
  the character and valid consequences of each Crossing
- A Staging Post applying wherever a crossing point is chosen
- No separate Crossing Site category
- TRAVEL and RISK procedures deferred to Away

### Nodes and Outposts

- A Node as a meaningful location anchored in Away geography
- An Outpost as a persistent Away foothold established within a Reach
- An Outpost remaining categorically distinct from The Colony
- Node interaction and Outpost functions deferred to Away

## 2.3 Biomes and Founding Reaches

Biomes give the continuous Corridor a recurring environmental vocabulary. Each
one describes a broad grammar of ground, vegetation, water, exposure,
infrastructure, spatial rhythm, shelter, and obstruction. A Reach realizes that
grammar as one particular place with its own arrangement, history, landmarks,
and present conditions.

A **founding Reach** is a curated occurrence whose local topology makes the
selected Core Species' spatial grammar immediately legible. Species selection
chooses a compatible founding site within the shared world; the terrain retains
the same identity when another species later encounters it.

> **Randomize the contents of the starting territory, not the spatial grammar
> that makes the species meaningful.**

### One world, species-relative fit

- Every biome remaining available to Mouse, Rabbit, Squirrel, Guests, and other
  animals throughout the Corridor
- Founding compatibility belonging to the particular site's topology rather
  than exclusive biome ownership
- The same biome able to serve as a founding Reach in one campaign and an
  ordinary Corridor Reach in another
- Species changing which features become useful, safe, connective, exposed, or
  worthy of attention while the physical place remains shared
- A biome establishing environmental identity without prescribing every Node,
  Place, resource, event, or local arrangement within a Reach

### Species-relative founding requirements

#### Mouse — JOIN

A Mouse founding Reach supplies edges, enclosure, seams, cavities, or
infrastructure capable of becoming one protected inhabited body. Expansion can
proceed from room to wing to connected second house.

- Continuous or joinable boundaries
- Sheltered low-level circulation
- Opportunities to thicken an inhabited envelope
- Legible distinctions among dry interior, exposed exterior, and protected
  transition
- Enough adjacency for growth to increase connection rather than scatter rooms
  into detached buildings
- Bridges supporting an already coherent fabric instead of substituting for
  contact between otherwise unrelated clusters

#### Rabbit — GATHER

A Rabbit founding Reach supplies cover, several plausible household refuges,
common safe ground, and multiple ways back into concealment. Expansion can
proceed from one complete court to a daughter court and eventual connection
between social centers.

- Shared clearing or court
- Household-scale refuge around its perimeter
- Brush, banks, roots, deadfall, or other protective edges
- More than one retreat path
- Room for communal life at an intimate rather than monumental scale
- Common ground whose safety arises from surrounding terrain and nearby cover

#### Squirrel — CONNECT

A Squirrel founding Reach supplies meaningful separation: multiple anchors,
differences in height, gaps, interrupted surfaces, or structures that become
useful through connection. Expansion can proceed from first reach to
reinforcement and then to a resilient network of loops.

- Several nodes rather than one dominant central structure
- Vertical and horizontal movement
- Trunks, branches, ledges, posts, cables, bridges, runs, or comparable route
  opportunities
- Alternate paths able to emerge as the Colony develops
- Continuity expressed through the network itself
- Central trees or towers serving as anchors within a larger web of choices

### The twelve biome grammars

| # | Biome | Primary environmental identity | Founding relationship |
|---:|---|---|---|
| 1 | **Rootbank Meadow** | Grass, eroded banks, exposed roots, shallow hollows, and sheltered clearings | Rabbit |
| 2 | **Bramble Hollow** | Dense thorn and vine cover organized around narrow passages and protected openings | Rabbit |
| 3 | **Culvert Garden** | Drainage infrastructure, wet soil, raised banks, stone, and seasonal flow | Mouse |
| 4 | **Concrete Trench** | Retaining faces, hard seams, broken slabs, runoff channels, heat, and shade lines | Mouse |
| 5 | **Wooded Median** | Trunks, canopy, roots, fallen branches, shade, and interrupted visibility | Squirrel |
| 6 | **Rock Cut** | Shelves, fissures, ledges, sparse trees, height changes, and natural gaps | Squirrel |
| 7 | **Thin Grass Ribbon** | Narrow exposed ground, long sightlines, wind, and road proximity | Corridor |
| 8 | **Creek Split** | A persistent longitudinal stream dividing banks, islands, and crossings | Corridor |
| 9 | **Pond Hollow** | Standing water, reeds, saturated ground, seasonal margins, and concealed approaches | Corridor |
| 10 | **Interchange Expanse** | Broad, disorienting territory among diverging roads and scattered infrastructure | Corridor |
| 11 | **Overpass Shadow** | Columns, beams, abutments, dry recesses, echo, vibration, and artificial shade | Unusual Corridor |
| 12 | **Abandoned Works** | Incomplete drainage, gravel beds, pipe, rebar, cut earth, and interrupted construction | Unusual Corridor |

The six Core-Species relationships define the founding pool. The remaining six
broaden the country encountered through exploration. Every biome can later
support traversal, Nodes, MEETs, Outposts, and possible habitation by any
species when the particular site permits them.

### Rootbank Meadow

Rootbank Meadow is broad enough to read as open country but broken by low
rises, erosion cuts, exposed roots, shallow banks, grass clumps, and irregular
shrub cover. Visible common ground alternates with immediate refuge. A strong
founding instance contains a modest central clearing bounded on several sides
by banks or roots, creating household-scale pockets without separating them
from one another.

- Rabbit recognizes a legible first court whose social meaning emerges through
  shelters, household edges, paths, stores, and communal Practices. Later
  growth may establish a daughter court behind another bank or root mass.
- Mouse reads root seams, low hollows, and fallen material as fragmented shelter
  opportunities.
- Squirrel reads shrubs, roots, posts, and low branches as a shallow network
  with limited vertical reach.
- The visual grammar preserves irregular cover, multiple escape paths, and
  terrain-led growth rather than a manicured or symmetrical village green.

### Bramble Hollow

Bramble Hollow is dominated by honeysuckle, thorn, deadfall, leaf litter,
interwoven stems, narrow animal runs, and pockets where cover opens
unexpectedly. Short visibility makes the Reach feel larger from within; its
central contrast lies between dense cover and small spaces of remarkable
safety.

- Rabbit makes a community from protected openings, with several household
  refuges facing one shared interior.
- Growth clears and tends passages while retaining the thicket's boundary and
  concealment. A daughter court may form beyond a dense screen through several
  protected approaches.
- Mouse reads the lower stem mesh as covered micro-runs, seed traps, and
  temporary wall texture.
- Squirrel reads upper bramble and deadfall as a secondary network leading
  toward stronger anchors.
- The visual grammar keeps the thicket spatially legible while allowing
  habitation to appear partly discovered within it.

### Culvert Garden

Culvert Garden centers upon a drainage mouth or connected drainage structure,
a narrow flow or seasonal trickle, damp soil, raised dry banks, stone, sedges,
volunteer plants, and material deposited by runoff. Staining, debris lines, and
scoured ground disclose flood history and distinguish ordinary flow from
high-water refuge.

- Mouse can incorporate the culvert directly into JOIN. Development may occupy
  banks, rim, structure, and attached rooms while maintaining protected
  internal circulation.
- The water leaves meaningful dry ground, so enclosure and connection remain
  player decisions rather than a predetermined facade.
- Rabbit reads the culvert as severe-weather shelter, hard boundary, escape
  mouth, and potentially dangerous deep pocket.
- Squirrel reads it as low understructure requiring connections upward to
  stronger anchors.
- The visual grammar preserves credible flood pressure, open buildable banks,
  and the culvert's role as an active environmental organ.

### Concrete Trench

Concrete Trench is a depressed or heavily hardened Median of retaining faces,
seams, drainage slots, broken slab, exposed aggregate, narrow soil pockets,
reflected heat, sudden shade, and concentrated runoff. Opportunistic vegetation
leaves the engineered human scale continuously visible.

- Continuous walls and slab edges give Mouse a powerful JOIN grammar. Chambers
  accrete against seams, beneath lips, within drainage voids, and along
  protected runs.
- Rabbit finds shade and hard boundaries alongside limited digging,
  channelized escape, and sparse concealment.
- Squirrel finds climbable faces, seams, ledges, and occasional infrastructure
  anchors with fewer living connections.
- Live traffic, maintenance traces, drainage, salt, and heat keep the Reach
  recognizably modern rather than ruinous or monumental.

### Wooded Median

Wooded Median contains mature or closely spaced trees, saplings, canopy breaks,
roots, fallen branches, leaf litter, shade, and limited long sightlines. Traffic
remains perceptible through noise, vehicle flashes, barriers, and openings
between trunks.

- Several trees or large branches provide Squirrel's initial nodes.
- Colony growth establishes provisional reaches, reinforces them, introduces
  vertical separation, and creates alternate paths and loops.
- Mouse reads roots, litter, fallen bark, and trunk bases as low cover and
  fragmented enclosure.
- Rabbit reads root pockets, deadfall, and brush clearings as refuge while dense
  trunks complicate shared ground.
- The founding composition preserves several viable anchors and keeps bridges
  dependent upon credible destinations rather than presenting one dominant
  tree as a complete settlement.

### Rock Cut

Rock Cut is formed by layered stone, fissures, shelves, narrow channels,
elevation changes, sparse vegetation, occasional wind-shaped trees, and abrupt
gaps. Its usable but incomplete spatial islands make height and separation
immediately visible.

- Ledges become Squirrel nodes; branches, roots, posts, and constructed runs
  connect them into a traversable Colony.
- Several plausible alignments preserve player agency and make redundancy an
  achieved quality.
- Mouse finds excellent individual shelter in fissures and undercuts while
  facing difficulty joining them.
- Rabbit finds refuge in shelves and pockets while shared courts may remain
  constrained or exposed.
- Road, barrier, drainage, and regional vegetation keep the scale rooted in a
  highway cutting rather than mountain country.

### Thin Grass Ribbon

Thin Grass Ribbon is a narrow Reach of low vegetation, few substantial objects,
strong wind, long sightlines, and constant awareness of both roads. A lone
shrub, damaged delineator, tire fragment, shallow depression, or weed-thick
drainage seam gains unusual importance because so little interrupts the ground.

- The biome tests Exposure, observation, distance, and the value of slight
  cover.
- Mouse searches for scarce continuous low edges.
- Rabbit finds feeding ground and long warning distance paired with broad
  exposure.
- Squirrel encounters isolated anchors and fragile connections with little
  vertical redundancy.
- Sparse terrain retains clear navigation structure and road proximity without
  acquiring decorative clutter.

### Creek Split

Creek Split contains a persistent longitudinal stream organizing the whole
Reach into parallel banks, intermittent islands, crossing places, undercut
edges, deposits, and seasonal high-water paths.

- The creek creates neighboring territories whose local connections change
  with rain, erosion, obstruction, and seasonal flow.
- Mouse seeks bank seams, roots, deposited material, and protected crossings
  while water interrupts JOIN.
- Rabbit reads parallel banks as cover systems linked by a limited number of
  safe crossing places.
- Squirrel treats banks and islands as nodes where branches or infrastructure
  may span the channel.
- The stream remains small enough to belong inside the Median and continuous
  enough to shape the entire Reach.

### Pond Hollow

Pond Hollow is a low basin of standing water, reeds, saturated margins,
seasonal mud, insects, amphibian life, concealed approaches, and temporarily
usable dry ground. Its shape and accessibility change more readily than its
identity.

- Water margin, uncertain footing, concealment, contamination, and strong
  ecological presence shape exploration and local MEETs.
- Mouse finds rich edge material and shelter pockets while moisture threatens
  low interiors.
- Rabbit finds cover and feeding opportunities while requiring dependable dry
  refuge and escape ground.
- Squirrel uses reeds, shrubs, posts, and overhanging branches as a network
  above difficult terrain.
- Runoff, barriers, litter drift, and culvert influence preserve the Hollow's
  Corridor origin and distinguish ordinary wetland from flood event.

### Interchange Expanse

Interchange Expanse is an unusually broad Reach formed where Roadways divide,
merge, curve, or cross nearby. Scattered infrastructure, irregular barriers,
long conflicting sightlines, isolated vegetation clusters, and several
apparent directions of travel make orientation its defining challenge.

- Mouse sees widely separated shelter seams and a difficult problem of
  protected continuity.
- Rabbit sees potential courts of cover separated by extensive open ground.
- Squirrel sees many possible anchors whose distance makes early connections
  fragile.
- Diverging highway geometry explains the breadth and keeps animal-scale
  navigation legible.
- **The Interchange** described in Chapter 6.5 is a singular authored campaign
  horizon occupying an exceptional Interchange Expanse; the biome name denotes
  the broader environmental grammar rather than that one destination.

### Overpass Shadow

Overpass Shadow lies beneath an overhead roadway or associated bridge
structure. Columns, beams, abutments, ledges, expansion joints, drainage
stains, protected dead spaces, echo, vibration, artificial shade, and sharp
light boundaries create a distinct architectural climate within the Corridor.

- Mouse reads abutment seams, drainage recesses, protected bases, and debris
  chambers as enclosure.
- Rabbit reads broad shade and sheltered edges alongside echo, hard ground, and
  potentially trapping boundaries.
- Squirrel reads columns, beams, joints, signs, and ledges as an artificial
  canopy.
- Active traffic overhead, modern materials, scale, vibration, and water
  staining keep the Reach continuous with the living Highway.

### Abandoned Works

Abandoned Works is an interrupted highway project reclaimed partly by weather
and ecology: incomplete drainage, gravel beds, stacked or scattered pipe,
rebar cages, cut earth, temporary barriers, erosion-control fabric, broken
pallets, and machinery fragments. Animal life has had time to inhabit it while
the unfinished human intention remains legible.

- Mouse sees prefabricated chambers and joinable material separated by unsafe
  open work ground.
- Rabbit sees earth cuts, fabric-covered banks, pipe shadows, and pockets of
  returning vegetation.
- Squirrel sees rebar, fencing, posts, stacked pipe, and temporary structures
  as a precarious artificial network.
- Dense material opportunity coexists with unstable shelter, blocked movement,
  sharp boundaries, and hidden voids.
- Local abandonment remains distinct from the active Highway and the broader
  inhabited world.

### Founding roster and opening selection

Each Core Species receives two contrasting founding expressions of the same
spatial grammar.

| Species | Founding biome A | Founding biome B | Contrast expressed |
|---|---|---|---|
| Mouse | Culvert Garden | Concrete Trench | One dominant infrastructural organ versus continuous hardened edges |
| Rabbit | Rootbank Meadow | Bramble Hollow | Open ground made safe versus concealment made communal |
| Squirrel | Wooded Median | Rock Cut | Living canopy network versus connections across exposed separation |

- The Founding Escape delivering the selected Core Species to one compatible
  founding Reach within the shared Corridor
- The selection method—direct player choice, bounded random selection, or
  authored presentation—remaining open for later authorial decision
- Starting contents, immediately available Nodes, minor resources, weather,
  and local details able to vary while the species-defining spatial grammar
  remains stable
- Both founding choices for one species required to produce materially
  different Colonies while preserving JOIN, GATHER, or CONNECT
- A founding biome remaining an ordinary part of the shared world when another
  species encounters it later

### Visual and spatial tests

Biome presentation establishes an inhabitable piece of highway country before
the Colony fills it. Each Reach makes the relationship among carriageways,
barriers, Median direction, terrain, water, vegetation, infrastructure,
animal-scale paths, refuge, exposure, and several plausible Places readable.

Founding-biome development may compare three stable views:

1. **Before Founding:** the territory showing why exhausted Founders recognize
   its potential.
2. **Early Colony:** a small settlement whose species grammar is already
   visible while much of the Reach remains available.
3. **Developed Colony:** growth that strengthens the same grammar and leaves the
   original terrain materially recognizable.

- Mouse images making the physical joins and protected circulation traceable
- Rabbit images making shared safe ground, participating households, protective
  edges, and alternate refuge paths traceable
- Squirrel images making distinct nodes, connective runs, network weakness,
  and future loops traceable
- Roads or their immediate Corridor context remaining visible enough to prevent
  generic pastoral or fantasy-land drift
- Animal scale, navigable space, irregular settlement form, fixed landmarks,
  and undecided buildable areas remaining consistent across development views
- At least one founding biome eventually shown as an unchanged uncolonized
  Reach attended to by another Core Species, demonstrating one world
  interpreted through different bodies

## 2.4 The Ecology of The Highway

### Shared ecology

- The animals of The Highway inhabiting one shared physical world
- The Median, Roadways, Margins, infrastructure, traffic, weather, plants, and
  animal activity forming one connected ecology rather than separate
  species-specific maps
- The chapter describing those common ecological conditions, with species
  distinctions in play reserved for DWELL

### The Median: relative sanctuary

- The Median as a long, narrow habitat band extending along the Corridor,
  enclosed between the Main Roadways and sometimes interrupted by a smaller
  road at a Reach border
- Soil, vegetation, drainage, cover, and reduced human access providing the
  conditions in which a permanent Colony can take root
- The Roadways that help isolate and protect the Median also confining it,
  limiting resources and routes of escape
- Sanctuary remaining relative: flooding, weather, scarcity, predators, and
  human maintenance can still disturb it

### The Roadways: barrier and exposure

- Crossing a Roadway being dangerous and consequential enough to occupy an
  entire Register: RISK; this chapter explains why, while its procedures come
  later
- The Main Roadways as large moving barriers between Median and Margins
- Smaller Reach-border roads as lighter but still consequential moving barriers
  within longitudinal Corridor travel
- Speed, noise, vibration, heat, fumes, water, and exposed pavement creating
  conditions unlike those of the Median or Margins
- Roadways dividing habitats that may be physically close and making every
  Crossing a distinct bodily threshold
- Roadway edges concentrating both hazards and opportunities through drainage,
  contamination, debris, and salvage

### The Highway Through the Day

- Morning, Midday, Evening, and Night changing the light, temperature,
  activity, and traffic rhythm of The Highway
- Those changing traffic conditions contextualizing phenomena such as River
  Spume
- Detailed time and traffic systems deferred to Chapter 2.5

### River Spume

- River Spume as the vehicle-generated turbulence, pressure shifts, and debris
  lift above and beside a Roadway
- Its character changing with traffic thickness—the present volume and spacing
  of vehicles—alongside speed, vehicle mix, surface wetness, weather, season,
  and time of day
- Dense traffic able to create sustained noise, fumes, moving air, spray, and
  debris disturbance while thinner high-speed traffic produces separated but
  forceful pulses
- Its effects strongest over and immediately beside the Roadway, then
  diminishing across the Margin toward the Sound Walls
- A Node's actual distance from the Roadway determining how strongly current
  River Spume enters its atmosphere, legibility, available responses, and
  possible consequences during MEET
- Roadway-proximate Nodes carrying an eligible chance for passing traffic to
  throw or dislodge an object into the situation, with likelihood and character
  following the present traffic, vehicle mix, weather, surface, season, and
  human activity
- A thrown object able to become immediate danger, interruption, material
  opportunity, or persistent Node change according to what physically arrives
- River Spume materially affecting Crossing, the Field, and situated MEETs
  without requiring one universal penalty or separate proximity meter
- Exact attenuation and thrown-object chances remaining a tuning question

### The Margins: Abundance and Disturbance

- Each Margin as the inhabited band between a Roadway and its Sound Wall,
  shaped by both without belonging fully to either
- Vegetation, insects, water, runoff, and accumulated human material making the
  Margins rich in food, shelter, salvage, and other Resources
- Margin Nodes forming around bushes and other natural features, thrown trash,
  scattered wreckage, or even a fully wrecked car
- These features functioning simultaneously as habitat, terrain, landmark,
  hazard, shelter, and source of Resources
- That abundance continually altered by contamination, flooding, mowing,
  maintenance, predators, human access, and River Spume
- The Sound Wall terminating the Margin as a hard world boundary rather than a
  playable zone

### Sound Walls: the sheltered boundary

- Sound Walls making the Corridor's human construction and lateral limit
  continuously legible
- Their material, height, joints, damage, drainage, and orientation shaping
  shade, warmth, wind, echo, vibration, runoff, and enclosure at animal scale
- Seeds, leaves, litter, water, and blown material collecting at their bases
  and supporting Nodes or passages where local geometry permits
- Wall-side growth tending toward greater shelter and stability than
  Roadway-edge growth while remaining exposed to mowing, maintenance, flood,
  heat, and contamination
- Openings, culverts, breaks, and service structures following their actual
  physical affordances without extending play beyond The Highway

### Resources Across the Margin

- Resource distribution following a broad gradient rather than rigid zoning
- Toward the Sound Walls, greater shelter and vegetation supporting bush Nodes
  that yield Perishable Sustenance
- Closer to the Roadway edge, thrown trash, deposited debris, and wreckage
  supporting Nodes that yield Flexible Scrap and Rigid Scrap
- A fully wrecked car becoming a major Node in its own right: part Resource
  deposit, part terrain, part shelter, and part persistent world feature
- Natural Node features occurring throughout the Margins and complicating the
  general Roadway-edge and Sound-Wall-edge pattern
- Roadway-adjacent Nodes tending toward greater exposure and volatile material
  opportunity, while sheltered Nodes tend toward greater stability and living
  Resources
- Exact Resource yields, gathering procedures, and economic uses deferred to
  Away and the later Resources chapter

### The Highway as Signal

- At animal scale, The Highway perceived through sound, vibration, and moving
  air as much as through sight
- Continuous traffic establishing an ordinary acoustic and vibrational
  background to life
- Horns, impacts, machinery, changing engine tones, altered vibration, and
  unusual silence signaling changed conditions before their causes are visible
- These signals providing partial information rather than perfect prediction
  and requiring interpretation through animal experience and folklore
- Detailed traffic and environmental-state effects deferred to Chapter 2.5

### Human activity as weather

Traffic is the continuous form of a broader relationship: animals experience
human activity as weather. They seldom see or understand its full cause, but
they can read rhythm, approach, intensity, direction, residue, and change.

- Traffic, maintenance, mowing, drainage work, litter, lighting, machinery,
  collisions, and Road Work arriving as large environmental conditions rather
  than as direct human interaction
- Repeated schedules and Day Bands allowing broad expectation while actual
  timing, extent, and local effect remain variable
- Sound, vibration, moving air, light, runoff, fumes, cut vegetation, displaced
  matter, and changed access often announcing human activity before its source
  is visible
- Human vehicles and machinery remaining fully depictable while human bodies
  stay outside the frame
- The animals responding through observation, preparation, shelter, movement,
  RISK, MEET, and persistent adaptation rather than through a separate
  human-behavior simulation

## 2.5 Time, Traffic, and Environmental Change

Time makes the Corridor legible, dangerous, and alive. One clock runs beneath
Home and Away. Light, traffic, season, weather, and human disturbance change
the same persistent places while the player's attention is elsewhere.

### One World, One Clock

- The calendar belonging to the world rather than to the current Mode or
  Register
- Meaningful commitments, movement, and duration advancing time; inspection,
  planning, reading, and camera movement not doing so
- Relevant conditions advancing everywhere when time advances anywhere
- Expeditions therefore occurring during Colony life rather than outside it on
  a detached mission clock

### DAWN and the Playable Day

- The daily sequence:

  **DAWN → Morning → Midday → Evening → Night → DAWN**

- Morning, Midday, Evening, and Night as the four playable Day Bands
- Day Bands changing light, temperature, animal activity, human disturbance,
  sound, scent, surface conditions, and the behavior of The Highway
- These effects belonging to particular circumstances rather than universal
  modifiers; Night, for example, mattering differently at different Places and
  Nodes instead of imposing one blanket penalty
- DAWN as an explicit transition rather than a playable Day Band, advancing the
  calendar, resolving daily accounting, progressing recovery and continuing
  work, reporting meaningful changes, and opening Morning in the active Mode
- The player choosing to proceed through DAWN after Night so that the calendar
  never rolls over unnoticed
- An active expedition receiving a concise Home accounting summary at DAWN and
  then resuming Morning TRAVEL at its persistent Field position

### Time at Home and Away

Home and Away use the same clock at the same resolution.

- The Day Band being the sole mechanical unit of world time

| Context | Relationship to time |
|---|---|
| **DWELL** | General Colony activity remains within the current Day Band. A normal Home Commitment advances the world to the next band. |
| **TRAVEL** | Direct movement consumes the current Band's projected reach. Exhausting that travel span advances one Day Band, with Rabbit bodies and present conditions determining its extent. |
| **MEET** | Time follows the action or situation being resolved; opening the decision matrix has no universal cost of its own. A completed Rest MEET or Homecoming advances one Day Band. |
| **RISK** | Crossing uses the current Day Band and traffic without adding another duration to the movement that brought the party there. |
| **EMBODY** | Ordinary life occurs within the current Day Band without becoming a time-payment action. |

- Colony conditions, Node conditions, MEET presentation, traffic, and the Field
  changing together when the Day Band changes
- The resolution changing between Home and Away while the chronology does not

### Traffic: Pattern, Threshold, and State

- Traffic behaving like weather: broadly predictable from the time of day, but
  variable in its actual expression
- Each Day Band supplying a weighted range from which the current traffic
  pattern is realized
- Volume, speed, spacing, pulse regularity, vehicle mixture, visibility, noise,
  fumes, and disruption combining to distinguish one pattern from another
- Each Day Band also permitting one named special state:

| Day Band | Eligible special state |
|---|---|
| **Morning** | **Morning Rush** |
| **Midday** | **Midday Window** |
| **Evening** | **Evening Rush** |
| **Night** | **Night Velocity** |

- A special state becoming active only when its defining threshold is reached;
  otherwise, The Highway retaining the ordinary variable traffic of that Day
  Band
- The active special state applying its modifier to the underlying traffic
  pattern rather than replacing that pattern or determining every vehicle
- The same special state therefore able to recur with materially different
  traffic on different days
- Weather, Road Work, collisions, maintenance, and other disturbances altering
  the pattern and affecting whether a threshold is crossed
- The realized pattern belonging to the world rather than to an individual
  Crossing and not being rerolled whenever the player enters or leaves RISK
- The Day Band telling the player what traffic is likely to do; observation of
  the Roadway revealing what it is doing now
- Waiting potentially producing another opportunity while spending world time
  and possibly changing light, weather, party condition, or the return margin
- Ordinary traffic and active special states affecting Crossing, River Spume,
  Roadway-adjacent Field conditions, and Field MEETs
- Exact traffic generation, thresholds, modifiers, and persistence intervals
  deferred to the later RISK chapters

### Season, Weather, and Human Disturbance

- Season changing the Corridor by accumulation; weather and human disturbance
  changing it through particular events
- Seasonal change altering vegetation, animal activity, Resource availability,
  Node recovery, routes, shelter, Colony needs, and expedition opportunity
- Similar pressures taking different seasonal forms: spring flooding, summer
  heat, autumn wind and debris, or winter cold and snow
- Green-season abundance supporting preservation, winter drawing upon what was
  saved, and the surviving surplus or shortfall shaping spring
- Seasonal preparation mattering without turning every winter day into
  emergency triage; a well-sustained Colony able to pass through ordinary
  difficult days in relative calm
- Rain, wind, heat, cold, flooding, mowing, maintenance, and Road Work affecting
  the Places, Nodes, and routes they can credibly reach
- Their effects appearing through existing play as changed TRAVEL conditions,
  altered RISK, different MEETs, threatened Places, or new DWELL work
- No separate weather economy, seasonal minigame, universal climate statistic,
  or blanket environmental penalty
- Exact season lengths, weather generation, and Sustenance accounting deferred
  to their later system chapters

### World Pressure and Civic Balance

Weather, traffic, River Spume, season, animal activity, and human disturbance
become **World Pressure** when their present effects bear upon the Colony. They
do not create one universal environmental score. Each actual circumstance may
add contextual Load to the Role axes it tests, act through relevant Places and
Practice Strength, interact with existing Readiness or Pressure, or supply the
subject of a Home MEET.

- Heavy rain able to test drainage, cultivated ground, Stores, shelter, care,
  warning, or coordination according to where the water actually goes
- Wind able to matter through coverings, routes, hanging stores, exposed
  Practices, and the Citizens who depend upon them
- Heat, cold, flood, traffic disturbance, predator movement, or human work
  locating their Load in the civic domains and physical Places genuinely
  involved
- Adequate Readiness and situated Practice Strength able to keep an ordinary
  pressure within routine DWELL, while a consequential shortfall or choice
  brings it into MEET
- The same world condition changing TRAVEL reach, Node circumstances, Rest,
  RISK, or Away MEET for the expedition experiencing it

### Road Work

Road Work is a current but deliberately undeveloped World Pressure family for
v0.5. It represents active human alteration of The Highway: lane work, barrier
repair, mowing, drainage clearance, culvert work, resurfacing, temporary
materials, machinery, and related disturbance.

- Road Work able to change traffic, River Spume, sound, vibration, light,
  drainage, vegetation, paths, Nodes, Roadway edges, and Crossing conditions
- Its physical signs able to Telegraph an approaching intervention before
  Impact
- Persistence able to leave changed ground, displaced material, obstruction,
  access, shelter, or a new situated opportunity after the workers depart
- Particular effects following the event arc and existing World Pressure,
  TRAVEL, RISK, MEET, and aftermath systems
- Exact generation, duration, work families, warning language, and mechanical
  consequences reserved for later authorial development

### Events Through Time

Environmental events unfold through a persistent four-phase arc.

| Phase | Meaning |
|---|---|
| **Telegraph** | The world shows signs of what may happen while preparation can still alter the stakes. |
| **Impact** | The pressure arrives and acts upon the preparation, Readiness, bodies, and Places already present. |
| **Persistence** | The condition continues, changes, or produces a situation requiring attention. |
| **Aftermath** | Damage, displacement, care, repair, changed routes, memory, and other consequences remain. |

- Not every phase opening MEET; a warning able to remain ambient until the
  player has a meaningful choice
- Persistence carrying an unresolved situation beyond its first MEET when the
  world has not yet changed enough to settle it
- Impact not being disguised as a leisurely decision after the event has
  already struck
- Heavy wind potentially announcing itself through bending reeds and humming
  lines before tearing an exposed covering; the storm passing while closure,
  care, repair, and memory remain
- An event not warning, striking, and repairing itself within one card; its
  consequences entering the persistent world and becoming part of its history

# PART III — HOME: COLONY, DWELL, AND EMBODY

## 3.1 Home

**Colony DWELL is MEDIAN's base-builder mode of play.** The player builds,
tends, organizes, prepares, understands, and inhabits one permanent Colony.

More precisely, **Home** is the Mode, **Colony** is its principal Register, and
**DWELL** is the operator through which the player acts upon collective life.
Together, Colony DWELL names MEDIAN's base-building experience.

### The inward Mode

- Home as the Mode in which the player's primary responsibility is the founding
  Colony
- Its direction being Inward: toward one permanent settlement, its civic
  condition, and the named lives accumulated there
- Colony and Embodiment belonging intrinsically to Home, with MEET able to bring
  a consequential Home situation into focus
- Home not being a camera, map, interface, or generic safe zone

### Four related terms

| Term | Meaning |
|---|---|
| **Home** | The Inward Mode of responsibility. |
| **Colony** | The permanent civic settlement and mechanical subject of Home play. |
| **Home Median** | The physical median occupied by the Colony. |
| **Sanctuary** | The materially, civically, and socially credible condition the Colony creates and restores. |

### One permanent center

- The founding Colony remaining the campaign's permanent center
- Growth improving, densifying, inhabiting, damaging, repairing, and remembering
  it rather than replacing it
- Outposts, Stopovers, and allied settlements never becoming
  duplicate Homes
- Corridor growth increasing the Colony's reach without moving its emotional or
  mechanical center

### Sanctuary made credible

- Sanctuary being achieved and maintained through understandable material,
  civic, and social conditions
- Sanctuary remaining relative rather than perfect: weather, scarcity, injury,
  displacement, predators, and human disturbance can still reach Home
- The player establishing and periodically restoring the conditions for
  ordinary life rather than preventing perpetual collapse
- Consequence able to enter Home without turning it into another exposure zone

### Ordinary life as the purpose

- Rest, care, work, conversation, play, ritual, relationship, and familiar
  routine as part of the civilization being built
- Stability as a successful condition rather than failed pacing
- A sufficiently sustained Colony releasing attention toward observation,
  attachment, chosen Projects, and EMBODY
- Ordinary life not being idle production Capacity

### Return changes Home

- Away mattering because particular Citizens leave a credible sanctuary
- Homecoming reintegrating material, bodily, relational, civic, and remembered
  consequences
- The Colony receiving what returned before the game becomes fully Home again
- Every return able to alter the Home from which the next departure begins

### From Home to DWELL

- Chapter 3.2 explaining how the player works upon this permanent civic subject
  through DWELL
- Later chapters explaining its Places, species placement, Roles, Practices,
  situations, resources, population, and embodied life

## 3.2 DWELL

DWELL is the ongoing stewardship of the Colony in Home. It remains open by
default: the player chooses where to look, what responsibility to sustain, and
which lasting changes justify committed effort.

### The Colony in view

- The Colony as DWELL's mechanical subject, with every named Citizen remaining
  visible within collective civic accounting
- The player understanding and arranging Home through Places, Practices, Roles,
  Projects, resources, and situated conditions
- The Colony's material, civic, and social state remaining legible both in the
  world and in concise functional form
- An elevated, freely navigable presentation expressing the Colony's state
  without defining DWELL itself

### Attention and time

- Routine information and continuing work remaining native to DWELL rather than
  seizing the camera or interrupting the player
- Inspection, reading, planning, and camera movement not advancing time
- A meaningful Home commitment advancing the shared world clock by one Day Band
- DAWN resolving the completed day's accounting and surfacing only meaningful
  change
- Persistent Colony state not implying continuous real-time advancement
- DWELL preparing the Colony for Launch and receiving its recalculated state
  after Homecoming, while those connector procedures use MEET rather than
  becoming ordinary DWELL actions

### Civic Balance: Shares, Load, Readiness, and Pressure

- **Civic Balance** tracking Core Residence and the Colony's ordinary Role
  responsibilities as separate axes rather than pooling unlike obligations
  into one capacity
- Citizens choosing whether their Civic Shares sustain ordinary Role
  responsibility or become committed to an active Project
- Each Practice carrying a separate situated strength through established
  physical purpose, Role support, and Spatial Alignment
- Practice Strength remaining distinct from passive production or
  transformation, which requires at least one usable relevant Practice and one
  Citizen sustaining its defined production Role
- Practice infrastructure never advancing a Project without committed Citizens

#### Shared balance grammar

Every Civic Balance axis compares the Capacity available to answer an
obligation with the full Load created by that obligation:

**Balance = Capacity − Load**

**Readiness = max(Balance, 0)**

**Pressure = max(−Balance, 0)**

- Load remaining the gross weight of the responsibility whether or not the
  Colony currently covers it
- A positive Balance producing Readiness, zero being **Covered**, and a negative
  Balance producing Pressure equal to the uncovered Load
- An axis with neither current Load nor Capacity being shown as **N/A** rather
  than as an obligation the player ought to fill
- Capacity and Load being compared only within their own axis, with no surplus
  in one civic domain concealing Pressure in another

#### Role Balance

- **Civic Share** as the Body-Unit-normalized measure of ordinary Home
  responsibility contributed by an available Citizen through their chosen Role
- Each Rabbit, Squirrel, and v0.5 Guest Citizen contributing one Civic Share
- Each Mouse Citizen contributing one-half Civic Share, so two Mice provide one
  standard unit of aggregate civic contribution
- Civic Share measuring Colony-scale contribution rather than citizenship,
  authority, aptitude, or personal worth
- Load as the weight placed upon the Colony by growth and expansion, including
  additional population, dependency, inhabited ground, Practices, routes,
  stores, and other added obligations that must be sustained
- Each Citizen sustaining the relevant Role contributing their full Civic Share
  against its Load
- Personality, prior service, Away capability, equipment, and personal history
  never changing the value supplied by the Citizen's species Body Unit
- A Citizen who is Away, unavailable, sustaining another Role, or committed to a
  Project not contributing that Civic Share against the present Role's Load
- Each Role retaining its own balance:

  **Role Balance = sustaining Civic Shares − Role Load**

#### Housing Balance

- Every Core Species Citizen creating Housing Load according to Body Units
- Each completed usable Core Residence providing two Body Units of Housing
  Capacity
- A Well-Placed Core Residence providing three Body Units instead, a fifty-percent
  Spatial Alignment bonus
- Rabbit and Squirrel Citizens each occupying one Body Unit, so one Residence
  accommodates two of them, or three when Well Placed
- Mouse Citizens each occupying one-half Body Unit, so one Residence
  accommodates four of them, or six when Well Placed
- Core Housing retaining its own balance:

  **Housing Balance = usable Core Residence Capacity − Core Citizen Housing Load**

- Positive Housing Balance becoming **Housing Readiness** and zero being Covered
- The magnitude of negative Housing Balance becoming **Housing Pressure**
- A Core Residence that loses capacity leaving its Citizens in place, with each
  uncovered Body Unit contributing Housing Pressure rather than causing eviction
- Guest housing remaining outside Core Housing Balance and occupying a dedicated
  Place whose requirements belong to the individual Guest species

#### Readiness and Pressure

- Positive Role Balance becoming that Role's **Readiness**: Civic Shares beyond
  what its ordinary responsibility presently requires
- Zero Role Balance being **Covered**: that Role's ordinary responsibility met
  without surplus Readiness
- Negative Role Balance becoming that Role's **Pressure**: uncovered
  responsibility within that civic domain
- An unstaffed Role with no present contextual Load being N/A rather than
  requiring an artificial assignment merely to keep its category filled
- Readiness and Pressure remaining attached to their Roles, so surplus in one
  domain never conceals a shortfall in another
- Readiness supporting ordinary stability and deliberate response without
  guaranteeing immunity from events or consequence

#### Capacity and materials

- Civic Capacity answering routine Load without consuming stock merely because
  the responsibility exists
- Covered responsibility representing the ordinary acts through which a
  Practice and Role sustain daily life
- Resources enabling Projects and preparation, protecting stakes during MEET,
  and supporting recovery without purchasing exemption from Civic Load or
  replacing sustaining Citizens

#### Civic Pressure, World Pressure, and Colony Pressure

- Current Housing Pressure and the separate Role Pressures forming the Colony's
  **Civic Pressure profile** without being summed into one civic balance
- **World Pressure** describing the external corridor conditions that may add
  contextual Load, test Readiness, alter ordinary life, or supply the
  circumstance for a Home situation
- **Colony Pressure** as the hidden, momentary director calculation that weighs
  the separate Civic Pressure profile against current World Pressure, internal
  circumstances, depth and persistence, bounded randomness, and recent Home
  MEET history
- Colony Pressure influencing when circumstances develop into situations
  requiring attention without becoming a stored civic value, player-visible
  score, or predictable incident counter
- The greatest relevant Role shortfall determining a situation's primary civic
  stake
- Prominent Housing Pressure locating a situation in the affected Residence and
  Citizens while the relevant Role profile determines its civic stakes
- A second relevant shortfall determining its collateral civic stake when one
  exists
- A situation with no meaningful second Role drawing its collateral stake from
  the actual Citizen, Place, Practice, relationship, resource, or environmental
  circumstance involved
- Role shortfalls being ranked by absolute uncovered Load, with the physical
  circumstances resolving ties
- Pressure creating vulnerability rather than inflicting automatic daily
  damage

#### Practice Strength

- Each completed usable Practice carrying a **Practice Strength** score when a
  situation occurs through or meaningfully involves it
- An unsupported Practice contributing one-half point of Practice Strength
- A Practice supported by at least one full compatible Civic Share in ordinary
  Role responsibility contributing one point instead
- A Well-Placed Practice contributing one additional Spatial Alignment point
- Practice Strength therefore being 0.5, 1, 1.5, or 2 according to Role support
  and placement
- Compatible Civic Shares aggregating automatically across Citizens and Roles,
  with no player-created link or Mouse pairing
- One sustaining Mouse satisfying a defined process's requirement for an actual
  Citizen while contributing one-half Civic Share; full Practice support still
  requiring one aggregate compatible Civic Share
- A shared Practice carrying one Practice Strength for the whole situation,
  never multiplying its contribution by the number of relevant Roles
- Situated Practice Strength, relevant Role Readiness, preparation, resources,
  and Signatures helping determine whether an environmental test remains an
  ordinary report or requires a Home MEET
- Practice Strength not erasing Role Load in the standing civic ledger

#### Civic choice and Projects

- Each available Citizen directing their Civic Share either to ordinary Role
  responsibility or to an active Project, never to both simultaneously
- A Civic Share committed to a Project advancing that defined persistent change
  while ceasing to counter its Role Load, support a compatible Practice, or
  support passive throughput
- Several Citizens in one Role able to divide their Civic Shares between
  ordinary responsibility and Projects
- A usable Practice continuing to provide its situated Practice Strength while
  accommodating a Project, recalculated according to whatever compatible
  ordinary Role support remains
- Project progress always requiring at least one committed Citizen regardless of
  available Practice infrastructure

#### Passive production and transformation

- Passive production or transformation existing only where a Role and Practice
  define a specific output
- Output being zero unless at least one usable relevant Practice and one Citizen
  sustaining its defined production Role are both present
- Each usable relevant Practice contributing one yield chunk
- Each Civic Share sustaining the defined production Role contributing one
  yield chunk
- Each Well-Placed relevant Practice contributing one additional half chunk
- Ordinary throughput following the shared relationship:

  **Passive Throughput = usable relevant Practices + sustaining Civic Shares + (0.5 × Well-Placed relevant Practices)**

- One usable Poorly Placed Practice and one full sustaining Civic Share
  therefore producing two yield chunks, or two and one-half when that Practice
  is Well Placed
- One Mouse sustaining the production Role contributing one-half Civic Share,
  so the same Poorly Placed Practice produces one and one-half yield chunks;
  two Mice restore the two-chunk standard
- Fractional throughput accumulating within its defined process until it forms
  a whole yield chunk
- DAWN releasing only whole chunks to Colony stock and carrying the remainder
  forward; throughput of 1.5 therefore releasing one chunk on its first DAWN,
  two on its second, then repeating that cadence
- Citizens committed to Projects not contributing to passive throughput
- Available inputs, player targets and reserves, seasonal conditions, and
  situated modifiers constraining or modifying output only after ordinary
  throughput has been established
- The shared relationship not inventing passive output for a Role or Practice
  that defines none

### Quiet and consequential attention

- A well-sustained Colony remaining in DWELL without compulsory intervention
- Pressure remaining ordinary Colony information until a bounded situation
  requires judgment
- MEET beginning when stakes, choice, and consequence bring that situation into
  focus
- Quiet Equilibrium as Home's sole tracked condition, active while the Colony's
  ordinary obligations are covered and no acute situation demands attention
- Quiet Equilibrium opening EMBODY while active and closing EMBODY when lost,
  without becoming a resource or reward
- Observation and voluntary Projects remaining available independently of
  Quiet Equilibrium

## 3.3 Places and Species Placement

A **Place** is physical ground designated within Home. A Builder designates that
ground at zero cost. A vacant designation may be withdrawn freely; committing
its first Residence or Practice Project establishes the Place permanently. An
established Place may stand vacant, host one Core Residence, host one Guest
residence, or host one Practice. A Guest species may depart from this default
only through an explicit authored exception. Species placement determines how
efficiently an established use serves the Colony.

### Place uses

- An established Place carrying its location, footprint, physical condition,
  species-spatial relationship, and intended or established use
- A Practice Place taking its functional name from the Practice situated there
  rather than receiving a separate building-type name
- A Place hosting no more than one Core Residence, Guest residence, or Practice
  except where a Guest species explicitly permits its Residence to be
  incorporated into a particular Practice
- The same Practice retaining one civic function wherever it is placed and
  whichever Core Species builds it
- An established Place able to remain vacant or carry an unfinished, usable,
  damaged, adapted, or transformed Residence or Practice
- Displacement and other lasting physical consequences remaining attached to
  the persistent Place
- An established Place able to change use or stand vacant without ever being
  erased back into neutral ground
- A Place not leveling up or changing automatically; development making a
  specific new physical fact true there

### Builder designates Places

- Builder as the Role through which the player designates every Place
- Designation committing ground without requiring a Project or consuming
  material, Civic Shares, or time
- A vacant designation remaining freely withdrawable and providing no Practice
  Strength, Housing Capacity, passive output, or transformation by itself
- Establishing a Residence or Practice at that Place requiring a Builder Project
  that commits Builder Citizens, appropriate material, and time
- Commitment of that first Project making the Place permanent whether or not
  the Project has yet been completed
- The first Workshop as the sole Practice-establishment bootstrap exemption,
  with its founding Project still requiring committed Builder Citizens,
  material, and time
- Every other Practice, including Gathering Place, following the ordinary
  Builder Project rule
- An unfinished Residence contributing no Housing Capacity and an unfinished
  Practice contributing no Practice Strength, passive output, or transformation
- Completion making a Residence or Practice usable, after which the Residence
  provides Housing Capacity or compatible Role support may strengthen the
  Practice's civic purpose
- Builder designating the ground and making the physical fact without owning the
  completed Practice or replacing the Role responsible for it
- Later adaptation belonging to the Role whose persistent result it serves;
  physical Builder involvement not transferring ownership from that Role

### Core Residence

- Residence as an inhabited use of Place rather than a Practice or building-type
  family
- Each completed usable Core Residence providing two Body Units of Housing
  Capacity
- A Well-Placed Core Residence providing three Body Units of Housing Capacity
- Core Housing Capacity answering the Housing Load of accepted Citizens rather
  than granting or withholding citizenship
- Insufficient Housing Capacity creating Housing Pressure without preventing an
  arrival, removing belonging, or evicting any Citizen
- Rabbit and Squirrel Residences therefore accommodating two Citizens, or three
  when Well Placed
- Mouse Residences therefore accommodating four Citizens, or six when Well
  Placed
- Residence contributing no Practice Strength, passive output, or Project
  capacity
- Guest housing occupying a dedicated Place apart from Core Species Residences,
  with any authored Practice-sharing exception defined by the Guest species
- A Guest residence following its individual species' bodily and spatial housing
  requirements rather than contributing to pooled Core Residence Capacity
- Guest Residence Fit being defined with the Guest species in Chapter 4.3

### Species placement

- Every completed usable Core Residence and Practice Place being either **Well
  Placed** or **Not Well Placed** according to how its relationship to
  surrounding Colony ground expresses the Colony's Core Species spatial
  operator
- Mouse **JOIN** emphasizing contact, enclosure, adjacency, and accumulated
  nearness
- Rabbit **GATHER** emphasizing open common space, mutual visibility,
  neighborhood scale, and protective edges
- Squirrel **CONNECT** emphasizing reachable nodes, elevation, alternate routes,
  anchors, and redundancy
- Placement being assessed from the Place's spatial relationship rather than
  from a species-themed building skin
- A Practice remaining the same Practice when built by another Core Species,
  while its physical expression and placement test change
- Core Residence expressing the same Body Unit capacity through species form:
  Mouse joining a room, Rabbit completing or budding a court, and Squirrel
  adding and securing a node
- A Guest residence being Well Placed or Not Well Placed according to the
  housing requirements of its individual Guest species

### Spatial Alignment

- A Well-Placed Place contributing one Spatial Alignment point to the Practice
  situated there
- A Not-Well-Placed Place contributing no Spatial Alignment unit rather than
  imposing a separate numerical penalty
- A Well-Placed Core Residence increasing its Housing Capacity from two to three
  Body Units
- Spatial Alignment adding one full point to situated Practice Strength, making
  species-conforming placement a significant source of civic resilience
- Where the Practice defines passive production or transformation, its Spatial
  Alignment unit also contributing to ordinary throughput
- Spatial Alignment contributing only through a completed usable Practice and
  never replacing the required Practice-and-Citizen production gate
- Well-Placed status recalculating as the completed usable layout of Home changes,
  while vacant designations have no effect upon it
- Colony evolution therefore able to improve or degrade Spatial Alignment, as
  when later growth obscures the central court upon which a Rabbit Place relies
- The interface previewing alignment and capacity changes before the player
  commits the Project that would cause them
- Lost Core Residence Capacity creating Housing Pressure without ever evicting
  a Citizen
- Placement also shaping access, adjacency, resilience, exposure, circulation,
  and failure geometry without creating a parallel species-specific civic
  system

### Place development

- Sustained use, seasonal experience, civic need, consequence, or another
  concrete change in the world able to make a specific Place improvement
  evident
- A Guest able to bring the understanding needed for an improvement, and the
  Rest-Stop Metropolis able to reveal it through an appropriate relationship or
  MEET
- Such understanding becoming a direct, persistent possibility for the Colony
  rather than a Knowledge resource or progression track
- A Home MEET presenting that possibility when it warrants interpretation,
  competing commitments, or a meaningful choice
- Recognition of the possibility never completing the improvement by itself
- A Role-owned Project making the improvement real whenever lasting physical or
  civic work is required
- Completion changing only the particular Place involved rather than every
  Residence or Practice of the same kind
- An improvement adapting the Place's existing Residence or Practice without
  adding a second hosted use
- Every Practice supporting at least one authored improvement over the course of
  the campaign
- Practice improvements normally adding a specific capability, response, range,
  or form of resilience rather than a generic increase to throughput, Practice
  or Project capacity
- Winter Cultivation as the defined Garden improvement: a Gardener Project
  physically adapting one Garden for limited winter production

## 3.4 Roles and Practices

The Civic Balance established in Chapter 3.2 governs every Role and Practice
below. Sustaining Civic Shares cover the Load of their Roles. Completed
Practices provide situated Practice Strength according to compatible Role
support and placement. Project commitment withdraws Citizens and their Civic
Shares from ordinary responsibility, Practice support, and passive output.

### Roles and their Practices

Each Role is first established through its civic responsibility, ordinary
contribution, related Practices, characteristic Projects, vulnerabilities, and
limits. Shared Practices appear under every Role that uses them and are
identified together after the Role entries so that none appears to belong to
the first Role that uses it.

| Role | Practices |
|---|---|
| **Builder** | Workshop |
| **Gardener** | Garden |
| **Crafter** | Workshop |
| **Caretaker** | Hearth; Kitchen |
| **Healer** | Hearth |
| **Teacher** | Gathering Place; Hearth |
| **Watchkeeper** | Watchpost |
| **Leader** | Gathering Place |

### Builder

- Builder carrying responsibility for the physical soundness and deliberate
  transformation of Home
- Every available Citizen assigned Builder contributing their full Civic Share,
  without personality, prior service, Away capability, or equipment changing
  that Body-Unit-normalized contribution
- **Workshop** as Builder's principal Practice
- Workshop naming the Practice, and therefore the land committed to that civic
  purpose, rather than a separate production-building type
- Workshop Practice Strength representing prepared material, protected working
  ground, established methods, suitable access, and accumulated physical order
  rather than autonomous labor
- At least one full Civic Share sustained through Builder supporting completed
  usable Workshops without requiring a separate assignment among Citizens
- A Builder committed to a Project withdrawing that share from ordinary
  Readiness and applying it to the Project
- Several Builders therefore able to divide present effort between structural
  Readiness and deliberate change
- Workshop continuing to provide situated Practice Strength while supporting a
  Project, recalculated according to remaining compatible Role support
- Workshop unable to advance a Project without committed Citizens
- Other Practices able to create structural obligations or receive Builder
  Projects without becoming additional Builder Practices

#### The first Workshop

- The Colony able to undertake the Project establishing its first Workshop
  without an existing Workshop, avoiding a circular prerequisite
- The founding Project still requiring material, time, and committed Builder
  Citizens
- The unfinished Workshop contributing no Practice Strength
- Completion ending the founding permission automatically
- Each completed Workshop thereafter supporting one active Project
- The first Workshop establishing situated structural support beyond the
  Colony's Civic Shares alone

#### Standing responsibility

- Builder Readiness expressing whether the Colony can keep its inhabited
  physical world sound under present conditions
- Ordinary Builder work including small structural corrections, coverings,
  lashings, retaining earth, protected openings, drainage, access, route
  anchors, passages, and connections
- Covered structural obligations meaning that Home does not deteriorate merely
  because time passes; Builders are already performing ordinary upkeep
- Structural soundness remaining a Colony posture rather than a separate repair
  order for every wall, chamber, ladder, court edge, covering, drain, or route

#### Builder Projects

- Builder Projects committing named Citizens to make a defined physical fact
  newly true
- Establishing a Residence or Practice at a designated Place; reinforcing
  shelter, access, drainage, routes, or anchors; restoring major structural
  damage; and completing major physical or Tier-defining work
- The receiving Residence or Practice remaining the subject of the change: a
  Builder Project may alter Hearth, Garden, Gathering Place, Watchpost,
  Workshop, Residence, or another established use without creating a separate
  Builder facility inside it
- Projects consuming committed Citizen effort and appropriate material
- Builder shares committed to Projects not simultaneously contributing to
  ordinary Builder Readiness
- Growth therefore asking the Colony to risk some present structural assurance
  in order to make a lasting improvement

#### Structural vulnerability

- Insufficient Builder Readiness creating vulnerability rather than automatic
  daily damage
- Relevant pressure including heavy wind, flood or failed drainage, softened or
  frost-heaved ground, damaged coverings or anchors, broken access, structural
  overextension, and persistent damage requiring restoration
- MEET localizing consequential structural vulnerability to actual inhabited
  ground such as a room, court edge, roofline, route, opening, anchor, or
  Practice
- Resolution ordinarily completing the immediate transaction rather than
  generating a redundant compulsory repair task
- A restoration Project following only when a persistent physical result
  genuinely remains unfinished

#### Boundaries

- Builder not becoming a personal construction statistic, superior class of
  Citizen, local repair-click system, generic Project-speed bonus, source of
  passive construction, immunity from weather, or building-durability meter
- Tool-making remaining Crafter's responsibility even though Tools require
  physical material
- Guest Signatures able to reveal hidden structural circumstances or open a
  better response without replacing Builder responsibility or performing
  Projects without Citizens

### Gardener

- Gardener carrying responsibility for cultivation, seasonal yield, and the
  continuing health of cultivated ground
- Every available Citizen assigned Gardener contributing their full Civic Share,
  without personality, prior service, Away capability, or equipment changing
  that Body-Unit-normalized contribution
- **Garden** as Gardener's Practice and the ground that enables ordinary
  Gardener production
- Gardener Citizens choosing whether to sustain ordinary Gardener
  responsibility or commit their Civic Shares to active Projects

#### Garden

- Garden naming the Practice, and therefore the land committed to cultivation,
  rather than a separate production-building type
- A Builder ordinarily establishing a Garden through a Builder Project after
  the first Workshop has been completed
- Garden receiving no founding or bootstrap exemption
- An unfinished Garden contributing no Practice Strength and producing no
  Sustenance
- Garden Practice Strength representing committed ground, established
  cultivation, protected growth, prepared soil, suitable access, and
  accumulated order rather than autonomous labor
- At least one full Civic Share sustained through Gardener supporting completed
  usable Gardens without requiring a separate assignment among Citizens
- Garden unable to produce Sustenance without at least one sustaining Gardener

#### Passive production

- Passive production requiring at least one completed usable Garden and one
  Citizen sustaining Gardener; if either is absent, production being zero
- Each usable Garden and each Civic Share sustaining Gardener contributing one
  Sustenance chunk, with each Well-Placed Garden adding one-half chunk
- Normal production following the relationship:

  **Perishable Sustenance = usable Gardens + sustaining Gardener Civic Shares + (0.5 × Well-Placed Gardens)**

- During green seasons, one usable Not-Well-Placed Garden and one full
  sustaining Gardener Civic Share producing two Perishable Sustenance chunks
  at the ordinary DAWN cadence, or two and one-half when that Garden is Well
  Placed
- Two Well-Placed Gardens and one Not-Well-Placed Garden sustained by two
  full Gardener Civic Shares therefore producing six Perishable Sustenance
  chunks
- Gardener Citizens committed to Projects withdrawing their civic shares from
  ordinary yield
- Seasonal and situated modifiers applying only after normal production has
  been determined
- Suitable managed Nodes and Sustenance-bearing Outposts able to provide bounded
  situated additions or modifiers without counting as Practices or bypassing
  the Garden-Gardener production gate

#### Standing responsibility

- Gardener Readiness expressing whether the Colony can sustain cultivated
  ground and expected seasonal yield under present conditions
- Ordinary Gardener work including planting, tending, gathering, protecting
  growth, maintaining soil, responding to ordinary heat or rain, and preserving
  cultivated continuity between yields
- Covered Gardener responsibility preserving Garden condition and next-season
  readiness even when the current season permits no ordinary production
- Cultivation remaining Colony-scale stewardship rather than per-plot staffing,
  individual harvest orders, or simulated routes between Gardens

#### Winter Cultivation

- An ordinary Garden producing no regular Perishable Sustenance in winter
- **Winter Cultivation** as a learned Practice requiring both a physically
  adapted Garden and sustaining Gardener coverage
- Learning Winter Cultivation not producing food or adapting every Garden
  automatically
- Each Garden becoming winter-capable only through its own Gardener Project and
  remaining otherwise unchanged
- Eligible winter production equaling one-quarter of normal production after
  the ordinary Garden-Gardener gate has been satisfied
- Winter yield using the shared fractional-throughput accumulation rule

#### Gardener Projects

- Gardener Projects committing named Citizens to make a defined cultivation
  fact newly true rather than performing routine yield
- Establishing a cultivated line; restoring persistently damaged ground;
  adapting one Garden for Winter Cultivation; reshaping a Garden for a newly
  understood use; or creating another lasting seasonal or ecological change
- Routine planting, tending, gathering, and green-season yield not automatically
  becoming Projects
- Gardener shares committed to Projects not simultaneously contributing to
  passive production or ordinary Gardener Readiness
- Workshop and Builder involvement able to establish or physically alter Garden
  without transferring its continuing cultivation purpose away from Gardener

#### Gardener vulnerability

- Insufficient Gardener Readiness creating vulnerability to drought, heat,
  washout, crop loss, poor yield, damaged soil, lost cultivated continuity, and
  winter shortage
- Gardener shortfall not creating food independently, concealing the explicit
  production gate, or requiring every Garden to suffer separately
- Consequential shortfall becoming situated through MEET at the actual Garden,
  family, reserve, or threatened part of Home

#### Boundaries

- Gardener not becoming a personal cultivation statistic, superior class of
  Citizen, autonomous farming system, per-Garden worker assignment, harvest
  queue, or source of winter yield without learned and physically established
  support
- Passive production applying only to the defined Perishable Sustenance output
  and not inventing an output for every Gardener activity or Practice
- Guest Signatures able to alter cultivation circumstances or open a lasting
  Garden Project without creating superior Gardener coefficients or bypassing
  the Garden-Gardener production gate

### Crafter

- Crafter carrying responsibility for transforming recovered material into
  functional civic and Away capability
- Every available Citizen assigned Crafter contributing their full Civic Share,
  without personality, prior service, Away capability, or equipment changing
  that Body-Unit-normalized contribution
- **Workshop** supporting both Crafter and Builder responsibility without
  becoming a separate building type or requiring Citizens to be assigned to an
  individual Workshop
- Crafter Citizens choosing whether to sustain ordinary Crafter responsibility
  and Supply Preparation or commit their Civic Shares to Tools and other active
  Projects

#### Workshop

- Workshop Practice Strength representing protected working ground, organized
  material, established methods, suitable access, and accumulated physical
  order rather than autonomous fabrication
- At least one full Civic Share sustained across Builder and Crafter supporting
  completed usable Workshops without multiplying their Practice Strength
- Workshop requiring no Crafter bootstrap exemption because Builder establishes
  the first Workshop through the founding Builder permission
- One Workshop supporting no more than one active Project at a time, whether
  that Project's principal purpose belongs to Builder, Crafter, or another Role

#### Supply Preparation

- **Supply Preparation** as ordinary transformation rather than an item-by-item
  Project queue
- Passive Supply Preparation requiring at least one completed usable Workshop
  and one Citizen sustaining Crafter; if either is absent, transformation being
  zero
- Each usable Workshop and each Civic Share sustaining Crafter contributing one
  yield chunk, with each Well-Placed Workshop adding one-half chunk
- Normal transformation following the relationship:

  **Supply Preparation = usable Workshops + sustaining Crafter Civic Shares + (0.5 × Well-Placed Workshops)**

- Supply Preparation consuming appropriate Sustenance, Flexible Scrap, Rigid
  Scrap, or other defined inputs according to known class recipes
- Output remaining bounded by available ingredients, known recipes, and
  player-set targets and reserves, and never creating Supplies from nothing
- Crafter producing Binding, Device, and Offering Supplies while Remedies remain
  Healer's responsibility
- Prepared Supplies remaining anonymous expedition resources rather than named
  possessions or records of their maker
- Crafter Citizens committed to Projects withdrawing their civic shares from
  ordinary Supply Preparation and Crafter Readiness

#### Standing responsibility

- Crafter Readiness expressing whether the Colony can maintain ordinary
  functional material capability under present conditions
- Ordinary Crafter work including sorting recovered matter, maintaining common
  working methods, preparing bounded Supplies, preserving usable material, and
  making credible substitutions during routine pressure
- Covered Crafter responsibility supporting ordinary capability without
  passively manufacturing permanent Tools or advanced expedition solutions
- Fabrication remaining Colony-scale civic work rather than simulated benches,
  maker aptitude, component inventories, or individual production percentages

#### Tools and Crafter Projects

- Tools as deliberate durable Away-function Items rather than incidental or
  passive output
- Making a Tool requiring a Crafter Project that consumes appropriate Scrap,
  time, a usable Workshop, and committed Crafter Citizens
- Ordinary Tool maintenance and repair remaining part of Crafter responsibility
- Transformative restoration or adaptation of a Tool requiring a Crafter
  Project only when it makes a new persistent fact true
- Other Crafter Projects including adapting Workshop to a newly understood use,
  establishing a lasting fabrication capability, creating a defined civic
  artifact, or producing components for a larger persistent change
- Crafter Projects making a defined material fact newly true rather than
  keeping a queue full for its own sake
- Physical collaboration with Builder or another Role not transferring a
  Project's principal purpose away from the Role whose persistent result it
  serves

#### Fine Work

- **Fine Work** as the defined Workshop improvement, established in one
  particular Workshop through a Crafter Project
- Fine Work opening **Specialist Tools** as a second Tool tier
- Each Specialist Tool granting one specific authored capability unavailable to
  the five ordinary Tool classes rather than increasing a percentage or generic
  Tool power
- A Specialist Tool design able to become known through a Guest, the Rest-Stop
  Metropolis, or another direct world source
- Each known Specialist Tool requiring its own recipe and Crafter Project at a
  Workshop improved for Fine Work
- Specialist Tools remaining persistent, individually held, one-slot personal
  Tools
- A Specialist Tool being reproducible once understood, distinguishing it from
  a singular Special Artifact
- Fine Work not increasing Supply Preparation, Practice Strength, or Project
  capacity

#### Crafter vulnerability

- Insufficient Crafter Readiness creating vulnerability to unavailable
  Supplies, tool failure, disordered or unusable material, failed substitution,
  and inability to answer a situated material need
- Crafter shortfall not automatically consuming stored material, breaking Tools
  on a daily schedule, or generating a compulsory stream of fabrication chores
- Consequential shortfall becoming situated through MEET, an active Project, a
  particular Tool, or the actual Place and civic need under pressure

#### Boundaries

- Crafter not becoming a personal fabrication statistic, generic Project-speed
  bonus, industrial production line, per-bench worker assignment, component
  taxonomy, or source of infinite value from quiet Home time
- Passive transformation applying only to defined Binding, Device, and Offering
  Supply Preparation and not to Tools, Keepsakes, Special Artifacts, or every
  Crafter activity
- Tools remaining made for work rather than violence, even when their physical
  functions provide narrow contextual utility during danger
- Guest Signatures able to reveal material possibilities or open a distinctive
  response without creating superior Crafter coefficients, bypassing recipes,
  or producing Tools outside Projects

### Caretaker

- Caretaker carrying responsibility for receiving, provisioning, nurturing,
  and preserving ordinary life
- Every available Citizen assigned Caretaker contributing their full Civic
  Share
- Caretaker Citizens choosing whether to sustain ordinary Caretaker
  responsibility or commit their Civic Shares to active Projects

#### Hearth

- **Hearth** as the foundational shared Practice of nurture, dependency, and
  recovery
- Caretakers using Hearth to feed, settle, clean, comfort, and support vulnerable
  Citizens; receive injured or exhausted returnees; care for young Citizens and
  Patients between specialized treatment or teaching; and help displaced,
  newly arrived, or dependent Citizens enter ordinary life
- Hearth drawing upon Caretaker, Healer, and Teacher Readiness as its needs
  require

#### Kitchen

- **Kitchen** as a later expansion dedicated to preservation and Provisioning
- Kitchen Practice Strength representing preserved working ground, protected
  provisions, established methods, and physical organization rather than
  autonomous labor
- Kitchen supporting Perishable-to-Durable preservation, ordinary Sustenance
  preparation, organization and protection of reserves, family
  provisioning, seasonal preparation, and recovery from disrupted provisions
- Passive preservation requiring at least one completed usable Kitchen and one
  Citizen sustaining Caretaker; if either is absent, preservation being zero
- Each usable Kitchen and each Civic Share sustaining Caretaker contributing
  one yield chunk, with each Well-Placed Kitchen adding one-half chunk
- Normal transformation following the relationship:

  **Preservation Throughput = usable Kitchens + sustaining Caretaker Civic Shares + (0.5 × Well-Placed Kitchens)**

- Preservation remaining bounded by available Perishable Sustenance, known
  methods, and player-set targets and reserves, and never creating food from
  nothing
- Herbal or cultural knowledge able to qualify or modify preservation without
  replacing the required Kitchen or sustaining Caretaker
- Caretaker Citizens committed to Projects withdrawing their Civic Shares from
  passive preservation
- Preservation operating through Provisioning rather than a queue of individual
  Projects or orders for every bundle, cache, reserve, or meal
- Kitchen requiring no founding exemption because Caretaking already exists
  through Hearth before the Colony undertakes the Project establishing Kitchen
  as a dedicated expansion

#### Receiving

- Receiving remaining a Caretaker responsibility rather than a separate
  Practice
- Homecoming, hospitality, displacement, and aftermath able to ask Caretakers
  to receive returning Citizens, food and ordinary material, Guests or
  Wanderers, Patients, threatened reserves, displaced inhabitants, or
  questionable goods
- The situation resolving through Hearth, Kitchen, Residence, Homecoming, or
  MEET according to what is being received
- Colony Stock remaining abstract civic inventory whose physical expression may
  appear as pantries, caches, wrapped reserves, Residence stores, or protected
  holdings without creating a Stores Practice

#### Caretaker Projects

- Caretaker Projects creating persistent changes rather than performing routine
  care
- Adapting Kitchen or Hearth for a lasting care need; establishing a new
  preservation function within an existing Kitchen; reorganizing reserves after
  permanent loss or growth; completing lasting resettlement; or creating a
  durable seasonal preparation beyond ordinary Provisioning
- Evacuation, ordinary stock movement, immediate receiving, routine
  preservation, and changes to Provisioning targets or reserves not
  automatically becoming Projects

#### Open Table

- **Open Table** as the defined Kitchen improvement, established in one
  particular Kitchen through a Caretaker Project
- A completed usable Open Table Kitchen opening **Shared Meal**, a rare
  whole-Colony EMBODY opportunity while Quiet Equilibrium keeps EMBODY open
- Shared Meal allowing the player to be with the Colony together through food,
  service, conversation, proximity, and the species-specific use of common
  space
- Arrivals, Homecomings, recovery, seasonal observance, grief, celebration, and
  recent shared history able to shape the experience without turning it into a
  consequential MEET
- Shared Meal drawing upon ordinary Colony Sustenance rather than creating a
  separate prepared item, Feast currency, or additional economic reward
- Open Table not resolving Guest Terms, disagreement, injury, or civic Pressure
  merely by gathering the Colony
- Open Table not increasing Preservation Throughput, Practice Strength, or
  Project capacity

#### Caretaker vulnerability

- Insufficient Caretaker Readiness creating vulnerability to spoilage,
  inaccessible or disordered reserves, crowding, displacement, failed
  receiving, unmet dependency, family disruption, and insufficient winter
  preparation
- Caretaker shortfall not inflicting automatic daily harm upon named Citizens
- Consequential shortfall becoming situated through MEET

#### Boundaries

- Caretaker not becoming a generic domestic worker, anonymous food-production
  unit, replacement for Healer or Teacher, automatic immunity from spoilage or
  displacement, per-Residence simulation, or queue of meals, preservation
  batches, and chores
- Caretaker not owning Hearth exclusively
- Caretaker Civic Shares supporting ordinary responsibility across Hearth and
  Kitchen without requiring assignment to either Practice
- Resident Signatures able to change how a particular threat is understood or
  received without replacing Caretaker responsibility

### Healer

- Healer carrying responsibility for medical readiness, particular Patients,
  recovery, and the bodily aftermath of exposure
- Every available Citizen assigned Healer contributing their full Civic Share,
  without personality, prior service, Away capability, or equipment changing
  that Body-Unit-normalized contribution
- **Hearth** as Healer's primary Practice and the shared civic ground through
  which treatment and recovery enter ordinary life
- Healer Citizens choosing whether to sustain ordinary Healer responsibility,
  answer a particular treatment need, or commit their Civic Shares to active
  Projects, including Wound Recovery

#### Care through Hearth

- Hearth belonging exclusively to the civic Practice of care and nurture rather
  than naming a family unit
- Hearth drawing upon Healer Readiness when injury, illness, exposure,
  rehabilitation, or bodily aftermath requires specialized care
- Caretaker and Teacher Readiness entering the same Practice according to
  actual need without substituting for Healer responsibility
- Hearth Practice Strength representing prepared recovery ground, clean
  shelter, established methods, suitable access, and accumulated order rather
  than autonomous treatment
- A Colony without Patients or relevant health pressure having no automatic
  Healing Load merely because the Role exists
- Named Patients, consequential treatment, incapacity, and recovery remaining
  individually legible while Healer Load and Readiness remain Colony-scale
  civic accounting

#### Remedy Preparation

- **Remedy Preparation** as Healer's defined passive transformation within
  ordinary Provisioning
- Passive Remedy Preparation requiring at least one completed usable Hearth and
  one Citizen sustaining Healer; if either is absent, transformation being zero
- Each usable Hearth and each Civic Share sustaining Healer contributing one
  yield chunk, with each Well-Placed Hearth adding one-half chunk
- Normal transformation following the relationship:

  **Remedy Preparation = usable Hearths + sustaining Healer Civic Shares + (0.5 × Well-Placed Hearths)**

- Remedy Supplies consuming Sustenance and Flexible Scrap according to known
  recipes and remaining bounded by available inputs and player-set targets and
  reserves
- Remedy Supplies remaining distinct from the ordinary non-Remedy Supplies
  prepared by Crafters
- Caretaker and Teacher Civic Shares aggregating with compatible Hearth support
  without counting as Healers for Remedy Preparation
- Healer Citizens committed to Projects withdrawing their civic shares from
  ordinary care, Healer Readiness, and Remedy Preparation

#### Standing responsibility

- Healer Readiness expressing whether the Colony can meet present health and
  recovery needs without allowing bodily consequence to become civic collapse
- Ordinary Healer work including diagnosis, cleaning and stabilizing injury,
  managing illness, guiding recovery, preparing Remedies, and receiving the
  bodily aftermath of Homecoming or Home MEET
- Adequate Healer Readiness supporting recovery without erasing wounds,
  Maiming, incapacity, or the historical consequence attached to a named life
- Healing remaining credible care over time rather than an instant restoration
  command, generalized health meter, or immunity from future harm

#### Healer Projects

- Healer Projects creating persistent care capability or changing a lasting
  health circumstance rather than turning every treatment into construction
- Adapting Hearth to a newly understood need; establishing a durable treatment
  or recovery capability; restoring care after persistent contamination or
  displacement; recovering a named Citizen from Wound; or completing a lasting
  rehabilitation change
- Immediate treatment, field stabilization, Remedy Preparation, triage, and
  care that does not recover Wound not automatically becoming Projects
- Builder, Crafter, Caretaker, or Teacher involvement able to support a
  persistent care change without transferring its principal purpose away from
  Healer

#### Rehabilitation

- **Rehabilitation** as the defined Hearth improvement, established in one
  particular Hearth through a Healer Project
- The improved Hearth providing protected movement space, bodily supports, and
  sustained care arrangements through which wound or Maiming amelioration may
  become available
- Rehabilitation Projects being individualized to a named Citizen and the
  lasting consequence they carry
- Amelioration able to establish an adapted way to move, work, communicate, or
  eventually Launch where that Citizen's condition permits
- Rehabilitation not guaranteeing restoration of former capability, erasing
  Maiming, removing history, or accelerating ordinary recovery
- Healer owning each Rehabilitation Project, with Caretaker and Teacher
  Readiness contributing when the Citizen's actual needs require them and
  Leader contributing none
- One improved Hearth accommodating no more than one Rehabilitation Project at
  a time under the ordinary Project-capacity rule
- Detailed bodily and personal outcomes belonging to Chapter 4.4

#### Healer vulnerability

- Insufficient Healer Readiness creating vulnerability to delayed recovery,
  untreated injury or illness, exhausted care, inadequate Remedies,
  contamination, and clustered Patient need
- Healer shortfall not inflicting anonymous daily damage, making every Citizen
  equally ill, or concealing which named lives require care
- Consequential shortfall becoming situated through MEET, Homecoming, a
  particular Patient, or the actual Hearth and inhabited ground under pressure

#### Boundaries

- Healer not becoming a personal medicine statistic, superior class of Citizen,
  generic recovery-speed bonus, automatic immunity, queue of routine treatment,
  or source of Remedies without material inputs
- Passive transformation applying only to defined Remedy Preparation and not
  treating care, recovery, or every Healer activity as produced output
- Guest Signatures able to reveal a condition, contain aftermath, or open a
  distinctive response without creating superior Healer coefficients, erasing
  illness, or replacing ordinary Healing Load

### Teacher

- Teacher carrying responsibility for teaching young Citizens, integrating
  newcomers, transmitting practical and cultural understanding, and sustaining
  social memory
- Every available Citizen assigned Teacher contributing their full Civic Share,
  without personality, prior service, Away capability, or equipment changing
  that Body-Unit-normalized contribution
- **Gathering Place** as Teacher's primary public Practice, shared with Leader
  without belonging exclusively to either Role
- **Hearth** drawing upon Teacher Readiness when nurture, dependency, early
  learning, or recovery requires it
- Teacher Citizens choosing whether to sustain ordinary Teacher responsibility,
  answer a need through Hearth, or commit their Civic Shares to active Projects

#### Teaching through Gathering Place and Hearth

- Gathering Place Practice Strength representing established communal ground,
  accumulated
  objects and records, shared conventions, suitable access, and remembered use
  rather than autonomous teaching
- Teaching, interpretation of Laws and Sayings, storytelling, observances,
  memorials, After-name recognition, Maturity, arrival, and the recounting of
  Chronicle material able to occur through Gathering Place
- Hearth supporting Teaching when care and learning are inseparable without
  becoming a family unit
- Caretaker and Healer Civic Shares aggregating with compatible Hearth support
  without counting as Teachers

#### Standing responsibility

- Teacher Readiness expressing whether the Colony can transmit what its people
  need to live together and remain historically continuous
- Ordinary Teacher work including lessons, practical transmission, cultural
  interpretation, newcomer integration, accompaniment of young Citizens,
  memorial continuity, and helping consequential experience become shared
  understanding
- A Colony without young Citizens, newcomers, lessons, grief, or a transition
  in practical or cultural understanding having no automatic Teaching Load
- Ordinary Chronicle and Citizen Tale continuity carrying no itemized labor
  charge
- Teaching remaining inhabited civic life rather than a passive-output channel
  or a hidden progression system

#### Teacher Projects

- Teacher Projects creating a defined persistent cultural or educational fact
  rather than turning every lesson or story into scheduled production
- Integrating a consequential discovery into communal understanding; creating
  a lasting memorial or observance; adapting Gathering Place to a newly
  understood need; or carrying a major cultural transition into ordinary life
- Routine lessons, storytelling, record consultation, interpretation,
  maturation, and ordinary newcomer welcome not automatically becoming Projects
- Builder or Leader involvement able to support a lasting cultural change
  without transferring its principal teaching purpose away from Teacher

#### Teacher vulnerability

- Insufficient Teacher Readiness creating vulnerability to failed newcomer
  integration, interrupted practical transmission, loss of shared meaning,
  neglected grief or memorial duty, and unmet needs among young Citizens
- Teacher shortfall not deleting known facts, erasing records, halting Maturity
  automatically, or imposing an abstract ignorance or culture penalty
- Consequential shortfall becoming situated through MEET, a particular Citizen,
  Gathering Place, Hearth, memorial, observance, or transition under pressure

#### Boundaries

- Teacher not becoming a personal instruction statistic, superior class of
  Citizen, Maturity-speed bonus, research specialist, archive worker, culture
  producer
- Guest knowledge able to enter communal life through Teaching without creating
  a superior Teacher coefficient
- Teacher having no defined passive production or transformation merely because
  other Roles possess one

### Watchkeeper

- Watchkeeper carrying the singular civic responsibility of noticing pressure
  early enough for the Colony to respond deliberately
- Every available Citizen assigned Watchkeeper contributing their full Civic
  Share, without limiting the Role itself to one Citizen
- Watchkeeper governing warning and Telegraph rather than generalized defense

#### Watchpost

- **Watchpost** as Watchkeeper's sole Practice
- Watchpost Practice Strength representing preserved sightlines and listening
  lines, known approaches, warning markers, protected observation, and
  established communication into inhabited Home rather than autonomous
  surveillance
- At least one full Civic Share sustained through Watchkeeper supporting
  completed usable Watchposts without requiring assignment to an individual
  Watchpost
- Watchpost retaining situated Practice Strength while supporting an active
  Project, recalculated according to remaining Watchkeeper support
- Edges, high lines, listening points, routes, and approaches remaining physical
  circumstances of Watchpost rather than additional Practices
- Watchkeeper able to perform basic watch before Watchpost exists, making
  Watchpost an expansion that requires no founding exemption

#### Standing responsibility

- Watchkeeper Readiness expressing whether the Colony receives useful warning
  before pressure becomes consequence
- Ordinary watch attending settlement approaches and boundaries, flood signs
  and changing water, human activity, predator movement, route obstruction,
  weather Telegraph, and unusual sound, vibration, scent, or absence
- Adequate Watchkeeper Readiness producing earlier, clearer, and
  better-localized Telegraph; allowing ordinary pressure to be absorbed; and
  improving the circumstances in which a consequential response begins
- Adequate Readiness not guaranteeing that nothing happens or displaying exact
  probabilities
- Warning remaining meaningful only when it gives the Colony time or
  information with which to choose

#### Citizen choice

- A Watchkeeper Citizen choosing whether to sustain ordinary Watchkeeper
  responsibility, answer a temporary need through DWELL or MEET, or commit
  their Civic Share to an active Project
- A Watchkeeper committed to a Project withdrawing that share from ordinary
  Watchkeeper Readiness
- Several Watchkeepers able to divide present effort between continuous warning
  and persistent improvement without creating per-edge staffing
- Focused observation, forecast preparation, and threat survey remaining
  temporary civic commitments rather than Projects unless they establish a
  persistent result

#### Watchkeeper Projects

- Watchkeeper Projects making a defined warning fact newly true rather than
  manufacturing observation work
- Adapting Watchpost; extending useful warning to newly inhabited ground;
  creating a lasting signal or communication line; restoring a lost warning
  connection; or adapting warning infrastructure to a recurring environmental
  pressure
- Watchkeeper having no compulsory repeatable Project once the Colony's warning
  posture is adequate
- Workshop and Builder involvement able to support physical work without
  transferring the Project's principal warning purpose away from Watchkeeper

#### Far Warning

- **Far Warning** as the defined Watchpost improvement, established in one
  particular Watchpost through a Watchkeeper Project
- The improved Watchpost extending established observation and signaling beyond
  Home's immediate approaches
- Far Warning able to reveal the family of an eligible approaching seasonal,
  environmental, animal, human, or route pressure early enough to create an
  additional preparation window
- The warning remaining qualitative: it gives neither an exact probability or
  countdown nor certainty about severity, location, or consequence
- Far Warning not guaranteeing that every pressure is observable, preventing an
  event, or adding generic Watchkeeper Readiness, Practice Strength, or Project
  capacity
- Builder or Crafter involvement able to support its physical means without
  transferring the improvement's warning purpose away from Watchkeeper

#### Watchkeeper vulnerability

- Insufficient Watchkeeper Readiness making warning late, incomplete, or badly
  localized rather than directly causing damage
- Characteristic pressure including predator arrival, flood warning, human
  work, route closure, and dangerous weather
- Shortfall reducing preparation, narrowing available response, or allowing a
  threat to reach inhabited ground before the Colony understands it
- MEET locating the resulting pressure in the actual Place, route, Residence,
  Practice, or Citizen at risk
- Watchkeeper shortfall never authorizing catastrophic loss to occur unseen
  while the player's attention is Away

#### Boundaries

- Watchkeeper not becoming a combat or guard class, tactical defense unit,
  prediction engine, exact event-probability display, universal surveillance
  system, per-edge worker assignment, or repeatable scouting chore
- Watchkeeper warning of danger without automatically preventing it or owning
  the Colony's response
- Resident Signatures such as Night Sky-watch or Boundary Deterrence able to
  provide a distinctive warning or response without replacing ordinary
  Watchkeeper responsibility

### Leader

- Leader carrying responsibility for coordinating civic decisions, making
  competing commitments legible, buffering social strain, and enabling
  deliberate Colony-scale action
- Every available Citizen assigned Leader contributing their full Civic Share,
  without personality, prior service, Away capability, or equipment changing
  that Body-Unit-normalized contribution
- **Gathering Place** as Leader's sole Practice, shared with Teacher without
  belonging exclusively to either Role
- Leader Citizens choosing whether to sustain ordinary Leader responsibility,
  answer a temporary civic need, or commit their Civic Shares to active
  Projects
- Leader not supporting Hearth Practice Strength

#### Gathering Place

- Gathering Place as the principal cultural and ceremonial Practice where
  Citizens assemble to interpret their shared life and make consequential civic
  choices together
- Gathering Place Practice Strength representing recognized common ground,
  established civic
  convention, suitable access, accumulated use, and shared orientation rather
  than autonomous leadership
- Tier recognition, major collective deliberation, civic ceremonies, and
  dispute resolution able to occur as Gathering Place MEETs

#### Community Board

- **Community Board** as the defined Gathering Place improvement, established
  in one particular Gathering Place through a Leader Project
- The improvement giving selected information already known to the Colony
  persistent shared expression in DWELL
- The Almanac remaining the always-available interface lens for current Colony
  and world information whether or not Community Board exists
- Community Board able to mirror known civic balance, seasonal pressure,
  forecasts, Telegraph, and preparation without detecting or improving any of
  them
- Its physical board, notices, or markers able to stand within the Gathering
  Place or elsewhere in Home without designating another Place or hosting a
  second Practice
- The improved Gathering Place remaining one Practice that can accommodate no
  more than one Project at a time
- Community Board remaining useful but non-gating: its absence never prevents
  ordinary civic decisions or hides information the player otherwise knows
- Community Board adding no Gathering Place Practice Strength, Leader Readiness,
  Project capacity, detection, forecast accuracy, or autonomous decision-making

#### Standing responsibility

- Leader Readiness expressing whether the Colony can recognize shared pressure,
  choose deliberately among competing needs, and carry collective decisions
  into action
- Leader Load arising from actual coordination, dispute, hospitality,
  agreement, emergency, transition, or other shared commitment rather than from
  the Role's mere existence
- A Colony with no current Leader Load incurring no Leader Pressure when the
  Role is unstaffed
- Ordinary Leader work including coordination, deliberation, dispute handling,
  emergency orientation, communicating commitments, receiving civic claims,
  and helping unequal burdens remain collectively intelligible
- Adequate Leader Readiness not guaranteeing agreement, removing sacrifice, or
  substituting for the particular Role needed to answer a material problem
- Leadership remaining a civic responsibility among equals rather than rank,
  command, office, personal charisma score, or ownership of Colony decisions

#### Leader Projects

- Leader Projects creating a defined persistent civic fact rather than turning
  every decision or meeting into scheduled work
- Adapting Gathering Place to a lasting civic need, including establishing its
  Community Board improvement;
  establishing a durable agreement, signal, or communication function; or
  supporting a Tier-defining civic change
- Ordinary coordination, dispute handling, emergency deliberation, information
  display, and Tier-recognition ceremony not automatically becoming Projects
- Builder, Teacher, Watchkeeper, or another Role able to support a lasting civic
  change without transferring its principal coordinating purpose away from
  Leader

#### Leader vulnerability

- Insufficient Leader Readiness creating vulnerability to delayed decisions,
  unresolved disagreement, uneven sacrifice, failed coordination, social
  strain, and inability to mobilize around a shared pressure
- Leader shortfall not removing player agency, forcing irrational behavior,
  creating automatic dissent, or making one Citizen sovereign over the Colony
- Consequential shortfall becoming situated through MEET, a particular civic
  decision, Gathering Place, Community Board, relationship, or shared pressure

#### Boundaries

- Leader not becoming a ruler, commander, mayor, superior class of Citizen,
  wildcard civic support, cross-Role Load reduction, universal Project-speed
  bonus, policy tree, or source of passive production
- Guest Signatures able to alter communication, attention, or a bounded civic
  response without creating superior Leader coefficients or replacing ordinary
  Leader responsibility

### Shared Practices

- **Workshop**, **Hearth**, and **Gathering Place** remaining shared Practices
  that compatible Roles draw upon as circumstances require
- **Hearth** as the shared Practice of healing, nurturing, and sustaining
  dependent or recovering lives
- Caretakers, Healers, and Teachers able to use Hearth according to actual need,
  without requiring all three continuously or creating a Hearth-specific Role
- **Family** remaining the provisional term for domestic relationship, separate
  from Hearth as a civic Practice

### Project Queue

The **Project Queue** is the shared execution layer for deliberate work that
makes a defined, persistent result true.

#### Project capacity

- Each completed usable Practice accommodating one active Project
- Project capacity belonging to individual Practices rather than to an abstract
  Colony-wide slot total
- The supporting Practice and the Project's target not needing to be the same
  Place
- A Workshop accommodating a Builder Project that establishes a new Residence
  or Practice at a designated Place
- A Workshop accommodating a Builder Project that establishes an Outpost at an
  eligible known Away location or restores a damaged Outpost
- A Workshop accommodating a Crafter Project that creates a Tool
- A Garden accommodating a Gardener Project that converts that Garden for
  Winter Cultivation
- An available Hearth accommodating one Healer Project that clears a named
  Citizen's Wound
- Two suitable Practices able to accommodate two Projects concurrently
- A Practice supplying Project capacity but never advancing a Project without
  committed Citizens
- Builder able to conduct the founding Workshop Project without Practice support
  before the first Workshop is complete, with completion ending that exemption

#### Creating an entry

Each Project Queue entry identifies:

- The defined persistent result
- Its owning Role
- Its supporting Practice
- Its target Place, Citizen, or created object where applicable
- Required material
- Required Civic Share-Days
- The named Citizens committed to it

Project ownership follows the result: new Residence or Practice construction is
Builder work, Tool creation is Crafter work, and Winter Cultivation conversion
is Gardener work. Outpost construction is Builder work. Clearing a named
Citizen's Wound is Healer work.

#### Queue operations

- The player selecting an eligible Project and supporting Practice
- The player able to reserve required material before commitment
- The player assigning one or more Citizens of the owning Role
- The interface showing the resulting loss of Role coverage, Practice support,
  and passive throughput before confirmation
- Commitment occupying the Practice's Project capacity and withdrawing the
  named Citizens' Civic Shares from ordinary work
- Each committed Citizen contributing Civic Share-Days equal to their Civic
  Share whenever the shared clock advances through the relevant day
- Fractional Civic Share-Days accumulating inside the Project until DAWN records
  whole progress
- DAWN recording accumulated progress
- Completion creating the persistent result, releasing the supporting Practice,
  and returning the Citizens to ordinary Role availability
- A committed Project not being interruptible or cancellable
- An uncommitted material reservation remaining releasable

A Wound Recovery Project is the sole v0.5 exception that requires exactly one
committed Healer and advances by one Healer-Day regardless of that Citizen's
Body Unit value. Its required Healer-Days therefore also establish its minimum
elapsed recovery time; additional Healers cannot accelerate biological
recovery.

The Practice continues contributing its situated Practice Strength while
accommodating a Project. Its support is recalculated from the compatible Civic
Shares that remain in ordinary work; those Citizens may also continue Role
coverage and passive production.

## 3.5 Pressure, Situations, and Home MEETs

Pressure shows where the Colony may struggle when weather, scarcity, danger,
disagreement, or another real circumstance tests it. Consequence arises through
the concrete situation and its resolution.

If the Colony can absorb that test through Readiness, ordinary life continues
and the player receives a brief account of what happened. If the test presents
meaningful stakes, choice, and consequence, DWELL yields to a Home MEET.

### World Pressure

**World Pressure** is an externally originating corridor condition that may add
contextual Load, test Readiness, alter ordinary life, or supply the circumstance
for a Home situation. Its origin lies outside civic allocation even though the
Colony can prepare for and mediate its consequences.

- Atmospheric Pressure including wind, rain, hail, heat, cold, humidity, and
  smoke
- Water and ground Pressure including flood, saturation, drought, erosion,
  freeze-thaw, ice, and blocked drainage
- Biological Pressure including predators, disease ecology, migration, forage
  cycles, and unusual abundance or scarcity
- Human Pressure including mowing, maintenance, roadwork, salting, pesticide,
  litter removal, and drainage work
- Traffic and mechanical Pressure including changing density, crashes,
  vibration, debris throw, idling, lane closure, and vehicle fire
- Exceptional corridor events able to combine or intensify several families
- Internal civic and social circumstances remaining outside World Pressure even
  when they create contextual Load or open a Home situation
- Biome, Season, Day Band, and special events changing the intensity, duration,
  forecastability, footprint, and expression of shared Pressure families rather
  than creating separate Home engines
- World state remaining continuous while Home adjudicates only at DAWN, a
  materially relevant Day Band transition, the start or end of a forecast
  event, a special-event trigger, or another meaningful state change
- Severe or exceptional World Pressure able to open a Home MEET even when every
  Civic Balance axis is Covered, with Readiness still shaping resilience and
  response
- A Civic deficit able to produce a shortage-shaped situation under ordinary
  World Pressure without requiring a special external event

### Bringing Pressure into focus

- Current World Pressure or an actual internal civic circumstance establishing
  plausible situation families and their background intensity
- The separate Civic Pressure profile influencing where a situation may find
  purchase and how likely meaningful attention becomes without directly
  scheduling a MEET
- Hidden Colony Pressure being recalculated at meaningful checks rather than
  accumulating as a visible global meter
- Bounded randomness keeping timing uncertain while World Pressure, civic
  posture, and campaign history keep it causal
- A deficiency that has recently shaped a Home MEET being temporarily damped so
  that its persistence does not generate another MEET every day
- A continuing deficiency able to return after time has passed, with its depth
  or duration able to increase the stakes rather than merely increasing event
  frequency
- Recently used situation families, Roles, Places, and threatened values being
  weighted downward so that clusters remain possible without directly
  duplicating or tightly overlapping one another
- The most pressured relevant Role shaping what is chiefly at risk
- A second relevant weakness shaping the collateral stake when one exists
- Prominent Housing Pressure locating the situation in the affected Residence
  and Citizens while relevant Role shortfalls shape its civic stakes
- A situation involving only one relevant Role drawing its collateral stake
  from an actual material, social, or environmental circumstance
- Pressure becoming specific to the Citizens, Places, Practices, relationships,
  or resources involved
- Relevant Role Readiness and the one Practice Strength of any Practice through
  which the situation occurs helping determine whether the test remains an
  ordinary report or requires a Home MEET
- The player understanding why the Colony is vulnerable without being shown a
  predictable incident counter

### Telegraph and rebalancing

- Watchkeeping as the Colony's general source of Telegraph
- A relevant Guest Signature able to provide bounded, species-specific warning
  or interpretation without contributing a general Watchkeeper Civic Share
- Telegraph communicating an observable situation family, approximate
  likelihood or urgency, likely exposed Roles, and relevant Places without
  displaying exact probabilities
- Useful Telegraph arriving before the event check or Impact and giving the
  player a DWELL opportunity to rebalance
- Rebalancing able to reassign uncommitted Civic Shares, alter Provisioning
  targets or reserves, make an available preparation, or knowingly accept the
  risk
- Citizens committed to Projects remaining committed and unavailable for that
  rebalancing
- Rebalancing able to prevent or delay a Home MEET, reduce its stakes, or change
  which shortfall shapes it without guaranteeing control over the event
- Stronger Watchkeeping making warning earlier, clearer, and better localized,
  with a relevant Guest Signature able to extend or sharpen it
- Some events remaining insufficiently observable to Telegraph
- The Almanac presenting all Telegraph known to the player and providing the
  functional lens for rebalancing
- A Community Board improvement mirroring selected known Telegraph and
  preparation inside DWELL without creating the warning, improving its
  accuracy, or gating access to the Almanac

### Choosing through Home MEET

- Home MEET presenting the same Colony and Places the player knows through DWELL
- A Pressure-driven Home MEET ordinarily offering three clear responses:
  - Commit resources, preparation, or available civic support to protect the
    primary stake
  - Make a different commitment to protect the collateral stake
  - Endure the situation without either commitment and accept the combined
    consequence
- Each response making its immediate cost, protected value, and likely
  consequence understandable before commitment
- The three-response structure applying to Pressure-driven situations rather
  than every conversation, ceremony, arrival, or transition at Home
- A Home MEET consuming world time even when the choice itself is resolved
  quickly

### Consequence and aftermath

- Weather, flood, predators, human activity, structural failure, shortage, and
  other dangers remaining Home situations rather than becoming a separate
  defense mode
- Roles, Readiness, situated Practice Strength, warning, prepared resources, and
  relevant Signatures shaping what the Colony can do
- Consequences able to affect named Citizens, resources, relationships, Places,
  Practices, and other concrete parts of the persistent world
- Injury, displacement, grief, death, or lasting physical change occurring only
  when supported by the situation and the player's choice
- Catastrophic loss never occurring unseen merely because the player is Away
- Resolution updating the Colony and completing the immediate situation
- An immediate response able to protect Citizens, redirect consequence, or buy
  time without removing the underlying Pressure that made the Colony vulnerable
- Underlying Pressure remaining until added Capacity, restored Housing, reduced
  Load, repair, or another actual state change restores the relevant Balance
- A Project entering the Project Queue only when a defined persistent result
  still needs to be built, restored, adapted, or made civically true
- That Project belonging to the Role that owns its persistent result
- Resolved consequences never generating redundant compulsory work
- An ordinary shortfall not being charged simultaneously through automatic
  daily decay, increased situation frequency, worse choices, and redundant
  repair

## 3.6 Resources, Production, and Provisioning

### Resources

| Resource | Function |
|---|---|
| **Perishable Sustenance** | Green-season food; normally consumed first and vulnerable to spoilage. |
| **Durable Sustenance** | Preserved food for winter, disruption, and reserves. |
| **Flexible Scrap** | Material suited to binding, wrapping, weaving, lashing, and sealing. |
| **Rigid Scrap** | Material suited to bracing, shielding, surfacing, and reinforcement. |
| **Supplies** | Prepared, expendable capability used during Away or situated need. |
| **Tools** | Durable functional Items created deliberately through Crafter Projects. |

Resources remain Colony-scale stocks. Scrap does not divide into component
inventories, and prepared Supplies do not retain individual makers.

### Production and transformation

- Garden with Gardener producing Perishable Sustenance
- Kitchen with Caretaker preserving Perishable Sustenance as Durable Sustenance
- Workshop with Crafter preparing non-Remedy Supplies
- Hearth with Healer preparing Remedy Supplies
- Each process using the shared Practice-and-Citizen gate and passive-throughput
  relationship established earlier
- Well-Placed Places contributing Spatial Alignment to their Practices'
  throughput
- Production remaining bounded by available inputs, season, known recipes,
  targets, and reserves
- Practices without defined output producing nothing merely because they exist

### Provisioning

- **Prepare:** transforming inputs while requirements permit and stock remains
  below the player's target
- **Hold:** suspending transformation while preserving the Role assignment
- **Unavailable:** the required Practice, Citizen, input, method, or condition
  being absent
- Player-set targets preventing automatic overproduction
- Player-set reserves protecting stock from Provisioning and unrelated Projects
- Reservations remaining visible and releasable before commitment
- Provisioning never creating resources from nothing

### Beautification

Beautification is the shared passive civic expression of Builder, Teacher,
Watchkeeper, and Leader effort.

- Builder, Teacher, Watchkeeper, and Leader as the non-producing Roles that
  contribute to Beautification
- Each Civic Share sustaining one of those Roles contributing one point of
  Beautification progress at DAWN
- A Citizen committed to a Project contributing no Beautification progress
  while committed
- Every contribution entering one Colony-wide Beautification track rather than
  a separate track for each Role
- Reaching a threshold creating one small authored **Frill** appropriate to a
  contributing Role, the Core Species, a suitable Place, and recent Colony
  history
- A completed Frill waiting to appear until Quiet Equilibrium when necessary,
  then remaining as a persistent part of Home even after equilibrium is lost
- A Frill able to anchor an EMBODY invitation while Quiet Equilibrium keeps
  EMBODY open
- Frills remaining mechanically inert: they create no Load, Readiness,
  resource, passive output, Project capacity, or Spatial Alignment
- Well-Placed Practices not accelerating Beautification
- Exact thresholds remaining a tuning value rather than another player-facing
  optimization problem

### DAWN accounting

DAWN resolves the day just completed, then establishes the state of the new day.
Results completed at that DAWN first contribute during the new day.

1. Resolve Sustenance consumption, normally drawing from Perishable Sustenance
   before Durable Sustenance.
2. Resolve active preservation and Supply preparation from the remaining
   eligible stock.
3. Apply aggregate spoilage to eligible Perishable Sustenance. Perishable stock
   carries no individual batches, ages, freshness values, or FIFO order, and
   Durable Sustenance does not decay ordinarily.
4. Add new passive production. Each process adds its calculated yield to any
   carried fractional remainder, releases only whole chunks to Colony stock,
   and retains the new remainder for a later eligible DAWN. New Perishable
   Sustenance therefore receives one full decision window before becoming
   eligible to spoil.
5. Add Beautification progress from the sustaining Civic Shares that
   contributed during the elapsed day.
6. Add committed Civic Share-Days, complete eligible Projects, release their
   supporting Practices, and return their Citizens to ordinary Role
   availability.
7. Resolve recovery and other changes in Citizen presence or availability.
8. Recalculate usable Places, Spatial Alignment, Housing Balance, Role Balance,
   and Colony Pressure for the new day.
9. Report meaningful changes, including stock movement, shortages,
   transformations, Frills, completed Projects, availability, and civic balance.

- Every Citizen creating Sustenance demand scaled by their Body Unit, with the
  exact per-Body-Unit quantity reserved for tuning
- A Residence or Practice completed at the present DAWN becoming usable during
  the new day and first contributing passive output at the following DAWN
- A Citizen whose recovery completes at the present DAWN becoming available
  during the new day

### Resources and Projects

- Projects drawing only their defined material requirements
- A planned Project able to reserve some or all required material
- Commitment protecting that material from unrelated use
- Building a Practice remaining a Builder Project and creating a Tool remaining
  a Crafter Project
- Ordinary structural upkeep remaining part of Builder responsibility
- Lasting construction, restoration, or adaptation requiring a defined Project
- Time alone not causing automatic structural decay

## 3.7 Population and Settlement Growth

MEDIAN is a low-population colony builder. Growth adds named lives, and every
new Citizen brings both civic possibility and new responsibility. A mature
Colony remains a community of dozens whose absences, arrivals, needs, and
contributions stay legible.

### Population at Home

- **Colony Roster** counting every living named Citizen who belongs to the
  Colony, including adults, young Citizens, Guests, Patients, and Citizens who
  are Away
- **Citizens at Home** counting the Roster Citizens physically present at the
  Home Median
- **Available Civic Population** counting Home-present adults currently able to
  sustain Roles or commit Civic Share-Days
- **Dependents and Patients** identifying present Citizens who require support
  without currently contributing an ordinary Civic Share
- The interface keeping these counts distinct so that total population never
  appears to be interchangeable workforce
- DAWN resolving location and availability before calculating Role Balance and
  Practice support
- A Citizen who is Away, acutely injured, receiving intensive care, or otherwise
  unavailable remaining a full member of the Roster without contributing a
  current Home Civic Share

### Capability and obligation

- Each available adult contributing the Civic Share established by their Body
  Unit: one for a Rabbit, Squirrel, or v0.5 Guest and one-half for a Mouse
- A new available adult therefore adding both one complete named life and their
  Body-Unit-normalized civic contribution
- Every new Core Species Citizen also requiring sufficient Core Residence
  Capacity, Sustenance, safe access, care, protection, civic integration, and
  remembrance
- Population growth increasing relevant Load according to the Colony's actual
  new obligations
- Young Citizens and unavailable adults adding responsibility before they add
  or recover a Civic Share
- Citizens supported by the Colony continuing to count toward Body-Unit-scaled
  ordinary Sustenance demand while Away, abstracting preparation and routine
  eating without creating an Away ration inventory
- Bodily consumption using the Body Unit relationships defined for the Core
  Species without reducing any Citizen's personhood or Roster standing

### Supporting a larger Colony

- Supported Core population depending upon usable Residence Capacity, Stores,
  routes, care, Readiness, and seasonal preparation rather than one abstract
  population limit
- Each Core Residence providing two Body Units of Housing Capacity, or three when
  Well Placed
- Rabbit and Squirrel Residences accommodating two or three Citizens, while
  Mouse Residences accommodate four or six
- Available Housing Capacity being one visible constraint without guaranteeing
  that further growth is responsible
- Planned Core growth requiring sufficient future Residence Capacity and a
  civic posture capable of absorbing the added Load
- Emergency hospitality able to exceed ordinary comfort through visible
  Housing Pressure and a concrete provisional shelter arrangement
- Temporary refuge and permanent welcome remaining different civic commitments
- The player receiving a plain-language preview of the changes to Housing
  Balance, Sustenance, Role Load, care, and available Civic Shares before
  authorizing Core growth
- Growth remaining optional even when the Colony could support it

### Three paths of growth

- **Wanderers** adding named Core-Species adults through refuge, rescue, and
  integration
- **Nesting** adding a small number of named young Citizens through a rare,
  seasonal Colony commitment
- **Guest residency** adding named non-Core Citizens or an explicitly authored
  collective-bodied household through relationship and hospitality
- Each path changing the Colony's obligations and history rather than acting as
  an interchangeable add-population command
- Population growth resolving principally through Home or Homecoming even when
  first contact occurs Away

### Wanderers and arrival

- Wanderers as the primary early path for adult population growth
- Each Wanderer arriving with a Given Name, Prior-life Tale, and any relevant
  injury, relationship, knowledge, or unfinished circumstance
- Arrival resolving through MEET, with choices shaped by the Colony's actual
  ability to offer refuge
- The player able to welcome the Wanderer permanently, offer temporary refuge,
  help them continue elsewhere, or refuse
- Provisional shelter permitting urgent refuge before permanent accommodation
  is ready while making its added Housing Pressure and other Load visible
- An accepted and integrated Wanderer becoming an equal Core Citizen and, when
  present and available, contributing the Civic Share of their Body Unit
- Refusal remaining possible and becoming part of Colony history without every
  refusal being converted into automatic punishment

### Nesting

- Nesting as a rare, voluntary, Colony-wide seasonal commitment rather than
  passive population production
- A species-appropriate green-season window making Nesting eligible without
  beginning it automatically
- Quiet Equilibrium creating the civic room in which particular Citizens may
  voice a wish to parent without causing that wish or guaranteeing a proposal
- The first eligible DAWN after the intended campaign interval allowing one
  authored **Nesting Proposal** to arise from mature, present Core Citizens
- The prospective parent or parents being selected through their particular
  relationships, Tales, ages, and circumstances rather than a universal
  friendship state, pairing score, or player assignment
- No eligible prospective parent meaning that no proposal arises during that
  window
- An active or sufficiently recent Nesting commitment suppressing another
  proposal for the intended campaign interval
- The Nesting Proposal becoming a Home MEET in which the named Citizens express
  their wish and the Colony considers the commitment
- Colony readiness determining whether the proposal can be supported rather
  than whether the Citizens may want it
- The readiness review showing credible future living accommodation, protected
  Sustenance, a usable Hearth, and sufficient civic support for care, teaching,
  protection, and any expected health needs
- Authorization reserving a visible quantity of Sustenance scaled to the
  expected new Body Units, with the exact multiplier remaining a tuning value
- One expected Rabbit or Squirrel young counting as one Body Unit for that
  reservation, and the usual two Mouse littermates together counting as one
  Body Unit
- The Nesting reserve remaining protected from Provisioning, unrelated
  Projects, and discretionary spending once the commitment is authorized
- The player seeing the temporary commitment and which Role balances will lose
  Readiness or enter Pressure before authorizing Nesting
- The player able to accept, defer within the seasonal window, or refuse the
  proposal without issuing a reproductive command
- Deferral or refusal becoming part of the involved Citizens' history without
  imposing an automatic relationship penalty
- Normally no more than one successful Nesting commitment resolving during a
  Colony-wide seasonal window
- A successful commitment adding a very small number of fully named young
  Citizens, with species-scale outcomes defined in the Citizens chapters
- Young Citizens entering the Roster and adding Sustenance, accommodation,
  Caretaker, Teacher, protection, and possible Healer Load immediately
- Young Citizens contributing no Civic Share until the Maturity transition
- Adoption and chosen-family formation following their own authored life events
  rather than being classified as Nesting or waiting for nesting season
- Family, Maturity, and the personal lives of young Citizens belonging to Part IV
  rather than being simulated as Colony production

### Hospitality and Guest residency

- Hospitality expressing the Colony's credible ability to house, sustain, know,
  and integrate a Guest through actual Places, access, resources, and civic
  support
- Guest accommodation following the species' single Residence Fit, ordinarily
  within its own dedicated Place rather than consuming or extending pooled Core
  Residence Capacity
- An authored species exception able to incorporate its Guest Residence into a
  named Practice as defined in Chapter 4.3
- The Guest Residence's Well-Placed status being judged by that fit as a whole
- Guest residency completing only after the promised accommodation and other
  agreed Terms of Hospitality have become true
- A welcomed Guest entering the Roster, creating ordinary support and Load, and
  contributing one Civic Share while present and available
- Guest residency remaining optional at every Colony Tier
- Guest identity, accommodation, Signatures, relationships, and the complete
  path to residency belonging to Chapter 4.3

### Scale and continuity

- Every increase producing named Citizens with Tales, obligations, and
  visible relationships to Home
- Mouse Colonies able to sustain denser named populations than Rabbit or
  Squirrel Colonies without treating individual Mice as fractions of Citizens
- Population bands serving encounter, visual-density, accommodation, Load, and
  campaign-tuning needs without becoming a player-facing hard ceiling
- Stability, memory, and chosen ambition defining a complete civic world even
  when the Colony remains small
- Population loss changing the Colony's present capacity and obligations without
  erasing the civic history or Tier it has already achieved

## 3.8 EMBODY

**Colony DWELL is MEDIAN's version of base-building play. EMBODY is MEDIAN's
version of cozy play.**

EMBODY lets the player live as or be with individual Citizens inside the
sanctuary created through DWELL. To live as a Citizen is to participate in a
bounded activity. To be with a Citizen is to accompany their movement, rest,
relationships, and experience of Home. Rare authored experiences may gather
the whole Colony while preserving every Citizen as an individual.

### Access and invitation

- Quiet Equilibrium opening EMBODY and its loss closing EMBODY
- EMBODY remaining strictly Home-only and never becoming available at an Away
  camp, Stopover, uncontested Node, or other merely calm location
- The player entering through a present and available Citizen at a safe, usable
  Place
- Individual experiences appearing as invitations rather than compulsory tasks
- An unavailable Citizen or unsafe Place remaining temporarily ineligible
- A Citizen in active Tharn remaining unavailable for EMBODY
- The player being free to leave an experience without penalty

### Participation and Presence

EMBODY has two primary forms:

- **Participation:** limited direct involvement in a bounded activity such as
  running, gathering, carrying, arranging, grooming, or playful movement
- **Presence:** guided attention to what a Citizen experiences through looking,
  listening, posture, movement, or repose
- An experience able to move naturally from Participation into Presence
- Controls remaining specific to the moment rather than expanding into
  unrestricted free movement
- Every experience carrying an authored arrival, sensory or relational
  development, and natural release
- The Citizen retaining agency over exact posture, pace, response, and social
  behavior
- Participation experiences expressing work already resolved through DWELL
  rather than producing superior output
- Cosmetic arrangements or meaningful remembered details able to persist when
  appropriate

### Experience families

- **Flow Traversal:** safe movement, rhythm, balance, momentum, and confidence
- **Small Work:** ordinary work felt through small tactile actions
- **Sensory Repose:** warmth, stillness, listening, breathing, and relief
- **Social Play:** chasing, teasing, imitation, curiosity, and mutual delight
- **Comfort and Care:** safety expressed through closeness, grooming, food, rest,
  and tending
- **Observation and Watch:** familiar attention to Home without threat-scanning
  play
- **Weather Enjoyment:** conditions that create Exposure Away becoming pleasure
  under shelter
- **Shared Meal:** the whole Colony gathering through an Open Table Kitchen,
  with the player accompanying collective ordinary life rather than commanding
  it

These families may overlap. Shared Meal is available only after Open Table has
been established; the others require no universal Practice improvement. The
families organize authored experiences without becoming separate progression
tracks.

### Species embodiment

- EMBODY translating the Colony's spatial grammar into bodily experience
- Mouse **JOIN** becoming fitted adjacency, shared walls, accumulated interior,
  warmth, and nearby life
- Rabbit **GATHER** becoming open common space, mutual visibility, bounding
  movement, familiar neighbors, and protected edges
- Squirrel **CONNECT** becoming height, balance, sway, junctions, alternate
  routes, and confidence across separation
- The same Place geometry mattering in both DWELL and EMBODY
- Species expression arising through bodies, movement, scale, sound, and spatial
  relationships rather than cosmetic styling alone

### Citizens and relationships

- Most experiences belonging to a particular Citizen in a particular Place,
  with Shared Meal as the bounded whole-Colony exception
- Shared Meal retaining every participant as a named Citizen with their own
  relationships, timing, and response rather than treating the Colony as a
  crowd unit
- Other Citizens retaining their own timing and responses rather than behaving
  as commanded props
- Play, affection, comfort, imitation, and attention feeling offered by
  relationships
- Injury, recovery, age, memory, and prior events shaping eligible
  experiences without reducing Citizens to condition displays
- Care experiences expressing recovery and trust without replacing Caretaker,
  Healer, or Teacher responsibility
- Young Citizens participating only in experiences appropriate to their present
  life stage

### Memory and reward

- The experience itself being the primary reward
- EMBODY granting no production multiplier, Civic Share, progression
  currency, or superior Citizen statistic
- Exposure ebbing through sanctuary and ordinary Home recovery, with EMBODY
  able to portray that change but never accelerate it
- EMBODY never clearing Tharn or substituting for the care and recovery that
  resolves it
- A moment entering the Record only when something particular and worth
  remembering occurs
- Repeated experiences remaining available for pleasure without manufacturing
  duplicate historical importance
- Quiet Equilibrium creating permission for attention rather than converting
  calm into a spendable resource

### Boundaries

- EMBODY remaining guided and bounded rather than becoming a second traversal
  game
- EMBODY having no hard failure, with mistakes creating texture, hesitation,
  rearrangement, or a gentler finish rather than punishment or repeated retry
- Flow Traversal emphasizing pleasure and confidence rather than lethal falls,
  harsh retries, or score pressure
- Small Work never becoming the required manual method for ordinary production
- Presence remaining meaningful even when the player's only actions are looking,
  listening, settling, approaching, or waiting
- EMBODY never erasing injury, grief, or other consequence merely by
  depicting comfort
- Loss of Quiet Equilibrium closing an active experience safely rather than
  nesting an urgent Home MEET inside EMBODY
- The system preserving the distinction between maintaining sanctuary through
  DWELL and inhabiting it through EMBODY

# PART IV — THE CITIZENS

Across Core and Guest species, balance means equivalent authorial completeness,
mechanical credibility, expressive richness, vulnerability, and opportunity
for attachment. Difference in body, mechanics, frequency, and magnitude is the
substance of that balance.

## 4.1 Citizenhood

MEDIAN is about a civilization small enough for every member to remain a
person. A **Citizen** is a named member of the Colony with a history, present
relationships, and a possible future. Their location, age, injury, and current
ability to contribute may change while their standing as a Citizen endures.

MEDIAN distributes the functions of a traditional player character across its
Citizens. Each carries part of what makes a player character matter: a
particular body, relationships, possessions, capabilities, history, risks, and
possible future. The Colony's roster collectively carries the player's
continuity through the world.

In this sense, Citizens are fractional player characters. Each remains a whole
person while sharing the player's attention with the rest of the Colony. By
building a life around them, sharing their experiences, and living with their
consequences, the player should ideally come to feel attachment to—and
something like friendship with—their Citizens. Familiarity, accompaniment, and
shared history cultivate that friendship.

### The Citizen

- Every living member of the Colony appearing by name in its Roster
- One named animal as the ordinary Citizen form, with Chapter 4.3 defining the
  only two exceptions
- Citizens being known through their bodies, relationships, belongings,
  histories, routines, and possible futures rather than personality scores
- Equal standing meaning equal civic and historical consequence rather than
  identical bodies or capabilities
- Young, injured, dependent, elderly, non-expedition, Core, and Guest Citizens
  remaining equally complete Citizens

### Individual expression

- Each Citizen distinguished through appearance, voice, temperament, habits,
  preferences, relationships, possessions, and accumulated history
- Those qualities shaping dialogue, advice, routines, animation, EMBODY, Focus,
  and contextual authored responses
- Individual expression never changing the Body-Unit-normalized Civic Share,
  ordinary Home contribution, or hidden aptitude
- Citizens able to change through experienced events without using personality
  scores, trait tiers, or an optimization taxonomy

### Core and Guest Citizens

- Core Citizens as Mice, Rabbits, or Squirrels belonging to the campaign's
  founding civilization
- Guest Citizens as non-Core animals welcomed into the Colony
- Both using the same underlying architecture of citizenship, relationships,
  presence, consequence, memory, and personal identity
- Species and origin changing how a Citizen inhabits that architecture without
  creating superior or lesser Citizens
- Chapters 4.2 and 4.3 providing the respective deep dives

### Body Units

- **Body Unit** as MEDIAN's normalization layer for aggregate mechanics, while
  Citizen remains the unit of individual life
- One Rabbit, one Squirrel, or two Mice constituting one Body Unit
- Every individual Guest in v0.5 constituting one Body Unit
- The two collective-bodied Guest households each constituting one Citizen and
  one Body Unit despite their visible multiplicity
- A single Citizen able to constitute more than one Body Unit only when an
  explicit species rule says so
- Each Body Unit providing one Civic Share, so a Rabbit, Squirrel, or v0.5 Guest
  contributes one and each Mouse contributes one-half
- Body Units governing Housing, Sustenance, Civic Balance, passive Role
  contribution, ordinary Project progress, Beautification, party composition,
  hazard normalization, and baseline Carry
- Names, relationships, personal items, harm, memory, and death following
  Citizens rather than Body Units
- Individual Tool, Supply, and Keepsake positions following Citizens and
  creating an explicit Mouse headcount advantage rather than aggregate output
- Body Unit value never changing Citizen standing, authorial attention, or
  personal consequence
- A Body Unit never merging several individual Citizens into one life or
  dividing one Citizen's personhood

### Belonging, location, and availability

Three separate questions govern a Citizen's current state:

1. **Belonging:** Is this animal a living member of the Colony?
2. **Location:** Where are they now?
3. **Availability:** What can they presently contribute or participate in?

- The Colony Roster answering belonging
- A Citizen's location showing **Home** while they are at the Home Median and
  their current Away position while they are traveling, Crossing, at a Node,
  or stopping at an Outpost
- Civic availability answering whether the Citizen can sustain a Role or enter
  a Project
- Young Citizens, Patients, and other dependents remaining present members
  without an available Civic Share
- Launch, Homecoming, Project commitment, injury, treatment, or another
  temporary barrier changing location or availability without removing
  citizenship
- Death removing a Citizen from the living Roster without erasing their
  historical belonging

### One Citizen across the game

- DWELL treating Citizens as named contributors to collective civic life
- EMBODY letting the player live as or accompany particular Citizens
- TRAVEL, RISK, and MEET exposing individual bodies, capabilities,
  relationships, possessions, and consequences
- A change occurring in one Register remaining true everywhere else
- The game never creating separate Home and Away copies of the same Citizen
- Every population, Role, presence, and availability total resolving back to
  particular names
- No Citizen receiving a hidden Home aptitude, worker quality, or generic
  productivity rank

## 4.2 The Three Core Species

### Shared foundation

- Each Core Species as a complete playable civilization
- Shared Citizen, Role, relationship, item, consequence, and memory architecture
- Species changing bodily and spatial expression without changing civic worth

The illustrative maxim is: **Mouse Builds a Manor House, Rabbit Builds a
Cul-De-Sac, Squirrel Builds a Web.** These are images of how each species shapes
Home, not named building types or required layouts.

### The animals

#### Mouse — JOIN

Mouse lives at a quick bodily and mental tempo. Its heart beats fast, and its
thought and attention move rapidly among scent, sound, touch, nearby motion, and
company. The world is immense at Mouse scale, so safety depends upon many quick
judgments made close to the body.

Mouse reads walls, roots, pipes, bark, litter, and the bases of human structures
as edges to follow and spaces to inhabit. Adjacency supplies cover, orientation,
and accumulated shelter; broad exposed ground becomes a profound interruption.
A small area can contain many distinct rooms, caches, routes, and lives.

Mouse therefore understands safety through enclosure, connection, and
accumulated nearness. Its civilization **JOINs** one protected interior to
another until many small spaces and quick individual lives become one inhabited
whole.

#### Rabbit — GATHER

Rabbit lives between vigilant stillness and explosive movement. Its attention
reaches outward across sound, motion, open ground, nearby companions, and the
concealment surrounding them. Safety lies in knowing when to freeze, when to
run, and where refuge waits.

Rabbit inhabits the surface among grass, brush, deadfall, clearings, and the
sheltering edges of human structures. Open ground becomes useful when cover
bounds it: a place where neighbors remain visible and concealment can be reached
in a few decisive bounds.

Rabbit therefore understands safety socially as well as spatially. Its
civilization **GATHERs** around open common spaces that remain protected at
their edges and difficult for the outside world to read.

#### Squirrel — CONNECT

Squirrel lives through balance, reach, and continuous judgment in motion.
Grasping paws, a flexible body, and a balancing tail make trunks, branches,
narrow surfaces, and interrupted heights into a navigable world. Safety depends
upon seeing the present foothold and the next possible movement together.

Squirrel reads trees, posts, signs, cables, fallen wood, and human structures as
anchors, routes, refuges, lookouts, and gaps. A safe place belongs to a larger
network from which another way home remains reachable.

Squirrel therefore understands safety through connection and redundancy. Its
civilization **CONNECTs** distant footholds, reinforces fragile links, and turns
isolated routes into a resilient network.

### Body and scale

#### Rabbit

- One Rabbit constituting one Body Unit
- Rabbit's ground-running body combining vigilant stillness, powerful
  acceleration, and decisive movement toward refuge

#### Squirrel

- One Squirrel constituting one Body Unit
- Grasp, balance, climbing, leaping, and tail-assisted motion allowing Squirrel
  to use vertical and interrupted terrain

#### Mouse

- Mouse's small body allowing two complete Citizens to constitute one Body Unit
- Each Mouse contributing one-half Civic Share and one-half Civic Share-Day to
  aggregate Home systems
- A standard three-Body-Unit Mouse party therefore able to contain six named
  Mice
- Each Mouse retaining an individual Tool, Supply position, Keepsake,
  relationships, personal consequences, and possible death

### Home expression

Each Core Species applies its spatial operator to both Residence and Practice
Places. The operator determines how Well-Placed status is judged while the
Place retains its civic function and Practice name.

#### Squirrel — CONNECT

- Home taking shape as a network of reachable nodes, anchors, and routes
- A Place being Well Placed when it participates securely in that network, with
  credible onward movement and sufficient alternatives if one route fails
- A Squirrel Residence accommodating two Squirrels, or three when Well Placed
- Growth adding or reinforcing nodes, bridging gaps, and turning fragile routes
  into resilient connections
- Height alone being insufficient; isolation, dependence upon one crossing, or
  loss of an important anchor able to make a Place Not Well Placed

#### Mouse — JOIN

- Home taking shape as an inhabited fabric composed of adjoining rooms,
  sheltered edges, shared boundaries, and accumulated interior
- A Place being Well Placed when it directly adjoins the Colony's protected
  inhabited fabric, without requiring a passage between the adjoining spaces
- A Mouse Residence accommodating four Mice, or six when Well Placed
- Growth adding chambers, pockets, and sheltered edges beside what is already
  inhabited, often incorporating roots, pipes, walls, foundations, and found
  materials
- An isolated pocket, exposed break, or lost adjacency able to make a Place Not
  Well Placed

#### Rabbit — GATHER

- Home taking shape around open common spaces bounded by concealment and
  accessible refuge
- A Place being Well Placed when it forms, faces, or preserves open common space
  while retaining protective edges, mutual visibility, and nearby refuge
- A Rabbit Residence accommodating two Rabbits, or three when Well Placed
- Growth completing one protected court or green before budding another
  neighborhood around new open common space
- Mere openness being insufficient; obscured common space, severed refuge,
  fragmentation, or exposed edges able to make a Place Not Well Placed

### Away expression

The party's actual bodily composition determines which Core Species traits it
contains. Species traits scale with the bodies or Body Units that possess them;
Guests contribute their own bodily properties and Signatures.

#### Rabbit

- Each actual Rabbit Body Unit contributing an equal share of the party's
  additional TRAVEL progress
- A full three-Rabbit party receiving doubled TRAVEL progress, with mixed
  parties receiving the proportional share physically present
- Crossing asking when the road opens and treating the highway as one temporal
  opening
- Planning making traffic patterns legible through accumulated observation
  before the player selects a launch moment, broad line, and far-side destination
- Commitment sending the whole party through one brief, uninterrupted sprint
- The exact relationship between Rabbit party composition and Crossing acuity
  being defined in Chapter 5.3

#### Mouse

- Each Mouse contributing six slots of secured Carry, so one Mouse Body Unit
  provides twelve slots rather than the ordinary ten
- A full Mouse party therefore carrying thirty-six secured slots rather than
  thirty
- Physical adversity being distributed among the individual Mice while
  remaining normalized by Body Unit, with the procedure reserved for Part V
- Crossing asking where continuity can be made and revealing the road as
  pavement-scale topology
- Planning establishing a limited chain of three to six meaningful waypoints,
  where added continuity may also lengthen exposure or produce awkward deviation
- Commitment sending the Mouse party through the complete chain as one
  continuous scurry without reopening planning at each waypoint

#### Squirrel

- Each actual Squirrel Body Unit contributing ten slots of optional Strained
  Carry
- Strained Carry remaining one shared party capacity rather than separate
  personal Squirrel inventories
- Additional fungible Cargo being exposed to the small visible Jostle risk
  defined in Chapter 5.2 and to explicit situated stakes in RISK or MEET
- Crossing asking how movement can flow through traffic rather than waiting for
  a static opening
- Planning defining a flowing trajectory through moving traffic geometry, with
  one or two predeclared redirects and a far-side climbable refuge or anchor
- Commitment sending the party through one continuous vector run, with the
  final affordance and characteristic failure geometry defined in Chapter 5.3

### Characteristic player decision

#### Squirrel

- Whether to attempt a larger material return through optional Strained Carry

#### Rabbit

- How to use a larger practical itinerary within the same expedition time

#### Mouse

- Which particular Citizens—and therefore which relationships, capabilities,
  and risks—to bring within a party that can hold more individual lives

### Limits

#### Mouse

- Mouse headcount increasing individual Tool, Supply, and Keepsake capacity
  across the party without increasing collective action
- Quick heartbeat and speed of thought shaping expression without granting
  extra actions or additional experienced time
- Mouse's modest secured-Carry advantage remaining distinct from Squirrel's much
  larger optional Strained Carry and its corresponding Jostle risk

#### Squirrel

- Strained Carry increasing neither secured Carry, Supply capacity, collective
  actions, nor protection for named or meaning-bearing objects

#### Rabbit

- Rabbit speed increasing neither Carry, Supply capacity, collective actions,
  MEET Rounds, nor experienced time

No Core Species trait creates a slowest-member rule or hierarchy of species
power.

## 4.3 Guest Citizens

MEDIAN's world contains many more animal lives than the Colony's Core Species.
A **Guest Citizen** is a named non-Core animal welcomed into the Colony through
relationship and accommodation.

Kehaar in Richard Adams's *Watership Down* is a central inspiration: a
conspicuously different outsider whose practical importance opens the way to
friendship in which difference remains fully visible.

Guest describes a Citizen's origin. A welcomed Guest holds full civic rank,
receives a Residence, belongs to the Roster, contributes one Civic Share when
available, forms relationships, faces consequence, enters memory, and may be
experienced through EMBODY.

Difference remains visible after welcome. A Guest remains fully their own
species: their body, senses, habits, communication, spatial needs, and way of
participating continue to matter. Each Guest species also offers the Colony a
distinct capability, expressed through one bounded **Signature**.

Hospitality begins when the Colony encounters an animal, comes to understand
what living together would require, and chooses whether to make that promise
real. The player may accept, delay, or refuse those Terms. Every arrival is
therefore a deliberate act of making room for a particular new Citizen.

### Guests at a glance

The canonical short name appears in tables, headings, mechanical rules, and
other reference material. A longer species name may appear naturally in
descriptive prose for variation. Tables and paired labels use the canonical
short name alone.

#### Expedition Guests

Each Expedition Guest contributes one Civic Share through the individual
Citizen's authored Home Role. Every species remains one Body Unit while
contributing its own fixed amount of secured Carry.

| Species | Secured Carry | Signature | Residence Fit |
|---|---:|---|---|
| Raccoon | 12 | **HANDLE — Latchwork** | dry exterior access |
| Crow | 9 | **HANDLE — Trialwork** | high open perch |
| Gull | 9 | **READ — Long View** | broad open landing |
| Fox | 12 | **HANDLE — Carcass Claim** | drained boundary ground |
| Weasel | 10 | **INTERCEDE — Drive Off** | narrow multi-exit bank |
| Hedgehog | 8 | **INTERCEDE — Living Cover** | concealed hedge |
| Snake | 6 | **SPEAK — Display** | sun-warmed shelter |
| Mink | 10 | **REACH — Water Reach** | safe waterline |

#### Resident Guests

Each Resident Guest contributes one Civic Share through its fixed Role. Its
Signature remains a distinct species-specific capability.

| Species | Fixed Role | Signature | Residence Fit |
|---|---|---|---|
| Owl | Watchkeeper | **Night Sky-watch** | high listening hollow |
| Sparrow | Teacher | **SPEAK — Day Call** | concealed social perch |
| Toad | Caretaker | **Wet-Ground Care** | wet edge with dry refuge |
| Fireflies | Leader | **SPEAK — Lantern Procession** | dark damp flight space |
| Groundhog | Gardener | **Seasonal Telegraph** | deep drained ground |
| Turtle | Caretaker | **Water Garden Residence** | shallow water and basking |
| Bumblebees | Gardener | **Garden Cohabitation** | sheltered flower access |
| Mole | Builder | **Subsurface Diagnosis** | visible undisturbed soil |
| Bat | Builder | **Workshop Roost** | high dry-dark roost |
| Pigeon | Leader | **Gathering Loft** | open built ledge |
| Skunk | Watchkeeper | **SPEAK — Boundary Deterrence** | downwind boundary |
| Possum | Healer | **Hearth Annex** | ventilated receiving edge |

### Shared Guest architecture

Every Guest has full Citizen standing. Their Civic Share supports an ordinary
Role, while their Signature provides one bounded capability unique to
that animal. Residence, relationships, and EMBODY make that difference legible
as a particular life.

| Property | Expedition Guest | Resident Guest |
|---|---|---|
| Citizen standing | Full | Full |
| Civic Share while present and available | One | One |
| Home Role | Individual-authored | Species-fixed |
| Signature operates | Away | At Home |
| May Launch | Yes | No |
| Personal Away consequence | Yes | No |
| Residence, relationships, memory, and EMBODY | Full | Full |

#### Civic contribution

- Each present and available adult Guest contributing one ordinary Civic Share
- Personality, species, Signature, equipment, and prior history never
  changing the value of that share
- An Expedition Guest's Home Role belonging to the particular Citizen
- A Resident Guest's Home Role being fixed by species
- The Guest directing their share either to ordinary Role responsibility or an
  active Project under the same rules as any other Citizen
- Absence, unavailability, or Project commitment withdrawing that share from
  ordinary Role support
- No Guest possessing a hidden aptitude or generally superior productivity
  coefficient; any authored production exception being explicit, situated, and
  part of that species' single Signature

#### Signatures

- Each Expedition Guest having one bounded Signature that operates Away
- Each Resident Guest having one situated Signature that operates at Home
- **Attribution:** the responsible Citizen or household remaining visible
- **Situation:** the Signature mattering in one bounded circumstance or
  explicitly named Place relationship rather than operating generally across
  the Colony
- **Restraint:** the Signature opening or changing a choice or explicitly
  defined Place relationship without automatically solving the whole situation
- **Species grounding:** the option following from the animal's body, senses,
  behavior, or ecology
- **Suspension:** absence, injury, season, or Residence condition able to make
  the Signature unavailable when relevant
- Resident life remaining mechanically and expressively complete without Launch

Guest type is not a player toggle, rarity, or civic rank. An authored life event
may move an Expedition Guest into Resident life, but type never changes through
routine reassignment.

### Hospitality and residence

#### From MEET to arrival

1. The Colony first encounters a named animal in a situation that exists
   independently of recruitment.
2. The outcome establishes recognition: a relationship, obligation, promise,
   shared interest, or unresolved tension.
3. **Terms of Hospitality** state what continued life together requires. They
   always include one completed Guest Residence satisfying that species'
   Residence Fit, plus any explicit relational or safety promise belonging to
   that Guest. The Residence occupies a dedicated Place unless the species has
   an authored Practice-sharing exception.
4. A Builder designates its Place, or uses its named host Practice, and completes
   or adapts the Residence through an ordinary Builder Project.
5. Once the Terms are true, Arrival brings the Guest Home, adds them to the
   Roster, and begins their civic life.
6. The player may refuse, delay, or fail to fulfill the Terms. This remains a
   consequential relationship outcome, not failed collection.

#### Guest Residence

- One Guest Residence housing one Guest Citizen or collective-bodied household
- The Residence ordinarily occupying one dedicated Place, contributing no Core
  Housing Capacity, and being unable to host a Practice simultaneously
- A species-specific exception able to incorporate the Guest Residence into one
  named Practice without creating a general mixed-use Place rule
- An incorporated Residence still requiring an ordinary Builder Project,
  appropriate material, and time, while consuming no separate Place
- The host remaining one Practice with its ordinary improvement rules and
  one-Project capacity; the Residence adding neither another improvement nor
  another Project slot
- Each Guest species having one defining **Residence Fit** judged as a whole
- A completed Residence being either Well Placed or Not Well Placed according to
  that fit
- A completed Well-Placed Guest Residence fulfilling the housing portion of the
  Terms of Hospitality
- Core-species architecture able to shape its visual expression without adding
  a second placement test
- No separate housing checkboxes, partial fit scores, or cumulative bonuses
- Further bodily, material, and atmospheric detail remaining descriptive rather
  than becoming additional requirements

#### Change after arrival

- Later loss of Residence Fit never evicting the Guest or removing their
  citizenship
- The Not-Well-Placed Residence becoming a visible accommodation problem at that
  Place
- Loss of fit able to suspend the Guest's Signature when the missing fit is
  directly relevant
- The Guest retaining their Civic Share unless a separate condition makes them
  unavailable
- Repair or adaptation using ordinary Project rules
- No separate Guest Housing score, capacity pool, or numeric Load axis
- A vacated Guest Residence persisting as a Place, or as a physical part of its
  host Practice, and remaining part of Colony history

### Life in the Colony

Welcoming a Guest creates an ordinary life within the Colony. A Guest's
Residence, Role, routines, relationships, absences, embodied experiences, and
Signature make their membership visible throughout Home.

#### Role and presence

- A present and available adult Guest contributing one Civic Share through
  their Home Role
- Role support remaining Colony-wide rather than assigning the Guest to a
  particular Practice
- Resident Guest Roles fixed by species without creating separate Guest
  Practices
- Expedition Guest Roles belonging to individual Citizens rather than their
  species
- Either type able to sustain ordinary Role responsibility or commit their
  Civic Share to an eligible Project
- Launch removing an Expedition Guest's Role support and leaving their
  Residence visibly unoccupied
- Resident Guests remaining at Home but able to become unavailable through
  injury, illness, season, displacement, or another actual condition
- Absence and unavailability removing contribution without removing citizenship

#### Ordinary Home life

- Every Guest having routines grounded in body, Residence Fit, time, season,
  relationships, and civic participation
- Guests appearing throughout ordinary Colony life rather than only when their
  Signature becomes relevant
- A Guest's fixed or individual Role expressed through visible activity without
  creating site-by-site assignment
- Residence use, movement, sound, rest, food, conversation, and social habits
  making species difference legible
- Guest needs creating meaningful situations without becoming a queue of
  personal maintenance chores
- A Signature remaining one capability within a larger life rather than the
  Guest's sole identity

#### EMBODY

- Any present and available Guest eligible for Home EMBODY while Quiet
  Equilibrium is open
- **Activity** allowing the player to join a bounded species action such as
  basking, listening, sorting, swimming, tending flowers, tracing a route, or
  guiding light
- **Presence** allowing the player simply to accompany a characteristic state
  such as warm rain, a dark roost, still water, evening flight, scent-reading,
  or a household waking
- Control able to use bodily movement, sensory emphasis, guided attention,
  collective flow, small gestures, or cinematic accompaniment
- Guest EMBODY not required to reproduce Core-species locomotion or become a
  traversal challenge
- The purpose being to understand how a particular friend inhabits Home

#### Relationship and vulnerability

- Every Guest forming particular relationships rather than representing a
  species stereotype
- Species difference able to create affection, curiosity, dependence, friction,
  fear, mentorship, obligation, or shared routine
- Guests participating in ordinary Home situations and consequences
- Injury, absence, Residence trouble, and relationship change remaining visible
- Irreversible named loss never occurring off-screen merely because the player
  is attending another Register
- The Record, Tales, and long-term memory governed by Chapter 6.1

### Collective-bodied Citizens

Nearly every MEDIAN Citizen is one named animal. Firefly Family and Bumblebee
Household are the two closed v0.5 exceptions. For these Guests, the household
is the smallest living subject the Colony can meaningfully know.

Each household is one Citizen and one Body Unit, represented by several visible
bodies.

#### One civic subject

- One Roster entry, Guest Residence, Hospitality commitment, fixed
  Role, Civic Share, Signature, and continuous identity
- Several bodies never multiplying civic contribution, Project support,
  production, housing demand, or Signature
- A clear distinction from Mice: two Mice may share one Body Unit but remain two
  complete Citizens; a collective-bodied household is itself one Citizen
- No additional collective-Citizen types in v0.5

#### Visible plurality

- Firefly Family known through its recurring formation, pulse, route, and
  shared light
- Bumblebee Household known through circulation, hum, collective activity, and
  repeated return to its Residence
- Individual bodies not receiving separate names, Roles, inventories,
  assignments, or administrative tracking
- No hidden miniature colony, individual pollination simulation, or raw-body
  census

#### Continuity and consequence

- Availability and major consequences applying to the household as a whole
- Visible thinning or changed activity able to express injury, loss, season, or
  generational change without creating separate Citizens
- The household contributing either its full Civic Share or none; it never
  contributes fractional shares
- The named household persisting through changes in visible membership while
  its social continuity remains
- Departure, dissolution, or death requiring an authored and visible event
  rather than occurring through background simulation

#### EMBODY

Collective-bodied EMBODY treats the household as one coordinated living flow.
Movement, pulse, sound, circulation, and shared attention make the household's
plurality playable as one Citizen.

### Expedition Guest profiles

Every Expedition Guest is one named individual Citizen and one Body Unit. Each
may Launch and participates in the shared Away action economy through their own
body, secured Carry, and Signature. Their Home Role belongs to the individual
Citizen. Guest EMBODY opens at Home during Quiet Equilibrium as an expressive
part of that Citizen's life.

#### **Raccoon**

**Animal identity.** Dexterous forepaws, material intelligence, curiosity, and
familiarity with human refuse make Raccoon the clearest human-object specialist.
Raccoon knows how to open and handle things built for hands unlike its own.

**Body and Citizen form.** Raccoon is a strong climbing quadruped with unusually
dexterous, sensitive forepaws. It can grasp, turn, sort, and inspect suitable
objects, while consequential interaction with human-made closures remains
governed by Latchwork.

**Residence.** Build the Residence where it has dry access from outside the
Colony. Raccoon can then arrive with found objects without carrying them through
enclosed Home spaces.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — HANDLE: Latchwork.** Raccoon may directly open or
manipulate one accessible human-made closure or simple mechanism. Lids, catches,
caps, knots, tied bags, and similar constructions become possible to handle
according to how they work.

**Limits.** Latchwork does not reveal contents, identify contamination,
guarantee useful material, or remove carrying cost. It applies only to an
accessible closure or mechanism that Raccoon can plausibly manipulate.

**EMBODY Activity.** Handle, turn, inspect, and sort familiar objects with
sensitive forepaws.

**EMBODY Presence.** Rest among a personal collection while light and Colony
movement pass the Residence opening.

#### **Crow**

**Animal identity.** Crows meet the world with close attention, durable memory,
social intelligence, and opportunistic object use. Flight provides perspective,
but Crow's defining distinction is experimental curiosity: Crow discovers how
something may work.

**Body and Citizen form.** Crow uses the shared Flyer bodily grammar while
manipulating small objects through beak and grasping feet. Flight and object
handling remain bodily capabilities; Trialwork governs the distinct moment when
Crow recruits one available object to test or act upon another.

**Residence.** Build the Residence on a high, open perch. Crow needs clear air
for arrival and departure without an enclosing roof or obstructed flight path.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — HANDLE: Trialwork.** Crow may recruit one available object
for one plausible test or indirect manipulation. It may probe an opening, draw
something closer, place a marker, or drop one thing to provoke or measure a
response.

**Limits.** Trialwork requires one available object and one plausible
interaction. Crow cannot invent material, manufacture elaborate Tools,
guarantee the result, or replace Raccoon's direct manipulation of closures.

**EMBODY Activity.** Grasp, place, compare, and rearrange familiar objects with
beak and feet.

**EMBODY Presence.** Settle on the high perch and turn attention among calls,
weather, and movement below.

#### **Gull**

**Animal identity.** Gull inhabits a broad, human-shaped landscape in which
highways, rooftops, reservoirs, parking lots, storms, and distant feeding
grounds remain connected. Conspicuous and comfortable in open weather, Gull
understands what lies beyond the Colony's ordinary horizon.

**Body and Citizen form.** Gull uses the shared Flyer bodily grammar and
requires broad, open space to launch and land. Flight changes its position and
viewpoint, but never removes the Citizen from party composition, elapsed time,
Exposure, or consequence.

**Residence.** Build the Residence at a broad, open landing. Gull needs an
unobstructed approach, landing, and departure through open air.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — READ: Long View.** From an eligible open vantage, Gull
reveals situated context about broad geography, weather, water, traffic, human
activity, or the relationship among distant Places. Long View informs the
ground party before commitment without resolving the situation itself.

**Limits.** Long View requires an eligible open vantage and may be constrained
by obstruction, distance, darkness, or weather. It provides neither
omniscience, exact mapping, future prediction, fast travel, party transport,
nor a safe Crossing bypass.

**EMBODY Activity.** Face the wind, preen, and make a short circuit between the
Residence and nearby open landing points.

**EMBODY Presence.** Rest on the exposed landing while weather and the distant
human landscape move around Home.

#### **Fox**

**Animal identity.** Red Fox is substantially larger than most Citizens, led
strongly by scent, and unmistakable as a predator. Its competence around
carcasses can materially aid the Colony, while its silhouette ensures that
welcome and instinctive fear must coexist honestly.

**Body and Citizen form.** Red Fox has the largest individual body in the v0.5
expedition roster but still constitutes one Body Unit. Its size changes which
openings, shelters, surfaces, and social spaces it can use. Its fixed Guest
Carry reflects that body without changing its Civic Share or Body-Unit value.

**Residence.** Build the Residence on well-drained ground at the Colony
boundary. The location gives Red Fox's larger body direct outside access while
keeping the Residence part of Home.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — HANDLE: Carcass Claim.** At an eligible carcass or roadkill
Node, Red Fox may process suitable matter into the one Supply specified by that
Node. Carcass Claim is the biological counterpart to RENDER: it produces the
same authored kind of outcome without requiring a Render Tool.

**Limits.** Carcass Claim consumes the suitable matter and follows ordinary
Supply-placement rules. It cannot choose an arbitrary Supply, identify
contamination, guarantee that a carcass is usable, prevent rivals, erase time
or consequence, or create Resources, Tools, Keepsakes, or Artifacts. Because no
Tool is used, it makes no Tool Strain check; Red Fox remains personally exposed
to any authored risk or consequence of the process.

**EMBODY Activity.** Read and retrace the Colony boundary through scent, tracks,
and disturbed ground.

**EMBODY Presence.** Curl inside the earth and attend to Home through sound and
scent from its outer edge.

#### **Weasel**

**Animal identity.** A Weasel's narrow body, explosive speed, intense attention,
and ability to enter confined ground make it an active intercessor. It changes
danger by pressing into the space between a threat and something vulnerable.

**Body and Citizen form.** Weasel's long, narrow body supports fast ground
movement and entry into spaces larger Citizens cannot physically use. Such
access applies to Weasel alone and may separate it from companions rather than
silently opening a route for the whole party.

**Residence.** Build the Residence in a narrow bank with more than one exit. The
confined space suits Weasel's body while preserving alternate ways in and out.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — INTERCEDE: Drive Off.** Weasel may press a small predator
or aggressive animal away from something vulnerable. Drive Off can redirect
the threat, hold its attention, or create an interval for escape.

**Limits.** Drive Off applies to one small predator or aggressive animal, not
every threat or an entire battle. Weasel remains exposed to injury and
separation, and the threat is redirected rather than automatically defeated.

**EMBODY Activity.** Run a short bank route, inspect its openings, or play
through the Residence's alternate exits.

**EMBODY Presence.** Groom or rest inside the narrow bank while remaining alert
to movement beyond it.

#### **Hedgehog**

**Animal identity.** A Hedgehog's deliberate pace, low body, protective spines,
and vulnerable face and underside create an unusual relationship with danger.
Its protection comes through sheltering, escort, and steadfast presence rather
than speed or aggression.

**Body and Citizen form.** Hedgehog is a low, ground-bound quadruped whose
spines protect its back and flanks while leaving its face and underside
vulnerable. The spines shape contact and defensive posture but do not provide
generic armor or immunity from Exposure.

**Residence.** Build the Residence inside a concealed hedge. The hedge shelters
Hedgehog's low, deliberate movement while preserving a usable route into the
Colony.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — INTERCEDE: Living Cover.** Hedgehog may shelter one injured
or very small Citizen, shield one fragile Cargo stake, or provide cover during
a withdrawal. Living Cover allows something vulnerable to keep moving when
ordinary retreat would leave it exposed.

**Limits.** Living Cover protects only one vulnerable Citizen or Cargo stake in
a bounded movement. Hedgehog cannot shield the whole party, ignore a major
threat, or escape the danger it enters.

**EMBODY Activity.** Forage beneath leaves or walk slowly beside another
Citizen through protected ground.

**EMBODY Presence.** Curl within the concealed hedge and gradually relax as
nearby activity becomes familiar.

#### **Snake**

**Animal identity.** Limbless movement, scent-led perception, dependence on
warmth, and expressive stillness distinguish Garter Snake from every other
Citizen. Its presence also confronts inherited prey fear and asks the Colony
and Snake to negotiate that bodily history honestly.

**Body and Citizen form.** Garter Snake moves through continuous bodily contact
with the ground, reads scent through tongue and air, and depends upon available
warmth. Equipment and carried belongings must suit a limbless body rather than
assuming hands, pockets, or ordinary harnessing. This constraint is expressed
through Snake's uniquely low secured Carry rather than additional equipment
exceptions.

**Residence.** Build the Residence in a sheltered place warmed by the sun.
Garter Snake needs dependable basking warmth with protected space in which to
withdraw.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — SPEAK: Display.** Garter Snake may use posture, movement,
and deliberate stillness to communicate with animals that recognize snake
display. Display can open PARLEY, YIELD, intimidation, recognition, or mutual
withdrawal where ordinary speech carries no force.

**Limits.** Display works only where another animal can perceive and understand
snake posture. It is neither a venom attack nor universal translation, mind
control, or guaranteed surrender.

**EMBODY Activity.** Follow warmth or scent across a short route through
continuous whole-body movement.

**EMBODY Presence.** Bask in stillness or coil beside a trusted Citizen who has
learned not to startle.

#### **Mink**

**Animal identity.** American Mink belongs as fully to water edges as most
Citizens belong to dry ground. Its long, powerful body, swimming ability, and
familiarity with currents, culverts, and flooded spaces make water a lived and
traversable domain.

**Body and Citizen form.** American Mink moves on land and swims and dives
through suitable water. Water competence changes its available movement and
perception, but does not eliminate cold, current, contamination, separation, or
the need to return to dry refuge.

**Residence.** Build the Residence at a safe waterline. Mink needs direct water
access with dry refuge above ordinary high water.

**Civic contribution.** One Civic Share through this Citizen's authored Home
Role; neither body nor Signature changes its value.

**Signature — REACH: Water Reach.** American Mink may enter water,
flooded culverts, drainage channels, or waterlogged spaces that the ordinary
party cannot safely use. Water Reach allows Mink to inspect, retrieve, or
rescue within that domain on the party's behalf.

**Limits.** Water Reach does not ferry the party or eliminate cold, current,
contamination, separation, or Cargo loss. Mink can enter the waterborne
situation but cannot guarantee retrieval or rescue.

**EMBODY Activity.** Swim a protected waterline, dive beneath roots, or groom at
the Residence entrance.

**EMBODY Presence.** Float or rest beside the water while watching Home from its
surface level.

### Resident Guest profiles

Each Resident Guest contributes one Civic Share through a fixed Home Role and
lives their mechanical life at Home. Owl, Sparrow, Toad, Groundhog, Turtle,
Mole, Bat, Pigeon, Skunk, and Possum are individual Citizens; Fireflies and
Bumblebees are the two collective-bodied Citizen households. Each individual or
household constitutes one Body Unit. Guest EMBODY opens during Quiet
Equilibrium as an expressive part of that Citizen's life.

#### **Owl**

**Animal identity.** Barred Owl inhabits night through acute hearing, high
perspective, quiet patience, and a body adapted to darkness. Sound makes distant
or obscured activity legible long before most Citizens can see its source.

**Body and Citizen form.** Owl is one individual Citizen and one Body Unit. Its
body shapes visible movement, Residence use, EMBODY, and its Signature
without changing its Civic Share.

**Residence.** Build the Residence in a high listening hollow. Barred Owl needs
sheltered rest from which surrounding night sounds remain clear.

**Civic contribution.** One Civic Share through the fixed Watchkeeper Role.

**Signature — Night Sky-watch.** Night Sky-watch sharpens an existing
nocturnal Telegraph while Owl is present and available and a Watchpost is
usable. The clearer warning remains qualitative and passes through the ordinary
Almanac and Community Board presentation.

**Limits.** Night Sky-watch creates no new detection channel, probability
display, Practice Strength, additional Watchkeeper Civic Share, or automatic
defense.

**EMBODY Activity.** Turn toward sounds across Home and shift between the hollow
opening and a nearby listening perch.

**EMBODY Presence.** Remain in the high hollow while the Colony settles and
night changes the surrounding soundscape.

#### **Sparrow**

**Animal identity.** Song Sparrow becomes familiar through learned calls,
seasonal song, and repeated use of social perches. A particular voice can become
part of the Colony's shared understanding while retaining distinct meanings
across ordinary song, contact, and warning.

**Body and Citizen form.** Sparrow is one individual Citizen and one Body Unit.
Its body shapes visible movement, Residence use, EMBODY, and its Guest
Signature without changing its Civic Share.

**Residence.** Build the Residence at a concealed social perch. Song Sparrow
needs cover while remaining close enough for calls and company.

**Civic contribution.** One Civic Share through the fixed Teacher Role.

**Signature — SPEAK: Day Call.** Day Call becomes shared civic
understanding through ordinary life around the Gathering Place. In an eligible
daylight Home MEET, it opens a SPEAK response through which familiar Citizens
can understand one shared warning or instruction.

**Limits.** Day Call creates no alert state, production bonus, universal
translation, or automatic resolution.

**EMBODY Activity.** Sing from familiar perches, bathe in shallow water, or
gather material for the concealed nest.

**EMBODY Presence.** Sit nearby while a particular voice becomes part of the
Colony's morning.

#### **Toad**

**Animal identity.** American Toad moves between damp ground, shallow water,
and dry refuge. Stillness, sensitivity to moisture, and familiarity with runoff
make the changing boundary between water and inhabited ground central to its
life.

**Body and Citizen form.** Toad is one individual Citizen and one Body Unit. Its
body shapes visible movement, Residence use, EMBODY, and its Signature
without changing its Civic Share.

**Residence.** Build the Residence at a wet edge with dry refuge. American Toad
needs to move easily between damp ground and protected rest.

**Civic contribution.** One Civic Share through the fixed Caretaker Role.

**Signature — Wet-Ground Care.** During an eligible Garden Home MEET
concerning runoff, dampness, or invertebrate pressure, Wet-Ground Care opens a
Caretaker response that can redirect or contain the immediate problem and
protect current yield or cultivated continuity when either is already at stake.

**Limits.** Wet-Ground Care affects only the present Garden Home MEET and
changes neither standing yield nor the Garden's ordinary rules.

**EMBODY Activity.** Move through wet leaves, sit in warm rain, or make a small
feeding movement at dusk.

**EMBODY Presence.** Wait at the dry refuge while water gathers, passes, and
recedes around the Residence.

#### **Fireflies**

**Animal identity.** The Firefly Family appears as a small recognizable company
of lights whose formation, pulse, and route recur together. Coordinated
illumination makes the family more legible and memorable than any single tiny
body.

**Body and Citizen form.** Fireflies are one collective-bodied Citizen and one
Body Unit. Several visible bodies express one household; they create no
additional Civic Shares, assignments, inventories, or Signature uses.

**Residence.** Build the Residence in a dark, damp flight space. The Firefly
Family needs room to circulate together without harsh light overwhelming its
signals.

**Civic contribution.** One Civic Share through the fixed Leader Role.

**Signature — SPEAK: Lantern Procession.** During an eligible nighttime
SPEAK Home MEET, the household's shared light makes faces, gestures, and the
relationship among participants easier to understand, allowing an eligible
win-win resolution to become available.

**Limits.** Lantern Procession does not guarantee that resolution, extend the
workday, illuminate Home generally, or create permanent lighting.

**EMBODY Activity.** Guide the household as a loose constellation, widening or
gathering its formation above one familiar part of Home.

**EMBODY Presence.** Accompany first emergence as separate lights gradually
assemble outside the dark Residence.

#### **Groundhog**

**Animal identity.** Groundhog combines deep burrowing, upright observation,
close attention to changing ground, and a life strongly shaped by season. Green
growth is understood through timing and recurrence across the surrounding
season.

**Body and Citizen form.** Groundhog is one individual Citizen and one Body
Unit. Its body shapes visible movement, Residence use, EMBODY, and its Guest
Signature without changing its Civic Share.

**Residence.** Build the Residence in deep, well-drained ground. Groundhog needs
stable earth for a substantial burrow without ordinary waterlogging.

**Civic contribution.** One Civic Share through the fixed Gardener Role.

**Signature — Seasonal Telegraph.** Seasonal Telegraph sharpens existing
warning of an approaching seasonal or environmental pressure while Groundhog is
present and available. It identifies the kind of change becoming likely, such
as hard frost, flood, heat, or disruptive human work, and passes through the
ordinary Almanac and Community Board presentation so the player may rebalance.

**Limits.** Seasonal Telegraph predicts neither exact timing nor severity and
creates no forecast system, event immunity, or additional Watchkeeper Civic
Share.

**EMBODY Activity.** Clear the burrow entrance, stand upright at the lookout, or
settle into the sun.

**EMBODY Presence.** Sit beside the burrow while wind, temperature, and growing
things disclose the season bodily.

#### **Turtle**

**Animal identity.** Painted Turtle lives between shallow water, sun-warmed
surfaces, and the protection carried in its shell. Deliberate movement and
bodily patience give it a different relationship with urgency, shelter, and the
passage of time.

**Body and Citizen form.** Turtle is one individual Citizen and one Body Unit.
Its body shapes visible movement, Residence use, and EMBODY without changing
its Civic Share.

**Residence.** Establish the Residence within one completed Garden. The Garden
must provide shallow water and safe movement to a sun-warmed basking place.

**Civic contribution.** One Civic Share through the fixed Caretaker Role.

**Signature — Water Garden Residence.** A Garden satisfying Turtle's
Residence Fit may incorporate the Residence as an authored exception to
ordinary Place use. Establishing it still requires an ordinary Builder Project,
material, and time but consumes no separate Place. The Garden retains its
ordinary improvement rules and one-Project capacity.

**Limits.** Water Garden Residence changes only Place use; it adds no yield,
Practice Strength, or additional capacity.

**EMBODY Activity.** Bask, enter shallow water, and move deliberately through
the host Garden.

**EMBODY Presence.** Rest half in the water while highway light and Garden
movement pass across its surface.

#### **Bumblebees**

**Animal identity.** The Bumblebee Household is known through several visible
bodies, shared circulation, persistent hum, and repeated return. Collective
activity makes the household legible as one Citizen through its coordinated
plurality.

**Body and Citizen form.** Bumblebees are one collective-bodied Citizen and one
Body Unit. Several visible bodies express one household; they create no
additional Civic Shares, assignments, inventories, or Signature uses.

**Residence.** Establish the Residence within one completed Garden. The Garden
must provide a protected nesting cavity with sheltered access to sustained
flowering growth.

**Civic contribution.** One Civic Share through the fixed Gardener Role.

**Signature — Garden Cohabitation.** The Bumblebee Residence may be
incorporated into one completed Garden as an authored exception to ordinary
Place use. Establishing it still requires an ordinary Builder Project, material,
and time but consumes no separate Place. The Garden retains its ordinary
improvement rules and one-Project capacity.

While the host Garden is usable and the Bumblebee Household is present,
available, and sustaining Gardener responsibility, that Garden contributes one
additional half chunk of Perishable Sustenance. The half chunk enters the
ordinary fractional-throughput cadence and adds to any half chunk earned through
the Garden's Spatial Alignment. Project commitment or other unavailability
withdraws both the household's ordinary Gardener contribution and this
half-chunk contribution.

**Limits.** Garden Cohabitation affects only the host Garden. It neither assigns
bees to routes, simulates pollination, modifies every Garden, nor creates a
second Signature.

**EMBODY Activity.** Accompany the household through an impressionistic circuit
between its protected nest and the host Garden's flowers.

**EMBODY Presence.** Feel the household's hum and warmth at first emergence or
remain with it as rising wind draws everyone home.

#### **Mole**

**Animal identity.** Eastern Mole perceives ground vibration, moving soil,
hidden voids, and the resistance of material around its body. It knows
constructed Home partly through what lies immediately beneath surfaces other
Citizens treat as solid.

**Body and Citizen form.** Mole is one individual Citizen and one Body Unit. Its
body shapes visible movement, Residence use, EMBODY, and its Signature
without changing its Civic Share.

**Residence.** Build the Residence in visible, undisturbed soil. Eastern Mole
needs workable ground while its entrances and surface mounds remain legible as
part of Home.

**Civic contribution.** One Civic Share through the fixed Builder Role.

**Signature — Subsurface Diagnosis.** When a Home MEET concerns the
ground beneath an established Place, Mole identifies the relevant hidden
physical cause, such as saturated soil, a void, undercutting, frost movement, or
a buried obstruction. That knowledge may change an existing response or
establish the need for an ordinary Builder Project.

**Limits.** Subsurface Diagnosis creates no underground simulation and neither
excavates, repairs, nor improves the Place automatically.

**EMBODY Activity.** Dig a short visible run, push loose earth into shape, and
pause to read vibrations through the ground.

**EMBODY Presence.** Rest at a familiar mound opening while footsteps, weather,
and Colony movement travel through the soil.

#### **Bat**

**Animal identity.** Little Brown Bat navigates through echolocation and local
flight while remaining sensitive to enclosed air and structural surfaces. Dry
darkness is an inhabited sensory space shaped by echo and moving air.

**Body and Citizen form.** Bat is one individual Citizen and one Body Unit. Its
body shapes visible movement, Residence use, and EMBODY without changing its
Civic Share.

**Residence.** Build the Residence in a high, dry-dark roost. A suitable
Workshop may incorporate that protected hanging space and clear flight opening
without consuming a separate Place.

**Civic contribution.** One Civic Share through the fixed Builder Role.

**Signature — Workshop Roost.** A suitable Workshop may incorporate
Bat's high, dry-dark, smoke-free Residence as an authored exception to ordinary
Place use. Establishing it still requires an ordinary Builder Project,
material, and time but consumes no separate Place. The Workshop retains its
ordinary improvement rules and one-Project capacity.

**Limits.** Workshop Roost adds no Practice Strength, passive output, Project
progress, or additional capacity.

**EMBODY Activity.** Hang and groom, turn toward returning echoes, or make a
short dusk circuit through the Workshop aperture.

**EMBODY Presence.** Remain in the dry-dark roost while sound and changing air
describe the Workshop and Home beyond it.

#### **Pigeon**

**Animal identity.** Rock Pigeon navigates human structures through landmark
memory, repeated routes, and social signals exchanged across distance. Ledges,
overpasses, rooftops, and faraway flock sites belong to one familiar inhabited
geography.

**Body and Citizen form.** Pigeon is one individual Citizen and one Body Unit.
Its body shapes visible movement, Residence use, and EMBODY without changing
its Civic Share.

**Residence.** Establish the Residence within one completed Gathering Place.
The Gathering Place must provide a stable open built ledge with clear air for
landing.

**Civic contribution.** One Civic Share through the fixed Leader Role.

**Signature — Gathering Loft.** A Gathering Place satisfying Pigeon's
Residence Fit may incorporate the Residence as an authored exception to
ordinary Place use. Establishing it still requires an ordinary Builder Project,
material, and time but consumes no separate Place. The Gathering Place retains
its ordinary improvement rules and one-Project capacity.

**Limits.** Gathering Loft changes only Place use; it adds no Practice Strength
or additional capacity.

**EMBODY Activity.** Dust-bathe, head-bob through the Gathering Place, or circle
Home before returning to the same ledge.

**EMBODY Presence.** Warm on the Gathering Loft while civic life continues
below and distant structures mark the horizon.

#### **Skunk**

**Animal identity.** Striped Skunk moves deliberately at night and communicates
warning before resorting to force. Posture, scent, and unmistakable boundary
presence make negotiated proximity part of life around this Citizen.

**Body and Citizen form.** Skunk is one individual Citizen and one Body Unit.
Its body shapes visible movement, Residence use, EMBODY, and its Guest
Signature without changing its Civic Share.

**Residence.** Build the Residence at the downwind Colony boundary. The location
lets ordinary airflow carry scent away from the inhabited center while
preserving direct outside access.

**Civic contribution.** One Civic Share through the fixed Watchkeeper Role.

**Signature — SPEAK: Boundary Deterrence.** During an eligible SPEAK Home
MEET shaped by threatening animal pressure at the Colony boundary, Skunk's
deliberate warning projects credible toughness and allows a favorable nonviolent
resolution to become available.

**Limits.** Boundary Deterrence does not guarantee success or automatic
defense; it changes only the available SPEAK resolution.

**EMBODY Activity.** Walk the downwind boundary, test the air, root through
leaves, or groom outside the den.

**EMBODY Presence.** Rest near the Residence while the Colony's familiar
activity keeps a respectful lane open.

#### **Possum**

**Animal identity.** Virginia Opossum is a nocturnal climber and scavenger
comfortable around remains that other Citizens avoid. Careful handling, bodily
resilience, and profound stillness under danger complicate an outward
appearance that may initially inspire mistrust.

**Body and Citizen form.** Possum is one individual Citizen and one Body Unit.
Its body shapes visible movement, Residence use, and EMBODY without changing
its Civic Share.

**Residence.** Establish the Residence within one completed Hearth. The Hearth
must provide a ventilated outer annex where Possum can rest apart from its warm,
clean center.

**Civic contribution.** One Civic Share through the fixed Healer Role.

**Signature — Hearth Annex.** A Hearth satisfying Possum's Residence Fit
may incorporate the Residence as an authored exception to ordinary Place use.
Establishing it still requires an ordinary Builder Project, material, and time
but consumes no separate Place. The Hearth retains its ordinary improvement
rules and one-Project capacity.

**Limits.** Hearth Annex changes only Place use; it adds no Remedy Preparation,
Practice Strength, or additional capacity.

**EMBODY Activity.** Climb through the Hearth Annex, balance with the tail, and
arrange a sheltered sleeping place.

**EMBODY Presence.** Wake slowly in the ventilated shade while Hearth activity
continues nearby.

### Departure and continuity

- Injury, aging, relationship, or another authored life event able to change how
  a Guest participates without reducing Citizen standing
- Expedition-to-Resident transition possible as an authored life change rather
  than routine reassignment
- Departure and death changing the living Roster without erasing relationships,
  memory, or history
- A vacant Guest Residence persisting as a Place or part of its host Practice,
  and remaining available as an absence, memorial, or later adaptation

### Roster boundaries

- Guest recruitment optional at every Tier
- No Tier, victory condition, or essential system requiring a Guest, particular
  species, or completed roster
- Physical accommodation, civic responsibility, and relationship governing
  hospitality rather than a collectible capacity or rarity system
- Refusal, delay, non-arrival, departure, and no-Guest play remaining complete
  campaign outcomes
- No rarity tiers, collection percentage, or recruit-all reward

## 4.4 Relationships and Family

Citizens become particular friends, relatives, companions, rivals, teachers,
students, caregivers, and mourners. A relationship belongs to the Citizens who
live it, and the game remembers that relationship as a qualitative truth with
its own history and expression.

### Particular relationships

- Relationships persisting between particular Citizens rather than attaching
  generic social values to a species, Role, Residence, or party
- Friendship, affection, trust, partnership, kinship, mentorship, rivalry,
  estrangement, obligation, grief, and other authored relationships able to
  coexist without forming one progression ladder
- A relationship able to begin before citizenship through a Prior-life Tale or
  arise during the campaign through shared life
- The same relationship remaining true across Home, Away, and every Register
  until an experienced event changes it
- Authored content referring to the particular Citizen or relevant relationship
  it concerns rather than testing for a universal **Trusted Friend** state
- No relationship score, affection currency, social rank, or hidden friendship
  threshold

### Change and social autonomy

- Relationships forming and changing through witnessed choices, shared events,
  ordinary proximity, care, conflict, absence, return, MEET, and EMBODY
- The player able to make time, keep promises, offer care, choose responses, and
  place Citizens in circumstances where a relationship may change
- Citizens retaining ownership of affection, trust, forgiveness, estrangement,
  and other social responses
- No direct command to create a friendship, declare an emotion, end a rivalry,
  or reconcile Citizens
- Not every shared activity producing a relationship change
- A consequential formation, reversal, separation, or reconciliation becoming
  visible rather than occurring as an unexplained off-screen update

### Family

- **Family** being a set of persistent relationships among particular Citizens,
  not a separate population unit, household object, or civic institution
- Family relationships arising through parenthood and birth, siblinghood,
  adoption, partnership, chosen kinship, sustained care, or another authored
  recognition of belonging
- Sustained care becoming family only when the Citizens recognize that
  relationship through an authored event
- A family able to cross species, generations, origins, Residences, and Guest or
  Core status
- Cohabitation able to express family life without defining who is family
- A Citizen able to belong within several overlapping family relationships
- Family remaining wholly separate from Hearth, which is exclusively a Practice
- Family composition never being limited to a breeding pair or biological
  descent
- No Family entity, household score, genetic traits, bloodline score, inherited
  aptitude, breeding optimization, or family technology tree

### Relationships in play

| Register | Relationship expression |
|---|---|
| **DWELL** | Citizens seek company, share routines, advise, avoid, care for, and notice one another throughout ordinary Home life. |
| **TRAVEL** | Companions converse, disagree, encourage, worry, and reveal how distance or return matters to them. |
| **RISK** | A relationship may shape hesitation, protection, separation, or whom a Citizen attempts to reach without granting an extra action. |
| **MEET** | A particular relationship may change the stakes, open a contextual response, or become part of the consequence. |
| **EMBODY** | Social Play, Care, activity, and Presence allow the player to accompany a relationship without commanding its emotion. |

- Relationships informing dialogue, Focus, advice, aid, hesitation, protection,
  reunion, and consequence only where the present situation makes them relevant
- Any mechanical effect being defined by the event or owning system rather than
  supplied by a universal relationship bonus
- Family and other relationships providing meaningful stakes without making one
  party composition, social arrangement, or life history optimal
- Separation, reconciliation, inheritance, grief, and memorial continuity
  remaining consequences among particular Citizens
- Death ending a Citizen's present action without erasing their relationships
  from surviving Citizens, Tales, or the Record
- The Citizen view presenting current relationship state from the Almanac and
  relevant shared history from the Citizen's Tale, as governed by Chapter 6.1

## 4.5 The Life Course

Every Citizen has an origin, a present life stage, and a possible future. The
life course makes growth, aging, and loss visible through selected changes and
authored events. v0.5 uses two mechanically distinct stages: **Young** and
**Adult**.

### Origins and arrival

- Founders beginning with shared pre-campaign history and established
  relationships to one another
- Campaign-born Citizens entering through a completed Nesting commitment with
  Given Names and immediate family relationships
- Adoption and other authored arrivals able to bring a young Citizen into new
  family relationships without being classified as Nesting
- Wanderers and Guests arriving with Prior-life Tales, relationships, and lives
  that precede their place in the Colony
- Origin changing what history and relationships accompany a Citizen without
  creating different grades of civic standing
- Every arrival becoming legible through the Roster, Almanac, and their Tale at
  the moment that Citizen enters Colony life

### Young Citizens

- A young Citizen being fully named and counted from arrival rather than held in
  an anonymous population pool
- Each young Citizen having a Residence association, family and other
  relationships, ordinary needs, and a developing Tale
- Rabbit and Squirrel young each constituting one Body Unit, while the usual two
  Mouse littermates constitute one Body Unit without ceasing to be two Citizens
- Young Citizens adding Sustenance, accommodation, Caretaker, Teacher,
  protection, and possible Healer Load as defined by Population and Settlement
  Growth
- Young Citizens contributing no Civic Share, holding no ordinary Role,
  supporting no Project, and being unable to Launch
- Age-appropriate participation in DWELL, Home MEET, family life, and eligible
  EMBODY experiences
- Young Citizens being particular lives with futures rather than replacement
  stock for an absent or dead Citizen

### Maturity

- **Maturity** as the sole mechanical life-stage transition in v0.5
- Maturity following sufficient seasons and authored life events, with exact
  timing reserved for campaign pacing and tuning
- Time establishing eligibility while the Citizen's relationships, ordinary
  life, and remembered events give the transition its particular meaning
- The Maturity event ending Young status and beginning the ordinary Civic Share
  supplied by that Citizen's Body Unit
- A newly mature Core Citizen becoming eligible for ordinary Role assignment
  without receiving a superior aptitude, inherited profession, or training rank
- Civic Maturity and eligibility to Launch remaining distinct, with expedition
  requirements governed by Part V
- Family and the wider Colony recognizing the transition through a visible
  event at a fitting Place
- Maturity entering the Record and the Citizen's Tale
- No experience bar, age-up button, Teacher-speed modifier, stat-training
  ladder, or grindable shortcut

### Adulthood and aging

- Adult being the only post-Maturity functional life stage in v0.5
- Age continuing as a personal truth expressed through appearance, movement,
  routine, relationships, responsibility, memory, and changing needs
- No universal Elder state, age bar, lifespan countdown, accumulating age
  penalty, or automatic loss of capability
- An authored life event able to change a particular Citizen's availability,
  Role participation, expedition eligibility, care needs, or ordinary life when
  age is genuinely relevant
- Veteran, disabled, caregiving, and non-expedition adult lives remaining
  complete forms of citizenship rather than incomplete retirement states
- Species biology informing authored portrayal without creating automatic
  expiry or unequal civic worth
- Age never reducing Citizen standing, family membership, relationship, or the
  significance of a life

### Death and continuity

- Death remaining possible but rare, explicit, and visible rather than arising
  from routine attrition, an unattended roll, or an old-age timer
- Detailed causes and harm procedures belonging to the relevant Away, Crossing,
  or MEET system
- Death removing the Citizen from the living Roster and ending their present
  Civic contribution without deleting their historical belonging
- The death entering the Record while the Citizen's Tale closes and remains
  accessible
- Family, other relationships, Keepsakes, possessions, Places, routines, the
  Record, and Tales carrying the particular absence forward
- Surviving Citizens able to experience grief, inheritance, changed
  responsibility, remembrance, or another authored consequence
- No birth, adoption, arrival, or young Citizen being framed as a mechanical
  replacement for the person who died

## 4.6 Personal Items and Focus

Personal items help the player know who a Citizen is and remember what has
happened to them. They remain attached to particular lives while collective
MEET resolution remains shared.

### Personal identity and Away loadout

| Position | Eligible Citizens | Persistence | Purpose |
|---|---|---|---|
| **Keepsake** | Every Citizen | Personally persistent | Carries emotional meaning and one bounded contextual effect. |
| **Tool** | Launch-eligible Citizens | Persistent; freely reassigned at Home | Supplies one reusable working capability Away. |
| **Supply** | Launch-eligible Citizens | Assigned for one Expedition; consumed when committed | Supplies one prepared intervention Away. |

- A Citizen able to have no Keepsake without appearing unfinished
- Tool and Supply positions appearing only for Citizens eligible to prepare for
  Launch
- Young Citizens and Resident Guests therefore retaining complete personal
  identity without displaying inert Away-equipment positions
- Core Citizens and Expedition Guests following the same Tool, Supply,
  Keepsake, and Focus rules whenever each position applies
- Tool or Supply eligibility never creating a higher grade of Citizen
- Body compatibility expressed through the item's physical manifestation rather
  than a separate proficiency or species-aptitude system
- Tools and Keepsakes remaining visible at Home, while their defined mechanical
  effects belong to Away unless an explicit rule states otherwise

### Tools

A **Tool** is a persistent named working object held by one Launch-eligible
Citizen. It provides a narrow reusable capability Away while retaining its own
material history at Home.

- Five ordinary Tool classes: **Carry**, **Reach**, **Cut**, **Brace**, and
  **Render**
- Any Launch-eligible Citizen able to hold any class when its physical form is
  credible for that body
- Species, Home Role, prior work, and personality creating no proficiency gate
  or Tool-effect coefficient
- Multiple Tools of one class providing redundancy and different possible
  protagonists without stacking their effect on one Round
- The player able to equip, clear, or reassign a Tool freely through the Citizen
  view while at Home
- Tool assignment becoming fixed once the Citizen Launches
- A relevant Tool appearing only after the player chooses an Approach it can
  credibly affect
- Selecting that Tool supplying one contextual effect and placing its holder in
  Focus
- Selecting a Tool in MEET committing it to the Round and placing it in hazard
- The Tool providing its complete effect before any resulting Damage is applied
- Tool hazard resolving through the MEET's situated consequences rather than a
  universal damage probability or separate Strain roll
- A Tool remaining outside that Round's ordinary Tool hazard when it is not used,
  unless the situation explicitly threatens carried equipment generally
- A Damaged Tool remaining with its Citizen but becoming unavailable for the
  rest of the Expedition
- Ordinary repair after Homecoming belonging to existing Crafter responsibility
  rather than requiring a Project
- Permanent Tool loss or destruction requiring an explicit severe consequence
- A Carry Tool providing its standing Cargo effect without taking Focus and
  entering hazard when a MEET or other situation materially stakes that
  capacity or its carried load
- Ordinary Tools having no levels, aptitude modifiers, or unique mechanical
  riders beyond their class
- **Specialist Tools** providing specific authored capabilities opened through
  Fine Work rather than numerical upgrades to ordinary Tools
- A Tool able to be adapted, damaged, repaired, lost, or destroyed through the
  applicable Project or authored-consequence rule
- Routine use and reassignment not manufacturing history, while consequential
  creation, recovery, use, adaptation, damage, repair, loss, or destruction may
  enter the Tool's record

### Supplies

A **Supply** is one anonymous prepared intervention assigned to a
Launch-eligible Citizen for one Expedition.

- Every Supply being one discrete, body-scaled object that its carrier can
  physically carry and deploy rather than a kit, bundle, or abstract capacity

The four provisional Supply classes are:

| Supply | Physical form | Direction |
|---|---|---|
| **Binding** | One prepared cord, strip, wrap, or fastening | Connect or secure. |
| **Device** | One small prepared contrivance | Produce one temporary physical or sensory effect. |
| **Offering** | One prepared morsel or meaningful token | Place something into an encounter with another being. |
| **Remedy** | One prepared dose, dressing, or poultice | Treat or protect a body. |

- Binding able to tie, tether, wrap, patch, restrain, or fasten by creating one
  temporary connection
- Device able to wedge, mark, signal, trigger, screen, or probe through one
  compact deployed object
- Offering able to be given, shared, exchanged, placed, promised, or used as
  bait without compelling another participant to accept or respond as intended
- Remedy able to clean, soothe, stabilize, or protect against a bodily
  consequence
- Remedy able to stabilize a Wound through Homecoming, lessen one defined
  immediate physical effect, or contain the acute Wound accompanying Maiming
- Remedy having no effect upon Tharn once it occurs
- Remedy never reversing death or retroactively removing a resolved
  consequence
- Crafter preparing Binding, Device, and Offering Supplies while Healer prepares
  Remedies
- Each class remaining a functional family rather than dividing into named
  subtypes, qualities, or separate item records
- Supplies produced through ordinary Provisioning and drawn from the Colony's
  prepared stock during Launch
- Each participating Citizen able to carry at most one Supply
- Assignment becoming fixed Away, with no transfer or between-MEET loadout
  management
- A relevant Supply appearing only after the player chooses an Approach it can
  credibly affect
- Committing the Supply providing its stated effect and consuming it whether or
  not the Approach achieves its intended outcome
- The authored MEET stating the exact available effect rather than allowing a
  Supply to become any object or solution the player imagines
- A Supply able to soften a consequence, preserve an additional stake, extend
  an achieved result, or enable a credible alternate resolution without
  replacing the Round or guaranteeing success
- Remedy able to be spent on its carrier, another party member, or another
  present animal whose credible bodily need makes that care applicable
- Remedy able to express PARLEY through offered or shared care, but not as a
  generic barter token and never compelling trust, agreement, recruitment, or
  repayment
- Unspent Supplies returning to the prepared Colony pool at Homecoming and all
  Supply positions then clearing
- A Supply discarded during TRAVEL leaving play rather than returning Home
- No individual maker, personal name, provenance, persistent carrier
  relationship, or Item Tale

### Keepsakes

A **Keepsake** is a persistent emotional object whose meaning belongs to one
Citizen's life. Every Citizen may have one, but an empty position remains a
complete and valid life.

- A Keepsake carrying one narrow circumstance in which its personal meaning can
  matter during an eligible Home or Away MEET
- The player choosing the Approach before any Keepsake expression appears
- One relevant Keepsake able to become the Round's single personal-item
  expression
- The holder taking Focus when the Keepsake shapes the Round
- The Keepsake able to soften a personal consequence, preserve one personally
  meaningful stake, or permit a response within the chosen Approach
- A Keepsake never creating an Approach, adding a Round, changing the party's
  general aptitude, or guaranteeing success
- A Keepsake being present rather than spent, charged, refreshed, or placed on
  cooldown
- Home-present young Citizens and Resident Guests able to matter through their
  Keepsakes in eligible Home MEETs without acquiring an Away loadout
- Damage, gifting, loss, sacrifice, surrender, succession, replacement, and
  memorial display occurring only through an explicit consequential event
- A current Keepsake remaining personally held until such an event changes that
  relationship

### Ownership and succession

- Tools being transferable working objects whose present holder and
  consequential history remain legible
- Supplies belonging to the current Expedition rather than acquiring permanent
  personal ownership
- Keepsakes remaining personally rooted rather than entering a Colony-wide
  equipment pool
- A new Keepsake replacing an existing one only through a meaning-making event
  and player confirmation
- Gifting, succession, memorial display, or another consequential transfer
  preserving the relationship and history carried by the object
- Routine Tool reassignment remaining equipment management rather than a
  remembered event
- Death never becoming an inventory-looting transaction; the relevant
  Homecoming, family, succession, or memorial consequence determines what
  happens to a Tool or Keepsake

### Focus

**Focus** identifies the Citizen whom the current MEET Round naturally follows.
The party still chooses and resolves its Approach collectively; Focus makes one
particular life visible within that shared action.

1. The MEET presents its valid choices.
2. The player chooses an Approach.
3. Relevant Tools, Supplies, Keepsakes, relationships, or authored
   circumstances become visible.
4. The player may choose no personal-item expression or one Tool, Supply, or
   Keepsake expression.
5. Focus follows from the chosen expression or authored circumstance when one
   identifies a particular Citizen.

- No direct choose-any-Citizen Focus command
- A selected Tool or Keepsake placing its holder in Focus, with Supply use
  following its carrier when the intervention requires a personal actor
- A relationship or authored circumstance able to establish Focus without an
  item
- Collective narration remaining valid when nothing identifies one Citizen
- Focus governing camera, animation, principal speech or action, resolution
  language, and possible Tale attribution rather than changing the party's
  decision
- No extra action, hidden contribution, success guarantee, consequence
  immunity, Focus tally, or Focus progression
- A Focused moment entering a Tale only when the underlying event already meets
  the ordinary memory threshold

# PART V — AWAY: EXPEDITION AND RETURN

Part V begins when named Citizens leave Home and ends when Homecoming returns
their material, bodily, relational, and remembered consequences to the Colony.

**TRAVEL is the Away mirror of DWELL.** DWELL is the open, ongoing Register for
inhabiting and stewarding Home; TRAVEL is the open, ongoing Register for moving
through and reading the Field. MEET presents applicable situational decision
matrices within either mode. RISK temporarily replaces ordinary TRAVEL when a
Roadway Crossing demands immediate bodily commitment.

Launch, Rest, and Homecoming form a related family of dedicated MEETs. Launch
carries a chosen party outward, Rest creates a temporary Away Stopover, and
Homecoming receives the changed party back into Home. Each uses a grammar
fitted to its transition rather than the responses of a contested Away MEET.

## 5.1 Leaving Home

Leaving Home is the outward threshold between collective stewardship and the
lives of particular Citizens. An expedition begins with the player's commitment
of named Citizens to the unpredictable world beyond Home. Their passage through
the Home Median begins the journey itself.

### Reasons to leave

Expeditions may arise from domestic need, chosen ambition, or current world
conditions:

- **Domestic need:** the Colony lacking Sustenance, material, medicine, or
  another necessary resource
- **Chosen ambition:** the player wanting to explore, reach farther, make
  contact, establish an Outpost, or pursue another possibility beyond Home
- **World conditions:** a season, migration, resource appearance, weather
  change, road work, or other visible circumstance making departure timely
- These remaining reasons rather than formal mission types
- No required primary objective, completion checklist, or predefined measure
  of success
- The player able to leave simply to explore, change direction, follow an
  unexpected discovery, or return with a different benefit than first imagined

### Preparing for uncertainty

Citizens prepare broadly for an outside world whose particular situations
remain undisclosed.

- The Launcher presenting only current world facts the Colony could reasonably
  know, including Day Band, weather, visible traffic, known terrain and
  passages, and known bodily conditions
- No disclosure of unreached Nodes, upcoming MEETs, recommended party
  composition, ideal equipment, exact odds, or hidden passage requirements
- Standing Tools remaining with their current holders rather than being
  reassigned at Launch to counter predicted obstacles
- Supplies providing broad portable possibilities rather than bespoke answers
  to forecast encounters
- Party composition expressing which particular friends the player is willing
  to expose rather than an optimization puzzle with a correct solution
- TRAVEL revealing the Field's conditions, opportunities, and consequences
  through movement

### The Launch MEET

- The player initiating Launch from DWELL
- Launch being available only while no expedition is active
- The present Colony and prospective expedition entering one consequential
  scene
- Every mechanically eligible Citizen being available for direct player
  selection
- Eligibility depending only upon explicit state, including Home presence,
  Maturity, Guest type, bodily availability, and incompatible current
  commitment
- A Citizen committed to a Project remaining ineligible to Launch until that
  non-interruptible Project is complete
- The player freely choosing the party, with no volunteering, refusal,
  insistence, persuasion, willingness score, personality veto, or hidden
  preference
- Young Citizens, Resident Guests, Citizens already Away, and Citizens
  physically incapable of departure being ineligible
- Wounds, relationships, and history remaining visible consequences and
  expedition considerations rather than grounds for refusal
- Body Units expressing the party's physical composition without combining
  individual Citizens or their consequences
- Mouse parties carrying more individual Items across the board because every
  Mouse retains their own Tool, Supply position, and Keepsake
- The player assigning prepared Supplies while each Citizen's standing Tool
  and Keepsake remain visible
- Carry contribution, bodily state, and relevant known facts remaining legible
- The player able to revise the party, proceed, or withdraw without time
  advancing
- Confirmation fixing party membership and Supply assignment, transitioning
  directly into Away, and beginning TRAVEL
- Confirmation making this the one active expedition and keeping Away under
  player operation until Homecoming completes
- The party beginning its journey through the Home Median

### Party scale

- An ordinary Expedition requiring at least one and one-half Body Units and
  allowing no more than three Body Units
- More than one individual animal always being required to Launch
- Each Rabbit, Squirrel, and v0.5 Expedition Guest occupying one Body Unit
- Each Mouse occupying one-half Body Unit
- Three Mice therefore constituting the smallest all-Mouse party, while one
  Mouse and one full-Body-Unit Citizen also meet the minimum
- Any Core and Expedition Guest mixture being valid when it meets both the
  Body Unit range and the minimum of two animals
- A smaller party preserving more Home Civic Shares while accepting less bodily
  capacity Away
- Every departing Citizen withdrawing the Civic Share supplied by their Body
  Unit: one for a Rabbit, Squirrel, or v0.5 Guest and one-half for a Mouse
- Party membership becoming fixed at Launch
- No ordinary Colony Tier, Tool, Practice, or Outpost improvement increasing
  the three-Body-Unit maximum

### Departure and Home subtraction

- Confirmation immediately changing every selected Citizen from Home-present
  to Away
- Each departing Citizen ceasing to contribute their Civic Share to their
  current Role while retaining that Role as their standing assignment
- Role Load remaining unchanged because departure removes support rather than
  responsibility
- Role Balance recalculating immediately, with departure able to reduce
  Readiness, leave a Role Covered, or create Pressure
- A departing Citizen ceasing to support compatible Practices, passive
  throughput, and Beautification
- Passive production or transformation becoming zero when departure removes
  the final sustaining Citizen of its defined Role
- The Citizen remaining on the Colony Roster
- The Citizen's Core or Guest Residence remaining theirs, with departure not
  releasing its Housing Capacity for another Citizen
- Any Pressure created by departure becoming visible civic vulnerability
  rather than a guaranteed Home event
- Home continuing under the resulting civic state while attention is Away

### The subtraction preview

- The Launch MEET showing the exact current Colony state beside its state after
  the proposed departure
- Civic Shares removed from each Role and the resulting Role Balances
- Changes to ordinary Practice support, passive throughput, and Beautification
- Citizens unavailable because of non-interruptible Project commitment
- The preview explaining known domestic consequences without estimating the
  occurrence of a later Home MEET

### Partial-day accounting

- Civic Share availability remaining binary at any moment: the Citizen either
  contributes their whole personal Share or contributes none of it
- Launch removing that contribution immediately
- Passive production, transformation, Beautification, and any other defined
  time-based contribution accumulating only for the Day Bands during which the
  Citizen actually sustained the relevant Role
- Each eligible Day Band contributing one-quarter of the ordinary daily amount
- Fractional contributions remaining unseen and attached to their defined
  accumulators until they form whole amounts
- DAWN awarding only completed integer amounts and carrying any remaining
  fraction forward to a later DAWN
- Half-share Mouse contribution remaining legible in aggregate Role Balance,
  while fractional Resource and Project progress stays inside its accumulator
- Homecoming restoring present Civic Share contribution immediately and
  beginning accumulation again for the remaining elapsed time
- Late departure preserving contribution already made without granting a full
  day's output, and early return contributing only after the Citizen is
  actually Home

## 5.2 TRAVEL: The Field

**TRAVEL is the Away mirror of DWELL.** DWELL lets the player inhabit and
steward the Colony as a collective body. TRAVEL lets the player accompany and
guide a particular party through the world beyond domestic life.

Both are open, ongoing forms of play. Inspection, observation, and consideration
leave time paused. Direct Field movement consumes the current Day Band's travel
span, while other meaningful commitments advance time according to their owning
systems. Ordinary activity stays within its Register. MEET takes focus when a
situation benefits from a bounded decision matrix, and TRAVEL yields to RISK
when movement reaches a Roadway Crossing.

Their subjects distinguish them:

- **DWELL asks:** What can this Colony sustain, and what should it become?
- **TRAVEL asks:** Where can this party go, and what will it encounter along the
  way?

### The Field

The **Field** is the continuous Away world as experienced by a traveling party.
It extends the Colony's persistent world outward through the Median, Roadways,
Margins, and the places they contain.

Launch begins TRAVEL while the party is still moving through the Home Median.
The Colony remains physically behind them. The Median extends longitudinally
through successive Reaches, with smaller roads sometimes cutting across it at
their borders. Each Reach also contains its corresponding Main Roadways and
Margins.

- Upcorridor and downcorridor movement carrying the party along the Median
- A Reach-border road requiring RISK before the party can continue into the
  next Reach
- A Main Roadway requiring RISK before the party can enter a Margin or return
  from it
- Each Margin extending between its Main Roadway and the hard boundary of its
  Sound Wall
- Nodes, Outposts, paths, shelters, vegetation, drainage, debris, and human
  infrastructure remaining fixed within that geography
- Return carrying the party back through the same persistent world rather than
  selecting Home from a destination menu

### The world underfoot

The Field is authored at animal scale even while TRAVEL presents it from above.
Soil, grass, roots, drainage, barriers, shoulders, wreckage, culverts, signs,
litter, water, and human maintenance form mechanically operative terrain.

Grade, cover, exposure, visibility, sound, weather, and continuity of passage
determine where the party can move and what it can perceive. A short human-scale
distance may therefore contain substantial animal-scale geography.

The Median provides relative sanctuary with local dangers of its own. Margins
offer greater abundance alongside contamination, disturbance, predators,
mowing, flooding, human access, and River Spume. Roadways function as moving
barriers that require a distinct bodily Crossing.

One physical feature may function simultaneously as path, landmark, shelter,
resource, obstruction, and danger. Landscape differences change the party's
actual play.

### The party in TRAVEL

The party moves through TRAVEL as one controllable Field subject while every
member remains named, visible, and individually inspectable.

- Destination, elapsed time, ordinary movement, Carry, and general burden
  remaining party-level facts
- Tools, Supplies, Keepsakes, wounds, Exposure, relationships, and
  personal consequences remaining attached to particular Citizens
- Species traits arising from the actual bodies present
- No formation grid, marching order, individual pathfinding commands, or
  separate movement action for every Citizen
- Separation occurring only through an explicit consequence rather than
  routine navigation

### Attention while Away

An active expedition keeps Away under player operation until Homecoming. Home
remains part of the same world and continues under the commitments already
established there.

- The player able to inspect Home state, Citizens, Civic Balance, Project
  progress, Telegraphs, and forecasts through the established information
  lenses
- Ordinary DWELL camera operation, construction, Role reassignment, new Project
  commitment, and another Launch remaining unavailable during the expedition
- The party moving, resting, engaging Nodes, and entering Away decisions only
  while directly operated by the player
- No autonomous travel, Node use, Crossing, or Away decision occurring while
  attention is briefly taken by an information view or cross-modal MEET
- Day-Band changes, DAWN, Projects, passive production, Civic Balance, Pressure,
  and known world conditions continuing at Home
- DAWN showing a concise Home accounting summary and returning operation to the
  party at its persistent Field position
- A Home situation that crosses the MEET threshold able to interrupt Away,
  resolve through its applicable choices and time, and then return operation to
  the same party position
- Any world-time advancement caused by that Home MEET updating the shared Day
  Band and conditions while the party remains stationary

### Movement, time, and range

The Day Band is the sole mechanical unit of world time. Every elapsed action
resolves through whole Day Bands or through the owning situation's explicit
timing.

#### Direct movement and the travel span

The player directly drives the party through the top-down Field. Directional
input moves one compact party figure composed from the actual Citizens present.
The figure remains the controlled expression of those particular lives rather
than an abstract expedition state.

Each Day Band begins with a projected **travel span**: the amount of
terrain-adjusted movement the party can complete before world time advances.
The interface expresses the remaining span through the ground still credibly
reachable from the party's present position rather than through a second unit
of time.

1. The player drives the party continuously across physically traversable
   ground.
2. Actual path length consumes the current travel span, including detours and
   backtracking.
3. Terrain, weather, Carry, bodily condition, Rabbit composition, and pushing
   determine how much ground that span can cover.
4. Stopping movement pauses further consumption at the party's precise
   persistent position.
5. Exhausting the span pauses movement and advances the world to the next Day
   Band.
6. The new Band realizes its light, traffic, weather, Colony state, and renewed
   span before movement continues.
7. Exhausting Night reaches DAWN, where the player explicitly proceeds through
   daily accounting before Morning begins.

Travel span is spatial capacity within the current Band. It creates no Time
Mark, fractional time currency, or additional action allowance.

#### Nodes within a Day Band

- Passing, observing, or arriving at a Node not automatically consuming another
  Band
- A brief uncontested interaction able to resolve within the Day Band that
  reached it
- Work that genuinely occupies time advancing the next Band
- A consequential situation opening MEET
- MEET presentation itself carrying no time cost, with its selected action
  determining whether time advances
- Several nearby Nodes able to remain visible and available without the party
  being entitled to resolve a fixed number of them
- No replacement encounter allowance, action-point pool, or hidden half-Band

### Terrain, pace, range, and burden

#### Paths and projected reach

TRAVEL turns physical geography into direct movement choices. The Field
outlines the ground the party can still credibly reach during the current Day
Band under known conditions and identifies known destinations within it.

- Projected reach reflecting terrain, distance, weather, burden, bodily
  condition, and Rabbit contribution
- Directional input carrying the party along a physically continuous path
  through the ground that is presently legible
- Grade, surface, cover, exposure, drainage, obstruction, and shelter making
  different paths meaningfully distinct
- Road-edge paths generally offering greater abundance and interruption;
  Sound-Wall-edge paths generally offering quieter, slower passage
- No path being universally best: the chosen way determining the kind of day
  the party undertakes
- The projection remaining honest without revealing unknown situations, exact
  odds, or an optimal path
- Ordinary movement reaching the ground the interface presents unless a visible
  physical obstruction or consequential situation interrupts it
- Altered, opened, or obstructed paths changing future projected reach through
  their actual physical effects
- The party retaining its precise Field position whenever it stops, changes
  course, or turns back

#### Rabbit contribution to TRAVEL

Rabbit bodies increase the party's normal TRAVEL rate on an absolute
three-Body-Unit scale:

**Rabbit TRAVEL multiplier = 1 + (Rabbit Body Units ÷ 3)**

| Rabbit Body Units | Normal travel span |
|---:|---:|
| 0 | 1× |
| 1 | 1⅓× |
| 2 | 1⅔× |
| 3 | 2× |

- Rabbit contribution depending upon bodies present rather than their
  percentage of the current party
- An underfilled two-Rabbit party therefore moving at 1⅔× rather than
  receiving the full three-Rabbit rate
- One Rabbit contributing the same pace benefit whether the remaining party
  capacity is filled or empty
- Non-Rabbit party members imposing no slowest-member penalty
- Underfilling the party preserving Home Civic Shares without amplifying
  Rabbit contribution
- Terrain, weather, burden, and bodily condition modifying the resulting
  projected reach
- Rabbit contribution extending distance available within a Day Band rather
  than the number of Day Bands available
- No additional RISK action, MEET Round, Carry, or experienced time
- The Field showing projected reachable ground without needing to expose the
  underlying multiplier

#### Food during Away

Ordinary food is abstracted during Away. Away Citizens continue to count toward
the Colony's ordinary Sustenance demand. Expedition range and return remain
grounded in the party's bodily and environmental circumstances.

- No ration position, provision meter, daily food deduction, Hunger track, or
  automatic starvation procedure
- Food recovered in the Field able to become Cargo brought Home without also
  becoming a separate expedition resource
- Expedition range constrained by time, terrain, weather, known shelter,
  bodily condition, accumulated burden, RISK, and the physical return journey
  rather than a food clock

#### Carry and the growing haul

**Carry** is one public, party-wide capacity for Cargo. The amount carried is a
physical fact that directly changes travel and danger through projected reach
and situated consequence.

- Each Rabbit or Squirrel Body Unit contributing ten slots of secured Carry
- Each individual Mouse contributing six slots, so one Mouse Body Unit provides
  twelve and a full six-Mouse party provides thirty-six
- Each Expedition Guest contributing the fixed species value listed in Chapter
  4.3, from Snake's six slots to Raccoon and Fox's twelve
- Tools, Supplies, and Keepsakes remaining in their personal positions without
  consuming Cargo slots
- Current and maximum secured Carry remaining visible to the player
- Added Cargo directly contracting projected reach and entering applicable RISK
  or MEET situations as physical burden
- The Field expressing travel cost through its changing reachable ground rather
  than a separate burden score, threshold band, or hidden Load value
- Carry Tools increasing or reorganizing Cargo capacity while their holders
  remain present and capable
- Squirrel Strained Carry providing optional capacity beyond secured Carry under
  its own risk rule
- The player choosing what to take, leave, protect, or abandon whenever
  available capacity or a situated consequence requires it

#### Squirrel Strained Carry

**Strained Carry** represents the inherently precarious additional haul a
Squirrel holds through mouth, bulging cheeks, and awkward exterior carriage.
Each Squirrel Body Unit contributes ten optional Strained Carry slots beyond
the party's secured Carry.

- All Strained Carry forming one shared party capacity rather than separate
  personal inventories
- Only fungible Cargo entering Strained Carry; Artifacts, Keepsakes, named
  objects, and other meaning-bearing possessions requiring secured carriage
- Strained Cargo contracting projected reach and affecting situated danger like
  every other part of the haul
- One visible Jostle check occurring for each Squirrel whenever a Day Band ends
  after the party has materially moved while carrying any Strained Cargo

**Jostle chance = 10% × (current Strained Cargo ÷ maximum Strained Carry)**

- No Jostle check when Strained Carry is empty or the party does not travel
- A successful check immediately and visibly losing one randomly selected
  Strained Cargo unit without creating a recoverable ground object or marker
- The fill proportion being recalculated after each loss before another
  Squirrel checks
- The current chance and each result remaining visible rather than being hidden
  until Homecoming
- RISK or MEET able to make Strained Cargo an explicit stake when the situation
  warrants it
- A RISK or MEET consequence that already resolves the danger to Strained Cargo
  replacing the ordinary Jostle checks for that elapsed Band rather than
  charging the same burden twice

#### Rest, Stopover, and safe range

A rested party may spend three Day Bands traveling at its normal projected
reach. It may then push through as many as three further TRAVEL Bands at an
increasing pace penalty before rest becomes mandatory. This is one shared
bodily cadence for the whole party.

| TRAVEL Band since Rest | Projected-reach multiplier |
|---:|---:|
| 1–3 | 1× |
| 4 | ¾× |
| 5 | ½× |
| 6 | ¼× |
| 7 | Unavailable until Rest |

- Every Day Band in which the party materially travels counting when that Band
  ends, including when another action advances time before the travel span is
  exhausted
- The player able to rest earlier
- Every new traveling Band after the third being visibly identified as a push
  before movement begins
- Rabbit contribution, terrain, weather, bodily condition, and Cargo
  establishing normal projected reach before the push multiplier applies
- A party that completes six traveling Bands being unable to TRAVEL again until
  it rests
- MEET and Node work neither counting as TRAVEL nor resetting the cadence unless
  the resolved action explicitly provides rest
- The current number of traveled Bands and the need to rest remaining visible
  in the party interface
- Pushing creating no automatic Wound or Exposure charge; its universal
  penalty being diminished reach while Jostle and situated danger continue to
  operate normally
- RISK and MEET able to treat extended exertion as relevant context without
  creating another generic Fatigue statistic or automatic penalty
- No individual sleep schedule, stamina statistic, or hidden exhaustion meter

A **Rest MEET** may be initiated wherever the party can physically stop. It
presents how the party sleeps, settles, keeps watch, and cares for immediate
needs in the conditions actually present. Completing it advances one Day Band,
resets the three-Band travel cadence, and creates a **Stopover** at the party's
current persistent location.

- Open or poor ground permitting rest while exposing the party to contextual
  weather, disturbance, Exposure, or Cargo consequences
- Natural shelter improving the available protection without becoming a second
  Outpost class
- A usable Outpost providing reliable rest and low-level healing
- Ordinary Field rest restoring travel capacity without automatically healing
  wounds
- Outpost healing neither removing Maiming nor replacing serious care at Home
- The party remaining Away throughout a Stopover

Known shelter defines safer range, not a hard boundary. Home, natural refuges,
Outposts, and other established safe stops show where a traveling day can end
with greater confidence. The player may press beyond that chain, stop in
exposed ground, or directly travel back toward Home.

- No arbitrary locked-zone gate or mandatory shelter itinerary
- Projected reach continuing to describe physical travel during the current
  Band while known shelter makes the consequences of stopping legible
- Distance from Home, passing time, current conditions, bodily state, Cargo,
  and the remaining return journey informing how far the player chooses to
  press
- Turning back being an ordinary player choice to TRAVEL through the Field
  toward Home rather than a separate action or subsystem

#### Field Cards

**Field Cards** are occasional interruptions that come to the party between
Nodes. They keep the Corridor active while Nodes remain the primary intentional
content of TRAVEL.

- One 10% Field Card check following each exhausted travel span
- At most one Field Card occurring within a Band
- No check when RISK or another consequential MEET has already occupied that
  Band
- The next two otherwise-eligible exhausted travel spans becoming ineligible
  for another Field Card after one occurs
- Selection reflecting the actual Reach, position, terrain, season, Day Band,
  weather, and persistent world state
- Candidate families including opportunity, environmental change, passing
  animals, and human disturbance
- A minor card directly changing or revealing the Field without opening a
  decision matrix
- A consequential card opening MEET with the present party, terrain, stakes,
  and available responses
- The card occurring as that travel span ends unless the action chosen in its
  MEET genuinely requires additional time
- No player-held deck, draw action, guaranteed interruption quota, or hidden
  replacement encounter allowance

**Nodes are the meal; cards are the weather.** Nodes remain the party's primary
intentional Away content. Field Cards punctuate movement and keep travel
unpredictable without displacing the world the player chose to explore.

- Landscape Voice able to accompany first entry into a new or materially
  changed Reach, first sight of an important destination, an overlook, or a
  meaningful change of scale

## 5.3 RISK: Crossing

**RISK is the Away Register dedicated to Crossing a Roadway.** It concentrates
the highway's traffic, noise, fumes, wind, width, broken sightlines, and
human-scale speed into one brief bodily threshold. RISK temporarily takes focus
from TRAVEL and resolves the Crossing in continuous action. A sufficiently
consequential result may then open MEET.

### Road scale and Crossing

- Main Roadways carrying the broadest, fastest, and most exposed traffic bands
  between the Median and Margins
- Smaller roads cutting across the Median at some longitudinal Reach borders
- Either road scale opening RISK whenever the party must cross it
- The selected Core Species supplying the same planning and execution grammar
  at both scales
- Width, traffic, surface, sightlines, weather, River Spume, and far-side refuge
  determining the actual information, difficulty, and consequence range
- A lightly trafficked Reach-border road able to provide a gentler Crossing
  while retaining real time, motion, uncertainty, Exposure, and consequence
- Every completed Crossing carrying the party fully to its far side

### One Roadway, three Crossing experiences

The same traffic and environmental simulation underlies every Crossing, but
the Colony's Core Species determines how the player reads, plans, and
experiences it.

| Core Species | RISK asks | Planning form | Execution |
|---|---|---|---|
| **Rabbit** | When does the Roadway open? | Choose a traffic window, broad line, and far-side refuge. | One uninterrupted sprint. |
| **Mouse** | Where can continuity be made? | Connect three to six body-credible pavement features. | One continuous chained scurry. |
| **Squirrel** | How can movement flow through traffic? | Set a trajectory with one or two planned redirects and a far-side anchor. | One continuous vector run. |

- Species difference changing the fundamental play experience rather than
  merely modifying speed, odds, or presentation
- Rabbit treating the whole Roadway as one temporal opening
- Mouse revealing pavement-scale terrain through continuity among meaningful
  features
- Squirrel seeking a viable line that moves through traffic geometry
- Each grammar retaining the shared contour **Plan → Commit → Continuous Run →
  Resolve**

### Guests and Flyers within the Core Species grammar

The Colony's Core Species supplies the ground Crossing grammar for every party.
A Rabbit Colony's party therefore experiences Rabbit RISK regardless of its
granular composition, including a party composed entirely of Guests.

- Each land-bound Guest's actual body determining which ground, refuge,
  opening, and movement choices remain physically credible within that grammar
- A large Guest in a Mouse Colony therefore requiring body-credible features
  rather than being drawn through a Mouse-sized crack
- Guest Signatures able to change an applicable choice only where their defined
  circumstances actually arise
- Land-bound Guests participating in the ground party's continuous Crossing

Crow and Gull are the only Guest Species whose bodies produce a different RISK
experience. Both use one shared **Flyer** expression during the same Crossing:

- The player making one Crossing commitment
- The ground party performing the Colony's Core Species grammar
- Crow and Gull automatically attempting a parallel flight during the same
  continuous Run
- River Spume, vehicle turbulence, wind, weather, debris, visibility, and
  credible launch and landing space affecting the flight
- A Flyer able to cross cleanly, be buffeted, lose eligible ordinary Cargo, or
  be injured
- The Flyer's result able to differ from the ground party's result but resolving
  visibly with the Crossing
- Flight bypassing neither elapsed time, RISK, Exposure, nor consequence and
  introducing no aerial route, separate Register, rescue system, or additional
  minigame

Gull's **READ — Long View** may improve the information available before
commitment when its stated conditions apply. Crow's **HANDLE — Trialwork**
provides no general Crossing or aerial-information benefit.

### The Staging Post

A **Staging Post** is the immediate ground from which a party attempts a
Crossing. It names the present Roadway edge and the conditions from which the
party observes, waits, plans, and commits.

- Staging exposing current traffic, Day Band, weather, River Spume, far-side
  refuge, and Cargo
- The player able to plan and commit, wait, or resume TRAVEL away from the
  Roadway
- Waiting advancing one Day Band and realizing that Band's traffic conditions
- Planning and committing within the current Band adding no duration beyond the
  TRAVEL movement that brought the party there
- Staging remaining a compact commitment view rather than a tactical loadout or
  positioning phase

### Shared RISK contour

1. **Plan.** Read the present Roadway and construct one complete
   Core-Species-conditioned passage.
2. **Commit.** Explicitly accept the plan; strategic revision then closes.
3. **Continuous Run.** The party carries out the complete Crossing without the
   Roadway pausing for turns or renewed planning.
4. **Resolve.** Determine the party's global passage result, then attach any
   bodily or material adversity to the Citizens and Cargo that experienced it.
5. **Continue.** Return the party to TRAVEL on the far side, or open MEET when a
   consequence requires focused situational choice.

### Planning before commitment

RISK tests the player's judgment before Commitment. The Continuous Run then
realizes the complete plan through the party's bodies and present conditions.

- Traffic able to remain animated during observation while planning may pause
  or step as accessibility and legibility require
- Rabbit selecting a represented traffic window rather than requiring a
  perfectly timed real-time button press
- Mouse selecting its physical features and Squirrel setting its trajectory and
  planned redirects before Commitment
- **Commit** serving as the final mechanical input into the Crossing
- The Continuous Run executing the complete plan without steering, quick-time
  prompts, reaction buttons, or mid-Roadway replanning
- Camera control and attention able to remain available without altering the
  result
- A new decision waiting until the party reaches the far side and RISK has
  applied the Crossing's consequences before MEET opens
- RISK never freezing a Citizen beneath an approaching vehicle to request a
  player choice
- The Run remaining the brief embodied and uncertain realization of the
  player's constructed plan rather than a detached cinematic reward

### Passage and consequence

Every committed Crossing carries the entire party to the far side. RISK's
uncertainty lies in what that passage costs.

- The party resolving once as a group rather than checking every Citizen
  separately
- The Continuous Run never stopping at a refuge, opening a mid-Roadway MEET,
  requiring rescue from traffic, or leaving a Citizen stranded in the Roadway
- Delay, Exposure, far-side separation, Cargo loss, wounds, Maiming,
  Tharn, or rarer consequences being applied visibly after the Run
- Any decision created by those consequences opening as a MEET from the far
  side
- Adversity following Body Units rather than raw headcount, so a Mouse party
  receives no additional checks merely because it contains more named Citizens
- An ordinary Mouse adversity result affecting one named Mouse
- One causal result able to produce connected effects without stacking
  unrelated penalty rolls for the same event
- Maiming, Tharn, or death arising only as a rare, visible consequence of an
  adequately severe event rather than as opaque routine attrition
- Crow and Gull retaining their separately resolved Flyer outcomes within the
  same completed Crossing
- A Citizen's first RISK Crossing of the current expedition establishing the
  initial Exposure floor defined in Chapter 5.6 after RISK resolves
- Wounds, Maiming, and Exposure caused by RISK entering their ordinary
  persistence mechanics after the Crossing resolves; an awarded Exposure gain,
  for example, still being doubled by an unstabilized Wound

### Return Crossing

Return Crossing preserves the cost and tension of each previously crossed
Roadway through a lighter ordinary procedure. At the Staging Post on the
outward side, the player reads current conditions and chooses whether to cross
homeward now or wait.

When the player chooses to cross, the party's actual circumstances select one
of two presentations:

- **Automatic Return:** the ordinary result. The party crosses continuously
  without opening the planning interface. A hidden adjudication produces a
  clean return or a bounded penalty, then shows and applies that result on the
  homeward side.
- **Full RISK:** an uncommon result whose likelihood rises under difficult
  conditions. The ordinary Core-Species planning grammar opens and receives
  its own Commit before the Continuous Run. Full RISK still carries the party
  to the homeward side, but its end consequences may reach the complete RISK
  range.

Return adjudication responds to:

- Current traffic and Day Band
- Weather, visibility, and River Spume
- Cargo and Strained Cargo
- TRAVEL Bands since Rest
- Party bodies and applicable Guest Signatures

Automatic Return uses those present circumstances to produce a clean passage
or a bounded penalty such as delay, Exposure, loss of eligible fungible Cargo,
or a Wound. Conditions able to reach Maiming, Tharn, or death invoke Full RISK.
Every result is shown after the party has cleared the Roadway, and every return
consequence leaves the party on the homeward side.

- Landscape Voice able to accompany emergence onto the far Margin after a
  consequential Crossing without interrupting unresolved RISK

## 5.4 Nodes in the Field

The Field is continuous, but some places retain particular meaning. A **Node**
is a recognizable place whose material, ecology, shelter, inhabitants,
alteration, or history can matter across more than one visit.

TRAVEL reveals and carries the party among Nodes. A Node opens MEET only when
the party encounters a consequential situation there.

### What makes a Node

- A fixed location in the Field rather than a temporary event
- Persistent state able to change through season, weather, occupation,
  disturbance, use, or player choice
- A place the party may revisit through continuous Field movement
- Relevant qualities becoming known through direct observation, interaction,
  and persistent change
- A known, quiet Node remaining part of ordinary TRAVEL

### Node qualities

Each Node may express several overlapping qualities.

| Quality | Examples | State that may persist |
|---|---|---|
| **Ecological** | Bramble patch, seed fall, insect bloom, water source | Season, abundance, recovery, disturbance |
| **Material** | Toolbox, litter catch, carcass, construction debris | Contents, condition, depletion, alteration |
| **Shelter** | Pipe, root pocket, hollow, culvert ledge | Safety, exposure, damage, occupation |
| **Relational** | Den, Guest camp, claim, meeting landmark | Occupant, relationship, terms, prior choices |
| **Human-made** | Drain, grate, barrier, vehicle cavity, worksite | Configuration, access, activity, hazard |

One Node may have several qualities. A culvert might simultaneously be
human-made, sheltering, ecological, and occupied.

**Hazard** is a current condition or present animal at a Node rather than a
Node family. **Memory** is history attached to any Node rather than a separate
kind of place.

### Nodes and MEET

- A quiet Node requiring no decision remaining part of TRAVEL
- A meaningful use, change, claim, opportunity, or danger opening a contextual
  MEET
- Contest existing only when another animal, group, or condition opposes what
  the party is trying to do
- Contest being a current situation rather than a permanent Node
  classification
- MEET presenting the choices applicable to the current situation
- Outcomes changing the Node, party, relationship, or world directly

### Renewal and change

Ecological Nodes may replenish or transform according to their actual season
and condition. Repeated taking, disturbance, neglect, weather, or another
animal's use may change what remains. Renewal follows authored ecological
state.

## 5.5 MEET: consequential situations

Away MEET brings the party's present location, bodies, Cargo, Items,
relationships, and accumulated consequences into focused choice. The party
acts through the people, capabilities, possessions, and relationships actually
present with it.

Chapter 1.5 governs the shared MEET contract. This chapter defines how that
contract specializes when particular Citizens meet the Field.

### Situational opposition

Opposition exists when an animal, group, or condition presently resists what
the party is trying to do. Contest is a state of that particular situation.

An unopposed opportunity receives direct contextual responses: gather a
particular material, provide care, enter shelter, examine visible evidence, or
leave it alone. Its display presents those concrete actions directly.

When opposition exists, responses draw from five stable families:

| Family | Meaning |
|---|---|
| **CONTEST** | Overcome, resist, hold, seize, protect, or endure directly. |
| **EVADE** | Bypass, escape, hide, distract, or use terrain to avoid opposition. |
| **PARLEY** | Ask, offer, trade, bargain, persuade, deceive, or invoke a relationship. |
| **YIELD** | Concede a particular stake, claim, possession, priority, or cost to preserve something else. |
| **WITHDRAW** | End the party's participation and leave the objective or situation behind. |

### The fixed contested display

Every contested Away MEET shows the five families in this order:

**CONTEST → EVADE → PARLEY → YIELD → WITHDRAW**

- A family becoming active only when at least one physically and situationally
  credible response belongs to it
- Each active family containing exactly one concrete response in the current
  Round
- The response stating the particular action available in this situation
- An inactive family remaining in its established position, greyed and paired
  with a concise, knowable reason
- No greyed family implying that the player has overlooked a puzzle solution
- An unavailable explanation revealing no fact the party could not know
- No weak or redundant response being invented merely to activate a family
- Tools, Supplies, relationships, and Guest Signatures already present being
  considered when determining which families are active or altered
- Provisional selection revealing the exact applicable expressions before
  Commit under the shared MEET sequence
- Different Tools, Supplies, relationships, Keepsakes, and Signatures acting as
  expressions of that one response rather than opening a submenu of parallel
  actions within its family
- A changed situation able to present a different response under the same
  family in a later Round
- The fixed display belonging only to contested Away MEET, never to an
  unopposed opportunity, Home MEET, Launch, Rest, or Homecoming
- These response families creating neither combat, tactical positioning, nor a
  universal success check

### Group result and personal consequence

An Away MEET resolves the party's shared objective before assigning particular
consequences. Personal consequence follows physical and narrative cause rather
than Focus or a separate check for every Citizen.

1. Resolve what the party collectively achieves, prevents, accepts, or leaves
   unfinished.
2. Identify the Citizens actually exposed by what they carried, used,
   protected, confronted, or were already suffering.
3. Attach a consequence deterministically when one Citizen clearly bears it.
4. When several Citizens are equally exposed, select randomly from that causal
   set.
5. Show the result immediately, including its cause and its effect on the
   party's continuing choices.

- Focus able to coincide with the affected Citizen without causing or
  redirecting the consequence
- Raw party headcount never creating one consequence check per Citizen; a
  six-Mouse party not being penalized merely for containing six named lives
- One principal personal consequence ordinarily arising from a Round
- One causal incident able to produce linked effects, such as a Wound and
  Exposure, without adding unrelated penalties
- A clearly authored group-scale event able to affect several Citizens when
  its actual physical or social cause requires it
- Group success never granting personal immunity, and personal harm never
  automatically erasing the group result

### Carried expressions Away

Only capabilities physically present with the party can shape an Away
response.

- A relationship mattering only when a present participant or the situation's
  known history makes it relevant
- A Keepsake able to inform a response through recognition without becoming
  the Round's active item
- Offering, using, surrendering, or placing a Keepsake at stake making it the
  active item, so that no Tool or Supply can also be committed in that Round
- Using or risking an Item making its carrier causally involved and therefore
  eligible for Focus and applicable personal consequence
- A Guest Signature remaining a bodily capability rather than an Item and able
  to coexist with the active Item when its defined circumstances apply
- No expression supplying an unspecified bonus, extra action, or immunity from
  consequence

### Persistence and aftermath

An Away MEET ends by returning every changed fact to the Field, party, or other
system that owns it.

- Spent Supplies remaining spent and Tool hazard remaining resolved
- Gained or abandoned material changing the party's Cargo immediately rather
  than entering the Colony's stores before Homecoming
- Injury, Exposure, relationships, and possessions remaining attached to
  the particular Citizens and objects that bear them
- A changed Node, inhabitant, resource, claim, or physical feature retaining
  its actual new state without receiving a generic **cleared** or **completed**
  tag
- An unresolved situation continuing into another Round only when the changed
  circumstances still meet the MEET threshold
- A resolved situation returning the player to TRAVEL or the next applicable
  Register without a redundant dismissal choice
- Campaign Memory receiving an event only when it independently meets that
  system's selection rules, not merely because a MEET occurred
- Landscape Voice able to accompany a resolved moment whose meaning is
  inseparable from its physical setting

## 5.6 Exposure and Bodily Consequence

Exposure and bodily consequence belong to particular Citizens throughout
Away. TRAVEL circumstances, RISK outcomes, MEET, and Stopovers may create or
alter them. This chapter defines their shared persistence, consequence,
stabilization, and recovery.

### Accumulated Exposure

**Exposure** is a hidden per-Citizen measure of accumulated life beyond
ordinary safety. It records increasing vulnerability to personal consequence
and is communicated through observable behavior, voice, narration, and
contextual warning.

- Each Citizen having six accumulated Exposure steps above baseline, tracked
  internally from 0 through 6
- Each Citizen's first RISK Crossing of an expedition setting their Exposure to
  at least 1 after the Crossing resolves
- This initial floor not being an Exposure gain, receiving no Wound multiplier,
  and adding nothing when the Citizen is already at 1 or higher
- Any additional Exposure caused by that Crossing applying afterward as its
  distinct resolved consequence
- A resolved circumstance that explicitly creates Exposure ordinarily adding
  one step
- One cause creating at most one base Exposure gain rather than charging the
  same danger again across TRAVEL, RISK, MEET, or another resulting transition
- Exposure rising through actual hazardous circumstances and committed choices
  rather than automatically for elapsed Day Bands, MEET Rounds, or ordinary
  time Away
- Exposure stopping at 6 without guaranteeing the worst permitted consequence
  or widening the situation's valid range
- Exposure imposing no standing penalty to Carry, movement, Civic Share,
  response availability, player control, or any Citizen's aptitude
- Exposure never causing a Citizen to refuse the player
- The situation and committed response first determining whether personal
  consequence is possible and which Citizens are causally exposed
- Causal target selection occurring without reference to Exposure
- Outside RISK's defined exception, the selected Citizen's Exposure then
  weighting resolution toward the more serious end of that situation's valid
  personal-consequence range
- When genuine uncertainty remains, one hidden Exposure escalation check using
  a chance equal to 10% for each current Exposure step
- A successful check moving the selected Citizen's result one position toward
  the serious end of that situation's ordered valid range
- No check when the result is already determined or already occupies the most
  serious valid position
- One consequence receiving at most one Exposure escalation check, with
  Exposure neither consumed nor checked separately for linked effects
- Exposure increasing neither the number of consequences nor the range of
  outcomes the situation can support
- Exposure never inventing a consequence unrelated to the present situation or
  changing the party's shared result
- Distinctions, Keepsakes, After-names, relationships, and other favorable
  developments arising from what a Citizen actually did and what happened,
  never from a favorable Exposure roll
- The player reading Exposure through bodily behavior, voice, narration, and
  contextual warnings rather than a number, meter, or named Condition ladder
- Wounds, Maiming, and Tharn remaining distinct persistent facts rather
  than being folded into Exposure
- A normal one-step Exposure gain becoming two when the Citizen already has an
  unstabilized Wound
- Each Citizen having only one possible Wound state, so the multiplier never
  stacks or compounds
- One resolution using the Citizen's state before that resolution, so a Wound
  created by the incident does not double Exposure created by the same incident
- Exposure never worsening a Wound directly into Maiming or death

For example, if a hawk MEET supports a range from no lasting harm through
additional Exposure to a Wound, greater Exposure weights the selected Citizen
toward the latter outcomes. It cannot introduce Maiming or death unless the
situation is independently severe enough to permit them.

### Forms of personal consequence

Exposure, Wounds, Maiming, Tharn, and death are distinct forms of consequence.
Each follows its own causes and persistence rules.

| Consequence | Meaning |
|---|---|
| **Wound** | A single named, recoverable bodily-injury state. It constrains only actions the injury physically affects, doubles new Exposure while unstabilized, and recovers through credible care and time. |
| **Maiming** | The lasting bodily change caused by a maiming injury, not a larger class of Wound. The incident also creates an acute Wound; that Wound may heal while the Maiming remains. Rehabilitation can establish adapted participation without erasing the history. |
| **Tharn** | An acute shutdown during immediate danger. The Citizen cannot continue the present action, and saving them supersedes the MEET's former objective. |
| **Death** | A rare, final consequence available only in an explicitly severe situation whose fatal stakes were legible before Commit. |

- No Health points, Spirit bar, generic damage meter, or Condition ladder
- Each Citizen being either Wounded or not Wounded, with no multiple Wounds,
  Wound slots, or stacking Wound states
- A Wound result affecting an already-Wounded Citizen able to change the
  injury's description and set its remaining Healer-Days to the greater of its
  current remainder or the new incident's authored one-to-three requirement,
  but never creating a second Wound or becoming Maiming unless Maiming is
  independently within the situation's valid range
- A maiming injury establishing one connected pair: an acute Wound governed by
  ordinary stabilization and recovery, and a lasting Maiming governed by
  adaptation and Rehabilitation
- Healing or stabilizing the accompanying Wound never removing the Maiming
- Tharn remaining an immediate acute break rather than a synonym for
  unconsciousness or accumulated damage
- One incident able to create linked facts without using severity as permission
  to stack unrelated penalties
- Every consequence persisting across Registers and returning through
  Homecoming
- Care able to recover a Wound or Tharn or support adaptation to Maiming without
  erasing what happened
- Death never arising from Exposure alone, routine attrition, an unattended
  roll, or an off-screen event

### Tharn

**Tharn** is MEDIAN's sole deliberate loan-word from Richard Adams's
*Watership Down*. In MEDIAN it names an acute bodily shutdown under
overwhelming strain. It may affect any Species.

- Tharn arising only from an event whose immediate physical or sensory
  circumstances credibly support shutdown
- Accumulated Exposure and an unstabilized Wound increasing susceptibility
  without ever causing Tharn by themselves
- An unstabilized Wound counting as two additional Exposure steps when Tharn is
  within the event's valid consequence range
- The combined escalation chance stopping at 80%, with the Citizen's single
  Wound contribution applied no more than once
- Rest or Remedy stabilization removing the Wound contribution
- RISK able to produce Tharn from an adequately severe Crossing while remaining
  exempt from pre-existing Exposure and Wound weighting
- No Exposure maximum, Wound, ordinary inconvenience, or routine loss opening
  a separate Tharn check

The possibility of Tharn is never stated or highlighted before resolution. The
interface shows the actual situation, the Citizen's observable state, and every
ordinary fact an attentive player might use to recognize the danger, but it
provides no Tharn label, icon, warning, preview, or probability. Its arrival is
meant to be shocking without depending upon an unobservable cause.

When Tharn occurs, the game names it explicitly and immediately makes its
effect legible. The Citizen cannot continue the present action. Any group result
already resolved remains true, but an unfinished objective can no longer be
pursued within that MEET.

If danger remains, the next Round replaces the former subject with securing the
struck Citizen. **YIELD** and **WITHDRAW** are the ordinary active families:
the party concedes what the situation demands or leaves with the Citizen. A
different family may remain active only when its response directly makes that
rescue or departure physically possible, never to continue the superseded
objective. Every response retains the struck Citizen; abandoning them is not an
option. Once they are secure, the MEET closes into aftermath or an applicable
Rest MEET.

Tharn then makes Rest mandatory. The party cannot activate another Node, enter
RISK, or resume another expedition objective while any member remains Tharn.
Completing one Rest MEET ends Tharn and resets the party's ordinary travel
cadence without reducing the Citizen's accumulated Exposure or clearing any
Wound or Maiming. Remedy cannot shorten, replace, or improve this recovery.

### Remedy expressions

A Remedy may be committed as the Round's one active item expression when an
applicable response concerns a bodily consequence. Its exact preventive,
stabilizing, or lessening effect is shown before Commit, and the Supply is
consumed when committed.

- Remedy stabilizing the treated Wound through Homecoming, preventing that
  Wound from doubling new Exposure without healing it
- A completed Rest MEET providing the shorter stabilization defined above
- Remedy applied to a maiming injury acting upon its acute Wound while its
  lasting Maiming remains
- Remedy having no effect on Tharn
- Remedy able to be used for a party member through an applicable situational
  response or Rest MEET
- Remedy able to enter PARLEY when another participant has a credible bodily
  need, allowing offered treatment or shared care to open the response, change
  its terms, protect a bodily stake, or affect the resulting relationship
- PARLEY use depending upon the Remedy's actual medical relevance rather than
  treating it as a general Offering or unit of barter
- Another participant remaining free to refuse care, terms, relationship, or
  repayment
- Remedy never guaranteeing the party's shared result or erasing the persistent
  history of the fact it treats

### Wound Recovery Projects

A **Wound Recovery Project** provides the Wounded Citizen's sustained care at
Home through the ordinary Project Queue.

- The Project requiring one completed usable Hearth and exactly one named
  Citizen committed as Healer
- The Hearth needing to be available: it cannot already be committed to the
  care of Young Citizens, another Wounded Citizen, a Rehabilitation Project, or
  another active Project
- The Hearth providing care rather than Residence; the Patient remains housed
  through the ordinary Residence system
- The Patient being the Project's named target rather than a committed worker
- A Wounded Citizen who is present at Home creating one Healer Load until the
  Wound is cleared, whether or not its Recovery Project can begin immediately
- Project entry not itself removing the Patient's Civic Share; availability
  following only the actions that the actual Wound physically prevents
- Each Wound receiving an authored recovery requirement of one to three
  Healer-Days without creating named severity tiers
- The committed Healer contributing one Healer-Day at each DAWN, so recovery
  takes the same one to three elapsed Dawns and cannot be accelerated by adding
  Healers
- The Project making no progress while its Hearth is unusable, while remaining
  committed under the ordinary non-interruption rule
- Completion at DAWN clearing Wound, releasing the Hearth and Healer, and
  preserving the event and recovery wherever Campaign Memory warrants them
- The acute Wound accompanying Maiming using the same binary Wound state and
  Recovery Project; completion clearing Wound while leaving Maiming intact
- Rehabilitation remaining a separate later Project for adaptation to the
  lasting Maiming
- Rest and Remedy stabilization never supplying Healer-Days or shortening the
  Recovery Project

### Stopover and Home recovery

- An exposed Stopover able to add Exposure through its resolved circumstances
- Ordinary natural shelter able to prevent further Exposure without providing
  a guaranteed reduction
- A completed Rest MEET stabilizing the party's current Wounds through its next
  three TRAVEL Bands and the situations resolved within them
- A Wound that remains present becoming unstabilized again when ordinary rest
  next becomes due
- A completed Rest at a usable Outpost removing one internal Exposure step
- Repeated Outpost Rest able to continue that ebb as world time passes, but
  never removing the final step while the Citizen remains Away
- Each DAWN removing up to three Exposure steps from every Citizen who remains
  present at Home, to a minimum of 0
- A Citizen at maximum Exposure therefore returning to baseline over two Home
  Dawns: 6 to 3, then 3 to 0
- Relaunch before recovery completes preserving the Citizen's remaining
  Exposure
- Outpost and Home Exposure recovery neither clearing nor substituting for the
  distinct recovery of wounds, Maiming, or Tharn
- EMBODY able to portray Home recovery without accelerating it

## 5.7 Outposts and Stopovers

Away range grows through places where a party can stop safely enough to rest.
An Outpost makes one such stop reliable while remaining part of Away.

### Refuge, Stopover, and Outpost

- A **natural refuge** being an existing physical shelter that may improve the
  circumstances of Rest without becoming Colony property or infrastructure
- A **Stopover** being the temporary Away state created when a party completes
  a Rest MEET at its current location
- An **Outpost** being a persistent constructed Away refuge at one eligible
  known location
- A natural refuge able to support a Stopover without becoming an Outpost
- An Outpost improving the Stopover made there rather than creating another
  Mode, Register, settlement, or expedition endpoint
- Departure ending the Stopover while the location, natural refuge, and any
  Outpost remain persistent world facts
- Known shelter extending practical range by making Rest more reliable rather
  than imposing or removing an arbitrary travel boundary

### Establishing an Outpost

The Colony establishes an Outpost through the ordinary Project Queue. The
Project abstracts routine construction travel and labor so that civic
commitment remains legible at Home. Its completed result appears at the known
remote target.

- The target needing to be an eligible location the Colony has already found
  and can identify
- A completed usable Workshop supplying the Project capacity
- Builder owning the Project and the entry stating its required material and
  Builder Civic Share-Days
- The player committing named Builder Citizens through the Colony Project
  Queue under the ordinary rules
- Those Builders withdrawing their Civic Shares from ordinary Builder
  coverage and remaining unavailable to Launch until completion
- The Outpost location remaining the remote Project target without requiring
  the player to form a construction party, assign Home Roles inside Away, or
  resolve routine building travel through TRAVEL, RISK, or MEET
- The abstraction creating no Exposure or personal consequence for the
  committed Builders
- Completion at DAWN establishing the persistent Outpost and releasing its
  Workshop and Builders

### Persistence, damage, and restoration

- An Outpost requiring no routine upkeep payment, maintenance assignment, or
  degradation meter
- An Outpost becoming damaged only through an explicit visible event rather
  than silently decaying while outside player attention
- A damaged Outpost remaining a persistent known physical location but losing
  its protected Rest, Exposure reduction, and Cargo-transfer functions
- Whatever shelter the damaged structure still physically affords able to
  support an ordinary natural-refuge Stopover
- Restoration using another remote Builder Project through a completed usable
  Workshop, under the same abstraction as initial construction
- Complete destruction occurring only through an appropriately severe
  on-screen MEET and never through unattended attrition
- Outposts having no functional upgrades, specializations, or tiers in v0.5

### Rest at an Outpost

- Reaching an Outpost not ending the expedition or causing Homecoming
- Rest still resolving through a Rest MEET rather than applying merely because
  the party passes the location
- A completed Outpost Rest resetting the party's travel cadence and ending
  Tharn under the ordinary Rest rules
- A completed Outpost Rest stabilizing Wound through the next three TRAVEL
  Bands and removing one Exposure step from each resting Citizen
- The Outpost protecting the Rest from ordinary consequences of sleeping in
  exposed ground while remaining subject to any particular active threat or
  damage that actually compromises it
- Repeated Outpost Rest able to ebb Exposure as world time passes, but never
  removing a Citizen's final Exposure step while they remain Away
- Rest at an Outpost neither clearing Wound, progressing a Wound Recovery
  Project, removing Maiming, nor providing the complete recovery of Home
- The player able to offload any amount of Cargo from the party's Carry during
  the Stopover
- Offloaded Cargo leaving Carry immediately and entering the single Colony
  Stock through abstract routine transport
- Colony sync completing the transfer immediately and freeing party Carry for
  continued exploration
- The player able to inspect the present party and then continue through TRAVEL
  or begin the return journey

### Outpost boundaries

- An Outpost functioning as uninhabited Away infrastructure for temporary
  visiting parties
- Colony sync transferring offloaded Cargo directly into the single Colony
  Stock
- Tools, Supplies, Keepsakes, Artifacts, and other individually tracked Items
  remaining with their holders rather than entering Cargo transfer
- Stopover, Rest, Cargo transfer, continued TRAVEL, and the return journey
  forming its available scope
- Care at the Outpost remaining limited to the defined Rest effects
- A calm Outpost remaining part of Away regardless of any quieter or more
  settled presentation used during its Rest MEET

## 5.8 Return and Homecoming

Return carries the party back through the same continuous world. Homecoming
then receives the changed expedition into the Colony.

### Turning Homeward

- The player able to turn toward Home whenever the party can ordinarily travel
- Turning back occurring through the next homeward TRAVEL choice rather than a
  separate **Return** command, failure state, or destination-menu extraction
- Ordinary Day Bands, terrain, weather, Carry, Wound, Exposure, Rest, Nodes,
  and MEET continuing to govern the journey
- The player continuing to choose what the party carries, protects, abandons,
  or offloads at an Outpost
- The party able to change direction or stop again without forfeiting what it
  has already discovered or accomplished
- Each Roadway encountered on the homeward journey following the Return
  Crossing procedure in Chapter 5.3
- Every Return Crossing resolving on the homeward side of the Roadway with the
  whole party clear of traffic

### Physical arrival

- Clearing the Roadway returning the party to the Home Median but not
  teleporting it directly into the Colony
- The party completing the remaining physical approach through ordinary
  TRAVEL
- Homecoming beginning when the returning party reaches the Colony itself
- Citizens, companions, Cargo, Items, relationships, and bodily consequences
  remaining the same persistent facts throughout the approach

### The Homecoming MEET

**Homecoming** is the state-transition MEET that ends every expedition and
converts its personal Away facts into shared Home facts. It is reconciliation,
expressing how the Colony receives what has returned.

- Homecoming occurring after every expedition, including an uneventful return
- Completing Homecoming advancing the shared world clock by one Day Band to
  represent reception, unloading, immediate care, and civic reintegration
- A routine Homecoming remaining brief and warm, with no artificial choice,
  score, grade, or redundant dismissal required even though world time advances
- A consequential Homecoming expanding only when care, a new arrival, a
  damaged or singular Item, a relationship, loss, or another unresolved matter
  actually requires player attention
- Additional time arising only from a consequential allocation or follow-up
  situation that independently requires it, never from the amount of accounting
  shown
- The MEET following the shortened state-transition sequence of **Frame →
  Recognize and receive → Reconcile → Continue**, with Care or Allocation
  opening from Reconciliation when applicable
- Recognition preceding accounting: the Colony first receives the named lives
  that returned before reducing the expedition to totals
- The returning party, its material result, and its most important personal or
  relational consequence being grouped into a small number of intelligible
  concerns
- Homecoming using its own contextual allocations rather than the five fixed
  response families of contested Away MEET

### Homecoming flow

Homecoming moves through **recognition and reception → reconciliation**.
Assessment gathers the returning facts. Care and allocation follow wherever
those facts require a decision, and civic reintegration completes the same
transaction.

#### Recognition and reception

- Showing who returned, who did not, and what has visibly changed about the
  party before presenting totals
- Showing the Colony that receives them as it now exists, including any
  material development or waiting situation that arose during their absence
- Letting the returning party and changed Home become visible to one another
  before either is reduced to an interface summary
- The Colony physically receiving particular friends rather than absorbing an
  anonymous unit into inventory
- Relationship, family, Guest, and civic responses appearing when the actual
  return makes them relevant
- Relief, alarm, grief, welcome, or uncertainty arising from what returned
  rather than being imposed as one mandatory celebratory tone
- Arrival remaining a shared Colony moment even when no player decision is
  required

#### Reconciliation

Assessment and reintegration form one operation. Most returned facts reconcile
automatically. Facts with materially different persistent outcomes open the
applicable Care or Allocation choice from within that same operation.

- Accounting for remaining Cargo, spent or unspent Supplies, damaged or lost
  Tools, Keepsakes, Artifacts, discoveries, relationships, Wound, Maiming,
  Exposure, death, and other resolved consequences
- Showing cause and bearer for personal or meaningful facts rather than listing
  them as detached gains and losses
- Preserving every fact already resolved Away; Homecoming reports consequence
  but never rerolls, grades, or retroactively improves it
- Every returning Citizen changing from Away-present to Home-present when
  Homecoming completes
- Each available Citizen then resuming the Civic Share of their standing Role,
  with partial-day accumulation continuing under Chapter 5.1
- A Wound or other actual bodily restriction determining availability without
  changing Citizen standing or Role identity
- Civic Balance, Practice support, passive throughput, Project availability,
  and current Home circumstances recalculating from the Citizens and material
  now present
- Campaign Memory receiving only the facts selected by its own backend rules,
  without asking the player to curate the hidden Record during Homecoming

**Care arising from assessment**

- A returning Wounded Citizen creating the defined Healer Load
- Homecoming showing whether an eligible Hearth and Healer are available for a
  Wound Recovery Project
- The player able to commit that Project through the ordinary Colony Queue or
  defer it without preventing Homecoming from completing
- An unavailable Hearth, absent Healer, or deferred Project leaving Wound
  present and legible rather than causing automatic treatment or anonymous
  worsening
- The acute Wound accompanying Maiming entering ordinary Wound recovery while
  the lasting Maiming remains
- Exposure entering its three-steps-per-DAWN Home recovery without being erased
  merely by crossing the Colony boundary
- A larger unresolved care need opening its own Home MEET after reconciliation
  rather than overloading Homecoming with a second subject

**Allocation arising from assessment**

- Remaining Cargo entering the single Colony Stock and clearing from party
  Carry
- Unspent Supplies returning to the prepared Colony pool while their expedition
  positions clear
- Tools, Keepsakes, Artifacts, and other tracked Items retaining their holders,
  owners, states, and histories
- A damaged Tool entering ordinary Crafter repair after Homecoming rather than
  being restored invisibly during the return
- A returning non-Citizen being received through the applicable Guest,
  hospitality, or relationship decision rather than entering the Roster
  automatically
- A deceased Citizen's returning Keepsake or another meaning-bearing Item
  receiving its necessary relationship, succession, or memorial disposition
  through Homecoming rather than becoming loot or anonymous Colony inventory
- Only allocations with materially different persistent results becoming
  player choices; routine stock and Supply reconciliation remaining automatic

- Completion ending the expedition and restoring DWELL as the ordinary form of
  player attention
- Homecoming guaranteeing neither Quiet Equilibrium nor immediate access to
  EMBODY
- EMBODY reopening only when the Colony actually satisfies Quiet Equilibrium
- A difficult return able to leave Home under Pressure without converting the
  expedition into failure

## 5.9 Landscape Voice: The Playable Page

Landscape Voice is an immediate presentation ambition: playing MEDIAN should
sometimes feel like reading a page in a book whose events the player is causing.
It accompanies and interprets present play as it occurs.

Landscape Voice is MEDIAN's human third-person narrator. Its intended literary
feel draws from the landscape-attentive narrators of Richard Adams and J. R. R.
Tolkien: a voice able to describe country, weather, movement, and simple events
with clarity and weight. Adams and Tolkien establish critical lineage for an
original MEDIAN voice. Landscape Voice stands outside the animal community; it
is distinct from animal speech and from the animal cultural voice that may
shape Chronicle, Tale, or scene presentation.

### The playable page

- Visual composition and prose working together like an illustrated page
- The player continuing to act, read the world, and cause events rather than
  watching a literary cutscene
- The narrator able to describe named Citizens as actors without making any
  Citizen the story's protagonist or point of view
- No first-person Citizen narration, selected viewpoint character, rotating
  party narrator, or access to private interior thought
- Landscape remaining present during action because terrain determines
  perception, movement, safety, and choice
- Narration able to widen into observation or contract around danger
- Sentence length, rhythm, and perceptual breadth reflecting the actual tempo
  of play
- Landscape Voice using established history for continuity when relevant
  without belonging to Campaign Memory or requiring a Record transaction

### What the Voice attends to

- Locating the party plainly within Day Band, light, weather, direction, and
  the ground immediately around it
- Following collective movement through successive terrain: leaving one kind
  of cover, entering another, climbing, descending, spreading out, catching
  up, keeping together, or following a physical feature
- Allowing an uneventful stretch of TRAVEL to pass in a few concrete sentences
  without pretending that nothing existed between mechanical destinations
- Moving attention naturally between the animals, their near ground, middle
  distance, horizon, and sky
- Naming vegetation, water, soil, weather, infrastructure, and distance when
  those facts make the place more exact
- Letting small external events—a change of wind, diminishing light, moving
  water, a distant animal call, or the return of silence—complete a passage
- Giving ordinary actions weight through their location and timing rather than
  manufacturing plot, suspense, or psychological revelation
- Using natural description during quiet travel as readily as during danger or
  discovery
- Favoring concrete sequence and restrained observation over ornamental lore,
  constant metaphor, or summary of what the player should feel

### One narrator, several bodies

- Mouse bodies making seams, edges, cavities, enclosure, and fine passages
  materially relevant to the events the narrator describes
- Rabbit bodies making cover, exposed distance, shared ground, and warning
  materially relevant
- Squirrel bodies making anchors, height, gaps, momentum, and continuity of
  passage materially relevant
- Guest bodies likewise changing which physical details matter when their
  actual capabilities or vulnerabilities enter the event
- Mixed parties remaining together in one narrated landscape rather than
  dividing the passage into competing viewpoints
- The same human narrator describing these bodily relationships without
  adopting an animal's cultural voice or creating separate realities,
  cognitive limits, or rigid species prose templates

### Truth and interpretation

- Landscape Voice remaining authoritative about situated perception and
  restrained about interpretation
- Current terrain, weather, light, sound, visibility, party composition,
  bodily condition, established relationships, and resolved consequences able
  to inform a passage
- No hidden knowledge, undiscovered hazard, unresolved outcome, unsupported
  emotion, or moral conclusion entering through narration
- No essential mechanical instruction being conveyed only through prose
- The voice changing tempo and attention without changing truth

### Earned use

- Candidate moments including entry into a new or changed landscape, first
  sight of a significant destination, emergence from constricted terrain, an
  overlook, the far Margin after a consequential Crossing, the resolved
  aftermath of a spatially important MEET, return through familiar ground, and
  Homecoming after meaningful absence
- Landscape Voice remaining scarce enough for its appearance to retain weight
- Prose entering unobtrusively and yielding naturally to ordinary input rather
  than imposing a cutscene or fixed wait
- The game remaining mechanically complete when a passage is absent, with the
  passage succeeding when it deepens the player's apprehension of place,
  action, and participating lives
- No sixth Register, reward, progression system, memory category, narrative
  currency, or parallel authority

### Landscape as syntax

**Terrain → perception → available choices → movement → consequence**

- Physical landscape producing action and meaning rather than serving as
  interchangeable decoration
- Human infrastructure becoming geography, ecology, refuge, boundary, danger,
  and territory at animal scale

# PART VI — THE CAMPAIGN

## 6.1 Campaign Memory

**Campaign Memory** is the campaign-wide system through which the game retains
what happened and presents what the Colony remembers. It combines one hidden
factual Record with written and visual expressions made for the player.

```text
Record — hidden factual history
├── Chronicle — selected Colony history
├── Citizen Tales — history applying to particular Citizens
├── Item Tales — history applying to particular Items
└── canon images — the evolving visual record of Citizens and the Colony
```

- One resolved event able to matter at Colony, Citizen, Item, Place, and
  relationship scales without being copied into separate competing histories
- Home and Away contributing to the same Campaign Memory
- Chronicle, Tales, and canon images selecting and translating established
  facts without changing what happened
- Memory supporting later dialogue, relationships, memorials, Frills, MEET,
  and EMBODY
- Campaign Memory naming the complete historical architecture rather than one
  additional event ledger or player-maintained scrapbook

### The Record

The **Record** is the incremental back-end database that grows throughout the
Colony's life. It is the authoritative factual history of what occurred. The
Chronicle, Tales, canon images, and intentional inspection tools translate its
facts for player-facing use.

- Each resolved state-changing or authored historical event adding one
  structured entry rather than rewriting earlier history
- An entry identifying the relevant time, Place, participants, objects,
  relationships, decision, outcome, and persistent consequences
- Home, Away, Return, birth, arrival, Maturity, relationship change, Project
  completion, recognition, injury, loss, and death all able to write to the
  same Record
- The Record retaining machine-readable facts rather than composing narrative
  prose
- Routine animation, repeated ambience, interface use, and mechanically empty
  repetition not generating historical entries
- The player encountering the Record itself only in debug mode or through an
  intentionally provided inspector, never as the ordinary history interface
- An inspector exposing the underlying facts without displacing the Chronicle,
  Tales, canon images, or Almanac in normal play
- Recorded facts never being contradicted or silently replaced by a later
  written or visual rendering

### Back-end selection and presentation

- The back end deciding which Record entries qualify for the Chronicle and each
  Tale, consolidating related entries, sorting them, and presenting the result
  to the player
- Significance, subject, relationship, and chronology guiding that selection
  without requiring the player to tag, approve, rank, or file events
- The player able to browse the history presented to them without becoming its
  editor or archivist
- Omitted routine detail remaining in the Record when historically relevant
  rather than being converted into player-facing clutter
- Every translation remaining traceable to established facts even when several
  entries are expressed as one passage or image

### The Chronicle

The **Chronicle** is the Colony's in-story translation of selected Record
entries.

- Chronicle selection favoring events with shared civic, historical, or
  cultural meaning
- Several related Record entries able to become one concise Chronicle passage
- The Chronicle able to name patterns, consequences, and remembered meaning
  that a raw database entry cannot express
- Selection and translation able to omit routine detail without inventing an
  event, participant, relationship, or outcome
- A later Chronicle passage able to add perspective to earlier history without
  changing its recorded facts
- Chronicle material remaining readable as the Colony grows
- The host Core Species' habits of attention able to shape which concrete
  relationships the Chronicle emphasizes and how the Colony expresses its
  shared history

### Tales and Prior-life Tales

A **Tale** is a subject-specific translation of selected Record entries. Every
Citizen and those Items whose histories matter possess one.

- A Citizen's Tale presenting events that apply to that Citizen's life,
  including origin, family, relationships, Role history, meaningful Home and
  Away events, injury, recognition, possessions, aging, death, and legacy
- A Tool's Tale presenting consequential creation, recovery, holders, uses,
  adaptations, Damage, repair, loss, or destruction while omitting routine use
  and reassignment
- A Keepsake's Tale preserving origin, personal meaning, gifting, succession,
  loss, and the relationships carried through it
- A Special Artifact able to carry a Tale proportionate to its singular civic
  history
- Supplies receiving no Tale because they remain anonymous consumable units
- Tales translating remembered facts rather than granting progression or
  inventing unrecorded life events
- A closed Tale remaining accessible after death, destruction, departure, or
  another definitive ending
- A Tale's language able to reflect the subject's Species, body, community,
  and learned vocabulary while preserving the same recorded facts

A **Prior-life Tale** establishes the life a Founder or arriving Citizen had
before the Colony knew them. When that history becomes known, its established
facts enter the Record as prior history distinguished from events witnessed
during the campaign. Material relevant to hospitality, safety, relationship,
or present capability is not concealed merely to manufacture surprise; further
detail may emerge through relationship, return, MEET, EMBODY, or contact with
the Citizen's past.

### Evolving canon images

Campaign Memory has a visual complement: evolving canon images of individual
Citizens and a small, purpose-built canon representation set for the Colony.
These images let the player see particular lives and a settlement changing
alongside their written continuity.

- Every Citizen having exactly one current canon image in ordinary play,
  amended when an established, materially visible fact about that Citizen
  changes
- Earlier Citizen images remaining accessible through secondary history views
  without competing with the current image in the Citizen panel
- The Colony having a small current set of complementary canon views where one
  image cannot establish its spatial form, material construction, and inhabited
  life clearly enough
- The Colony retaining selected superseded views as an intentional visual
  archive of growth, season, damage, repair, and other visible history
- The back end deciding when a change warrants a new visual presentation and
  which established details it must express
- Every model-assisted image using the relevant existing canon Citizen, Colony,
  location, and object imagery as mandatory visual source material
- The Record and current state governing factual truth, the canon imagery
  governing visual identity and continuity, and the immediate situation
  governing only the change in composition
- Canon imagery anchoring dramatic scenes after a resolved MEET, Register
  transitions and loading images, Citizen information panels, Chronicle and
  Tale illustrations, Homecoming, and Colony milestones
- A composed scene changing framing, pose, light, and immediate context while
  preserving its subjects and established state; it does not replace a canon
  image unless a separate lasting change warrants and validates that amendment
- Whole-Colony moments using a composed civic view rather than an arbitrary
  fixed lineup of Citizen portraits
- Visual presentation complementing written memory while the Record remains
  factual authority

Appendix C defines how canon images are established, amended, reused, and
validated without allowing a generative model to author new facts.

### The Almanac

The **Almanac** stands outside Campaign Memory. It presents present state and
the known, scheduled, forecast, or possible future states and events that bear
upon current decisions.

- Current Citizens, locations, availability, Roles, relationships, Places,
  Practices, resources, Projects, civic balances, Pressure, season, weather,
  traffic, and known world circumstances
- Scheduled commitments, expected completions, seasonal windows, Telegraphs,
  and other legible future events
- Uncertain information remaining visibly uncertain rather than becoming
  prediction or omniscience
- A future event leaving the Almanac's prospective view when it resolves,
  updating present state and adding its factual outcome to the Record
- The Almanac remaining continuously available as an interface lens, with the
  Community Board providing optional diegetic expression in DWELL
- No historical narration, retrospective interpretation, or exhaustive
  simulation diary

### Given Names

- Every Citizen entering play with an appropriate Given Name
- Cultural naming conventions
- Collective household names for the two defined exceptions
- No serial worker labels or rarity presentation
- A naming, renaming, or collective-household continuity event entering the
  Record and appearing wherever the current name is shown

### Distinctions and After-names

- Distinction as narrow favorable recognition grounded in meaningful conduct
- After-name as rarer public recognition of durable life history
- Both able to arise from Home or Away
- Neither automatic nor selected from a reward list
- No generic rank, experience level, or required numerical effect
- Recognition entering the Record, appearing in the Citizen's Tale, and
  entering the Chronicle only when it carries Colony-scale meaning

### Memorial continuity

- Death, departure, destruction, and irreversible loss changing present state
  without deleting the relevant Record entries
- Chronicle preserving selected shared history while Tales preserve the shape
  of particular lives and objects
- Places, relationships, Keepsakes, memorials, and later events able to refer to
  the same underlying Record
- Empty Places and absent routines remaining available as visible historical
  consequences
- Memorial continuity preserving particularity rather than converting loss into
  a generic morale modifier

## 6.2 The opening campaign

The opening campaign mechanically enacts the Founding Escape narrated in Part
0. It briefly lets the player inhabit the kind of Home they will spend the
campaign learning to build, then joins MEDIAN's ordinary forms of play into a
directed **cut sequence**. This chapter governs player control, system
integrity, persistent state, and transition throughout that sequence.

### Mechanical sequence

1. **Reach 4 flash-forward — directed presentation.** Show the exhausted
   founding party running toward the final smaller Reach-border road. Player
   control begins after the sequence returns to the ancestral Colony.
2. **Ancestral Colony — guided DWELL.** Let the player look around the grand,
   inhabited Colony and apprehend a mature expression of the selected Core
   Species. Persistent management actions remain reserved for the new Colony.
3. **A lesson — short EMBODY.** Open Presence through a future Founder observing
   a Teacher conduct a lesson for young Citizens at the Gathering Place.
4. **Chaos — state-transition MEET.** Render the Colony's destruction through
   animal-scale vibration, sound, dust, obscured sight, and failing ground. Bring
   the Founders into focus and commit the party to flight.
5. **First flight — guided TRAVEL.** Direct the party upcorridor while retaining
   playable bodily movement through the Field. The fleeing party consists of
   three Rabbits or Squirrels, or four Mice in the Mouse opening.
6. **First Reach border — playable RISK.** Use a lightly trafficked smaller road
   to teach the selected species' ordinary Crossing grammar and carry the party
   into Reach 2.
7. **Long escape — authored montage.** Compress continued TRAVEL and the
   Crossings into Reaches 3 and 4, give brief apprehensions of both landscapes,
   and catch up with the Reach 4 opening image.
8. **Final border — montage Crossing.** Carry the party across the fourth
   Reach-border road into Reach 5 and establish maximum Exposure for every
   Founder.
9. **Promising ground — Landscape Voice.** After movement subsides, attend to
   the changed air, quiet, ground, vegetation, and bodily relief, arriving at
   the recognition that it feels good here.
10. **Founding — state-transition MEET.** Let the player inspect the ground and
    commit **Make Home**, select the first Leader, and name the permanent Colony.
    Then open its territory in ordinary DWELL before the first construction
    commitment.

### Guided use of the Registers

- Each playable form retaining its ordinary visual and mechanical identity
- The authored sequence constraining available subject, direction, and
  commitment while leaving the player's actual looking, movement, selection,
  and Crossing input intact
- The ancestral DWELL presenting a mature Species expression and inhabited
  civic life while reserving construction, reassignment, and other persistent
  management for the Colony the player will found
- EMBODY beginning from Quiet Equilibrium in the old Home and establishing the
  intimacy of ordinary life before its interruption
- The Chaos MEET using the state-transition threshold and presenting flight
  as the one physically truthful continuation
- Guided TRAVEL teaching bodily movement through real terrain before RISK takes
  focus
- The first Crossing using the ordinary species grammar and a consequence
  range suited to its low-traffic road; fatality, Maiming, and Tharn remain
  outside that authored range
- Later montage Crossings remaining true events in the party's journey while
  compressing repeated planning and the passage of great distance
- Actual hazardous circumstances across destruction, flight, and four
  Crossings bringing every Founder to Exposure 6 by arrival
- Exposure remaining hidden and causing no automatic Wound or Tharn

### Flash-forward and return

- The opening image remaining brief, wordless, and initially noninteractive
- The exhausted founding party, Reach 4 ground, and approaching smaller road
  supplying its complete visible content
- The cut back to the ancestral Colony establishing the player's first agency
  in calm DWELL
- The long-escape montage eventually returning to the same composition and
  carrying it forward through the final Crossing
- Recognition arising from the repeated image rather than from an explanatory
  chronology label

### Founding the permanent Home

- Reach 5 providing unfamiliar ground capable of sustaining the selected Core
  Species
- Reach 5 realizing one of that Core Species' two founding-biome relationships
  from Chapter 2.3 while remaining part of the shared Corridor
- Landscape Voice entering after the final Crossing, when the world becomes
  spacious and perceptible again
- The passage ending on the simple recognition that it feels good here
- The founding MEET allowing inspection before commitment and treating **Make
  Home** as an explicit state transition
- The Founder who received Focus during the decisive Round of the Chaos MEET
  appearing as the default first Leader
- The player able to select another Founder, with Focus supplying continuity
  rather than rank, aptitude, or a permanent claim to leadership
- One Founder required to take Leader responsibility before the Colony is
  named
- Colony naming remaining the player's one direct naming decision, expressed
  through the Leader on behalf of the founding party
- The ancestral Colony's established name remaining visible during the naming
  decision
- The player assembling the name from curated word, sound, and form lists
  through approved name patterns, with every available construction remaining
  inside MEDIAN's cultural and tonal palette
- Ground, hope, and memory influencing suggestions and component groupings as
  overlapping meanings a name may embrace
- The complete assembled name being visible before confirmation, with the
  player free to exchange components or consider another valid construction
- Confirmation establishing and naming the one permanent Colony
- The confirmed name remaining permanent and entering Campaign Memory as part
  of Founding
- The new territory opening immediately in ordinary DWELL before its first
  construction commitment

### Early Colony development

The permanent Home begins with an exhausted founding party, undeveloped ground,
and a short reserve that makes the first decisions possible. Rabbit and
Squirrel campaigns begin with three Founders. The Mouse campaign begins with
four and uses an authored early arrival to reach the same three-Body-Unit civic
scale before ordinary construction begins. The opening sequence teaches
recovery, Place designation, Projects, Housing Pressure, Sustenance, and DAWN
through the ordinary systems established in Part III.

#### Starting state and recovery

- Every Founder entering Home at Exposure 6
- One Founder beginning as Leader, with the other two Rabbit or Squirrel
  Founders or three Mouse Founders remaining available for their first ordinary
  Role commitments
- Home recovery reducing each Founder's Exposure from 6 to 3 at the first DAWN
  and from 3 to 0 at the second
- The territory beginning with no completed Residence or Practice
- The player able to designate prospective Places through Builder at no cost
- A fixed founding reserve containing enough Sustenance for the initial
  three-Body-Unit recovery interval and enough material for the first Workshop
  followed by one initial Residence or Garden Project
- The reserve permitting Residence or Garden to come first while leaving the
  postponed need materially consequential

#### The Mouse arrival

- Four named Mouse Citizens escaping the ancestral Colony and founding the new
  Home together
- An authored Home MEET occurring immediately after **Make Home** and before the
  ordinary construction tutorial
- That MEET introducing two named Mouse Wanderers traveling together and
  receiving them into the new Colony as part of the Mouse opening
- The Wanderers becoming complete individual Citizens with their own names,
  bodies, relationships, and Tales rather than functioning as a population
  grant
- The resulting six Mice constituting three Body Units, bringing the Mouse
  Colony to aggregate civic parity with the three Rabbit or Squirrel Founders
  before the ordinary construction tutorial and open-ended play begin
- The arrival remaining a specific authored opening event rather than making
  later Wanderer acceptance automatic

#### First Workshop and first development choice

- DWELL introducing Civic Balance through the separate Housing Balance and
  highlighting the shortfall created by three Body Units and no Residence
- Housing Pressure remaining a persistent condition for the player to answer
  rather than becoming a compulsory tutorial objective
- The Rabbit or Squirrel tutorial guiding one available Citizen into Builder;
  the Mouse tutorial suggesting two available Mice so their half shares provide
  one aggregate Civic Share while leaving a single Mouse assignment legal
- Establishing the first Workshop as a guided Builder Project under its sole
  bootstrap exemption
- A selected Builder designating a Place for the Workshop at no cost and
  establishing the Practice through the Project
- The Project committing the selected Builder Citizen or Citizens, consuming
  its stated material, and advancing through Civic Share-Days
- Two committed Mouse Builders producing the same one-Civic-Share-per-day
  progress as one Rabbit or Squirrel Builder; one committed Mouse Builder
  remaining valid while taking twice as many days to meet the same requirement
- The interface using this difference to teach share aggregation without
  pairing Mice or changing the Project requirement by species
- The Project completing at the applicable DAWN
- Workshop completion ending the bootstrap exemption and opening ordinary
  Project capacity
- The first strategic development choice being whether to establish a
  Residence or a Garden
- Residence addressing immediate Housing Pressure and Garden enabling passive
  Sustenance production
- DWELL presenting Residence as the direct remedy while allowing the player to
  build the Garden first and knowingly carry Housing Pressure
- The unchosen need remaining present and legible until the Colony answers it
- For every Core Species opening, one Well-Placed first Residence clearing the
  three-Body-Unit Housing Pressure while a Not-Well-Placed first Residence
  leaves one Body Unit uncovered

### The first expeditions

The opening campaign then releases into ordinary Away play. The player chooses
who leaves, how far the party travels, and whether it first searches the Home
Median or crosses outward into a Margin.

#### Opening Nodes and encounters

- The Home Median Reach able to contain Sustenance Nodes and minor Scrap Nodes
  that support the Colony's first expeditions
- The first Node encountered on the Home Median able to be an uncontested
  Sustenance opportunity
- The first Node encountered in a Margin being Contested and using the fixed
  contested Away MEET display
- Subsequent Nodes following the ordinary ecological, situational, and
  opposition rules of Chapter 5.4
- At least one Guest species appearing within the first four post-founding
  MEETs, introducing the wider animal community through the present situation
- That first appearance able to begin recognition or relationship while
  carrying no requirement of immediate Guest adoption

#### First Launch and Homecoming

- The first Launch MEET presenting the currently available Citizens and guiding
  the player to form a legal party of one and one-half to three Body Units
- Carry, standing Tools, Keepsakes, broad-purpose Supplies, and the known
  departure conditions remaining visible without disclosing an unseen Node or
  prescribing an expected solution
- The subtraction preview showing the Civic Shares, Role support, passive
  throughput, and Beautification the proposed party would remove from Home
- Confirmation committing the selected Citizens, fixing the party and its
  Supplies, and beginning ordinary TRAVEL through the Home Median
- The player choosing whether to explore the Home Median first or travel toward
  a Margin and its first Crossing
- The opening Node and Guest-species exceptions above operating within that
  chosen journey rather than forcing one route through the tutorial
- The player choosing when to turn homeward and completing the physical return
  through the same continuous Field
- The first full Homecoming MEET recognizing the named Citizens who returned,
  reconciling Cargo, Supplies, Items, discoveries, relationships, arrivals, and
  bodily consequences, and advancing the shared clock by its ordinary one Day
  Band
- Completion returning available Citizens and their Civic Shares to Home,
  entering the expedition's established facts into Campaign Memory, and
  releasing the campaign into open-ended play

## 6.3 Civic progression

Colony Tiers recognize the scale a stable Colony has reached and give it a
shared historical name. Population establishes eligibility. The player chooses
whether to commit the material that triggers recognition through Home.

### The four Colony Tiers

Tier number is the shared mechanical vocabulary. Each Core Species gives the
same Tier its own architectural and civic name.

| Tier | Mouse | Rabbit | Squirrel |
|---|---|---|---|
| **I** | **First Rooms** | **Close Commons** | **First Anchors** |
| **II** | **Joined House** | **Open Commons** | **Linked Ways** |
| **III** | **Manor House** | **Court** | **Living Web** |
| **IV** | **Grand Manor** | **Grand Court** | **Grand Web** |

- Tier I becoming true through Founding and the first Leader's naming of the
  Colony
- Tier II recognizing a Colony able to prepare rather than live wholly from one
  immediate need to the next
- Tier III recognizing a mature Colony able to endure, choose, and remain a
  stable campaign home
- Tier IV recognizing the optional ambition of the Colony's grand
  species-specific civic form
- Tier III providing a complete and durable plateau for campaigns that do not
  pursue Tier IV
- A recognized Tier remaining part of Colony history through later loss,
  contraction, or damage

### Population gate

Population is the sole Tier gate. Reaching the next threshold makes that Tier
eligible for recognition.

| Next recognition | Required living Body Units |
|---|---:|
| **Tier II** | **7** |
| **Tier III** | **12** |
| **Tier IV** | **18** |

- The threshold applying equally to Mouse, Rabbit, and Squirrel Colonies
- Every living named Citizen on the Colony Roster contributing their ordinary
  Body Unit, including young Citizens, Guests, Patients, and Citizens who are
  presently Away
- Rabbit, Squirrel, and ordinary v0.5 Guest Citizens therefore contributing one
  Body Unit each and Mouse Citizens one-half
- The threshold remaining a measure of lives belonging to the Colony rather
  than of their current location, Civic Shares, Residence Capacity, or
  availability

### Civic Dedication

Recognition requires a **Civic Dedication**: a large, escalating commitment of
Colony resources incorporated permanently throughout Home. The Dedication gives
material and symbolic weight to advancement and serves as its deliberate
player-controlled trigger.

- Tier I Founding requiring no additional Civic Dedication
- Each later Tier requiring a substantially greater Civic Dedication than the
  last
- The exact ingredients and quantities being established through the dedicated
  Items and Resources tuning phase rather than inferred from Outpost cost alone
- Mechanical cost remaining equal across Core Species while its physical
  expression follows the Colony's species and new Tier name
- Mouse Dedication becoming joinery, partitions, furnishings, reinforcement,
  and accumulated detail throughout the House
- Rabbit Dedication shaping, protecting, and dignifying the Commons or Court
- Squirrel Dedication strengthening anchors, crossings, bindings, and the
  visible Web
- Dedicated material becoming part of the Colony's built fabric rather than a
  separate Place, Practice, inventory object, or source of numerical Capacity
- Civic Dedication occupying no Project Queue slot
- Civic Dedication respecting protected Colony reserves so recognition cannot
  consume resources reserved for ordinary life
- The exact interaction between Dedication recipes and protected reserves being
  established through the dedicated Items and Resources tuning phase

### Recognition MEET

- Reaching the next Population threshold making its Tier eligible
- Quiet Equilibrium being active when recognition begins, confirming that
  ordinary obligations are covered and no acute situation demands attention
- Recognition requiring a Home-present, available Citizen actively sustaining
  Leader
- The required Civic Dedication being available outside protected Colony
  reserves
- The player able to leave an eligible Tier unrecognized for any length of time
- Committing the Civic Dedication consuming its resources, using the present Day
  Band, and triggering the Home Recognition MEET
- The player choosing Focus when several active Leaders are available
- The active Leader calling and conducting a Home Recognition MEET
- Gathering Place hosting the recognition when available without becoming an
  additional advancement requirement
- The MEET presenting the Colony's scale, species-specific Tier name, active
  Leader, Civic Dedication, and ceremonial recognition
- Resolution recording the Tier in Campaign Memory and making the Colony's new
  civic and architectural identity visible in DWELL
- Recognition proceeding one Tier at a time even when later Population
  thresholds have already been met
- Later loss of Quiet Equilibrium, population, or material never revoking a
  recognized Tier

## 6.4 Corridor progression

Corridor progression is the expanding portion of the continuous world that the
Colony has reached, experienced, and made practically accessible. It proceeds
through ordinary TRAVEL, RISK, MEET, relationships, and Outpost construction.
Home remains the permanent center from which that outward history accumulates.

### Reaching farther

- The adjoining Reaches and Margins existing continuously from the beginning
- Parties entering new ground through ordinary TRAVEL and Crossings
- Distance, Exposure, rest cadence, Carry, bodily condition, and the return
  journey determining practical range
- Physical obstruction or a situated inhabitant able to constrain passage
  through the ordinary world and MEET systems
- Every visited location, encountered Node, established relationship, and
  resolved change persisting as world state

### Supported range

Natural refuges and Outposts make longer expeditions credible by giving parties
places to stop.

- A known natural refuge improving the circumstances of a Rest MEET
- A completed Outpost providing protected Rest, limited Exposure relief, Tharn
  recovery, Wound stabilization, and Cargo transfer
- Several Outposts forming a useful chain through their actual geographic
  spacing rather than through a separate network score
- Each Outpost extending practical reach while travel through the intervening
  terrain remains continuous
- Travel between Outposts remaining subject to the ordinary Field, weather,
  Crossing, and MEET systems
- Outpost construction continuing to draw its Builder commitment and Project
  capacity from Home

### A changing known world

Progress appears through differences the player can revisit.

- A formerly Contested Node becoming approachable through a relationship
- A resource site changing through use, season, recovery, or neglect
- Shelter becoming reliable through an Outpost
- A prior MEET changing who is present and what responses are available
- A Guest, neighbor, or settlement recognizing the party through established
  history
- A once-distant place becoming a familiar part of the Colony's ordinary
  expedition range
- The map and Almanac presenting these established facts directly

### Social reach

Relationships expand what the Colony can participate in while keeping access
particular to the animals, places, and circumstances involved.

- Neighboring animals and settlements encountered through situated MEETs
- Trust, obligation, exchange, hospitality, warning, and access remaining
  particular relationship facts
- A relationship able to change a Node's contest, open shelter or exchange,
  reveal a Practice improvement, or create a future situation
- Rest-Stop Metropolis serving as the corridor's greatest social concentration
  and a source of relationships, Guests, Items, and Practice-improvement
  understanding
- Social access resolving through the involved party and situation rather than a
  universal reputation score

### Independent ambition

- A small Colony able to travel ambitiously when it can bear the domestic
  subtraction and Away risk
- A large Colony able to remain close to Home
- Outposts, distant relationships, the Ancestral Home, the Interchange, and
  Metropolis contributing to campaign possibility independently of Colony Tier
- Civic Dedication giving recovered resources a major Home use while leaving
  exploration voluntary
- Corridor development continuing after any Tier plateau
- Individual Outposts and the continuous terrain between them remaining the
  authoritative world state, with an Outpost chain serving as a descriptive
  geographic result rather than another tracked system

## 6.5 Campaign horizons

Campaign horizons are large authored Field territories within the continuous
world. Each contains sublocations, Nodes, and MEETs governed by the ordinary
Away registers and persistent world state. Parties reach them through ordinary
Corridor expeditions at whatever Colony Tier their practical range permits.

Three canonical horizons give the Corridor its broadest civic contrasts:

- The Ancestral Home: society lost
- The Interchange: plurality organized through immediate circumstance
- The Rest-Stop Metropolis: plurality gathered into a lasting city

### The Ancestral Home

The Ancestral Home is the total wreck from which the Founders escaped. It
remains a persistent, revisitable Field territory at the far end of the opening
journey. Returning parties reach it through ordinary Corridor travel and
encounter the same ruined Colony first established in Part 0 and the mechanical
opening.

Its wreckage forms a dense authored zone of specialist Nodes. These Nodes hold
particular remains, hazards, traces, and opportunities that call upon the
party's relevant Roles, Tools, Supplies, Signatures, relationships, and MEET
choices. Their primary campaign value is recovery, recognition, and reckoning:
learning what became of the old Colony and deciding how its surviving history
enters the life of the new one.

A low-frequency encounter may reveal a lone escapee still hiding within the
wreckage. Once encountered, that animal and the consequences of the meeting
become persistent world state.

When a returning party includes a Citizen who escaped from the Ancestral Home,
the territory can offer a Remembrance MEET. Founding Citizens and authored
Wanderer escapees qualify equally. The involved Citizen's lived connection
opens choices through which the player may recognize a place, loss,
relationship, possession, or memory and allow the result to enter Campaign
Memory.

The new Colony remains Home. The Ancestral Home is an optional horizon of
return, and campaign play continues after its exploration.

### The Interchange

The Interchange is an emergent crossroads and an anarchistic analogue to
Metropolis. Ramps, barriers, underpasses, pillars, drains, embankments, and
adjoining Roadways funnel many kinds of animal through one human-made knot.
Shelter, vegetation, runoff, discarded materials, and the danger of traffic
concentrate opportunity without giving the territory to any single community.

Its order is particular and present-tense:

- Travelers, regulars, scavengers, temporary camps, territorial animals, and
  predators meeting in unusual variety
- Several species able to participate in one situation when their immediate
  interests intersect
- Claims, exchanges, warnings, favors, grudges, shelters, and agreements
  belonging to the animals and locations involved
- Familiar relationships changing later MEETs without creating universal
  safety or reputation
- Guest introductions occurring frequently while citizenship remains only one
  possible consequence
- CONTEST, EVADE, PARLEY, YIELD, and WITHDRAW each finding regular use
- Tools, Supplies, Signatures, relationships, and carried Items changing the
  choices available within otherwise ordinary MEETs

The Interchange is a persistent Field territory whose population and situations
can vary across visits. It offers situational exchange, unusual Items and
Resources, information, obligation, and a dense sample of how other animals
live. An Outpost may occupy a suitable site at its edge or within one sheltered
part, extending the Colony's practical range while leaving the wider
Interchange under its many local arrangements.

The Interchange is encountered through ordinary Corridor exploration at
whatever Colony Tier a party can reach it. It stands between Home and
Metropolis as a place where many animals coexist through local accommodation.
Metropolis answers that same plurality with dependable venues, hospitality,
specialized craft, exchange, and Practice-improvement understanding.

### The Rest-Stop Metropolis

The Rest-Stop Metropolis is a large, persistent Field territory experienced in
TRAVEL. Its markets, shelters, workshops, gathering places, and other civic
venues form a dense network of specialist Nodes within a visibly living,
constructed animal city. The visiting expedition remains an Away party as it
moves among them.

- Local movement proceeding through the Metropolis territory and its connected
  venue Nodes
- Arrival, important transactions, hospitality, consequential encounters, and
  departure resolving through MEET
- A Stopover offering substantial rest and Exposure relief while the expedition
  remains Away
- Dependable venues supporting trade, shelter, specialized craft, information,
  Guest encounters, and Practice-improvement understanding
- Established relationships changing how particular residents and venues
  receive the party
- Residents continuing the city's ordinary life and work while the player
  chooses how the visiting party navigates and participates in it

Metropolis can visually echo the activity and construction of DWELL while
retaining TRAVEL's rules and player affordances. Home is a place the player
shapes; Metropolis is a place the player learns to navigate.

### Continuing the campaign

The Ancestral Home, Interchange, Metropolis, and the Corridor beyond them remain
available as continuing sources of exploration, relationship, and change.
MEDIAN v0.5 has no formal victory condition.

# PART VII — PRESENTATION AND DEVELOPMENT BOUNDARY

## 7.1 Interface and information design

MEDIAN's interface follows one persistent world through five distinct
Registers. Each Register changes what the player attends to and how they act
while preserving the same Citizens, Places, objects, time, and consequences.
The world remains visually primary; controls and summaries clarify what the
player can know and do within it.

### Shared interface grammar

- Inspection, interface navigation, and provisional selection leaving time
  paused
- Every discrete commitment clearly identified before it advances time or
  exposes anything to consequence, while direct TRAVEL movement makes its
  accumulating spatial cost and Day-Band boundary continuously legible
- Known facts stated exactly and meaningful uncertainty presented honestly
- Information appearing beside the Citizen, Place, Node, Item, or situation it
  concerns whenever practical
- Broader detail remaining available through inspection rather than occupying
  the primary view continuously
- Changed facts showing what happened and why without success grades or
  detached reward screens
- Register transitions preserving visual, spatial, and historical continuity

### Register presentation

- **DWELL** presenting the Colony as a collective body, with an operational
  view that makes Citizens, Places, Practices, Projects, Resources, Civic
  Balance, and current situations understandable together
- **TRAVEL** following the named party at animal scale while terrain ahead,
  nearby Nodes, shelter, Day Band, rest need, Carry, and visible bodily state
  remain readable around it
- **RISK** concentrating the view around the selected Core Species' Crossing
  grammar, keeping planning information legible before commitment and
  presenting the continuous run without interruption by additional menus
- **MEET** taking focus within the existing scene and gathering the subject,
  participants, known facts, stakes, and response matrix while keeping the
  underlying Colony or Field recognizable
- **EMBODY** bringing one available Citizen and their immediate surroundings
  into intimate focus while routine interface recedes so motion, activity,
  relationships, and sensory life can carry the experience

### Visibility by context

The interface distinguishes between information the player may inspect and
information the simulation retains privately.

- Civic Shares, Role Load, Readiness, Role Balance, Housing Balance, known
  Telegraphs, and other actionable Colony facts remaining legible
- Colony Pressure remaining a hidden situational calculation whose causes are
  expressed through known state and Telegraphs
- Exposure remaining hidden while rest need, Wound, Tharn, and other
  experienced consequences remain visible
- Fractional production and Project contributions accumulating unseen until
  they produce whole results at DAWN
- The Record remaining a hidden factual back end
- Almanac, Chronicle, Tales, Citizen views, maps, and current canon images
  presenting the appropriate player-facing selections of established state
- Community Board mirroring selected Almanac information inside DWELL without
  gating access to it

### Selection and commitment

Selection is reversible inspection; Commit changes the world.

- Provisional selection revealing the exact immediate cost, affected subjects,
  and likely direction of consequence
- The player able to revise or leave a provisional selection while time remains
  paused
- Commit receiving a clear, consistent presentation across Registers
- Costs, elapsed time, and exposure to consequence beginning only at Commit for
  discrete actions, with direct TRAVEL movement taking effect through the
  player's continuous directional input
- The interface avoiding repeated confirmation steps when the committed action
  and consequence are already unmistakable
- Resolution remaining in the present scene wherever practical
- Changed facts appearing beside the Citizens, Items, Places, or Nodes that now
  carry them
- Multiple-Round MEETs retaining the same scene while updating their facts,
  stakes, and responses

### Contextual availability

Each interface shows the possibilities relevant to its actual task.

- The Launch selector presenting only mechanically eligible Citizens;
  unavailable Citizens remaining visible through DWELL and the Roster without
  appearing as selectable expedition candidates
- Core Citizens never presenting refusal, willingness, or personality approval
  because they remain fractional player characters
- Ordinary MEETs showing their authored relevant responses
- A relevant unavailable response remaining visible only when understanding its
  absence matters
- Irrelevant responses remaining absent
- Contested Away MEETs always showing **CONTEST → EVADE → PARLEY → YIELD →
  WITHDRAW** in that order
- An inactive contested family remaining greyed in place with one concise
  explanation based entirely on facts the party can know
- Provisional response selection revealing only the Tools, Supplies, Keepsakes,
  relationships, and Signatures that can express or change that response
- Focus resolving after Commit; when several Citizens qualify equally,
  selection occurring randomly
- State-transition MEETs presenting reconciliation and necessary allocations
  instead of artificial competing responses

### Presentation by Register

#### DWELL

DWELL uses an elevated, isometric-style operational view inspired by classic
base-building presentation. Its default angle makes the Colony readable as one
inhabited arrangement while supporting free camera rotation, spatial sliding,
and continuous zoom.

Every Core Colony and every operationally relevant part of its life remain
above ground and visibly presented. Rooms, Places, Citizens, connections, work,
storage, common space, and household life must remain readable through the
ordinary DWELL view. Operational visibility takes precedence wherever literal
ecological concealment would hide the civilization from play.

- Rotation allowing the player to examine Home freely from around its built and
  natural form
- Sliding carrying the view across the Colony without changing the selected
  subject or entering another Register
- Zoom moving continuously between whole-Colony relationships and the legible
  activity of particular Citizens, Places, and Practices
- The camera revealing the Colony directly through rotation, sliding, and zoom
  rather than requiring an underground layer or sectional-management system
- The broad view emphasizing placement, access, species form, current work, and
  Civic Balance across Home
- The close operational view preserving DWELL's collective stewardship even
  when an individual Citizen or physical detail becomes prominent
- Selection, inspection, Place designation, Practice construction, Project
  commitment, and Role assignment operating directly through the presented
  Colony
- Mouse retaining the phenomenology of interior life through dense above-ground
  rooms, joined edges, shared walls, covered links, and accumulated shelter
  while the inhabited whole remains visible

#### TRAVEL

TRAVEL uses a top-down overworld presentation in the tradition of classic
adventure games. A stable camera orientation follows the party through a
continuous, densely detailed Field while direct directional input drives its
overworld figure across the landscape.

- The party figure presenting a compact animated grouping of the actual named
  Citizens present, including the larger visible headcount of a Mouse party
- Continuous scrolling keeping the party, traversable ground, and approaching
  landscape in one spatially stable view
- Limited panning while paused allowing inspection of nearby known ground
- A modest zoom range preserving terrain readability without reducing the
  party to an abstract map token
- Soil, vegetation, cover, drainage, debris, shelter, human infrastructure,
  paths, Nodes, Margins, and Roadways remaining directly readable from above
- Directional controls driving the party as one subject while individual
  movement commands and formation management remain outside TRAVEL
- The remaining travel span appearing through the ground still credibly
  reachable in the current Day Band
- Actual movement consuming that span by path length, terrain, conditions, and
  burden until the next Day Band begins
- Rabbit bodies extending the distance available within the Band through their
  defined TRAVEL multiplier
- A Node becoming visually distinct within the landscape before engagement
  brings its consequential situation into MEET
- A Roadway occupying the approaching edge of the overworld before its Staging
  Post takes focus and RISK begins
- The party resuming from its exact Field position and remaining travel span
  after inspection, a brief interaction, or a completed Crossing

#### RISK

RISK uses a schematic Crossing view whose operative form changes with the
Colony's Core Species. The schematic is loosely backplated by the Staging Post
angle: the animals' present view from ground at the Roadway edge, looking across
traffic toward the far side.

- Transition from TRAVEL lowering attention to the party's roadside viewpoint
  while preserving the actual Staging Post, Roadway, Day Band, weather, traffic,
  River Spume, and far-side refuge
- The operative schematic normalizing Roadway orientation and scale enough to
  make movement, openings, and the complete proposed passage legible
- The background plate carrying place, atmosphere, and danger while the
  schematic carries planning information and player input
- **Rabbit RISK** presenting the broad traffic pattern, a represented opening,
  the party's complete line, and the selected far-side refuge
- **Mouse RISK** presenting pavement-scale features from which the player links
  three to six body-credible points into one continuous scurry
- **Squirrel RISK** presenting traffic geometry as a flowing trajectory with
  one or two planned redirects and a far-side anchor
- Land-bound Guests remaining within the Colony's Core-Species schematic while
  their actual bodies constrain credible features, openings, and movement
- Crow or Gull flight appearing as a parallel Flyer expression within the same
  Crossing rather than opening another view or Register
- Commit closing planning input and animating the complete schematic passage as
  one uninterrupted Continuous Run
- Traffic, sound, movement, and the Staging Post plate continuing beneath the
  schematic so the Run remains the bodily realization of the party's present
  Roadway rather than an abstract calculation
- Resolution carrying the whole party to the far side, applying visible group
  and personal consequences there, and returning to the top-down TRAVEL
  overworld unless a resulting situation opens MEET

#### MEET

MEET uses a deliberately presentational scene-and-matrix composition. Its
backplate depicts the actual location in which the situation occurs: the
engaged Node, affected part of Home, far-side Staging Post, or other owning
Place. Time, weather, condition, and persistent change remain recognizable even
when the foreground arrangement is staged for clarity rather than literal
spatial realism.

- The player-aligned party, Colony, Citizen, or other acting subject composed on
  the left
- The antagonist, counterpart, condition, opportunity, threatened Place, or
  other answering entity composed on the right
- Antagonist naming the dramatic position within the matrix without requiring
  hostility, personhood, or opposition
- Both sides depicted at the scale and separation needed to make participants,
  relationships, and stakes immediately readable
- A concise subject and one to three active stakes framing the situation
- The choice buttons occupying a stable response band while the backplated
  location and two sides remain prominent
- Ordinary MEETs presenting their contextual choices and contested Away MEETs
  preserving the five fixed family positions
- Provisional selection expanding the chosen response in place to show only its
  applicable Tools, Supplies, Keepsakes, relationships, Signatures, costs, and
  likely direction
- Commit resolving through the staged figures, animation, speech, sound, and
  Focus within the same composition
- A later Round retaining the backplate and participants while changed facts,
  stakes, and choices replace those already resolved
- Launch, Rest, Homecoming, Recognition, and other state-transition forms using
  the same presentational grammar with procedures shaped to their actual
  subjects
- Simulation time pausing during consideration while ambient motion may
  continue without changing world state

#### EMBODY

EMBODY enters through one present and available Citizen in a safe, usable part
of Home. Its presentation draws close to that particular life while preserving
the same above-ground Colony, surrounding Citizens, relationships, objects, and
current Day Band established in DWELL.

- Entry carrying the DWELL view toward the selected Citizen and Place before
  settling into the experience's authored intimate framing
- Participation ordinarily using close third person so the player remains able
  to see the Citizen whose bounded activity they share
- Presence using Citizen-height or companion framing near the animal's body and
  attention, including moments of looking, listening, approaching, settling,
  and waiting
- The presentation moving naturally between Participation and Presence when an
  authored experience benefits from both
- Routine operational summaries receding while the Citizen, immediate Place,
  motion, sound, touch, weather, and nearby relationships carry the experience
- Controls belonging to the particular activity and permitting only the
  movement, attention, or participation it requires
- The Citizen retaining their own exact posture, pace, response, and social
  behavior while the player lives as or remains with them
- Other Citizens remaining particular inhabitants of the same Home rather than
  controllable scenery
- Shared Meal widening the intimate presentation to the whole Colony through
  Open Table while every participant remains a named individual
- Natural release or player departure returning to DWELL without penalty
- Loss of Quiet Equilibrium ending the experience safely, returning attention
  to DWELL, and allowing an urgent situation to open MEET from its owning
  Register

### Information lenses

The game's principal information lenses remain available from any paused
Register presentation. Opening one pauses direct TRAVEL movement and preserves
the current camera, selection, location, and provisional decision so closing it
returns the player to the same moment.

- Selecting a visible Citizen, Place, Practice, Node, Outpost, Item, or other
  persistent subject opening its appropriate contextual view directly
- The **Almanac** presenting current known state, Telegraphs, schedules,
  forecasts, and meaningful uncertainty
- The **map** presenting known continuous geography, the current party position,
  remaining projected reach, discovered Nodes, Outposts, shelter, and
  established world changes
- The **Roster** and **Citizen view** presenting belonging, current location,
  availability, body, Role, relationships, possessions, current canon image,
  and access to the Citizen's Tale
- The **Chronicle** and **Tales** presenting the player-facing selections of
  Campaign Memory while the Record remains the hidden factual back end
- Earlier canon images remaining accessible through their established secondary
  history views
- Contextual access during MEET allowing the player to inspect known
  participants, Items, relationships, and capabilities before Commit
- Full reference access closing during a committed Continuous Run and returning
  as soon as RISK resolves
- Community Board providing an optional in-world route to selected Almanac
  information while every essential lens remains available through the ordinary
  interface
- Each authoritative fact receiving one functional presentation rather than
  being repeated across parallel ledgers

### Active Mode and attention

Home and Away are operationally exclusive and informationally permeable. The
player operates one Mode while remaining able to inspect the known state of the
other through the established information lenses.

- Launch transferring active operation from DWELL to the one active expedition
- Away remaining active throughout TRAVEL, RISK, Away MEETs, Stopovers, and the
  physical return journey
- Homecoming reconciling the expedition and restoring ordinary DWELL operation
- Home views opened during an expedition remaining informational rather than
  granting construction, Role assignment, Project commitment, or another
  Launch
- The Colony continuing predictably through its established civic state while
  attention is Away
- The Away party receiving no autonomous movement, rest, Node interaction,
  Crossing, or decision while another view has attention
- DAWN presenting the Colony's completed accounting concisely before returning
  to the active party
- A consequential Home MEET able to take focus when the situation calls,
  resolve through the ordinary shared clock, and return operation to the party
  at its persistent Field position
- The interface preserving a clear distinction between inspecting the other
  Mode and operating it

### Controls and accessibility

- Every control being fully remappable
- Keyboard, mouse, controller, and equivalent directional input supporting the
  same game actions
- Direct TRAVEL movement accepting digital or analog direction without changing
  its travel-span accounting
- DWELL rotation, sliding, zoom, selection, and camera reset remaining available
  without requiring simultaneous precision input
- Inspection, planning, provisional selection, and decision interfaces
  remaining untimed
- RISK planning allowing traffic observation to pause or advance in readable
  steps
- The committed Continuous Run requiring no reaction input, quick-time event,
  or mid-Crossing correction
- Text scaling, readable contrast, captions, and adjustable interface density
- Information conveyed through text, shape, position, and icon as well as color
- Greyed responses retaining readable labels and explicit reasons
- Adjustable camera motion, shake, flashing, and transition intensity
- EMBODY experiences using bounded controls appropriate to the activity and
  allowing departure without penalty
- Commit, return, pause, and contextual inspection using consistent controls
  across Registers
- Accessibility settings changing presentation and input demands while
  preserving the same world state and authored decisions

## 7.2 Art and sound

### Visual identity and Register contrast

MEDIAN uses grounded stylized realism at animal scale. Fur, feather, grass,
root, bark, mud, rain, and moving bodies meet asphalt, concrete, salt, rust,
rubber, plastic, drainage metal, and reflected road light. Animal civilization
grows within those materials through scavenging, craft, spatial knowledge, and
collective use.

The visual tone moves between warmth and magnitude. Home can be lively,
domestic, and gently storybook; the Field makes the same animals feel small
within a larger, colder, and less accommodating world. Danger gains weight
through scale, weather, sound, obscured visibility, and sudden motion while the
broader game retains color, tenderness, humor, and ordinary civic life.

Each Register expresses this identity through its established presentation:

- DWELL renders the Colony as a dense, visible, inhabited composition whose
  ordinary work can be read across rooms, paths, Places, and shared spaces.
- TRAVEL turns the terrain into a direct-drive overworld, keeping the party and
  the physical character of the landscape legible from above.
- RISK abstracts immediate danger into a species-shaped schematic grounded by
  the actual place, weather, traffic, and far-side refuge.
- MEET composes a situated decision as a deliberate tableau, placing the
  involved parties, condition, or opportunity around a stable field of choices.
- EMBODY brings the camera close enough for an individual Citizen, companion,
  activity, and surrounding Place to carry the experience.

Night retains the highway's material identity rather than erasing it. Headlight
wash, brake-light red, reflective signs, wet asphalt, distant windows, and
roadside lamps make darkness uneven, brilliant, and deeply shadowed.

### Strategic transparency

Every Core Colony is physically built above ground and remains visible as a
functioning settlement. Mouse Rooms, Rabbit common spaces, and Squirrel
connections differ in form while keeping their Citizens, relationships, and
ordinary operations available to the DWELL camera.

The camera may fade roofs, omit near walls, thin foliage, or clarify overlaps
so rooms, paths, and civic relationships can be read. This **strategic
transparency** belongs to presentation: open to the player does not mean
exposed within the world. Spatial fidelity preserves the implied Place and its
relationships while representational shorthand keeps them operable.

### Animal bodies and anthropomorphism

MEDIAN's Citizens are fully anthropomorphic as characters while retaining
recognizable animal bodies. They speak, work, build, remember, and form
communities; their movement, scale, posture, and physical capabilities remain
grounded in their species. Clothing, Tools, and crafted objects fit those
bodies and arise from scavenged roadside materials. The result is animal
civilization rather than miniature human society.

Citizens may stand, grasp, carry, gesture, and use posture as the activity and
their bodies permit. Locomotion remains species-faithful, and Crossing presents
grounded Citizens moving on four feet while Flyers use their established
parallel expression. Expression begins with the body—ears, head, stance, gait,
stillness, and relation to nearby animals—and may be supported by the face
without replacing recognizable animal anatomy.

### Material culture

Citizens build a material culture from natural matter and what the corridor
sheds. Bark, shell, grass, roots, twine, leaves, cloth scraps, plastic, paper,
rubber, wire, caps, fragments, and other found objects are selected and remade
at animal scale. A human-made object may enter animal life through a purpose
entirely different from the one for which it was made.

Clothing is selective rather than universal. Fitted scraps, wraps, cloaks,
belts, pouches, weather coverings, and adaptive devices can distinguish and
protect a Citizen while fur, feathers, posture, individual markings, and
Keepsakes remain equally important forms of recognition. Richly equipped
Citizens represent one end of the visual range rather than the everyday
minimum.

A Role may influence what a Citizen has at hand without becoming a uniform. A
Builder's lashings, a Gardener's gathering cloth, or a Healer's Remedy can make
present work legible while the Citizen remains an individual whose appearance
also carries species, history, relationships, and personal choice. Tools and
Supplies appear as unitary animal-scaled objects that their bearer can grasp or
carry.

Colony advancement improves the selection, fit, stitching, repair, adaptation,
and ornament of scavenged material. Civic grandeur arises through accumulated
care and mastery of limited matter. Weapons, armor, military uniforms, and
adventurer loadouts remain outside this visual language; conflict is expressed
through animal bodies, terrain, Tools, circumstances, and decisions.

A Keepsake that is worn or kept close can become part of a Citizen's visible
identity. Maiming and any adaptive device also persist respectfully in that
Citizen's current canon image, movement, and ordinary life. These features
remain consistent across the presentations generated from that image.

### Canon images and visual continuity

Each Citizen's current canon image anchors their recurring visual identity.
Species, body, markings, Keepsake, clothing, Maiming, adaptive devices, and
other persistent distinctions carry from that image into Roster views, MEET
tableaux, EMBODY, dramatic aftermaths, Register transitions, Citizen panels,
Chronicle presentation, and other generated setups. A lasting change to the
Citizen updates the current image while earlier images remain available
through secondary history views.

The Colony uses a small current canon representation set when complementary
views are needed to establish its spatial form, inhabited Places, material
culture, and ordinary life. Superseded views enter its visual archive at
meaningful stages, preserving season, damage, repair, growth, and remembered
occasions. These images complement the written Record and provide established
visual material from which later presentations can be composed.

A generated setup interprets current canon images within the actual place and
state being presented. Register composition, camera, light, posture, and
participating entities may change while persistent bodies, objects,
relationships, geography, and consequences remain recognizable.
In the model-assisted realization, the relevant existing canon imagery is
mandatory input rather than optional inspiration; Appendix C defines the
complete reference-and-amend method.

### Animal scale and human infrastructure

Human infrastructure retains its full magnitude around the animals. Lane
paint, barrier seams, guardrail bolts, tire fragments, drainage grates, culvert
mouths, vehicle cavities, signposts, and machinery give the player familiar
scale anchors while functioning as terrain, shelter, obstruction, resource,
and danger at animal scale. A short distance measured by a human body may hold
an extensive animal landscape.

Human presence is expressed through moving vehicles, maintenance, machinery,
roadwork, litter, runoff, noise, light, and sudden disturbance. Human bodies
remain outside the frame. The animals know **Giants** through partial
observation, inherited explanation, and the effects of an active human world,
while the absence of a visible operator lets that world retain its vast and
mostly indifferent character.

Vehicles and operating machinery can be shown in full. Their size, speed,
noise, vibration, and displaced air communicate force before proximity does.
Catastrophe is carried through obscured sight, narrowed perception, impact,
dust, weather, sound, aftermath, and animal reaction, preserving bodily stakes
without making explicit injury imagery the spectacle.

The same feature may change visual meaning with context. A culvert seen from
TRAVEL can become shelter, a Node, a flooded obstruction, or the entrance to an
Outpost; a wreck may be distant orientation, specialist salvage ground, or a
MEET backplate. Reusing persistent geography at different scales keeps the
world coherent across Registers.

### Light, weather, and season

Light, weather, and season make persistent geography visibly temporal. A Place
or Node remains recognizable as Morning becomes Midday, rain darkens its
materials, wind changes its movement, autumn thins its cover, or snow gathers
across familiar edges. These changes express the one world clock shared by Home
and Away.

Each Day Band carries a distinct light environment alongside its current
traffic, temperature, animal activity, and human disturbance. The transition
changes the readable condition of the world rather than applying a decorative
filter. Long shadows, glare, reflected road light, wet surfaces, fog, headlight
wash, and uneven darkness can reveal or conceal the same terrain in materially
different ways.

Weather acts upon surfaces, bodies, vegetation, visibility, shelter, sound, and
moving air. River Spume makes traffic's displaced air and debris visible around
the Roadway and its neighboring Field. Mechanically relevant conditions remain
legible through several aligned signals—such as motion, shape, texture, sound,
text, and icon—so their meaning survives changes in camera and accessibility
settings.

Season accumulates through the world. Plant growth and dieback, water level,
stored matter, animal presence, wear, repair, ground condition, and civic
adaptation give each period a material history. Familiar places therefore
change without becoming interchangeable seasonal versions of themselves.

Art and sound express the consequences already owned by terrain, Nodes,
Practices, Pressure, TRAVEL, RISK, and MEET. A storm can alter travel, threaten
a Place, or create a situated decision because those systems recognize its
effects; its presentation makes that state perceptible and particular.

### Environmental and civic sound

Sound makes the Corridor readable as well as present. Traffic has direction,
density, rhythm, mixture, approach, and mass; a large vehicle may first arrive
as low vibration through the ground. Changes in engines, horns, impacts,
machinery, rain, displaced air, or unusual quiet can disclose a changed
condition before its cause enters view.

Home sounds inhabited and held together. Species-specific movement,
conversation, work, construction, teaching, shared activity, weather against
shelter, and the filtered presence of the road form its civic sound bed. Quiet
Equilibrium sounds secure enough for ordinary details to be heard. Guest
Citizens add their own movement, calls, song, echo, or other species-shaped
presence as part of living at Home.

The Field opens that sound bed outward. Wind, vegetation, water, insects,
distant animals, drainage, human disturbance, and traffic locate the party
within actual terrain. RISK brings the Roadway forward until speed, gaps,
vehicle type, River Spume, and approach can be read by ear as well as sight.
Every mechanically important audio signal receives an aligned visual form.

Individual sound remains bodily. Footfall, breath, fur or feathers against
material, carried objects, vocalization, and adaptive devices help distinguish
species and Citizens. Maiming changes movement sound consistently and
respectfully. When Tharn strikes, the wider field narrows abruptly around the
Citizen's breath, pulse, fixation, and immediate peril.

Landscape Voice occupies its own clear narrative register. Its human narrator
can describe country, weather, movement, and simple events over the world while
remaining distinct from Citizen speech, animal cultural expression, and
mechanical notification.

Music is sparse and adaptive. It may support transitions, Homecoming,
ceremonial MEETs, wonder, grief, and other authored changes in emotional scale,
then recede so the place itself can be heard. Environmental and civic sound
remain primary. The score follows what has become perceptible or meaningful to
the player, preserving the shock of concealed dangers such as Tharn.

## 7.3 Content-authoring doctrine

This section governs the creation of player-facing MEDIAN content. The
Authorial Grammar governs terminology, capitalization, semantic typography,
and specification prose; the present doctrine governs how an established game
system becomes a particular place, situation, choice, image, or passage.

**Author a concrete situation in the physical world, identify the existing
system that owns it, and let the player meet it through the appropriate
Register. Content gives established mechanics a particular place,
participants, stakes, choices, and consequences.**

### Authoring from established play

- Beginning with a real state already held by the world, Colony, Place, Node,
  Citizen, party, Item, relationship, or clock
- Identifying the existing mechanic and Register that can make that state
  playable
- Giving the state concrete geography, bodies, material, time, and present
  circumstances
- Building player choice from credible affordances within that situation
- Returning the outcome to the same persistent world through its established
  owner
- Allowing authored exceptions when they express a particular species, Guest,
  Place, object, or event clearly enough to remain bounded
- Expanding the system only through an explicit design decision rather than
  using one piece of content to imply a new universal mechanic

### Constructing a MEET

Chapter 1.5 owns the shared MEET form. A content author supplies the particular
situation that form will present:

1. Name the owning system and the world-state facts that make the MEET
   eligible.
2. State its subject in one concrete sentence.
3. Establish the actual Place or Node, Day Band, conditions, participants, and
   known uncertainty.
4. Select one to three present stakes.
5. Author materially different responses and the circumstances that make each
   available; contested Away MEETs retain their five canonical response
   families and order.
6. Attach each Tool, Supply, Keepsake, relationship, Signature, or civic
   commitment to the exact response it can express and state what it changes.
7. Resolve shared results first, then assign bodily, personal, material, and
   relational consequences through causal involvement.
8. Return every changed fact to its established owner and identify any
   credible continuation or Campaign Memory expression.

An ordinary decision MEET offers at least two meaningfully different courses.
A state-transition MEET instead earns its presentation by reconciling several
important persistent facts together. Multiple Rounds follow Chapter 1.5 and
arise because a committed response materially changes the situation while
leaving it open.

The **particularity test** asks whether the content would remain substantially
unchanged if moved to another species, place, time, or condition. A strong
MEET depends upon at least one of those facts and expresses that dependency in
its available responses, costs, or consequences. Reusable structure may
remain, while the played situation belongs to this world state.

### Names and animal language

Names translate the relationship between an animal community and its world.
They favor concrete animal-scale perception—material, enclosure, openness,
height, route, sound, weather, use, or remembered history—while remaining
plain enough to speak and recognize in play.

Functional names remain shared game terms. Garden, Workshop, Hearth, Gathering
Place, and other Practices keep the same names across Colonies; the Practice
also gives its Place that functional name. Proper names belong to particular
Colonies, Reaches, Nodes, landmarks, and remembered locations.

Core-Species cultures carry tendencies rather than exclusive vocabularies:

- Mouse names often notice edges, interiors, joins, shelter, and the material
  enclosing a place.
- Rabbit names often notice shared ground, breadth, neighborhood, company, and
  gathering.
- Squirrel names often notice height, anchors, lines, crossings, direction, and
  reach.

A memorable event, inhabitant, use, danger, or change may name a place for any
species. Names such as Rushbottom or Graywall work because they compress a
physical or remembered relationship into speakable geography. Curated name
banks may support each culture without becoming procedural laws.

Every individual Citizen receives an appropriate Given Name from a curated
cultural set. An After-name arises more rarely from durable personal history.
The two collective Citizen forms receive their approved household names. Guest
species use their canonical short names in headings, tables, labels, and rules;
descriptive prose may also use an established longer species name.

A Hyphen-bound form marks one deliberately adopted animal-language word whose
translation requires several English elements, such as After-name or
Prior-life Tale. Ordinary compound names follow ordinary prose rather than
acquiring hyphens as decorative animal flavor.

Species voice arises from selective attention rather than accent, intelligence
ranking, or rigid syntax. Rabbit expression may first notice what gathers life
and keeps shared ground safe; Mouse expression what joins, opens, encloses, or
fails at fine scale; Squirrel expression what connects points across height,
distance, and motion. Chronicle passages, Tales, dialogue, and scenes may use
those tendencies to present the same established world through animal culture.
They change emphasis, comparison, and assumed vocabulary without changing
facts or constructing separate realities.

An unfamiliar human object may first be expressed through sensed material,
movement, sound, danger, or use. Repeated familiarity establishes an ordinary
shared term. MEDIAN's animals retain knowledge of their human-made environment
rather than rediscovering common fences, drains, vehicles, and structures each
time they appear.

### Narrative throughout the Concept Sourcebook

Narrative enters the Concept Sourcebook in the form best suited to its present
work. It makes time, relationship, particularity, decision, consequence, or
remembered change legible while the surrounding specification remains the
authoritative account of the game.

1. **Sustained narrative** carries a major sequence whose experience depends
   upon continuity. The Founding Escape is its primary use. A continuous Away
   expedition may also thread through Part V so Launch, TRAVEL, RISK, MEET,
   Return, and Homecoming can be understood as one accumulating journey.
2. **Recurring lived moments** return to the established story Colonies,
   Citizens, Places, objects, and relationships at different points in their
   histories. Each later appearance respects what earlier appearances have
   made true, allowing familiarity and attachment to accumulate across the
   book.
3. **Worked play sequences** show the temporal and causal operation of systems
   in which player judgment matters. They follow concrete state through
   available choices and resolution, then return changed facts to their
   persistent owners.
4. **Literal game presentations** reproduce Chronicle, Tale, Almanac, MEET,
   RISK, Community Board, and other game forms when the form itself is being
   demonstrated. Their language and design express the authority and limits of
   the actual presentation.
5. **Narrative-bearing environment and art** use Landscape Voice, captions,
   recurring geography, visual continuity, and question-bearing physical
   detail to imply lived history from established canon. Suggestive detail
   invites attention while rules introduced by the image receive direct
   expression in their owning prose.

Part openings vary with the transition they perform. Sustained narrative
appears when a threshold benefits from being lived as a sequence. A full-plate
Part opening may instead carry one or two sentences of Landscape Voice along
its lower edge when country, weather, movement, or a simple event gives the
transition meaning. Another opening may use a recurring Citizen, a game
presentation, or a silent plate. The seven Parts therefore share a deliberate
rhythm without repeating one compulsory opening device.

Narrative sits beside the system or experience it illuminates. Clear formulas,
inventories, comparisons, and fixed relationships favor tables, diagrams, or
infographics; narrative favors bodily scale, uncertain judgment, sequence,
recognition, relationship, departure, return, and accumulated history. A
narrative augment earns space through one of those functions rather than by
restating adjacent rules.

Ordinary life establishes what danger can change. Work, proximity,
hospitality, accommodation, rest, observation, small disagreements, and
familiar routines supply the majority of recurring lived material. Hazard and
loss gain weight through their effects upon lives and places the reader already
knows.

The three Core-Species civilizations receive balanced cumulative presence
across the complete book. Rabbit's sustained role in the Founding Escape is
answered by strong Mouse and Squirrel presence through later recurring
moments, worked sequences, art, and examples. Selection follows the needs of
each passage while book-level review preserves parity.

Narrative augments remain flexible in length, layout, and frequency. Their
authoring brief identifies the governing section, narrative function, form,
participants, place and time, incoming state, outgoing state, visual or
Register relationship, and reason the material improves understanding. The
Augments Phase assigns those briefs page by page after the Appendices have been
detailed.

### Positive canon and illustrative material

The GDD expresses current design through positive canon: it states the thing
that exists, the action the player takes, the rule the game applies, and the
consequence the world retains. An introductory passage establishes purpose and
experience before qualifications. Boundaries appear where they protect an
actual distinction in play.

When a former mechanic, entity, or term is removed, the active specification
closes around its approved successor. Historical explanation, reconciliation
notes, and declarations that the former material was removed belong to
provenance rather than to the playable design.

Examples make an established rule concrete. An example's particular names,
numbers, layout, dialogue, labels, meters, and visual composition govern only
the propositions the text explicitly adopts. A concept image or sample passage
may reveal a strong direction while remaining illustrative as a whole.

Authorial review can promote a proposition from illustrative material into the
GDD. The adopted proposition is then stated directly in its canonical home so
future readers need not infer a rule from an image, discarded draft, or
development conversation.

### Numerical restraint

MEDIAN uses a number when the number creates a legible decision, preserves an
important ratio, or gives a bounded system the exactness it needs. Whole units,
small ranges, and a few memorable fractions carry most player-facing
relationships. Fractional contribution accumulates quietly and appears when it
becomes a whole award through its established cadence.

- One value carrying one meaning across the systems that use it
- Exact formulas reserved for stable relationships the player can reason about
- Qualitative state carrying differences that do not benefit from arithmetic
- A bounded range expressing variation more clearly than a long probability
  table
- Examples using the fewest numbers needed to demonstrate the rule
- Display precision matching the decisions actually available to the player
- Resource costs, chances, durations, and thresholds remaining identifiable as
  tuning when playtesting must determine their final values

An example quantity demonstrates behavior unless the text establishes it as a
rule. A canonical value states a designed relationship, such as Body Unit
parity or a defined Capacity contribution. Tuning changes may adjust balance
within that relationship while preserving its purpose.

### Canonical, provisional, tuning, and open content

The GDD distinguishes four authorial states when the distinction materially
helps a reader use the design:

| State | Meaning |
|---|---|
| **Canonical** | Authorially approved v0.5 design stated in its owning section. |
| **Provisional** | Approved direction whose exact structure, wording, or bounded detail remains subject to the identified later pass. |
| **Tuning** | A quantity or balance relationship to be tested without reopening the system's purpose. |
| **Open** | An unresolved design question awaiting authorial judgment. |

These states are expressed locally in the owning prose. They do not require a
second registry, completeness matrix, or lifecycle. Source documents, corpus
atoms, drafts, examples, and concept images provide evidence; the GDD receives
the approved result.

An open matter remains open until decided. Authors may build around a known
gap when its boundary is clear, while content whose result depends upon that
decision waits for the decision itself.

### Landscape Orientation

**Landscape Orientation** is the content-authoring method for turning a
specific physical location into MEDIAN terrain, visual composition, narration,
and situated play.

1. Establish the governing specifications and known world state.
2. Construct a concrete place with an exact physical cross-section, grade,
   materials, vegetation, drainage, light, weather, sound, visibility, and
   human infrastructure.
3. Select an animal-scale observation point within that place.
4. Determine what is visible, concealed, reachable, traversable, useful,
   dangerous, familiar, and unknown from that point.
5. Read the same physical facts through the bodies, species, purposes, and
   histories actually present.
6. Derive candidate movement, choices, situations, visual compositions, and
   Landscape Voice passages from those relationships.
7. Check every candidate against the governing specification and obtain the
   authority appropriate to any proposed addition or exception.

- One physical world supporting several bodily readings
- Terrain shaping perception, available choices, movement, and consequence
- Environmental art able to reveal candidate affordances and development needs
- A compelling image or passage remaining illustrative until its propositions
  receive explicit authorial acceptance
- Landscape Voice rendering established play while the governing systems and
  persistent state retain authority
- Locations differing through causal geography as well as visual identity

## 7.4 v0.5 scope and explicit deferrals

MEDIAN v0.5.0 is a concept book about a theoretical game. It establishes what
that game is, how its parts relate, what the player experiences, and which
principles govern future elaboration. Conceptual coherence is the completion
standard for this first draft.

### Concept-book completeness

The provisional first draft is complete because it establishes:

- The attachment-forward premise, player position, and dramatic cycle
- One persistent world across Home and Away and the five Registers
- The Corridor's geography, ecology, time, traffic, and environmental change
- The Colony's Places, Practices, Roles, Projects, Civic Balance, Resources,
  population, and progression
- Core and Guest Citizens as named lives with species-shaped bodies,
  affordances, residences, relationships, and histories
- Launch, TRAVEL, Field Nodes, Carry, RISK, MEET, Exposure, Wound, Maiming,
  Tharn, Rest, Outposts, return, and Homecoming
- Quiet Equilibrium and EMBODY as the lived positive expression of sanctuary
- Campaign Memory, the Almanac, the Founding Escape, campaign horizons, and
  continued play
- The interface, art, sound, and content-authoring doctrines that make those
  systems one recognizable work

These relationships define a game that can be imagined, discussed, tested for
internal consistency, and developed further without requiring the concept book
to function as a software-production plan.

### Dedicated Items and Resources conceptual tuning phase

- Tune the resource economy as one connected acquisition, transport,
  consumption, and construction loop
- Establish Node yields, Carry burden, Jostle exposure, expedition duration,
  Sustenance generation, preservation, travel drain, and other recurring costs
  before fixing major recipes
- Set the material and Civic Share-Day requirements for Places, Practice
  improvements, Tools, Supplies, Outposts, restoration, and Civic Dedications
  against that shared economy
- Test the distinct Mouse, Rabbit, and Squirrel Carry and travel experiences
  while preserving their aggregate civic parity
- Evaluate large costs through the expeditions, risks, time, and domestic
  opportunity costs needed to satisfy them rather than by comparing isolated
  Scrap totals
- Resolve the provisional Supply-class names within the same connected pass

This is conceptual balance work for a later revision of the theoretical game.
It preserves the adopted system relationships while making their quantities
coherent.

### Other bounded tuning

- Population-growth timing, maturation cadence, and the remaining housing
  multipliers
- World Pressure cadence, eligibility thresholds, smoothing, clustering, and
  Telegraph frequency
- Season length, weather generation, traffic thresholds, Node renewal, and
  broader campaign pacing
- Exact chances, ranges, durations, and content frequencies marked for tuning
  in their owning sections

### Exemplified content

The first draft defines the grammar and representative content for MEETs,
Places, Nodes, Practice improvements, Citizen histories, names, Tales,
Chronicle selections, Landscape Voice, and visual setups. A later authoring
pass may create broader banks and additional examples. The complete Practice
catalogue will give each Practice at least one improvement.

Appendix development precedes the Augments Phase. Once the Appendices carry
their intended reference, language, conceptual, manifestation, and market
treatments, the Augments Phase will map narrative, diagrams, tables,
infographics, game presentations, partial-page illustration, and full plates
across the unified book. That pass applies the narrative doctrine in Section
7.3 and determines the exact placement of each form without reopening the
systems it explains.

### Open language and design

**Family** remains the provisional term for the domestic relationship developed
in Chapter 3.7. Any other matter explicitly marked open in its owning section
remains available for direct authorial resolution. A quiet gap carries no
implied mechanic.

### Manifestations and later-version work

The desktop and console computer game is the primary full-spectrum theoretical
manifestation described by this GDD. Tabletop roleplaying, cooperative
fixed-content card, and standalone mobile forms are translations developed in
their companion framework and may receive separate concept books.

Later-version material may extend MEDIAN after an explicit decision brings it
into the relevant scope. Ideas retained outside v0.5 remain evidence for that
future work rather than unfinished obligations of this first draft.

## 7.5 Canonical summary

MEDIAN is an attachment-forward animal-colony base builder set within the
median strips of an active modern highway. The player stewards one permanent
Home whose safety, beauty, capability, and history arise from a small
population of named Citizens. Sanctuary is achieved through credible Game
Logic, and its deepest reward is the successful stillness in which the player
can notice the Colony as a place worth caring about.

The game holds one persistent world across Home and Away. DWELL lets the player
understand, build, arrange, and sustain the Colony. TRAVEL directly guides one
party through the Field. RISK expresses the bodily threshold of Crossing in a
different form for Mouse, Rabbit, and Squirrel. MEET presents focused
situational decisions and consequential transitions wherever they arise.
EMBODY lets the player live as or be with an individual Citizen when Quiet
Equilibrium releases attention from urgent stewardship.

Home grows through Places designated by Builder, Residences, Practices,
Projects, and the Civic Shares of its Citizens. Roles express how those shares
meet current Load; Readiness reveals the Colony's ability to answer it, and
positive Load becomes Pressure. Completed Practices can contribute durable
strength while active Role support enables their fullest civic and productive
use. Species placement makes the physical organization of Home matter, and
Projects turn chosen Citizens' shares toward lasting change.

Mouse, Rabbit, and Squirrel inhabit the same world through distinct bodies and
civilizational grammars. Mouse JOINs protected interiors, Rabbit GATHERs around
open common ground, and Squirrel CONNECTs Places through a branching Web. Body
Units preserve civic parity while population, Carry, TRAVEL, RISK, Residence,
and spatial expression give each campaign a different character. Guest
Citizens retain their own species, bodies, residences, routines, and bounded
Signatures while belonging to the Colony as full Citizens.

Away begins with Launch and carries particular lives into a continuous world
of Reaches, Margins, Roadways, Nodes, Outposts, weather, traffic, and other
animals. Carry creates useful bodily constraint. Exposure accumulates through
the journey; Wound, Maiming, and Tharn make consequence personal without
turning every expedition into attrition. Rest and Outposts offer partial
relief. Return follows the same geography, and Homecoming receives the party's
Citizens, Cargo, Guests, injuries, relationships, civic availability, and
memory back into Home.

MEET is the shared grammar through which a Colony or party faces a concrete
situation. It gathers the actual place, participants, known facts, stakes, and
available responses; Tools, Supplies, Keepsakes, relationships, Guest
Signatures, and civic commitments express those responses. Focus identifies
whose life a Round follows while resolution remains collective and
consequences return to the systems and named lives that own them.

The Campaign Memory preserves what this Colony has become. Its hidden Record
holds factual history; the Chronicle and Tales select and translate that
history for the player; canon images preserve the changing visual truth of
Citizens and Home. The Almanac presents present state and known possibility.
Together they allow building, departure, consequence, return, and remembrance
to deepen one another across a continuing campaign.

The Founding Escape begins that campaign by chaining DWELL, EMBODY, MEET,
TRAVEL, and RISK into the flight from the ancestral Colony and the choice to
found a new Home. Population Tiers, Practice improvements, Guests, Outposts,
the Metropolis, the Interchange, and the Ancestral Home provide horizons rather
than a mandatory victory sequence. The Colony can grow, endure, remember, and
become enough.

Across every system, MEDIAN uses one governing movement:

**Sanctuary → Exposure → Consequence → Return → Memory**

# APPENDICES

The Appendices make MEDIAN findable and carry material that usefully describes
the work from outside its principal game-and-world reading path. They support
the unified Concept Sourcebook rather than becoming a second GDD or a separate
technical volume.

Reference Appendices condense, tabulate, and cross-reference rules whose full
meaning remains established in the main treatment. Conceptual Appendices hold
essays, translation plans, and contextual analysis that belong outside the
beam. Every Appendix states current positive m050 design. Superseded mechanics,
decision history, source reconciliation, implementation contracts, tuning
registries, QA records, and production metadata remain outside the published
book.

## Appendix A — Lexicon and Canonical Usage

MEDIAN's written forms carry game meaning. Capitalization, all-caps operators,
dots, hyphens, and species grammar let the reader distinguish a defined game
concept, an act of play, a semantic address, a translated animal word, and an
archetypal animal body.

The chapters introduce that language through play. This Appendix gathers its
compact forms for reference and supplies concise principal-treatment locations.
Its final alphabetical Lexicon will include only terms that carry a stable
MEDIAN meaning in the current book.

### How MEDIAN Writes

| Meaning | Written form | Examples | What the form tells the reader |
|---|---|---|---|
| Defined game concept | Initial Caps | Citizen; Place; Body Unit; Quiet Equilibrium | The word or phrase carries a stable MEDIAN definition. |
| Experiential operator | ALL CAPS | DWELL; TRAVEL; RISK; MEET; EMBODY | The player acts through one of the game's five Registers. |
| Core-Species spatial operator | ALL CAPS | JOIN; GATHER; CONNECT | A civilization expresses its characteristic relationship to inhabited space. |
| Semantic address | Dot-delimited UpperCamelCase in code style | `Home.Colony.Practice.Garden`; `Away.Crossing` | An MSID gives one game property a stable address across prose, navigation, and manifestations. |
| Animal-language word | Hyphen-bound form with one initial capital | After-name; Prior-life Tale | Several English elements translate one deliberately adopted word in an animal language. |
| Archetypal Core Species | Bare Initial-capped singular with singular agreement | Mouse builds a Manor House. | One representative body expresses the characteristic logic of its species. |

#### Registers and experiential operators

| Register | Mode | Operator | Player relationship |
|---|---|---|---|
| Colony | Home | **DWELL** | Sustain, organize, build, and inhabit collective life. |
| Field | Away | **TRAVEL** | Direct an expedition party through the continuous world. |
| Crossing | Away | **RISK** | Commit particular bodies to immediate spatial danger. |
| Encounter | Home or Away | **MEET** | Answer a bounded situation through consequential choice. |
| Embodiment | Home | **EMBODY** | Live as or remain with a Citizen inside achieved sanctuary. |

#### Core-Species spatial operators

| Core Species | Operator | Civic expression |
|---|---|---|
| Mouse | **JOIN** | Adjoining rooms and sheltered edges become one protected inhabited body. |
| Rabbit | **GATHER** | Places form around open common ground with protective edges and nearby refuge. |
| Squirrel | **CONNECT** | Anchors and routes become a resilient Web with credible alternate movement. |

An MSID belongs to the game property it identifies. Page number, chapter,
manifestation, and implementation may change while the semantic address
persists. The final Lexicon will expose MSIDs as a restrained reference column
after its term set and the Sourcebook's navigation hierarchy are stable.

> **Typography is part of MEDIAN's semantic system. It tells the reader what
> kind of meaning a written form carries before the surrounding prose explains
> that meaning in full.**

### Alphabetical Lexicon

The Lexicon includes terms whose MEDIAN-specific meaning recurs across systems
or whose exact distinction prevents the game from being misread. Content names
with a single local use remain in their owning chapter or reference Appendix.
The treatment pointer leads to the term's principal explanation rather than
listing every place it appears.

| Term | Concise meaning | Principal treatment |
|---|---|---|
| **After-name** | A rare public name earned through a Citizen's durable life history. | § 6.1, Distinctions and After-names |
| **Almanac** | The continuously available lens for present state and known, scheduled, forecast, or possible future circumstances. It stands outside Campaign Memory. | § 6.1, The Almanac |
| **Ancestral Home** | The ruined original Colony from which the Founders escaped, preserved as a distant campaign horizon and a place of possible return. | § 6.5, The Ancestral Home |
| **attachment-forward** | MEDIAN's design direction toward making particular Citizens, Places, objects, and histories knowable, memorable, and worth protecting. | § 1.2, The attachment-forward base builder |
| **Away** | The outward Mode in which responsibility extends from Home through a particular expedition party. | § 1.4, Home and Away; Part V |
| **Baseline** | The complete authored realization of a presentation that can be delivered immediately without model assistance. | Appendix C, Two channels and two realizations |
| **Beautification** | Colony-wide passive progress supplied by civic Roles without a defined material output; its thresholds create persistent, mechanically inert Frills. | § 3.6, Beautification |
| **Biome** | A recurring environmental grammar of ground, vegetation, water, infrastructure, shelter, exposure, and spatial rhythm from which a Reach is realized. | § 2.3, Biomes and Founding Reaches |
| **Body Unit** | MEDIAN's normalization layer for aggregate mechanics: one Rabbit, one Squirrel, two Mice, or one v0.5 Guest Citizen ordinarily equals one Body Unit. | § 4.1, Body Units |
| **Campaign Memory** | The campaign-wide historical architecture combining one hidden factual Record with written and visual expressions made for the player. | § 6.1, Campaign Memory |
| **Capacity** | The amount available within one Civic Balance axis to answer that axis's Load. | § 3.2, Civic Balance |
| **Cargo** | Fungible resources carried by an Away party within its shared Carry; personal Tools, Supplies, and Keepsakes occupy their own positions. | § 5.2, Carry and the growing haul |
| **Carry** | The visible party-wide capacity that holds Cargo and makes the growing haul matter to TRAVEL, RISK, and MEET. | § 5.2, Carry and the growing haul |
| **Choice Event** | An authored bounded situation that enters its owning context through MEET and uses MEET's shared choice-and-aftermath grammar. | § 1.5, Choice Events |
| **Citizen** | A named living member of the Colony whose body, relationships, belongings, history, and possible future remain particular across every Register. | § 4.1, Citizenhood |
| **Civic Balance** | The shared comparison of Capacity and Load within each separate Housing or Role axis, producing Readiness, Covered, or Pressure. | § 3.2, Civic Balance |
| **Civic Dedication** | A large, escalating commitment of resources incorporated throughout Home to trigger eligible Colony Tier recognition. | § 6.3, Civic Dedication |
| **Civic Pressure** | The Colony's separate Housing and Role Pressures considered together as a profile rather than summed into one value. | § 3.2, Civic Pressure, World Pressure, and Colony Pressure |
| **Civic Share** | The Body-Unit-normalized measure of ordinary Home responsibility contributed by an available Citizen through a Role or committed to a Project. | § 3.2, Role Balance |
| **Colony** | The particular permanent civic settlement at Home: a community, an inhabited built place, and an accumulating history. | § 3.1, Home |
| **Colony Pressure** | The hidden momentary director calculation that weighs the Civic Pressure profile with current circumstances and recent Home MEET history to influence when a Home situation requires attention. | § 3.2, Civic Pressure, World Pressure, and Colony Pressure |
| **Colony Tier** | A lasting recognition of the stable scale a Colony has reached, shared mechanically by number and expressed through a Core-Species civic name. | § 6.3, The four Colony Tiers |
| **Community Board** | The Gathering Place improvement that gives selected information already known to the Colony a persistent shared expression in DWELL. | § 3.4, Community Board |
| **CONNECT** | Squirrel's spatial operator: anchors and traversable links form a resilient inhabited Web. | § 2.3, Squirrel — CONNECT; § 4.2 |
| **Core Residence** | A Place used to house Core Citizens, providing Housing Capacity according to its usable and Well-Placed state. | § 3.3, Core Residence |
| **Core Species** | Mouse, Rabbit, or Squirrel as the civilization chosen for a campaign, shaping spatial expression at Home and the fundamental experience of RISK. | § 4.2, The Three Core Species |
| **Corridor** | The continuous longitudinal organization of The Highway through successive Reaches. | § 2.2, From Corridor to Reach to Median |
| **Covered** | The state of a Civic Balance axis whose Capacity exactly equals its Load, producing neither Readiness nor Pressure. | § 3.2, Shared balance grammar |
| **Crossing** | The concentrated Away Register in which a party traverses a Main Roadway or smaller Reach-border road through RISK. | § 1.4, The Crossing Register; § 5.3 |
| **DAWN** | The explicit transition that resolves the completed day's accounting, advances the calendar, reports meaningful change, and opens Morning. | § 2.5, DAWN and the Playable Day; § 3.6 |
| **Day Band** | The sole mechanical unit of world time: Morning, Midday, Evening, or Night. | § 2.5, DAWN and the Playable Day |
| **Distinction** | Narrow favorable recognition grounded in a Citizen's meaningful conduct. | § 6.1, Distinctions and After-names |
| **DWELL** | The operator of the Colony Register: understand, build, arrange, and sustain collective life at Home. | § 1.4, The Colony Register; § 3.2 |
| **EMBODY** | The operator of the Embodiment Register: live as or remain with a particular Citizen inside achieved sanctuary. | § 1.4, The Embodiment Register; § 3.8 |
| **Encounter** | The cross-modal Register that brings a bounded consequential situation into focused choice. | § 1.4, The Encounter Register; § 1.5 |
| **Expedition Guest** | A Guest Citizen who may Launch, bears personal Away consequence, and carries one Away Signature and an individually authored Home Role. | § 4.3, Expedition Guests |
| **Exposure** | A hidden six-step, per-Citizen measure of accumulated life beyond ordinary safety that weights applicable personal consequence toward the serious end of its valid range. | § 5.6, Accumulated Exposure |
| **expression** | A Tool, Supply, Keepsake, relationship, Signature, civic commitment, or other capability through which a selected MEET response becomes possible or changes. | § 1.5, Responses and expressions |
| **Field** | The continuous Away Register in which the player directly moves a particular expedition party through the Corridor. | § 1.4, The Field Register; § 5.2 |
| **Field Card** | An occasional situated interruption between Nodes that keeps the Corridor active without displacing intentional exploration. | § 5.2, Field Cards |
| **Focus** | The Citizen whose life a MEET Round naturally follows in presentation after the collective response has been committed. | § 1.5, Focus; § 4.6 |
| **Frill** | A small, persistent, mechanically inert expression of Colony life created when Beautification reaches a threshold. | § 3.6, Beautification |
| **Game Logic** | MEDIAN's legible and causally trustworthy rules, through which competence and stability release attention for attachment. | § 1.3, Game Logic opens Attachment Space |
| **GATHER** | Rabbit's spatial operator: Places face and protect open common ground while retaining nearby refuge. | § 2.3, Rabbit — GATHER; § 4.2 |
| **Guest Citizen** | A named non-Core animal welcomed into the Colony with full civic standing, a Residence, and one bounded species Signature. | § 4.3, Guest Citizens |
| **Guest Residence** | The dedicated or explicitly incorporated accommodation that satisfies one Guest Citizen's species-specific Residence Fit. | § 4.3, Guest Residence |
| **Home** | The inward Mode centered upon responsibility for the permanent Colony. | § 1.4, Home and Away; § 3.1 |
| **Home Median** | The particular geographic median occupied by the Colony; it is geographic shorthand rather than the Colony's name or the Home Mode. | § 2.2, The Colony and the Home Median |
| **Homecoming** | The state-transition MEET that ends an expedition and reconciles its returned lives, material, relationships, and consequences with Home. | § 5.8, The Homecoming MEET |
| **The Highway** | The complete physical setting formed by the Corridor's Median, Main Roadways, Margins, Sound Walls, and situated human infrastructure. | § 2.1; § 2.2, The Highway in cross-section |
| **Housing Balance** | Usable Core Residence Capacity minus the Body-Unit Housing Load created by Core Citizens. | § 3.2, Housing Balance |
| **Housing Capacity** | The Body Units of Core Citizens that completed usable Core Residences can accommodate. | § 3.2, Housing Balance |
| **Housing Load** | The Body-Unit housing obligation created by Core Citizens belonging to the Colony. | § 3.2, Housing Balance |
| **Housing Pressure** | The uncovered Body Units produced when Core Citizen Housing Load exceeds usable Core Residence Capacity. | § 3.2, Housing Balance |
| **JOIN** | Mouse's spatial operator: adjoining rooms and sheltered edges become one protected inhabited body. | § 2.3, Mouse — JOIN; § 4.2 |
| **Keepsake** | A persistent emotional object whose meaning and bounded contextual effect belong to one Citizen's life. | § 4.6, Keepsakes |
| **Landscape Voice** | MEDIAN's human third-person, landscape-attentive narrator, which interprets present play without adopting a named protagonist or an animal cultural voice. | § 5.9, Landscape Voice |
| **Launch** | The state-transition MEET in which the player selects and commits an eligible expedition party, transferring active operation from Home to Away. | § 5.1, The Launch MEET |
| **Load** | The gross weight of one civic responsibility, compared only with Capacity belonging to the same Civic Balance axis. | § 3.2, Shared balance grammar |
| **Maiming** | A lasting bodily change caused by a maiming injury; its accompanying acute Wound may heal while the Maiming remains. | § 5.6, Forms of personal consequence |
| **Main Roadway** | Either continuous lateral traffic band flanking the Median and separating it from a Margin. | § 2.2, The Highway in cross-section |
| **MEET** | The operator of the Encounter Register: frame and resolve a bounded consequential situation through contextual choice and aftermath. | § 1.5, MEET |
| **Median** | The central habitat band that continues through successive Reaches between the two Main Roadways. | § 2.2, From Corridor to Reach to Median |
| **Mode** | The inward or outward center in which primary life and responsibility are currently situated: Home or Away. | § 1.4, Mode, Register, operator, and view |
| **Moment Brief** | A bounded projection of current state and relevant Record facts used to realize one truthful narrative or visual presentation. | Appendix C, The Moment Brief |
| **MSID** | A dot-delimited semantic address that identifies one game property independently of page, chapter, manifestation, or implementation. | Appendix A, How MEDIAN Writes |
| **Node** | A fixed recognizable place in the Field whose material, ecology, shelter, inhabitants, alteration, or history can matter across visits. | § 5.4, Nodes in the Field |
| **Operator** | The characteristic action through which the player engages a Register. | § 1.4, Mode, Register, operator, and view |
| **Outpost** | A persistent Away foothold established within a Reach, providing bounded refuge, Rest, storage, and Colony synchronization while remaining categorically distinct from Home. | § 5.7, Outposts and Stopovers |
| **Party** | The fixed group of named Citizens committed to one active expedition, ordinarily between one and one-half and three Body Units and always containing more than one animal. | § 5.1, Party scale |
| **Place** | Designated physical ground within Home that becomes permanent when its first Residence or Practice Project is committed. | § 3.3, Places and Species Placement |
| **Practice** | The functional use established at a Place through which compatible Roles support situated civic purpose, production, transformation, or Projects. | § 3.4, Roles and Practices |
| **Practice improvement** | A specific persistent adaptation that adds a capability, response, range, or resilience to one existing Practice without adding another hosted use. | § 3.3, Place development |
| **Practice Strength** | The situated civic contribution of one completed usable Practice, determined by compatible Role support and Spatial Alignment. | § 3.2, Practice Strength |
| **Presence** | EMBODY's guided-attention form, in which the player remains with what a Citizen experiences through looking, listening, posture, movement, or repose. | § 3.8, Participation and Presence |
| **Pressure** | The amount by which Load exceeds Capacity within one Civic Balance axis. | § 3.2, Shared balance grammar |
| **Project** | Committed deliberate work that makes one defined persistent result true through material, time, Citizens of its owning Role, and ordinarily a supporting Practice. | § 3.4, Project Queue |
| **Project Queue** | The shared execution layer through which Practices accommodate and committed Citizens advance Projects. | § 3.4, Project Queue |
| **Provisioning** | Player-directed recurring transformation governed by a defined Practice-and-Citizen process, available inputs, targets, and protected reserves. | § 3.6, Provisioning |
| **Quiet Equilibrium** | Home's sole tracked condition, active while ordinary obligations are covered and no acute situation demands attention; while active, it opens EMBODY. | § 3.2, Quiet and consequential attention |
| **Reach** | One comprehensible longitudinal segment of the Corridor, containing its portion of Median, Roadways, and Margins. | § 2.2, From Corridor to Reach to Median |
| **Readiness** | The surplus produced when Capacity exceeds Load within one Civic Balance axis. | § 3.2, Shared balance grammar |
| **Record** | The hidden incremental factual database of what has occurred throughout the Colony's life and the authority from which remembered presentations are selected. | § 6.1, The Record |
| **Register** | A structural form of play, engaged through its characteristic Operator and expressed through an appropriate view or interface. | § 1.4, Mode, Register, operator, and view |
| **Rehabilitation** | A Healer Project that establishes adapted participation after Maiming without removing the lasting bodily change or its history. | § 3.4, Rehabilitation; § 5.6 |
| **Residence** | An inhabited use of a Place that accommodates Citizens rather than functioning as a Practice. | § 3.3, Core Residence; § 4.3, Guest Residence |
| **Residence Fit** | The single species-specific placement requirement by which a Guest Residence is judged as a whole. | § 4.3, Guest Residence |
| **Resident Guest** | A Guest Citizen whose species-fixed Role and situated Signature operate at Home and who does not Launch. | § 4.3, Resident Guests |
| **response** | What the Colony or party attempts during a MEET Round before choosing any capability through which to express it. | § 1.5, Responses and expressions |
| **Rest** | A systemic MEET through which an Away party stops, advances time, resets its travel cadence, and receives the recovery permitted by its location. | § 5.2, Rest, Stopover, and safe range; § 5.7 |
| **Return** | The party's ordinary physical TRAVEL homeward through the same continuous world after the player turns back. | § 5.8, Turning Homeward |
| **RISK** | The operator of the Crossing Register: plan, commit, and resolve one complete species-conditioned passage across a Roadway. | § 1.4, The Crossing Register; § 5.3 |
| **Role** | A standing domain of ordinary Colony responsibility sustained by the Civic Shares of available Citizens. | § 3.4, Roles and Practices |
| **Role Balance** | The sustaining Civic Shares assigned to one Role minus that Role's current Load. | § 3.2, Role Balance |
| **Roster** | The complete list of living named Citizens who belong to the Colony, including Citizens who are young, dependent, receiving care, or Away. | § 3.7, Population at Home; § 4.1 |
| **Round** | One complete MEET decision sequence: Frame, Select, Express, Commit, Focus, and Resolve. | § 1.5, Multiple Rounds |
| **Signature** | One bounded species-grounded capability through which a Guest Citizen changes an applicable Away response or situated Home relationship. | § 4.3, Signatures |
| **Spatial Alignment** | The one-unit Practice or Core Residence benefit contributed when a completed usable Place satisfies the Colony's Core-Species placement grammar. | § 3.3, Spatial Alignment |
| **Staging Post** | The immediate Roadway-edge ground from which a party observes, waits, plans, and commits to a Crossing. | § 5.3, The Staging Post |
| **Stopover** | The temporary Away state created when a party completes a Rest MEET at its current location. | § 5.7, Refuge, Stopover, and Outpost |
| **Strained Carry** | Squirrel's optional additional Cargo capacity, whose unsecured burden creates visible Jostle risk after movement. | § 5.2, Squirrel Strained Carry |
| **Supply** | One anonymous prepared and expendable body-scaled intervention assigned to a Launch-eligible Citizen for one expedition. | § 4.6, Supplies |
| **Tale** | A subject-specific player-facing translation of selected Record entries belonging to one Citizen or historically meaningful Item. | § 6.1, Tales and Prior-life Tales |
| **Telegraph** | Observable warning of what may happen while preparation can still alter the stakes. | § 2.5, Events Through Time; § 3.5 |
| **Terms of Hospitality** | The explicit Residence, relational, and safety commitments the Colony must fulfill before a recognized non-Citizen can arrive as a Guest Citizen. | § 4.3, From MEET to arrival |
| **Tharn** | An acute bodily shutdown under overwhelming immediate strain that supersedes the current objective and requires Rest before the expedition can continue. | § 5.6, Tharn |
| **Tool** | A persistent named working object held by one Launch-eligible Citizen that provides one narrow reusable capability Away. | § 4.6, Tools |
| **TRAVEL** | The operator of the Field Register: directly guide an expedition party through the continuous world beyond Home. | § 1.4, The Field Register; § 5.2 |
| **Well Placed** | The positive state of a completed usable Place whose relationship to surrounding Home expresses the applicable Core-Species spatial operator or Guest Residence Fit. The adjectival form is **Well-Placed**. | § 3.3, Species placement |
| **World Pressure** | An externally originating Corridor condition that may add contextual Load, test Readiness, alter ordinary life, or supply a Home situation. | § 3.5, World Pressure |
| **Wound** | A single named recoverable bodily-injury state that constrains only physically affected actions and doubles new Exposure while unstabilized. | § 5.6, Forms of personal consequence |
| **Wound Recovery Project** | A Home Healer Project through which one available Hearth and one committed Healer provide a Wounded Citizen with sustained care. | § 5.6, Wound Recovery Projects |
| **Young Citizen** | A complete Citizen before Maturity who belongs to the Colony, consumes ordinary support, and remains unavailable for Roles, Projects, or Launch. | § 4.5, Young Citizens |

## Appendix B — Names, Place-Names, and Narrative Language

Names express the relationship between particular lives, communities, history,
and inhabited ground. MEDIAN distributes naming authority deliberately: every
Citizen arrives with a Given Name, durable history may grant an After-name, the
world and its inhabitants name particular geography, and the player composes
the one permanent name of the Colony. The same Appendix defines the distinct
human and animal voices through which the Sourcebook and theoretical game
render those lives and places.

### Naming authority

| Subject | Source of its name | Form of player involvement |
|---|---|---|
| **Citizen** | An appropriate cultural Given Name arrives with the individual. | The player learns and uses the name. |
| **Citizen with an After-name** | Durable life history gives rise to rare public recognition. | The player witnesses the history and recognition. |
| **Collective-bodied Citizen** | One household name identifies the complete civic subject. | The player encounters the household by that name. |
| **Ancestral Colony** | Its established cultural name belongs to the world before play begins. | The player learns and remembers the name during the Founding Escape. |
| **Colony** | The founding party names its permanent Home through its first Leader. | The player assembles and confirms one name from curated components. |
| **Reach, Node, or landmark** | Physical character, local use, inhabitants, discovery, or remembered history gives the place its name. | The player learns the name and may cause the history from which a later name arises. |

### The Colony's one player-composed name

The Founding MEET gives the player one direct act of naming. The first Leader
speaks for the founding party while the player assembles the Colony's name from
curated word, sound, and form lists through approved patterns. The ancestral
Colony's established name is shown beside that act as part of what the Founders
carry with them.

- Every available component and completed construction belonging to MEDIAN's
  plain, animal-scale linguistic register
- Shared lists supplying the broad naming language, with Core-Species culture
  influencing sounds, forms, weighting, and suggested combinations
- Ground, hope, and memory functioning as overlapping semantic influences that
  may appear together within one name
- The founding location and ancestral Colony supplying additional relevant
  components
- A continuation pattern able to carry the complete ancestral name forward,
  as **Elderbank** becomes **New Elderbank** in the Rabbit story civilization
- Other approved patterns able to carry one ancestral component into a newly
  assembled name
- Ancestral inheritance remaining one available expression of memory while a
  name may instead arise from the founding ground, forward hope, or several
  influences together
- Only combinations that have been authored or validated as complete names
  appearing in the assembly interface
- The player able to replace components, move among applicable patterns, and
  preview the complete written and spoken name before confirmation
- Confirmation making the name permanent, establishing it throughout the
  interface and presentation, and entering the naming into Campaign Memory
- The Colony name identifying the civic Home while the Home Median retains its
  own geographic name

#### Colony and place-name patterns

Colony and place names assemble from whole words. Four patterns cover the
current story civilizations and establish the general naming grammar.

| Pattern | Construction | Current examples |
|---|---|---|
| **Closed compound** | `[Root][Place form]` | Elderbank; Morningside; Rushbottom; Ashcross; Elmwater |
| **Open compound** | `[Root or modifier] [Place form]` | Chaff End; Pipe End; Nine Beeches |
| **Descriptive phrase** | `The [Modifier] [Place form]` | The Long Verge |
| **Ancestral continuation** | `New [Ancestral name]` | New Elderbank |

- A component able to participate in more than one compatible pattern
- Closed compounds using authored joining, capitalization, plural, and spelling
  forms rather than automatic concatenation
- Open compounds and descriptive phrases retaining approved spacing and any
  article as part of the pattern
- Ancestral continuation preserving the complete established name after
  **New**, while partial inheritance uses one ancestral component through
  another pattern
- The assembly interface exposing only complete names validated for their
  chosen pattern
- Whole-word construction governing Colony and place names, while curated
  sound fragments remain available to Citizen-name authoring

### Given Names

- Every Citizen carrying an appropriate Given Name when first encountered
- Core Citizens drawing from curated cultural banks associated with Mouse,
  Rabbit, or Squirrel, with species sensibility carried through sound,
  material, scale, and place
- Guest Citizens retaining names grounded in their lives and communities when
  they arrive
- Fireflies and Bumblebees using their approved household name as the Given
  Name of one collective-bodied Citizen
- Name changes occurring only through an authored life event and entering the
  Record wherever they become true

#### The shared naming register

Citizen names belong to one broad animal vocabulary before species weighting
shapes them. They favor concrete plants, materials, weather, shapes, sounds,
places, and small objects: things an animal might perceive, carry, shelter
within, move through, or remember. Most are one to three clear syllables, plain
to read aloud, and emotionally open. A Given Name does not predict a Citizen's
Role, personality, fate, or eventual Tale.

Human-made words remain part of this register because human remnants have
become animal-scale geography and material. **Thimble**, **Rivet**, **Pipe**,
and **Lintel** can feel as native to MEDIAN as **Bramble**, **Rowan**, or
**Moss**.

#### Core-Species Given-Name weighting

The three Core Species share the register without sharing identical emphasis.
Weighting determines which names surface more readily; it does not make a word
the exclusive possession of one Species. Names such as **Moss**, **Hazel**, or
**Reed** may suit more than one culture.

- **Rabbit** names favor low plants, forage, ground texture, shade, small
  stones, and protected edges. Their frequent cadence is leafy, soft, and often
  two syllables: **Bramble**, **Fennel**, **Teasel**, **Yarrow**.
- **Squirrel** names favor trees, wind, direction, tension, fastenings, and
  suspended forms. They often join a crisp anchor to a sense of air or motion:
  **Cobb**, **Gale**, **Rivet**, **Rowan**.
- **Mouse** names favor grain, cloth, joinery, stored material, fitted
  interiors, and small handled objects. They tend to be compact and tactile,
  and readily support complementary family names: **Pip**, **Tuck**, **Seam**,
  **Thimble**.

| Core Species | Current Given-Name bank |
|---|---|
| **Rabbit** | Bramble; Briar; Clover; Daisy; Dock; Fennel; Fern; Hazel; Moss; Nutmeg; Pebble; Reed; Sorrel; Teasel; Thistle; Twig; Vetch; Willow; Yarrow |
| **Squirrel** | Alder; Aspen; Beech; Birch; Cobb; Gale; Gable; Hazel; Keel; Knot; Larch; Latch; Rime; Rivet; Rowan; Spindle; Tassel; Vane; Wick; Windle |
| **Mouse** | Barley; Bobbin; Bodkin; Bran; Chaff; Crumb; Flax; Fold; Husk; Lath; Lintel; Muslin; Niche; Nook; Oat; Peg; Pip; Pleat; Purl; Rye; Seam; Sheaf; Spool; Stitch; Thimble; Tow; Tuck; Warp; Weft |

These banks include the names of current story Citizens and adjacent names in
the same register. They establish a productive base rather than a claim that
every campaign must exhaust or repeat the same roster.

#### Complementary names

Related Citizens may carry names that answer one another without collapsing
them into a collective identity: **Weft and Warp**, **Spool and Bobbin**,
**Oat and Rye**, **Pleat and Fold**, **Lintel and Niche**, **Needle and
Thread**, **Peg and Wedge**, or **Stitch and Seam**. This construction remains
available wherever it suits a family, but Mouse culture receives it most
strongly. Mouse multiplicity makes the pattern especially expressive while
every Mouse remains a complete individual Citizen.

Reviewed compound Given Names, such as **Shadepatch**, may appear as complete
curated names. Their internal construction is authored rather than freely
assembled by the player.

#### Guest Given Names

Guest names draw from the same readable register through stronger
species-specific fields of body, voice, habitat, material, movement, and prior
community. Guests arrive already named; their names are encountered rather
than generated by the Colony.

- Bodily or vocal names include **WHOOT**, **Lilt**, and **Velvet**.
- Habitat or rhythm names include **Stillwater**, **Rootwake**, and
  **Morrow**.
- Material or action names include **Latch**, **Slate**, and **Keel**.
- Collective-bodied Citizens may carry household names such as **The
  Lanterns** or **The Goldwings**.

### After-names

- After-name as a rare public recognition of durable life history
- Recognition able to arise from Home or Away through repeated conduct,
  relationship, rescue, failure, adaptation, service, or another defining
  experience
- Most Citizens retaining only their Given Name throughout life
- An earned After-name persisting in interface, dialogue, Tale, and applicable
  Chronicle material
- The recognition functioning through identity, public use, and memory
- Concrete descriptors and actions able to supply After-name language, while
  the Citizen's lived history alone determines which meaning becomes true
- After-name selection arising through the authored event and the Record,
  rather than player construction or random decorative assignment
- **Sharpnose** as the current story example: Shadepatch's changed public name
  follows a defining history rather than predicting it

### Place-names

- A shared curated folk-name grammar producing names that remain homely,
  concrete, and easy to speak
- Physical ground, material, flora, water, enclosure, openness, height, sound,
  weather, animal trace, human infrastructure, use, and history supplying its
  principal vocabulary
- Core-Species culture weighting attention without dividing the world into
  exclusive vocabularies
- Mouse names tending toward edges, interiors, joins, shelter, and enclosing
  material
- Rabbit names tending toward shared ground, breadth, neighborhood, company,
  and protective boundaries
- Squirrel names tending toward height, anchors, lines, crossings, direction,
  and reach
- A place carrying one current geographic name while its tags separately state
  functional information such as Biome, Roadway width, or known condition
- A consequential history able to give a Node or landmark a later remembered
  name grounded in what occurred there

### Animal language and Hyphen-bound forms

A Hyphen-bound form translates one deliberately adopted animal-language word
through several English elements. The first element receives an initial
capital, while the remaining elements follow ordinary prose capitalization.

- **After-name** naming the public identity earned through durable life history
- **Prior-life Tale** naming the translated account of life before the present
  Colony knew a Citizen
- Additional Hyphen-bound forms translating stable animal concepts that
  genuinely require several English elements
- Ordinary English compounds and functional names retaining their ordinary
  prose forms

### Species-influenced animal voice

Animal voice arises through selective attention. The Species share one
persistent world and remain equally capable of memory, planning, civic life,
and individual expression, while their bodies and cultures make different
relationships salient.

- **Rabbit — GATHER:** what gathers life, holds shared ground, carries warning,
  or keeps familiar cover near
- **Mouse — JOIN:** what joins, opens, encloses, fits, or fails at fine scale
- **Squirrel — CONNECT:** what connects points across height, distance,
  movement, and alternate ways home

One tree therefore remains one tree while a Rabbit may first recognize shared
warning ground or a forage boundary, a Mouse a textured wall or protected seam,
and a Squirrel an anchor or branch network. This difference can shape Chronicle
and Tale prose, animal dialogue, scene writing, inspection text, infographics,
and environmental art direction.

Species influence governs attention, metaphor, comparison, and assumed
vocabulary. It creates no accent, rigid sentence pattern, constructed language,
intelligence hierarchy, compulsory collective grammar, or species-exclusive
truth. Individual Citizens retain their own voices inside those cultural
tendencies.

Landscape Voice remains separate. It is the human third-person narrator of
country, weather, movement, and simple events; species bodies may change which
physical details matter to a passage without turning that narrator into an
animal speaker. Chronicle, Tales, dialogue, and scenes are the principal homes
for animal cultural voice.

### Landscape Voice

Landscape Voice is MEDIAN's human third-person narrator. It attends to country,
weather, light, distance, animal-scale movement, and simple events, allowing
the physical world to become briefly literary while remaining continuous with
what the game presents. Landscape or group movement remains its subject rather
than a named protagonist's interior voice.

The completed Appendix will define its cadence, sentence scale, sensory
priorities, treatment of time and direction, relationship to animal bodies,
use of repetition, degree of interpretive warmth, and boundary with mechanical
notification. It will acknowledge the literary influences that make an
attentive human narrator desirable while establishing an original MEDIAN voice
through fresh examples drawn from different Reaches, Day Bands, seasons, and
Registers.

Landscape Voice appears sparingly enough to retain weight. A full-plate Part or
Chapter transition may carry one or two sentences along its lower edge, letting
the image and language complete one observation together. Longer passages
belong at major thresholds such as the Founding arrival or another moment when
movement resolves into newly perceived country.

### Component banks

The final Appendix will supply the curated banks and legal patterns used for
Core-Species Given Names, the Colony name, and folk place-names. Each bank will
state its scope, compatible patterns, and a small set of worked names so the
construction itself guarantees the register.

#### Colony and place-name lexical bank

| Source | Approved components |
|---|---|
| **Plants and ground** | Alder; Ash; Beech; Bramble; Briar; Chaff; Clover; Elder; Elm; Fern; Hazel; Moss; Reed; Root; Rowan; Rush; Sedge; Thistle; Thorn; Willow |
| **Water, weather, and light** | Brook; Creek; Dawn; Dew; Dusk; Mist; Moon; Morning; Pond; Rain; Rill; River; Shade; Spring; Sun; Water; Wind; Winter |
| **Human trace and material** | Brick; Culvert; Glass; Iron; Pipe; Rail; Stone; Tin; Wall; Wire |
| **Qualities and relations** | Close; Deep; Far; First; Good; Gray; High; Long; Low; Near; New; Old; Open; Quiet; Small; Still; Twin; Warm |
| **Place forms** | Bank; Bottom; Bough; Branch; Cross; End; Field; Gap; Grove; Hollow; Ledge; Line; Mouth; Nook; Reach; Rest; Rise; Seam; Side; Span; Verge; Wall; Water; Way |

Compatible plant components may also appear as plural physical features, as
**Beech** becomes **Beeches** in **Nine Beeches**.

#### Core-Species weighting

The lexical bank is shared. Species weighting shapes which components and
combinations appear readily while leaving every compatible construction
available.

| Core Species | Frequently surfaced roots | Frequently surfaced forms |
|---|---|---|
| **Mouse** | Chaff; Moss; Pipe; Rush; Sedge; Tin; Wall; Wire | Bottom; End; Mouth; Nook; Seam; Wall |
| **Rabbit** | Ash; Bramble; Briar; Clover; Elder; Fern; Reed; Willow | Bank; Bottom; Cross; Field; Hollow; Rest; Verge |
| **Squirrel** | Alder; Ash; Beech; Dawn; Elm; Hazel; Morning; Rowan; Wind | Bough; Branch; Line; Side; Span; Water; Way |

- Weighting applying to suggestions and list order rather than component
  ownership
- Compatibility governing the completed construction independently of its
  source lists
- The founding Biome, visible ground, and established ancestral name able to
  raise the weight of components already present in the campaign
- Ground, hope, and memory tags able to raise related suggestions together
  without becoming separate naming modes

## Appendix C — Campaign Memory and Record-to-Presentation

Campaign Memory turns the accumulated truth of a campaign into writing and
imagery the player can encounter, recognize, and remember. The Record remains
the hidden factual authority. Chronicle, Tales, canon images, and situated
scenes are selected translations of that authority rather than parallel
versions of history. The Almanac remains outside Campaign Memory because it
concerns present and possible future conditions.

This Appendix describes the conceptual presentation architecture of the
theoretical game. It establishes what each presentation must preserve and how
the experience behaves when model assistance is absent, late, or invalid; it
does not specify vendors, services, storage, prompt syntax, or production
infrastructure.

### One truth, several presentations

A present situation and a remembered event use related but distinct flows.

> **Live:** current state + applicable history → Moment Brief → narrative and
> visual presentation → player decision → resolved state → Record

> **Historical:** Record → selected Moment Brief → Chronicle, Tale, or visual
> remembrance

An unresolved possibility may be prepared for presentation, but it is not
history. Only the outcome actually experienced and committed enters the
Record. Every later retelling therefore has one factual source even when its
length, voice, image, or point of emphasis changes.

### The Moment Brief

The **Moment Brief** is the smallest sufficient projection of truth for one
presentation. It gives either realization channel the facts needed for that
moment without disclosing the whole Record or inviting the presentation layer
to infer new canon.

A Moment Brief may identify:

- its origin, time, location, Register, and current conditions
- the participating Citizens, other entities, relevant relationships, and
  point of attention
- persistent bodies, appearances, possessions, Places, and visible state
- the limited prior history that makes the moment intelligible
- the selected response, its expressions, and its committed outcome, or the
  still-open branches when several results are being prepared
- details that must appear, details that may vary, and details that are
  prohibited
- the required narrative voice, presentation purpose, eligibility window, and
  delivery deadline

The Brief is a derived working object, not a second Record. If it conflicts
with current state or established history, the Record governs and the Brief is
invalidated or rebuilt.

### Two channels and two realizations

The same Moment Brief can feed two presentation channels. The **Narrative**
channel produces written language. The **Image** channel produces a visual
composition. Each channel has a complete **Baseline** realization and may have
an enriched **model-assisted** realization.

| | Baseline | Model-assisted |
|---|---|---|
| **Narrative** | Authored structures, selected clauses, names, and controlled agreement produce immediate truthful prose. | The bounded Brief is rendered with greater variation and contextual fluency, then validated against its facts and voice. |
| **Image** | Current canon imagery, authored composition, and designed interface framing provide the required visual presentation. | Mandatory canon reference imagery is transformed into a fresh composition, then validated before display. |

These four labels clarify the architecture in this Appendix; they do not need
to become badges throughout the Sourcebook or labels exposed to the player.
Model assistance enriches expression but owns no unique game information. The
Baseline must remain sufficient to understand the situation, make the decision,
and receive its consequence.

### Narrative realization

Baseline narrative is assembled from authored structures appropriate to its
purpose: direct interface language, a Chronicle account, a subject-specific
Tale, animal dialogue, or Landscape Voice. It remains coherent, grammatical,
and repeatable without relying upon generated prose.

A model-assisted narrative receives only the Moment Brief and the applicable
voice constraints. It may choose cadence, emphasis, comparison, and fresh
phrasing, but it may not invent a Citizen, relationship, possession, action,
place, cause, result, or remembered event. Its output is checked against the
Brief before it can become the player's experienced presentation.

Voice follows the subject rather than the production method:

- **Landscape Voice** is the human third-person narrator of country, weather,
  movement, distance, and simple events.
- **Chronicle, Tales, animal dialogue, and animal scenes** may express
  species-influenced attention through GATHER, JOIN, or CONNECT while
  preserving common facts.
- **Interface language** states choices, state, and consequence directly.

### Visual realization

#### Reference-and-amend

The generative image system transforms; it does not author. Every
model-assisted image must use the relevant existing canon Citizen, Colony,
location, and object imagery as image-to-image reference. Text alone cannot
stand in for an established visual subject.

Three authorities govern the result:

1. The Record and current game state govern factual truth.
2. Current canon imagery governs visual identity and continuity.
3. The Moment Brief governs the immediate composition or exact visible change.

The brief distinguishes features to preserve, features to modify, contextual
features that may vary, and incidental material that must not be inherited.
Clothing in a Citizen portrait may establish that Citizen's present clothing;
an incidental figure in a Colony overview does not establish an unnamed
Citizen. A label embedded in a concept reference does not become part of the
world. A visually compelling invention remains invalid if the Record does not
support it.

#### Current canon imagery

Each Citizen has exactly one current canon image. It establishes that
Citizen's recognizable body, markings, current Keepsake, clothing, Maiming,
adaptive devices, and other durable visible distinctions. Earlier versions
remain in secondary history views rather than competing with the current
portrait.

The Colony may require a small current **representation set** rather than one
impossible master image. A principal overview establishes its recognizable
whole; only the additional spatial, material, or inhabited-life views needed
to preserve the Colony clearly join that set. The set is needs-based, not a
mandatory shot list. Superseded views enter the Colony's more readily visible
visual archive.

The first canon image for a new Citizen is established from that Citizen's
authored identity, current facts, and clean references for species anatomy,
scale, and material culture. The first Colony set is established from its Home
territory, current Places, Core-Species spatial grammar, and construction
language. Once accepted, these images become the same-subject anchors for
future work.

#### Canon amendment

A lasting visible change begins with the current canon image, the exact change
already established in the Record, and any other required references. The
result is checked before it becomes the new current image. The prior version
then enters history.

This serial continuity applies to the subject's canon lineage, not to every
image in which the subject appears. When cumulative image drift becomes
visible, the system returns to the cleanest earlier same-subject anchor and
reapplies the complete current state. One Citizen, Colony, or Core-Species
civilization is never derived from another merely as a shortcut.

#### Moment composition

A moment composition uses current canon imagery to place known subjects into a
new dramatic or informational arrangement. It may change camera, pose, light,
expression, weather, and immediate context as the Moment Brief permits. It may
not change identity or persistent state.

This is the generative realization's central experiential use. Current canon
imagery can anchor:

- a dramatic scene shown after a MEET has resolved
- a Register transition or loading image that carries the player between ways
  of seeing the same continuous world
- the backplate of a Citizen information panel or another contextual view of a
  known Citizen
- a Chronicle or Tale illustration selected from recorded history
- a Homecoming, completed Project, Colony Tier ceremony, or other civic
  milestone
- an EMBODY or ordinary-life presentation grounded in the Citizen and Place
  actually present

The resulting scene is a truthful presentation of the moment, not a new canon
portrait. A Citizen's current canon image changes only through a separately
warranted canon amendment. Every new scene returns to the current canon
references rather than using the preceding dramatic scene as its visual source.

If every required subject cannot be referenced or preserved reliably, the
Baseline is used. A whole-Colony moment may be built from the Colony's current
representation set and the specific Citizens who must be recognizable; it does
not require an exhaustive portrait lineup.

#### Visual validation

Before a model-assisted image is shown, it is checked for:

- recognizable Citizen identity and correct animal anatomy
- the required participants and absence of invented participants
- current clothing, Keepsakes, Tools, Supplies, Wounds, Maiming, and adaptive
  devices where visible
- the correct Place, geography, Colony structure, scale, season, time, weather,
  and resolved consequence
- composition consistent with the Moment Brief
- absence of inherited labels, invented objects, false relationships, and
  unsupported structural change
- absence of generated text carrying semantic or instructional meaning

A failed candidate leaves both the Record and canon imagery unchanged.

### Predictive preparation and delivery

When a MEET or another bounded situation presents several choices, the game may
prepare likely narrative or visual realizations while the player deliberates.
Each candidate remains attached to its branch. Unchosen branches are discarded
and never enter Campaign Memory.

A Register transition or loading interval is a natural opportunity to finish
an applicable image, but the player is never made to wait for optional model
assistance. Every presentation has a deadline. If the enriched realization is
absent or invalid at that deadline, the game delivers the Baseline cleanly.

A late model-assisted result does not silently replace what the player already
experienced. When valid, it may later appear as a Chronicle or Tale
interpretation of the recorded event. The Record retains which realization was
actually shown so future references do not pretend the player saw something
else.

### Selection, duration, and memory

Not every presentation becomes a durable remembrance. The back end selects and
sorts material according to established significance without asking the player
to curate the Record directly.

- A moment may remain an immediate scene and leave only its factual outcome in
  the Record.
- A Citizen- or Item-specific consequence may later appear through a Tale.
- A Colony-significant event may receive Chronicle treatment.
- A lasting visible change may amend a Citizen image or the Colony's current
  representation set and preserve the superseded image in history.

These outcomes can overlap because they answer different questions. Chronicle
and Tale translate what an event meant; canon imagery preserves and reuses what
the world and its inhabitants have visibly become.

### Sourcebook demonstration

The completed Appendix should make the architecture legible through one compact
authority diagram, one readable Moment Brief, and one event shown through its
Baseline and model-assisted Narrative and Image realizations. A smaller inset
can show predictive branch preparation, deadline fallback, and later Chronicle
reuse. Exact page composition belongs to the Augments phase.

## Appendix D — Home Systems Reference

This Appendix gathers the principal Home relationships for quick reference.
Part III remains the full account of how DWELL and EMBODY feel and why their
systems exist; this treatment keeps the values, formulas, dependencies, and
exceptions near one another.

### Home system contour

> Citizens supply Civic Shares → Civic Shares sustain Roles or advance
> Projects → Places hold Residences and Practices → Residences answer Housing
> Load → Practices strengthen situated civic response, enable defined
> production, and accommodate Projects → DAWN resolves the day's accumulated
> change

Pressure develops where current Capacity does not cover current Load. Quiet
Equilibrium becomes active when ordinary obligations are covered and no acute
situation demands attention. It opens EMBODY and permits certain ceremonial or
reflective moments without becoming a spendable resource.

### Places, uses, and establishment

A Builder designates physical ground as a Place at no cost. The designation is
freely withdrawable until its first Residence or Practice Project is committed;
that commitment makes the Place permanent. Completion makes the new use usable.

| Place state | Civic effect |
|---|---|
| **Vacant designation** | Reserves no material and supplies no Capacity, Practice Strength, production, or Project capacity. |
| **Committed establishment** | Permanently establishes the Place, occupies its supporting Practice, and advances through committed Builder Civic Share-Days. |
| **Unfinished use** | Supplies no Housing Capacity, Practice Strength, passive output, or transformation. |
| **Completed usable Residence** | Supplies Core Housing Capacity or satisfies the applicable Guest Residence Fit. |
| **Completed usable Practice** | Supplies situated Practice Strength, participates in any defined production process, and accommodates one active Project. |
| **Damaged or unusable use** | Retains its Place and history while its unavailable functions cease until restored. |

One established Place ordinarily holds one Core Residence, one Guest Residence,
or one Practice. A Guest may depart from that rule only through an explicit
species exception. Practice Places take the names of their Practices rather
than acquiring separate building-type names.

Every new Residence or Practice is established through a Builder Project. The
first Workshop is the sole Practice-establishment bootstrap exemption: its
founding Project still consumes material, time, and committed Builder effort,
but begins before a supporting Workshop exists. A Place may later change use or
stand vacant while remaining established ground.

### Spatial Alignment and Residence Capacity

Each completed usable Core Residence or Practice is either Well Placed or Not
Well Placed according to the Colony's spatial operator: Mouse **JOIN**, Rabbit
**GATHER**, or Squirrel **CONNECT**. Layout changes can improve or degrade that
status. The interface previews a committed Project's expected alignment and
capacity effects.

| Core Residence | Not Well Placed | Well Placed |
|---|---:|---:|
| **Housing Capacity** | 2 Body Units | 3 Body Units |
| **Rabbit or Squirrel Citizens accommodated** | 2 | 3 |
| **Mouse Citizens accommodated** | 4 | 6 |

Insufficient Housing Capacity creates Housing Pressure while every accepted
Citizen remains housed in the civic and narrative sense; capacity loss never
evicts a Citizen. Guest Residences remain outside pooled Core Housing Capacity
and use the Residence Fit defined for their species.

A Well-Placed Practice contributes one Spatial Alignment point to Practice
Strength. Where that Practice has defined passive production or transformation,
it also contributes one-half yield chunk to that process.

### Civic Balance

Every Housing or Role axis resolves independently:

**Balance = Capacity − Load**

**Readiness = max(Balance, 0)**

**Pressure = max(−Balance, 0)**

Positive Balance is Readiness, zero Balance is Covered, and negative Balance is
Pressure equal to the uncovered Load. An axis with neither Load nor Capacity is
N/A. Surplus in one axis never conceals a shortfall in another.

| Citizen body | Civic Share while present, adult, and available | Body Unit |
|---|---:|---:|
| **Rabbit** | 1 | 1 |
| **Squirrel** | 1 | 1 |
| **Mouse** | 0.5 | 0.5 |
| **Ordinary v0.5 Guest** | 1 | 1 |

**Role Balance = sustaining Civic Shares − Role Load**

**Housing Balance = usable Core Residence Capacity − Core Citizen Housing Load**

Each available Citizen directs their Civic Share either to one ordinary Role
or to an active Project. A Citizen who is Away, unavailable, assigned elsewhere,
or committed to a Project supplies no current share to that Role. Body Unit
normalizes aggregate contribution and obligation without changing citizenship,
authority, aptitude, or personal worth.

Current Housing and Role Pressures form the **Civic Pressure profile**. Hidden
Colony Pressure weighs that profile with World Pressure, present circumstances,
depth and persistence, bounded randomness, and recent Home MEET history. The
greatest relevant Role shortfall normally supplies a situation's primary civic
stake; another actual shortfall or situated fact supplies its collateral stake.
Pressure creates vulnerability and MEET context rather than automatic daily
damage.

### Practice Strength

Practice Strength expresses the situated civic value of one completed usable
Practice when a situation meaningfully involves it.

| Compatible ordinary Role support | Not Well Placed | Well Placed |
|---|---:|---:|
| **Less than 1 sustaining Civic Share** | 0.5 | 1.5 |
| **At least 1 sustaining Civic Share** | 1 | 2 |

Compatible Civic Shares aggregate automatically across Citizens and Roles; the
player creates no link between a Citizen and an individual Practice. One Mouse
can satisfy a defined process's requirement for an actual sustaining Citizen,
while full Practice support still requires one aggregate compatible Civic
Share. A shared Practice carries one Practice Strength for the situation rather
than multiplying its value by the number of Roles that use it.

### Roles and Practices

| Role | Ordinary responsibility | Practice or Practices | Defined output or passive civic expression | Characteristic deliberate work |
|---|---|---|---|---|
| **Builder** | Physical soundness and deliberate transformation of Home | Workshop | Beautification | Establish Residences and Practices; construct or restore Outposts; complete major structural changes |
| **Gardener** | Cultivation, seasonal yield, and cultivated continuity | Garden | Perishable Sustenance | Restore or adapt cultivated ground; establish Winter Cultivation |
| **Crafter** | Functional material and Away capability | Workshop | Binding, Device, and Offering Supply preparation | Create Tools, Specialist Tools, and lasting fabrication capabilities |
| **Caretaker** | Provisioning, nurture, dependency, and ordinary care | Hearth; Kitchen | Perishable-to-Durable preservation through Kitchen | Adapt nurture or provisioning to a persistent need |
| **Healer** | Injury, illness, recovery, and bodily adaptation | Hearth | Remedy preparation | Conduct Wound Recovery and Rehabilitation Projects |
| **Teacher** | Teaching, integration, cultural continuity, and social memory | Gathering Place; Hearth | Beautification | Establish a memorial, observance, or lasting cultural understanding |
| **Watchkeeper** | Timely warning and useful Telegraph | Watchpost | Beautification | Extend or restore warning and signaling capability |
| **Leader** | Coordination, deliberation, shared commitment, and ceremony | Gathering Place | Beautification | Establish persistent civic agreements or coordinating functions |

Workshop, Hearth, and Gathering Place are shared Practices. Compatible Roles
draw upon the Practice as circumstances require, but the Practice retains one
situated strength and one Project slot. Hearth is the civic Practice of healing,
nurturing, dependency, and recovery; **family** remains a domestic relationship.
Leader contributes no Hearth support.

Builder, Teacher, Watchkeeper, and Leader Civic Shares sustained in ordinary
work each add one point to the Colony-wide Beautification track at DAWN. A
threshold produces one small persistent, mechanically inert Frill. Well-Placed
Practices and Project-committed Citizens add no Beautification progress.

### Defined Practice improvements

Each current Practice has at least one specific improvement. An improvement
makes a bounded persistent capability true at one existing Practice through a
Project owned by the Role that benefits from the result. It adds no generic
level, Practice Strength, or Project slot.

| Practice | Improvement | Owning Role | Effect |
|---|---|---|---|
| **Workshop** | **Fine Work** | Crafter | Opens individually defined Specialist Tool recipes. |
| **Garden** | **Winter Cultivation** | Gardener | Makes that Garden eligible for winter yield at one-quarter of its normal production. |
| **Kitchen** | **Open Table** | Caretaker | Opens the whole-Colony Shared Meal EMBODY opportunity. |
| **Hearth** | **Rehabilitation** | Healer | Allows individualized Rehabilitation Projects after Maiming. |
| **Watchpost** | **Far Warning** | Watchkeeper | Qualitatively identifies an eligible approaching pressure family early enough to provide another preparation window. |
| **Gathering Place** | **Community Board** | Leader | Gives selected Almanac information already known to the Colony a persistent shared expression in DWELL. |

The physical Community Board may stand elsewhere within Home while remaining
the improvement of its Gathering Place. Winter Cultivation, Open Table, Far
Warning, and Community Board modify only their stated capability. Wound Recovery
uses an available Hearth and requires no Rehabilitation improvement.

### Passive production and transformation

A process produces zero unless it has at least one completed usable relevant
Practice and at least one Citizen sustaining its defined Role. Once that gate
is satisfied:

**Passive Throughput = usable relevant Practices + sustaining Civic Shares +
(0.5 × Well-Placed relevant Practices)**

| Process | Required Practice | Sustaining Role | Result |
|---|---|---|---|
| **Cultivation** | Garden | Gardener | Perishable Sustenance during eligible seasons |
| **Preservation** | Kitchen | Caretaker | Perishable Sustenance transformed into Durable Sustenance |
| **Supply Preparation** | Workshop | Crafter | Binding, Device, and Offering Supplies from defined inputs |
| **Remedy Preparation** | Hearth | Healer | Remedy Supplies from defined inputs |

Each usable Practice and each sustaining Civic Share adds one yield chunk; each
Well-Placed Practice adds one-half. Project-committed Citizens contribute
nothing to throughput. Inputs, recipes, seasons, targets, protected reserves,
and situated modifiers apply after ordinary throughput is calculated and can
bound the result. The formula creates no output for a Practice without a defined
process.

Each process carries its own fractional remainder. DAWN releases whole chunks
and retains the fraction: throughput of 1.5 releases one chunk, then two, then
one across successive eligible DAWNs.

Provisioning places an eligible transformation in **Prepare**, **Hold**, or
**Unavailable** state. Player targets prevent automatic overproduction, while
protected reserves prevent committed inputs from being consumed by unrelated
Provisioning or Projects.

### Project Queue

Every Project makes one defined persistent result true. Its queue entry records
the result, owning Role, supporting Practice, target, required material,
required Civic Share-Days, and named committed Citizens.

- Each completed usable Practice accommodates one active Project.
- The supporting Practice and Project target may be different Places.
- The owning Role follows the result: Builder establishes a Practice, Residence,
  or Outpost; Crafter creates a Tool; Gardener converts a Garden for Winter
  Cultivation; Healer conducts Wound Recovery.
- The player may reserve material before commitment and release an uncommitted
  reservation.
- Commitment occupies the supporting Practice and withdraws the named Citizens'
  shares from Role coverage, Practice support, passive throughput, and
  Beautification as applicable.
- Each Citizen adds Civic Share-Days equal to their Civic Share as the relevant
  days pass. Fractional contribution accumulates unseen until DAWN records
  whole progress.
- A committed Project cannot be interrupted or cancelled.
- Completion creates the result, releases the Practice, and returns the Citizens
  to ordinary availability.
- The supporting Practice retains its situated Practice Strength while occupied,
  recalculated from ordinary compatible support that remains.

The founding Workshop Project alone begins without a supporting Practice. A
Wound Recovery Project alone requires exactly one committed Healer and advances
one Healer-Day per elapsed day regardless of Body Unit; additional Healers do
not accelerate biological recovery.

### Population and growth

| Population view | Includes |
|---|---|
| **Colony Roster** | Every living named Citizen belonging to the Colony, including young Citizens, Patients, Guests, and Citizens Away |
| **Citizens at Home** | Roster Citizens physically present at the Home Median |
| **Available Civic Population** | Home-present adults currently able to sustain Roles or commit to Projects |
| **Dependents and Patients** | Present Citizens requiring support without a current ordinary Civic Share |

Growth occurs through three distinct relationships:

| Path | Opening | Commitment | Result |
|---|---|---|---|
| **Wanderer** | Refuge, rescue, or integration MEET | Permanent welcome or bounded temporary refuge under the Colony's actual conditions | A named Core adult joins the Roster with a Prior-life Tale and their Body-Unit Civic Share when available. |
| **Nesting** | A rare green-season proposal from particular mature Core Citizens while Quiet Equilibrium creates civic room | Protected Sustenance and visible future accommodation, care, teaching, protection, and Role support | A very small number of named young Citizens enter the Roster and create support needs before contributing Civic Shares at Maturity. |
| **Guest residency** | Relationship and Terms of Hospitality | The promised Residence Fit, access, support, and other agreed conditions become true | A named Guest or explicitly collective-bodied household joins the Roster under its species profile. |

Every arrival adds a named life, history, Sustenance demand, and actual civic
obligations. Core Citizens also add Body-Unit-scaled Housing Load; Guest
Citizens require their species' Residence Fit.

Housing, Sustenance, routes, care, protection, and Role support constrain
responsible growth without forming one abstract population cap. Emergency
hospitality may exceed Housing Capacity and make the resulting Pressure visible.
The player sees the expected change to Housing, Sustenance, Role Load, care, and
available Civic Shares before authorizing planned growth.

### Colony Tier recognition

Tier number is the common mechanical vocabulary; each Core Species expresses
that recognized scale through its own civic name.

| Tier | Required living Body Units | Mouse | Rabbit | Squirrel |
|---|---:|---|---|---|
| **I** | Founding | **First Rooms** | **Close Commons** | **First Anchors** |
| **II** | 7 | **Joined House** | **Open Commons** | **Linked Ways** |
| **III** | 12 | **Manor House** | **Court** | **Living Web** |
| **IV** | 18 | **Grand Manor** | **Grand Court** | **Grand Web** |

Population is the sole Tier gate. Every living Citizen on the Roster contributes
their ordinary Body Unit regardless of age, health, or current location. Once
eligible, recognition additionally requires Quiet Equilibrium, an available
Home-present Citizen actively sustaining Leader, and the Tier's escalating
Civic Dedication outside protected reserves.

The player may defer recognition indefinitely. Committing the Dedication
consumes its resources, advances one Day Band, and opens the Recognition MEET.
The active Leader conducts the ceremony, with Gathering Place hosting when one
is available. Recognition proceeds one Tier at a time and remains part of
Colony history through later contraction, Pressure, or damage. Exact Civic
Dedication ingredients and quantities belong to the dedicated Items and
Resources tuning phase. The Dedication occupies no Project Queue slot; its
material becomes part of the Colony's built fabric, with equal mechanical cost
and species-specific physical expression.

### DAWN reference order

DAWN closes the elapsed day and establishes the new one:

1. Consume Sustenance, normally Perishable before Durable.
2. Resolve active preservation and Supply preparation from eligible stock.
3. Apply aggregate Perishable Sustenance spoilage.
4. Add new passive production, releasing whole chunks and carrying fractions.
5. Add Beautification progress and create any earned Frill.
6. Add Project progress, complete eligible Projects, and release their Practices
   and Citizens.
7. Resolve recovery and other changes in Citizen location or availability.
8. Recalculate usable Places, Spatial Alignment, Housing and Role Balance, and
   Colony Pressure.
9. Report meaningful stock, Project, availability, and civic changes.

A Residence or Practice completed at this DAWN becomes usable during the new
day and first contributes passive output at the following DAWN. A Citizen whose
recovery completes becomes available during the new day.

## Appendix E — Resources, Items, Carry, and Body Units

MEDIAN distinguishes Colony-scale stocks, party Cargo, and personally tracked
Items. Body Units allow bodies of different sizes to enter shared civic and
expedition math while every Tool, Keepsake, Wound, relationship, memory, and
death remains attached to a particular Citizen.

### Four material layers

| Layer | Unit and ownership | Examples | Where it persists |
|---|---|---|---|
| **Colony stock** | Fungible Colony-scale quantity | Sustenance, Scrap, prepared Supplies | Home's shared stores; synchronized Outpost transfers enter the same stock |
| **Cargo** | Fungible units held within one party-wide Carry capacity | Sustenance or Scrap recovered Away | The expedition until offloaded at an Outpost or reconciled at Homecoming |
| **Personal Item** | One physically credible object attached to a Citizen or assigned expedition position | Tool, Supply, Keepsake | Its owning or carrying rules rather than Cargo slots |
| **Singular tracked Item** | Authored, individually persistent object | Special Artifact or another meaning-bearing object | Its current holder, location, state, and possible Item Tale |

Colony stocks and Cargo do not retain makers or individual unit histories.
Personally or historically meaningful objects remain tracked. A fungible
resource can become a defined Item through an authored transformation; an Item
never dissolves into anonymous stock merely because it reaches Home.

### Body Units

**Body Unit** is the normalization layer for aggregate mechanics. **Citizen**
remains the unit of life.

| Citizen body | Body Units | Civic Share | Ordinary secured Carry contribution |
|---|---:|---:|---:|
| **Rabbit** | 1 | 1 | 10 |
| **Squirrel** | 1 | 1 | 10, plus optional Strained Carry |
| **Mouse** | 0.5 | 0.5 | 6 per individual Mouse; 12 per Body Unit |
| **v0.5 Guest** | 1 | 1 | Species-fixed value |

Fireflies and Bumblebees each form one collective-bodied Citizen household and
one Body Unit despite visible multiplicity. A later species may count as more
than one Body Unit only through an explicit species rule; no current v0.5
Citizen does.

Body Units govern:

- Housing Load and Core Residence Capacity
- Sustenance demand
- Civic Shares, Role Balance, ordinary Civic Share-Day Project progress, and
  Beautification contribution
- party composition and bodily hazard normalization
- baseline Carry, subject to the explicit Mouse and Guest values

Citizen identity governs:

- name, relationships, family, personal history, and Campaign Memory
- individual Tool, Supply, and Keepsake positions
- Role identity and Guest Signature
- Wound, Maiming, Tharn, Exposure, recovery, and death
- Focus and personal consequence during MEET

Two Mice therefore equal one Rabbit in aggregate civic scale while remaining
two complete lives with two sets of relationships and personal Item positions.
Mouse's greater headcount within the same Body Unit allowance is a deliberate
advantage in possible Item carriage and a deliberate multiplication of
particular lives placed at risk.

### Party normalization

An ordinary expedition contains at least one and one-half and no more than
three Body Units, and always contains more than one actual animal.

| Example | Body Units | Legal ordinary party? |
|---|---:|---|
| Three Mice | 1.5 | Yes; the smallest all-Mouse party |
| One Mouse and one full-Body-Unit Citizen | 1.5 | Yes |
| Three Rabbits, Squirrels, Expedition Guests, or any full-unit mixture | 3 | Yes; the ordinary maximum |
| Six Mice | 3 | Yes; six particular Citizens within the same maximum |

Each departing Citizen withdraws the Civic Share supplied by their Body Unit
from Home. Party membership remains fixed until Homecoming. No ordinary Tool,
Practice, Colony Tier, or Outpost improvement raises the three-Body-Unit limit.

### Resource and production categories

| Resource | Principal function | Ordinary source or transformation |
|---|---|---|
| **Perishable Sustenance** | Immediate and green-season food; vulnerable to aggregate spoilage | Garden and Gardener production; eligible Field recovery |
| **Durable Sustenance** | Preserved food for winter, disruption, and protected reserves | Kitchen and Caretaker preservation of Perishable Sustenance |
| **Flexible Scrap** | Binding, wrapping, weaving, lashing, sealing, and suitable construction | Field recovery and authored exchange or consequence |
| **Rigid Scrap** | Bracing, shielding, surfacing, reinforcement, and suitable construction | Field recovery and authored exchange or consequence |
| **Supplies** | Prepared expendable interventions for Away or situated need | Crafter or Healer Provisioning from defined inputs |
| **Tools** | Durable personal working capability Away | Crafter Projects at a usable Workshop |

Perishable Sustenance is normally consumed before Durable Sustenance. Scrap
does not divide into component inventories. Production, Provisioning, and
Projects draw only their defined inputs, and protected reserves remain outside
unrelated automatic use.

Perishable Sustenance, Durable Sustenance, and Scrap remain fungible stocks.
Prepared Supplies remain stock until Launch assigns one to a Citizen's
expedition position. A completed Tool enters personal Item tracking when its
Crafter Project creates it. Supply and Tool therefore belong to the material
economy without remaining anonymous Colony stock throughout their use.

Ordinary food is abstracted during Away. Away Citizens continue to count toward
the Colony's Body-Unit-scaled Sustenance demand. Food recovered in the Field is
Cargo for Home rather than a ration position, hunger meter, or separate
expedition resource.

### Resource flow

> Field recovery or exchange → party Cargo → Outpost Colony sync or Homecoming
> → Colony stock → consumption, Provisioning, reservation, or Project
> commitment

The party never sends ordinary Cargo directly to Home from arbitrary Field
ground. A completed Outpost can transfer offloaded fungible Cargo into the one
Colony stock through Colony sync, immediately freeing Carry. Homecoming
automatically transfers remaining Cargo into that same stock.

Reserved Project material remains part of Colony stock but unavailable to
unrelated use. Commitment protects and consumes it according to the Project.
Provisioning uses player-set targets and reserves so recurring transformation
does not exhaust material intended for ordinary life or deliberate work.

### Personal Item positions

| Position | Eligible Citizens | Persistence | Capacity |
|---|---|---|---:|
| **Keepsake** | Every Citizen | Personally persistent | 0 or 1 |
| **Tool** | Launch-eligible Citizens | Persistent and freely reassigned at Home | 0 or 1 |
| **Supply** | Launch-eligible Citizens | Assigned for one expedition and consumed when committed | 0 or 1 |

Young Citizens and Resident Guests retain complete identity and may hold a
Keepsake without displaying unused Away-equipment positions. Core Citizens and
Expedition Guests use the same applicable positions. Body compatibility changes
the item's credible physical form rather than creating proficiency ratings.

Tools, Supplies, and Keepsakes occupy their own positions and consume no Cargo
slots. Artifacts and other singular meaning-bearing objects require secured
carriage when they travel but retain their own identity rather than becoming
fungible Cargo.

### Tools

A Tool is one persistent, named, body-scaled working object held by a
Launch-eligible Citizen. The five ordinary classes are **Carry**, **Reach**,
**Cut**, **Brace**, and **Render**.

- Any Launch-eligible Citizen may hold any Tool whose form is credible for that
  body.
- Role, Species, personality, and prior service create no proficiency gate or
  effect coefficient.
- A Tool supplies one narrow, reusable contextual capability rather than a
  general bonus.
- Relevant Tools appear after the player chooses a MEET response; the player
  may select one personal-Item expression for the Round.
- A selected Tool supplies its full effect, places its holder in Focus, and
  enters the Round's situated hazard.
- Multiple Tools of one class provide redundancy and possible protagonists
  rather than stacking upon one Round.
- A Carry Tool provides its standing Cargo effect and enters hazard when the
  capacity or carried load is materially at stake.
- A Damaged Tool remains with its Citizen but is unavailable for the remainder
  of the expedition. Ordinary repair after Homecoming belongs to Crafter
  responsibility; a new persistent capability requires a Project.
- Fine Work opens specifically authored Specialist Tools rather than numerical
  levels for ordinary Tools.

Routine use and reassignment create no history by themselves. Consequential
creation, recovery, use, adaptation, damage, repair, loss, or destruction may
enter the Tool's record.

### Supplies

A Supply is one anonymous, unitary, body-scaled object prepared for a single
intervention and assigned to one Launch-eligible Citizen for one expedition.
It is something an animal can physically carry and deploy, rather than a kit,
bundle, or abstract charge.

The present Supply-class names remain provisional until the dedicated Items and
Resources tuning phase.

| Supply | Physical form | Direction | Prepared by |
|---|---|---|---|
| **Binding** | One cord, strip, wrap, or fastening | Connect or secure | Crafter |
| **Device** | One small contrivance | Produce one temporary physical or sensory effect | Crafter |
| **Offering** | One morsel or meaningful token | Place something into an encounter with another being | Crafter |
| **Remedy** | One dose, dressing, or poultice | Treat or protect a body | Healer |

- Binding may create one temporary tie, tether, wrap, patch, restraint, or
  fastening.
- Device may wedge, mark, signal, trigger, screen, or probe through one compact
  deployed object.
- Offering may be given, shared, exchanged, placed, promised, or used as bait;
  it never compels acceptance or the intended response.
- Remedy may clean, soothe, stabilize, or protect. It can stabilize a Wound
  through Homecoming, lessen one defined immediate physical effect, contain the
  acute Wound accompanying Maiming, or express PARLEY through applicable care.
  It does not relieve Tharn.

The authored MEET states a Supply's exact applicable effect. Committing it
provides that effect and consumes the Supply regardless of the overall outcome.
It may soften consequence, preserve a stake, extend an achieved result, or
enable a credible alternative without replacing the Round or guaranteeing
success.

Supplies carry no personal name, maker, quality tier, provenance, or Tale.
Unspent Supplies return to the prepared Colony pool at Homecoming and all
expedition Supply positions clear. A Supply discarded during TRAVEL leaves
play.

### Keepsakes and singular Items

A Keepsake is a persistent emotional object rooted in one Citizen's life. Its
position may remain empty without making that life incomplete.

- One narrow personal circumstance can make the Keepsake relevant during an
  eligible Home or Away MEET.
- A selected Keepsake becomes the Round's one personal-Item expression and
  places its holder in Focus.
- Its meaning may soften a personal consequence, preserve a meaningful stake,
  or permit a response within the chosen Approach.
- A Keepsake is present rather than spent, charged, refreshed, or cooled down.
- Damage, gifting, loss, sacrifice, surrender, succession, replacement, and
  memorial display require an explicit consequential event.

A Special Artifact or another singular tracked Item can retain a holder,
location, visible state, history, and Item Tale without becoming a standard
loadout position. Meaning-bearing Items return, transfer, or receive memorial
disposition through the event and relationships involved; death never turns a
Citizen's possessions into anonymous loot.

### Items within MEET

MEET preserves collective decision while allowing one object and one Citizen to
become particular.

1. The player chooses a valid response.
2. Relevant Tools, Supplies, Keepsakes, relationships, and authored
   circumstances appear.
3. The player chooses no personal-Item expression or one Tool, Supply, or
   Keepsake expression.
4. The chosen expression establishes its effect, bearer, Focus, and applicable
   stake.

A Guest Signature is a bodily capability rather than an Item and may coexist
with the active Item when its circumstances apply. No Item provides an
unspecified bonus, extra Round, success guarantee, or immunity from consequence.

### Secured Carry

Carry is one visible party-wide capacity for fungible Cargo. Personal Item
positions remain separate.

**Secured Carry = (10 × Rabbit Body Units) + (10 × Squirrel Body Units) +
(6 × individual Mice) + Expedition Guest Carry + applicable Carry Tool effects**

| Expedition Guest | Secured Carry |
|---|---:|
| **Raccoon** | 12 |
| **Crow** | 9 |
| **Gull** | 9 |
| **Fox** | 12 |
| **Weasel** | 10 |
| **Hedgehog** | 8 |
| **Snake** | 6 |
| **Mink** | 10 |

Current and maximum Carry remain visible. Added Cargo contracts projected
TRAVEL reach and can become a situated RISK or MEET stake. The Field expresses
that burden through reduced reachable ground rather than another Load score.
Whenever capacity or consequence requires it, the player chooses what to take,
leave, protect, offload, or abandon.

### Squirrel Strained Carry

Each Squirrel Body Unit supplies ten optional Strained Carry slots beyond
secured Carry. This is one shared capacity representing precarious mouth,
cheek, and exterior carriage.

**Maximum Strained Carry = 10 × Squirrel Body Units**

Only fungible Cargo may enter it. Artifacts, Keepsakes, and other singular
objects require secured carriage. Strained Cargo contracts projected reach and
enters situated danger like the rest of the haul.

After a Day Band in which the party materially moved while carrying Strained
Cargo, each Squirrel makes one visible Jostle check:

**Jostle chance = 10% × (current Strained Cargo ÷ maximum Strained Carry)**

A successful check immediately loses one randomly selected Strained Cargo unit.
The fill proportion recalculates after each loss. No check occurs while the
capacity is empty or the party did not travel. When RISK or MEET already
resolves danger to Strained Cargo for that Band, its consequence replaces the
ordinary Jostle checks.

### Homecoming and persistence

Homecoming reconciles layers according to what they are:

- remaining Cargo enters Colony stock and clears from Carry
- unspent Supplies return to the prepared pool and their positions clear
- spent or discarded Supplies remain gone
- Tools, Keepsakes, Artifacts, and other tracked Items retain their holders,
  states, and histories
- damaged Tools enter ordinary Crafter repair
- a deceased Citizen's meaning-bearing possessions receive their disposition
  through relationship, succession, or memorial context

An Outpost Colony sync transfers fungible Cargo only. Personal and singular
Items remain with their holders until Homecoming or another explicit event
changes them.

### Current tuning boundary

The architecture above is current m050 design. A dedicated conceptual tuning
phase will set Node yields, recurring costs, Carry burden, major recipes,
Sustenance demand and spoilage, Supply and Tool costs, Outpost and Place costs,
Project material requirements, Civic Dedications, and the final Supply-class
names as one connected economy. Tuning may change quantities and provisional
labels while preserving the distinctions among stock, Cargo, personal Items,
Body Units, and particular Citizen consequence.

## Appendix F — The Highway and Living World Reference

This Appendix gathers the persistent physical and environmental world in which
Home and Away occur. It treats The Highway as one living system: Corridor
geometry, Biomes, Sound Walls, traffic, human activity, weather, Nodes, and the
World Pressure they create. Appendix G separately gathers the actions Citizens
take within that world.

### Corridor geometry

The Highway is one persistent world organized longitudinally as the Corridor.
Its cross-section is:

> **Sound Wall ‖ Margin | Main Roadway | Median | Main Roadway | Margin ‖
> Sound Wall**

| Term | Reference meaning |
|---|---|
| **Corridor** | The continuous longitudinal organization of The Highway, extending beyond the presently known Reaches |
| **Reach** | One comprehensible segment containing its portion of Median, both Main Roadways, and both Margins |
| **Median** | The central habitat band continuing through successive Reaches |
| **Main Roadway** | One of the two broad lateral traffic bands separating Median from Margin |
| **Margin** | The inhabited band between a Main Roadway and its hard Sound Wall boundary |
| **Sound Wall** | The lateral limit of playable ground |
| **Home Median** | The particular geographic median occupied by the Colony; the Colony retains its own proper name |

Upcorridor and downcorridor movement proceeds longitudinally through the
Median. A smaller road may cross the Median at a Reach border. Transverse
movement between Median and Margin crosses a Main Roadway. Both road scales use
RISK, with width, traffic, visibility, surface, weather, River Spume, and
far-side refuge determining the particular Crossing.

### The world in cross-section

The simple cross-section names the major bands; play occurs within their
animal-scale detail. From the Corridor's center toward either outer boundary,
the ground ordinarily reads as:

| Cross-sectional position | Physical character and use |
|---|---|
| **Median interior** | Soil, vegetation, water, drainage, shelter, paths, Nodes, and the possibility of permanent Home |
| **Median Roadway edge** | Verge, shoulder, drainage, exposed sightline, deposited material, and possible Staging Post ground |
| **Main Roadway** | Moving traffic surface and the full Crossing threshold |
| **Roadway-side Margin** | Strong River Spume, volatile material opportunity, disturbance, and exposed Nodes |
| **Middle Margin** | Mixed vegetation, infrastructure, runoff, shelter, animal activity, and scattered material |
| **Sound-Wall-side Margin** | Greater shelter, trapped moisture and debris, denser vegetation, and living-resource Nodes |
| **Sound Wall** | Hard lateral boundary whose base, shade, runoff, sound, and accumulated material remain part of the playable Margin |

The same sequence mirrors on the other side of the Median. Actual Reaches bend,
narrow, widen, flood, harden, or interrupt these tendencies without losing the
underlying relationship. A smaller Reach-border road creates a compressed
version of Roadway edge, moving surface, and far-side refuge within
longitudinal travel.

### Sound Walls

Sound Walls terminate the Margins and make the Corridor's human construction
continuously legible. The ground at their base remains playable; the wall
itself is a hard boundary rather than another territory beyond The Highway.

- Wall material, height, joints, damage, drainage, and orientation shaping
  shade, warmth, wind, echo, vibration, runoff, and animal-scale enclosure
- Seeds, leaves, litter, water, and blown material accumulating at the base and
  supporting sheltered Nodes or passages where the actual place permits them
- Sound-Wall-side vegetation tending toward greater stability than Roadway-edge
  growth while remaining subject to mowing, maintenance, flooding, heat, and
  contamination
- The wall giving reliable lateral orientation even when dense vegetation or
  complex infrastructure obscures the larger Corridor
- Openings, culverts, breaks, and service structures functioning only according
  to their actual geometry, without turning the far side of the wall into a
  playable expansion zone
- Human work upon or beside a Sound Wall entering the same traffic-as-weather
  and World Pressure systems as other maintenance

### Environmental bands

| Band | Character | Typical opportunities and pressures |
|---|---|---|
| **Median** | Relative sanctuary with soil, vegetation, drainage, cover, and reduced human access | Colony life, longitudinal travel, local Nodes, flood, scarcity, predators, and maintenance |
| **Roadway** | Moving barrier of pavement, traffic, heat, noise, vibration, fumes, water, and exposed distance | Crossing, deposited material, River Spume, immediate bodily danger |
| **Margin** | Abundant but disturbed ground between Roadway and Sound Wall | Sustenance, insects, water, shelter, Scrap, wreckage, contamination, mowing, predators, flooding, and human access |

Margin resources follow a broad tendency rather than rigid zoning. Vegetation
and Perishable Sustenance become more common toward sheltered Sound Wall edges;
Flexible and Rigid Scrap become more common near Roadways, debris deposits, and
wreckage. Natural features can occur throughout. A wrecked car may be terrain,
shelter, landmark, hazard, and major Node at once.

**River Spume** is the vehicle-generated turbulence, pressure change, and debris
lift above and beside a Roadway. Its force follows current traffic and is
strongest on and immediately beside the road, diminishing across the Margin.

### Biome reference

A Biome is a recurring environmental grammar. A Reach realizes that grammar as
one particular arrangement with its own Nodes, history, conditions, and
landmarks. Founding compatibility belongs to local topology; no Biome is
exclusive to one Species.

| # | Biome | Primary identity | Founding relationship |
|---:|---|---|---|
| 1 | **Rootbank Meadow** | Grass, eroded banks, exposed roots, hollows, and sheltered clearings | Rabbit |
| 2 | **Bramble Hollow** | Dense thorn and vine cover, narrow passages, and protected openings | Rabbit |
| 3 | **Culvert Garden** | Drainage infrastructure, wet soil, raised banks, stone, and seasonal flow | Mouse |
| 4 | **Concrete Trench** | Retaining faces, hard seams, broken slabs, runoff, heat, and shade lines | Mouse |
| 5 | **Wooded Median** | Trunks, canopy, roots, fallen branches, shade, and broken visibility | Squirrel |
| 6 | **Rock Cut** | Shelves, fissures, ledges, sparse trees, height change, and gaps | Squirrel |
| 7 | **Thin Grass Ribbon** | Narrow exposed ground, long sightlines, wind, and road proximity | Corridor |
| 8 | **Creek Split** | A longitudinal stream dividing banks, islands, and crossing places | Corridor |
| 9 | **Pond Hollow** | Standing water, reeds, saturated ground, insects, and changing margins | Corridor |
| 10 | **Interchange Expanse** | Broad disorienting ground among diverging roads and scattered infrastructure | Corridor |
| 11 | **Overpass Shadow** | Columns, beams, recesses, echo, vibration, drainage, and artificial shade | Unusual Corridor |
| 12 | **Abandoned Works** | Gravel, pipe, rebar, cut earth, incomplete drainage, and interrupted construction | Unusual Corridor |

The founding pool pairs Culvert Garden and Concrete Trench for Mouse, Rootbank
Meadow and Bramble Hollow for Rabbit, and Wooded Median and Rock Cut for
Squirrel. Starting contents may vary while the topology that makes JOIN,
GATHER, or CONNECT legible remains stable.

### Shared time

One world clock governs Home and Away:

> **DAWN → Morning → Midday → Evening → Night → DAWN**

Morning, Midday, Evening, and Night are the four playable Day Bands. DAWN is the
explicit accounting and calendar transition. Meaningful action, movement, and
duration advance time; inspection, reading, planning, and camera movement
leave it paused. Time changes the same light, weather, traffic, Colony state,
Nodes, and Field conditions whichever Mode currently holds attention.

| Register or context | Time relationship |
|---|---|
| **DWELL** | A normal Home commitment advances to the next Day Band. |
| **TRAVEL** | Direct movement consumes projected spatial reach within the current Band; exhaustion advances the Band. |
| **RISK** | Crossing uses the current Band and its traffic without adding another duration to the arrival movement. |
| **MEET** | Presentation has no universal cost; the selected action supplies its time. Rest and Homecoming each advance one Band. |
| **EMBODY** | Ordinary life remains within the current Band. |

Day Band is the sole mechanical world-time unit. TRAVEL uses no Time Mark,
action-point allowance, or hidden half-Band.

### Human activity as weather

Animals experience traffic and the broader field of human activity as weather:
large recurring conditions that can be anticipated in kind, sensed through
their effects, and never controlled. Traffic is its continuous expression;
maintenance, mowing, machinery, drainage work, litter, collisions, lighting,
and Road Work provide episodic fronts and disturbances.

- Day Band and season supplying recognizable rhythms without fixing the actual
  moment or local intensity
- Sound, vibration, air displacement, light, fumes, water, cut vegetation,
  debris, and changed access often arriving before the animals can perceive a
  cause
- Human bodies remaining outside the frame while vehicles, machinery,
  materials, and environmental effects remain fully present
- Traffic and work changing physical state through the same persistent world
  rather than arriving as detached encounter modifiers

### Traffic

Each Day Band produces variable traffic from a broadly predictable weighted
range. Traffic **thickness** describes how continuously vehicles occupy the
Roadway through their present volume and spacing; speed, pulse, vehicle mixture,
visibility, noise, weather, and disruption give that thickness its particular
character. One named state may become active when its threshold is reached:

| Day Band | Eligible special traffic state |
|---|---|
| **Morning** | **Morning Rush** |
| **Midday** | **Midday Window** |
| **Evening** | **Evening Rush** |
| **Night** | **Night Velocity** |

The state modifies the realized traffic pattern rather than replacing it. That
pattern belongs to the world and is not rerolled when RISK opens. Waiting may
offer different traffic by advancing one Day Band and also changing light,
weather, party condition, and the remaining return margin.

Season alters daylight, surface temperature, precipitation, vegetation,
visibility, human schedules, vehicle mixture, roadside work, and loose material.
Time of day and season therefore influence traffic without turning either into
a deterministic timetable.

### River Spume

River Spume is the atmospheric reach of the moving Roadway: turbulence,
pressure change, spray, grit, fumes, noise, vibration, and lifted debris created
by passing vehicles.

- Increasing traffic thickness tending toward sustained atmospheric pressure,
  while thinner high-speed traffic can create separated forceful pulses
- Speed, spacing, vehicle size and mixture, surface wetness, wind, precipitation,
  season, and Day Band changing its present expression
- Strength peaking over and immediately beside the Roadway and diminishing with
  actual distance across the Margin
- Roadway-proximate Nodes receiving stronger effects upon audibility,
  visibility, scent, footing, loose material, available responses, and
  consequence during MEET
- Nodes near enough to passing traffic carrying a situated chance for a thrown
  or dislodged object, scaled by present traffic and conditions
- The arriving object able to create atmospheric interruption, immediate
  danger, material opportunity, or persistent Node change
- Distance operating through the Node's physical position rather than a second
  proximity score or universal penalty band

### Weather and World Pressure

Season accumulates change across vegetation, animal activity, resources, Node
recovery, shelter, and civic need. Weather acts through particular ground:
rain, wind, heat, cold, flood, frost, and snow alter what can be reached, used,
heard, seen, protected, or sustained.

At Home, a present environmental condition becomes World Pressure by adding
contextual Load, testing relevant Readiness and Practice Strength, or supplying
the subject of a MEET. It remains attached to the actual Places, Roles, and
lives affected rather than becoming one pooled weather score. Away, the same
condition changes TRAVEL, Nodes, Rest, RISK, MEET, and physical consequence.

Environmental and human events use **Telegraph → Impact → Persistence →
Aftermath**. A phase opens MEET only when the Colony or party has a meaningful
choice; otherwise it changes or reports persistent world state directly.

### Road Work

Road Work is an acknowledged but undeveloped World Pressure family in v0.5. It
includes active lane and barrier work, resurfacing, mowing, drainage and culvert
clearance, temporary material, machinery, and related maintenance.

- Telegraph appearing through markings, equipment, cut vegetation, altered
  traffic, staged material, sound, light, vibration, or unusual human schedule
- Impact able to redirect traffic and River Spume or alter a Roadway edge,
  drainage feature, passage, Node, Sound Wall, or part of Home
- Persistence and Aftermath able to leave obstruction, access, shelter,
  displaced material, changed water, damaged ground, or a new opportunity
- Existing World Pressure, TRAVEL, RISK, MEET, and persistent-state rules
  carrying its effects
- Exact work families, generation, duration, warnings, and mechanical outcomes
  remaining for later authorial development

### Persistent places and Nodes

A Node is a fixed, recognizable Field location whose ecology, material,
shelter, inhabitants, alteration, or history can matter across visits.

| Quality | Examples | Persistent state |
|---|---|---|
| **Ecological** | Bramble, seed fall, insect bloom, water source | Season, abundance, recovery, disturbance |
| **Material** | Toolbox, litter catch, carcass, construction debris | Contents, condition, depletion, alteration |
| **Shelter** | Pipe, root pocket, hollow, culvert ledge | Safety, exposure, damage, occupation |
| **Relational** | Den, Guest camp, claim, meeting landmark | Occupant, relationship, terms, prior choices |
| **Human-made** | Drain, grate, barrier, vehicle cavity, worksite | Configuration, access, activity, hazard |

A Node may carry several qualities. Hazard is a present condition, and history
attaches directly rather than creating a separate Memory type. Renewal,
depletion, occupation, and alteration follow the Node's actual ecology and
world state.

### Current world-development boundary

Exact traffic generation and thresholds, River Spume effects and thrown-object
chances, season lengths, weather generation, Node renewal and yields, Road Work
content, and broader event frequency remain assigned to later authorial and
conceptual tuning. Current design establishes their relationships, causal
inputs, persistent world effects, and points of contact with Civic Balance and
Citizen activity.

## Appendix G — Citizen Activities and Expedition Reference

This Appendix gathers what Citizens and the player do within the world defined
by Appendix F. It follows the expedition from Launch through direct TRAVEL,
Rest, RISK, MEET, bodily consequence, Outposts, Return, and Homecoming.

### Expedition contour

> **Launch MEET → TRAVEL → Node, Rest, or RISK as encountered → contextual
> MEET where consequence requires choice → physical Return → Homecoming MEET
> → DWELL**

The Launch MEET selects a legal party from mechanically eligible Citizens,
shows the exact subtraction from Home, assigns prepared Supplies, and commits
the one active expedition. Party size, Body Units, Items, and Carry are
tabulated in Appendix E.

An active expedition keeps Away under player operation until Homecoming. The
player may inspect Home through established information lenses, while ordinary
DWELL construction, reassignment, Project commitment, and another Launch remain
closed. The party never travels, activates a Node, crosses, or decides
autonomously. Home's clock-bound systems continue, and a Home situation that
crosses the MEET threshold may briefly take focus before operation returns to
the party's exact persistent position.

### TRAVEL and projected reach

TRAVEL presents the Field from above and lets the player directly drive one
compact party figure through animal-scale continuous geography. Every Citizen
remains individually inspectable even though destination, movement, elapsed
time, and Carry are party-level facts.

Each Day Band begins with a projected **travel span**. Terrain, weather, Cargo,
bodily state, Rabbit composition, and pushing determine how much actual ground
the party can cover. Path length—including detours and backtracking—consumes
that span. Pausing movement preserves the party's position and remaining reach;
exhausting it advances the world to the next Day Band.

The Field shows reachable ground rather than exposing a second movement
currency. Grade, surface, cover, drainage, obstruction, shelter, and exposure
make paths meaningfully different. Changed physical passages alter later reach
through their actual geography rather than through a route-progression system.

Rabbit bodies modify normal travel span on the absolute three-Body-Unit scale:

**Rabbit TRAVEL multiplier = 1 + (Rabbit Body Units ÷ 3)**

| Rabbit Body Units | Normal travel span |
|---:|---:|
| 0 | 1× |
| 1 | 1⅓× |
| 2 | 1⅔× |
| 3 | 2× |

The multiplier increases distance within one Day Band. It adds no time, Carry,
MEET Round, or RISK action. Non-Rabbit party members impose no slowest-member
penalty. Carry and Squirrel Strained Carry follow Appendix E.

### Travel cadence and Rest

A rested party receives three traveled Day Bands at normal reach, then may push
through three more at declining reach:

| Traveled Band since Rest | Projected-reach multiplier |
|---:|---:|
| 1–3 | 1× |
| 4 | ¾× |
| 5 | ½× |
| 6 | ¼× |
| 7 | TRAVEL unavailable until Rest |

A Band counts when it ends after material travel, including when another action
advances time before the span is exhausted. MEET and Node work neither count as
TRAVEL nor reset cadence unless their resolved action explicitly supplies Rest.
Pushing reduces reach while Jostle and situated risk continue normally; it
creates no generic Fatigue state or automatic Wound or Exposure.

A Rest MEET may begin wherever the party can physically stop. Completion
advances one Day Band, resets travel cadence, stabilizes each current Wound for
the next three traveled Bands and their resolved situations, ends Tharn, and
creates a Stopover at that location. Open ground, weather, disturbance, and
available shelter determine contextual consequences. Natural refuge improves
those circumstances; a usable Outpost provides the reliable effects specified
below.

### Field Cards

Field Cards are occasional situated interruptions between Nodes:

- one 10% check follows each exhausted travel span
- at most one card occurs in a Day Band
- no check occurs when RISK or another consequential MEET has already occupied
  that Band
- after a card occurs, the next two otherwise-eligible exhausted spans are
  ineligible
- selection follows actual Reach, position, terrain, season, Day Band, weather,
  and persistent state
- a minor card changes or reveals the Field directly; a consequential card
  opens MEET

Nodes remain the primary intentional Away content: **Nodes are the meal; cards
are the weather.**

### Engaging Nodes

Appendix F defines Nodes as persistent world locations. TRAVEL reveals and
carries the party among them.

- A quiet Node remaining part of TRAVEL without requiring a decision
- Brief uncontested use able to resolve within the Day Band that reached it
- Work that genuinely occupies time advancing the next Band
- Meaningful use, opposition, danger, change, or opportunity opening contextual
  MEET
- The outcome changing the Node, party, relationship, Cargo, or world directly
- Material left behind becoming part of an authored Node change or being
  abandoned rather than creating a free Cargo cache on arbitrary ground

### RISK and Crossing

RISK begins at the selected **Staging Post**, the immediate Roadway-edge ground
from which the party observes current traffic, Day Band, weather, River Spume,
Cargo, and far-side refuge. The player may plan and commit, wait one Day Band,
or resume TRAVEL away from the road.

Its operative view is schematic and loosely backplated by the actual Staging
Post angle from the animals' side of the Roadway. The backplate preserves place,
traffic, weather, and danger while the species-specific schematic makes the
complete proposed passage legible.

Every Crossing follows:

> **Plan → Commit → Continuous Run → Resolve → Continue**

| Core Species | Question | Planning | Continuous Run |
|---|---|---|---|
| **Rabbit** | When does the Roadway open? | Select a represented traffic window, broad line, and far-side refuge. | One uninterrupted sprint. |
| **Mouse** | Where can continuity be made? | Connect three to six body-credible pavement features. | One chained scurry. |
| **Squirrel** | How can movement flow through traffic? | Set a trajectory, one or two redirects, and a far-side anchor. | One vector run. |

The Colony's Core Species supplies the RISK grammar for the whole party.
Land-bound Guests act through their real bodies within it. Crow and Gull alone
use the parallel Flyer expression: they share the Crossing commitment and time,
resolve flight through River Spume, weather, visibility, launch, and landing,
and may receive a different visible outcome from the ground party.

Commit is the final strategic input. The Roadway then remains in motion while
the complete plan resolves without steering, reaction prompts, or mid-road
MEET. Every committed Crossing brings the entire party to the far side. Group
passage resolves first; delay, Exposure, separation, Cargo loss, Wound,
Maiming, Tharn, or rarer valid consequences apply afterward. Any new decision
opens from the far side.

Adversity follows Body Units rather than headcount. RISK selects no additional
targets merely because a Mouse party contains more Citizens. One causal result
may create connected effects while avoiding duplicate charges for the same
danger.

### Return Crossing

At a homeward Staging Post, the player reads current conditions and crosses now
or waits. Present traffic, weather, visibility, River Spume, Cargo, traveled
Bands since Rest, party bodies, and applicable Signatures select one of two
presentations:

- **Automatic Return:** the ordinary procedure; hidden adjudication produces a
  clean crossing or a bounded penalty such as delay, Exposure, eligible Cargo
  loss, or Wound.
- **Full RISK:** an uncommon procedure opened when current conditions can
  support Maiming, Tharn, death, or the complete RISK consequence range.

Both carry the whole party continuously to the homeward side and show any
penalty only after it is clear of traffic.

### Away MEET

Unopposed situations present their concrete contextual actions directly.
Contested Away MEET always displays five response families in this order:

| Family | Direction |
|---|---|
| **CONTEST** | Overcome, resist, hold, seize, protect, or endure directly |
| **EVADE** | Bypass, escape, hide, distract, or use terrain |
| **PARLEY** | Ask, offer, trade, bargain, persuade, deceive, or invoke relationship |
| **YIELD** | Concede one stake, claim, possession, priority, or cost to preserve another |
| **WITHDRAW** | End the party's participation and leave the objective or situation |

Each active family contains one concrete response for the current Round.
Inactive families remain in place, greyed with one concise knowable reason.
Tools, Supplies, Keepsakes, relationships, and Guest Signatures already present
may make a response available or change how it operates. The provisional choice
shows its exact expressions before Commit.

The party's shared result resolves before personal consequence:

1. Resolve what the party achieves, prevents, accepts, or leaves unfinished.
2. Identify Citizens causally exposed by what they used, carried, protected,
   confronted, or were already suffering.
3. Assign consequence directly when one bearer is clear; otherwise select
   randomly among the equally exposed causal set.
4. Show cause, bearer, and continuing effect immediately.

One principal personal consequence ordinarily follows a Round. Focus may make
the same Citizen prominent but never causes or redirects harm. The changed
party, Node, relationship, object, and world state persist after MEET.

### Exposure

Exposure is a hidden per-Citizen measure from 0 through 6. It weights applicable
personal consequence toward the serious end of the range already supported by
the situation; it neither selects the causal target nor expands that range.

- A Citizen's first RISK of an expedition sets Exposure to at least 1 after the
  Crossing resolves. This floor is not a gain and receives no Wound multiplier.
- A circumstance that explicitly creates Exposure ordinarily adds one step.
- One cause supplies at most one base gain across its connected resolution.
- An unstabilized Wound doubles a normal one-step Exposure gain to two. A Wound
  created by that same incident does not double its linked gain.
- Exposure caps at 6 and creates no standing penalty to movement, Carry,
  response availability, Civic Share, control, or aptitude.

RISK first resolves Crossing consequence from the plan, bodies, traffic, and
environment without pre-existing Exposure or Wound weighting. Any Exposure
awarded by that resolved Crossing then enters ordinary persistence, including
the doubling of a normal gain when the Citizen already had an unstabilized
Wound.

When genuine uncertainty remains after situation and causal target are known:

**Exposure escalation chance = 10% × current Exposure**

One hidden check may move the selected Citizen's result one position toward the
serious end of the situation's ordered valid range. No check occurs when the
result is already determined or already most serious. Exposure is neither
consumed nor checked again for linked effects.

The interface communicates Exposure through body, behavior, voice, narration,
and context rather than a number or named ladder.

### Personal consequences

| Consequence | Persistence and effect |
|---|---|
| **Wound** | One binary, named recoverable injury. It limits only physically affected actions and doubles new Exposure while unstabilized. |
| **Maiming** | A lasting bodily change caused by a maiming injury. The incident also creates one acute Wound; recovery may clear that Wound while Maiming remains. |
| **Tharn** | Acute bodily shutdown during immediate danger. It supersedes the former objective and makes securing the Citizen and Rest mandatory. |
| **Death** | A rare final outcome available only when an explicitly severe situation made fatal stakes legible before Commit. |

A new Wound result upon a Wounded Citizen changes the injury description and
sets remaining recovery to the greater current or authored one-to-three
Healer-Day requirement. It creates no second Wound. Maiming enters adaptation
and possible Rehabilitation after its acute Wound follows ordinary recovery.

Remedy may stabilize a Wound through Homecoming, lessen one defined immediate
physical effect, or contain the acute Wound accompanying Maiming. Rest
stabilization lasts through the next three traveled Bands and their resolved
situations. Remedy can also enter PARLEY through credible offered care. It
never relieves Tharn.

### Tharn reference

Tharn occurs only when the immediate event can credibly produce shutdown.
Exposure and an unstabilized Wound increase susceptibility without causing it
independently. When Tharn lies within the event's valid range outside RISK:

**Tharn escalation chance = min(80%, 10% × (Exposure + 2 if Wounded and
unstabilized))**

RISK may produce Tharn from an adequately severe Crossing but is exempt from
pre-existing Exposure and Wound weighting.

The possibility of Tharn is never labeled, previewed, or given a probability.
The player sees only the actual situation and observable Citizen state. When it
strikes, the game names it and changes the MEET's subject immediately. YIELD
and WITHDRAW ordinarily remain available to secure the struck Citizen; another
family remains active only when it directly enables rescue or departure. The
party always retains the Citizen.

While Tharn persists, the party cannot activate another Node, enter RISK, or
resume an expedition objective. One completed Rest MEET ends it without
reducing Exposure or clearing Wound or Maiming.

### Exposure recovery

| Recovery context | Effect |
|---|---|
| **Ordinary Rest** | Ends Tharn, resets travel cadence, and stabilizes Wound for the next three traveled Bands; Exposure reduction depends upon place and outcome. |
| **Usable Outpost Rest** | Supplies ordinary Rest effects and removes one Exposure step, but never the final Away step. |
| **Home at DAWN** | Removes up to three Exposure steps from each Home-present Citizen, to a minimum of 0. |

Maximum Exposure therefore returns to baseline across two Home DAWNs: 6 to 3,
then 3 to 0. Relaunch preserves any remainder. Exposure recovery never clears
Wound or Maiming. Home Wound Recovery uses the Hearth, one committed Healer,
and the one-to-three Healer-Day Project defined in Appendix D.

### Outposts and Stopovers

A Stopover is the temporary Away state created by a completed Rest MEET. A
natural refuge can improve that Rest. An Outpost is persistent uninhabited Away
infrastructure that makes one known stopping place reliable.

The Colony establishes or restores an Outpost through a remote Builder Project
in the ordinary Home Project Queue:

- the target is an eligible location already found and identified
- one usable Workshop supplies Project capacity
- named Builder Citizens, required material, and Civic Share-Days are committed
  at Home
- routine construction travel and labor remain abstracted into that civic
  commitment, creating no Away party, Exposure, or personal consequence
- completion at DAWN establishes the Outpost and releases the Workshop and
  Builders

An Outpost has no stationed Citizens, routine upkeep, specialization, upgrade,
or Tier in v0.5. Explicit visible events alone can damage or destroy it. A
damaged Outpost persists physically but loses protected Rest, Exposure
reduction, and Cargo transfer until a remote Builder restoration Project
completes.

A Rest MEET at a usable Outpost:

- advances one Day Band and resets travel cadence
- ends Tharn and stabilizes Wound for the next three traveled Bands
- removes one Exposure step from each resting Citizen without removing the
  final Away step
- protects ordinary sleep from exposed-ground consequences
- permits any amount of fungible Cargo to enter Colony stock through abstract
  Colony sync, immediately freeing party Carry

The party remains Away. Tools, Supplies, Keepsakes, Artifacts, and other tracked
Items remain with their holders. Outpost Rest supplies no Healer-Days, clears
no Wound, removes no Maiming, and creates no second Home.

### Return and Homecoming

The player turns homeward through ordinary TRAVEL. Time, terrain, Carry,
Exposure, bodily state, Nodes, Rest, MEET, and Return Crossings continue to
govern the same physical journey. Clearing the last Roadway returns the party
to the Home Median; it still travels the remaining ground to the Colony.

Arrival opens Homecoming after every expedition. Homecoming advances one Day
Band and follows:

> **Frame → Recognize and receive → Reconcile → Continue**

Recognition presents the named lives that returned, anyone absent, visible
change, and the Colony that receives them before totals. Reconciliation then:

- transfers remaining Cargo into Colony stock
- returns unspent Supplies and clears their expedition positions
- preserves spent Supplies, Item damage or loss, discoveries, relationships,
  Wound, Maiming, Exposure, death, and every other resolved Away fact
- restores each eligible returning Citizen's standing Role contribution and
  recalculates Civic Balance, Practice support, production, and Home state
- offers an available Wound Recovery Project through Hearth and Healer when
  applicable
- opens only Care, Allocation, Guest, succession, memorial, or other choices
  whose alternatives produce materially different persistent results

A routine Homecoming remains brief and warm. Consequential return expands
around its actual concerns without rerolling or grading the expedition. When
reconciliation completes, the expedition ends and DWELL resumes. Quiet
Equilibrium and EMBODY return only when the Colony's actual resulting state
supports them.

### Current activity-tuning boundary

Base travel distances, Crossing adjudication, contextual Rest consequences,
personal-consequence distributions, Wound recovery requirements, and related
activity pacing remain subject to their dedicated conceptual tuning work.
Tuning may alter those quantities while preserving the single Day-Band clock,
direct TRAVEL, species-distinct RISK, six-step Exposure system, causal personal
consequence, bounded Rest, and Homecoming reconciliation defined here.

## Appendix H — Citizens and Species Reference

MEDIAN's civilization remains small enough for every Citizen to stay a
particular life. Species changes body, spatial understanding, capability, and
the shape of play while preserving equal civic and historical standing.

### Shared Citizen architecture

| Aspect | Reference rule |
|---|---|
| **Citizen** | One named member of the Colony with a body, relationships, belongings, history, present circumstances, and possible future |
| **Fractional player character** | Each Citizen carries part of the continuity, agency, attachment, and consequence ordinarily concentrated in one player character |
| **Belonging** | The living Roster records who belongs to the Colony |
| **Location** | Each Citizen is at Home or at one current Away position |
| **Availability** | A present adult Citizen contributes when available; age, injury, treatment, absence, or another actual condition may temporarily suspend contribution |
| **Civic Share** | The normalized contribution supplied by the Citizen's Body Unit while present, adult, and available |
| **Individual continuity** | Names, relationships, Tools, Supplies, Keepsakes, Wounds, Maiming, memory, and death follow particular Citizens |
| **Cross-Register truth** | A change in DWELL, EMBODY, TRAVEL, RISK, or MEET remains true in every other Register |

Individual appearance, voice, temperament, habits, preferences, relationships,
and history shape expression without creating hidden aptitude or productivity
tiers. Core and Guest Citizens use the same underlying architecture of
citizenship, consequence, and memory.

### Core Species

Mouse, Rabbit, and Squirrel are complete playable civilizations. Each supplies
one bodily scale, one characteristic understanding of inhabited space, and one
distinct Away advantage. The comparisons below rotate their order so reference
layout implies no hierarchy among them.

The illustrative maxim is: **Mouse Builds a Manor House, Rabbit Builds a
Cul-De-Sac, Squirrel Builds a Web.** It describes three civilizational shapes;
Residence and Practice retain their shared functional names.

#### Body, civic scale, and Residence

| Core Species | Animal expression | Body Unit and Civic Share | Core Residence | Well-Placed Residence |
|---|---|---:|---:|---:|
| **Mouse** | Quick heartbeat and speed of thought; close attention to scent, sound, touch, edges, and nearby movement | 0.5 per Mouse | 4 Mice | 6 Mice |
| **Rabbit** | Vigilant stillness, broad attention, explosive ground movement, and decisive refuge-seeking | 1 | 2 Rabbits | 3 Rabbits |
| **Squirrel** | Grasp, balance, climbing, leaping, and continuous judgment between present foothold and next movement | 1 | 2 Squirrels | 3 Squirrels |

Two individual Mice equal one Body Unit while remaining two complete Citizens.
Each keeps a name, relationships, personal positions for one Tool, one Supply,
and one Keepsake, and their own exposure to consequence. Aggregate Home systems
therefore treat two Mice as equivalent to one Rabbit or Squirrel while personal
life continues at the animal level.

#### Home and spatial expression

| Core Species | Operator | Colony shape | A Place is Well Placed when… | Characteristic growth |
|---|---|---|---|---|
| **Rabbit** | **GATHER** | Places face protected open common ground with mutual visibility and nearby refuge | it forms, faces, or preserves that common space while retaining protective edges and a quick way to cover | complete one protected court or green, then bud another neighborhood around new common space |
| **Squirrel** | **CONNECT** | Places become nodes in a branching, redundant Web of anchors and traversable links | it participates securely in the network with credible onward movement and an alternative if one route fails | add or reinforce nodes, bridge gaps, and turn fragile routes into resilient connections |
| **Mouse** | **JOIN** | Adjoining rooms, sheltered edges, shared boundaries, and accumulated interior become one inhabited fabric | it directly adjoins the protected inhabited fabric without requiring a passage between the spaces | add chambers, pockets, and sheltered edges beside what is already inhabited |

The operator judges both Residence and Practice Places. A completed usable
Place contributes its ordinary function in either placement state; Well-Placed
status adds the defined Housing or Practice benefit. Later physical change may
alter that state while the Place and its history persist.

#### Away expression

| Core Species | Party advantage | Secured Carry | Crossing question and commitment | Characteristic player decision |
|---|---|---:|---|---|
| **Squirrel** | Each Squirrel Body Unit adds 10 optional Strained Carry beyond secured capacity; moved Strained Cargo receives the visible proportional Jostle check | 10 per Squirrel | **How can movement flow through traffic?** Set one vector trajectory, one or two redirects, and a far-side anchor; then resolve one continuous run | whether a larger possible return justifies carrying an inherently precarious haul |
| **Mouse** | Each Mouse carries 6 secured slots, giving a full Body Unit 12 instead of the ordinary 10; greater headcount also provides more personal Item positions | 6 per Mouse; 12 per Body Unit | **Where can continuity be made?** Join three to six body-credible pavement features; then resolve one continuous scurry | which particular Citizens, relationships, capabilities, and risks to include in the larger party roster |
| **Rabbit** | Each Rabbit Body Unit adds one-third normal TRAVEL span, reaching double progress with three Rabbit Body Units | 10 per Rabbit | **When does the Roadway open?** Choose a traffic window, broad line, and far-side refuge; then resolve one uninterrupted sprint | how to use the larger practical itinerary created by greater movement |

An ordinary party contains one and one-half to three Body Units and at least two
actual animals. Species effects follow the bodies physically present: mixed
parties receive Rabbit movement and Squirrel Strained Carry in proportion to
their actual Body Units, while every individual Mouse supplies its six secured
Carry and personal Item positions. Adversity remains normalized by Body Unit so
a larger Mouse headcount creates no extra hazard selections.

### Guest Citizens

A Guest is a named non-Core animal welcomed through relationship and
accommodation. Welcome grants full civic rank, a place in the Roster, one Body
Unit and Civic Share in v0.5, a Residence satisfying one species-specific Fit,
ordinary relationships and memory, and one bounded Signature that makes bodily
difference useful and visible.

#### Names and reference usage

Each Guest species has a **canonical short name** for headings, tables, labels,
and rules. Descriptive prose may use that name or the listed prose form. Where
the present design has established no separate long form, prose retains the
short name rather than supplying an unapproved taxonomic distinction.

| Short name | Prose form | Short name | Prose form |
|---|---|---|---|
| Raccoon | Raccoon | Owl | Barred Owl |
| Crow | Crow | Sparrow | Song Sparrow |
| Gull | Gull | Toad | American Toad |
| Fox | Red Fox | Fireflies | Firefly Family |
| Weasel | Weasel | Groundhog | Groundhog |
| Hedgehog | Hedgehog | Turtle | Painted Turtle |
| Snake | Garter Snake | Bumblebees | Bumblebee Household |
| Mink | American Mink | Mole | Eastern Mole |
|  |  | Bat | Little Brown Bat |
|  |  | Pigeon | Rock Pigeon |
|  |  | Skunk | Striped Skunk |
|  |  | Possum | Opossum or Virginia Opossum |

#### Shared Guest types

| Property | Expedition Guest | Resident Guest |
|---|---|---|
| Citizen standing | Full | Full |
| Body Unit and Civic Share | 1 | 1 |
| Home Role | Authored for the individual Citizen | Fixed by species |
| Signature operates | Away | At Home |
| Launch | Eligible | Home-resident |
| Personal Away consequence | Applies normally | Arises through applicable Home events |
| Residence, relationships, memory, and EMBODY | Full | Full |

An Expedition Guest's departure withdraws their Civic Share from Home like any
other departing Citizen. A Resident Guest may sustain their fixed Role or
commit their share to an eligible Project. Their Signature remains one situated
capability within a complete civic and personal life.

#### Expedition Guest roster

Every Expedition Guest is one individual Citizen. Carry remains secured party
capacity; Snake's limbless body creates the sole low outlier. Crow and Gull are
the only Guests with the shared parallel Flyer expression in RISK.

| Guest | Home Role | Secured Carry | Away Signature | Residence Fit | Citizen form |
|---|---|---:|---|---|---|
| **Raccoon** | Authored per Citizen | 12 | **HANDLE — Latchwork:** directly manipulate one accessible human-made closure or simple mechanism | dry exterior access | Individual |
| **Crow** | Authored per Citizen | 9 | **HANDLE — Trialwork:** recruit one available object for one plausible test or indirect manipulation | high open perch | Individual; Flyer |
| **Gull** | Authored per Citizen | 9 | **READ — Long View:** reveal situated context about broad geography, weather, water, traffic, or distant activity before commitment | broad open landing | Individual; Flyer |
| **Fox** | Authored per Citizen | 12 | **HANDLE — Carcass Claim:** process suitable matter at an eligible carcass Node into its specified Supply, as the biological counterpart to RENDER | drained boundary ground | Individual |
| **Weasel** | Authored per Citizen | 10 | **INTERCEDE — Drive Off:** press one small predator or aggressive animal away from something vulnerable | narrow multi-exit bank | Individual |
| **Hedgehog** | Authored per Citizen | 8 | **INTERCEDE — Living Cover:** shelter one injured or very small Citizen, one fragile Cargo stake, or one bounded withdrawal | concealed hedge | Individual |
| **Snake** | Authored per Citizen | 6 | **SPEAK — Display:** use recognized posture, movement, and stillness to open a fitting social response | sun-warmed shelter | Individual |
| **Mink** | Authored per Citizen | 10 | **REACH — Water Reach:** enter suitable water, flooded culverts, drainage channels, or waterlogged spaces on the party's behalf | safe waterline | Individual |

#### Resident Guest roster

Resident Signatures operate through Home situations, relationships, or one
named Practice relationship. Fireflies and Bumblebees are the complete v0.5
collective-bodied set: each visible household is one Citizen, one Body Unit,
one Civic Share, one Roster entry, and one continuous subject of consequence.

| Guest | Fixed Role | Home Signature | Residence Fit | Citizen form |
|---|---|---|---|---|
| **Owl** | Watchkeeper | **Night Sky-watch:** sharpen one existing nocturnal Telegraph while Owl is available and a Watchpost is usable | high listening hollow | Individual |
| **Sparrow** | Teacher | **SPEAK — Day Call:** use learned calls and social voice to improve understanding in an eligible Home SPEAK situation | concealed social perch | Individual |
| **Toad** | Caretaker | **Wet-Ground Care:** open a Caretaker response during an eligible Garden Home MEET concerning runoff, dampness, or invertebrate pressure | wet edge with dry refuge | Individual |
| **Fireflies** | Leader | **SPEAK — Lantern Procession:** coordinated light makes participants easier to understand and opens an eligible win-win response during a nighttime Home MEET | dark damp flight space | Collective-bodied household |
| **Groundhog** | Gardener | **Seasonal Telegraph:** make an approaching seasonal change legible early enough for civic response | deep drained ground | Individual |
| **Turtle** | Caretaker | **Water Garden Residence:** incorporate one suitable Guest Residence into a completed Garden | shallow water and basking | Individual |
| **Bumblebees** | Gardener | **Garden Cohabitation:** incorporate the household Residence into one Garden and add its bounded yield benefit while the household sustains Gardener responsibility | sheltered flower access | Collective-bodied household |
| **Mole** | Builder | **Subsurface Diagnosis:** reveal the practical condition beneath one visible Place or proposed Place when hidden ground matters | visible undisturbed soil | Individual |
| **Bat** | Builder | **Workshop Roost:** incorporate one suitable Guest Residence into a completed Workshop | high dry-dark roost | Individual |
| **Pigeon** | Leader | **Gathering Loft:** incorporate one suitable Guest Residence into a completed Gathering Place | open built ledge | Individual |
| **Skunk** | Watchkeeper | **SPEAK — Boundary Deterrence:** open a favorable nonviolent response in an eligible threatening-animal Home MEET | downwind boundary | Individual |
| **Possum** | Healer | **Hearth Annex:** incorporate one suitable Guest Residence into a completed Hearth | ventilated receiving edge | Individual |

#### Residence and Practice-sharing exceptions

One completed Guest Residence ordinarily occupies one dedicated Place and
houses one Guest Citizen or collective-bodied household. It uses one simple
Residence Fit judged as a whole. A Well-Placed Residence fulfills the housing
portion of the Guest's Terms of Hospitality; later loss of fit creates a
visible accommodation problem while citizenship endures.

Five Resident Signatures provide explicit Practice-sharing exceptions:

| Guest | Host Practice | Incorporated Residence effect |
|---|---|---|
| **Turtle** | Garden | Uses no separate Place and adds no yield, Practice Strength, or capacity |
| **Bumblebees** | Garden | Uses no separate Place; while the Garden is usable and the household is present, available, and sustaining Gardener responsibility, adds 0.5 Perishable Sustenance to that Garden's ordinary fractional-throughput cadence |
| **Bat** | Workshop | Uses no separate Place and adds no Practice Strength, passive output, Project progress, or capacity |
| **Pigeon** | Gathering Place | Uses no separate Place and adds no Practice Strength or capacity |
| **Possum** | Hearth | Uses no separate Place and adds no Remedy Preparation, Practice Strength, or capacity |

Each incorporated Residence still requires an ordinary Builder Project,
material, time, and its complete Residence Fit. The host remains one Practice
with its normal improvement rules and one-Project capacity. These five authored
exceptions establish no general mixed-use Place rule.

### Species difference in ordinary life

Species remains visible between mechanical interventions. Bodies determine
movement, posture, spatial use, rest, equipment expression, and EMBODY;
Residence, sound, activity, season, and relationship shape recurring Colony
presence. Song, calls, hum, flight, scent, water movement, digging, nocturnal
activity, and other species-grounded expressions may enter the Colony's sound
bed and visible routine without becoming additional bonuses or meters.

Every Guest forms individual relationships and accumulates their own history.
Their Signature makes one ecological capability legible, while ordinary civic
life, vulnerability, friendship, and memory keep that capability from becoming
their entire identity.

### Scope and extension

- Every current individual Guest remaining one Body Unit; a later larger or
  smaller value requiring an explicit species rule
- Fireflies and Bumblebees remaining the only collective-bodied Citizen types
  in v0.5
- Resident Guests remaining Home-resident and Expedition Guests retaining
  individual-authored Home Roles
- Guest Residence Fits remaining one whole requirement rather than an
  additional housing score or checklist
- Core-Species advantages changing campaign texture while preserving shared
  civic output and collective action
- Exact species content, tuning, presentation, and future Guest additions able
  to expand from this common architecture without changing Citizen standing

## Appendix I — Attachment-Forward Design

`Philosophy.Pillar.AttachmentForward`

Attachment-forward design is an orientation toward making imagined people,
places, objects, relationships, and histories emotionally durable.

It asks:

> **What does this work enable someone to know, value, remember, and become
> unwilling to lose?**

A fictional person may become companionable enough to be remembered with
something like the texture of a friend. A fictional place may become familiar
enough to be missed. An object may matter because of who made it, carried it,
repaired it, or left it behind. A remembered event may change how everything
around it is understood.

These attachments cannot be commanded. A work cannot instruct its audience to
love a character or declare a place meaningful on their behalf. It can create
the conditions in which attachment becomes possible: legibility, continuity,
repeated contact, successful care, recognizable identity, shared history,
credible danger, consequence, and return.

Attachment-forward design deliberately creates those conditions.

### A direction rather than a promised response

The word **forward** names the direction in which the design points. It does
not guarantee that attachment will occur, determine what a player will value,
or prescribe an approved emotional response.

Different players may form attachments to different subjects. One may care
most about a particular character. Another may become invested in a settlement,
a familiar landscape, a handmade object, or a history that emerged through
play. Some may appreciate the design without developing strong personal
attachment at all.

The design succeeds by allowing particularity to accumulate and remain
perceptible. It gives people enough continuity and freedom to decide what
matters to them.

Attachment-forward is therefore neither a genre nor a tone. It can inform
strategy, simulation, role-playing, adventure, survival, management, narrative,
or contemplative design. It can coexist with humor, warmth, grief, danger,
difficulty, or calm.

### Three design orientations

Production-forward, survival-forward, and attachment-forward design may share
many of the same mechanics. The distinction is the purpose those mechanics
serve when priorities conflict.

| Orientation | The designed subject is primarily understood as… | Successful play tends toward… |
|---|---|---|
| **Production-forward** | A machine or process that transforms inputs into increasingly valuable outputs | Efficiency, acceleration, expansion, mastery, and replacement |
| **Survival-forward** | A vulnerable system resisting scarcity, entropy, or hostile conditions | Continued existence, recovery, security, and the postponement of collapse |
| **Attachment-forward** | A particular world inhabited by particular lives and accumulated history | Stability, familiarity, durable meaning, and chosen risk on behalf of what matters |

A single work may use all three orientations. A settlement can require
productive competence and credible survival while still being designed
primarily to become known and valued as a particular home.

Attachment-forward design changes the hierarchy of purpose. Production
supports continuity. Survival protects particularity. Progress deepens or
extends an existing world rather than continually replacing it with more
efficient content.

### The four anchors of attachment

Attachment commonly forms around four kinds of subject.

| Anchor | What acquires particularity | Common manifestations |
|---|---|---|
| **Person** | A recognizable life with a body, behavior, relationships, belongings, history, vulnerability, and possible future | Named characters, recurring companions, distinct habits, personal choices, visible change, persistent relationships |
| **Place** | Somewhere known through use, movement, habitation, alteration, and return | Homes, settlements, rooms, paths, landmarks, neighborhoods, repeated viewpoints, spatial history |
| **Object** | A material thing carrying use, provenance, association, and consequence | Personal equipment, gifts, repaired possessions, handmade things, inherited objects, items carried through important events |
| **Memory** | An event or condition whose persistence changes the meaning of the present | Records, stories, scars, memorials, altered environments, recurring dialogue, images, rituals, remembered absences |

Relationships pass through all four anchors. A person may be remembered through
a place. An object may preserve a relationship. A place may become significant
because of what happened there. A memory may alter how a familiar person or
object is perceived.

Strong attachment-forward design lets these associations accumulate without
requiring every one to become a formal bonus.

### The attachment chain

Attachment depends upon comprehensible interaction with a persistent subject.

> **Legibility → competence → stability → attention → attachment**

**Legibility** allows someone to understand what exists and what is happening.

**Competence** allows them to act with reasonable confidence and recognize the
relationship between decision and result.

**Stability** creates intervals in which immediate operational demands no
longer consume all available attention.

**Attention** can then move from controlling the system toward noticing its
inhabitants, details, histories, and ordinary rhythms.

**Attachment** may form as those particulars become familiar and personally
significant.

Repeated contact operates throughout this sequence. A person, place, or object
must usually remain present long enough to become known.

Once attachment exists, it changes the meaning of subsequent decisions:

> **Attachment → chosen risk → consequence → return → deeper
> attachment**

Risk becomes more significant when something particular is at stake.
Consequence becomes more meaningful when it changes an already known subject.
Return allows the changed person, object, or understanding to re-enter a
familiar context.

This cycle can deepen attachment without requiring continual escalation. A
small return to a familiar place may matter more than the discovery of a larger
but interchangeable one.

### How attachment-forward design manifests

Attachment-forward design is visible in the relationships among systems,
presentation, persistence, and pacing. It is rarely created by one feature.

#### Legible continuing subjects

The work gives the audience recognizable subjects whose continuity can be
followed.

A population remains comprehensible enough for individual absences to matter.
A home retains a stable physical identity. An object remains the same object
after being used, damaged, repaired, or transferred. A history remains
accessible enough to inform the present.

The audience should be able to answer questions such as:

- Who is this?
- Where do they belong?
- What has changed?
- What happened here?
- Who carried this?
- Why does this matter now?

#### Particularity rather than categorical variation

Procedural variation can produce abundance without producing attachment. A
thousand randomized residents may remain interchangeable if none can be
recognized across time.

Particularity requires persistent distinctions. These distinctions may include
appearance, voice, habits, relationships, location, possessions, authorship,
prior events, or visible consequences. Their purpose is to make one subject
distinguishable from another and one history distinguishable from a reset
state.

Statistical uniqueness alone is insufficient. A character with a rare
numerical combination may still feel generic. A mechanically ordinary
character may become irreplaceable through accumulated association.

#### Continuity through change

Persistence becomes emotionally meaningful when a subject can change without
becoming a different disposable instance.

A place may expand while retaining its earlier rooms. An object may show
repair. A character may age, recover, acquire a disability, alter a
relationship, or assume a new responsibility. The present should contain
legible evidence of the past.

Change gives continuity shape. Continuity gives change weight.

#### Meaningful dependence and care

Care becomes credible when the subject has understandable needs and when the
audience's actions materially affect what happens.

This does not require converting affection into a currency. The player may
care because care is strategically relevant, but they must also be allowed to
care because someone or somewhere has become particular.

The strongest systems make practical responsibility and emotional attention
reinforce one another without becoming identical. Supplying shelter may be
necessary. Choosing to linger, remember, accompany, or preserve may remain
voluntary.

#### Successful stillness

Continual instability can prevent attachment by keeping attention fixed on
emergency response. A system that always deteriorates may be engaging as
survival pressure while leaving little space for familiarity or observation.

Attachment-forward design therefore benefits from achievable stability.
Competent play can produce a period in which ordinary life proceeds without
constant correction. Stillness becomes evidence that the system is working.

This does not mean nothing happens. It means the audience can attend to
activity whose importance is not limited to crisis resolution: routine, play,
conversation, craftsmanship, rest, environmental change, or companionship.

#### Credible consequence

Consequence gives protection, preparation, and return weight. It works best
when it is causally legible and proportionate to the situation.

The audience should understand:

- What was at stake
- What choice was made
- Who or what became exposed
- Why the consequence followed
- What changed afterward
- How that change persists

Arbitrary loss discourages attachment because investment becomes irrational.
Total safety can make protection decorative because nothing meaningful can
change. Attachment-forward design occupies the middle: enough continuity to
encourage investment and enough consequence for that investment to matter.

#### Return and recontextualization

Return is one of the strongest attachment structures.

A person leaves a familiar place and later re-enters it changed. An object
comes back carrying new provenance. A discovery alters how an old location is
understood. A home receives the consequences of an outside experience.

The emotional force lies in comparison between the remembered state and the
present one. Return makes change legible because the audience already knows
what is being returned to.

#### Memory without compulsory reward

Memory systems can preserve meaningful events without converting every event
into an advantage.

A scar, journal entry, altered room, archived image, relationship change, or
remembered line may matter through interpretation alone. Mechanical
consequences remain appropriate where the event genuinely changes future
possibilities, but universal rewards can turn remembrance into another
optimization routine.

Some memories should change play. Others should change meaning.

#### Presentation as continuity

Attachment can also manifest through visual, auditory, spatial, and linguistic
continuity.

A character's appearance may evolve while remaining recognizable. A settlement
may be depicted repeatedly from related viewpoints. A familiar sound may
return after an absence. A record may place an old and current image in
relation. A recurring phrase may acquire new meaning through context.

Presentation should help the audience recognize continuity rather than merely
deliver novelty.

### Systemic attachment and expressive texture

Attachment-forward design needs both working systems and non-instrumental
expression.

A substantial repeatable system must perform genuine design work. It should
alter what can be understood, chosen, prepared, risked, protected, built,
carried, restored, remembered, or otherwise made consequential.

This does not require every expressive moment to produce a reward.
Environmental detail, ordinary behavior, affection, humor, beauty, and quiet
presence may exist without instrumental output. Their value may be perceptual
or emotional.

The distinction concerns the demand placed upon attention:

- A passing detail may remain texture.
- A recurring presentation may establish familiarity.
- A persistent fact may enrich identity.
- A formal system must transform understanding, choice, state, or consequence.

Sentiment unsupported by credible logic can feel ornamental. Logic that never
releases attention leaves no room for sentiment.

### Attachment-forward is not the same as cozy

Cozy and attachment-forward describe different dimensions of design.

**Cozy** commonly describes an experiential condition: safety, softness,
abundance, manageable demands, comforting repetition, and relief from imminent
loss. It primarily asks:

> **How does this experience feel?**

**Attachment-forward** describes a design direction. It asks:

> **What does this experience allow someone to know, value, remember, and
> become unwilling to lose?**

A work can be cozy without producing deep attachment. It may offer gentle
activity, pleasant company, reassuring abundance, and an attractive
environment while allowing every inhabitant, object, and location to remain
interchangeable.

A work can also be strongly attachment-forward while containing uncertainty,
grief, danger, difficult decisions, and permanent change.

Attachment-forward is therefore not an intensified form of coziness. It is an
orientation toward particularity.

#### Cozy conditions can support attachment

Safety and softness can create the attention needed for familiarity. Repeated
domestic routines can make people and places recognizable. Relief from pressure
can give the audience time to observe details that urgent play would obscure.

Cozy conditions are especially valuable when they feel connected to a
particular place or relationship. Comfort becomes more meaningful when the
audience understands whose comfort it is, how it was created, and what history
it contains.

#### Danger can also support attachment

Danger is not inherently opposed to attachment. Selective danger can reveal
what already matters.

The purpose of danger in an attachment-forward design is not to establish
seriousness through cruelty. It gives weight to protection, preparation,
absence, and return. Consequence should ordinarily change lives before erasing
them, allowing experience to remain visible in the people and world that
continue.

If nothing meaningful can change, safety may become decorative. If loss is
constant or arbitrary, attachment becomes unreasonable. The design needs enough
security for emotional investment and enough trusted consequence for that
investment to matter.

#### Cozy is a state; attachment-forward is a direction

| Dimension | Primary concern |
|---|---|
| **Cozy condition** | Whether the present experience feels safe, familiar, restorative, abundant, or gently occupied |
| **Attachment-forward direction** | Whether particular people, places, objects, and histories become increasingly knowable, memorable, and worth protecting |

Either may exist without the other. They become especially powerful together
when comfort belongs to a recognizable person or place and has been established
through credible effort.

MEDIAN offers one illustration. Its Home can become warm, abundant, familiar,
and quiet, while departure exposes particular Citizens to an active and
dangerous outside world. Its intended emotional rhythm is:

> **Sanctuary → departure → exposure → consequence → return**

Cozy conditions occupy an important place inside that rhythm. They are the
ordinary life made possible by successful stewardship and the condition to
which changed Citizens return.

> **MEDIAN earns its cozy.**

The phrase describes a particular application of the wider philosophy: comfort
gains meaning because it has a history, belongs to someone, and remains worth
protecting.

### Manifestation across media

Attachment-forward design has no mandatory interface. Its principles must be
translated into forms native to each medium.

| Medium | Characteristic attachment opportunities |
|---|---|
| **Simulation and videogames** | Persistent state, visible habitation, spatial familiarity, recurring behavior, direct consequence, evolving appearance, revisitation, and systemic return |
| **Tabletop role-playing** | Shared authorship, performed voice, recurring relationships, ritual, negotiated memory, player-created history, and continuity across changing protagonists |
| **Board games** | Physical construction, inhabited arrangements, visible absence, repeated handling of named pieces, persistent campaign records, and tactile return |
| **Card games** | Singular cards accumulating association, personal stacks or sleeves preserving change, tableau history, recurring combinations, and remembered draws |
| **Mobile games** | Brief intimate visits, portrait-scale character attention, tactile interaction, personal archives, and player-controlled return without coercive scheduling |
| **Books and sourcebooks** | Recurring characters and locations, maps, cross-references, marginal memory, visual continuity, narrative examples, and cumulative understanding through rereading |

Translation should preserve relationships rather than reproduce features
literally. A videogame's persistent simulated settlement might become a Colony
sheet in a role-playing game, a modular physical arrangement in a board game,
or a recurring illustrated location in a book.

The test is whether the translated form still allows something particular to
be known, changed, remembered, and revisited.

### Design protections

Attachment-forward work benefits from several protections:

- Keep important populations within emotional comprehension.
- Give recurring subjects stable identities across change.
- Let places accumulate rather than continually replacing them.
- Make important state legible without reducing every personal truth to a
  number.
- Provide enough stability for observation and familiarity.
- Connect consequences to understandable causes.
- Let danger change subjects before routinely erasing them.
- Preserve the history of objects and places where that history matters.
- Allow memory to persist without requiring a reward.
- Keep care from becoming solely an optimization economy.
- Avoid measuring affection as proof that attachment occurred.
- Let the audience choose what becomes important.
- Translate attachment relationships across media rather than copying
  interfaces.
- Use novelty to deepen an existing world as well as to introduce new content.

### Acceptance test

An attachment-forward design should support affirmative answers to these
questions:

1. Can the audience identify particular people, places, or objects rather than
   knowing only their functions?
2. Do those subjects remain recognizable across time and change?
3. Can the audience understand why the present state exists?
4. Does competent participation create enough stability for attention to move
   beyond operation?
5. Can ordinary activity matter without always producing a reward?
6. Does absence become noticeable because a particular presence was previously
   established?
7. Do important consequences follow intelligible causes?
8. Does return reveal what changed?
9. Can history alter meaning without always becoming a modifier?
10. Does growth deepen or extend what already matters?
11. Can the audience care without being instructed, scored, or rewarded for
    caring?
12. Would the loss or transformation of a subject feel specific because the
    work previously allowed its identity to accumulate?

Attachment-forward design succeeds when a system, world, or work stops feeling
interchangeable.

It becomes this place, this object, this history, and these lives.

### References

- [Project Horseshoe, *Coziness in Games: An Exploration of Safety, Softness,
  and Satisfied
  Needs*](https://projecthorseshoe.com/reports/featured/ph17r3.htm)
- [Wholesome Games, *About*](https://wholesomegames.com/)

## Appendix J — Manifestations: MEDIAN in Other Forms

A **Manifestation** is an authored expression of MEDIAN in another form. The
desktop and console computer game remains the primary Manifestation and the
subject of this Concept Sourcebook. The possibilities below identify what
MEDIAN might offer other media without proposing ports of the primary game or
promising additional products.

### Translation principle

MEDIAN translates through its world, relationships, and emotional direction
rather than through feature count. Another form may choose its own scale,
procedures, pacing, and player position while drawing upon the same narrow
animal country, active human Roads, particular Citizens, accumulated Home, and
movement between sanctuary and exposure.

> **A Manifestation succeeds when the player recognizes the same sanctuary,
> the same exposure, and the same particular friends even when almost none of
> the controls are shared.**

The briefs below describe promising directions rather than specifications.
Each would require its own design and prototype if ever pursued.

### Tabletop role-playing game

MEDIAN offers a role-playing group one shared Home and a small community of
animals whose relationships, journeys, injuries, and memories can accumulate
across a campaign. Spoken play could bring exceptional depth to animal
perspectives, Colony life, Guest encounters, and the question of what is worth
risking beyond sanctuary. Its promise lies in collective storytelling around
particular lives rather than reproduction of the computer game’s management
systems.

> **The adventure is important because someone must carry it Home.**

### Spatial board game

MEDIAN naturally offers a striking physical object: one animal Colony built on
a narrow strip between two active Roads. Players could watch named pieces leave
visible absences, construct a species-shaped Home together, and preserve the
marks of earlier sessions on the board. Its promise lies in making constrained
space, shared stewardship, and attachment to a physically accumulated place
tangible.

The defining image is a table where players can point to a patched shelter and
remember who built it, what crossed the Road to complete it, and who once lived
there.

### Cooperative fixed-content card game

MEDIAN’s Citizens, relationships, objects, journeys, and consequences are well
suited to cards that recur and acquire meaning through association. A Citizen’s
departure could literally alter the Colony deck; a returned object or lasting
injury could remain in circulation for the rest of the campaign. Its promise
lies in making presence, absence, and memory structural within one complete
authored set.

> **Every Citizen changes the deck simply by being present.**

### Standalone mobile game

A portrait phone screen already resembles a small median held between two
Roads. MEDIAN could become an intimate game of brief, voluntary visits to a
persistent Colony: noticing familiar Citizens, accompanying one small event,
and watching a particular Home change over time. Its promise lies in
pocket-scale familiarity and return, protected from streaks, absence penalties,
and emotional coercion.

> **The Colony waits without demanding.**

The following concept is the sole in-depth example. It demonstrates how a
Manifestation might embrace its medium and MEDIAN’s themes without
transliterating the primary game’s mechanics. Its detail gives the other forms
neither lesser status nor an implied production order.

### In-depth example — Standalone mobile game: *MEDIAN: One Small Place*

#### Pitch

An intimate Colony chronicle played through short, deliberate visits to a
living median.

The portrait screen becomes the world’s geography. Home occupies a narrow
vertical strip through its center while traffic moves continuously along both
edges. The player holds the Colony between the Roads in their own hand.

This is a slow game about noticing a particular place often enough for it to
become familiar.

> **Each visit lets the player notice one thing, accompany one life, and leave
> one mark.**

#### Voluntary return

A visit lasts roughly five to eight minutes, although the player may remain and
observe for as long as desired. Time advances only when the player deliberately
turns the next Page. Closing the application leaves the Colony safe at its
current moment.

No Citizen becomes hungry because the player was busy. No project finishes
through idle accumulation. No notification summons the player back.

#### Home as a vertical living illustration

The main screen opens directly onto Home. The central median contains:

- visible shelters and familiar Places;
- moving, individually recognizable Citizens;
- plants changing with the season;
- objects retained from earlier events;
- traces of damage and repair;
- visiting animals;
- memorials and alterations; and
- ordinary activity.

Traffic at the screen edges supplies continual movement, light, sound, wake,
rain, litter, and disturbance. It makes the narrow safety of the center
perceptible without requiring constant emergencies.

The player may slide through the length of Home, pinch closer, or hold on a
location to listen and watch. The same doorway, gathering ground, Garden,
overlook, or patched roof appears repeatedly under different conditions.

#### Invitations rather than tasks

Each Page contains several subtle Invitations. The game does not immediately
list them.

A Citizen may pause near something unfinished. Grass may move where no resident
is visible. Someone may be setting out an extra portion. A familiar object may
be missing. An animal may repeatedly look toward the Road. The soundscape may
reveal something the image does not.

Touching and holding an Invitation opens its moment.

The player may discover several but follow only one before turning the Page:

- help with a part of Home;
- accompany a Citizen;
- welcome or observe a stranger;
- investigate a change;
- spend time within an ordinary routine;
- prepare for something beyond Home; or
- revisit something remembered.

Unchosen Invitations are not failed quests. Some recur, some develop
independently, and some pass. The Colony’s identity emerges partly from what
the player repeatedly chooses to notice.

#### One lasting mark

Most visits culminate in one small, persistent change:

- an object is placed;
- material becomes part of a shelter;
- two Citizens establish a routine;
- a Guest becomes familiar;
- someone learns a capability;
- a wound alters movement;
- a Citizen begins using a different Place;
- an absence becomes recognized; or
- a memory attaches to something visible.

The player sees the change rather than receiving a reward summary. A new strip
of fabric remains on the roof. Two animals begin sitting together at dusk. A
returning Citizen favors one leg. An object changes hands.

Many marks provide no mechanical advantage. They make this Colony increasingly
unlike every other one.

#### Citizens in the hand

Touching a Citizen opens a compact portrait with three layers:

- **Now** — where they are and what presently occupies them;
- **Familiar** — established habits, relationships, objects, and Places; and
- **Remembered** — selected moments that changed how the Colony knows them.

There are no affection bars. Repeated attention does not compel friendship or
manufacture intimacy through a meter. Familiarity grows because the player
recognizes continuity across appearances.

The player may follow different Citizens on different Pages. The Colony
remains the continuing subject; individual Citizens provide the lives through
which it becomes known.

#### Accompanying a Citizen

Some Invitations lead beyond Home. The presentation becomes a sequence of tall
illustrated spaces through which the player moves upward with the Citizen.

A journey is a chain of embodied moments:

- moving beneath wet grass;
- listening beside a Sound Wall;
- waiting under a discarded container;
- encountering another animal;
- deciding whether to continue into unfamiliar ground;
- carrying something awkward; or
- finding a different way back.

The player advances by touch, pause, observation, and occasional directional
choice. The sequence can last several Pages, leaving that Citizen visibly
absent from Home until their return.

#### The phone turns when the world does

Home is held in portrait orientation: a narrow sanctuary between two moving
edges.

When a Citizen attempts a Roadway Crossing, the player rotates the phone into
landscape orientation. The Road suddenly fills the screen.

Traffic passes laterally through image, sound, and haptic vibration. The player
watches for movement, feels approaching weight, and uses a small number of
deliberate gestures to move, shelter, wait, or retreat. The Crossing lasts less
than a minute, but the physical reorientation makes it feel like entering a
different and overwhelming world.

After reaching the opposite Margin or returning Home, the player rotates the
phone upright. The median becomes visible again.

Accessible visual, audio, and simplified-control alternatives preserve the
same dramatic transformation without requiring sound, vibration, precise
timing, or physical rotation.

#### Species transforms the phone

Each Core Species reorganizes the same portrait device.

##### Mouse — joined detail

Mouse Home becomes a dense sequence of linked interiors and adjacent spaces.
The player moves through it by slipping between close views rather than
surveying broad ground. Several Mice are often visible together, and an
accompanied moment may involve a pair whose small differences gradually become
recognizable.

##### Rabbit — open center

Rabbit Home preserves a broad vertical commons through the center of the
screen. Citizens cross one another’s paths visibly and gather in changing
groups. Away movement covers long stretches through fluid upward gestures,
while Crossing emphasizes decisive bursts.

##### Squirrel — vertical connection

Squirrel Home climbs the screen. Bridges, branches, supports, and hanging
Places create several elevations inside the portrait frame. The player follows
connections upward and downward, with the device naturally becoming a view
into the Web.

Species changes what the player’s thumb learns to do and what kind of space
becomes familiar.

#### Quiet Pages

Some Pages contain no consequential Invitation.

The player may watch a meal, follow a Citizen’s ordinary route, listen to rain
under shelter, find animals sleeping in unexpected arrangements, or remain
with the changing sound of evening traffic.

A **Stay** gesture delays the next Page for as long as the player wishes.
Nothing is earned for staying, and nothing is lost by moving on.

Quiet is part of the game’s content rather than an interval between rewards.

#### Illustrated memory

Every lasting mark produces a visual amendment to the Colony or a Citizen’s
current image. At the end of a season, the game assembles selected Pages into
an illustrated vertical Chronicle.

The player can scroll backward through:

- earlier forms of Home;
- arrivals and departures;
- recovered objects;
- relationships becoming visible;
- dangerous Crossings;
- ordinary repeated moments;
- seasonal transformations; and
- Citizens who are no longer present.

The Chronicle is generated from established play. The player does not select
flattering highlights or write captions to prove that something mattered.

Earlier images remain available, but ordinary play always opens on the Colony
as it exists now.

#### Campaign shape

A complete first campaign might contain sixty to one hundred Pages, experienced
whenever the player chooses. It follows one Colony through a year of
settlement, relationships, departures, Guests, weather, and change.

Completion produces a final current portrait and a readable seasonal
Chronicle. The player may continue into another year, close this Colony’s book,
or begin again with another Core Species.

A five-minute visit remains meaningful because it belongs to a history
accumulated over weeks or months of voluntary return.

#### Characteristic visit

The player opens the game after ten days away. No time penalty has accumulated.
Home resumes at a rainy morning Page.

Holding on the Kitchen reveals that its roof is dripping. Holding on a young
Citizen reveals that she is watching a Groundhog Guest preparing to leave.
Holding near the Road reveals a bright piece of waterproof material caught
against the verge.

The player follows the young Citizen and the Groundhog toward it. At the
Roadway, the phone rotates. They wait through the vibration of two passing
trucks, retrieve the material, and return.

Back in portrait view, the player places it over the Kitchen. The Page closes
on the two animals sheltering beneath the newly patched roof while rain
continues along both Roads.

Weeks later, the same blue material remains visible.

#### Product ethic

The game is sold as a complete work. Its return rhythm comes from attachment
rather than pressure:

- no streaks;
- no expiring daily rewards;
- no deterioration during absence;
- no push notification claiming that a Citizen needs help;
- no premium currency;
- no randomized purchases; and
- no payments attached to recovery, survival, or affection.

Optional notifications may announce only a reminder deliberately requested by
the player. The Colony never impersonates emotional distress to compel
engagement.

#### Form-native thesis

The design uses the device itself as part of MEDIAN’s meaning:

- the portrait screen resembles the long, narrow territory of a median;
- the player physically holds Home between two Roads;
- touch encourages attention to small movement and detail;
- rotation lets the Roadway overwhelm the device during Crossing;
- sound and haptics make human traffic physically present;
- brief Pages support a relationship built through recurring voluntary visits;
  and
- the image archive allows a Colony to remain literally carried in the
  player’s pocket.

> **The Colony waits without demanding. The player returns because it has
> become somewhere worth visiting.**

Time advances only through player-advanced Pages. Real-world light or season
may gently recolor presentation, but absence never advances needs, ends
opportunities, or harms Citizens. This protects the difference between
attachment and coercion.

### Manifestation boundary

The four forms above are creative possibilities rather than announced
products, canonical rule translations, or production commitments. The mobile
example demonstrates a method: begin with what MEDIAN makes promising in a
medium, then design an original game around that promise. Any future
Manifestation would earn its own specification only through separate authorial
development and prototyping.

## Appendix K — Market Position and Comparative Landscape

- The Concept Sourcebook's product position and MEDIAN's cumulative
  distinctiveness
- Current neighbors, structural ancestors, creative influences, audience
  intersections, resemblance risks, and positioning language
- Durable comparison separated from a visibly dated and freshly verified
  market-status account

# END MATTER

Bibliography and endnotes, index, credits and colophon, version information,
and the End Plate remain distinct end matter rather than numbered Appendices.
