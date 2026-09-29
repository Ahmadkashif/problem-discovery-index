# Long-Horizon Incrementality From Marketing Science

**Niche:** [[niches/game-liveops-services/event-evaluation/profile|Event Evaluation]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Marketing science built incrementality testing and long-term effect measurement because short-window attribution was misleading everyone, and live ops still reports the week.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #time-series-forecasting #evaluation-metrics #survival-analysis #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to measure what an event cost over the following months rather than what it earned in the week it ran — and whoever measures the cost takes the account.

## The Problem
Marketing spent two decades learning that short-window attribution systematically misleads, and built the response: geo and audience holdouts, incrementality testing, long-term brand effect measurement, and models that separate short-run response from lasting equity effects. The parallel is exact — a promotion that lifts this week's sales while eroding the brand is the same object as an event that earns this week while exhausting the player base — and live operations has none of the machinery.

## What Already Exists
Holdout-based incrementality testing; long-term versus short-term effect decomposition; brand equity measurement; promotion-depth erosion analysis; and geo experiment design.

## The Customization Gap
The adaptation is to a captive population inside a product rather than an audience in a market. It requires: (1) holdouts constructed inside the game's own population, which is far easier than geo testing and removes most of the design difficulty — the substantive difference is that the experiment is cheap and nobody runs it; (2) the long-term quantity being player goodwill and engagement rather than brand equity, which needs a behavioural definition rather than a survey; (3) event exposure that is self-selected, since players choose to participate, making the naive comparison badly confounded; (4) a compounding calendar where events interact, unlike largely independent campaigns; and (5) an operator who controls both the treatment and the outcome measurement completely.

## Target Customer
Live game operators, live ops and analytics vendors, product leadership, and marketing measurement firms.

## Impact If Solved
Marketing built incrementality testing because short-window attribution misled everyone. Here the holdout lives inside the game's own population, which makes the experiment cheap — and it still is not run.
