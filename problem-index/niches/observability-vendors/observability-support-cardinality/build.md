# Discovered Through the Bill

**Niche:** [[niches/observability-vendors/observability-support-cardinality/profile|Observability Support & Cardinality]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A developer adds a label containing a user identifier, the metric's series count multiplies, and the customer finds out from an invoice or a slow query weeks later.
**Tags:** #change-point-detection #gradient-boosting #k-means-clustering #time-series-forecasting #confidence-intervals #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor that takes this seriously is fighting to stop cardinality explosions and instrumentation gaps before they reach a support queue — and whoever does that takes the support organisation, because those two topics are most of what its engineers do all day.

## The Problem
An engineer adds a label to a metric so they can break it down by customer. The label takes one value per customer, and there are four hundred thousand customers. The metric's series count goes from twelve to nearly five million. Nothing warns anybody. Queries on that metric become slow, then the month's bill arrives with an increase nobody can explain, then a support ticket is filed, then a support engineer explains cardinality for the fortieth time this month, then the label is removed and the data is deleted. The distribution of values in the label's first two minutes made this entirely predictable: identifiers look nothing like enumerations.

## Why Nobody Has Built This
Ingestion is revenue, and warning a customer before they ingest something expensive reduces it, which is the same commercial conflict that keeps telemetry value measurement unbuilt. The check also has to happen at ingestion time on the hot path, which is a performance constraint the pipeline was not designed around — though the check itself is cheap. And the problem is experienced as a billing surprise rather than as a product defect, which routes it to support and finance rather than to engineering.

## What to Build
Predict the explosion in the first minutes and act on it. Classify each newly observed label from the distribution of its first values — cardinality growth rate, value length and character composition, whether values repeat — which distinguishes an identifier from an enumeration with high accuracy within minutes, because the two look completely different. Warn at that moment, to the engineer who introduced it, with the projected series count and the projected cost, which is the intervention and is worth more than every downstream remedy combined. Offer a cap with an alert rather than silent ingestion, which is a product decision the category has avoided because ingestion is revenue and which customers would overwhelmingly choose if offered. Attribute cost to the specific service, metric and label rather than to a team, so the conversation is about a line of code rather than about a budget. Detect the trajectory for labels that grow slowly rather than exploding immediately, which is the harder and commoner case. And measure detection lead time — minutes from first appearance to warning — and cost avoided, both of which are directly computable from the trajectory that did not happen.

## Target Customer
Observability vendors' product and support organisations, platform teams managing telemetry cost, and the collector ecosystem where the check can be made before data leaves the customer.

## Impact If Built
Value distribution in the first few minutes is highly predictive, which makes this unusually tractable for the cost it avoids. The absence of the capability is a product choice rather than a technical limitation, and a collector-side implementation removes the conflict entirely.
