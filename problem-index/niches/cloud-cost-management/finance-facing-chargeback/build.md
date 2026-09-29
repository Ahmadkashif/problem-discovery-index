# A Forecast That Extrapolates the Past

**Niche:** [[niches/cloud-cost-management/finance-facing-chargeback/profile|Finance-Facing Allocation & Chargeback]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Cloud spend is forecast by extending the recent trend, in an organisation that knows exactly which products it is launching and which workloads it is migrating next quarter.
**Tags:** #time-series-forecasting #gradient-boosting #bayesian-inference #linear-regression #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor here is fighting to produce a cloud allocation that reconciles to the invoice, survives audit and forecasts accurately enough to plan against — and whoever does that takes the finance account, because a number that does not add up is worse than no number.

## The Problem
The annual plan includes a cloud line derived by taking last year's spend and adding a growth percentage. During the year: a large customer onboards and triples one service's volume, a migration retires a legacy environment, a new product launches, and a commitment purchase changes the effective rate. Each of these was known in advance by somebody in the organisation. The forecast knew none of them and is wrong by a wide margin in both directions across the year, which means the plan is revised quarterly and the cloud line is treated as unpredictable — a characterisation that is convenient for everybody and is not true.

## Why Nobody Has Built This
Forecasting from the billing series alone is what the available data supports, and the vendors' data stops at the bill. The information that would improve it — the product roadmap, migration plans, customer onboarding schedule, capacity plans — lives in the organisation and has never been connected, partly because it is qualitative and partly because nobody has asked for it in a structured form. Extrapolation is also defensible in the way that not being wrong for an obvious reason is defensible, and a forecast that is confidently wrong from an incorporated assumption is politically worse than one that is vaguely wrong from a trend.

## What to Build
Forecast from drivers rather than from the series. Decompose spend into components with different behaviour — baseline capacity, volume-driven consumption, storage accumulation, data transfer, and one-off project spend — since these have entirely different dynamics and forecasting the total obscures all of them. Attach business drivers where they exist: customers onboarded, transactions processed, data retained, which converts the forecast into a function of things the business plans rather than of time. Incorporate known events explicitly — migrations, launches, retirements, commitment purchases — captured in a structured form from the people who know them, which requires a small recurring input process and is the difference between a forecast and an extrapolation. Report the forecast with an interval and with its assumptions listed, so a variance can be traced to an assumption rather than to an unpredictable cloud. Reconcile actuals to the forecast by driver, which makes the next forecast better and is the loop that does not exist. And quantify commitment exposure within the forecast, since a commitment purchase changes the effective rate and the coverage decision depends on the forecast it is also an input to.

## Target Customer
Finance and financial planning functions with a material cloud line, technology business management teams, and the cost management vendors competing for the finance buyer.

## Impact If Built
The organisation knows most of what will move its cloud spend and the forecast uses none of it. Driver-based decomposition with explicit known events converts a quarterly revision cycle into a plan that can be held, and makes variance explicable rather than mysterious.
