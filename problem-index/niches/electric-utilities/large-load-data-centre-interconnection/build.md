# A Realisation Model for the Large-Load Pipeline

**Niche:** [[niches/electric-utilities/large-load-data-centre-interconnection/profile|Large-Load & Data Centre Interconnection]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Utilities plan billions of capital spending on large-load requests whose chance of energising nobody estimates request by request.
**Tags:** #survival-analysis #gradient-boosting #bayesian-inference #time-series-forecasting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell a data-centre or factory developer how many megawatts it can have, by when and for what upgrade, while screening out speculative requests, and whoever's answers still hold when the load energises takes the account.

## The Problem
The large-load request log mixes signed, collateralised projects with exploratory enquiries filed at several utilities. Forecasters either include requests at face value, overbuilding into rates, or apply a blanket discount that ignores what is known about each request. Commissions and intervenors now question these forecasts in resource-plan and rate proceedings.

## Why Nobody Has Built This
The pipeline is new at this scale, history is short, and each request's stage history lives in emails and account managers' notes. Withdrawals are rarely recorded with dates or reasons.

## What to Build
A pipeline of record with dated stage gates (enquiry, application, study, agreement, collateral, construction, first energisation, ramp) and requester attributes (developer track record, site control, land and fibre status, multi-utility filing). On that, a survival model of time to energisation or withdrawal per request, updated as stages pass, and a forecast that sums requests as probability-weighted ramps with uncertainty bands for planning and testimony.

## Target Customer
System planning and load forecasting directors at utilities with multi-gigawatt request logs, and the regulatory witnesses who defend those forecasts.

## Impact If Built
Probability-weighted pipelines could cut forecast large-load peak by ~20%–50% against face-value counting (estimate), sizing capital plans for the load likely to arrive and flagging fading requests a quarter or more earlier.
