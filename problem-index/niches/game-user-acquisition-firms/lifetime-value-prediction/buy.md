# Tail Estimation From Insurance and Finance

**Niche:** [[niches/game-user-acquisition-firms/lifetime-value-prediction/profile|Lifetime Value Prediction]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Insurance and finance built extreme value theory because the tail is the whole risk, and UA models optimise mean squared error.
**Tags:** #probability-distributions #confidence-intervals #bayesian-inference #evaluation-metrics #survival-analysis #monte-carlo-methods #revenue-impact #maximum-likelihood-estimation
**Contested on:** Every serious competitor in this niche is fighting to predict a cohort's lifetime value from a few days of behaviour when most of that value comes from players who have not spent anything yet — and whoever predicts it better takes the account.

## The Problem
Insurance and quantitative finance confronted heavy-tailed distributions and built the mathematics for them. Extreme value theory, tail index estimation, threshold exceedance models, capital allocation against tail risk and validation methods designed for rare events are all mature, published and taught, precisely because in those fields the tail is the entire business and the mean is uninformative. Games revenue has the same shape and is modelled with standard regression and tree ensembles optimised on average error.

## What Already Exists
Extreme value distributions and tail index estimation; peaks-over-threshold modelling; tail-aware validation for rare events; mixture models separating body from tail; and capital allocation under heavy-tailed loss.

## The Customization Gap
The adaptation is to a tail that is positive revenue rather than loss, predicted at the cohort level from behaviour. It requires: (1) a tail of high-value players rather than catastrophic losses, so the objective is capturing upside rather than bounding risk — this is the substantive difference and inverts much of the practical intuition; (2) prediction from a few days of behavioural covariates rather than from a long loss history; (3) a tail whose realisation depends on future content, which no financial model has to contend with; (4) decisions made per cohort per source daily rather than per portfolio per quarter; and (5) truncated observation, since cohorts are still accruing value when the decision is made.

## Target Customer
UA teams and agencies, mobile publishers, measurement vendors, and quantitative modelling consultancies.

## Impact If Solved
Insurance and finance built the tail mathematics because the tail is the business, and it is published and taught. A positive tail predicted from a few days of behaviour, whose realisation depends on future content, is what has to be rebuilt.
