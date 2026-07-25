> ## ⚠ SUPERSEDED — do not use
> Replaced by `PROMPT_03_Three_Species_v042_rev2.md`.
> **Kept for the record.** This version worked and produced a good plate, but carried a v0.2 holdover: a five-field descriptor schema that put Speed, Carry and Food in per-column lists, where they cannot be compared. Rev 2 moves them to a shared comparison strip, adds Pressures, and adds the no-cross-recruitment rule.

# Illustration prompt — "The Three Species" · v0.4.2

**Plate:** The Three Species (Part I, §4) · 16:9 landscape
**Method:** two-pass. Run Pass 1 for a finished, text-bearing plate. Run Pass 2 to reskin if needed. Then ask the same tool to strip all text, keeping panels, rules, icons and diagrams — that stripped version is the base plate for PowerPoint.
**Why text is specified exactly:** generated text garbles only where the prompt leaves it to invention. Every string below is given verbatim so the layout is sized for the real copy before it is stripped.

---

## PASS 1 — the prompt

> I'd like a new infographic plate for the MEDIAN game design sourcebook.
>
> **Image Generation Prompt Specification (Landscape — 16:9)**
>
> **Core Subject:** A detail-heavy widescreen sourcebook plate presenting the three playable species of the animal colony-builder MEDIAN. The 16:9 canvas is divided into three equal vertical columns separated by thin hairline rules.
>
> **Overall Style & Aesthetic**
>
> - **Visual philosophy:** grounded, warm, stylized realism at animal scale — a naturalist's field sourcebook with a literary survival tone in the spirit of *Watership Down*. Naturalistic anatomy, no cartooning, no oversized human eyes. High focus on micro-texture: real fur, damp earth, root fibre, moss, weathered concrete, rusted steel, wet asphalt.
> - **Colour palette:** warm cream paper, sepia and soft black ink, moss and olive green, damp earth brown, weathered concrete grey, with a single restrained accent of deep sign-green. Warm and tactile, never grim. Absolutely no neon, no glowing holograms, no brushed metal, no blueprint-blue technical chrome.
> - **Interface layer:** over the artwork sit clean, razor-thin muted vector callout lines and small technical labels, integrated as if inked onto the page — never as a screen interface or HUD.
>
> **Column-by-Column Layout**
>
> **COLUMN 1: RABBIT**
> - **Header:** the single word "RABBIT" at the top centre of the column, in a bold serif face.
> - **Narrative blurb**, centred beneath the header: "Grounded, communal and architectural. Rabbits build downward, and their civilisation is a problem of depth and flow — chambers, tunnels, and enough ways out that no alarm ever finds the colony with only one door."
> - **Central visual:** a cutaway of a rabbit warren beneath a grassy highway median at dusk. Below ground: connected chambers, a nursery, a dry food store, rabbits moving through the tunnels. Above ground: **six or more separate bolt holes** dotted across the turf, with one further hole visible far off at the edge of the frame. In the foreground one rabbit hauls a bundle of dried grass down into an entrance while a second sits upright at a different entrance, ears high, watching the road. Trucks pass on wet asphalt in the background.
> - **Technical descriptors**, in small crisp callouts along thin vector lines mapping the tunnel network:
>   - `SPATIAL IDENTITY: Burrow — depth and flow`
>   - `SIGNATURE SYSTEM: Warren Flow`
>   - `SPEED: Fastest`
>   - `CARRY CAPACITY: 10`
>   - `FOOD CONSUMPTION: 10`
>
> **COLUMN 2: SQUIRREL**
> - **Header:** the single word "SQUIRREL" at the top centre of the column, in a bold serif face.
> - **Narrative blurb:** "Mobile, opportunistic and dispersed. Squirrels build upward and outward, trading the convenience of one full storehouse for the resilience of many small ones, scattered where no single raid can take them all."
> - **Central visual:** a layered vertical settlement in a wooded median. Nests high in the trunks, small bridges of twisted vine and salvaged wire strung between trees and down to a steel highway guardrail. In the foreground a squirrel presses an acorn into a bark crevice, and **three or four other small caches are visible at different heights** — in a fork, under a root, behind loose bark — deliberately scattered, never one central store. The highway runs below, vehicles visible through the trunks.
> - **Technical descriptors**, along arc-based vector lines tracing the canopy routes:
>   - `SPATIAL IDENTITY: Canopy — dispersal and redundancy`
>   - `SIGNATURE SYSTEM: Cache Network`
>   - `SPEED: Standard`
>   - `CARRY CAPACITY: 20`
>   - `FOOD CONSUMPTION: 10`
>
> **COLUMN 3: WOOD MOUSE**
> - **Header:** the two words "WOOD MOUSE" at the top centre of the column, in a bold serif face.
> - **Narrative blurb:** "Ingenious, quiet and cooperative. Mice build densely and carry little, dividing every load across short handoffs until many small bodies move what no one of them could carry alone."
> - **Central visual:** dense micro-infrastructure at the mouth of a concrete culvert. Many tiny interconnected rooms, root passages and grass tunnels packed into the earth. In the foreground **one mouse passes a seed head to another** at a small worn station, and behind them a **chain of further mice stands along the route**, each waiting to take the load the next short stretch. The highway and passing vehicles are visible beyond the culvert.
> - **Technical descriptors**, along fine vector lines mapping the relay route and its stations:
>   - `SPATIAL IDENTITY: Distributed — density and handoff`
>   - `SIGNATURE SYSTEM: Relay Network`
>   - `SPEED: Standard`
>   - `CARRY CAPACITY: 6`
>   - `FOOD CONSUMPTION: 5`
>
> **The animals — strict rules.** These animals wear **nothing at all**: no clothing, no cloaks, no belts, no harnesses, no packs, no armour, and no weapons of any kind. They are at home, and at home they are simply animals. They sit up on their haunches to work with their forepaws and go on all fours to travel — never standing and walking like small people. **Each column contains only its own species.**
>
> **Compositional framing.** A thin horizontal header bar runs across the very top of the canvas carrying the text "THE THREE SPECIES" in a clean serif face, with the smaller text "MEDIAN · PART I · SECTION 4" set at the right-hand end. Beneath each column's illustration, a bordered cream panel holds that column's five technical descriptors as a neat aligned list. A narrow footer bar runs across the bottom of the canvas carrying the text "OBSERVE. PLAN. ADAPT. TEACH THE YOUNG. THE MEDIAN REMEMBERS."
>
> Render every text string exactly as written above, and **do not invent any additional labels, captions or annotations** — unspecified text becomes unreadable gibberish, so leave un-named anything I have not named.
>
> **Do not include:** any human figure or body part · brushed metal, rivets, screws, blueprint grids, targeting reticles or HUD chrome · glowing screens, wires, solar panels, sensors or any electronics · swords, spears, shields, bows or armour · animals dressed as people · rats · version stamps · measurements in millimetres or any dimension figures.

---

## PASS 2 — if the reskin is needed

> Redo with a warmer naturalist sourcebook feel — cream paper, botanical restraint, inked linework — and no industrial or military styling.

---

## PASS 3 — the strip

> Now produce the same plate with **all text removed**. Keep every illustration, panel border, hairline rule, icon and callout line exactly as it is, and keep the ruled lines where the text sat, so the layout still reads. Leave every text area completely blank.

---

## Notes

**What changed from the v0.2 prompt.** The stat assignments were inverted against canon — §4.1 makes the rabbit *fastest*, the squirrel the *best* carrier at 20, and the mouse cheapest to feed at 5. Pheromone routing is rejected by name (§4.4, Decision 8). "Bypasses ground-level traffic entirely" violates the no-bypass rule — every species engages the crossing. Version stamps and millimetre dimensions are both out.

**What was kept.** The five-field parallel schema, which is what makes three pictures read as one system. And the notched-ear idea from the v0.2 rabbit is worth reviving later on a Character Record plate — it is a Maiming rendered as character, exactly the Pillar 2.5 image the artwork list wants.

**Each central visual specifies an action**, not an inventory: a rabbit hauling while another watches from a second hole, a squirrel adding to the fourth of several caches, a mouse handing a load along a chain. The signature systems are shown as behaviour rather than diagrammed.
