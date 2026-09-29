# Numbers That Cannot Be Added Together

**Niche:** [[niches/performance-marketing-agencies/cross-platform-measurement/profile|Cross-Platform Measurement & Allocation]]
**Industry:** [[industries/performance-marketing-agencies|Performance Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The allocation decision an agency is paid to make is made against numbers each platform reports about itself, which double-count, use incompatible windows, and cannot be added together.
**Tags:** #causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #revenue-impact #monte-carlo-methods #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to produce one allocation decision from platform numbers that double-count and cannot be added — and whoever does that credibly is selling the only judgement a platform cannot supply about itself.

## The Problem
Three platforms each report the conversions they caused. Each uses its own attribution window, its own identity graph, its own definition of a view-through and its own judgement about what it caused. A shopper who saw all three is claimed by all three. The agency's weekly report adds them up. The total exceeds the number of orders the client took. Everyone in the meeting knows this, nobody corrects it, and the allocation for next month is decided from it. The single decision the agency is retained to make rests on an arithmetic operation that is not valid.

## Why Nobody Has Built This
Each platform's number flatters that platform, and an agency whose reconciled figures are lower than the platform's has an awkward conversation with a client who can see both — the incentive runs against honesty at every level. Building a reconciled measurement requires statistical capability and client data access most agencies do not have. Clients ask for the platform numbers because that is what they see in their own accounts. And the agency is paid on spend, so a finding that reduces spend reduces income.

## What to Build
Produce one number the agency will stand behind. Deduplicate conversions across platforms by joining to the client's own order record, which is the foundation and immediately dissolves the arithmetic problem — the client's orders are the denominator everything must reconcile to. Normalise attribution windows and definitions before any comparison, since the platforms' defaults differ in ways that change the ranking of channels. Apply incrementality priors per platform and vertical, which is the portfolio corpus niche and is what turns reconciliation into allocation. Validate with geographic or holdout experiments run on the client's own spend, since a model without experimental grounding is another opinion. Allocate against marginal return rather than average, because the decision is where the next pound goes and average return cannot answer it. Model saturation per channel, as the marginal curve flattens and most allocation ignores it entirely. Report a single reconciled figure alongside the platform numbers with the gap explained, which is the presentation that lets a client accept a smaller number without concluding the agency is failing. Forecast the effect of a proposed reallocation with an interval, which is what the client is actually asking for. Make the method inspectable, since an agency's reconciled number will be challenged and must survive. And measure the agency's own allocation recommendations against realised outcomes, which is the credibility that justifies a fee in a market where the platforms do the buying.

## Target Customer
Performance agencies differentiating on measurement, in-house performance teams, and the clients whose weekly reports sum incomparable numbers.

## Impact If Built
The one decision the agency is retained to make rests on an invalid addition, and every participant knows it. Joining to the client's own orders dissolves the arithmetic problem, and incrementality priors turn reconciliation into an allocation the platforms cannot supply.
