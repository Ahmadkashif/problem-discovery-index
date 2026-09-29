# Buy: Telemetry Platforms That Already Hold the Answer

**Niche:** Match Rate Measurement
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SIEM and endpoint platforms match indicators against telemetry continuously as their core function, and none of them reports back on how each feed performed.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #data-integration #automation #workflow-orchestration
**Contested on:** Whether anyone will publish how often a feed's indicators actually fire against real telemetry.

## The Problem

Every organisation running threat intelligence already performs the computation. The SIEM or endpoint platform ingests feeds, matches indicators against telemetry continuously, and generates alerts when something hits. That matching is the entire mechanism by which threat intelligence produces value.

The result is not retained as an analytic. The platform reports alerts, which are the matches. It does not report which feed produced how many, what proportion of each feed's indicators ever fired, which feeds produce alerts that get closed as false positives, or which feeds contribute alerts nothing else would have caught.

So the organisation has performed the measurement millions of times and kept none of it. At renewal, with four subscriptions and a budget question, nobody can say which feed earned its cost.

The data is sitting in the alert history and the matching logs. The analysis is a handful of queries. Nobody has built the report because feed evaluation is nobody's job.

## What Already Exists

SIEM platforms: Splunk, Sentinel, Chronicle, Elastic and the rest, ingesting threat intelligence, matching against telemetry and recording every alert with its source.

Endpoint platforms: CrowdStrike, SentinelOne, Defender and peers, matching indicators at scale with their own intelligence and third-party feeds.

Threat intelligence platforms: Anomali, ThreatConnect, OpenCTI and MISP, aggregating feeds with deduplication, scoring and routing — the natural place for a feed performance view and the place it is least developed.

Detection engineering practice: an emerging discipline that measures detection rule performance with precision and recall, and applies the same thinking to rules and almost never to feeds.

Alert triage data: the outcome of every alert, recorded in the case management system, which is the ground truth for the precision half.

## The Customization Gap

**Feed attribution is lost at the alert.** Most platforms record that an alert fired without cleanly attributing which feed supplied the matching indicator, particularly after deduplication across feeds. Retaining source attribution through the matching pipeline is the enabling change.

**No coverage denominator.** Platforms report matches. Match rate requires knowing how many indicators were loaded and never matched, which means retaining the full feed inventory alongside the match log — a small storage cost nobody incurs.

**Deduplication destroys the comparison.** Threat intelligence platforms deduplicate indicators across feeds, which is operationally correct and makes per-feed attribution impossible unless provenance is retained for every source that supplied an indicator.

**No feed-level reporting exists.** The threat intelligence platforms are the obvious home for a feed scorecard — they already hold every feed and every match — and none of them ships one.

**Alert outcomes are not joined back.** The case management system records whether an alert was a true or false positive. Joining that to the feed that produced it is the precision measurement, and the two systems are rarely connected.

**Detection engineering has the right habits and the wrong scope.** Teams that measure detection rule precision and recall would apply the same rigour to feeds immediately if the tooling reported it.

## Target Customer

Threat intelligence platform vendors — Anomali, ThreatConnect, OpenCTI, MISP — for whom feed performance reporting is the obvious missing feature of a product whose whole purpose is managing multiple feeds.

SIEM and endpoint vendors, who hold the matching and could report feed attribution with a provenance change.

Security operations leadership as the buyer, since the output directly informs subscription decisions worth substantial money.

## Impact If Solved

An organisation could answer which of its subscriptions earns its cost, from data it already generates, which is currently answered by impression.

Retaining feed provenance through deduplication is a small engineering change that unlocks every per-feed comparison, and its absence is the specific reason the analysis is not done.

And joining alert outcomes back to the feed that produced them would give customers their own precision measurement without waiting for any vendor to publish one — which is the practical path to the harder half of feed quality.
