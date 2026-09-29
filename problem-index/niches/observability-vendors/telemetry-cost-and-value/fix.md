# The Cost Anomaly Attributed to a Team

**Niche:** [[niches/observability-vendors/telemetry-cost-and-value/profile|Telemetry Cost & Value]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The bill went up forty percent and the platform reports which team is responsible, which starts an argument, when it could report which metric, which label and which commit.
**Tags:** #change-point-detection #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to tell an engineering organisation which telemetry is worth its cost — and whoever does that takes the budget conversation, because customers are currently cutting by volume, which is the only attribute they can see.

## The Problem
Ingestion rises sharply over a fortnight. The cost dashboard shows the increase by team, and the platform team takes the number to the owning team, who say they have not changed anything. Both are right: a library upgrade in a shared dependency began emitting a new metric with a label that varies per request. Establishing that takes two days of investigation across three teams. The increase started on a specific day, from a specific service, on a specific metric, attributable to a specific deployment, and every one of those facts is in the platform's own ingestion records.

## Why It's Still Broken
Cost reporting was built for chargeback, which needs team-level attribution and nothing finer, so the dimensions stop there. Attribution to a metric, a label and a deployment requires joining ingestion records to the change stream, which is the same unmade join the incident diagnosis niche describes. And the conversation has become adversarial in most organisations — cost reporting is used to allocate blame rather than to diagnose — which discourages the granularity that would make it diagnostic instead.

## What a Fix Looks Like
Attribute to the cause, not the cost centre. Detect ingestion change points per service, per metric and per label rather than in the aggregate, which localises the increase to the day and the object and is elementary time series analysis over records the platform already keeps. Join to the change stream so the deployment or configuration change that coincides is named in the report, which usually ends the investigation immediately. Report the marginal cost of each object rather than only totals, so the conversation is about one label rather than about a team's whole budget. Alert on the change when it happens rather than when the invoice arrives, since a fortnight of unnecessary ingestion is money already spent. Distinguish growth from an increase — traffic doubling and a new label being added look identical in a total and are entirely different problems. And present it to the engineer who made the change rather than to the platform team, since they are the one who can reverse it and they currently never hear about it.

## Who Feels the Pain
Platform teams conducting cost investigations across several teams; engineers blamed for increases they did not cause; and organisations spending weeks of unnecessary ingestion before anyone notices.

## Impact If Fixed
Per-object change point detection and a join to the change stream turn a two-day investigation into a line in a report. Alerting at the change rather than at the invoice removes the weeks of spend that accumulate before anybody looks.
