# The Change Stream Nobody Joins to the Incident

**Niche:** [[niches/observability-vendors/incident-diagnosis/profile|Incident Diagnosis]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Most incidents follow a change, every change is recorded somewhere, and the on-call engineer finds out what changed by asking in a chat channel.
**Tags:** #descriptive-statistics #change-point-detection #graph-theory #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to meet the engineer at the page with a ranked explanation rather than a dashboard — and whoever does that takes the account, because time to diagnosis is the largest component of incident duration and the moment the category's value is either delivered or not.

## The Problem
An engineer is paged. Their first question, correctly, is what changed. The answer is spread across a deployment system, a configuration repository, a feature flag service, an infrastructure provisioning tool, a database migration log and a cloud provider's status feed, each with its own interface and none joined to the telemetry. So they ask in the incident channel, and someone eventually remembers a deployment. Fifteen minutes have gone, and the deployment was recorded with a timestamp in a system the observability platform could have queried in the first second.

## Why It's Still Broken
Change data lives in delivery tooling and telemetry lives in observability tooling, and the two are separate purchases with separate owners. Integrations exist as deployment markers on a graph, which is a visual annotation rather than a queryable join, and they usually cover only the primary deployment system. Feature flags in particular are a major cause of incidents and are almost never in the change feed, because the flag system is owned elsewhere and flags change without a release. And nobody has asked for it as a capability because the chat-channel workaround functions, slowly.

## What a Fix Looks Like
Join the change stream to the telemetry properly. Ingest every change source — deployments, configuration, feature flags, infrastructure provisioning, schema migrations, dependency updates, provider status — into one timeline with a consistent schema, which is integration work rather than invention and is the whole fix. Attach changes to the services they affect, so the on-call engineer sees changes to the failing service and to everything upstream of it rather than to the whole estate. Rank by proximity and plausibility: a deployment to an upstream service eight minutes before the anomaly outranks an unrelated configuration change from that morning. Include the change's author and its link, since the fastest resolution is often asking the person who made it. Surface it automatically at page time rather than requiring a search, since the engineer's attention is the scarce resource. And report the base rate afterwards — what proportion of incidents followed a change of each type — which is a straightforward analysis that tells the organisation where its risk actually is and which nobody produces.

## Who Feels the Pain
On-call engineers spending their first fifteen minutes asking what changed; incident commanders assembling a timeline by hand; and organisations whose most common incident cause is recorded in a system nobody consults under pressure.

## Impact If Fixed
The change data exists and is unjoined, which makes this integration work with an outsized return at the single most time-critical moment in the category. Feature flags in particular are a major and almost entirely unrepresented source, and adding them alone changes many diagnoses.
