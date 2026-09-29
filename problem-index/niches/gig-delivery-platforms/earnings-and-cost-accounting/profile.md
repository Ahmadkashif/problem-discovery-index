# Earnings, Pay & Cost Accounting

**Parent Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether anyone can state, from records rather than from estimates, what a courier earns per hour after costs.

## Profile
**Market Size:** ~$5.4B — 6% of US gross order value
**Share of Parent Industry:** ~6%
**Digital Adoption:** Moderate — payment is automated, accounting for it is not
**Target Buyer:** Platform finance and compliance; couriers; regulators and researchers
**Automation Potential:** Very high — the inputs are all instrumented

## What Makes This a Distinct Niche

Independent estimates of net hourly earnings in gig delivery vary by a factor of two or more, and the variance is not a research failure. It reflects that the computation requires joining earnings, engaged time, online time, mileage and cost assumptions — and only the platforms hold the first four, while only the courier knows the fifth.

This is a distinct niche from courier-side tooling because the subject is the platform's own accounting and its reporting obligations, and distinct from offer construction because it concerns realised outcomes rather than predictions. It is where minimum earnings standards bite: a jurisdiction setting a floor per engaged hour requires the platform to compute and reconcile exactly this, and the systems built for those jurisdictions prove the computation is entirely feasible.

## Current Tools & Gaps

Platforms run payment systems that pay accurately and on time, with instant-payout options, weekly statements and 1099 generation. Where minimum earnings standards apply, reconciliation systems compute engaged-hour earnings and top up shortfalls. Third-party tools attempt net computation from the courier's side with partial data.

The gaps are definitional and jurisdictional. Engaged time versus online time is the central definitional battle and the two produce very different rates. Mileage is recorded by the platform and not reported to the courier in deductible form. Cost assumptions are nobody's responsibility. And the platform's own realised earnings distribution, by market and time, is computed internally and never published — so the public argument runs on estimates while the measurement sits in a data warehouse.

## Problems
- [[niches/gig-delivery-platforms/earnings-and-cost-accounting/build|🔨 Build: A Defensible Net Earnings Ledger]]
- [[niches/gig-delivery-platforms/earnings-and-cost-accounting/buy|🛒 Buy: Contractor Payment Platforms Adapted to Earnings Standards]]
- [[niches/gig-delivery-platforms/earnings-and-cost-accounting/fix|🔧 Fix: The Mileage Log the Platform Has and the Courier Reconstructs]]
