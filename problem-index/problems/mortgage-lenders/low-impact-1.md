# Post-Closing QC Inside the 90-Day Cycle

**Industry:** [[mortgage-lenders|Mortgage Lenders]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every agency seller runs the same monthly post-closing QC cycle (sample, re-underwrite, reverify, rebut, report to management in 90 days) on generic audit software and outsourced reviewers, and samples mostly at random when the risk is concentrated.
**Tags:** #random-forests #gradient-boosting #hypothesis-testing #evaluation-metrics #large-language-models #compliance #workflow-orchestration #automation

## The Problem
Fannie Mae requires a lender to select loans for post-closing QC at least monthly: a random sample of at least 10% of what it originates (or a statistical sample at 95% confidence and 2% precision), plus discretionary selections aimed at higher-risk loans. Each selected file is re-underwritten, its income, employment and assets reverified with third parties, its appraisal reviewed, and every finding classified by severity. Findings go to operations for rebuttal, then to senior management in a report, and the whole cycle must finish within 90 days of the month of disbursement, shortened from 120 days in 2023. A lender closing 1,500 loans a month reviews 150 or more files every month (estimate), usually through an outsourced QC firm, and repeats the process for FHA and VA with their own requirements.

The cycle is mechanical and the output is thin. The random sample spends most of the reviewers' time on clean files, while the discretionary selection is driven by a few simple rules (new loan officers, low credit scores, manual underwriting). Findings are written in each reviewer's own words, so trend reporting across months rests on someone recoding them by hand.

## What Already Exists
ACES Audit Technology and similar QC platforms manage samples, checklists, findings and reporting, and outsourced QC firms supply reviewers. Generic audit-management tools (AuditBoard, Workiva) and BI dashboards cover the reporting. The agencies publish defect taxonomies, and Fannie Mae's and Freddie Mac's own quality tools show how a lender's delivered loans compare.

## The Customisation Gap
The generic tools manage the checklist; they do not decide what to review. The mortgage-specific logic is: discretionary selection driven by a risk model trained on the lender's own past findings and the agencies' defect notices, not by fixed rules; severity classification mapped to the agency taxonomy so findings are comparable with what Fannie Mae and Freddie Mac report back; a 90-day cycle tracker that flags rebuttals at risk of missing the reporting deadline; reverification routed by document type (IRS transcripts, written verifications, bank statements); and findings linked to the underwriter, processor, loan officer and branch so management reporting points at causes. Each lender builds a version of this in spreadsheets around the QC platform.

## Impact If Solved
Risk-ranked discretionary sampling finds more of the defects that matter with the same review budget, and lets the lender show the agencies a QC programme that learns. At $300–$600 per outsourced file review (estimate), redirecting even a third of discretionary reviews from clean files to high-risk ones changes the yield of a six-figure annual QC spend without adding reviewers.
