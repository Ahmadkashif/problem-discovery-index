# Piece-to-Assay Reconciliation for Every Scrap Lot

**Niche:** [[niches/pawnshops/scrap-precious-metal-settlement/profile|Scrap Precious-Metal Lots & Refiner Settlement]]
**Industry:** [[industries/pawnshops|Pawnshops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A pawnshop tests every piece before it goes in the scrap lot, records almost none of it, and so cannot tell whether a short assay came from its own sorting or the refiner.
**Tags:** #random-forests #bayesian-inference #hypothesis-testing #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to settle a pawnbroker's scrap gold and silver lots for the most metal at the best moment — accurate karat sorting before shipment, an assay the shop can check, and timing against spot — and whoever closes the gap between the shop's estimate and the refiner's settlement takes the account.

## The Problem
A 14k lot is expected to assay near 58.5% gold. It comes back at 55%. One mis-sorted 10k chain, a heavy plated piece, solder and stones left in, or a refiner's error could explain it, and the shop has no way to tell which.

## Why Nobody Has Built This
Piece-level testing results are never captured in a structured form; refiners report only the lot; and the shop sees the settlement weeks after the sorting.

## What to Build
Log every scrap piece with weight, stamp photograph, tests and assigned karat; compute expected fine weight per lot with an uncertainty band; reconcile against the refiner's assay; and learn, over many lots, each buyer's and each karat band's bias, so systematic errors are found and a refiner whose assays run consistently low is identified with evidence.

## Target Customer
Jewellery directors at chains; high-volume independent gold buyers.

## Impact If Built
Settlement gaps become explainable, sorting improves where it is weak, and the shop can negotiate with its refiner on data.
