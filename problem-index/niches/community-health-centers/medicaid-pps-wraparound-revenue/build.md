# A PPS-Due Ledger for Every Medicaid Visit

**Niche:** [[niches/community-health-centers/medicaid-pps-wraparound-revenue/profile|Medicaid PPS & Managed-Care Wraparound Revenue]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A health center is owed its PPS rate on every qualifying Medicaid visit, but no system records that amount next to what the plan and the state actually paid, so the shortfall is found at year-end settlement, if at all.
**Tags:** #gradient-boosting #change-point-detection #feature-engineering #descriptive-statistics #data-integration #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to collect the full Medicaid PPS rate on every qualifying health center visit, including managed-care wraparound and change-in-scope adjustments, and whoever leaves the smallest gap between PPS due and PPS collected per Medicaid visit takes the account.

## The Problem
The billing system knows what was charged and what each payer paid. It does not know what the center was owed. The reimbursement manager rebuilds that from a spreadsheet of rates, plan remittances and state wrap reports, a quarter or a year late. A plan that quietly stops paying same-day behavioral visits shows up as a slow drift in collections that nobody attributes.

## Why Nobody Has Built This
Revenue cycle vendors build for national payer rules, and PPS is fifty different state programmes. Encounter definitions, wrap mechanics and reconciliation timetables live in state plans and provider manuals, not in clearinghouse edits. Each center is too small to fund the build, and from CY2026 HRSA no longer asks for wrap collections in Table 9D (the OMB-approved 2026 UDS tables (ICR 202606-0915-002, approved 3 September 2026)).

## What to Build
A ledger that classifies every visit under the state's encounter rules and attaches the PPS rate in force that day. It records plan payment, wrap claimed and wrap received, and carries the open balance. Change-point detection on payment ratios by plan and code family flags a payer behaviour change within weeks. A running settlement estimate and a change-in-scope monitor sit on top.

## Target Customer
CFOs at health centers with $10M–$100M of Medicaid revenue in managed-care states, and the HCCNs and revenue cycle outsourcers that serve them.

## Impact If Built
Recovering a 1–3% wrap shortfall is worth $200,000–$600,000 a year for a center with $20M of Medicaid revenue (estimate), and catching a plan payment change three months earlier saves a quarter of the underpayment.
