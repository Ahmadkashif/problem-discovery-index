# Killing Most Prototypes on Three Days of Data

**Industry:** [[mobile-game-publishers|Mobile Game Publishers]]
**Type:** High Impact
**One-liner:** A retention number from a few thousand installs decides whether a concept continues, the threshold is inherited folklore, and nobody knows what the killed games would have done because none of them were allowed to continue.
**Tags:** #survival-analysis #bayesian-inference #confidence-intervals #gradient-boosting #causal-inference #hypothesis-testing #probability-distributions #evaluation-metrics

## The Problem
The publishing funnel runs on early kill decisions. A prototype gets a small install campaign, and within days its day-one retention, cost per install and early session metrics are compared against thresholds. Most concepts are killed. A few advance to a larger test, fewer still to soft launch, and a very small number to scale.

The decision rests on a weak signal. Day-one retention on a few thousand installs carries substantial sampling error before any modelling question arises, and the relationship between it and long-run performance varies enormously by genre, by how much of the game exists in the prototype, and by the acquisition source that supplied the installs. Two prototypes with identical day-one retention can be entirely different propositions, and the threshold does not know that.

The thresholds themselves are usually inherited rather than derived. Numbers circulate in the industry as rules — a day-one figure below which nothing proceeds — and are applied across genres and across a changed economic landscape. They originated when acquisition was cheap and games were shallow; acquisition costs rose substantially after tracking restrictions and the industry moved toward deeper hybrid-monetised games, and the kill metrics did not move with it.

The evidentiary problem underneath is the serious one. Every analysis of what predicts success is conducted on the games that passed the filter, because the ones that failed it were never built out. The funnel therefore validates itself: thresholds look predictive because everything below them was terminated, and there is no counterfactual anywhere in the data.

## Why It's Unsolved
Letting failures through costs money visibly. The value of knowing what a below-threshold prototype would have done is real and diffuse; the cost of funding one is a line in a budget. Every publisher faces that trade and almost all resolve it the same way, which is why the industry has run this funnel for a decade without ever measuring its false negative rate.

The statistical difficulty is genuine too. The outcome of interest is long-run revenue, which is heavy-tailed — a small number of games produce most of the returns — so the quantity being predicted is dominated by the tail that early signals identify worst. Predicting the median outcome well is not the same as identifying the outlier, and the funnel is looking for outliers.

The signal also degraded. Aggregated and delayed attribution means small test campaigns return coarse data, and the privacy threshold suppresses campaign identifiers exactly at the volumes prototype tests run at — so the measurement got worse at the same time the decision got more expensive.

And the organisational structure rewards the current approach. A portfolio of many cheap tests with fast kills is defensible, legible to finance, and produces a steady cadence. A slower funnel that occasionally funds a below-threshold concept requires someone to defend a specific decision that will usually look wrong.

## What a Solution Looks Like
Derive the thresholds from outcomes rather than inheriting them. A publisher's own history of prototypes, their early metrics and their eventual results supports an estimate of the predictive relationship per genre and per prototype completeness — and will very likely show that a single threshold across the portfolio is substantially worse than a genre-conditioned one.

Report the kill decision as a probability with an interval, not a pass or fail. A prototype whose early metrics place it just below a threshold on two thousand installs is not distinguishable from one just above, and the current binary presentation hides that entirely. A decision framed as an expected value under uncertainty, against the cost of the next test stage, is a different and better decision.

Fund a deliberate false-negative allowance. A small, randomised subset of below-threshold prototypes carried to the next stage is the only way to measure what the funnel is missing. It costs money, it is the single highest-value experiment available to a publisher, and it produces the counterfactual on which every other estimate here depends.

Model the tail explicitly. If the portfolio's returns come from rare outliers, the selection criterion should be the probability of being an outlier rather than the expected median outcome — and those rank prototypes very differently. Optimising for the average is how a funnel reliably produces competent games and no hits.

## Impact If Solved
This funnel allocates a publisher's entire development capacity, and its selection rule is folklore validated by a filter that eliminated its own counterfactual. Genre-conditioned thresholds derived from outcomes, probabilistic kill decisions, and a funded false-negative allowance would tell a publisher for the first time what its funnel costs it — and in a business whose returns come from rare outliers, the games being wrongly killed are the entire question.
