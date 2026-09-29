# Seasonality and Regime Modelling, Properly Applied

**Niche:** [[niches/observability-vendors/alert-quality-and-thresholds/profile|Alert Quality & Thresholds]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Time series modelling with multiple seasonalities, level shifts and regime changes is a mature statistical discipline, and the category's anomaly detection flags every Monday morning.
**Tags:** #time-series-forecasting #exponential-smoothing #gaussian-mixture-models #hidden-markov-models #change-point-detection #confidence-intervals #hypothesis-testing #evaluation-metrics
**Contested on:** Every serious competitor here is fighting to replace thresholds somebody guessed with numbers backtested against the organisation's own incidents — and whoever does that takes the reliability account, because alert fatigue is the most cited operational complaint in the category.

## The Problem
Decomposing a series into trend, multiple seasonal components and residual is standard. Detecting a level shift distinct from a gradual trend is standard. Modelling a process that switches between operating regimes is standard. Service metrics exhibit all three — daily and weekly seasonality, step changes at deployments, and distinct regimes under different traffic mixes — and the anomaly detection shipped in this category routinely models none of them, which is why practitioners distrust it.

## What Already Exists
Seasonal decomposition and forecasting methods with multiple seasonalities; exponential smoothing variants; change-point detection for level shifts; mixture models and hidden Markov models for regime identification; and conformal and quantile approaches for prediction intervals. All with mature open implementations and a long applied record in other domains.

## The Customization Gap
The adaptation is to service metrics with deployment-driven discontinuities. It requires: (1) deployment events as known exogenous inputs, since a step change at a deployment is expected behaviour rather than an anomaly, and a model without that input will alert on every release — this is the single most important adaptation and is what most implementations lack; (2) multiple seasonalities including holiday and business-calendar effects, because a retailer's traffic on a promotion day is not an anomaly and a model with one daily cycle will say it is; (3) regime awareness, since services genuinely operate in distinct modes and a unimodal model will find one of them anomalous permanently; (4) evaluation against the incident record rather than against reconstruction error, because the question is whether the detector would have caught the real events and reconstruction error answers something else entirely; and (5) an explanation with every alert, since an anomaly score with no account of what is unusual will be ignored by an engineer at three in the morning and rightly so.

## Target Customer
Observability vendors, incident response platforms, and site reliability teams building their own detection.

## Impact If Solved
The statistical machinery is mature and the category's implementations skip the structure that makes service metrics distinctive, which is why the feature is distrusted. Deployment events as exogenous input and evaluation against the incident record are the two changes that would make the output credible.
