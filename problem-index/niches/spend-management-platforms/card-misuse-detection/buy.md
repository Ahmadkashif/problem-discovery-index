# Internal Fraud Detection From Audit Analytics

**Niche:** [[niches/spend-management-platforms/card-misuse-detection/profile|Card Misuse Detection]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Audit analytics has a mature library of tests for expense and procurement fraud, designed to run once a year on exported data.
**Tags:** #compliance #graph-theory #evaluation-metrics #gradient-boosting #confidence-intervals #descriptive-statistics #automation #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to find the spend that is within policy and still wrong — and whoever detects insider misuse without accusing honest employees takes the risk the rule engine was never built to see.

## The Problem
Internal audit and forensic accounting developed a substantial body of tests for exactly this: duplicate payment detection, round-number and threshold-avoidance analysis, vendor and employee address matching, weekend and holiday transaction review, Benford-style digit analysis, and behavioural red flag libraries. They are well documented and effective. They are also typically run annually by an audit team on a data extract, months after the fact.

## What Already Exists
Audit analytics test libraries for expense and procurement fraud; forensic accounting red flag frameworks; continuous controls monitoring products; vendor master file analysis; and investigation and case management practice.

## The Customization Gap
The adaptation is to continuous operation inside the transaction system. It requires: (1) tests running continuously at the point of transaction rather than annually on an extract, which is the substantive difference and changes detection from forensic to preventive; (2) behavioural modelling supplementing deterministic tests, since the classic library catches the crude cases and misses the patient ones; (3) peer comparison across companies, which no single-entity audit can perform and which the platform can; (4) findings delivered to a controller rather than to an audit team, so the presentation must be non-accusatory and actionable; and (5) false positive costs that are human rather than merely operational, which the annual cadence largely insulated the original from.

## Target Customer
Card operations leadership, customer internal audit and finance, external auditors, and audit analytics vendors running on extracts.

## Impact If Solved
The test library is mature and runs once a year on exported data. Running it continuously at the transaction, with peer comparison across companies, turns forensic detection into prevention.
