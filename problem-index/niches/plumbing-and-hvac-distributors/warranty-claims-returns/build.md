# A Claim Pre-Checker Trained on Each Manufacturer's Rejections

**Niche:** [[niches/plumbing-and-hvac-distributors/warranty-claims-returns/profile|Warranty Claims & Defective-Part Returns]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The reasons manufacturers reject warranty claims are knowable in advance, and nobody checks for them before the claim is filed.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn each warranty replacement handed across the counter into a claim the manufacturer pays on first submission, and whoever posts the highest first-pass paid-claim rate takes the account.

## The Problem
A clerk files a compressor claim; three weeks later it comes back rejected because the unit was never registered and the base warranty term had expired by the serial date. The part was given away in July. Most rejections fall into a handful of reasons per manufacturer (estimate), but the clerk learns them one rejection at a time.

## Why Nobody Has Built This
Rejection histories sit in each manufacturer's portal; distributors rarely export them, and no vendor has assembled them across brands.

## What to Build
A model trained on the house's claim history with each manufacturer's acceptance and reason codes, using serial-date decoding, registration status, install date, model family, defect code, photos present and time since replacement, that scores every claim before filing and names the fix. A demo works on a synthetic claim set built from public warranty terms.

## Target Customer
Warranty managers and controllers at HVAC and water-heater distributors.

## Impact If Built
If ~5–15% of claims are now rejected (estimate) and half of those are preventable, a distributor filing ~20,000 claims a year (estimate) recovers hundreds of thousands of dollars of credits it now writes off.
