# Trend Detection Adapted to Menu Adoption Curves

**Niche:** [[niches/catering-companies/foodservice-market-intelligence/profile|Foodservice Market Intelligence Firms]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Trend detection products find things that are growing fast; the commercially valuable question is whether an item that is growing fast in independent restaurants will reach chain menus in eighteen months, and that is a different problem.
**Tags:** #time-series-forecasting #survival-analysis #change-point-detection #gradient-boosting #feature-engineering #causal-inference #evaluation-metrics #confidence-intervals #automation #data-integration

## The Problem
Clients pay for anticipation. A manufacturer deciding what to develop needs to know which of the hundreds of ingredients currently appearing on ambitious independent menus will diffuse into mid-market chains, which will stay niche, and which are already peaking. Growth rate alone does not answer it — plenty of items grow fast among early-adopter operators and never cross over, while others diffuse quietly through a segment before anyone notices. Analysts make the call from experience and pattern recognition across the many adoption curves they have watched, which is genuine expertise and is neither documented nor evaluated. The firm has, in its own database, the complete adoption history of thousands of prior items and does not use it to inform the next call.

## What Already Exists
Time series and trend tooling is abundant and cheap. Prophet, statsmodels, and the Nixtla libraries handle decomposition, changepoint detection, and forecasting; the cloud anomaly services flag emerging growth; commercial trend platforms in adjacent industries do rank-and-surface well. For finding what is growing, nothing needs building.

## The Customization Gap
All of it models a series in isolation and answers whether it is rising. Menu diffusion is a structured process rather than a free-running series: items move through operator segments in a characteristic order — fine dining and ambitious independents, then fast casual, then chain — with lags that differ by ingredient type, and they arrive attached to other items in recognizable clusters. The right formulation is diffusion across a segment hierarchy with the firm's own history of completed adoption curves as training data, which is a survival-and-diffusion problem, not a forecasting one. The adaptation adds the primitives that requires: operator segment as an ordered dimension rather than a filter, adoption stage inferred from where in that hierarchy an item currently sits, cluster structure so co-occurring items inform each other, and explicit prediction of crossover probability and timing rather than of next period's count. Because the firm has thousands of resolved historical curves, the model can be evaluated honestly on out-of-time data — which also produces the accuracy record analysts' judgment has never had.

## Target Customer
Directors of trend research and client-facing insight leads at foodservice intelligence firms, and the manufacturer innovation teams who buy these calls and currently have no basis for weighing them.

## Impact If Solved
Moves the flagship claim from growth reporting to diffusion prediction, which is what clients actually need and what commands a different price. It also converts the analysts' accumulated pattern recognition into an evaluable asset, and produces the accuracy record that lets the firm argue its calls are better rather than merely earlier.
