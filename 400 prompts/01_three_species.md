# Illustration prompt — "The Three Species" · v0.4.2 rev 2

**Changes from rev 1:** the five-field schema was a v0.2 holdover. Speed / Carry / Food move out of the per-column lists into a **shared comparison strip**, because their whole purpose is comparison and they cannot be compared while split across three columns. **Pressures** are added — §4 gives every species failure modes, and a species plate without them is a sales sheet. And the **no-cross-recruitment rule** is added, because it is what makes this plate a decision rather than a bestiary.

Also carried forward from the last generation: the culvert framing the highway, and the flow arrows through the warren, both of which the model invented and both of which are better than what was asked for.

---

## PASS 1 — the prompt

> I'd like a new infographic plate for the MEDIAN game design sourcebook.
>
> **Image Generation Prompt Specification (Landscape — strict 16:9)**
>
> **Core Subject:** A detail-heavy widescreen sourcebook plate presenting the three playable species of the animal colony-builder MEDIAN. The canvas is divided into three equal vertical columns separated by thin hairline rules, above a full-width comparison strip.
>
> **Overall Style & Aesthetic**
>
> - **Visual philosophy:** grounded, warm, stylized realism at animal scale — a naturalist's field sourcebook with a literary survival tone in the spirit of *Watership Down*. Naturalistic anatomy, no cartooning, no oversized human eyes. High focus on micro-texture: real fur, damp earth, root fibre, moss, weathered concrete, wet asphalt.
> - **Color palette:** warm cream paper, sepia and soft black ink, moss and olive green, damp earth brown, weathered concrete grey. Warm and tactile, never grim. No neon, no glowing holograms, no brushed metal, no blueprint-blue chrome.
> - **Annotation layer:** fine ink callout lines and small pale directional arrows drawn *into* the artwork, showing movement and route. These are inked onto the page, never a screen interface.
>
> **Column 1: RABBIT**
> - **Header:** "RABBIT", top center of the column, bold serif.
> - **Blurb:** "Grounded, communal and architectural. Rabbits build downward, and their civilization is a problem of depth and flow — chambers, tunnels, and enough ways out that no alarm ever finds the colony with only one door."
> - **Central visual:** a cutaway of a rabbit warren beneath a grassy highway median at dusk. Below ground, connected chambers, a nursery of young, a dry grass store, and rabbits moving through the tunnels, with **pale ink arrows tracing the circulation routes between chambers and up to the exits.** Above ground, **at least seven clearly separate bolt holes** scattered irregularly across the turf — not in a neat row — and **one further bolt hole far away near the edge of the frame**, well apart from the rest. In the foreground one rabbit hauls a bundle of dried grass down into an entrance while a second sits upright at a different entrance, ears high, watching the road. Trucks pass on wet asphalt behind.
> - **Descriptors:**
>   - `SPATIAL IDENTITY: Burrow — depth and flow`
>   - `SIGNATURE SYSTEM: Warren Flow`
>   - `STRENGTHS: Fast over open ground · Coordinated hauling · Strong rescue`
>   - `PRESSURES: High food demand · Damp and collapse · Crowding at entrances`
>
> **Column 2: SQUIRREL**
> - **Header:** "SQUIRREL", top center of the column, bold serif.
> - **Blurb:** "Mobile, opportunistic and dispersed. Squirrels build upward and outward, trading the convenience of one full storehouse for the resilience of many small ones, scattered where no single raid can take them all."
> - **Central visual:** a layered vertical settlement in a wooded median. Nests high in the trunks, and small bridges of twisted vine and salvaged wire strung between trees and down to a steel highway guardrail. **Five or six small food caches are clearly visible at different heights and must read unmistakably as stores rather than nests** — a handful of acorns wedged in a bark fissure, seeds tucked under a peeling flap of bark, nuts pressed into a knot-hole, a cache in a root hollow at the base — each one small, separate, and obviously deliberate, with **pale ink arrows linking them into a route.** In the foreground a squirrel presses one more acorn into a crevice. The highway runs below with vehicles visible through the trunks.
> - **Descriptors:**
>   - `SPATIAL IDENTITY: Canopy — dispersal and redundancy`
>   - `SIGNATURE SYSTEM: Cache Network`
>   - `STRENGTHS: Vertical mobility · Heaviest hauling · Redundant routes`
>   - `PRESSURES: Exposed infrastructure · Weather damage · Theft and spoilage`
>
> **Column 3: WOOD MOUSE**
> - **Header:** "WOOD MOUSE", top center of the column, bold serif.
> - **Blurb:** "Ingenious, quiet and cooperative. Mice build densely and carry little, dividing every load across short handoffs until many small bodies move what none of them could carry alone. Their expeditions fail by degrees rather than all at once, and they reach pockets of ground no other species can enter — though only ever after the same crossing everyone takes."
> - **Central visual:** the mouth of a concrete culvert, framing a view through to the wet highway and passing vehicles beyond. Around and beneath it, dense micro-infrastructure: many tiny interconnected rooms, root passages and grass tunnels packed into the earth. In the foreground **one mouse passes a seed head to another** at a small worn station, and behind them **a chain of further mice waits along the route**, each ready to take the load the next short stretch, with **pale ink arrows following the relay from station to station.**
> - **Descriptors:**
>   - `SPATIAL IDENTITY: Distributed — density and handoff`
>   - `SIGNATURE SYSTEM: Relay Network`
>   - `STRENGTHS: Cheapest to feed · Stealth and small voids · Unreachable pockets`
>   - `PRESSURES: Low load · Wind shear and fragility · Narrow-route congestion`
>
> **THE COMPARISON STRIP.** Running the full width beneath the three columns, a single bordered panel headed "THE SHARED STAT FRAME — ALL VALUES INTEGER", laid out as a small clean table of three rows and four columns, with column headings "SPECIES", "SPEED", "CARRY", "FOOD":
>
> - `RABBIT · Fastest · 10 · 10`
> - `SQUIRREL · Standard · 20 · 10`
> - `WOOD MOUSE · Standard · 6 · 5`
>
> Beneath the table, one line of italic text across the strip: "One campaign, one species. The core species never cross-recruit — a rabbit colony never takes in squirrels or mice, and never will. Found family lives in the Guest system instead."
>
> **The animals — strict rules.** These animals wear **nothing at all**: no clothing, no cloaks, no belts, no harnesses, no packs, no armor, no weapons of any kind. They are at home, and at home they are simply animals. They sit up on their haunches to work with their forepaws and go on all fours to travel — never standing and walking like small people. **Each column contains only its own species.**
>
> **Compositional framing.** A thin horizontal header bar across the very top of the canvas reads "THE THREE SPECIES" in a clean serif, with smaller text "MEDIAN · PART I · SECTION 4" at the right-hand end. A narrow footer bar across the bottom reads "OBSERVE. PLAN. ADAPT. TEACH THE YOUNG. THE MEDIAN REMEMBERS."
>
> Render every text string exactly as written above, in US spelling, and **do not invent any additional labels, captions, annotations, measurements or version numbers** — unspecified text becomes unreadable gibberish, so leave un-named anything I have not named.
>
> **Do not include:** any human figure or body part · brushed metal, rivets, screws, blueprint grids, reticles or HUD chrome · glowing screens, wires, solar panels, sensors or electronics · swords, spears, shields, bows or armor · animals dressed as people · rats · dimension figures or measurements · version stamps.

---

## PASS 2 — the strip, for a PowerPoint base

Note the tightened wording. The previous strip deleted the header and blurb zones and let the illustrations expand upward into them, which destroyed the type positions.

> Produce the same plate with all text removed. **Preserve the exact position and size of every panel, border, rule and text block — including the now-empty header bar, the three column headings, the three narrative blurb areas, the descriptor panels, the comparison strip and the footer bar. Do not expand, re-crop, re-compose or enlarge any illustration into space vacated by removed text.** Keep the ruled lines where text sat. Maintain the exact 16:9 aspect ratio.

---

## Checks on the returned image

- **Count the rabbit's bolt holes.** Seven or more, irregularly placed, plus one far off near the frame edge. This is the single detail carrying Warren Flow's readable signature; three or four looks fine and means nothing.
- **Do the squirrel's caches read as food stores** rather than as nest cavities? If they read as holes, the plate does not say what it needs to say.
- **Stats:** Rabbit Fastest / 10 / 10. Squirrel Standard / 20 / 10. Wood Mouse Standard / 6 / 5. The v0.2 material had these close to inverted.
- **Any upscale or re-render pass gets this same check again.** A "4K clarity" pass re-generates rather than upscales, and the last one quietly reduced the rabbit's bolt holes.
