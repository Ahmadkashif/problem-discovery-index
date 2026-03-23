# Unit Economics Visibility on Small-Balance Portfolios

**Niche:** [[niches/collections-agencies/small-balance-portfolio/profile|Small-Balance Portfolio Specialists]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Portfolio buyers purchase small-balance debt without account-level cost tracking, so they cannot tell which segments are profitable and which are consuming resources without recovery.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #data-integration

## The Problem
A portfolio buyer purchases 50,000 accounts at 2 cents on the dollar ($300K investment). Over 12 months, the agency recovers $2.1M — a healthy 7x return on paper. But without account-level cost tracking (postage, SMS, dialer minutes, agent time per account, payment processing fees, skip trace costs), the buyer cannot determine that 60% of the recovery came from 15% of the accounts, and that 40% of accounts consumed resources without any recovery at all. Future portfolio purchase decisions are based on aggregate ROI, not segment-level profitability.

## Why It's Still Broken
Collection platforms track recovery at the account level but not cost at the account level. Costs are tracked in aggregate (total postage spend, total dialer cost) and allocated evenly or not at all. Building account-level cost attribution requires integrating data from the collection platform (contacts, payments), the dialer (call minutes), the letter vendor (postage), the SMS provider (message costs), and skip trace feeds (per-query fees) — data from 5-6 systems that are not connected.

## What a Fix Looks Like
A portfolio analytics dashboard that attributes all direct costs to individual accounts by integrating cost data from each channel (dialer, mail, SMS, skip trace, payment processing). The dashboard shows per-account and per-segment profitability: which balance ranges, debt types, debtor demographics, and vintages are profitable vs. unprofitable. Portfolio purchase models are trained on historical segment-level profitability rather than aggregate ROI.

## Who Feels the Pain
Portfolio buyers making $100K-$1M purchase decisions based on aggregate portfolio performance without knowing which segments drove the returns — leading to overpaying for portfolios heavy in unprofitable segments.

## Impact If Fixed
Enables 10-20% improvement in portfolio purchase ROI by avoiding overvaluation of portfolios with high concentrations of unprofitable account segments. Identifies which collection channels to apply to which segments, reducing waste by 15-25%.
