# A PBJ Pre-Submission Auditor That Predicts Star Effects

**Niche:** [[niches/skilled-nursing-facilities/pbj-staffing-reporting/profile|PBJ Submission & Staffing Data Reconciliation]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A facility submits its quarterly staffing file without knowing whether it will trigger a CMS audit or what it will do to its staffing star.
**Tags:** #hypothesis-testing #gradient-boosting #time-series-forecasting #evaluation-metrics #compliance #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn payroll, timeclock and agency invoices into a PBJ file that matches the hours actually worked, and whoever's submissions pass CMS's PBJ audits and never cost the facility a staffing star takes the account.

## The Problem
PBJ files are validated for format but not for plausibility before submission. A quarter with missing agency hours, a mis-mapped job code or a census mismatch looks like understaffing on Care Compare. A pattern of implausible data can fail a CMS audit, which now excludes the facility from the risk-based survey.

## Why Nobody Has Built This
Payroll vendors treat PBJ as an export. Analytics vendors look at PBJ after CMS publishes it. Nobody sits between the payroll file and the submission, comparing it with the facility's own history, its peers and the star thresholds.

## What to Build
A pre-submission check that scores each day and job code for implausibility against the facility's history and peers (sudden drops in RN hours, weekends with no aides, hours without matching census). It reconciles against timeclock and agency invoices, and estimates the staffing measures and star the file will produce, using CMS's published method on public data. It flags fixable errors before the deadline and keeps an audit-ready reconciliation trail.

## Target Customer
Payroll and compliance managers at chains; independents through their payroll vendor or consultant.

## Impact If Built
Fewer stars are lost to data errors and fewer audits fail; 242 facilities were excluded from the risk-based survey in June 2026 for a failed PBJ audit (CMS QSO-26-14-NH). The facility also knows its staffing rating before the public does.
