# Coverage Reconciliation From Asset Management

**Niche:** [[niches/observability-vendors/instrumentation-coverage/profile|Instrumentation Coverage]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reconciling an expected inventory against an observed one is the foundation of asset management, patch compliance and endpoint security, and observability coverage has no equivalent.
**Tags:** #graph-theory #descriptive-statistics #change-point-detection #evaluation-metrics #confidence-intervals #compliance #data-integration #automation
**Contested on:** Every serious competitor here is fighting to tell an organisation what it cannot see before an incident rather than during one — and whoever does that takes the platform account, because every capability in the category is worthless on a service that emits nothing.

## The Problem
Endpoint security reconciles managed devices against the corporate directory and reports which machines have no agent. Patch management reports which hosts are unaccounted for. Configuration management reports drift. All three are built on the same idea: an authoritative expected inventory, an observed inventory, and a difference. Observability has both inventories available and does not compute the difference.

## What Already Exists
Asset and configuration management databases with reconciliation; endpoint agent coverage reporting; cloud resource inventory APIs; deployment system records; service catalogue tooling; and the reconciliation pattern itself, which is well understood. Agent health reporting exists in every endpoint security product and in almost no observability product.

## The Customization Gap
The adaptation is to ephemeral services with several signal types. It requires: (1) an expected inventory that handles ephemerality, since containers and functions appear and disappear constantly and a naive reconciliation produces thousands of false gaps — the unit must be the service rather than the instance; (2) coverage expressed per signal type and per capability rather than as a binary, because a service with metrics and no traces is instrumented for alerting and blind for diagnosis, and a single coverage number hides that; (3) health as distinct from presence, since a detached auto-instrumentation library and an idle service are indistinguishable by volume and must be separated by version and configuration inspection; (4) propagation verification as a graph property rather than a per-service one, because context is dropped at boundaries and the affected traces belong to services that are themselves correctly instrumented; and (5) consequence-weighted prioritisation from the dependency graph, since a complete gap list in a large estate is unusable without ordering.

## Target Customer
Observability vendors, platform engineering teams, and the asset and configuration management vendors for whom this is an adjacent reconciliation.

## Impact If Solved
The reconciliation pattern is standard in three adjacent disciplines and absent here, despite both inventories being available. Per-signal coverage and health-versus-presence are the two adaptations that make the report actionable rather than merely alarming.
