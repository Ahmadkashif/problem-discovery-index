# The Model Is Accurate on Average and Wrong Where It Counts

**Niche:** [[niches/game-user-acquisition-firms/lifetime-value-prediction/profile|Lifetime Value Prediction]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The model reports excellent error metrics and systematically underestimates the cohorts worth buying.
**Tags:** #quick-win #evaluation-metrics #confidence-intervals #descriptive-statistics #probability-distributions #hypothesis-testing #revenue-impact #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to predict a cohort's lifetime value from a few days of behaviour when most of that value comes from players who have not spent anything yet — and whoever predicts it better takes the account.

## The Problem
The lifetime value model's reported accuracy is good, and the reported accuracy is an average. Because nearly all players are worth little, a model that predicts little for everyone scores well. The cohorts that matter — those containing a disproportionate share of high-value players — are underestimated, so the bids against them are too low, and the firm systematically underbuys exactly the inventory it should be competing hardest for. The metric conceals this completely.

## Why It's Still Broken
The evaluation metric averages over a population where almost everything is near zero — an error measure dominated by the worthless majority will report success while the valuable minority is mispriced, and nothing in the standard reporting shows it. Tail accuracy is not reported. The model appears to work. And the underbuying is invisible because it never happened.

## What a Fix Looks Like
Evaluate by value decile before changing anything about the model. Report model error by realised value decile rather than in aggregate, which is the fix and immediately shows where the model fails. Check specifically whether high-value cohorts are systematically underpredicted, since that is the direction that costs money. Compare predicted against realised cohort value at ninety and one hundred and eighty days for past cohorts, which is a backtest the data already supports. Break the comparison out by acquisition source, as the bias usually varies sharply between them. Estimate the value of the inventory not bought because of underprediction, which is the number that funds any further work. Apply a source-level correction factor as an interim measure, which is crude and better than nothing. Report the share of cohort value coming from the top percentile, so everyone understands the shape they are predicting. Add a tail metric to the model's standard reporting permanently. Widen bidding margins where the model is known unreliable. And stop reporting average error as the headline, which is the change that makes the rest possible.

## Who Feels the Pain
UA teams underbuying their best inventory; publishers whose acquisition underperforms for an invisible reason; data scientists whose model reports success; and the growth that did not happen.

## Impact If Fixed
An error measure dominated by the worthless majority will report success while the valuable minority is mispriced, and nothing in the standard reporting shows it. Error by realised value decile is a backtest against data already held.
