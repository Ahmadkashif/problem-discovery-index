# Change Impact Routed to Affected Product Classifications

**Niche:** [[niches/customs-brokers/global-trade-content-databases/profile|Global Trade Content Databases]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A tariff action changes duty on a range of codes overnight, and every subscriber independently works out which of their own products just became more expensive.
**Tags:** #bert #transformers #large-language-models #graph-neural-networks #word-embeddings #evaluation-metrics #transfer-learning #compliance #data-integration #revenue-impact

## The Problem
The content is organized around tariff schedules and the subscriber is organized around products. When a duty action lands — a new tariff line, a trade agreement provision, a suspended preference — it matters to a given importer only if it touches the codes their goods are classified under, in the countries they source from, on the terms they use. The publisher knows the change; the subscriber knows their product catalogue; nobody joins the two. So alerting is broadcast and thousands of importers and brokers each perform the same mapping exercise against the same change, at exactly the moment when speed matters because entries are being filed against the old duty rate.

## Why Nobody Has Built This
The content grew as a reference library indexed by jurisdiction and schedule, which is right for publishing and wrong for routing. Impact routing also requires knowing the subscriber's classified product catalogue, which means an integration the publisher has historically avoided because it edges them toward being a system of record and toward liability for classifications they did not make. And cross-jurisdiction product equivalence is genuinely hard: the same product carries different codes in different countries, and the mapping between national schedules below the harmonized level is a judgment nobody has recorded systematically.

## What to Build
A product-level impact layer over the schedule content. National schedules are cross-referenced at the level where they diverge, so the system knows when a change in one jurisdiction touches goods classified elsewhere under a different code. Subscribers map their catalogue once — to their own classifications, which they already maintain — and changes route to the specific products affected, with the duty delta computed and the entries at risk identified. The routing is advisory and clearly separated from the classification itself, which preserves the boundary the publisher needs. Alerting sorts by exposure, so an importer sees the change that moves a million dollars of landed cost ahead of the one that touches a product they import twice a year. And because subscriber catalogues accumulate, the publisher gains something a reference library never has: retained value that makes leaving expensive.

## Target Customer
VPs of content and heads of trade research at content publishers running 200-800 analysts, and the global trade compliance leaders at importers whose teams currently map every tariff action to their catalogue by hand.

## Impact If Built
Turns a library into a routing engine, which is a different category with real switching costs. It also eliminates the duplicated mapping that every subscriber performs independently — the exact labour the subscription was meant to remove — and does it at the moment of maximum urgency, which is when the product's value is most visible.
