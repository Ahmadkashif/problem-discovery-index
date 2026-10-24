# The January Reset Nobody Re-Prices

**Niche:** [[niches/clinical-laboratories/routine-claims-contract-underpayments/profile|Routine Test Claims & Contract Underpayments]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** On 1 January 2027 every percentage-of-CLFS contract reprices, and the lab finds out which payers loaded it wrongly only months later, one puzzling remittance at a time.
**Tags:** #change-point-detection #descriptive-statistics #automation #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to recover underpaid and bundled-away dollars on routine lab claim lines worth a few dollars each, and whoever recovers the most net dollars per thousand claims worked takes the account.

## The Problem
When the schedule changes, payers update their fee tables on their own timetables. Some apply the new rates early or late, some miss codes, some apply the cut twice through a contract that already referenced a frozen base year. The lab's expected-payment tables, if it has them, are updated by hand weeks after the remits start arriving.

## Why It's Still Broken
From 2020 to 2026 the CLFS barely moved for most codes, so labs stopped maintaining schedule-indexed expectations. Contract terms sit in PDFs owned by managed care staff, not by billing, and the quarterly CMS files are not loaded anywhere automatically.

## What a Fix Looks Like
Load the final CY2027 CLFS the week CMS posts it in November 2026. Recompute expected payment for every contract and code before the first January remits, then compare each payer's first two weeks of 2027 payments with expectation code by code. Flag any payer whose ratio shifts in a way the contract does not explain, and send a single dated notice to the payer while the error is fresh.

## Who Feels the Pain
Reimbursement analysts reconciling unexplained short-pays, finance teams forecasting a year of cuts, and outreach directors defending margins to hospital executives.

## Impact If Fixed
Catching a mis-loaded schedule in January rather than June saves five months of underpayment on every affected code. On a payer paying $5M a year, a 3% loading error is ~$60,000 recovered or avoided (estimate) per payer per reset, three resets running.
