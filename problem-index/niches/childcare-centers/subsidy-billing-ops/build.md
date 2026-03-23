# Multi-Payer Billing Reconciliation Engine

**Niche:** [[niches/childcare-centers/subsidy-billing-ops/profile|Subsidy & Mixed-Payment Billing Operations]]
**Industry:** [[industries/childcare-centers|Childcare Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system reconciles what a center billed across 3-4 payment sources per family against what was actually received from each source — directors discover revenue leakage months later when bank deposits don't match expectations.
**Tags:** #isolation-forest #anomaly-detection #tabular-ml #revenue-impact #data-integration

## The Problem
A center billing 80 families where 30 receive state subsidies, 20 use FSA, and all pay some co-pay or private rate generates 150+ individual payment streams per month across different payers, payment cycles, and amounts. The state subsidy payment arrives 30-60 days after the service month, often for a different amount than claimed (adjusted for absences, unauthorized hours, or rate changes). The parent co-pay is collected weekly via autopay but must be recalculated when the subsidy amount changes. FSA reimbursement requires the center to issue compliant receipts with specific tax ID and dependent information. No system currently ties these streams together at the family level to show: "For the Smith family in October, we billed $1,800 total — $1,200 to the state (received $1,080 due to 2 absence deductions), $400 co-pay from parent (collected in full), $200 FSA-eligible (receipt issued, reimbursement status unknown) — net variance: -$120, action needed." Directors discover these variances only through quarterly manual audits, if at all.

## Why Nobody Has Built This
The reconciliation logic is state-specific: each state's subsidy program has different payment calculation rules, absence policies, rate schedules, and adjustment mechanisms. Building a multi-state reconciliation engine requires encoding the billing rules for 50+ state subsidy programs (plus DC and territories), each of which changes annually. The data also lives in separate systems — subsidy claims in the state portal, parent payments in the childcare platform, FSA receipts in a separate tracking system, and bank deposits in accounting software. No single vendor has access to all four data sources simultaneously.

## What to Build
A reconciliation layer that ingests billing data from the childcare management platform, subsidy claim/payment data from state portals (via API or file import), parent payment collection data, and bank deposit records. It performs automated three-way matching at the family level: billed amount vs. received amount vs. expected amount, flagging variances with root cause classification (absence deduction, rate change, claim rejection, parent payment failure, timing lag). Monthly reconciliation reports show total revenue leakage by source, with drill-down to individual family-level discrepancies and recommended actions (resubmit claim, adjust co-pay, issue FSA receipt).

## Target Customer
Center Directors and Business Managers at the estimated 120,000+ centers that serve at least some subsidized families — particularly multi-site operators where reconciliation complexity scales multiplicatively across locations and states.

## Impact If Built
Centers recover an estimated 3-5% of subsidy revenue currently lost to undetected underpayments, unchallenged absence deductions, and missed resubmission windows — worth $5,000-$15,000 annually per center. Reduces billing reconciliation labor from 15-20 hours/month to under 3 hours, freeing director/business manager time for enrollment growth and parent relationships.
