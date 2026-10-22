# Tomorrow's Segregation Excess, Forecast Tonight

**Niche:** [[niches/commodity-brokers/segregation-capital-reporting/profile|Segregation, Capital & Regulatory Reporting]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** FCMs learn at noon whether yesterday's segregation excess was enough, when they could have forecast it the night before.
**Tags:** #time-series-forecasting #bayesian-inference #exponential-smoothing #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce the daily segregation, secured-amount and cleared-swap computations and the monthly capital report correctly before the deadline, with every number traceable for the DSRO, and whoever files every computation before noon with no restatements takes the account.

## The Problem
Each FCM sets a residual interest target, the firm's own money held in segregation as a buffer above what customers are owed. Set it too low and a volatile day risks a shortfall, a reportable event. Set it too high and capital sits idle. Treasury sets the target by experience and adjusts after surprises.

## Why Nobody Has Built This
Back-office vendors compute the requirement as of yesterday; forecasting it needs client wire behaviour, margin rate changes and position data joined in a way their systems don't do.

## What to Build
A nightly forecast, by currency and customer class, of the next day's requirement and excess as quantiles. It is built from open positions, settlement prices, announced clearing-house margin changes, expected wires and client payment patterns, and gives the probability of breaching the residual interest target and a recommended transfer.

## Target Customer
Controllers and treasurers at FCMs with volatile customer bases (agricultural, energy and retail).

## Impact If Built
Fewer near-miss shortfalls on volatile days, less idle capital on quiet ones, and a documented basis for the residual interest target that examiners can review.
