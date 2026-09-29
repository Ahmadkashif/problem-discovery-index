# Arriving Before They Run Out

**Niche:** [[niches/subscription-commerce/replenishment-subscriptions/profile|Replenishment Subscriptions]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The entire value of a replenishment subscription is that the product arrives as the last one runs out, which is a per-household prediction, and the industry ships on a plan-level schedule.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #revenue-impact #probability-distributions #hypothesis-testing
**Contested on:** Every serious competitor in this sub-niche is fighting to have the next delivery arrive as the last one runs out — and whoever does that keeps the subscriber, because the alternative is a customer who simply buys it when they need it and does not need a subscription at all.

## The Problem
A coffee subscription ships a bag every four weeks. One household drinks it in nine days and runs out for nineteen; another takes eleven weeks and has seven bags in a cupboard. Both cancel, for opposite reasons, and both appear in the churn report as cancellations. The company knows how much it ships and does not estimate how much is consumed, even though the behavioural evidence is abundant: the first household reorders separately and the second skips repeatedly, and both of those are recorded as commercial events rather than as measurements of consumption.

## Why Nobody Has Built This
Cadence was designed as a customer preference rather than as a prediction, so the system has no place to put an estimate. Consumption is unobserved directly, which is treated as making it unknowable rather than as making it an inference problem. Shipping more often increases short-run revenue, so the incentive at the default runs against accuracy. And the two failure modes look identical in a churn report, which hides that half the cancellers wanted more and half wanted less.

## What to Build
Estimate consumption and ship to it. Infer per-household consumption rate from behaviour — skips, delays, separate reorders, quantity changes, engagement with pre-charge reminders, and direct usage where a connected product or a scan provides it — which is a well-posed estimation problem with continuous evidence and is the core of the build. Update the estimate every cycle, since consumption changes with seasons, household size and habit, and a one-time estimate decays. Ship to a target stock-out probability rather than to a fixed interval, which is the inventory framing and makes the trade-off explicit rather than implicit. Adjust quantity as well as timing, since for many products changing the amount is better than changing the frequency and most platforms only offer the latter. Ask directly when uncertain, since a single question — did that last longer or shorter than expected — is cheap, willingly answered, and resolves most ambiguity. Detect the two failure modes separately in the churn data, because they are currently pooled and have opposite remedies. Report predicted stock-out and over-supply rates as operating metrics. And communicate the adjustment, since a customer who sees the company noticing their usage experiences the core promise of the product working.

## Target Customer
Replenishment operators, subscription platform vendors, and the subscribers currently running out or accumulating.

## Impact If Built
Consumption is unobserved and continuously evidenced by skips and reorders that the system records as commercial events. Shipping to a stock-out probability rather than a fixed interval makes the trade-off explicit, and a single question resolves most of the remaining uncertainty.
