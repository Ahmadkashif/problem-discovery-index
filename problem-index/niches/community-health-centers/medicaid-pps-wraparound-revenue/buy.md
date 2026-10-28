# Revenue Cycle Platforms Configured for State PPS and Wrap Rules

**Niche:** [[niches/community-health-centers/medicaid-pps-wraparound-revenue/profile|Medicaid PPS & Managed-Care Wraparound Revenue]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Health center EHRs and revenue cycle platforms bill and post well, but they need each state's encounter definitions, PPS rates and wrap mechanics loaded as rules before they can say what the center is owed.
**Tags:** #feature-engineering #descriptive-statistics #data-integration #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to collect the full Medicaid PPS rate on every qualifying health center visit, including managed-care wraparound and change-in-scope adjustments, and whoever leaves the smallest gap between PPS due and PPS collected per Medicaid visit takes the account.

## The Problem
The center already pays for a billing module and often an outsourcer. Both work denials and posting by payer, and neither models the second payment owed by the state.

## What Already Exists
NextGen, eClinicalWorks, athenaOne and OCHIN Epic billing; revenue cycle outsourcers; clearinghouses; FQHC reimbursement consultancies preparing cost reports and rate requests.

## The Customization Gap
The configuration a health center needs:

- the state's billable-encounter definition, including same-day and provider-type rules, as dated logic;
- PPS rates with effective dates and pending change-in-scope adjustments;
- the wrap mechanism (per-claim, supplemental or annual reconciliation) and its file formats;
- reports of PPS due against collected, by plan, site and service line.

## Target Customer
Reimbursement managers at mid-sized centers that use an EHR vendor's billing module or an outsourcer and lack an in-house reimbursement analyst.

## Impact If Solved
Configured rules turn wrap reconciliation from ~2 days a month of spreadsheet work into a review of exceptions (estimate), and expose shortfalls while they are still collectible.
