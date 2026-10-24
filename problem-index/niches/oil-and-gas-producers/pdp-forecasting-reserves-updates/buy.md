# Demand-Forecasting Platforms Adapted to Decline Curves

**Niche:** [[niches/oil-and-gas-producers/pdp-forecasting-reserves-updates/profile|Producing-Well Forecasting & Reserves Updates]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail and supply-chain forecasting platforms already produce calibrated forecasts for millions of series; a producing well is a series with physics and reserves rules attached.
**Tags:** #time-series-forecasting #exponential-smoothing #bayesian-inference #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to re-forecast every producing well as each month's volumes arrive, and whoever's proved-developed forecasts miss the following year's actual production by the least takes the account.

## The Problem
Forecasting thousands of wells monthly with uncertainty is a scaled time-series problem, the same shape as forecasting demand for every product in every store. Reserves engineers do it with tools built around one curve at a time.

## What Already Exists
Hierarchical probabilistic forecasting platforms and libraries used in retail and supply chain (cloud forecasting services, open-source panel forecasting libraries) that forecast large panels with quantiles and automatic backtesting.

## The Customization Gap
Decline physics as constraints (monotone decline, b-factor bounds, terminal decline), handling of shut-ins and downtime as censoring rather than demand drops, offset-completion interference as an event, aggregation to lease and reserve category, and SEC-style reasonable-certainty rules for proved volumes. Exports must load into ARIES, PHDwin or ComboCurve.

## Target Customer
Operators with data science teams who want enterprise forecasting infrastructure rather than another reserves tool.

## Impact If Solved
Reusing a scaled forecasting platform lets a team of two forecast ~20,000 wells (estimate) monthly with automatic backtests, against the weeks per cycle the same team now spends refitting curves by hand.
