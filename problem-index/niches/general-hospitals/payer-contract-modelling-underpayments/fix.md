# The Variance Threshold That Hides Systematic Underpayment

**Niche:** [[niches/general-hospitals/payer-contract-modelling-underpayments/profile|Payer Contract Modelling & Underpayment Recovery]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** Analysts only work variances above a dollar threshold, so a payer that shorts thousands of outpatient lines by $12 each is never caught.
**Tags:** #descriptive-statistics #change-point-detection #evaluation-metrics #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to compute, for every remittance line, what each payer's contract says the hospital should have been paid, and whoever catches the most underpaid dollars inside the contract's dispute window takes the account.

## The Problem
Contract-management worklists are filtered to variances worth chasing one claim at a time, often $100 or more (recalled). Systematic small underpayments, such as a fee schedule loaded a quarter late or a modifier misread, sit under the threshold and add up to real money.

## Why It's Still Broken
The workflow is claim-by-claim. Nobody looks at variances as a pattern by payer, code and date, because the tools present them as individual accounts to follow up.

## What a Fix Looks Like
Aggregate sub-threshold variances by payer, code, modifier and effective date. Run change-point detection to spot when a payer's payment on a code shifted, and generate one batch dispute per pattern with the contract clause and the affected claims attached.

## Who Feels the Pain
Contract analysts with no time for small variances; CFOs whose margin is made of small numbers.

## Impact If Fixed
Batch disputes recover underpayments that were never individually worth chasing, often ~$20,000–$300,000 per pattern (estimate), with one analyst action each.
