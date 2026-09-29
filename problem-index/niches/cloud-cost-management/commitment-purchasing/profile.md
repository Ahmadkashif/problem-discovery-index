# Commitment Purchasing

**Parent Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to turn a multi-year capacity commitment into a decision made under stated uncertainty rather than an extrapolation of last quarter — and whoever does that takes the largest single controllable lever in the category.

## Profile
**Market Size:** ~$540M US attributable to commitment management and rate optimisation
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** Medium — recommendations exist and look backwards
**Target Buyer:** Cloud economics, finance and procurement
**Automation Potential:** Very High — this is a portfolio optimisation problem under uncertainty

## What Makes This a Distinct Niche
Commitment purchasing is the largest single lever most organisations have over their cloud bill and the one most exposed to being wrong. Reserved instances and savings plans require forecasting usage one to three years ahead, and the tools recommend from the recent past — which is a reasonable heuristic for a stable workload and a poor one for a business that will re-architect the workload within eighteen months. Buy too little and pay list rates on a large volume; buy too much and pay for capacity nobody uses, with limited resale options. The decision structure is genuinely interesting: overlapping instruments with different flexibility and different discounts, a multi-year horizon, an uncertain demand forecast, and an option value to waiting that nobody computes. It is a portfolio optimisation problem under uncertainty and it is made by looking at a coverage percentage and a recommendation derived from thirty days of history.

## Current Tools & Gaps
Commitment recommendations from the providers and third parties, coverage and utilisation dashboards, commitment marketplaces and management services, and negotiated enterprise agreements. The gaps: recommendations extrapolate recent usage and ignore known future change, which is the central failure; the trade-off between instrument types — flexible and less discounted against rigid and more — is not modelled, so organisations default to one; risk is not quantified, so a recommendation is a point estimate with no statement of downside; the option value of waiting is never computed, although the commitment can be made at any time; and portfolio ladder structure — staggering expiries to avoid a single large renewal decision — is a practitioner technique that no tool supports.

## Problems
- [[niches/cloud-cost-management/commitment-purchasing/build|🔨 Build: A Three-Year Bet on an Eighteen-Month Workload]]
- [[niches/cloud-cost-management/commitment-purchasing/buy|🛒 Buy: Portfolio Optimisation Under Uncertainty]]
- [[niches/cloud-cost-management/commitment-purchasing/fix|🔧 Fix: Coverage Reported as a Single Percentage]]
