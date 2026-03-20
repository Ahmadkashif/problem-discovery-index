# Parts Sourcing Optimization

**Industry:** [[auto-repair-shops|Auto Repair Shops]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Parts ordering tools can search catalogs, but they can't optimize the daily decision of which supplier to use for each part considering price, availability, quality tier, delivery time, and core return logistics.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #entropy-cross-entropy-kl-divergence #automation

## The Problem
A typical shop orders 15-40 parts per day across 3-6 suppliers. Each part has multiple options: OEM, premium aftermarket, economy aftermarket, and remanufactured. The same brake rotor can cost $35 from AutoZone, $52 from NAPA, and $78 from the dealer — but the $35 option might be backordered and the $78 option comes with a 3-year warranty vs. 1-year. Parts specialists spend 1-2 hours daily comparing options, calling suppliers, and managing delivery logistics. The wrong choice costs money (overpaying), time (waiting for backorders), or quality (cheap parts that fail).

## What Already Exists
PartsTech and Nexpart aggregate catalogs from multiple suppliers for single-screen comparison. RepairLink connects to dealer inventories. These tools show availability and price but don't learn from the shop's purchase patterns, quality outcomes, or customer segment needs.

## The Customisation Gap
An intelligent parts sourcing system would need to: (1) learn the shop's quality-tier preferences by repair type and customer segment, (2) predict delivery times based on historical supplier performance not just listed availability, (3) optimize daily ordering across suppliers to hit volume discount thresholds, (4) track warranty claim rates by supplier/brand to inform future sourcing, and (5) factor in core return logistics for remanufactured parts.

## Impact If Solved
Saves 1-2 hours of parts specialist time daily. Reduces parts cost 8-15% through optimized supplier selection and volume consolidation. Decreases parts-related comebacks by routing away from suppliers with high failure rates.
