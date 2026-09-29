# A Scored Forecast Record for Residual Value Calls

**Niche:** [[niches/auto-dealers-independent/vehicle-valuation-guides/profile|Vehicle Valuation Guide Publishers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The house publishes residual forecasts that lenders and lessors bet billions against, the market settles every one of them within a few years, and nobody assembles the scorecard.
**Tags:** #time-series-forecasting #autoregressive-models #gradient-boosting #evaluation-metrics #cross-validation #confidence-intervals #change-point-detection #causal-inference #data-integration #revenue-impact

## The Problem
Residual value forecasting is the highest-stakes thing the publisher does. A lessor setting residuals on a model year is committing capital against the publisher's projection, and the projection resolves — the vehicle eventually sells at auction and the truth is known. Across thousands of configurations and many years, the publisher has generated an enormous set of resolved predictions and retains none of them as an evaluated record. Forecasts are produced, published, superseded by the next cycle, and archived as published values. So the organization cannot answer the questions that most determine whether its clients keep licensing: where is the house systematically optimistic, which segments does it call well, how does accuracy degrade with horizon, and did the methodology change three years ago actually help.

## Why Nobody Has Built This
The data is spread across publication vintages stored as current-state tables rather than as versioned forecasts, so recovering what was predicted for a given configuration at a given time is itself a reconstruction project. Scoring also requires a defensible realization target, and choosing one is genuinely contested — realized auction price is the obvious candidate, but mix shifts, condition variation, and channel differences mean a naive comparison penalizes the forecast for things it never claimed to predict. And there is the familiar institutional disincentive: a publisher whose numbers are used to set capital allocation does not volunteer a record of when it was wrong, so nobody has been asked to build one.

## What to Build
An engine that captures every published forecast as a versioned, resolvable claim and scores it as the market settles. Each forecast records the configuration, the horizon, the value, the methodology version in force, and — where the process included one — the analyst override and its rationale. Realization is measured against a stated target defined at publication time, with mix and condition normalized so that the comparison tests what was actually forecast. The resulting record supports what the organization currently cannot do at all: accuracy and bias decomposed by segment, horizon, body style, powertrain, and market, so systematic error becomes visible rather than anecdotal; before-and-after evaluation of methodology changes, so improvement can be demonstrated instead of asserted; and calibrated uncertainty published alongside the point estimate, since a lender setting advance rates benefits far more from a well-characterized interval than from a slightly better midpoint.

## Target Customer
Chief analytics officers and heads of valuation research at guide publishers running 100-500 analysts, and the risk officers at lender and lessor clients who currently take residual forecasts on reputation because no accuracy record is available to evaluate.

## Impact If Built
Creates the asset that most differentiates a valuation publisher and that none currently holds: a measured track record. In a market where several houses publish similar numbers and compete on trust, demonstrated accuracy by segment is the strongest possible commercial claim. Internally it redirects analyst effort toward the segments where the house is measurably weak, which is not where effort currently goes, and it makes methodology investment defensible with evidence rather than argument.
