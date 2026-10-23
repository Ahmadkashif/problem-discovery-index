# Marketing Mix Models Fitted to Visitor Data

**Niche:** [[niches/visitors-bureaus/leisure-campaign-attribution/profile|Leisure Destination Marketing & Campaign Attribution]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer brands already estimate each channel's contribution with marketing mix models; bureaus have the spend data and an outcome series but no model.
**Tags:** #bayesian-inference #linear-regression #regularization #time-series-forecasting #causal-inference #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show that a campaign caused overnight visits that would not otherwise have happened, and whoever produces an incrementality estimate that both the city's auditor and the hotel board accept takes the account.

## The Problem
Bureaus split budgets across search, social, streaming TV, print guides and co-op programmes by habit and agency recommendation, without an estimate of each channel's contribution to visits.

## What Already Exists
Open-source Bayesian marketing mix models (Google Meridian, Meta Robyn, PyMC-Marketing) and the consultancies that run them for consumer brands.

## The Customization Gap
The bureau version needs: an outcome built from visitor data (panel visits, card spend, hotel room nights, tax receipts) with each source's bias and lag; origin-market granularity in place of national sales; strong seasonality and event effects; long lags from inspiration to trip; co-op spend by hotels and attractions included; and priors borrowed across bureaus, since one bureau has only a few years of monthly data.

## Target Customer
Marketing and research leads at state offices and large city bureaus.

## Impact If Solved
A channel budget backed by a model, updated each year, with the uncertainty stated.
