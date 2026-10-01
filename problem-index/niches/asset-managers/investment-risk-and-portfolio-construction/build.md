# Explaining the Miss Between Forecast and Realised Risk

**Niche:** [[niches/asset-managers/investment-risk-and-portfolio-construction/profile|Investment Risk & Portfolio Construction]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The risk model forecast a 3% tracking error, the portfolio delivered 5%, and nobody can say in a sentence whether the model, the regime or the PM caused the gap.
**Tags:** #pca #matrix-decompositions #linear-regression #bayesian-inference #change-point-detection #evaluation-metrics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make the ex-ante risk forecast something a portfolio manager believes — explaining why realised tracking error and drawdowns differed from the model — and whoever does that becomes the risk system PMs actually consult before trading.

## The Problem
PMs learn to discount risk forecasts after a few quarters in which realised risk departed from forecast without explanation. Once that happens, the risk team's output becomes a compliance artefact rather than an input to portfolio construction.

## Why Nobody Has Built This
Commercial models are built for forecasting, not post-mortem. Decomposing a miss into factor-covariance error, specific-risk error, exposure drift within the period and regime change requires the daily holdings history, the model's historical forecasts and realised factor returns together — data that sits in different places and is rarely archived as it was at the time.

## What to Build
An archive of every forecast as issued, with the portfolio and model version, and a standing post-mortem that decomposes forecast error each month into its sources with confidence bands; regime-change detection that warns when realised factor correlations have broken from the model's estimation window; and a one-paragraph explanation for the PM in plain language.

## Target Customer
Heads of investment risk and CROs at active managers.

## Impact If Built
Risk forecasts regain credibility with PMs because their misses are explained rather than ignored, and portfolio construction starts using the risk budget as intended.
