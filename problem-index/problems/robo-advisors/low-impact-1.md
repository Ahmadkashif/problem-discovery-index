# Tax-Loss Harvesting Value and Wash-Sale Exposure

**Industry:** [[robo-advisors|Robo-Advisors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Harvesting is the industry's headline feature, its value is quoted as an average that applies to almost nobody, and the wash-sale risk that could invalidate it lives in accounts the platform cannot see.
**Tags:** #gradient-boosting #monte-carlo-methods #time-series-forecasting #confidence-intervals #evaluation-metrics #feature-engineering #data-integration #revenue-impact

## The Problem
Tax-loss harvesting sells a position at a loss, books the loss against gains or income, and buys a correlated substitute to maintain exposure. Every major platform automates it and quotes an expected annual benefit — often cited around one percent or a little more — derived from backtests over particular periods and particular client profiles.

For an individual client the actual value depends on their marginal rate, their state, whether they have realisable gains to offset, their contribution pattern, the volatility path of their holdings, their horizon, and whether they will ever realise the deferred gain or hold to a step-up basis. The dispersion around the quoted average is enormous. A client in a low bracket with no offsetting gains may receive close to nothing, while paying the tracking cost of holding substitutes.

Wash sales are the risk that undoes it. Buying a substantially identical security within thirty days either side of the loss sale disallows the loss. The platform enforces this rigorously inside its own accounts, and cannot enforce it at all across the client's 401(k), their spouse's IRA, their brokerage account elsewhere, or their employer stock plan — all of which count. A client with an S&P index fund in a workplace plan receiving automatic contributions is generating wash sales continuously against the platform's harvesting, and neither party knows.

Substitute selection is the third piece. The replacement must track closely without being substantially identical, a standard that has no bright line, and the choice affects both tracking error and the defensibility of the loss.

## What Already Exists
All major platforms automate harvesting with wash-sale avoidance within their own accounts. Direct indexing extends it to individual securities. Substitute pairs are maintained per asset class. Aggregation through Plaid or Yodlee can expose held-away holdings where the client connects them. Tax reporting is standard.

## The Customisation Gap
Per-client value estimation is absent. The platform holds every input needed to estimate what harvesting is actually worth to this specific client, under uncertainty, and instead quotes a category average. Clients for whom the benefit is negligible could be told, which is a fiduciary act that no competitor is performing.

Cross-account wash-sale detection is technically feasible for connected accounts and largely unattempted. Even a probabilistic warning — you hold an S&P fund in a connected workplace plan with regular contributions, which will disallow losses harvested on this position — is far better than silence.

Harvest timing is greedy. Most implementations harvest whenever a loss exceeds a threshold, which spends the opportunity early in a decline. Whether to harvest now or wait for a deeper loss is an optimal stopping problem with a known horizon and estimable volatility, and nobody treats it as one.

And realised benefit is not reported. Clients receive a count of losses harvested rather than an estimate of tax actually saved, which is the only number that means anything and is computable from their own return data.

## Impact If Solved
Harvesting is the primary differentiator in a category where portfolio construction has converged and fees have compressed to nearly nothing, and it is sold on an average that misdescribes most individual clients' experience. Estimating per-client value, warning on cross-account wash-sale exposure and optimising timing turns a marketing claim into a measured service, and telling the clients for whom it is worthless is the strongest possible demonstration of the fiduciary posture these platforms claim.
