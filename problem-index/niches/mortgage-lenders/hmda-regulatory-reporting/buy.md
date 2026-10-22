# Data Quality Platforms Adapted to HMDA Edits

**Niche:** [[niches/mortgage-lenders/hmda-regulatory-reporting/profile|HMDA & Regulatory Data Reporting]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data teams already run automated data-quality tests on every pipeline; HMDA data is still tested once a year.
**Tags:** #data-integration #descriptive-statistics #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce a HMDA register and NMLS Mortgage Call Report that pass every edit and an examiner's sample test without a pre-deadline scrub, and whoever catches data-field errors at the point of origination rather than in February takes the account.

## The Problem
HMDA and call-report data flow from the origination system into reports through extracts nobody tests continuously, so drift (a new loan program coded differently, a changed field mapping) shows up at filing time.

## What Already Exists
Data-quality and observability tools (Great Expectations, Monte Carlo, dbt tests) that run declarative checks on data pipelines and alert on anomalies.

## The Customization Gap
The HMDA layer: the platform's syntactical, validity and quality edits encoded as continuous tests; cross-field consistency rules from the filing instructions; reconciliation between the HMDA register, the Mortgage Call Report's loan activity and the lender's funded-loan records; tests that trace each field to the origination-system field and document it came from; and quarterly views for lenders above the 60,000-record threshold.

## Target Customer
Compliance and data teams at lenders large enough to run a data warehouse.

## Impact If Solved
Reporting drift caught the week it starts, and filings that reconcile across HMDA, call reports and finance.
