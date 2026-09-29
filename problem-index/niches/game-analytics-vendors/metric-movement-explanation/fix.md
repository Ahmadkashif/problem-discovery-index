# Retention Fell Four Points and Nobody Knows

**Niche:** [[niches/game-analytics-vendors/metric-movement-explanation/profile|Metric Movement Explanation]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The number dropped three weeks ago, several things happened that month, and the explanation in the deck is whichever one the analyst found first.
**Tags:** #quick-win #change-point-detection #descriptive-statistics #evaluation-metrics #confidence-intervals #causal-inference #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to say why a metric moved, when the dashboard can only say that it did — and whoever answers it takes the account.

## The Problem
A metric moves, an explanation is required, and several plausible causes occurred in the same window: a patch, a content drop, a campaign change, a competitor launch, a holiday. The analyst investigates in whatever order occurs to them, finds a plausible correlate, and reports it. It may be right. Nobody can tell, and the organisation then plans around an explanation with no evidential standing.

## Why It's Still Broken
The candidates are never enumerated — an explanation produced by searching until something plausible appears will stop at the first plausible thing, and the alternatives are never listed let alone tested. Change history lives in several systems. The deadline rewards an answer over a correct one. And nobody checks the explanation later.

## What a Fix Looks Like
List the candidates before investigating any of them. Maintain a single timeline of builds, config changes, content releases and campaign changes, which is the fix and is a merge of calendars that already exist. Identify the change point statistically rather than by eye, so the search window is correct. Enumerate every candidate that falls in that window before investigating, which prevents stopping at the first one. Check each candidate against the segments it should have affected, since a cause that should have hit one platform and hit all of them is not the cause. Compare against the same period in previous years for seasonality, which is the commonest overlooked explanation. Report the candidates that were ruled out and why, as that is what makes the surviving answer credible. State when the movement is within historical variation, which is frequently the truth. Record the explanation and revisit it when more data arrives, which is how the team learns whether it guesses well. Keep the timeline current rather than assembling it during an investigation. And say explicitly when the data cannot distinguish two causes, rather than choosing.

## Who Feels the Pain
Analysts producing explanations they cannot stand behind; studios planning around a guess; product leads acting on the wrong cause; and the next investigation, which starts from the same place.

## Impact If Fixed
An explanation produced by searching until something plausible appears will stop at the first plausible thing, and the alternatives are never listed. One merged change timeline plus a statistical change point makes the candidate set explicit.
