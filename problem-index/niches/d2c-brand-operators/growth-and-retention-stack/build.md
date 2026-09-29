# Two Businesses Sharing a Budget Line

**Niche:** [[niches/d2c-brand-operators/growth-and-retention-stack/profile|Growth & Retention Stack]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Acquisition buys attention in a rising auction and retention sends messages at almost no marginal cost, and the decision about how to split between them is made annually by argument rather than by evidence.
**Tags:** #convex-optimization #causal-inference #confidence-intervals #revenue-impact #survival-analysis #evaluation-metrics #hypothesis-testing #time-series-forecasting
**Contested on:** Not terminal — the contest differs by whether the customer has bought before, and the decomposition is recorded in the profile.

## The Problem
A brand's growth lead argues for more acquisition spend, pointing at a return on ad spend figure. The retention lead argues the acquisition is buying low-value customers and that the same money in lifecycle would produce more revenue, pointing at a repeat purchase rate. Neither number is comparable to the other: one is computed from platform-claimed conversions over a short window, the other from a cohort analysis that assumes the customers would not have bought again anyway. The decision is made on seniority and on who presented last. It is the single largest allocation decision in the business and there is no common unit in which to make it.

## Why Nobody Has Built This
The two functions came from different disciplines with different vocabularies and different vendors, and their metrics were never reconciled because nobody owned the reconciliation. Acquisition's numbers come from the platforms and retention's from the brand's own data, so they are not even measured on the same basis. And the honest common unit — incremental contribution margin per dollar — requires both the incrementality measurement and the order-level margin the category also lacks.

## What to Build
Build the common unit and the allocation on top of it. Express both halves in incremental contribution margin per dollar over a stated horizon, which is the only comparison that means anything and which requires the incrementality and margin work as inputs — saying so plainly is more useful than another dashboard. Measure retention incrementally too, since a repeat purchase from a customer who would have repurchased anyway is not caused by the email that preceded it, and holdouts are cheap and easy on owned channels in a way they are not in paid. Model the interaction, because acquisition determines the audience retention works on and a cheaper customer who never repurchases is not cheaper — the two halves are coupled and are optimised separately everywhere. Produce a marginal return curve for each and allocate to equalise the margin, which is elementary and is not what anybody does. State the horizon explicitly, since acquisition's return arrives over years and retention's over months and comparing them without a stated horizon is the root of the argument. Report cohort contribution over time as the shared scoreboard, which both functions affect and neither owns. Support the strategic case honestly, including the case that the brand's acquisition economics do not work at any volume, which is true for a number of them and is the finding nobody wants to present. And make the allocation a monthly measured decision rather than an annual argument.

## Target Customer
Brand leadership making the allocation, both growth functions, and the investors whose returns depend on the answer.

## Impact If Built
The largest allocation decision in the business is made without a common unit. Incremental contribution margin per dollar over a stated horizon is that unit, and measuring retention incrementally — trivially cheap on owned channels — removes the largest source of double counting.
