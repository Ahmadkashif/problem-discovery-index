# Fast in an Afternoon, Blocking in Month Three

**Niche:** [[niches/headless-commerce-vendors/developer-framework-headless/profile|Developer-Framework Headless]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A developer adopts the framework because a storefront runs in an afternoon and abandons it in month three when the abstraction prevents the specific behaviour their business needs.
**Tags:** #workflow-orchestration #evaluation-metrics #data-integration #automation #worker-facing #descriptive-statistics #compliance #graph-theory
**Contested on:** Every serious competitor in this sub-niche is fighting to get a developer from nothing to a working storefront faster than they could write it themselves, and to still be worth using in month six — and whoever does that takes the adoption, because the decision is made before anybody is paid.

## The Problem
A developer builds a working storefront in an afternoon from the quickstart. Three months later they need a custom cart behaviour the framework's cart abstraction does not permit, a caching strategy the framework's data layer overrides, and access to a commerce interface capability the framework does not expose. Each requires reading the framework's source, and two require patching it. They rewrite the storefront directly against the commerce interface in two weeks, which works, and the framework loses a production reference and gains a public criticism.

## Why Nobody Has Built This
Adoption is measured at the quickstart and the abandonment is invisible, so the design optimises for the first hour. Layered design that exposes every level is harder to document and demonstrates worse. Commerce is a domain where the specific requirements arrive reliably in month three, which makes the trajectory unusually predictable and unusually ignored. And the developers who leave do so quietly and are counted as adoption.

## What to Build
Design the layers so the exit is partial. Expose every level of the stack as a supported interface — the high-level component, the data primitives it composes, and the raw commerce call — so a developer needing control drops one layer instead of leaving, which is the design principle that separates frameworks people keep from frameworks people escape. Make the framework's own behaviour visible and overridable: the caching, the data fetching, the cart state management and the rendering strategy, each of which surprises somebody in production. Support incremental adoption, so a developer can use the cart component inside an otherwise hand-built storefront, which is how a framework earns its way in rather than demanding commitment. Document the overhead the framework adds in requests, payload and latency, which is currently unstated and is a real cost at scale. Treat the upgrade path as a first-class concern, since storefronts live longer than framework release cycles and pinning is the observed behaviour. Test against real catalogue sizes, which the fix note develops. Provide production references rather than demonstrations, since a developer evaluating will look for evidence it survives. And measure adoption at month six rather than at the quickstart, because that number reflects whether the design works.

## Target Customer
Developers choosing a commerce stack, the framework maintainers, and the platform vendors whose commercial products depend on framework adoption.

## Impact If Built
Adoption is measured at the quickstart and abandonment is invisible, which is why the design optimises for the first hour. Layered interfaces that let a developer drop one level rather than leave, and incremental adoption of single components, are what turn a framework into something people keep.
