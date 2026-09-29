# Feature Usage Analytics From Product Teams

**Niche:** [[niches/data-platform-integrators/usage-instrumentation/profile|Usage Instrumentation]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product teams instrument every feature to find what nobody uses, and data teams ship assets with no equivalent.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #automation #confidence-intervals #revenue-impact #survival-analysis #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to turn query logs, lineage and cost data into a standing account of what each asset is worth — and whoever produces that takes the account.

## The Problem
Product analytics established the practice of knowing which features are used. Adoption is tracked per feature and per cohort, abandonment is identified, and features that nobody uses are removed rather than maintained indefinitely. The discipline is standard, the tooling is commodity, and the underlying idea — that shipping something is not the same as it being used — is uncontroversial. Data teams ship hundreds of assets a year and track none of it.

## What Already Exists
Per-feature adoption tracking; cohort and segment breakdowns of use; abandonment identification; usage trends over time; and removal decisions driven by usage.

## The Customization Gap
The adaptation is to assets consumed by queries rather than by interface interactions. It requires: (1) usage arriving as query logs against objects rather than as instrumented events, so the analysis is over an existing log rather than something to instrument — this is the substantive difference and makes it far cheaper; (2) a dependency graph where assets are consumed by other assets as well as by people; (3) cost per use that is directly attributable in consumption-priced platforms, which product analytics rarely has; (4) internal consumers rather than customers, so small audiences may still be critical; and (5) an estate that is a supply chain rather than a product surface.

## Target Customer
Data platform teams, integrators, catalogue and observability vendors, and product analytics providers.

## Impact If Solved
Product analytics made it uncontroversial that shipping is not the same as being used, with commodity tooling. Usage arriving as an existing query log rather than instrumented events is what makes the data version cheaper to build.
