# Commitment Purchasing Under Uncertainty

**Industry:** [[cloud-cost-management|Cloud Cost Management]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every tool recommends reserved instances and savings plans from the recent past, and the purchase is a one-to-three-year bet on a workload that will be re-architected within eighteen months.
**Tags:** #time-series-forecasting #monte-carlo-methods #optimization-fundamentals #confidence-intervals #gradient-boosting #evaluation-metrics #revenue-impact

## The Problem
Cloud providers offer substantial discounts for committing to spend over one or three years. The savings are large enough that not committing is expensive and committing wrongly is worse, since an unused commitment is money spent on nothing.

Every cost tool recommends commitments. The recommendation is almost always an extrapolation of recent usage: you have run this steadily for ninety days, so commit to it.

That reasoning ignores everything that determines whether the commitment will be used. Planned migrations. A re-architecture that will move the workload to a different instance family or to serverless. A product launch. A customer contract ending. Seasonal patterns longer than the lookback window. A move to a different region.

Engineering knows all of this and is not in the conversation, because commitment purchasing sits with finance and procurement and is treated as a financial optimisation over a usage series.

The consequence is a portfolio of commitments that drifts out of alignment with the estate, and organisations that under-commit defensively because the last purchase went badly — paying full rate to avoid a repeat.

## What Already Exists
Native commitment recommendation exists at every hyperscaler and in every third-party tool, with utilisation and coverage reporting. Commitment marketplaces allow some resale of unused reservations. Savings plans are more flexible than the reserved instances they largely replaced. Consultancies and managed service providers offer commitment management as a service. Coverage and utilisation dashboards are standard.

## The Customisation Gap
Uncertainty is absent from the recommendation. A commitment is a decision under uncertainty and should be presented as a distribution — commit at this level and expected saving is this much, with this probability of waste under a range of scenarios — rather than as a point recommendation with an optimistic saving attached.

Planned change is the missing input and the most important one. Roadmaps, migration plans and architecture decisions are knowable inside the organisation and are never joined to the forecast. Even a coarse signal — this service is scheduled for migration next quarter — would materially change the optimal commitment.

Portfolio optimisation across term, coverage and flexibility is a real optimisation problem, and tools generally recommend one commitment at a time rather than solving the whole position.

Continuous rebalancing is the fourth gap: as the estate changes, the optimal position changes, and the portfolio is revisited when someone remembers rather than continuously.

## Impact If Solved
Commitment purchasing determines a large share of realised cloud discount and is decided by extrapolating the last quarter into the next three years. Presenting it as a decision under uncertainty, informed by planned change, is what would let organisations commit confidently rather than defensively — and defensive under-commitment is itself a large recurring cost.
