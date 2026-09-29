# The Whole Early Signal, Not One Number

**Niche:** [[niches/mobile-game-publishers/early-signal-modelling/profile|Early Signal Modelling]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A test produces thousands of players' complete behaviour and the decision uses one figure from it.
**Tags:** #survival-analysis #gradient-boosting #confidence-intervals #time-series-forecasting #evaluation-metrics #bayesian-inference #rnns #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to predict a game's 180-day outcome from its first three days of player behaviour, and whoever makes that prediction reliable enough to act on takes the account.

## The Problem
A prototype test yields complete behavioural telemetry for several thousand players: when each session started and ended, how far they progressed, where they stopped, what they engaged with, whether they returned and when. The publisher compresses this to the proportion who came back on day one. That single scalar is a lossy summary of a rich signal, it is noisy at the sample sizes involved, and the model that would use the rest of it is entirely buildable from data already in the warehouse.

## Why Nobody Has Built This
Day-one retention is the industry's lingua franca and switching costs are cultural rather than technical. The outcome labels are few, because most concepts were killed. The relationship is genre-dependent and pooling across genres hides it. And data science teams are pointed at live game monetisation, where the revenue already is.

## What to Build
Model the curve and the behaviour, not the point. Predict long-horizon performance from the full early behavioural record rather than from a retention scalar, which is the core — the shape of the first week's curve carries more information than its level and the standard metric discards the shape entirely. Model churn as a hazard over time rather than as a snapshot, since that is what retention actually is and it changes what early evidence means. Use sequence structure in session behaviour, as the order and pacing of early play distinguishes concepts that look identical on aggregates. Condition on genre and core mechanic, which is where the pooled model fails. Calibrate to realised outcomes and report calibration honestly, because an overconfident prediction here kills good games. Produce prediction intervals that widen appropriately at small sample sizes, which is the defensible output. Identify which early metrics carry signal for which genres, as that alone would improve the existing threshold practice. Provide a forecast update as the test extends, so the decision to run longer has a value attached. Separate the effect of the test audience from the effect of the game, which is the commonest confound. And report against the incumbent threshold rather than replacing it silently, since adoption depends on showing the disagreements.

## Target Customer
Mobile publishers, hybridcasual studios, publishing arms evaluating third-party titles, and games data platform vendors.

## Impact If Built
The shape of the first week's curve carries more information than its level and the standard metric discards the shape entirely. Modelling churn as a hazard over the full behavioural record uses evidence the publisher already paid to collect.
