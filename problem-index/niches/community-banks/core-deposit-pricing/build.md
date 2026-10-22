# Relationship-Level Deposit Beta and Runoff

**Niche:** [[niches/community-banks/core-deposit-pricing/profile|Core Deposit Franchise & Pricing]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** ALCO prices deposits with one beta per product when the bank's own history shows that the same product behaves completely differently for a forty-year customer with a loan and a two-year customer chasing rate.
**Tags:** #bayesian-inference #survival-analysis #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell a bank's ALCO which deposit balances will stay, and at what rate, when the policy rate next moves, and whoever predicts beta and runoff by relationship rather than by product most accurately takes the account.

## The Problem
A community bank's interest rate risk model assumes a decay rate and a beta for each deposit category, usually taken from the ALM vendor's peer study or a deposit study done every few years. During 2022–2024 those assumptions were tested in real time, and many banks found that a minority of relationships drove most of the runoff and rate pressure. The bank priced the whole product to defend that minority.

## Why Nobody Has Built This
Account-level history is locked in the core and hard to extract consistently through product code changes; ALM vendors work from aggregate balance sheet data; benchmark vendors see rates and balances across banks but not the bank's relationship structure. Few community banks have a data scientist.

## What to Build
A hierarchical model fitted on the bank's own account-level history through the full 2022–2025 cycle: balance retention and rate paid as functions of relationship tenure, breadth (loans, treasury management, payroll), account size, local competitor rates and the rate gap. Outputs feed the ALM model's assumptions by segment, price targeted offers to the relationships most likely to leave, and show ALCO the expected cost of a rate move before it is made.

## Target Customer
CFOs and ALCO chairs at community banks between $300M and $10B in assets.

## Impact If Built
Even a small reduction in deposit cost on a community bank's balance sheet is material to earnings (estimate), and the interest rate risk model stops relying on assumptions the last cycle disproved.
