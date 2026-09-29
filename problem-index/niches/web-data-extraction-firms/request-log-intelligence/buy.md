# Telemetry Analytics and Survival Modelling

**Niche:** [[niches/web-data-extraction-firms/request-log-intelligence/profile|Request Log Intelligence]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reliability analytics and survival modelling exist precisely to predict when a thing will fail from its history, and extraction fleets treat every breakage as a surprise.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #change-point-detection #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn a complete record of every request the firm makes into knowledge about targets, cost and risk — and whoever does that operates on evidence while everyone else operates on the last incident.

## The Problem
Predicting time to failure from historical patterns is what survival and reliability analysis do, with mature methods, good implementations and decades of industrial practice. Detecting that a monitored process has shifted is change-point detection. Both apply directly to extractions that break and to targets whose defences tighten, and both operate on data these firms already collect continuously. Neither is used.

## What Already Exists
Survival analysis with censoring and time-varying covariates; reliability engineering with failure prediction and maintenance scheduling; change-point detection on streaming signals; anomaly detection on operational telemetry; and cohort analysis for comparing populations over time.

## The Customization Gap
The adaptation is to failures caused by an adversary's deliberate choices. It requires: (1) survival modelling with an extraction as the subject and a site redesign as the hazard, where the covariates are structural volatility and observable site characteristics — a natural fit that nobody has set up; (2) change-point detection on block rates rather than on system metrics, since a target tightening its defences is a change point in an outcome the firm observes thousands of times an hour; (3) adversarial rather than random failure, because a target that has noticed you behaves differently from one that changed for its own reasons, and distinguishing the two matters for the response; (4) competing risks, since an extraction can fail through blocking, redesign or the page disappearing entirely and these have unrelated remedies; and (5) cross-target learning, where sites built on common platforms share hazard characteristics and a new target can inherit a prior from its platform.

## Target Customer
Extraction firms, their operations and finance functions, and the reliability analytics community for whom this is an unusually data-rich unclaimed application.

## Impact If Solved
Failure prediction is a mature discipline operating on exactly the data these firms already stream. Change-point detection on block rates gives early warning of a target tightening its defences, and cross-target priors let a new site inherit a hazard profile from its platform.
