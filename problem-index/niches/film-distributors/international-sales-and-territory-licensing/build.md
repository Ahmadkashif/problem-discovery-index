# Sales Estimates Scored Against Closed Deals

**Niche:** [[niches/film-distributors/international-sales-and-territory-licensing/profile|International Sales & Territory Licensing]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every independent film is financed partly on a sales agent's territory estimates, and no agent keeps an honest record of how those estimates compared with the deals that actually closed.
**Tags:** #tacit-knowledge-ml #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to issue territory sales estimates that buyers actually meet and lenders will finance against, and whoever's estimates land closest to the minimum guarantees finally closed gets the next package from producers and financiers.

## The Problem
For each package (script, director, cast, budget, genre), the head of sales writes a territory-by-territory estimate: France, Germany, Japan, Spain, the Middle East and thirty others, each with an ask and an expected take. The figures come from the agent's sense of each buyer's appetite and recent deals, and the agent knows when a buyer in Germany will stretch for a thriller with a certain actor and when they won't. Lenders discount the estimates by a rule of thumb because they cannot check them.

## Why Nobody Has Built This
Sales companies are small, each holds only its own deal history, and closed prices are confidential. The people who issue estimates have no incentive to publish their error rate. The market's collapse has made old estimates unreliable faster than anyone could recalibrate them by feel.

## What to Build
An estimate ledger joined to the agent's own deal records. It stores every estimate issued, by territory and date, and every deal closed or not closed against it, and reports bias by territory, genre, budget band and cast tier. A model trained on the ledger proposes calibrated ranges for new packages, which the head of sales edits. It also produces a lender-facing report of the agent's historical accuracy.

## Target Customer
Managing directors and heads of sales at international sales companies; secondarily, heads of production finance at gap lenders who would pay for an accuracy record.

## Impact If Built
An agent whose estimates are demonstrably calibrated closes financing faster and on better terms, and can show lenders why. Packages stop being financed on estimates the market stopped paying years ago.
