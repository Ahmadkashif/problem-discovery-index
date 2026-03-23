# CU-Specific Alert Prioritization Model

**Niche:** [[niches/credit-unions/bsa-aml-compliance-ops/profile|BSA/AML Compliance Operations]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A transaction monitoring model calibrated to credit union member behavior — not commercial bank customer behavior — that reduces the 90%+ false positive rate on BSA alerts by establishing individual member behavioral baselines from CU-specific transaction patterns.
**Tags:** #gradient-boosting #anomaly-detection #tabular-ml #compliance #automation

## The Problem
BSA/AML monitoring platforms trigger alerts when transaction patterns deviate from thresholds — but those thresholds are calibrated for commercial bank customer populations. A credit union member who runs a cash-intensive small business (landscaping, food truck, cleaning service) triggers structuring alerts every week because their regular $3,000-$5,000 cash deposits look suspicious against a bank-customer baseline. A BSA officer at a community CU knows this member personally and clears the alert in 30 seconds — but still must document the investigation. Multiply by 200-400 alerts per month with 90%+ false positive rates, and the BSA officer spends their entire week clearing alerts they know are benign.

## Why Nobody Has Built This
BSA/AML platform vendors (Verafin, Abrigo) sell across the financial institution spectrum and calibrate their models on aggregated data that includes banks, which have fundamentally different transaction distributions than CUs. Building a CU-specific model requires training on CU member transaction patterns, which are more concentrated in individual relationships (the BSA officer knows the member) and community patterns (the CU serves a specific geographic and economic community). The regulatory environment adds risk: a model that reduces alerts and misses a genuinely suspicious transaction creates regulatory liability. Vendors are conservative about reducing alert volumes for liability reasons.

## What to Build
A member-level behavioral baseline model that learns each member's normal transaction patterns from 12-24 months of history: typical cash deposit amounts and frequency, regular transfer destinations, seasonal cycles (holiday spending, tax refund deposits), and business-related patterns. New alerts are scored against the individual member's baseline rather than a population average — a $4,000 cash deposit is expected for the landscaping business owner but anomalous for the retired teacher. Alerts are ranked by deviation from individual baseline, not from population threshold. The BSA officer reviews the top 20% highest-anomaly alerts in depth; the bottom 80% receive streamlined review with pre-populated context showing why the transaction is consistent with the member's established pattern.

## Target Customer
BSA officers at CUs with $200M-$2B in assets processing 200-500 BSA alerts per month who spend 60-80% of their time clearing false positives from monitoring platforms calibrated for bank-scale transaction patterns.

## Impact If Built
Reduces BSA alert investigation workload by 50-70% by prioritizing genuinely anomalous transactions over routine member behavior. Improves actual suspicious activity detection by focusing BSA officer attention on the highest-risk alerts instead of spreading it across hundreds of false positives. Provides NCUA-auditable documentation that the model maintains or improves detection effectiveness while reducing false positive burden.
