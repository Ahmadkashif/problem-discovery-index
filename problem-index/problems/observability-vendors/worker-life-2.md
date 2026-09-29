# Support Engineer on Cardinality and Instrumentation

**Industry:** [[observability-vendors|Observability Vendors]]
**Type:** Worker Life Changing
**One-liner:** Observability support engineers stop explaining cardinality explosions after the bill and start preventing them, because a label about to multiply a metric by ten thousand is detectable before it lands.
**Tags:** #gradient-boosting #change-point-detection #k-means-clustering #bert #time-series-forecasting #evaluation-metrics #automation #worker-facing

## The Problem
Support at an observability vendor handles a distinctive queue. A customer's bill jumped and they want to know why. A metric is not appearing and the instrumentation is misconfigured. Traces are incomplete because context propagation breaks across a boundary. A query is timing out. Cardinality has exploded because somebody added a user identifier as a label.

Cardinality is the recurring one and the most frustrating, because it is always the same conversation. A label with unbounded values — a request identifier, a user identifier, a full URL path — was added to a metric, the time series count multiplied, and the customer discovers it through cost or through query slowness. The engineer explains the concept, identifies the offending label, and advises removing it. Then does it again next week for a different customer.

Instrumentation gaps are the second recurring class. A service is not reporting, or is reporting partially, and diagnosing why means reasoning about the customer's deployment, agent version, configuration and network from a description.

## Why It Matters to the Worker
Observability support engineers are strong systems engineers — they have to reason about distributed systems they cannot see, on behalf of customers who are themselves skilled. Spending that capability on the same cardinality explanation is a poor use of it.

The bill conversation is the worst part. An engineer explaining a cost overrun is defending the vendor's pricing model to an unhappy customer while privately agreeing that the model punished a reasonable mistake. That position is uncomfortable and recurs constantly.

There is also a structural frustration: the explosion was detectable at the moment the label was introduced, and the product let it through and billed for it. Support absorbs the consequence of a guardrail nobody built.

And the queue is heavily concentrated in a small number of causes, which everyone in the function can list, and which persist release after release.

## What a Solution Looks Like
Cardinality prediction before ingestion. A new label's value distribution is observable within minutes of it appearing, and a label heading toward unbounded cardinality is identifiable long before it reaches the bill. Warning at that point — or capping with an alert rather than silently accepting — is a guardrail the category should have had a decade ago.

Instrumentation validation as a health check. Whether a service is reporting the expected signals, whether trace context propagates across each boundary, and whether the agent is current are all checkable, and a customer-facing instrumentation health report would eliminate a large share of the queue.

Cost anomaly detection with attribution: which service, which metric, which label caused this week's increase, delivered as it happens rather than at the invoice.

Query performance guidance, since slow queries are usually a small set of recognisable anti-patterns that could be flagged in the editor rather than explained afterwards.

## Impact If Solved
The observability support queue is dominated by a handful of preventable causes that the platform can detect at the moment they occur rather than at the moment they are billed. Building the guardrails removes the volume and, more importantly, removes the conversation in which an engineer defends a bill for a mistake the product could have prevented.
