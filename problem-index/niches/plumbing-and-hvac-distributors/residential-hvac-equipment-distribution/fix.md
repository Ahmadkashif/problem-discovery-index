# The Sale Lost to a Missing Coil Nobody Records

**Niche:** [[niches/plumbing-and-hvac-distributors/residential-hvac-equipment-distribution/profile|Residential HVAC Equipment Distribution to Dealers]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** When a dealer walks out because the branch can't complete a system, the ERP records nothing, so next summer's buy repeats the gap.
**Tags:** #large-language-models #logistic-regression #feature-engineering #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to have the dealer's brand of complete, AHRI-matched system — now in R-454B or R-32 — on the branch shelf on the day a no-cool call becomes a replacement, and whoever keeps the highest in-stock rate on complete matched systems through the peak weeks takes the account.

## The Problem
A dealer calls for a 4-ton A2L condenser with a matching coil; the branch has the condenser but the coil is two days out; the dealer buys a whole system from another brand's distributor, or puts in a different tonnage. No sale is recorded, so no demand is recorded, and the purchasing plan built on sales history under-buys exactly what was missing.

## Why It's Still Broken
Counter and inside staff are too busy in July to log lost sales, ERPs have no easy field for them, and quotes that don't convert are rarely closed out.

## What a Fix Looks Like
Capture lost demand as a by-product: log every availability lookup in the dealer app and at the counter, every quote and every unconverted system request, and infer lost sales when a lookup or quote for a system is followed by no order within hours. Feed that demand into forecasts and into a weekly list of the components that broke the most matches.

## Who Feels the Pain
Purchasing managers planning the next season, branch managers judged on sales they never saw, and dealers sent elsewhere.

## Impact If Fixed
If lost system demand runs ~5–10% of peak-season sales (estimate), recording it corrects next year's buy in the components that matter and turns the transition-era guesswork into a measured gap.
