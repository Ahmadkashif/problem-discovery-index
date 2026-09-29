# Reuse Discipline From Software Engineering

**Niche:** [[niches/saas-implementation-partners/configuration-reuse/profile|Configuration Reuse]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering built libraries, versioning and dependency management so nothing is written twice, and implementation partners rebuild configurations.
**Tags:** #workflow-orchestration #data-integration #automation #compliance #evaluation-metrics #sets-and-logic #graph-theory #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to stop rebuilding what the firm has already built hundreds of times, and whoever industrialises that reuse takes the account.

## The Problem
Software engineering solved reuse thoroughly: shared libraries with owners, semantic versioning, dependency management, deprecation policy, and a culture in which writing something that already exists is a mistake rather than a necessity. The tooling is commodity and the practice is universal. Implementation partners produce configuration rather than code, face the same repetition at greater scale, and have almost none of it.

## What Already Exists
Shared component libraries with maintainers; semantic versioning and dependency resolution; deprecation and migration policy; package registries and discovery; and reuse measured as a practice metric.

## The Customization Gap
The adaptation is to configuration deployed into client-owned tenants rather than code compiled into a product. It requires: (1) artefacts that live in hundreds of separate client tenants under separate contracts, so a shared library cannot simply be depended on and must be deployed and diverge — this is the substantive difference; (2) configuration expressed in platform metadata with no dependency model; (3) client-specific variation as the norm rather than the exception, so patterns must be parameterised heavily; (4) platform releases three times a year changing the substrate underneath every asset; and (5) a billable model that pays for rebuilding, which is the commercial obstacle rather than the technical one.

## Target Customer
Implementation partners and systems integrators, delivery leadership, platform vendors, and developer tooling vendors.

## Impact If Solved
Software made reuse universal with libraries, versioning and deprecation policy, and the tooling is commodity. Configuration deployed into hundreds of separate client tenants that then diverge is what makes the dependency model different.
