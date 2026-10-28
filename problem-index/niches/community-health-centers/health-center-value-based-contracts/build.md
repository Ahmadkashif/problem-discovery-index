# PPS-Floor Reconciliation Inside a Capitated Contract

**Niche:** [[niches/community-health-centers/health-center-value-based-contracts/profile|Health Center Value-Based Contracts & FQHC-Led ACOs]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A health center that accepts a per-member payment still has to prove it received at least its PPS amount for the visits it provided, and the model that shows whether the contract beats PPS does not exist until the state reconciles a year later.
**Tags:** #monte-carlo-methods #survival-analysis #descriptive-statistics #data-integration #revenue-impact #compliance
**Contested on:** Every serious competitor in this niche is fighting to earn quality and shared-savings payments for a health center's attributed Medicaid and Medicare patients on top of the PPS floor, and whoever books the most value-based revenue per attributed patient takes the account.

## The Problem
Under a capitated Medicaid arrangement, the center is paid per member per month whether patients come or not. The state then compares that with what PPS would have paid for the visits delivered. The center's leadership cannot see during the year whether the contract is ahead of or behind PPS, or how attribution churn changes the answer.

## Why Nobody Has Built This
Population health tools model the payer's view of cost and quality. PPS reconciliation sits in state rules and the center's own visit data. Health center APMs are few and state-specific, so vendors have not invested.

## What to Build
A model that combines member months, visits by encounter type, PPS rates, quality incentive terms and attribution forecasts, and simulates year-end revenue under the contract against the PPS counterfactual. It shows which patient segments and visit patterns decide the difference.

## Target Customer
CFOs of centers entering Medicaid APMs or capitated managed-care contracts, and FQHC-led ACOs negotiating them.

## Impact If Built
Knowing mid-year that a contract is 3% behind PPS on a $15M Medicaid book is ~$450,000 of revenue the center can still act on (estimate), through outreach to attributed patients or a renegotiation at renewal.
