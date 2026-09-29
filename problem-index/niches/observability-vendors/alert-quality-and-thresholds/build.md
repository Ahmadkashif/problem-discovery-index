# A Number Somebody Guessed in 2021

**Niche:** [[niches/observability-vendors/alert-quality-and-thresholds/profile|Alert Quality & Thresholds]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Thresholds are numbers an engineer guessed when the monitor was created, on services whose normal behaviour nobody characterised, and the result is a stream that gets muted or a silence mistaken for health.
**Tags:** #change-point-detection #time-series-forecasting #gaussian-mixture-models #hypothesis-testing #confidence-intervals #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to replace thresholds somebody guessed with numbers backtested against the organisation's own incidents — and whoever does that takes the reliability account, because alert fatigue is the most cited operational complaint in the category.

## The Problem
A monitor alerts when latency exceeds eight hundred milliseconds. That number was chosen in 2021 by an engineer who looked at a graph for a minute. The service now serves three times the traffic, has a different caching layer, and has a legitimate daily peak that exceeds the threshold every weekday at nine. The alert fires every morning and everyone ignores it, which is rational and means that when it fires for a real reason nobody reacts. Elsewhere, a monitor set at a very high threshold has never fired, and the team believes the service is healthy. Neither number has been revisited and nothing has ever evaluated either.

## Why Nobody Has Built This
Thresholds are configuration and configuration is the customer's responsibility, which is where the category's obligation has been understood to end. Generic anomaly detection was offered as the alternative and performed badly, because real service metrics have strong daily and weekly seasonality, deploy-related step changes and genuinely multi-modal regimes, and a detector that flags every Monday morning is worse than the static threshold it replaced — which discredited the whole idea. Backtesting requires incident records linked to the metrics that moved, which exist in different systems and are inconsistently connected. And nobody has been accountable for alert quality, so nobody has asked.

## What to Build
Model the metric properly and backtest against the organisation's own incidents. Characterise each service metric's real structure: daily and weekly seasonality, deploy-related step changes, multiple operating regimes, and the difference between a slow drift and a step — because modelling the structure properly is the entire task and is what generic detectors skip. Backtest candidate thresholds against the incident record: would this number have caught the real events without firing on ordinary variation, reported as precision and recall against the organisation's own history, which is the only evidence an SRE will accept. Recommend thresholds with those numbers attached rather than asserting an anomaly score. Identify coverage gaps — incidents that occurred with no alert firing in time — which is the failure nobody looks for and is more dangerous than the noisy alerts everybody complains about. Encourage symptom-level alerting over cause-level, which is a design principle the tooling could express and does not. And re-evaluate continuously, since the service changes underneath the number and that is how every threshold became wrong in the first place.

## Target Customer
Site reliability and platform teams, observability and incident response vendors, and engineering leadership for whom the argument is on-call sustainability rather than features.

## Impact If Built
Alert fatigue is a leading contributor to on-call burnout and originates in numbers guessed once, and backtesting against incident history is entirely computable from data every platform holds. Coverage gaps are the more dangerous half and are the part nobody currently looks for at all.
