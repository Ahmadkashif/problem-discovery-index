# The Same Explanation, Forty Times a Month

**Niche:** [[niches/observability-vendors/observability-support-cardinality/profile|Observability Support & Cardinality]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The support queue is a precise specification of what the product fails to make obvious, and nobody reads it in aggregate.
**Tags:** #bert #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to stop cardinality explosions and instrumentation gaps before they reach a support queue — and whoever does that takes the support organisation, because those two topics are most of what its engineers do all day.

## The Problem
A support engineer writes, for the fortieth time this month, an explanation of why a label containing an identifier is expensive. Another writes, for the twentieth, an explanation of why traces are not appearing from a service whose library version is incompatible with the agent. Both explanations are good, both are the same every time, and both describe a concept the product could have made obvious at the moment the customer made the choice. The queue's composition has not been analysed in two years and nobody has been asked to.

## Why It's Still Broken
Support metrics are volume, resolution time and satisfaction, which measure how well the queue is handled rather than why it exists. Ticket categorisation is done by agents choosing from a taxonomy designed before the current product, so the reported categories do not reflect what tickets are about. Nobody owns the loop from support content back to product design, and the engineers with the clearest view of the product's failures spend their day on individual instances of them.

## What a Fix Looks Like
Read the queue as a specification. Cluster tickets semantically rather than by their chosen category, which is a straightforward text analysis over the support corpus and produces the real composition — usually a small number of topics accounting for a large majority of volume. Rank by total handling time rather than by count, since a small number of deep tickets can outweigh many quick ones. For each cluster, ask the product question directly: what would have prevented this, and is it a warning, a default, a validation or a documentation change. Route the top clusters to product with the evidence attached, which is the loop that does not exist. Measure prevention rather than deflection — did the ticket class shrink after the change — which is the honest metric and avoids the failure this vault documents in support analytics where abandonment counts as success. Give support engineers a mechanism to raise a pattern rather than only to resolve instances, since they know the answer already. And publish the composition internally, because an engineering organisation that can see that a third of its support volume is one preventable concept will fix it.

## Who Feels the Pain
Support engineers repeating the same explanation; customers encountering a preventable problem the vendor has seen hundreds of times; and product teams prioritising without the clearest available evidence of what the product fails to communicate.

## Impact If Fixed
Semantic clustering over the support corpus is an afternoon's work and produces a ranked list of preventable product failures. Ranking by handling time rather than count is what makes the list reflect cost, and measuring prevention rather than deflection is what keeps the loop honest.
