# Build: The Alert That Arrives Resolved

**Niche:** The SOC Analyst Receiving the Alerts
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Alerts that arrive with the age, infrastructure type, prior dispositions and environmental context already attached, so the analyst starts from an assessment rather than from a lookup.
**Tags:** #gradient-boosting #graph-theory #evaluation-metrics #confidence-intervals #bert #automation #worker-facing #workflow-orchestration
**Contested on:** Whether the alerts an intelligence subscription generates are worth the analyst's attention.

## The Problem

An alert says a host connected to a flagged address. That is all it says.

The analyst then spends several minutes assembling the context that determines the answer. What is this address — a cloud provider, a shared host, a residential range? When was the indicator first seen, and is that recent enough to mean anything? Which feed supplied it and what is that feed's track record here? Has this same alert fired before, and what was concluded? Is the internal host significant? Was there any other suspicious activity around it?

Every one of those is available. Infrastructure type is determinable from public data. Indicator age is in the feed metadata. Prior dispositions are in the case management system. Surrounding activity is in the telemetry. Feed history is in the alert record.

None of it is on the alert. So the analyst performs the same assembly, several minutes at a time, dozens of times a shift, for alerts that are mostly going to be dismissed.

The two facts that resolve the majority of these — the indicator is eight months old, and the address belongs to a shared hosting provider — are the cheapest to supply and the least frequently present.

## Why Nobody Has Built This

**Enrichment is configured per deployment.** Every organisation wires up its own enrichment, badly and partially, because it ships as a capability rather than as a configuration.

**The vendor's responsibility ends at the indicator.** Intelligence vendors deliver content. What the alert looks like is the platform's concern, and the platform treats all matches generically.

**Prior disposition requires the join.** Showing that this alert was dismissed three times before requires attributing alerts to indicators consistently, which is the provenance problem that also blocks feed measurement.

**Nobody owns the analyst's experience.** Security operations leadership owns throughput and coverage. Alert quality is diffused across the vendor, the platform and the tuning nobody has time for.

**Automated resolution is feared.** A system that pre-dismisses alerts might dismiss a real one, so the safe design shows everything with no assessment attached — which pushes the entire burden onto the analyst.

**The arithmetic is not explained.** Because nobody explains the base rate problem, alert fatigue is attributed to tooling rather than understood as a predictable consequence, which directs effort at the wrong remedies.

## What to Build

**Attach age and infrastructure type to every alert.** First seen, last seen, and whether the address or domain is shared hosting, a cloud range, a content delivery network, a dynamic residential address or a sinkhole. These two facts resolve a large share of alerts immediately and are both derivable from public data.

**Show prior dispositions for the same indicator.** Investigated three times in the last month, dismissed as benign each time, by these analysts. This prevents the most demoralising repetition in the job and requires only the alert-to-indicator join.

**Bring the surrounding telemetry.** What else that host did around the same time, whether the connection succeeded, how much data moved, whether the process is known. The analyst gathers this anyway and it should arrive with the alert.

**Score the alert and explain the score.** A prioritisation combining indicator age, infrastructure type, feed history, environmental significance and surrounding activity — presented with its reasoning so the analyst can disagree. Not automated dismissal; a starting assessment.

**Suppress automatically where the pattern is established.** An indicator dismissed as benign repeatedly, on the same infrastructure, should stop generating alerts until something changes — with the suppression visible and reversible.

**Explain the base rate, once, to the team.** A short explanation of why even good indicators produce mostly false positives at enterprise traffic volumes changes how the team understands its own queue and directs tuning effort at the right things.

**Feed dismissals upward.** Aggregate what is being dismissed and why, and send it to whoever manages feeds. The analyst's dispositions are the best available evidence about feed quality and currently reach nobody.

## Target Customer

Security operations leadership, where analyst capacity is the binding constraint and alert handling time is directly measurable.

The threat intelligence and SIEM platforms, for whom alert-time enrichment is a natural feature and is currently left to per-deployment configuration.

Managed detection providers, who feel this most acutely because they run the queue at scale across many customers.

## Impact If Built

Attaching indicator age and infrastructure type to every alert is cheap, uses public data, and would resolve a large share of alerts before the analyst opens them.

Showing prior dispositions ends the most demoralising pattern in the job — investigating the same benign match repeatedly with no memory that it has been done before.

And feeding dismissals back to feed management would close the loop that currently discards the best evidence anyone has about whether a subscription is worth its cost.
