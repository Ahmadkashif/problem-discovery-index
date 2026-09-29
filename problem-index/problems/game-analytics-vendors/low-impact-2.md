# Generic Predictions Shipped as Features

**Industry:** [[game-analytics-vendors|Game Analytics Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Churn scores and lifetime value estimates ship as standard features fitted generically across a customer base, and studios treat them as facts about their own players.
**Tags:** #gradient-boosting #survival-analysis #confidence-intervals #bayesian-inference #transfer-learning #cross-validation #evaluation-metrics #probability-distributions

## The Problem
Analytics platforms ship predictive features: churn probability, predicted lifetime value, spender propensity, segment labels. They appear in the interface as numbers attached to players, and studios use them for targeting offers, sizing acquisition bids and deciding where to intervene.

The models behind them are fitted generically, frequently across a heterogeneous customer base, on whatever events are common enough to be available for everyone. A puzzle game played in short daily sessions and a strategy game played in long weekly ones have completely different behavioural signatures for the same underlying state, and a model trained across both is fitted to neither.

Calibration is the specific failure. A churn score of 0.8 is used as though it means eighty percent, and typically nobody has checked whether it does for this game. When these numbers drive spending — an acquisition bid based on predicted lifetime value — a miscalibrated estimate costs money directly rather than ranking badly.

Uncertainty is absent from the interface. A prediction for a player with two sessions and one for a player with two hundred are displayed identically, and the first is nearly uninformative.

And the models are static relative to a game that is not. A live game's population and mechanics change continuously, and a model fitted at some point in the past degrades in ways the interface does not indicate.

## What Already Exists
Most analytics platforms ship churn and lifetime value predictions. Larger studios build their own, usually better. Mobile measurement partners provide their own predicted-value models for acquisition. Segmentation tooling is standard. General AutoML capability exists and is occasionally offered for customers to fit their own. Some vendors allow custom models to be uploaded and scored against their event stream.

## The Customisation Gap
Per-game fitting is the obvious requirement and is a product architecture question rather than a modelling one. The vendor has each customer's own event history and could fit per game, with the cross-studio corpus supplying a prior for small or new titles — which is exactly where a generic model is currently worst and a transfer-learned one would be best.

Calibration should be reported and monitored, not assumed. Displaying a reliability measure alongside any shipped prediction, and alerting when it degrades, is a small product change that would change how these numbers are used. The current presentation invites treating them as facts.

Uncertainty must reach the interface. A prediction with two sessions of evidence and one with two hundred should not look the same, and the downstream uses — offer targeting, bid setting — are exactly the cases where acting on a confident-looking uninformative number is expensive.

Retraining against a moving game is the fourth gap. Drift detection on the model's own performance, with automatic refitting and a visible record of when the model changed, is standard practice in mature machine learning operations and is absent from this category's shipped features.

## Impact If Solved
These predictions drive real spending decisions and are presented with a confidence nobody has verified. Per-game fitting with cross-studio priors, reported calibration, visible uncertainty and drift-triggered retraining would make them usable for the decisions they are already being used for — and would turn a checkbox feature into something a studio could defend to its finance team.
