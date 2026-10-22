# Random Samples That Keep Finding Nothing

**Niche:** [[niches/mortgage-lenders/qc-repurchase-defense/profile|Quality Control & Repurchase Defence]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Fix (Pain Point)
**One-liner:** Most of a lender's QC budget re-underwrites clean files, because discretionary selections follow a few fixed rules that have not changed in years.
**Tags:** #random-forests #hypothesis-testing #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to find a file's material defects before the agency does and to resolve the ones the agency finds by cure or fee rather than buyback, and whoever lowers the lender's repurchase cost per loan sold takes the account.

## The Problem
At ACES's ~1.50% average critical defect rate for 2025, a random sample of 150 files a month finds two or three critical defects. The discretionary sample, meant to target risk, is driven by rules like new loan officers, manual underwriting or low credit scores, which overlap heavily with what the random sample already covers.

## Why It's Still Broken
The rules were written once to satisfy the Selling Guide's requirement for discretionary selection, and changing them needs analysis the QC team has no time for. Findings are recorded in prose, so the team cannot easily see which loan characteristics predicted past defects.

## What a Fix Looks Like
Keep the random sample untouched for the defect-rate estimate, and replace the discretionary rules with a ranking refreshed monthly from the lender's own past findings and agency notices: income type, data changes after AUS submission, overridden fraud alerts, condition counts, the underwriter's and partner's history.

## Who Feels the Pain
QC managers reporting defect rates that do not explain agency notices; chief credit officers paying for reviews that find little.

## Impact If Fixed
Same reviews, more defects found before the agency finds them, and a QC programme the agencies see adapting to risk.
