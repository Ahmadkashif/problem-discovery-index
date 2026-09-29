# Record Linkage Adapted to VIN-Level Event Ambiguity

**Niche:** [[niches/auto-dealers-independent/vehicle-history-report-providers/profile|Vehicle History Report Providers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The VIN makes entity resolution look solved, which is why the hard problem is invisible: deciding whether three records describing damage to the same vehicle in the same month are one event or three.
**Tags:** #graph-neural-networks #contrastive-learning #bert #transformers #random-forests #k-means-clustering #evaluation-metrics #probability-distributions #data-integration #automation

## The Problem
Records arrive from tens of thousands of independent sources describing events on a vehicle, and the report must present a coherent history rather than a merged log. The vehicle identity is rarely the issue; the event identity is. A collision may generate an insurance claim record, a body shop service record, a police report, and a title brand — one event, four sources, four different dates, four different descriptions, sometimes a transposed VIN character or a mis-keyed odometer. Present them separately and the report shows four incidents where there was one, which materially misstates the vehicle and is the most damaging error the product can make. Merge too aggressively and two genuine incidents collapse into one, which is worse. The reconciliation is handled by accumulated rules, extended each time a new failure mode is discovered, and nobody can characterize how often it is wrong.

## What Already Exists
Entity resolution and record linkage are mature and competitive. Senzing, Zingg, Quantexa, and the enterprise MDM platforms all handle probabilistic matching, transitive clustering, survivorship, and human review queues at scale, with good tooling for blocking and for measuring match quality. For resolving records to entities, the market is well served.

## The Customization Gap
Every one of these resolves records to entities, and the entity here — the vehicle — is already resolved by the VIN. The unresolved layer sits above it: grouping a vehicle's records into events, which is a temporal and causal clustering problem rather than an identity problem. Nothing off the shelf models it, because in most domains events come with identifiers. The adaptation is an event resolution layer over the vehicle timeline where the primitives are automotive: event types with characteristic multi-source signatures, expected reporting lag by source type — an insurance record and a title brand for the same collision are typically weeks apart, and treating date proximity as the merge criterion gets it wrong — and causal ordering constraints, since a total loss brand cannot precede the loss. Odometer readings act as a strong consistency check across the whole timeline and are currently used only for rollback detection. Confidence must be explicit per grouping, so ambiguous cases can be presented as ambiguous rather than silently resolved in one direction.

## Target Customer
Heads of data engineering and product at history report providers, and the analysts who maintain the reconciliation rule set and absorb every new failure mode by hand.

## Impact If Solved
Removes the error class that does most reputational damage, in both directions — phantom incidents that wrongly devalue a clean vehicle and merged incidents that hide a bad one. Explicit event grouping with confidence also makes the report interpretable in a way it currently is not, which is what a dealer pricing inventory or a lender assessing collateral actually needs from it.
