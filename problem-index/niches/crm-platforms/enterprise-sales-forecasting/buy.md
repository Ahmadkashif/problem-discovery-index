# Forecast Combination Methods From Every Other Forecasting Discipline

**Niche:** [[niches/crm-platforms/enterprise-sales-forecasting/profile|Enterprise Sales Forecasting]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Combining a model's prediction with expert judgement is a solved problem with decades of literature in weather, economics and elsewhere, and sales forecasting resolves it by having a VP overwrite the model in a spreadsheet.
**Tags:** #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #descriptive-statistics #probability-distributions #revenue-impact
**Contested on:** Every serious competitor in sales forecasting is fighting to produce a number a sales leader will submit without rebuilding it in a spreadsheet — and whoever forecasts most accurately from unfalsifiable behaviour rather than from self-reported stage takes the account.

## The Problem
Three predictions exist for the same quarter: the system's, the manager's and the leader's. The organisation resolves them by taking the most senior one. Every other forecasting discipline learned long ago that the best answer is a weighted combination whose weights are set by measured historical accuracy, and that judgement adds most where the model is weakest — which is knowable and is never determined here because nobody keeps score.

## What Already Exists
Forecast combination, calibration assessment, proper scoring rules and the judgemental forecasting literature are all mature, with substantial published evidence on when expert adjustment helps and when it hurts. Weather forecasting, macroeconomic forecasting and demand planning all operate ensembles of model and expert input with tracked skill. Probabilistic forecast evaluation methods — Brier scores, calibration plots, prediction intervals — are standard and trivially implementable. Nothing needs inventing.

## The Customization Gap
The adaptation is to a forecasting process that is also a management process. It requires: (1) capturing each participant's prediction as a distinct, timestamped, scored artefact — representative, manager, leader and model — which is the foundational change and the one nobody has made; (2) proper scoring rules applied to probabilistic forecasts rather than accuracy on a point, since a forecaster who is right about the number by luck and wrong about the uncertainty is not a good forecaster; (3) combination weights learned per forecaster and per segment, because the published evidence is that expert adjustment helps in some conditions and harms in others and the pattern is discoverable; (4) recognition that the forecast influences behaviour, since a deal called at risk gets attention and may then close — which makes this a genuinely harder evaluation problem than weather and requires the effect to be acknowledged rather than assumed away; and (5) presentation that does not read as scoring individuals, because a system that publicly ranks managers on forecast accuracy will be gamed into uselessness within two quarters.

## Target Customer
Revenue operations organisations, CRM and revenue intelligence vendors, and the finance functions that consume the submitted number.

## Impact If Solved
Scoring the forecasters is the cheapest possible improvement and is absent everywhere: most organisations do not know whether their managers add or subtract accuracy. Combination with learned weights typically beats both the model and the senior override, and the methodology for doing it is decades old in disciplines that took forecasting seriously.
