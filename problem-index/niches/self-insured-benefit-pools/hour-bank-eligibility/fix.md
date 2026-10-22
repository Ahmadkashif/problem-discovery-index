# Claims Paid in Months Nobody Was Eligible

**Niche:** [[niches/self-insured-benefit-pools/hour-bank-eligibility/profile|Hour-Bank Eligibility & Self-Pay at Health and Welfare Funds]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Fix (Pain Point)
**One-liner:** When a payroll audit reverses hours or a self-payment bounces, the fund discovers it paid claims for months of coverage the member never earned.
**Tags:** #gradient-boosting #change-point-detection #feature-engineering #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide every member's coverage for next month from hours reported late and by hand, and whoever pays the fewest claims for people who were not eligible while cutting off nobody who was takes the account.

## The Problem
Eligibility is decided before the hours are verified. Payroll audits months later can reverse hours, employers go out of business owing contributions, and self-pay checks fail. The fund then has claims paid for ineligible months, recoverable only from providers or members, often not at all.

## Why It's Still Broken
Eligibility, contributions, audits and claims sit in different systems or with different vendors. Nobody quantifies the exposure until the auditor tests it.

## What a Fix Looks Like
A monthly reconciliation that joins audit findings, delinquencies and failed self-payments to the members and months they affect, sizes the paid claims at risk, and routes recovery or trustee decisions while the amounts are small.

## Who Feels the Pain
Fund administrators and trustees; members hit with retroactive bills; eligibility clerks reversing months of history by hand.

## Impact If Fixed
Exposure caught in weeks rather than at year-end audit, and fewer families billed for care they thought was covered.
