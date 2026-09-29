# Grading the Methods Against Each Other

**Niche:** [[niches/revops-consultancies/methodology-and-scoring/profile|Forecast Methodology & Scoring]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Several forecasting methodologies are sold with conviction and none has ever been compared to another on the same data.
**Tags:** #time-series-forecasting #evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #descriptive-statistics #gradient-boosting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to establish which forecasting method actually predicts best, and where the bias sits, using a retained history — and whoever scores it takes the account.

## The Problem
Revenue forecasting methodologies — weighted pipeline, commit categories, historical conversion, rep judgement, machine-learned scoring — are advocated vigorously and compared never. With a retained history, comparing them is straightforward: run each against the same past quarters and see which predicted better, at which horizon, for which segment. Without it, the choice is made on the consultant's conviction and the organisation's culture, which is how it has always been made.

## Why Nobody Has Built This
Nobody has the history, which is the sibling niche's problem. Comparing methods risks showing that the sophisticated one is not better. Consultancies have positions to defend. And the quarterly rhythm means a fair comparison takes years unless run retrospectively.

## What to Build
Backtest the methods against the same history and report where each fails. Score every available methodology against the retained series at each horizon, which is the core and is the comparison the discipline has never made. Decompose error into bias and variance, since a consistently optimistic forecast and a noisy one need entirely different remedies. Measure bias by representative, manager, stage and segment, as it is highly structured and the aggregate conceals it. Establish the horizon at which the forecast becomes informative, which governs how leadership should use it and is currently assumed. Report calibration, not just accuracy, because a forecast with honest uncertainty is more useful than a confidently wrong one. Adjust the forecast using the measured bias, which is an immediate improvement requiring no methodology change at all. Test whether a proposed change would have helped historically before adopting it, which is the evaluation the discipline lacks. Account for the forecast being a management instrument that changes behaviour when scored. Publish the comparison rather than defending a position, which is how a consultancy differentiates on evidence. And re-run it as the organisation changes, since the right method is not fixed.

## Target Customer
Revenue leadership and operations, RevOps consultancies, forecasting and revenue intelligence vendors, and analytics providers.

## Impact If Built
Several methodologies are advocated vigorously and compared never, because nobody has the history to compare them on. Backtesting them against the same series with bias decomposed by level is the comparison the field has never made.
