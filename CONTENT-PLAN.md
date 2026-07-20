# Volkman Farm Blog Content Plan

This file is the editorial calendar for `/blog/`. The `/blog-post` slash command reads it,
scaffolds the next unwritten post, and marks the row done. Do not delete rows; flip
`[ ]` to `[x] <filename>` when a post is drafted.

## Content focus

Three subjects, in this priority order:

1. **Microgreens**. The business. Varieties, kitchen uses, growing methods, delivery.
   This is the SEO engine; these posts link to /greens/, /order/, /delivery/, /restaurants/.
2. **Homesteading**. The honest journal of a family building out a backyard homestead
   in Sanford, FL. Early days, real progress, real failures.
3. **Permaculture**. Design principles applied to a Central Florida yard: sand soil,
   summer heat, rain patterns, closing loops between the microgreens shed and the garden.

## Voice and guardrails (non-negotiable)

- Plain, concrete, neighborly. First person plural ("we"). Short sentences.
- **No em-dashes.** Use periods, commas, or colons.
- **No post-harvest adulteration claims.** FL regulations prohibit washing, rinsing, or
  processing the product. Never imply we wash, rinse, trim, or treat greens after harvest.
  Equipment and tray cleaning is fine to mention; the product is not touched after cutting.
  The flip side, added 2026-07-18: our clamshell label says **wash before using**. Washing
  is the customer's step, and copy should state it that way, not offer it as a preference.
  Never write "if you like to rinse" or similar. When storage comes up, the order is store
  dry, wash the portion at the plate.
- **No gator, German, or Bavarian references.** That identity was retired.
- **No medical claims.** Nutrition facts with hedged verbs only: "carries", "is high in",
  "research suggests". Never "cures", "prevents", "treats".
- **Kids: no names, no ages, no faces.** Birth-order and role references are allowed
  ("our oldest daughter manages the food forest"). Decided 2026-07-08.
- **Only claim what is real.** The homestead is early-stage. If a topic touches something
  that may not exist yet (animals, structures, plantings), ask Albert before drafting or
  frame it explicitly as a plan.
- Facts you may use freely: five Volkmans in Sanford; Albert built the grow shed; the
  kids help pack; ten varieties at $3.50/oz; nine delivery neighborhoods on three routes;
  organic non-GMO seed; filtered water; wholesale for chefs; subscribe-and-save 10%.
- Delivery facts: greens go out in 64 oz clamshells, carried in an insulated cooler bag
  in transit to hold freshness; the clamshell is left on the porch, the cooler bag is not.
  The three routes fit the family calendar: Friday morning through Seminole County (home
  base); Monday and Wednesday evenings through north Orlando because those are taekwondo
  and rock climbing nights; Sunday afternoon downtown because church is in Parramore.
- Property facts (added 2026-07-16, from the parcel GIS in ~/openclaw/memory/homestead/):
  the lot is 2.17 acres in Sanford (county cadastral, 94,418 sq ft), zoned A-1
  (agricultural). It is not a small suburban yard; do not describe it as one. Soils are
  poorly drained fine sands with one very-poorly-drained depressional wet pocket; FEMA
  Zone X (minimal flood hazard). Planting rule from the LiDAR contours: trees and mounds
  on the higher ground, water-tolerant plants in the lows. Never publish the street
  address, the septic locations, or details about structures beyond the grow shed.
- Homestead facts (updated 2026-07-16): besides the fixed chicken run there is a moving
  chicken tractor; its year-old parked mulch piles become garden beds (our oldest
  daughter's second bed started as one). A sunn hemp food plot is already planted on the front
  three-quarter acre (seeded spring 2026, flowering by late June), with a new seed mix
  planned next. The chickens and mulch piles are in the backyard. A well and a rainwater cistern are planned, not built:
  frame both as plans.
- Homestead facts (updated 2026-07-08): chickens in a run out back. Spent tray material
  (soil, roots, cut leftovers) goes to the chickens, not a compost pile. A compost bin
  inside the run takes what chickens cannot eat; black soldier fly larvae eat the scraps,
  climb out when they pupate, and the chickens eat them. Mulch piles decomposed for a
  year, then were planted as food-forest mounds: lemon, 2 mangoes, 2 blueberries, banana,
  pineapple, sweet potatoes, Seminole pumpkin, okra, butterfly peas, sunflower, basil,
  shampoo ginger.
- Continuity: before drafting, skim the most recent posts. Refer back to and build on
  earlier posts when relevant (link them). When a fact evolves past what an old post
  said, say so plainly in the new post rather than pretending the old one never existed.
- Length follows the topic, it is not a fixed band. Many posts land 500-800 words, but a
  short observation or reader question can run 250-400 and a real walkthrough can push
  past 900. Vary it on purpose so the blog does not read formulaic; do not pad or trim to
  a number. Register varies by pillar too: growing notes and variety spotlights can be
  tight and structured, while homestead journal and permaculture posts should read looser,
  like a homesteader writing at the kitchen table. Subheads only where the post turns, not
  on a set cadence. One CTA per post, max. Every post internally links at least one site
  page (variety, city, order, subscribe, or restaurants).
- Every post ships with a hero image: a flat line-art SVG in the site palette at
  `assets/blog/<slug>.svg` plus a 1200x630 PNG social card. The /blog-post command
  covers the how.

## Weekly pillar rotation

| Day | Pillar | Focus |
|---|---|---|
| Mon | Variety spotlight | Microgreens |
| Tue | In the kitchen | Microgreens |
| Wed | Homestead journal | Homesteading |
| Thu | Permaculture in practice | Permaculture |
| Fri | On the route | Microgreens / community |
| Sat | Growing notes | Microgreens / homesteading crossover |
| Sun | Reader questions | Any focus, FAQ style |

Note (2026-07-18): the Friday Jul 17 "On the route" post was pulled to the backlog and
every row from Jul 18 on moved up one day. The rotation above no longer lines up with
the weekday column; pillars now sit one weekday earlier than the table says. Treat the
table as the intended cadence and the calendar rows as the truth. Re-align by dropping a
backlog post into an open slot when one comes up.

## Backlog

Written or planned posts with no date yet. Slot them in when a gap opens. Drafts live in
`drafts/`, which Eleventy skips: no page is built and they stay off the blog index. To
publish one, give it a calendar row above, set the date in its frontmatter, and move the
file back into `posts/`.

| Pillar | Working title | Angle | Status |
|---|---|---|---|
| On the route | A Friday morning, hour by hour | Harvest at sunrise, packing line, Sanford to Oviedo. Drafted and illustrated, never dated. Wants a Friday slot. | drafted, drafts/a-friday-morning-hour-by-hour.md |
| Growing notes | Water: why filtered matters | Chlorine, tender roots, consistency. Displaced from Fri Aug 7 on 2026-07-20 to make room for the amaranth follow-up, which is date-sensitive. Not written yet; slot it into the next open Growing notes row. | not drafted |

## Arcs

- **Arc 1 · Meet the greens and the ground** (Jul 7 - Aug 1). Baselines. Introduce the
  varieties, the shed, the yard as it actually is, and permaculture in plain language.
- **Arc 2 · Florida summer** (Aug 2 - Sep 5). Surviving the heat. Summer kitchen ideas,
  cover crops, water and shade design, school lunches when August starts.
- **Arc 3 · The fall setup** (Sep 6 - Oct 3). Central Florida's real planting season.
  Fall garden build-out, food forest groundwork, route stories, holiday lead-in.

---

## Calendar

### Week 1 · Jul 7-12 · Arc 1

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Tue Jul 7 | Homestead journal | Field notes from a Sanford backyard | Launch post. Why we're writing: greens, homestead, permaculture. Set the promise. | [x] posts/field-notes-from-a-sanford-backyard.md |
| Wed Jul 8 | Homestead journal | The shed Albert built | Tour of the grow shed: shelves, lights, trays. What it replaced and what it costs to run. | [x] posts/the-shed-albert-built.md |
| Thu Jul 9 | Permaculture | Permaculture without the jargon | What it means in one sentence: work with the yard you have. What we're applying here. | [x] posts/permaculture-without-the-jargon.md |
| Fri Jul 10 | On the route | Why we deliver to porches, not pickup lots | The route model. Link the nine neighborhoods. | [x] posts/why-we-deliver-to-porches.md |
| Sat Jul 11 | Growing notes | Seed to tray: how a crop starts | Seeding day walkthrough. Organic non-GMO seed, filtered water. | [x] posts/seed-to-tray-how-a-crop-starts.md |
| Sun Jul 12 | Reader questions | Are microgreens just sprouts? | No. Explain the difference: soil, light, harvest stage. | [x] posts/are-microgreens-just-sprouts.md |

### Week 2 · Jul 13-18 · Arc 1

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Mon Jul 13 | Variety spotlight | Pea tendrils, the gateway green | Sweet, crunchy, kid-friendly. Link /greens/pea/. | [x] posts/pea-tendrils-the-gateway-green.md |
| Tue Jul 14 | In the kitchen | Microgreens on eggs, three ways | Scrambled, omelet, fried. Which varieties hold up to heat. | [x] posts/microgreens-on-eggs-three-ways.md |
| Wed Jul 15 | Homestead journal | Mapping the yard before touching it | Observation first. Sun, shade, wet spots. What we noticed. | [x] posts/mapping-the-yard-before-touching-it.md |
| Thu Jul 16 | Permaculture | Zones for a suburban lot | Zone 0-5 scaled to 2.17 acres. Where the shed sits in the map. | [x] posts/zones-for-2-17-acres.md |
| Fri Jul 17 | Growing notes | The blackout phase | Why trays spend days in the dark. Germination basics. | [x] posts/the-blackout-phase.md |
| Sat Jul 18 | Reader questions | How long do microgreens last? | Honest shelf-life talk. Cut the morning of delivery, refrigerate at home. | [x] posts/how-long-do-microgreens-last.md |

### Week 3 · Jul 19-25 · Arc 1

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Jul 19 | Variety spotlight | Beet greens, the pretty ones | Color, earthiness, plating. The weekly standing wholesale crop. Link /greens/beet/. Swapped forward from Aug 9 on 2026-07-19. | [x] posts/beet-greens-the-pretty-ones.md |
| Mon Jul 20 | In the kitchen | Taco night needs a crunch | Radish and cilantro micros on tacos. Weeknight framing. | [x] posts/taco-night-needs-a-crunch.md |
| Tue Jul 21 | Homestead journal | What Florida sand taught us in week one | Soil reality check. Why "just plant a garden" fails here. | [ ] |
| Wed Jul 22 | Permaculture | Sand favors ants. We are building for worms. | The soil-biology angle on mulch. Bare Florida sand runs hot and dry, which suits ants; the worms we want need cool, moist, loamy ground. Native organic matter is often under 1% and burns off fast in the heat, and low CEC lets nutrients leach before they stabilize. A 3-4 inch mulch layer is the lever: roughly 20F cooler at the surface in summer, holds moisture, feeds decomposers, and slowly tips the yard from ant territory toward worm territory. Builds on Jul 9. Link /greens/. | [ ] |
| Thu Jul 23 | On the route | The text before the drop | How the delivery texting workflow works and why. | [ ] |
| Fri Jul 24 | Growing notes | Harvest morning timeline | Sunrise to porch in hours. What "cut this morning" actually means. | [ ] |
| Sat Jul 25 | Reader questions | Do you deliver to my street? | Route logic, how neighborhoods get added. Link /delivery/. | [ ] |

### Week 4 · Jul 26 - Aug 1 · Arc 1

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Jul 26 | Variety spotlight | Broccoli micros do the heavy lifting | Mild flavor, sulforaphane story with hedged verbs. Link /greens/broccoli/. | [ ] |
| Mon Jul 27 | In the kitchen | The smoothie you won't taste | Hiding broccoli micros in smoothies for kids. | [ ] |
| Tue Jul 28 | Homestead journal | The chickens run the compost | The run, the bin, what goes in, what the flock does with it. Builds on the Jul 9 post. | [ ] |
| Wed Jul 29 | Permaculture | The bug factory we didn't build | Black soldier flies in depth: how the larvae self-harvest and why that loop matters. | [ ] |
| Thu Jul 30 | On the route | What $3.50 an ounce pays for | Transparent cost breakdown. Seed, light, labor, gas. | [ ] |
| Fri Jul 31 | Growing notes | Keeping a grow shed cool in a Florida July | Heat management honestly told. | [ ] |
| Sat Aug 1 | Reader questions | Why aren't you USDA Organic certified? | Organic seed, clean inputs, certification economics for a small farm. | [ ] |

### Week 5 · Aug 2-8 · Arc 2

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Aug 2 | Variety spotlight | Arugula before it gets bitter | Micro arugula vs mature. Link /greens/arugula/. | [ ] |
| Mon Aug 3 | In the kitchen | Summer salads that don't wilt by noon | Building lunch salads with sturdy micros. | [ ] |
| Tue Aug 4 | Homestead journal | August plans, written in pencil | What we're planning for fall while it's too hot to plant. | [ ] |
| Wed Aug 5 | Permaculture | Cover crops: the summer garden that feeds the fall one | Sunn hemp, cowpeas, what we're trying. | [ ] |
| Thu Aug 6 | On the route | Meet Lake Mary and Sanford | First neighborhoods profile. Link both city pages. | [ ] |
| Fri Aug 7 | Growing notes | Did the amaranth work? | Follow-up owed to readers. The Jul 19 beet post promised a straight answer on the amaranth tray started that week, including if it failed. Report what actually happened: did it hold color, did it dodge the mold problem, is it staying or not. Do not write this one until Albert says how the tray turned out. Never claim a result to fill the slot. Amaranth is not one of the ten varieties and has no /greens/ page, so link /greens/beet/ or /restaurants/, not amaranth. Builds on Jul 19. | [ ] |
| Sat Aug 8 | Reader questions | Can I grow microgreens at home? | Generous honest answer: yes, here's the starter version. | [ ] |

### Week 6 · Aug 9-15 · Arc 2

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Aug 9 | Variety spotlight | Radish: the one with opinions | Peppery heat, fast grower. Link /greens/radish/. Swapped back from Jul 19 on 2026-07-19; draft and hero already written. | [ ] drafted, drafts/radish-the-one-with-opinions.md |
| Mon Aug 10 | In the kitchen | School lunches with a secret | Back-to-school week. Micros in wraps and lunchboxes. | [ ] |
| Tue Aug 11 | Homestead journal | The rain we get and the rain we lose | Watching August storms run off. Observation notes. | [ ] |
| Wed Aug 12 | Permaculture | Catching water where it falls | Swales, mulch basins, rain barrels: what fits a suburban lot. | [ ] |
| Thu Aug 13 | On the route | Meet Winter Springs and Oviedo | Second neighborhoods profile. Link both city pages. | [ ] |
| Fri Aug 14 | Growing notes | Tray sanitation between crops | Clean equipment, healthy crops. (Equipment only, never the product.) | [ ] |
| Sat Aug 15 | Reader questions | What do I do when the bag lands on my porch? | Handling at home, refrigeration, eating window. | [ ] |

### Week 7 · Aug 16-22 · Arc 2

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Aug 16 | Variety spotlight | Cilantro micros for people who swear they hate cilantro | Milder than the herb. Link /greens/cilantro/. | [ ] |
| Mon Aug 17 | In the kitchen | Grain bowls, assembled not cooked | No-stove August dinners with micros on top. | [ ] |
| Tue Aug 18 | Homestead journal | What died in July | Failure post. Honesty builds trust. | [ ] |
| Wed Aug 19 | Permaculture | Shade is an asset, not a problem | Reading shade patterns, planting into them. | [ ] |
| Thu Aug 20 | On the route | Meet Casselberry, Maitland, Winter Park | Third neighborhoods profile. Link city pages. | [ ] |
| Fri Aug 21 | Growing notes | Light schedules in the shed | Hours, spectrum, what tender greens want. | [ ] |
| Sat Aug 22 | Reader questions | Are microgreens safe for kids and pets? | Common-sense answer, hedged, no medical claims. | [ ] |

### Week 8 · Aug 23-29 · Arc 2

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Aug 23 | Variety spotlight | Kale you don't have to massage | Micro kale vs the tough stuff. Link /greens/kale/. | [ ] |
| Mon Aug 24 | In the kitchen | Pasta finishing: greens at the last second | Heat-off technique, which varieties. | [ ] |
| Tue Aug 25 | Homestead journal | Cover crop check-in | What's growing, what the soil looks like under it. | [ ] |
| Wed Aug 26 | Permaculture | Mulch: the cheapest tool we have | The practical how-to: where to source it, how deep (3-4 inches), and how often to replenish in Florida heat. Pairs with the Jul 23 soil-biology post; keep this one hands-on, not theory. | [ ] |
| Thu Aug 27 | On the route | Meet College Park and Downtown Orlando | Fourth neighborhoods profile. Link city pages. | [ ] |
| Fri Aug 28 | Growing notes | Troubleshooting: when a tray goes wrong | Damping off, uneven germination, what we do. | [ ] |
| Sat Aug 29 | Reader questions | Can I freeze microgreens? | Honest no for most uses, plus what works instead. | [ ] |

### Week 9 · Aug 30 - Sep 5 · Arc 2

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Aug 30 | Variety spotlight | Kohlrabi, the sleeper hit | Mild brassica crunch nobody expects. Link /greens/kohlrabi/. | [ ] |
| Mon Aug 31 | In the kitchen | Sandwiches that earn the name | Deli upgrade: micros instead of tired lettuce. | [ ] |
| Tue Sep 1 | Homestead journal | Sketching the fall garden | Beds, spacing, what a Florida fall garden can actually grow. | [ ] |
| Wed Sep 2 | Permaculture | Guilds: plants that work in teams | Companion planting framed as permaculture. FL examples. | [ ] |
| Thu Sep 3 | On the route | Why we stay small on purpose | Route capacity, quality, the anti-scale argument. | [ ] |
| Fri Sep 4 | Growing notes | Seed sourcing: who we buy from and why | Organic non-GMO suppliers, what we look for. | [ ] |
| Sat Sep 5 | Reader questions | Subscribe and save: how the 10% works | Standing orders explained. Link /subscribe/. | [ ] |

### Week 10 · Sep 6-12 · Arc 3

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Sep 6 | Variety spotlight | Mustard brings the heat | Wasabi-adjacent kick. Link /greens/mustard/. | [ ] |
| Mon Sep 7 | In the kitchen | Soups get their finish | First soup nights of fall. Garnish that matters. | [ ] |
| Tue Sep 8 | Homestead journal | Fall is Florida's spring | Cutting cover crops, prepping beds. The season flips. | [ ] |
| Wed Sep 9 | Permaculture | Chop and drop | Turning cover crops into mulch in place. | [ ] |
| Thu Sep 10 | On the route | The chefs on the route | Wholesale side of the farm. Link /restaurants/. | [ ] |
| Fri Sep 11 | Growing notes | Scaling trays for restaurant orders | Same shed, larger trays. Wholesale operations. | [ ] |
| Sat Sep 12 | Reader questions | What's the difference between your greens and the grocery store's? | Age, distance, handling. Core pitch as FAQ. | [ ] |

### Week 11 · Sep 13-19 · Arc 3

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Sep 13 | Variety spotlight | Swiss chard, stained glass edition | Color story, mild flavor. Link /greens/chard/. | [ ] |
| Mon Sep 14 | In the kitchen | Avocado toast, but make it yours | The obvious pairing done well. | [ ] |
| Tue Sep 15 | Homestead journal | Planting week | What went in the ground. Photos-first post. | [ ] |
| Wed Sep 16 | Permaculture | The food forest question | Layers explained. What we'd plant first in Central FL and why. | [ ] |
| Thu Sep 17 | On the route | Rain days and route days | What weather does to a delivery morning. | [ ] |
| Fri Sep 18 | Growing notes | Yield math: what one tray produces | Ounces per tray, per variety. Transparent numbers. | [ ] |
| Sat Sep 19 | Reader questions | Can I gift a delivery? | Gift orders, how to set one up. Link /order/. | [ ] |

### Week 12 · Sep 20-26 · Arc 3

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Sep 20 | Variety spotlight | Building a house blend | Mixing varieties: heat, crunch, color. Links several /greens/ pages. | [ ] |
| Mon Sep 21 | In the kitchen | Flatbreads and pizza night | Post-oven greens application. | [ ] |
| Tue Sep 22 | Homestead journal | Mulch day | Covering the new beds. Sweaty, satisfying, cheap. | [ ] |
| Wed Sep 23 | Permaculture | Natives and edibles, side by side | Florida native plants pulling weight in a food system. | [ ] |
| Thu Sep 24 | On the route | The neighbors we've met | Community stories from a season of porches (with permission). | [ ] |
| Fri Sep 25 | Growing notes | A day of jobs: who does what | Family operations. Kids pack, someone seeds, someone drives. | [ ] |
| Sat Sep 26 | Reader questions | Do restaurants really care about microgreens? | Chef perspective, plating, wholesale case. Link /restaurants/. | [ ] |

### Week 13 · Sep 27 - Oct 3 · Arc 3

| Date | Pillar | Working title | Angle | Status |
|---|---|---|---|---|
| Sun Sep 27 | Variety spotlight | Which green fits your kitchen? | Decision-guide roundup of all ten. Link /greens/. | [ ] |
| Mon Sep 28 | In the kitchen | The tailgate board | Fall gatherings, greens on the snack table. | [ ] |
| Tue Sep 29 | Homestead journal | Ninety days in: taking stock | Retrospective. What worked, what we'd redo. | [ ] |
| Wed Sep 30 | Permaculture | What we're designing for next year | Forward look. Water, trees, maybe animals. Plans framed as plans. | [ ] |
| Thu Oct 1 | On the route | Holiday season is coming to the route | Early holiday framing, standing orders before the rush. Link /subscribe/. | [ ] |
| Fri Oct 2 | Growing notes | The shed in October | Season shift inside the grow room. | [ ] |
| Sat Oct 3 | Reader questions | What should we write about next? | Ask readers. Collect topics for the next quarter's plan. | [ ] |

---

## After Oct 4

Run a planning session: review which pillars got traction (GA4), ask readers (the Oct 4
post), and draft the next quarter's calendar in this same format.
