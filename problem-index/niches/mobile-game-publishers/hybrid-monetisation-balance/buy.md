# Yield Management From Media and Airlines

**Niche:** [[niches/mobile-game-publishers/hybrid-monetisation-balance/profile|Hybrid Monetisation Balance]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines and broadcasters have optimised competing revenue streams over a shared finite inventory for decades, and publishers run two separate A/B tests.
**Tags:** #optimization-fundamentals #revenue-impact #causal-inference #confidence-intervals #evaluation-metrics #time-series-forecasting #gradient-boosting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to set the balance between advertising and in-app purchase when the two compete for the same player's attention and every test measures only one of them — and whoever measures both together takes the account.

## The Problem
Yield management is the mature discipline of allocating a fixed perishable inventory across revenue streams that compete for it. Airlines balance seat classes, broadcasters balance advertising load against audience retention, hotels balance segments — all with formal joint optimisation, explicit substitution modelling and a single objective function. A mobile game has a fixed perishable inventory too: the player's session attention. The industry allocates it with two teams testing separately.

## What Already Exists
Joint revenue optimisation across competing streams; substitution and cannibalisation modelling; inventory allocation under a shared constraint; audience retention as a cost of advertising load; and single-objective yield reporting.

## The Customization Gap
The adaptation is to an inventory that is a person's attention rather than a seat, and to a constraint that is behavioural rather than physical. It requires: (1) inventory defined by player tolerance rather than by a fixed capacity, so the constraint is discovered rather than known — this is the substantive difference and it means the model must learn the limit rather than be told it; (2) substitution between advertising and purchase within the same person, where broadcasting's trade is between advertising and audience size; (3) heterogeneity so extreme that most revenue comes from a small fraction, which changes the optimal allocation per segment rather than in aggregate; (4) effects on retention that accrue over weeks, far slower than a flight or a broadcast hour; and (5) real-time per-session decisioning rather than periodic planning.

## Target Customer
Mobile publishers, monetisation platform vendors, mediation providers, and yield management vendors seeking a digital vertical.

## Impact If Solved
Yield management exists because competing streams over shared inventory is an old problem. Here the inventory is player tolerance, which must be learned rather than known, and the substitution happens inside one person rather than across an audience.
