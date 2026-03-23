# Multi-Shipment Consolidation Optimizer

**Niche:** [[niches/freight-brokerage/ltl-consolidation/profile|LTL Consolidation Brokerages]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool analyzes a broker's daily pool of LTL shipments to identify which shipments should be consolidated into partial truckloads, which carrier offers the best consolidated rate, and what pickup/delivery coordination is required — turning reactive individual shipment quoting into proactive consolidation planning.
**Tags:** #k-means-clustering #gradient-boosting #automation #revenue-impact

## The Problem
An LTL broker with 50 shipments per day handles each individually: quote the shipment, select the cheapest carrier, book it. But some of those 50 shipments share origin regions, destination regions, and timing — they could be consolidated into a partial truckload at a significantly lower per-hundredweight rate than individual LTL. Identifying these consolidation opportunities manually requires scanning the entire shipment pool, matching by geography and timing, and re-quoting as a consolidated volume. Most brokers don't have time and miss 15-30% of consolidation opportunities.

## Why Nobody Has Built This
Consolidation optimization is a combinatorial problem that grows exponentially with shipment count. Each potential consolidation requires re-quoting with LTL carriers at the combined weight and freight class, checking pickup/delivery window compatibility, and comparing the consolidated rate against individual rates. Carrier rate APIs (SMC3) support individual shipment quotes but aren't designed for batch consolidation analysis. Building this requires both the optimization engine and the carrier rate API integration layer.

## What to Build
A daily consolidation planning engine that: (1) ingests the broker's pending LTL shipment pool; (2) clusters shipments by origin region, destination region, and pickup window; (3) evaluates consolidation scenarios by re-quoting clusters as combined shipments through carrier rate APIs; (4) presents the top consolidation opportunities with savings estimates and required coordination steps. The broker reviews and approves consolidations before booking.

## Target Customer
LTL desk managers at brokerages handling 30+ LTL shipments daily. Approximately 800 brokerages have dedicated LTL operations at this volume. Average contract value: $18-30K/year.

## Impact If Built
Consolidating 20% of shipments into partial truckloads saves 25-40% on per-shipment cost for those loads. On a $5M LTL book of business, this generates $250K-$400K in additional annual gross profit from consolidation margin improvement.
