# Performance Attribution Adapted to Pods

**Niche:** [[niches/hedge-funds/multi-manager-pod-platforms/profile|Multi-Manager Pod Platforms]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Factor-based performance attribution is a solved product; attributing a pod's return to stock-picking, timing and sizing at decision level is not.
**Tags:** #linear-regression #pca #matrix-decompositions #evaluation-metrics #feature-engineering #data-integration
**Contested on:** Every serious competitor in this niche is fighting to separate a pod's skill from its factor and crowding exposure fast enough to move capital before the drawdown — and whoever measures pod skill first decides how the platform's risk budget is allocated.

## The Problem
Every platform runs factor attribution from a commercial risk model: how much of a pod's return came from market, sector, style and residual. It answers "how much was alpha" and not "where did the alpha come from" — selection, entry timing, exit timing, sizing, or trading around a core position.

## What Already Exists
MSCI Barra and Axioma (now part of SimCorp) risk models with attribution modules, Bloomberg PORT, and in-house systems built on them.

## The Customization Gap
Pods need: decision-level decomposition of residual return into selection, timing and sizing; crowding-adjusted residuals, since a pod's "alpha" may be a crowded trade shared with other platforms; earnings and catalyst windows treated as distinct regimes; and the attribution delivered to the PM as a feedback tool, not only to risk as a control.

## Target Customer
Risk and portfolio-construction teams at multi-manager platforms already licensing a commercial risk model.

## Impact If Solved
Decision-level attribution gives PMs the feedback they cannot get from monthly factor reports, and gives the centre a richer basis for capital allocation than the residual line.
