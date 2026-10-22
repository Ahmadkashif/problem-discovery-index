# A Running Solvency Horizon for a Closed Group

**Niche:** [[niches/self-insured-benefit-pools/retiree-medical-trusts/profile|Retiree Medical VEBAs & OPEB Trusts]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A retiree trust learns its projected depletion date once a year from a valuation, long after the trend and mortality that moved it.
**Tags:** #survival-analysis #monte-carlo-methods #time-series-forecasting #bayesian-inference #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to cut a closed retiree trust's cost per retiree without cutting benefits, and whoever moves the most Medicare-eligible retirees onto group Medicare Advantage or subsidised exchange coverage with no loss of benefit takes the account.

## The Problem
Trustees must decide when to change benefits, subsidies or carriers to keep a closed trust solvent for its youngest retirees. The annual valuation gives one projected date under one set of assumptions. Medical trend, Medicare Advantage rate changes, drug costs and investment returns move it all year.

## Why Nobody Has Built This
Valuations are produced by consulting actuaries on an annual cycle for accounting and funding, not as a running decision tool, and smaller trusts cannot afford more frequent studies.

## What to Build
A monthly solvency model for the closed population: survival curves by cohort, claims trend by coverage type, carrier rate changes, and asset returns, simulated together to give the probability the trust lasts past each year. Trustees test benefit and carrier options against it and see each option's effect on the youngest cohort.

## Target Customer
Executive directors and trustees of union and employer VEBAs and public OPEB trusts without in-house actuarial staff.

## Impact If Built
Trustees act on a moving horizon rather than a once-a-year number, and make smaller changes earlier instead of large ones late.
