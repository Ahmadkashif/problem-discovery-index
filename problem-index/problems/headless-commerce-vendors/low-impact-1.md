# Catalogue and Pricing Consistency Across Services

**Industry:** [[headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every service in the stack keeps its own copy of the catalogue for performance, synchronisation is a solved engineering problem, and the copies still disagree in ways that charge customers the wrong price.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #graph-theory #evaluation-metrics #data-integration #workflow-orchestration

## The Problem
In a composed stack the product catalogue exists in several places. The commerce engine holds the canonical record. Search holds an indexed copy for retrieval. Personalisation holds attributes for targeting. The content management system holds merchandising content keyed to products. The front end caches at the edge. Pricing may be computed by a dedicated service with its own rules.

Each copy exists for a good reason and each can drift. A price change propagates to some services immediately and others on a schedule. A product goes out of stock and search still returns it. An edge cache serves a page with yesterday's promotion after it expired.

Most drift is invisible and harmless. The consequential cases are specific: a customer sees one price and is charged another, a promotion applies at the cart and not at payment, an item is purchasable and unfulfillable.

These are handled reactively. A customer complains, support investigates, engineering finds a stale cache, and the incident closes. Nobody knows how often it happens, because nothing checks.

## What Already Exists
Event-driven synchronisation with message queues is the standard architecture and works. Cache invalidation strategies are well understood. Product information management systems provide a canonical source. Distributed tracing can follow a request across services. Feature flags and staged rollouts are common. Each vendor monitors its own component's health.

## The Customisation Gap
Synchronisation is implemented and verification is not. Nothing periodically asks every service what it believes about the same product and compares the answers, which is a straightforward check that would surface drift immediately and is absent from every composed stack.

Consequence weighting is missing. A stale product description matters little and a stale price matters enormously, and drift detection should be weighted by the field's commercial consequence rather than treating all divergence equally.

Propagation timing is unmeasured. How long a price change takes to reach every service is knowable by instrumenting the propagation, and it is the number that determines how large a window of inconsistency exists after every merchandising action — which nobody can currently state.

Edge caching is the least visible layer and the most likely to serve stale content, since invalidation across a content delivery network is genuinely awkward and is frequently the actual cause when a customer sees an expired promotion.

## Impact If Solved
Price and inventory inconsistency charges customers incorrectly and sells items that cannot be shipped, and it is discovered by complaint because nothing verifies. Continuous cross-service comparison weighted by consequence is a small piece of engineering that makes a whole class of silent failure visible.
