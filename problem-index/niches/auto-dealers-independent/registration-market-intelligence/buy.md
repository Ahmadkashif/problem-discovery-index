# Forecast Tooling Adapted to Registration Lag and Revision

**Niche:** [[niches/auto-dealers-independent/registration-market-intelligence/profile|Vehicle Registration & Market Intelligence Data]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Forecasting platforms assume history is settled; registration history is not — states report late and revise, so the most recent months are always wrong in a direction that is knowable and never modelled.
**Tags:** #time-series-forecasting #autoregressive-models #exponential-smoothing #bayesian-inference #confidence-intervals #evaluation-metrics #feature-engineering #change-point-detection #automation #data-integration

## The Problem
The forecasts the firm sells are built on registration counts that are incomplete at exactly the point where they matter most. States report on their own schedules with lags from days to months, some backfill months later, and revisions are routine. So the trailing three to six months of any series — the part that drives the near-term forecast — understates reality by an amount that varies by state, month, and vehicle type. Analysts know this and correct for it with judgment, applying adjustment factors carried in spreadsheets and refined by experience. The correction is therefore inconsistent between analysts, undocumented, and impossible to validate. Every downstream forecast inherits it, and the client sees a point estimate whose largest single source of error is an informal adjustment nobody has measured.

## What Already Exists
The forecasting toolkit is strong and cheap. Prophet, statsmodels, Nixtla's libraries, and the cloud forecasting services all handle seasonality, hierarchical reconciliation, exogenous regressors, and backtesting well. Commercial platforms add scenario management and collaborative overrides. For forecasting a settled series, nothing needs to be built.

## The Customization Gap
Every one of these treats the historical series as ground truth. Registration data is a series of provisional estimates converging on truth at a rate that differs by state and by month, and no general forecasting tool has a representation for that. Fed a partially reported recent history, they faithfully forecast the understatement forward. The adaptation needed is vintage-aware modelling: retain each data vintage as it arrived rather than overwriting, estimate the reporting completion curve per state and vehicle type from the firm's own revision history, and produce a nowcast of the true recent level with uncertainty attached — before any forecasting model sees the series. That turns the analysts' informal adjustment into a measured, versioned quantity that can be validated against subsequent revisions, and it lets the published forecast carry an interval that honestly reflects reporting uncertainty rather than only model uncertainty. Hierarchical reconciliation then has to run across state, vehicle, and segment dimensions with completion uncertainty propagated through it, which is where off-the-shelf reconciliation stops.

## Target Customer
Heads of forecasting and chief economists at registration intelligence vendors, and the manufacturer planning teams who currently receive point forecasts built on silently understated recent history.

## Impact If Solved
Attacks the largest error source in the firm's flagship product, and does it in a way that is demonstrable — completion models are validated against subsequent revisions, so accuracy improvement is measurable rather than asserted. It also removes a dependency on a handful of analysts' personal adjustment factors, which is an operational risk nobody has written down.
