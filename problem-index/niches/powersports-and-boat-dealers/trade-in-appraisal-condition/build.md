# An Appraisal Graded Against What the Unit Brought

**Niche:** [[niches/powersports-and-boat-dealers/trade-in-appraisal-condition/profile|Trade-In Appraisal & Condition Assessment]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every trade's outcome is in the DMS and every appraisal is on a sheet, and nobody has joined them to find out which conditions and which managers lose money.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #gradient-boosting #survival-analysis #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price a used boat or machine at the moment of trade, and whoever has the smallest gap between the trade allowance plus reconditioning and the price the unit actually brings takes the account.

## The Problem
The used-unit manager's allowance decides whether the deal closes and whether the trade makes money. Reconditioning repair orders, days on lot and the final retail or wholesale price are recorded unit by unit. They are never compared with the appraisal, so the store doesn't know where its appraisals go wrong: wet transoms, high-hour outboards, rolled side-by-sides, salt-water boats, or one manager's habits.

## Why Nobody Has Built This
Guide publishers sell base values, not condition. DMS vendors hold outcomes but no appraisal evidence. Capturing evidence costs time on a trade desk where the customer is waiting, and the realised-price label is noisy and seasonal.

## What to Build
A guided walkaround on a phone that captures photos and short videos by zone, moisture and compression readings and engine downloads in under ~15 minutes (estimate), drafts condition notes, and records the allowance. Every record is joined to later repair orders and sale price, season-adjusted. Vision models flag damage; a gradient-boosted model predicts reconditioning and realised price; a survival model predicts days to sale. Managers see an allowance range with evidence, and the general manager sees a monthly appraisal-accuracy scorecard.

## Target Customer
Used-unit directors at marine and powersports dealer groups; general managers at single stores with heavy trade volume.

## Impact If Built
Closing $500–1,000 of the allowance-plus-recon gap on the worst tenth of trades (estimate) is worth $30,000–100,000 a year at a store taking 300 trades.
