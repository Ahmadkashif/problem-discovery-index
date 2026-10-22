# A Lift Test Every Data Vendor Has to Pass

**Niche:** [[niches/credit-card-issuers/acquisition-underwriting/profile|Acquisition & Underwriting Decisioning]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every alternative-data vendor claims lift on thin-file applicants, and issuers evaluate each claim with a bespoke retro study that takes months and is never comparable to the last one.
**Tags:** #gradient-boosting #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #feature-engineering #data-integration
**Contested on:** Every serious competitor in this niche is fighting to approve, and set the first line for, applicants the bureau file describes poorly — thin files, recent immigrants, near-prime rebuilders — at a loss rate it can predict in advance and explain in an adverse action notice, and whoever does that best takes the account.

## The Problem
An acquisition risk team is pitched a new data source every few weeks: cash-flow attributes, rent and utility payments, payroll data, device and email signals, an alternative score. Each vendor offers a retro study — they append their data to a sample of the issuer's past applications and show the improvement in Gini or KS. The issuer's analysts then rebuild the study themselves, because the vendor's sample, outcome window and baseline differ from theirs, and because the population that matters (applicants the issuer declined, whose outcomes it never saw) is the one a retro study cannot cover.

## Why Nobody Has Built This
Each issuer treats its application archive and performance data as proprietary, and the bureaus and score vendors who could standardise the test are also the ones being tested. Reject inference is genuinely hard, and model risk teams demand documentation that a vendor deck does not provide.

## What to Build
A standard evaluation harness inside the issuer: a frozen, point-in-time application archive with outcomes; a fixed baseline (the current score and strategy); a protocol for appending any vendor's data under the same permissible-purpose controls; and a report of incremental lift by segment (thin file, near-prime, recent immigrant), stability over time, reject-inference estimates with stated uncertainty, fair-lending disparity checks, and the cost per incremental good account. The output is the document model risk and fair lending need to approve or reject a source.

## Target Customer
Heads of acquisition risk and model risk at mid-size and large issuers, and the credit union service organisations that underwrite for many small issuers.

## Impact If Built
Data-source decisions in weeks instead of quarters, comparable across vendors, with the approval documentation produced as a by-product.
