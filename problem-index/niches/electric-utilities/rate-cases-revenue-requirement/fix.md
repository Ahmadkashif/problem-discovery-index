# The Adjustment Nobody Can Trace to a Ledger

**Niche:** [[niches/electric-utilities/rate-cases-revenue-requirement/profile|Rate Cases & Revenue Requirement]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** A pro forma adjustment in the revenue requirement workbook is challenged, and the analyst who built it has moved on.
**Tags:** #large-language-models #descriptive-statistics #compliance #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get a revenue requirement through a contested case with the fewest disallowances, and whoever builds the evidentiary record that survives discovery and intervenor cross-examination takes the account.

## The Problem
The revenue requirement is a chain of linked workbooks: test-year ledger extracts, normalising and pro forma adjustments, allocations to jurisdiction and class. When an intervenor asks how an adjustment was derived, the team reconstructs the logic from cell formulas and old emails. Unexplained numbers invite disallowance.

## Why It's Still Broken
Workbooks are rebuilt each case by whoever is available, links to ledger extracts break, and documentation is written after filing if at all.

## What a Fix Looks Like
Lineage tracking across the workbook chain from each filed schedule line back to the ledger accounts and source extracts. A plain-language explanation is drafted for every adjustment at the time it is made and confirmed by the analyst. The same record answers the data request when it comes.

## Who Feels the Pain
Rate analysts under deadline; witnesses defending numbers they did not build; regulatory managers explaining disallowances to executives.

## Impact If Fixed
Each adjustment explained in minutes rather than the ~1–2 days of reconstruction a challenged adjustment takes (estimate), with faster discovery responses and a filing the next team can update rather than rebuild.
