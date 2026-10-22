# ALM Deposit Studies Taken Down to the Account

**Niche:** [[niches/community-banks/core-deposit-pricing/profile|Core Deposit Franchise & Pricing]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ALM vendors already sell deposit studies that estimate decay and beta for examiners; they are built on product aggregates and delivered once every few years.
**Tags:** #time-series-forecasting #linear-regression #survival-analysis #evaluation-metrics #data-integration
**Contested on:** Every serious competitor in this niche is fighting to tell a bank's ALCO which deposit balances will stay, and at what rate, when the policy rate next moves, and whoever predicts beta and runoff by relationship rather than by product most accurately takes the account.

## The Problem
Examiners expect the bank's non-maturity deposit assumptions to be supported by the bank's own data. Most community banks commission a deposit study from their ALM provider and reuse it until the next one.

## What Already Exists
ALM providers (ZM Financial, Darling Consulting Group, Plansmith, and correspondent banks' balance sheet services) run deposit studies estimating average life, decay and beta by product from historical balances and rates, and report them in examiner-ready form. The vendors themselves are logged under Credit Unions as [[niches/credit-unions/alm-risk-modeling-vendors/profile|🔍 Asset-Liability & Interest Rate Risk Modelling Vendors]].

## The Customization Gap
The adaptation needs: (1) account-level rather than product-level estimation, segmented by relationship breadth and tenure; (2) refresh every quarter from a core extract instead of a multi-year study; (3) a pricing layer that answers ALCO's question (what happens to cost and balances if we move this rate by this much) rather than only the examiner's; and (4) back-testing of the last study's assumptions against what actually happened, which is the evidence examiners now ask for.

## Target Customer
CFOs who already license an ALM model and want the deposit assumptions to be live rather than periodic.

## Impact If Solved
The bank's deposit assumptions become a quarterly, testable estimate tied to its own customers, usable for pricing as well as compliance.
