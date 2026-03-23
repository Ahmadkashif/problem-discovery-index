# Member Financial Health Progression Tracking

**Niche:** [[niches/credit-unions/underbanked-community-cus/profile|Underbanked Community CUs]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Fix (Pain Point)
**One-liner:** Underbanked-serving CUs invest in financial education and coaching but cannot measure whether their members are actually becoming more financially healthy — making it impossible to prove program effectiveness to boards, regulators, or funders.
**Tags:** #gradient-boosting #regression #tabular-ml #data-integration #compliance

## The Problem
Community development CUs offer financial literacy workshops, one-on-one coaching, savings challenges, and credit-building products. Boards ask: "Are our members' financial health improving?" CDFI Fund and foundation grantors ask: "What outcomes did your financial capability program produce?" The CU cannot answer because it has no financial health measurement framework. Individual metrics exist — savings balance, credit score (for those who have one), overdraft frequency — but they're scattered across systems and never aggregated into a longitudinal financial health score that tracks a member's progression from underbanked to financially stable.

## Why It's Still Broken
"Financial health" is multi-dimensional — it encompasses savings adequacy, debt burden, income stability, credit access, and financial resilience. No CU core platform computes a composite score. The CFPB has published a financial well-being scale, but it's a survey instrument, not a data-driven metric. Building a financial health score from CU transaction data requires feature engineering that maps account behavior to financial health dimensions — work that individual small CUs don't have the data science capability to do.

## What a Fix Looks Like
A financial health scoring model that computes a multi-dimensional score for each member from CU account data: (1) savings adequacy (balance relative to monthly expenses, savings growth trajectory); (2) income stability (deposit amount consistency, employment continuity indicators); (3) debt management (loan payment timeliness, utilization trends); (4) financial resilience (emergency fund adequacy, overdraft frequency trend); (5) credit progression (score trajectory for bureau-reported members, internal score for thin-file). The score updates monthly, producing a longitudinal view: "Member improved from 35/100 to 62/100 over 18 months." Aggregate scores power program effectiveness reporting for boards, NCUA examiners, and grantors.

## Who Feels the Pain
Program directors and CEOs who invest $50K-$200K annually in financial education and coaching programs but cannot demonstrate measurable member outcomes, and grant managers who must submit impact reports to funders with anecdotal evidence rather than quantified health metrics.

## Impact If Fixed
Provides the first quantitative measure of member financial health progression — enabling data-driven program optimization instead of faith-based budgeting. Strengthens CDFI Fund and foundation grant applications with demonstrated outcome metrics. Identifies which interventions (coaching, savings programs, credit-building products) actually move the needle on financial health, allowing CUs to invest in what works.
