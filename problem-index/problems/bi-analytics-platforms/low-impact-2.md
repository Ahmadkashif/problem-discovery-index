# Data Quality Alerting

**Industry:** [[bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Data observability is now a well-funded product category with good tooling, and most teams still discover a broken pipeline when an executive asks why the number looks wrong.
**Tags:** #change-point-detection #time-series-forecasting #hypothesis-testing #confidence-intervals #gaussian-mixture-models #evaluation-metrics #automation

## The Problem
Data pipelines fail in two ways. They fail loudly — a job errors, someone is paged, it is fixed. And they fail quietly: a source system changes a field, a join starts dropping rows, an upstream API returns partial data, a currency code changes, a timezone shifts. The pipeline succeeds, the dashboard renders, and the number is wrong.

Quiet failures are the expensive ones because decisions are made on them. They are discovered when someone who knows the business notices the number looks implausible, which may be weeks later and may be never.

Data quality tests exist and are the standard remedy — assert row counts, null rates, uniqueness, freshness. They are written by hand, per table, by engineers who must guess the thresholds. A threshold set too tight fires constantly and is muted; set too loose it never fires. Both outcomes converge on the same place, which is nobody looking at the alerts.

The observability vendors emerged to automate this and have made real progress, and adoption remains partial and the alert fatigue problem persists in a different form.

## What Already Exists
dbt tests and Great Expectations provide declarative data testing widely used in modern stacks. Data observability platforms (Monte Carlo, Bigeye, Metaplane, Soda) offer automated anomaly detection on freshness, volume and distribution. Warehouse-native monitoring exists. Lineage tools identify downstream impact. Alerting integrates with the usual incident channels.

## The Customisation Gap
Thresholds are the whole problem and they are set either by hand or by generic anomaly detection that does not know the data's actual shape. Real business data has structure — weekly seasonality, month-end spikes, holiday troughs, a step change when a large customer onboarded — and a detector that treats those as anomalies produces the noise that causes muting.

Characterising each series properly, with seasonality and regime changes modelled, is what would make the alerts trustworthy, and it is a modest time-series problem that the tooling generally approximates rather than solves.

Consequence routing is the second gap. An anomaly in a table nothing reads is not an incident; the same anomaly in a table feeding the board deck is. The platforms hold the lineage and the usage data required to make that distinction and generally alert uniformly.

Silent-failure detection is the third and hardest. A pipeline that succeeds while producing subtly wrong output shows up as a distributional shift rather than a threshold breach, and detecting it requires modelling the distribution rather than the count — which is where the category's remaining gap actually lies.

## Impact If Solved
Every analytical output rests on pipelines that fail silently, and the alerting built to catch that is muted because it cries wolf. Modelling series structure properly and routing by downstream consequence is what converts data quality monitoring from a noise generator into something people read.
