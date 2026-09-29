# Buy: Observability Correlation for Forensic Sources

**Niche:** Evidence Collection & Timeline Assembly
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Distributed tracing correlates one action across many services and clocks as a matter of course, and forensic timeline assembly merges sources into a list and asks a human to spot the connections.
**Tags:** #graph-theory #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #automation #time-series-forecasting
**Contested on:** Whether a defensible sequence of events emerges from tooling, or from one examiner reconciling a dozen formats and three disagreeing clocks by hand.

## The Problem

Reconstructing what happened across many systems, from telemetry with different formats and imperfect clocks, is the central problem of observability — and it has been solved well enough to be routine.

Distributed tracing follows a single request through dozens of services, correlating spans that belong to one operation, presenting them as a tree rather than as interleaved log lines. Log correlation joins related events across sources. Clock skew is a known and handled problem. And the whole apparatus exists to let an engineer reason about a sequence of events across systems without doing the correlation by hand.

Forensic timeline assembly is the same problem without the trace identifier. There is no correlation token propagated through an attacker's activity, so the linking must be inferred — but the tooling patterns, the clock handling and the presentation all transfer.

The two disciplines sit in the same organisations, frequently in adjacent teams, and share almost nothing.

## What Already Exists

Distributed tracing: OpenTelemetry, Jaeger, Tempo and the tracing features in the observability platforms, with span correlation, causal ordering and clock skew handling.

Observability platforms: Datadog, Splunk, Elastic and Grafana, with cross-source correlation, anomaly detection and investigation workflows over very large event volumes.

Log correlation: the join and enrichment capabilities in SIEM and log platforms, used for detection rather than for reconstruction.

Forensic tooling: the forensic suites with parsers and timeline merging, and the specialised timeline tools used for supertimeline construction.

Process and entity graphs: endpoint platforms that build process trees and entity relationships, which is correlation of exactly the kind forensics needs and is scoped to the endpoint rather than across the estate.

## The Customization Gap

**No correlation identifier exists.** Tracing works because a trace identifier propagates. Attacker activity has no such token, so correlation must be inferred from timing, entity and causal plausibility — which is the hard part and the reason the transfer is not direct.

**Endpoint process trees are the right idea at the wrong scope.** Endpoint platforms already correlate process, network and file activity into a tree. Extending that correlation across hosts, identity and cloud is the missing layer and it is a smaller step than building from nothing.

**Forensic sources are heterogeneous in a way telemetry is not.** Observability data is designed to be emitted and correlated. Forensic artefacts are side effects of system operation, with inconsistent and sometimes absent timestamps.

**Clock handling needs stating, not hiding.** Observability tolerates skew because approximate ordering is adequate. Forensic conclusions may turn on whether one event preceded another, so the uncertainty must be explicit rather than smoothed.

**Presentation needs to be defensible.** A trace view is for an engineer debugging. A forensic timeline is an evidentiary artefact that must show its basis and survive challenge.

**Volume and interactivity.** Observability platforms handle enormous volumes interactively, which is exactly what timeline review needs and what forensic tooling handles worst.

## Target Customer

Observability vendors with security products — Splunk, Elastic, Datadog — for whom forensic timeline assembly is an adjacent application of correlation machinery they already own.

Endpoint platform vendors, whose process-tree correlation is the closest existing capability and whose natural extension is across the estate.

Forensics firms as buyers, and in-house response teams who frequently already have an observability platform and have never pointed it at this.

## Impact If Solved

Mature correlation machinery reaches a problem that is structurally the same and is currently solved by expert attention.

Extending endpoint process-tree correlation across hosts, identity and cloud is the specific achievable step, and it would turn four rows describing one action into one event automatically.

And interactive review over very large event volumes is something observability platforms do well and forensic tooling does badly, which is where the examiner's time actually goes.
