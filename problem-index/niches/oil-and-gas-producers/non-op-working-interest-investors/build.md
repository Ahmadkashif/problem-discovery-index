# AFE Election Model on Cross-Operator Outcomes

**Niche:** [[niches/oil-and-gas-producers/non-op-working-interest-investors/profile|Non-Op Working Interest Investors]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A non-operator sees AFEs and outcomes from dozens of operators but decides each election from the proposing operator's own estimate.
**Tags:** #gradient-boosting #bayesian-inference #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide each AFE election inside the joint operating agreement's window on better information than the operator's own proposal, and whoever's elected wells return the most cash per dollar committed takes the account.

## The Problem
Each AFE states the operator's cost estimate and, sometimes, its type curve. Operators differ systematically: some overrun costs, some under-deliver production, some are reliable. A non-op with years of AFEs, final costs and production across many operators holds the evidence to correct each proposal, but it sits in PDFs and accounting entries.

## Why Nobody Has Built This
Non-op teams are small and their data arrives in operators' formats. The large public non-ops build internal models; smaller funds and families cannot.

## What to Build
A model that predicts, for each proposed well, the final cost and 12-month production relative to the AFE and type curve. It is trained on the non-op's own history of AFEs, final JIB costs and production, plus public offset production, with operator, basin, spacing and timing effects. It outputs an election recommendation with expected return and downside before the deadline, and a running scorecard of each operator's AFE accuracy.

## Target Customer
Non-op investment teams at public companies, private funds and family offices holding interests across many operators.

## Impact If Built
For a non-op committing ~$300M a year across hundreds of AFEs (estimate), correcting operator optimism by even a few percentage points of return shifts tens of millions toward the better wells.
