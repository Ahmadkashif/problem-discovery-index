# Conditions Returned in Pieces

**Niche:** [[niches/mortgage-lenders/the-mortgage-underwriter/profile|The Mortgage Underwriter]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Fix (Pain Point)
**One-liner:** Processors send conditions back one or two at a time to show progress, and each partial return costs the underwriter another pass through the file.
**Tags:** #workflow-orchestration #automation #descriptive-statistics #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to let an underwriter clear a file in one full review with every income and asset figure traced to its source, and whoever cuts condition re-reviews without moving the lender's QC defect rate takes the account.

## The Problem
An approval with eight conditions comes back in four batches over a week. Each batch goes into the underwriter's queue as a new task, and each requires reopening the file and reorienting before the new documents can be judged.

## Why It's Still Broken
Processors are measured on how fast they submit conditions and loan officers push for visible movement, while underwriters are measured on turn time per submission, which rewards clearing what arrived rather than asking for the rest. Neither metric counts total underwriter touches per loan.

## What a Fix Looks Like
Measure touches per loan by processor and branch; hold partial submissions until the file is complete or a set time has passed, unless a condition blocks others; and show the underwriter a single checklist of what is still outstanding when a batch arrives.

## Who Feels the Pain
Underwriters; processors caught between loan officers and underwriting; borrowers whose closings slip.

## Impact If Fixed
A queue rule and a new metric remove repeated reviews without any new technology, recovering a meaningful share of underwriter time in peak months (estimate).
