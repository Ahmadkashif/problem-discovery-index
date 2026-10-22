# A Police Liability Rate That Sees Risk Before the Loss

**Niche:** [[niches/self-insured-benefit-pools/member-liability-rating/profile|Member Liability Rating & Contribution Allocation]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pools rate police liability on officer counts and past losses, so a department's risk shows up in its contribution only after the verdict.
**Tags:** #gradient-boosting #bayesian-inference #regularization #feature-engineering #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price each member's liability coverage close to its own risk (sworn officers, jail beds, payroll, road miles, past losses), and whoever keeps its low-loss members from leaving for commercial quotes at renewal takes the account.

## The Problem
Two cities with 40 sworn officers each pay similar law enforcement liability contributions until one has a seven-figure loss. The pool's loss-control staff often knew which department was the risk: high turnover, no early-warning system for officers, outdated pursuit policy, complaints rising. That knowledge does not enter the rate.

## Why Nobody Has Built This
Large police losses are too rare in one pool to validate risk factors, member boards resist charges based on judgement, and the data on department practices is collected in loss-control visits as narrative.

## What to Build
A credibility-weighted rating model that combines exposure and experience with structured risk-management indicators (policy adoption and update dates, training completion, complaint and use-of-force rates where reported, turnover, supervision ratios), with shrinkage toward pool or consortium priors. Each credit or debit is explained to the member and tied to actions that would earn it back.

## Target Customer
Underwriting and finance directors of municipal and county pools with law enforcement members.

## Impact If Built
Contributions that move with risk before losses arrive, and a price signal that gives councils a reason to fund the fixes loss control recommends.
