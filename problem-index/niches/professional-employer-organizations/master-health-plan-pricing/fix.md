# Plan Cost Surprises Reported a Quarter Late

**Niche:** [[niches/professional-employer-organizations/master-health-plan-pricing/profile|Master Health Plan Pricing & Underwriting]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Fix (Pain Point)
**One-liner:** A PEO learns its plan is running hot from paid-claims reports that lag incurred cost by months, and by then a year of prices has already been quoted.
**Tags:** #time-series-forecasting #bayesian-inference #change-point-detection #evaluation-metrics #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep a PEO's master health plan at its target loss ratio while still undercutting what small employers would pay on their own. But that is two contests with different winners: selecting and pricing prospects from a census and a few morbidity flags before a broker's quote deadline, which new-business underwriters and scoring vendors win, and setting each in-force client's renewal so low-claim groups stay and the plan does not spiral, which renewal actuaries and account teams win. Decomposed into contested sub-niches below.

## The Problem
Claims are paid weeks to months after care, and the carrier's reports show paid experience. A shift in trend, such as specialty drugs, GLP-1 uptake, or a rise in inpatient intensity, shows up in a PEO's results a quarter or two after it started. Meanwhile the new-business team keeps quoting at the old assumptions and renewals go out at last year's trend. Insperity raised its benefits-cost guidance mid-year in 2025 and then reported a 14% fall in full-year gross profit.

## Why It's Still Broken
Completion factors are applied annually by actuaries. Large-claim notices and pharmacy data, which arrive faster, are not combined with medical claims, and nobody owns a monthly incurred estimate that sales pricing listens to.

## What a Fix Looks Like
A monthly incurred-cost estimate: paid claims completed with lag models, large-claimant notices and pharmacy fills used as leading indicators, and a change-point alert when trend departs from the pricing assumption. The alert feeds straight into the rate tables new-business pricing uses.

## Who Feels the Pain
CFOs who restate guidance, underwriters pricing on stale trend, and the clients who get a large correction at the next renewal.

## Impact If Fixed
Pricing reacts in weeks instead of quarters, which on a multi-billion-dollar plan is a measurable share of a bad year's shortfall (estimate).
