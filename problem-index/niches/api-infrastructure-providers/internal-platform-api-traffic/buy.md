# Dependency Graphs the Mesh Already Computes

**Niche:** [[niches/api-infrastructure-providers/internal-platform-api-traffic/profile|Internal Platform API Traffic]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The service layer observes every call between every service and therefore holds an exact dependency graph, which organisations maintain instead as a diagram in a wiki.
**Tags:** #graph-theory #spectral-graph-theory #graph-neural-networks #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor here is fighting to carry service-to-service traffic with negligible latency cost and negligible friction for the teams deploying behind it — and whoever does that takes the platform account, because the alternative is that teams route around the layer entirely.

## The Problem
Graph analysis is mature: reachability, centrality, cycle detection, community detection, blast radius. The service layer produces the graph these techniques need as a by-product of routing every call. Organisations answer "what depends on this service" from an architecture diagram that was accurate eighteen months ago, and discover the real answer during an incident.

## What Already Exists
Graph libraries with every relevant algorithm; service dependency extraction in mesh and tracing products, usually rendered as a visualisation rather than exposed as a model; community detection for identifying implicit subsystems; and the observability category's work on dependency-based incident diagnosis, which is documented separately in this vault.

## The Customization Gap
The adaptation is from a picture to an operational model. It requires: (1) edges weighted by criticality rather than by volume, since a low-volume call on a payment path matters more than a high-volume health check, and volume-weighted graphs mislead consistently; (2) temporal treatment, because dependencies appear and disappear and a graph aggregated over a month conceals both the new coupling introduced last week and the one that only manifests at month end; (3) ownership resolution onto the graph, since the operational questions all end in which team, and mapping services to owners is data the platform must integrate; (4) queryability rather than visualisation, because a diagram of four hundred services is unreadable and the value is in answering specific questions such as what breaks if this is unavailable; and (5) the distinction between calls that are hard dependencies and those with a fallback, which is observable from behaviour during past failures and changes the blast radius completely.

## Target Customer
Platform engineering teams, mesh and gateway vendors, observability vendors, and the incident management products that need this graph at page time.

## Impact If Solved
The graph is produced as a by-product and is rendered as a picture, which wastes the most operationally useful artefact the platform layer creates. Criticality weighting and hard-versus-soft dependency classification are what make it answer real questions.
