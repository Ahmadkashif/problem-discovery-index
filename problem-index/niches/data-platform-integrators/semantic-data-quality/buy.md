# Drift Detection From Machine Learning Operations

**Niche:** [[niches/data-platform-integrators/semantic-data-quality/profile|Semantic Data Quality]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine learning operations monitors input distributions because a model degrades silently, and data pipelines monitor row counts.
**Tags:** #change-point-detection #probability-distributions #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #automation #entropy-cross-entropy-kl-divergence
**Contested on:** Every serious competitor in this niche is fighting to catch the data failures that matter — a field whose meaning changed — when the monitoring watches freshness and volume against thresholds somebody set at deployment.

## The Problem
Machine learning operations learned that a model fails silently when its inputs change, and built the response: monitor the distribution of every input feature, detect drift against a training baseline, alert on distributional distance, and tie it to downstream model performance. The methods are standard and the tooling is commodity. Data pipelines feeding reports have the same silent failure mode and monitor whether the rows arrived.

## What Already Exists
Feature distribution monitoring against a baseline; distributional distance measures with alerting; categorical drift detection; downstream performance linkage; and automatic baseline maintenance.

## The Customization Gap
The adaptation is to a reporting layer with no model performance signal to tie to. It requires: (1) no downstream accuracy metric to confirm that drift mattered, so the alert must stand on the distribution change alone and must therefore be far more precise about what changed — this is the substantive difference; (2) business semantics where a legitimate change and a break look identical distributionally, needing human context; (3) thousands of fields rather than a model's feature set, so the monitoring must be cheap and selective; (4) strong seasonality in business data that naive drift detection flags constantly; and (5) an alert whose recipient is a data engineer rather than a model owner.

## Target Customer
Data platform teams and integrators, observability and quality vendors, machine learning platform vendors, and data engineering leadership.

## Impact If Solved
Machine learning operations built distribution monitoring because models fail silently when inputs change, and the tooling is commodity. No downstream accuracy signal to confirm the drift mattered is what makes the reporting version harder.
