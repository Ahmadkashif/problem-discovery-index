# A Pacing Model That Learns Each GP's Own Call Pattern

**Niche:** [[niches/pension-funds/commitment-pacing-liquidity/profile|Commitment Pacing & Liquidity Planning]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pacing studies forecast calls from generic vintage curves while the plan holds years of evidence on how fast each of its own GPs actually calls and returns capital.
**Tags:** #time-series-forecasting #bayesian-inference #monte-carlo-methods #confidence-intervals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to forecast the programme's capital calls, distributions and NAV under stress well enough to set next year's commitment budget, and whoever keeps the plan inside its allocation ranges through a drawdown without forced sales of liquid assets takes the account.

## The Problem
A pacing study assumes a fund calls, say, a quarter of commitments in year one and distributes on a standard curve. Real GPs differ. Some deploy fast and use subscription lines, and some distribute slowly in weak exit markets. A plan with 300 fund interests holds the evidence but uses an average.

## Why Nobody Has Built This
Pacing is sold as an annual consultant deliverable, and the models are built to be explainable to a board, not to be learned. Fund histories are short and the last cycle was unusual, so a GP-specific model needs proper shrinkage toward peers.

## What to Build
A hierarchical Bayesian cash-flow model at fund level, with a GP-specific pacing parameter shrunk toward vintage and strategy priors and conditioned on public-market paths. Monte Carlo aggregation gives programme-level calls, distributions and NAV with intervals, plus the probability of breaching each allocation range under stress scenarios. It updates every quarter from statements, and the commitment budget it recommends is tied to the plan's benefit outflows.

## Target Customer
CIOs and heads of private markets at plans with large programmes; consultants who want a better engine behind their pacing studies.

## Impact If Built
Fewer forced sales in drawdowns, fewer missed targets from over-caution, and a commitment budget the board can see re-forecast quarterly rather than defended once a year.
