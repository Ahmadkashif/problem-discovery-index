# Quotes That Learn From Job Actuals

**Niche:** [[niches/aerospace-parts-suppliers/drawing-to-quote/profile|Drawing-to-Quote for Aerospace RFQs]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Shops quote a part, make it, and never compare the quoted hours with the actual hours in a way that changes the next quote.
**Tags:** #gradient-boosting #cnns #feature-engineering #cross-validation #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn an RFQ drawing package into a priced, routed quote inside the customer's window, and whoever's estimates land closest to the shop's own job actuals takes the account.

## The Problem
In an illustrative case, an estimator prices a titanium fitting at 2.4 hours of five-axis time based on a similar part from last year. The job runs 3.6 hours because of a thin wall that chattered. The ERP records the actual hours; nobody feeds them back. Across a few hundred parts, the shop wins the jobs it underpriced and loses the ones it priced right.

## Why Nobody Has Built This
Quoting tools and ERPs are separate systems, part similarity is hard to compute from drawings, and estimators distrust a model that cannot say why.

## What to Build
Extract geometric and requirement features from drawings and models (material, envelope, feature counts, tightest tolerances, special processes, characteristic count for FAI). Join them to job actuals by operation, and train per-operation hour models with intervals. Show estimators the nearest past parts with their quoted and actual hours, flag features that historically ran over, and log every quote and outcome.

## Target Customer
Estimating managers at AS9100 machine shops and structures suppliers quoting 50+ parts a month.

## Impact If Built
Cutting the absolute quote error on hours from ~25–35% to ~10–15% (estimate) protects margin on won work and raises the win rate on parts the shop can make profitably.
