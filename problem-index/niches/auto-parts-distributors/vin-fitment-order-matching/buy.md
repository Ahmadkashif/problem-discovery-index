# Parts-Identification Models Adapted to the Counter

**Niche:** [[niches/auto-parts-distributors/vin-fitment-order-matching/profile|VIN & Fitment Matching on Shop Orders]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Parts-identification models built for repair estimates already resolve damage into purchasable parts; at the parts counter they must resolve a shop's shorthand into the store's own catalog and stock.
**Tags:** #transformers #contrastive-learning #k-nearest-neighbors #evaluation-metrics #data-integration #ai-agent
**Contested on:** Every serious competitor in this niche is fighting to turn a shop's call, text or e-catalog request into the one part that fits that VIN, and whoever has the lowest fitment-return rate on the shop orders it matches takes the account.

## The Problem
The counter needs a ranked, explained answer on ambiguous lines, inside the store's lookup screen, in seconds.

## What Already Exists
Partly's Interpreter model, trained on 1M+ car models and 1B+ parts by its own description, resolves repair jobs into parts lists for collision shops, workshops and suppliers, and Partly was hiring a Staff/Senior Staff Software Engineer (Austin, posted 2026-08-11) and a Principal Product Engineer, US (Austin, 2026-10-20). E-catalog networks and the chains' catalogs return candidate lists.

## The Customization Gap
At the counter the input is a shop's request, not an estimate; the output must be a part the store or hub stocks, in its brands, at the shop's price; and success is measured in the store's fitment returns. The model needs the distributor's licensed catalog and qualifiers, its stock and brand mix, each shop's preferences, and a hook to log the outcome from the returns desk.

## Target Customer
Chains, warehouse distributors and programme groups; e-catalog networks embedding identification.

## Impact If Solved
If fitment returns on multi-candidate lines fell from ~8% to ~4% (estimate) at a store writing ~150 commercial lines a day, it would avoid ~1–2 wrong-part runs daily, ~$10K a year per store (estimate).
