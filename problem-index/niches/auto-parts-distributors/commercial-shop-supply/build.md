# The Lost-Request Ledger

**Niche:** [[niches/auto-parts-distributors/commercial-shop-supply/profile|Commercial Parts Supply to Independent Repair Shops]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every commercial supplier fights for the shop's first call, and none of them can measure its first-call fill rate, because the requests it failed to fill leave no record.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to be the independent shop's first call for the part a car on the lift needs, and whoever fills the largest share of the shop's first requests with the correct part takes the account.

## The Problem
A commercial supplier's reports show sales by shop and category. They do not show the call where the counter said "not in stock, I can have it this afternoon" and the shop hung up and called someone else, the e-catalog search where a competitor's price or availability won, or the part that went out wrong and came back. Those are exactly the events that move a shop's first call, and they are invisible until sales drop.

## Why Nobody Has Built This
The events live in different systems: lookup screens that discard searches with no sale, e-catalog networks that report orders but not lost quotes to the losing seller, returns desks with loose reason codes, and phone calls nobody logs. Joining them per shop needs a common request identifier that none of these systems creates.

## What to Build
A ledger that records every shop request across phone, text, counter and e-catalog with its outcome: filled correct, filled wrong (returned for fit), not in stock locally but filled from hub, not filled, or quoted and lost. From it, compute first-call fill rate per shop and per category, the causes of misses (stock, fitment, price), and the SKUs whose absence costs the most first calls. A churn model on the ledger flags shops whose fill rate has slipped before their spend does.

## Target Customer
Commercial directors at chains, warehouse distributors and programme groups; the business-system and e-catalog vendors who could carry the ledger as a feature.

## Impact If Built
If a store raised its first-call fill rate on its top 50 shops from ~80% to ~85% (estimate), and each point is worth ~1% of those shops' spend, a store selling ~$1.5M a year to them would add ~$75K of sales without a new account.
