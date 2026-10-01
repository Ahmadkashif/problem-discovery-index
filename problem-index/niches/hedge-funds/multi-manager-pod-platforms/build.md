# Pod Skill Measured From Decisions, Not Just P&L

**Niche:** [[niches/hedge-funds/multi-manager-pod-platforms/profile|Multi-Manager Pod Platforms]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform judges a PM on a few dozen independent bets a year and allocates hundreds of millions on the result, while the hundreds of decisions underneath the P&L go unused as evidence.
**Tags:** #bayesian-inference #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to separate a pod's skill from its factor and crowding exposure fast enough to move capital before the drawdown — and whoever measures pod skill first decides how the platform's risk budget is allocated.

## The Problem
Pod P&L over a year is the sum of a modest number of meaningful bets plus factor and market noise. Statistically, separating skill from luck on that sample takes years; platforms decide in months. What they have, and underuse, is the decision stream: every add, trim, exit and sizing change, timestamped, around earnings and catalysts. Decision-level analysis — does this PM add before good news and cut before bad, are their sizing changes informative, does their stock-picking survive factor neutralisation — carries far more statistical evidence than P&L alone.

## Why Nobody Has Built This
Risk systems were built to control exposure, not to evaluate judgement. Decision-level evaluation looks to PMs like surveillance and is sensitive at firms that compete to hire them. And the methods — event-time analysis of trades, hierarchical shrinkage of PM-level estimates — sit between quant research and risk, owned by neither.

## What to Build
A decision-level skill engine: event studies around each PM's trades relative to catalysts; sizing-informativeness metrics (do larger positions earn more residual return); hit rate and payoff ratio after factor and crowding neutralisation; and hierarchical Bayesian shrinkage so a new PM's estimate starts from the platform's prior and moves with evidence. Output a skill estimate with an honest interval, updated weekly, and recommended capital ranges that the allocation committee can override with a recorded reason.

## Target Customer
Heads of portfolio construction and CROs at multi-manager platforms; also allocators to multi-manager funds who want to understand the centre's process.

## Impact If Built
Faster and more accurate separation of skill from noise lets a platform scale capital to genuinely skilled PMs sooner and stop funding unlucky-looking but skilled ones less often — the central economic lever of the platform model.
