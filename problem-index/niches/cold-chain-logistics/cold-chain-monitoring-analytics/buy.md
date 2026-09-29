# Time Series Anomaly Detection Adapted to Product Stability

**Niche:** [[niches/cold-chain-logistics/cold-chain-monitoring-analytics/profile|Cold Chain Monitoring & Excursion Analytics]]
**Industry:** [[industries/cold-chain-logistics|Cold Chain Logistics]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Anomaly detection products flag deviations from normal; what matters here is whether cumulative thermal exposure has consumed the product's stability budget, which is a different question with a documented answer per product.
**Tags:** #time-series-forecasting #change-point-detection #probability-distributions #confidence-intervals #evaluation-metrics #feature-engineering #survival-analysis #automation #compliance #data-integration

## The Problem
Alerting is where the service is judged, and threshold alerting produces the wrong alerts. A shipment briefly touching the top of range during a dock transfer usually matters not at all; a shipment sitting just inside range for three days can consume more of a biologic's stability budget than a sharp brief excursion. Threshold logic fires on the first and misses the second. The result is alert volume that quality teams learn to discount, which is the worst possible failure mode for a monitoring service — the alert that mattered arrives in a stream nobody trusts. Analysts compensate by reviewing, which puts human attention on a volume problem.

## What Already Exists
Time series anomaly detection is abundant and inexpensive. The cloud anomaly services, the observability platforms, and mature open-source libraries all handle seasonality, level shifts, and multivariate anomalies with learned thresholds and good tooling. IoT platforms ship device-level alerting out of the box.

## The Customization Gap
All of them define anomalies statistically, against the signal's own history. The operative definition here is regulatory and physical: has cumulative thermal exposure exceeded what this product's stability data supports. That answer exists — it is in the product's mean kinetic temperature limits and stability study documentation — and it is per product, per formulation, sometimes per market. No general anomaly detector can incorporate it because none has a place to put it. The adaptation is a product stability model as a first-class input: each shipment carries its product's excursion tolerance and cumulative exposure budget, and alerting fires on budget consumption and on projected budget breach given remaining transit, not on threshold crossings. That converts alerting from reactive to anticipatory — the useful alert is the one that arrives while the shipment can still be intervened on. It also requires lane context, since the same remaining budget is a different risk on a route with a known customs delay than on a direct one, which is exactly what the company's own historical lane data can supply and no generic tool has.

## Target Customer
Heads of product and analytics at monitoring providers, and the quality assurance leaders at shippers who currently triage alert volume by hand and have learned to discount most of it.

## Impact If Solved
Fixes the credibility problem at the centre of the service. Alerts tied to stability budget are actionable and few, which is the opposite of the current position, and projected-breach alerting creates an intervention window that does not exist today. It also directly supports the release decision the customer is actually making, which moves the product from monitoring toward the decision itself.
