# Root Cause Analysis From Observability

**Niche:** [[niches/game-analytics-vendors/metric-movement-explanation/profile|Metric Movement Explanation]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Observability platforms correlate metric movements with deployments and changes as standard, and game analytics shows the metric alone.
**Tags:** #causal-inference #change-point-detection #confidence-intervals #evaluation-metrics #time-series-forecasting #data-integration #hypothesis-testing #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to say why a metric moved, when the dashboard can only say that it did — and whoever answers it takes the account.

## The Problem
Software observability made a version of this standard. When a metric moves, the platform overlays deployments, configuration changes and feature flag flips on the same timeline, correlates the movement with recent changes, and surfaces the most likely candidates. Engineers expect it. Game analytics platforms, whose customers ask an identical question about an identical kind of change event, show the metric with nothing alongside it.

## What Already Exists
Change and deployment event overlays on metric timelines; automatic correlation of movements with recent changes; anomaly detection with change attribution; segmented decomposition of a movement; and incident timelines assembled automatically.

## The Customization Gap
The adaptation is to a behavioural metric measured in days rather than a system metric measured in seconds. It requires: (1) effects that appear over days and weeks, so the correlation window is far wider and far noisier than a deployment correlation — this is the substantive difference and makes naive correlation useless; (2) causes that are external as well as internal, including seasonality, competitor launches and genre shifts, with no observability analogue; (3) acquisition mix as a composition effect that mimics a behavioural change; (4) change history that lives in the studio's systems rather than the analytics platform's; and (5) an audience of product managers rather than engineers, requiring a different explanation format.

## Target Customer
Game analytics vendors, studio data and product teams, publishers, and observability vendors entering the vertical.

## Impact If Solved
Observability made change correlation standard and engineers now expect it. Effects that appear over weeks, with external causes and composition shifts in the mix, is what makes the game version a harder correlation.
