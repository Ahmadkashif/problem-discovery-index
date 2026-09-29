# Warehouse Batching Practice

**Niche:** [[niches/live-commerce-platforms/post-show-fulfilment/profile|Post-Show Fulfilment]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Batch picking, order consolidation and cartonisation are mature warehouse disciplines, and a live seller packs three hundred orders off a kitchen table with none of them.
**Tags:** #dynamic-programming #convex-optimization #workflow-orchestration #automation #evaluation-metrics #optimization-fundamentals #revenue-impact #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to get a show's worth of one-off orders packed, combined and shipped without the host doing it by hand at midnight — and whoever does that determines how many shows a seller can run.

## The Problem
Warehouse management has thoroughly solved the problem of turning many small orders into an efficient sequence of physical actions: batch and zone picking, pick path optimisation, order consolidation, cartonisation, and rate shopping across carriers. The methods are well understood and the software is mature. It is all built for a facility with locations, a catalogue and staff. A live seller has hundreds of orders, no locations, no catalogue and one person, and therefore uses none of it.

## What Already Exists
Warehouse management with batch and wave picking; pick path optimisation; order consolidation and multi-order packing; cartonisation and dimensional weight optimisation; and multi-carrier rate shopping with batch label generation.

## The Customization Gap
The adaptation is from a facility to a room. It requires: (1) no stock-keeping units and no locations, so the sequencing must be derived from the stream timeline rather than from a bin map — this is the substitution that makes the whole body of practice usable and is what nobody has attempted; (2) consolidation across a time window rather than at order placement, because buyers keep buying through the show and after it; (3) cartonisation from an image and a spoken description rather than from catalogued dimensions, which is an estimation problem the warehouse stack never had; (4) a single operator doing pick, pack and ship in one pass, which collapses the role separation every warehouse system assumes; and (5) rate shopping pooled across many small sellers to reach negotiated pricing, since the individual volumes are far below any threshold.

## Target Customer
Live sellers and small consignment operations, live commerce platforms, and warehouse software vendors for whom the catalogue-free micro-seller is unserved.

## Impact If Solved
Deriving pick sequence from the stream timeline substitutes for the bin map warehouse practice requires, which is what makes the mature methods usable at all. Pooled rate shopping gives sellers pricing their individual volume could never reach.
