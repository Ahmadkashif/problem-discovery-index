# Award Optimization Adapted to Carrier Acceptance Behaviour

**Niche:** [[niches/freight-brokerage/freight-procurement-consultancies/profile|Freight Procurement & Bid Consultancies]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Optimization solvers find the cheapest feasible award; the cheapest feasible award is frequently the one carriers quietly stop accepting in March.
**Tags:** #optimization-fundamentals #convex-optimization #gradient-boosting #probability-distributions #confidence-intervals #evaluation-metrics #feature-engineering #monte-carlo-methods #automation #data-integration

## The Problem
Bid optimization is a constrained assignment problem and is solved as one: minimize cost subject to capacity, carrier limits, and service constraints. The solvers do this well. What they optimize is a number that assumes every award is honoured, which is precisely the assumption that fails. An award that is two percent cheaper but sits at the bottom of a carrier's acceptable range will be rejected the moment the market tightens, and the shipper pays spot. The consultant knows this and compensates with judgment — spreading awards, avoiding aggressive rates on volatile lanes — which is expertise applied outside the model rather than inside it.

## What Already Exists
Optimization tooling is mature and inexpensive. Commercial solvers handle large-scale assignment with complex constraints; the bid platforms include scenario optimization; the modelling libraries are free and well documented. For solving the stated problem, nothing needs building.

## The Customization Gap
Every available solver optimizes expected cost under the assumption of compliance. What is needed is optimization under uncertain acceptance: each candidate award carries an acceptance probability conditional on rate relative to market, carrier profile, lane characteristics, and volume commitment, and the objective becomes expected realized cost including the fallback path when a tender is rejected. That is a stochastic problem rather than a deterministic one, and it requires an acceptance model estimated from the firm's own bid and post-award history — which is why it cannot be bought. Risk should be expressible as a constraint the shipper chooses: a guide that is slightly more expensive on paper and materially more robust is the right answer for most shippers and cannot currently be described, let alone selected. And scenario output should report the distribution of realized cost rather than a single optimized number.

## Target Customer
Modelling leads and practice principals at procurement consultancies, and the transportation leaders who select award scenarios on paper cost because no other basis is offered.

## Impact If Solved
Moves the deliverable from cheapest-on-paper to lowest-expected-realized, which is the number the shipper actually experiences and the one the consultancy is implicitly judged on. It also brings the consultant's compensating judgment inside the model, which is where it becomes consistent and transferable.
