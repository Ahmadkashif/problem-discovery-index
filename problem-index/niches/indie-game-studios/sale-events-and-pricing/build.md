# The Discount Decision With a Number Behind It

**Niche:** [[niches/indie-game-studios/sale-events-and-pricing/profile|Sale Events & Pricing]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most of a game's lifetime revenue comes from discounts chosen by picking a round number.
**Tags:** #revenue-impact #time-series-forecasting #causal-inference #confidence-intervals #evaluation-metrics #gradient-boosting #optimization-fundamentals #automation
**Contested on:** Every serious competitor in this niche is fighting to tell a studio what a discount at a given depth and moment will actually earn over the title's remaining life — and whoever answers it takes the account.

## The Problem
A studio decides to run a sale, picks thirty-three or fifty percent because those are the numbers everyone uses, and observes the result without ever knowing what the alternative would have earned. Over a game's life this decision is made a dozen times and accounts for the majority of revenue after the launch window. There is no forecast, no memory of previous sales' performance, and no model of how each discount changes what the remaining audience is willing to pay.

## Why Nobody Has Built This
Pricing science lives in retail and in large publishers, not in studios of five people. The data needed spans many titles and the platforms hold it. The effect is delayed and confounded with the platform's own event traffic. And the studio's own history is a handful of sales, which is too few to learn from alone.

## What to Build
Forecast the sale and remember the last one. Model units and revenue at each candidate depth against the title's own sales history and comparable titles' trajectories, which is the core — the studio's question is what fifty earns versus thirty-three and nobody answers it. Separate the platform event's traffic from the discount's own effect, since running during a major sale conflates the two and is why studios misread their results. Model cannibalisation across the schedule, as a deep discount changes what the next one can achieve. Recommend the schedule rather than a single sale, which is where the compounding is. Set regional prices against local purchasing power rather than currency conversion, which is a large and entirely mechanical gain. Evaluate bundle participation with the revenue share and the cannibalisation modelled together. Keep a record of every previous sale with its conditions, so the studio accumulates evidence rather than impressions. Report confidence honestly, because these forecasts are weak on thin history and overconfidence here loses real money. Handle the long-tail price expectation, since a title that always discounts trains its audience to wait. And make it a decision support answer rather than a dashboard, as the studio will spend ten minutes on this.

## Target Customer
Indie studios, publishers with catalogues, platform partner managers, and games business intelligence vendors.

## Impact If Built
The studio's question is what fifty earns versus thirty-three and nobody answers it. Modelling depth against the title's own history, with platform event traffic separated out, turns the dominant post-launch revenue decision into an informed one.
