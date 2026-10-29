# Increase Sizes From a Dose-Response Curve, Not a Tier Table

**Niche:** [[niches/self-storage-operators/existing-customer-rate-increases/profile|Existing-Customer Rate Increases (ECRI)]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most operators outside the REITs size increases from a tier table ("+12% at month six, +8% after"), when the right size depends on how each kind of tenant responds. That response can be measured by varying increases slightly and watching who leaves.
**Tags:** #causal-inference #survival-analysis #monte-carlo-methods #optimization-fundamentals #gradient-boosting #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to size each existing tenant's increase so the added rent outweighs the move-outs it causes, and whoever earns the most net rent per increase notice after twelve months of induced move-outs takes the account.

## The Problem
An ECRI tier table treats a three-year contractor on autopay and a four-month tenant emptying the unit alike. The REITs weigh revenue against move-outs tenant by tenant. Regional operators, third-party managers and owners mostly cannot, because their data never shows what would have happened at a different increase. Every past increase was chosen by the expert, so the ledger confounds increase size with the expert's judgement of the tenant.

## Why Nobody Has Built This
Vendors sell recommendations, and a recommendation engine that admits uncertainty is harder to market than one that promises uplift. Randomising increases, even within a narrow band, sounds like experimenting on customers and needs legal sign-off. Measuring the result takes 6–12 months, longer than most pilots.

## What to Build
A dose-response engine. Each batch carries small, documented random variations in increase size within the operator's policy band, for example ±2 points. That variation identifies how move-out hazard rises with the increase and with the gap to street rate, by tenant segment. A survival model estimates the curve. An optimiser picks each tenant's increase to maximise expected net rent over 12 months. Every recommendation passes a rules table of state notice periods, emergency caps and the operator's fairness limits before it is sent. The two-week MVP is the same engine on a synthetic tenant ledger with known price sensitivity, plus street rates operators post publicly. It reports net rent against a flat +10% rule and against "raise to street rate" (see [[problems/self-storage-operators/ml-opportunity|ML Opportunities]] entry 2).

## Target Customer
VPs of revenue management at regional operators and third-party managers running 50–1,000 stores, and the platforms that serve them.

## Impact If Built
If a store's increases now earn ~$20,000–40,000 a year (estimate) and dose-response sizing keeps one more tenant in a hundred for the same uplift, the gain is ~$1,000–3,000 per store a year. Across 1,000 managed stores that is ~$1–3M a year. The randomised cells also give the operator its first honest record of what its increases cost in move-outs.
