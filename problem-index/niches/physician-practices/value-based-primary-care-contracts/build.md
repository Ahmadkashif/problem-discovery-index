# Attribution Churn Forecast Before the Year Starts

**Niche:** [[niches/physician-practices/value-based-primary-care-contracts/profile|Primary Care in Value-Based Contracts (ACOs & MA Risk)]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A primary care group plans its care management around the patients CMS attributes to it, then loses a share of them to specialists and other practices during the year, and nobody forecasts which ones.
**Tags:** #gradient-boosting #survival-analysis #monte-carlo-methods #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep an attributed population's cost under its benchmark, with quality and risk scores complete before the performance year closes, and whoever books the most shared savings per attributed patient with no benchmark or RADV clawback takes the account.

## The Problem
MSSP attribution follows where a beneficiary receives most of their primary care services. Patients who see a cardiologist or a retail clinic more often than their PCP can drift out, and new patients drift in. Care managers spend outreach time on patients who will not count. The group's savings estimate moves all year.

## Why Nobody Has Built This
Enablers report attribution after CMS publishes it quarterly. The claims needed to forecast it come through the ACO's CMS data feed, and few groups have analysts to model it. Prospective assignment (129 ACOs in 2026) reduces the problem but does not remove it.

## What to Build
A model that forecasts, for each patient, the probability of remaining attributed through year end. It is trained on prior years' claims, visit patterns, specialist use and the assignment algorithm's own rules. Simulations of the year show the savings range under expected churn. Outreach is targeted at patients likely to stay and at patients who should be brought back to primary care.

## Target Customer
Executive directors and analytics leads at physician-led ACOs of 5,000–50,000 beneficiaries, and the enablers that run them.

## Impact If Built
Focusing outreach on patients who will count could raise care-management yield by ~20% (estimate). Explaining churn early protects ~$50–$150 per attributed beneficiary a year in savings that would otherwise leak (estimate).
