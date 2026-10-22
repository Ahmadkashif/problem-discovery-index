# Pensionability Review on Every Payroll File

**Niche:** [[niches/pension-funds/employer-contribution-reporting/profile|Employer Contribution Reporting & Pensionable Pay Review]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every payroll file is checked for format and almost none are checked for whether the pay in them should count toward a pension.
**Tags:** #gradient-boosting #change-point-detection #k-means-clustering #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to validate each employer's payroll report against the plan's pensionability rules in the pay period it arrives, and whoever catches the most non-pensionable pay and tier errors before they reach a benefit calculation takes the account.

## The Problem
An employer adds a new pay code for a retention bonus and reports it as base pay. A member's earnings jump 25% in the last three years before retirement. A part-time employee is reported with full-time service. Each passes format validation. Each becomes a problem at retirement, when the compensation review finds it and the benefit must be recalculated.

## Why Nobody Has Built This
PAS vendors build portals to accept files and post contributions. Pensionability is treated as a policy matter for staff, and the labelled history that would train a model (compensation reviews, audit findings, disallowed-compensation determinations) sits in case files, not in the system.

## What to Build
A review layer on the portal. It applies the plan's pay-code rules by tier and bargaining unit, and clusters each employer's pay-code vocabulary to spot new or misused codes. Per-member change-point detection flags spikes in the final-average window. A classifier trained on past compensation reviews and audits ranks records by risk. Flagged records go back to the employer with the rule cited, and the review history feeds employer audit selection.

## Target Customer
Directors of employer services and employer audit managers at statewide and large county systems.

## Impact If Built
Pensionability errors are corrected by a payroll clerk in the same pay period instead of by a benefit cut decades later. Employer audits target the employers whose files show risk.
