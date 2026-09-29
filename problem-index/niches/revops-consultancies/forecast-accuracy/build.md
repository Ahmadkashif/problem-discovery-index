# Making the Forecast Scoreable

**Niche:** [[niches/revops-consultancies/forecast-accuracy/profile|Forecast Accuracy]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The discipline exists to make revenue predictable and has never scored a prediction.
**Tags:** #time-series-forecasting #evaluation-metrics #confidence-intervals #descriptive-statistics #hypothesis-testing #data-integration #revenue-impact #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to improve a forecast whose accuracy nobody can measure, because the series required to score it is destroyed every week — and whoever makes it scoreable takes the account.

## The Problem
A revenue organisation produces a forecast every week: by representative, by manager, by segment, rolled to a company number. It is presented, discussed, and then the underlying fields are updated for next week. No history survives. So nobody can say whether the forecast is biased, whose forecasts are reliable, at what point in the quarter it becomes meaningful, or whether last year's methodology change improved anything.

## Why Nobody Has Built This
The forecast lives in a CRM field that is updated in place, and nobody thought of the field as a series. Consultancies sell methodology rather than instrumentation. Retaining history would expose how bad the forecast has been. And nobody has been asked for it, because the absence is invisible.

## What to Build
Capture the series first, then grade everything against it. Snapshot every forecast at every level on a fixed cadence before it is overwritten, which is the core and is the precondition for every other claim this discipline makes. Score accuracy by horizon, level and segment rather than as one company number, since the bias is highly structured and the aggregate hides it. Measure systematic optimism by representative and by manager, which is the most actionable finding and the most sensitive. Establish at what point in the quarter the forecast becomes informative, as that governs how it should be used. Compare methodologies against the same history rather than against conviction, which is what makes a change defensible. Report calibration rather than a single accuracy number, since a forecast that is confidently wrong differs from one that is honestly uncertain. Include the pipeline snapshot alongside the forecast, so the movement can be explained. Keep the series indefinitely, because the value compounds and the storage is trivial. Feed the measured bias back into the forecast itself, which is a straightforward improvement available immediately. And report the accuracy publicly inside the organisation, which changes forecasting behaviour more than any methodology.

## Target Customer
Revenue operations leadership, RevOps consultancies, CRM and forecasting platform vendors, and revenue intelligence providers.

## Impact If Built
The number that would establish whether anything helped is overwritten by the process that produces it. Snapshotting the series and scoring by horizon, level and segment is the precondition for every claim the discipline makes.
