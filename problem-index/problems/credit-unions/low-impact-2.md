# BSA/AML Transaction Monitoring Tuned for Credit Union Patterns

**Industry:** [[credit-unions|Credit Unions]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** BSA/AML platforms like Verafin and Abrigo detect suspicious transactions using rule-based thresholds and ML models trained primarily on commercial bank data, producing 90%+ false positive alert rates at small credit unions where normal member transaction patterns trigger rules designed for different account behaviors.
**Tags:** #gradient-boosting #anomaly-detection #tabular-ml #compliance

## The Problem

Every credit union, regardless of size, must maintain a BSA/AML compliance program that monitors member transactions for suspicious activity and files Suspicious Activity Reports (SARs) with FinCEN. Small and mid-size CUs ($50M-$500M in assets) use platforms like Verafin, Abrigo, or NICE Actimize for automated transaction monitoring. These platforms generate alerts based on threshold rules (cash transactions above $X, wire transfers to high-risk jurisdictions) and pattern detection models trained predominantly on large commercial bank transaction data. The result: alert volumes that overwhelm small CU compliance teams. A CU with $200M in assets and one full-time BSA officer may receive 200-400 alerts per month, of which 90-95% are false positives — the local contractor who deposits $8,000-$12,000 in cash weekly from residential jobs, the retired farmer who wires funds to family abroad quarterly.

## What Already Exists

Verafin (owned by Nasdaq) dominates CU transaction monitoring. Abrigo offers integrated BSA/AML with its lending and financial analysis platform. Both provide configurable alert thresholds and case management workflows. Verafin's consortium model uses cross-institution data to improve detection. However, the underlying models and rule sets are calibrated for transaction patterns at institutions 10-50x the size of a typical small CU, where the statistical baseline for "normal" is fundamentally different.

## The Customisation Gap

CU-specific BSA/AML tuning requires: (1) baseline transaction modeling at the individual member level — establishing what is normal for each member based on their specific deposit/withdrawal patterns, seasonal income cycles, and historical behavior rather than institution-wide averages; (2) community context features — the CU's geographic area has specific cash-intensive businesses (agriculture, construction, hospitality) where high cash activity is normal, not suspicious; (3) alert prioritization scoring that accounts for the CU's specific risk profile and historical SAR filing patterns, suppressing recurring false positives for known member behaviors while escalating genuinely anomalous activity. The member-level behavioral baseline and community context calibration are the layers that bank-oriented platforms don't provide out of the box.

## Impact If Solved

Reduces BSA officer alert review workload by 60-80% — from 200-400 alerts per month to 40-80 genuine investigation candidates. For a small CU where BSA compliance consumes 0.5-1.0 FTE, this reclaims 15-25 hours per month for substantive investigation and examination preparation rather than dispositioning false positives. More importantly, reduces the risk of genuine suspicious activity being missed in the noise of false alerts — the primary regulatory risk for under-resourced CU compliance programs.
