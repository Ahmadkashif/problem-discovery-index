# Monthly Auto-Forecasts With Bands That Hold

**Niche:** [[niches/oil-and-gas-producers/pdp-forecasting-reserves-updates/profile|Producing-Well Forecasting & Reserves Updates]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Engineers re-fit thousands of decline curves by hand because auto-forecasts give no honest uncertainty and no record of past error.
**Tags:** #temporal-fusion-transformers #lstms-and-grus #bayesian-inference #time-series-forecasting #confidence-intervals #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to re-forecast every producing well as each month's volumes arrive, and whoever's proved-developed forecasts miss the following year's actual production by the least takes the account.

## The Problem
A reserves engineer responsible for several thousand wells cannot look closely at each one. Auto-fit tools produce a curve, but engineers do not trust it on wells with downtime, workovers or nearby fracs, so they redo the ones that matter and accept the rest. Nobody measures how either set performs a year later.

## Why Nobody Has Built This
Reserves software vendors compete on workflow and economics, not on forecast accuracy, and publishing error would invite scrutiny. Operators lack time to build and validate their own models.

## What to Build
A probabilistic forecaster for every producing well that combines a physics-constrained decline with a learned residual from offsets, downtime, lift changes and nearby completions, and produces P10/P50/P90 monthly volumes. It runs monthly, flags wells whose behaviour has changed, and keeps a forecast-versus-actual record by well type, so engineers review exceptions and the reserves manager sees calibration.

## Target Customer
Reserves managers at operators with thousands of producing wells and semi-annual borrowing base cycles.

## Impact If Built
Cutting engineer time on routine re-forecasting by ~50% (estimate) frees reserves teams for the wells that matter. Reducing systematic overstatement of proved-developed volumes by a few percent avoids reserve write-downs and borrowing-base surprises.
