# A Three-Year Bet on an Eighteen-Month Workload

**Niche:** [[niches/cloud-cost-management/commitment-purchasing/profile|Commitment Purchasing]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every tool recommends reserved instances and savings plans from the recent past, and the purchase is a one-to-three-year bet on a workload that will be re-architected within eighteen months.
**Tags:** #time-series-forecasting #bayesian-inference #monte-carlo-methods #convex-optimization #confidence-intervals #evaluation-metrics #revenue-impact #optimization-fundamentals
**Contested on:** Every serious competitor here is fighting to turn a multi-year capacity commitment into a decision made under stated uncertainty rather than an extrapolation of last quarter — and whoever does that takes the largest single controllable lever in the category.

## The Problem
A company commits to three years of a particular instance family at a substantial discount, on a recommendation derived from the last thirty days of usage. Fourteen months later the service is containerised and moved to a different instance family, the commitment is stranded, and the remaining twenty-two months are paid for capacity nobody uses. The engineering plan that caused this was known to the architecture team at the time of purchase. Nobody asked them, because the recommendation came from a tool that has no mechanism for asking and the purchase was made by finance on its output.

## Why Nobody Has Built This
Recommendation engines were built on billing data, which is historical by definition, and no vendor has built a way to incorporate the organisation's own knowledge of what it is about to do. The decision is also split: finance executes the purchase, engineering determines the usage, and nobody owns the join — which is the same organisational seam that appears throughout this category. Risk is not quantified because a point recommendation is easier to present than a distribution, and the downside of over-commitment is realised years later by somebody else.

## What to Build
Treat it as a decision under uncertainty with the organisation's own knowledge as an input. Forecast usage as a distribution rather than a point, incorporating planned architectural change, migrations, launches and retirements captured in a structured form from the teams who know them — which is the single most important input and is currently absent entirely. Model the instrument set properly: the flexible instruments with smaller discounts against the rigid ones with larger, across terms and payment options, as a portfolio rather than a single choice. Optimise coverage against the forecast distribution with an explicit risk preference, reporting the expected saving and the downside — if usage falls to the tenth percentile, this is what the stranded commitment costs — which is the statement that makes the decision defensible and which no tool produces. Compute the option value of waiting, since commitments can be purchased at any time and the value of information from another quarter is frequently larger than the discount forgone. Recommend a laddered structure with staggered expiries, which is what experienced practitioners do by hand and which converts one large periodic decision into a series of small ones. And measure realised outcomes against the recommendation, since a commitment engine that never learns whether its past recommendations were right cannot improve.

## Target Customer
Cloud economics, finance and procurement functions at organisations with material commitment spend, and the cost management vendors and commitment marketplaces competing on this decision.

## Impact If Built
This is the largest single controllable lever in the category and the decision is made from thirty days of history against a three-year horizon. Incorporating known architectural change and reporting the downside explicitly are the two changes that turn an extrapolation into a decision.
