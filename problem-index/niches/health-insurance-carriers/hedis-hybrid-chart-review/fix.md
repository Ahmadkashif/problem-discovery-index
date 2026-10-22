# The Over-Read That Fails a Measure in May

**Niche:** [[niches/health-insurance-carriers/hedis-hybrid-chart-review/profile|HEDIS Hybrid Chart Review & Stars Measurement]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Abstraction errors made by seasonal staff in February are found by the auditor's validation sample in May, when it is too late to re-abstract.
**Tags:** #evaluation-metrics #hypothesis-testing #descriptive-statistics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to retrieve and abstract every sampled chart for the hybrid measures before the June HEDIS submission, and whoever closes the most numerator hits that pass the auditor's medical record review validation takes the account.

## The Problem
The auditor's medical record review validation samples abstracted hits and checks them. Too many errors and the measure may have to be reported without its record review hits, usually at a lower rate (recalled). Errors cluster by abstractor and by measure, often from one misunderstood specification, but internal over-reads are thin and late.

## Why It's Still Broken
Quality assurance competes with throughput in a compressed season, temporary staff turn over, and nobody measures error rates by abstractor and measure as the season runs.

## What a Fix Looks Like
Run a statistical over-read from week one, sampling every abstractor's work on every measure, with the sample sized to detect the error rates the auditor will test. Flag drift within days, retrain on the specific rule misunderstood, and re-review that abstractor's earlier hits on the affected measure.

## Who Feels the Pain
Quality directors; abstractors whose errors are found months later; finance teams counting on the measure.

## Impact If Fixed
Measures pass validation, errors are corrected while there is time, and the plan's rate reflects its real performance.
