# Day One Was Fine and Day Thirty Was Not

**Niche:** [[niches/mobile-game-publishers/early-signal-modelling/profile|Early Signal Modelling]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** A concept clears the threshold, scales, and collapses at week four, and the early data contained the shape that predicted it.
**Tags:** #quick-win #survival-analysis #evaluation-metrics #descriptive-statistics #confidence-intervals #time-series-forecasting #revenue-impact #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to predict a game's 180-day outcome from its first three days of player behaviour, and whoever makes that prediction reliable enough to act on takes the account.

## The Problem
The expensive failure in publishing is not the killed concept — it is the one that passes. A prototype clears day-one retention, receives real acquisition budget, and falls apart weeks later when the content runs out or the loop exhausts itself. The early test contained the evidence: a retention curve decaying at the wrong rate, progression too fast, engagement narrow. None of it was looked at because the gate was a single day-one figure.

## Why It's Still Broken
The gate metric is a level and the failure is a slope — a threshold on one point of a curve cannot see the curve's trajectory, so a concept that starts well and decays steeply passes cleanly. Day-seven data arrives after the decision. Nobody reviews the passes, only the kills. And the failure is attributed to scaling rather than to selection.

## What a Fix Looks Like
Look at the curve's shape, not just its height. Fit the decay rate across the available days rather than reading a single point, which is the fix and needs no new data collection at all. Flag concepts whose curve is steep even when the level clears, since that combination is the characteristic profile of the expensive failure. Show progression pace against content depth, as running out of content is the commonest cause of the week-four collapse and is visible early. Check engagement breadth rather than only frequency, because a narrow loop decays faster. Extend the test by days rather than deciding on day one where the curve is ambiguous, which is cheap relative to the scaling spend at risk. Review the passes with the same rigour as the kills, which no publisher does. Record each scaled concept's early curve against its eventual outcome, so the pattern becomes learnable. Compare the curve against the genre's typical shape rather than against a universal number. Warn before budget commits rather than after, since the decision point is the money. And report the near-threshold passes explicitly, as those are where the errors concentrate.

## Who Feels the Pain
Publishers who committed acquisition budget to a concept that collapsed; teams scaled onto a game that was not ready; analysts who suspected the curve; and the portfolio that funded it.

## Impact If Fixed
A threshold on one point of a curve cannot see the curve's trajectory, so a concept that starts well and decays steeply passes cleanly. Fitting the decay rate on data already collected catches the expensive failure before the budget commits.
