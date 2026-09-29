# Bidding on a Prediction Nobody Has Scored

**Niche:** [[niches/app-marketing-firms/early-value-prediction/profile|Early Value Prediction]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every bid rests on a prediction of six-month value from a few early bits, and almost no team has compared those predictions to what the users were eventually worth.
**Tags:** #survival-analysis #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #monte-carlo-methods #time-series-forecasting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to predict six-month value from a delayed, coarsened and partly suppressed early signal — and whoever does that accurately bids on better information than everyone else in the auction.

## The Problem
The model takes an early signal and produces an estimate of what a cohort will be worth in six months. Budget is allocated on it, bids are set from it, campaigns are paused because of it. Six months later the actual value is known. In most teams nobody goes back and compares. The model is retrained on new data, its fit statistics look reasonable, and whether its predictions have been systematically high or low for a particular network, geography or campaign type is unknown. The discipline's central quantitative artefact is unscored, in an industry that prides itself on being quantitative.

## Why Nobody Has Built This
Realised value arrives months after the prediction and by then the campaigns are gone and the team has moved on — the feedback loop is longer than anyone's attention and nothing holds the record across it. Retaining predictions for later comparison requires a deliberate store nobody set up. Network-side optimisation obscures how much of the outcome the team's own model drove. And an unscored model cannot be shown to be wrong.

## What to Build
Score the predictions. Store every prediction with its context at the time it was made, which is the prerequisite and is the only reason a backtest is possible — retrospective reconstruction does not work because the inputs have changed. Compare against realised value at each horizon and report the error by segment: network, geography, campaign type, cohort size, which is where the systematic biases hide and where correcting them is worth real money. Model the delay structure explicitly rather than treating late-arriving signal as latency, since the delay is randomised in a known way and modelling it recovers information that is currently discarded. Handle suppression as structured missingness rather than dropping the cohort, connecting to the parent niche's fix. Produce calibrated uncertainty and carry it into the bid, so a cohort the model understands poorly is bid on differently from one it understands well — this is the practical payoff of honest uncertainty and nobody does it. Recalibrate continuously from the arriving ground truth, which is the mechanism that makes a model improve rather than merely persist. Separate the team's own prediction from the network's, since both are operating and attributing improvement to the wrong one wastes effort. Estimate the ceiling imposed by the schema, connecting to the sibling niche, because some error is not the model's to fix. Validate against incrementality where available, since an accurate prediction of attributed value is still not what the spend caused. And report prediction error as a standing metric, because a team that knows its own error can bid more aggressively where it is confident.

## Target Customer
User acquisition data science teams, agencies running acquisition at scale, and measurement vendors selling prediction products nobody scores.

## Impact If Built
The feedback loop is longer than anyone's attention and nothing holds the record across it, so the discipline's central artefact is unscored. Stored predictions compared against realised value by network and geography expose systematic biases worth real money, and calibrated uncertainty lets a team bid harder where it knows more.
