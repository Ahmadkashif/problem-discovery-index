# Schema Contract Practice

**Niche:** [[niches/customer-data-platforms/event-stream-governance/profile|Event Stream Governance]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Service interfaces are defined by contracts with compatibility checking and generated clients, and analytics events are defined by a spreadsheet.
**Tags:** #data-integration #compliance #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to make the event stream a contract product teams cannot break by accident — and whoever does that removes the failure mode that silently corrupts everything downstream.

## The Problem
Software engineering solved this for service interfaces. Schemas are defined formally, registries enforce compatibility rules, clients are generated so producers cannot emit an invalid message, breaking changes are versioned explicitly, and the build fails when a contract is violated. This is standard practice in any organisation running services at scale, and engineers would not accept an interface defined in a shared document. The same engineers emit analytics events governed by a spreadsheet maintained by another team.

## What Already Exists
Schema registries with compatibility enforcement; interface definition languages with code generation; consumer-driven contract testing; semantic versioning for interfaces; and build-time contract validation.

## The Customization Gap
The adaptation is to a consumer who is not a service and a producer with no incentive. It requires: (1) consumers that are segments, journeys and reports rather than services, so consumer-driven contract testing must express what a marketing audience depends on — translating that into a testable contract is the substantive work; (2) semantic rather than structural compatibility, since a field that keeps its type and changes its meaning passes every schema check and breaks everything downstream; (3) producers who gain nothing from compliance, unlike service contracts where both sides are engineering teams with shared incentives — this incentive asymmetry is why technical enforcement rather than process is required; (4) events emitted from clients the organisation does not fully control, including mobile applications with long update tails; and (5) a plan that non-engineers need to read, since marketing and analytics depend on it and cannot read a schema definition file.

## Target Customer
Data engineering and product teams, customer data platform vendors, and schema registry vendors for whom analytics event governance is an adjacent market.

## Impact If Solved
Engineers would not accept a service interface defined in a shared document and accept exactly that for analytics events. The incentive asymmetry between producer and consumer is why technical enforcement is required where service contracts get by on shared interest.
