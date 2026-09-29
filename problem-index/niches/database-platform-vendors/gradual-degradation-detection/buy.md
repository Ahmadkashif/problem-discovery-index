# Trend Modelling Applied to Engine Internals

**Niche:** [[niches/database-platform-vendors/gradual-degradation-detection/profile|Gradual Degradation Detection]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Trend extrapolation, change-point detection and time-to-event modelling are all standard, and the database exposes the series they need in its own catalogue views.
**Tags:** #time-series-forecasting #change-point-detection #survival-analysis #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to warn a team that a database is degrading weeks before it breaks — and whoever does that takes the account, because the engines already expose everything required and interpret none of it.

## The Problem
Projecting a growing series to a threshold, detecting a discontinuity, and estimating time until an event are all elementary applied statistics with mature tooling. A database publishes exactly these series — row counts, index sizes, bloat, cache hit ratios, plan costs, lock waits — through its own interfaces, continuously and for free. The connection has not been made, so the series are collected by monitoring tools and displayed as charts for a specialist to read.

## What Already Exists
Forecasting methods with seasonality and trend; change-point detection; survival and time-to-event modelling; anomaly detection over correlated series; and the database monitoring products that already collect the underlying series. Every engine exposes detailed statistics through documented interfaces.

## The Customization Gap
The adaptation is to engine-specific semantics. It requires: (1) knowing which series matter and what a value means, which is engine-specific and is the genuine intellectual content — a cache hit ratio, a bloat percentage and a plan cost each have an interpretation that differs between engines and versions, and encoding that is the work; (2) threshold semantics rather than statistical anomaly, because the events that matter are crossings of structural boundaries — a table exceeding the size at which a plan changes, a transaction identifier approaching wraparound — which are deterministic given the trend and are not anomalies in any statistical sense; (3) workload-conditioned modelling, since the same growth is harmless on a rarely-queried table and critical on a hot path, and an unconditioned model will alert on the wrong ones; (4) version awareness, because engine behaviour changes across major versions and a model trained on one version's planner behaviour will mislead on another; and (5) validated lead time, since the value of the whole thing is how far in advance the warning arrives and that must be measured rather than claimed.

## Target Customer
Database monitoring vendors, managed database providers, and the platform teams operating databases without specialist support.

## Impact If Solved
The statistical work is elementary and the engine publishes the inputs, which makes the engine-specific interpretation the entire barrier. Threshold crossings rather than statistical anomalies is the framing that matches how these systems actually fail.
