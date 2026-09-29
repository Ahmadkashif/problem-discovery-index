# Causal Structure From the Dependency Graph

**Niche:** [[niches/observability-vendors/incident-diagnosis/profile|Incident Diagnosis]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Causal discovery, change-point detection and graph learning are all developed fields, and the dependency graph that would make them applicable is produced as a by-product of tracing.
**Tags:** #causal-inference #graph-neural-networks #graph-theory #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to meet the engineer at the page with a ranked explanation rather than a dashboard — and whoever does that takes the account, because time to diagnosis is the largest component of incident duration and the moment the category's value is either delivered or not.

## The Problem
Causal inference has a substantial methodology for distinguishing cause from consequence, and its hardest requirement is usually knowing the causal structure. In a distributed system that structure is unusually available: tracing produces the service dependency graph directly, and requests flow along it in a known direction. The category has the structure that causal methods normally have to assume, and uses it to draw a map.

## What Already Exists
Causal discovery and structure learning; Granger-style temporal precedence testing; change-point detection with mature implementations; graph neural networks for propagation modelling; anomaly detection across correlated time series; and the incident diagnosis literature emerging from large-scale service operators. Tracing standards have made the dependency graph broadly available.

## The Customization Gap
The adaptation is to a production incident under time pressure. It requires: (1) treating the dependency graph as known structure rather than discovering it, which is the advantage here and changes the problem from causal discovery to causal attribution — substantially easier and rarely exploited; (2) fine temporal resolution, since propagation happens in seconds and telemetry aggregated to the minute destroys the ordering that carries the information; (3) calibration as the primary requirement, because a confidently wrong diagnosis at the most expensive moment costs more than no diagnosis and ends adoption permanently; (4) an evaluation metric of top-three accuracy rather than top-one, matched to how an engineer actually uses the output, together with a time-to-diagnosis measurement against a matched baseline of similar past incidents; and (5) a labelling strategy for confirmed root causes, which is the binding constraint — post-incident reviews are the only source, they are written inconsistently, and structuring their capture is a prerequisite rather than an afterthought.

## Target Customer
Observability and incident response vendors, and the large engineering organisations building this internally.

## Impact If Solved
The dependency structure that causal methods normally have to infer is handed over by tracing, which makes this more tractable here than in most domains. Calibration and structured root cause capture are the two requirements that determine whether the result is trusted or switched off.
