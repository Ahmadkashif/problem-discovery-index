# Telemetry Cost Attribution and Retention

**Industry:** [[observability-vendors|Observability Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every vendor offers sampling, tiered retention and usage dashboards, and customers still cannot tell which telemetry is worth its cost — so they cut by volume and lose the signal they needed.
**Tags:** #gradient-boosting #k-means-clustering #time-series-forecasting #logistic-regression #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
Observability spend has grown into a major line item, in many engineering organisations rivalling or exceeding the cost of the infrastructure being observed. It is a standing complaint, a recurring board question, and a periodic emergency when the bill jumps.

The response is a cost reduction exercise conducted almost blind. Which logs can we stop sending? Which metrics have too many dimensions? Which traces can we sample harder? The team decides by volume — cut what is biggest — because volume is the only attribute they can see.

Value is invisible. Nobody knows which telemetry has ever been queried, which appeared in an incident investigation, which underpins an alert that has actually fired usefully, or which would be missed if it disappeared. So the cuts are arbitrary, and the failure mode is discovering during the next incident that the signal you needed was the one you turned off six weeks ago.

The vendor knows exactly which data is queried, by whom, how often, and in what context. That information is not surfaced as a value signal, because surfacing it would tell customers what to stop paying for.

## What Already Exists
Usage and cost dashboards are standard, broken down by product line and often by team. Sampling — head-based and increasingly tail-based — is supported. Tiered storage with cheaper cold retention is widely available. Cardinality analysis tools identify expensive dimensions. OpenTelemetry collectors allow filtering and transformation before data ever reaches the vendor.

## The Customisation Gap
Value attribution per telemetry stream is the missing measurement. Every signal could carry a record of how often it has been queried, whether it participated in an incident investigation, whether an alert built on it has fired truly, and how recently any of that happened. Joining that to cost produces a value-per-dollar ranking, which is the artefact every customer wants and no vendor offers.

Value-based retention follows: keep queried signals hot, tier the rest, and delete what has never been read in a year — decided per stream rather than by a global policy.

Intelligent sampling should preserve the unusual. Uniform sampling keeps the ordinary and discards the rare, and the rare requests are the ones investigated during incidents. Tail-based sampling improves on this and is still configured by rule rather than by learned interest.

Cardinality prediction is the fourth gap: a new label about to explode a metric's cardinality is detectable before it lands, and customers currently discover it from a bill.

## Impact If Solved
Observability cost is a chronic and rising complaint that customers manage by cutting the biggest streams rather than the least useful, which periodically costs them the signal they needed. Value attribution is a straightforward join the vendors have declined to make, and it would move the category's conversation from volume to worth.
