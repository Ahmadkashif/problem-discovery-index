# Promotional Allowance Tracking and Credit Recovery

**Niche:** [[niches/food-distributors/invoice-reconciliation-automation/profile|Invoice Reconciliation Automation]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** Food distributors negotiate $2M-$10M annually in promotional allowances, rebates, and volume discounts from suppliers — but 15-25% of earned credits are never collected because tracking which promotions apply to which invoices is a manual process that falls through the cracks.
**Tags:** #gradient-boosting #anomaly-detection #tabular-ml #revenue-impact #automation

## The Problem
A $200M food distributor negotiates dozens of promotional programs annually with suppliers: temporary price reductions ($0.50/case off for 4 weeks), volume rebates ($0.25/case after purchasing 10,000 cases), new item introductory allowances (free fill on the first 500 cases), advertising allowances ($5,000 co-op marketing credit), and slotting fees ($2,000 per new item placed). These programs represent $2M-$10M in annual credits owed to the distributor. But tracking which purchases qualify for which promotions, verifying that supplier credits appear on invoices, and reconciling quarterly rebate statements against actual purchase volumes is a full-time job that most mid-market distributors do not staff. The result: 15-25% of earned promotional credits are never claimed. The buyer who negotiated the promotion assumes AP will catch the credit; AP assumes the buyer is tracking the promotion. Neither does.

## Why It's Still Broken
Promotional programs are negotiated in conversations, confirmed via email or PDF, and filed in the buyer's email inbox or a shared drive folder. No system connects the promotional agreement (supplier X offers $0.50/case on Product Y from March 1 to April 15) to the actual purchase transactions (did we buy Product Y from Supplier X during that period, and was the $0.50/case credit applied to the invoice?). The verification requires cross-referencing promotional terms against purchase history and invoice credits — a manual process that requires both the buyer's knowledge of what was negotiated and the AP clerk's access to invoice data. When volume rebates are involved, the calculation requires aggregating 3-6 months of purchases and comparing against tier thresholds, which no ERP performs automatically.

## What a Fix Looks Like
A promotional allowance management system that: (1) captures promotional agreements at the time of negotiation (buyer enters terms: supplier, product, amount, date range, type), (2) automatically matches qualifying purchases as they occur, accumulating toward rebate thresholds, (3) verifies that credits appear on supplier invoices within the promotional period, (4) flags missed credits ("Supplier X promotional allowance of $0.50/case was not applied to Invoice #12345 — 200 cases x $0.50 = $100 credit due"), (5) generates quarterly rebate claims with supporting purchase documentation, and (6) provides a dashboard showing total promotional value negotiated, earned, and collected — making the gap visible to management.

## Who Feels the Pain
Buyers who negotiate promotional programs but have no visibility into whether the credits are collected. AP clerks who lack the context to verify promotional credits against negotiated terms. Controllers who suspect promotional leakage but cannot quantify it. Ownership that is missing $300K-$2.5M annually in earned credits.

## Impact If Fixed
Promotional credit recovery improves from 75-85% to 95%+, recovering $300K-$2.5M annually in previously uncollected credits. Buyer negotiation effectiveness improves because they can demonstrate to suppliers exactly what was purchased and what is owed. AP processing of promotional credits simplified from manual cross-referencing to system-generated verification. ROI is extraordinary: a $500/month system recovering $500K/year in lost credits delivers 80x return.
