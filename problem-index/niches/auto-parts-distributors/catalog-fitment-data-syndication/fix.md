# Two Brands, Two Answers for the Same Car

**Niche:** [[niches/auto-parts-distributors/catalog-fitment-data-syndication/profile|Catalog Data Ingestion & Fitment Syndication]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Fix (Pain Point)
**One-liner:** One supplier says its pad fits every trim of a model year, another splits by brake package, and the counter has no way to know which file is right.
**Tags:** #graph-theory #k-nearest-neighbors #bayesian-inference #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to deliver supplier catalog data that resolves each part to the vehicles it fits, and whoever ships the catalog with the fewest fitment returns per thousand lines sold takes the account.

## The Problem
Interchangeable parts from different brands carry different applications for the same vehicles. The distributor syndicates both, so the lookup shows two brands with different coverage, and the counter either trusts the house brand's file or calls the veteran.

## Why It's Still Broken
Each supplier codes its own file; there is no shared reference for "the true application" of a part type on a configuration, and catalog teams merge files without comparing them across brands.

## What a Fix Looks Like
For each configuration and part type, compare applications across all interchangeable brands, flag disagreements, and resolve them with evidence: OE part numbers, interchange tables, the store's fitment returns by brand, and counter overrides. Show the counter a consensus with the disagreement noted, and send each supplier its outliers.

## Who Feels the Pain
Counter staff, catalog teams fielding complaints, and shops that receive the wrong brand's part.

## Impact If Fixed
If cross-brand disagreements were resolved on the ~5,000 highest-volume configuration and part-type pairs (estimate), perhaps a quarter of the multi-candidate lookups that now need a veteran (estimate) would resolve on screen.
