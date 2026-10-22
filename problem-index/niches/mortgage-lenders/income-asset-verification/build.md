# Validation Predicted Before the Order

**Niche:** [[niches/mortgage-lenders/income-asset-verification/profile|Income, Asset & Employment Verification]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lenders order the same verification waterfall for every borrower and discover afterwards which products hit, which validated, and which were wasted.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to verify income, employment and assets from third-party data so the agencies grant rep-and-warrant relief on that component, and whoever validates the largest share of files at the lowest cost per loan takes the account.

## The Problem
A typical sequence tries the payroll-data database first, then a payroll connector, then bank data, then paper. Each attempt costs money whether or not it returns a usable report, and a report that returns may still not validate in DU because the calculated income does not support the application.

## Why Nobody Has Built This
Verification vendors sell their own product, not a recommendation to use a competitor's. The lender holds the history of what was ordered, what hit and what validated across vendors, but in separate invoices and AUS findings.

## What to Build
A model trained on the lender's verification history that predicts, from employer, industry, income type, pay frequency and application data, the probability that each verification route returns a usable report and that DU will validate the component, and orders the cheapest route most likely to validate first. It also warns when the stated income is unlikely to be supported, before the file reaches underwriting.

## Target Customer
Operations and procurement leaders at lenders ordering tens of thousands of verifications a year.

## Impact If Built
Lower verification spend per loan, a higher share of files with rep-and-warrant relief, and fewer surprises when income does not validate late in the process.
