# Forecasting the Spike Before It Arrives

**Niche:** [[niches/game-hosting-providers/capacity-forecasting/profile|Capacity Forecasting & Allocation]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Concurrency multiplies within an hour in a specific region and the capacity was committed on somebody's estimate.
**Tags:** #time-series-forecasting #confidence-intervals #gradient-boosting #optimization-fundamentals #evaluation-metrics #revenue-impact #temporal-fusion-transformers #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to commit capacity in specific regions hours before a demand curve that can multiply within an hour, where being wrong costs either a large bill or the most public failure a multiplayer game can have — and whoever forecasts it takes the account.

## The Problem
Capacity has to be in place before the players arrive, in the right regions, and autoscaling cannot respond fast enough to a curve that multiplies in an hour. The forecast is typically the studio's estimate plus a margin someone chose. When it is too low the result is queues, disconnections and a launch that is publicly judged a failure within minutes. When it is too high the bill is large and visible on margins that do not absorb it.

## Why Nobody Has Built This
The external signals that predict demand — wishlists, preorder counts, streamer schedules, regional interest — sit outside the provider's systems and nobody has assembled them. Each title's launch is treated as unprecedented. The forecast error is absorbed asymmetrically and nobody has priced the asymmetry. And the studio's estimate is the path of least resistance.

## What to Build
Forecast from the signals that exist, and plan against an asymmetric cost. Build a demand model from observable pre-launch signals — wishlists, preorders, regional interest, streamer and creator schedules, comparable titles' curves — which is the core and is the evidence nobody currently uses. Forecast per region rather than globally, since the geographic specificity is what makes autoscaling insufficient. Model the cost asymmetry explicitly, because under-provisioning and over-provisioning are not symmetric errors and treating them as one is the central planning mistake. Produce a distribution rather than a point, as the decision is about the tail and a point estimate cannot inform it. Integrate the event and content calendar, which is the single largest predictable driver after launch. Detect the streamer-driven spike early from live signals and pre-warm, since those are short, sharp and currently unhandled. Learn from every past forecast error across the provider's whole portfolio, which is an asset no individual studio has. Recommend a pre-warm schedule with the associated cost, so the trade is made explicitly rather than implicitly. Handle the launch case separately from steady-state, which behaves entirely differently. And report the forecast and its error publicly to the studio, which is what makes the provider the trusted party in the decision.

## Target Customer
Game hosting providers, studios operating multiplayer titles, cloud capacity teams, and infrastructure cost management vendors.

## Impact If Built
Under-provisioning and over-provisioning are not symmetric errors and treating them as one is the central planning mistake. A regional demand distribution built from observable pre-launch signals turns the estimate into a forecast.
