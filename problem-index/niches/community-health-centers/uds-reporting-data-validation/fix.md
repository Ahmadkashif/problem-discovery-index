# Reviewer Questions Answered From Memory in March

**Niche:** [[niches/community-health-centers/uds-reporting-data-validation/profile|UDS Reporting & Data Validation (CY2026 Tables)]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** After submission, HRSA's UDS reviewer asks why a cell moved or fails an edit, and the analyst reconstructs the answer from queries she ran weeks ago because nothing ties each number to the records behind it.
**Tags:** #descriptive-statistics #hypothesis-testing #data-integration #compliance #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce a health center's UDS tables directly from patient-level records, and whoever submits the CY2026 report with the fewest unresolved HRSA edit flags at review takes the account.

## The Problem
"Why did your hypertension patients fall 12%?" The real answer may be a value-set change, a merged site or a lost interface. Finding it means re-running extracts after the data has moved on.

## Why It's Still Broken
Reports are produced as static extracts. Neither the EHR nor the analytics layer snapshots the patient list behind each cell at submission.

## What a Fix Looks Like
Freeze the patient-level lineage of every cell at submission, compare it with last year's lineage, and pre-write explanations for every cell that moved more than its peer range, ready for the reviewer before the question arrives.

## Who Feels the Pain
UDS analysts and quality directors in February and March, and CEOs who sign the report.

## Impact If Fixed
If a center fields ~15 reviewer questions a year at ~2 hours each (estimate), pre-written explanations save ~30 hours and avoid late corrections to published data.
