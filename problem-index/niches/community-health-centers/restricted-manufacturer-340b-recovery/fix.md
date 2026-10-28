# Rebate Denials Nobody Appeals

**Niche:** [[niches/community-health-centers/restricted-manufacturer-340b-recovery/profile|Restricted-Manufacturer Claims Data & 340B Rebate Claims]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** Under the rebate pilot a manufacturer may deny a claim with documentation within 10 days, and a health center with one part-time 340B coordinator will let most denials stand.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to recover the 340B discount on restricted manufacturers' drugs through their claims-data conditions and, from January 2027, the rebate pilot, and whoever recovers the most 340B savings per eligible restricted-drug prescription takes the account.

## The Problem
A denial says the claim was a duplicate discount, a non-patient or an incomplete file. Each needs evidence from the chart and the Medicaid record, and the coordinator has no queue.

## Why It's Still Broken
The workflow is new from January 2027, and health centers have small 340B teams. Administrators own the claims but not the denials.

## What a Fix Looks Like
A denial queue sorted by dollars and by likelihood of reversal, with the patient eligibility evidence, the Medicaid status and the dispense record attached, and a dispute draft in the format HRSA's dispute process expects.

## Who Feels the Pain
340B coordinators and pharmacy directors.

## Impact If Fixed
If 8% of rebate claims are denied (estimate) and half are reversible, a center claiming $400,000 a year recovers ~$16,000.
