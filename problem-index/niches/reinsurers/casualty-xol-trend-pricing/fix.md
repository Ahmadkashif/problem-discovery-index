# Large-Loss Listings Re-Keyed Every Renewal

**Niche:** [[niches/reinsurers/casualty-xol-trend-pricing/profile|Casualty Excess-of-Loss Trend & Development Pricing]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Fix (Pain Point)
**One-liner:** Every renewal a pricing analyst rebuilds each cedent's large-loss history from a new spreadsheet, matching claims to last year's by hand.
**Tags:** #large-language-models #k-nearest-neighbors #feature-engineering #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to put trend and development selections on long-tail excess layers that survive the next several years of ceded development, and whoever's selections still hold when the adverse development arrives takes the account.

## The Problem
Cedents send large-loss listings in their own formats, with claim numbers that change when systems migrate. Analysts match each claim to its prior evaluation to see development, a job that takes days per large cedent (estimate) and is redone every year.

## Why It's Still Broken
Each listing is treated as a renewal document rather than an update to a standing claim history, so nothing persists from one year to the next.

## What a Fix Looks Like
Ingest each listing into a standing claim history, match claims across years by date of loss, claimant, venue and amounts with a similarity model, and queue only ambiguous matches for the analyst.

## Who Feels the Pain
Casualty pricing analysts in November and December; actuaries whose trend fits depend on the matching.

## Impact If Fixed
Days of re-keying per cedent become an hour of review, and development is measured on matched claims rather than on totals.
