# Predicting the Transfer, Not Just the Test

**Niche:** [[niches/mobile-game-publishers/geographic-test-validity/profile|Geographic Test Validity]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A game is validated in three markets and scaled to fifty on the assumption that the numbers carry.
**Tags:** #causal-inference #bayesian-linear-regression #confidence-intervals #gradient-boosting #evaluation-metrics #hypothesis-testing #revenue-impact #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to know whether a number measured in a soft-launch market will hold when the game scales globally — and whoever can predict the transfer takes the account.

## The Problem
Soft launch produces a retention figure and a revenue per player figure from a small set of conventional markets. The global launch spends real acquisition money against those numbers. The relationship between them is not one-to-one: monetisation differs sharply by market, retention differs by genre and market together, acquisition cost structures differ, and platform mix differs. The publisher treats the test number as an estimate of the global number, and it is an estimate of something else.

## Why Nobody Has Built This
The convention works often enough that failures look like execution problems. Modelling the transfer requires many titles across many markets, which exceeds one publisher's history. The test markets were chosen for language and cost reasons and nobody revisits them. And the failures are attributed to the scaling campaign rather than to the validation.

## What to Build
Model the mapping between markets, not just the metric within one. Estimate a transfer function from test market to target market per metric, conditioned on genre and monetisation model, which is the core — the transfer is the quantity the decision depends on and nobody estimates it. Pool across titles hierarchically so a single game's thin evidence borrows strength from the publisher's history, since no one title has enough data. Produce the global forecast with an interval rather than restating the test number, which is what the acquisition commitment should be sized against. Evaluate which test markets are actually predictive for which genres, as that would change the market list itself and is the cheapest available win. Recommend a test market set per title rather than applying a fixed convention. Separate the acquisition cost structure from the game's performance, because a market where installs are cheap flatters every ratio. Account for platform and device mix differences, which shift retention independently of the game. Model the ramp rather than the steady state, since scaling changes the audience composition continuously. Record every past transfer error to calibrate the model against the publisher's own history. And state the markets where the forecast is weakest rather than presenting a uniform global number.

## Target Customer
Mobile publishers, user acquisition leads, publishing partners scaling third-party titles, and games market intelligence vendors.

## Impact If Built
The transfer between a test market and a global audience is the quantity the decision depends on, and nobody estimates it. A hierarchical transfer model conditioned on genre turns a restated test number into a forecast with an interval.
