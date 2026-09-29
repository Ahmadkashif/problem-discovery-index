# Experimentation Practice From Consumer Tech

**Niche:** [[niches/robo-advisors/drawdown-intervention/profile|Drawdown Intervention]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer technology runs thousands of controlled experiments a year on outcomes that barely matter, and advice platforms run none on the one that does.
**Tags:** #causal-inference #hypothesis-testing #evaluation-metrics #confidence-intervals #monte-carlo-methods #descriptive-statistics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to find out what actually stops a client selling at the bottom — and whoever has run the experiments owns causal evidence nobody else in the industry has.

## The Problem
Online experimentation is a mature engineering discipline: assignment infrastructure, sequential testing, variance reduction, heterogeneous effect estimation, guardrail metrics, and governance for what may be tested. It is applied routinely to button colours. The intervention that determines whether a client's retirement is materially worse has never been through it.

## What Already Exists
Experimentation platforms with assignment and analysis; sequential and always-valid testing methods; variance reduction and covariate adjustment; heterogeneous treatment effect estimation; and experiment governance and ethics review.

## The Customization Gap
The adaptation is to a rare, high-stakes, supervised setting. It requires: (1) experiments that run during unpredictable market events rather than continuously, so designs must be pre-registered and dormant — this is the substantive adaptation and is why the practice has not transferred; (2) outcomes measured in realised financial harm rather than in conversion, which changes power calculations and guardrails entirely; (3) a supervision and fiduciary frame, where every arm must be defensible as advice and the ethics review is genuinely load-bearing; (4) small effective sample sizes in any single event, since only a fraction of clients are at risk; and (5) results that must hold across regimes, where consumer tech can simply re-run next week.

## Target Customer
Product, data and investment leadership, compliance functions who must approve the designs, and experimentation vendors for whom regulated advice is unentered.

## Impact If Solved
The discipline is mature and is applied to trivia. Adapting pre-registered, dormant designs to rare market events is the missing piece, and it makes the highest-stakes intervention in the product testable.
