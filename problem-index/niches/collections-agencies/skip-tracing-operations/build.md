# Multi-Vendor Skip Trace Orchestration and Scoring Engine

**Niche:** [[niches/collections-agencies/skip-tracing-operations/profile|Skip Tracing Operations]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product optimizes which skip trace vendor to query for which debtor profile, merges results across vendors with quality scoring, and routes the highest-quality contact data to the dialer in priority order.
**Tags:** #gradient-boosting #ranking #tabular-ml #data-integration #revenue-impact

## The Problem
An agency subscribing to 3 skip trace vendors at $0.50-$2.00 per query faces a decision on every unlocated account: which vendor to query first? Vendor A may be better for debtors in the Southeast, Vendor B better for younger debtors with mobile phones, and Vendor C better for debtors with thin credit files. Currently, agencies query all vendors on every account (expensive) or always start with the cheapest vendor (suboptimal). The results are not quality-scored across vendors — the agency treats a "high confidence" result from Vendor A the same as one from Vendor B, even though historical accuracy may differ significantly.

## Why Nobody Has Built This
Building an orchestration engine requires tracking skip trace outcomes at the vendor level — which vendor's phone numbers actually resulted in right-party contact? This feedback loop must connect the skip trace query log to the dialer disposition log, which requires integrating two different systems. Agencies that have this data rarely analyze it systematically. Skip trace vendors have no incentive to facilitate cross-vendor comparison.

## What to Build
A skip trace orchestration platform that: (1) selects the optimal vendor(s) for each account based on debtor demographics and historical vendor accuracy by segment; (2) merges results across vendors, deduplicating and quality-scoring each phone number and address; (3) feeds ranked contact data to the dialer in priority order; (4) tracks contact outcomes by vendor and updates the vendor selection model in a feedback loop. The platform minimizes cost per right-party contact by routing queries to the vendor most likely to return accurate data for each debtor profile.

## Target Customer
Skip trace managers at agencies spending $50K+ per month on skip trace vendor fees who currently query all vendors on all accounts without optimization.

## Impact If Built
Reduces skip trace vendor costs by 20-30% by eliminating redundant queries. Increases right-party contact rate by 10-15% through better phone number quality scoring. Saves $10K-$30K per month in vendor fees while simultaneously improving contact rates.
