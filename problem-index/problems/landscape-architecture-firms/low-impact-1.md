# Plant Substitution and Submittal Review

**Industry:** [[landscape-architecture-firms|Landscape Architecture Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Submittal tools already route the contractor's paperwork; none of them knows whether a substituted 2-inch-caliper red maple from another nursery meets the planting specification, the design intent and the plant schedule it replaces.
**Tags:** #large-language-models #transformers #word-embeddings #k-nearest-neighbors #evaluation-metrics #workflow-orchestration #automation

## The Problem
Once a landscape project is bid, the contractor sends the landscape architect a stream of submittals: product data for pavers, site furnishings, edging, irrigation heads and controllers; soil and mulch test reports; mockup photos; and, on almost every job, plant substitution requests. The specified species is unavailable in the size listed, or the nursery's stock is a different cultivar, or the contractor proposes a cheaper equivalent. The project landscape architect has to check each request against Section 32 90 00 of the specification, the plant schedule, ANSI Z60.1 sizing for caliper, height and root ball, and the design intent — mature size, form, bloom, hardiness, salt and drought tolerance, and whether the swap upsets a massing pattern across forty other beds.

Each review is small and none is trivial. A rejected substitution delays planting into a hotter month; an approved one that turns out to be wrong for the site becomes the designer's problem at the warranty walk. Reviews are done from the office between design deadlines, from nursery availability sheets that arrive as PDFs, and are logged in an email chain.

## What Already Exists
Procore, Newforma, Autodesk Construction Cloud and Bluebeam Studio route submittals, track due dates and stamp responses; most small firms run the same process by email and a spreadsheet log. Land F/X and Vectorworks hold a plant schedule and a plant database. Plant reference sites and nursery catalogues describe species traits.

## The Customisation Gap
The generic tools move documents; they do not read them. The landscape-specific layer is: parsing nursery availability lists and substitution requests into species, cultivar, size and root-ball condition; checking them against the project's planting specification and ANSI Z60.1 rather than a generic product spec; ranking acceptable substitutes by functional and visual equivalence for the specific location (shade, soil, irrigation zone, mature spread against the spacing drawn); flagging where one substitution changes quantities or cost elsewhere in the schedule; and writing the response with the reason, linked back to the plant schedule so the record set reflects what was actually installed. None of the submittal platforms carries plant trait data, and none of the plant databases knows about submittal workflows.

## Impact If Solved
A plant-aware submittal review cuts a typical substitution response from an afternoon of cross-checking to minutes, keeps planting on schedule, and leaves the firm with an accurate as-built plant record — the input every later question about which specifications survived depends on.
