# Predicting a Number Whose Mass Is in People Who Have Not Spent Yet

**Industry:** [[game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** High Impact
**One-liner:** Bids are set on predicted lifetime value, most of that value comes from a tiny fraction of players, and at prediction time almost none of them have done anything to identify themselves.
**Tags:** #survival-analysis #probability-distributions #bayesian-inference #gradient-boosting #confidence-intervals #maximum-likelihood-estimation #evaluation-metrics #revenue-impact

## The Problem
A user acquisition team pays for installs and recovers the cost through purchases and advertising revenue over months. The bid is set from predicted lifetime value, estimated from the first few days of a cohort's behaviour.

The distribution being predicted is extreme. A small percentage of players produce the majority of in-app purchase revenue, and the top of that group produces a disproportionate share again. A cohort's realised value is therefore dominated by a handful of individuals, and at day three those individuals have usually not yet distinguished themselves — early spending is weakly related to eventual spending, and many high-value players spend nothing at all in the first week.

The standard modelling response predicts an expected value per cohort, which works better than per player and still handles the tail badly. A model minimising average error will fit the mass of low-value players well and be systematically wrong about the quantity that determines the outcome. Cohorts are frequently scaled on a day-three estimate and revised sharply downward at day thirty, and the spend has already happened.

The measurement constraints compound it. Attribution arrives aggregated and delayed, campaign identifiers are suppressed below privacy thresholds — which happens precisely at the volumes new campaigns and small geographies run at — so the cohorts where exploration happens are the ones with the worst data.

And the number being predicted is not fixed. A cohort's realised value depends on what the game ships afterward: content cadence, event quality, monetisation changes and balance. A cohort acquired before a strong content run performs better than an identical cohort acquired before a weak one, and the model attributes the difference to the acquisition source.

## Why It's Unsolved
Heavy-tailed prediction from weak early signal is genuinely difficult, and the discipline's standard tooling — regression on early metrics, evaluated on average error — is fitted to the wrong part of the distribution. Practitioners know this and the metrics reported internally still centre on mean predicted value against realised value.

The content dependency is structurally awkward. Acknowledging that lifetime value is a joint outcome of the player and subsequent content means UA cannot be evaluated on payback alone, which is how UA is budgeted and how UA managers are assessed. Nobody in either function benefits from opening it, so the confound is left in.

The measurement environment removes the natural remedies. With user-level attribution gone on much of the traffic, per-player modelling is constrained to aggregated cohort signals, and the suppression mechanism biases against exactly the small-volume exploration that would identify new sources.

And the incentives favour optimism in the short run. A higher predicted value justifies more spend, more spend shows growth, and the revision arrives a quarter later when the market conditions have changed enough to blur the attribution.

## What a Solution Looks Like
Predict the distribution, not the mean. The decision is a bid, so the quantity of interest is the expected value including the tail plus its uncertainty — and a model fitted with a loss that respects the heavy tail, evaluated on tail accuracy explicitly, ranks cohorts differently from one fitted on average error. Reporting a predicted distribution with the revision profile attached — how much cohorts like this one typically moved between day three and day thirty — changes scaling decisions directly.

Separate the player from the content. The same acquisition sources are observed across many content periods, which makes the decomposition estimable: how much of a cohort's realised value is attributable to who they were and how much to what the game shipped. That single analysis would let UA and content argue with evidence instead of by assertion, and it would correct a persistent misattribution in source evaluation.

Model the suppression rather than treating it as absence. Threshold-based identifier suppression depends on campaign size, which makes it a modellable missingness mechanism; ignoring it biases against small campaigns and quietly penalises exploration.

Anchor to incrementality on a schedule. Network self-reported performance needs a standing correction factor, and pooling geo and public service announcement tests across a portfolio of titles is what makes that affordable at the scale most games operate.

## Impact If Solved
This prediction allocates the majority of a game's marketing budget and determines whether the business is buying growth or losses. Fitting and evaluating for the tail changes which cohorts get scaled; reporting the revision profile prevents the most expensive recurring error, which is scaling on a day-three number that had not settled; and separating the content contribution corrects an attribution error that currently misprices acquisition sources and misdirects the argument between two functions that both need it resolved.
