# Supply Chain Consolidation Across Brands

**Industry:** [[ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Consolidated purchasing is the aggregator model's headline synergy, and it requires knowing that two acquired brands' products are similar enough to buy together — which nobody can determine across forty inconsistent catalogues.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #dbscan #cnns #evaluation-metrics #data-integration #optimization-fundamentals

## The Problem
The aggregator thesis promises procurement leverage: forty brands buying from overlapping supplier bases should negotiate better than forty individual sellers.

Realising it requires knowing what is actually comparable. Two brands may both sell a silicone kitchen product from a Guangdong factory, at similar specifications, with different branding — and identifying that from the acquired catalogues is genuinely hard. Product data arrived from forty sellers who each described their goods their own way. Specifications are in supplier documents in a shared drive. Supplier names are recorded inconsistently, including for the same factory under a trading company and its own name.

So the consolidation happens where it is obvious — two brands using the same named supplier — and misses the larger opportunity in products that are similar without sharing a supplier.

Freight, packaging and quality inspection have the same shape: real aggregation opportunity, gated by not knowing what is comparable across the portfolio.

## What Already Exists
Procurement and supply chain platforms handle purchase orders, supplier management and freight competently at enterprise scale. Product information management systems exist for catalogue normalisation. Sourcing platforms and agents provide supplier discovery. Freight forwarders offer consolidation services. Quality inspection services are established. Some aggregators have deployed enterprise resource planning systems across the portfolio.

## The Customisation Gap
Enterprise tooling assumes a coherent product master, and the aggregator has forty catalogues from forty sellers with no shared structure. The product resolution layer — determining which items across brands are substitutable or share a supplier base — does not exist and everything downstream depends on it.

Supplier identity resolution is the parallel problem. The same factory appears under different names, through different trading companies, at different addresses, and consolidating spend requires knowing they are one entity.

Specification comparison is the harder half. Two products may be functionally identical with different specifications written in different formats by different sellers, and determining substitutability requires reading supplier documents rather than matching catalogue fields.

Joint order optimisation is the fourth gap: once comparability is known, deciding what to order together, when, given different demand cycles, minimum order quantities and cash constraints across brands is a real optimisation problem and is currently a negotiation between brand managers.

## Impact If Solved
Procurement leverage is the aggregator model's main claimed synergy and it is realised only where the overlap is obvious. Resolving products and suppliers across the portfolio is the enabling layer for the entire thesis, and its absence is a substantial part of why the promised synergies did not materialise.
