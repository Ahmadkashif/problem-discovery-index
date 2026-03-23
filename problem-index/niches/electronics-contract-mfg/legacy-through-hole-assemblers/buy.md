# Lightweight MES for Manual Assembly Shops

**Niche:** [[niches/electronics-contract-mfg/legacy-through-hole-assemblers/profile|Legacy Through-Hole Assembly Houses]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** MES platforms like Aegis and Cogiscan are designed for automated SMT lines with machine integration — THT assembly shops need a simpler system that tracks manual operations (insertion, wave solder, touch-up, inspection, test) with barcode scan at each station, without the complexity and cost of machine-integrated MES.
**Tags:** #automation #workflow-orchestration #quick-win

## The Problem
THT assembly shops running on paper travelers cannot answer basic questions without physically locating the paper traveler on the shop floor: which boards are at which station? How many hours of work are queued at wave solder? When will this customer's order ship? The paper traveler moves with the board; if the board sits at a station for 2 days, the traveler (and its information) sits with it. Shop managers walk the floor 3-4 times per day to assess status. Customers call for updates and get "I'll check and call you back." This is operationally functional at 10-15 orders per week but breaks at 20+.

## What Already Exists
Enterprise MES platforms (Aegis FactoryLogix, Cogiscan, 42Q) provide production tracking but require machine integration, extensive configuration, and cost $50-200K to implement — uneconomical for a THT shop with $2-10M revenue. Lightweight manufacturing tracking tools (Tulip, Fulcrum) offer configurable workflow apps but require significant setup and lack electronics-specific features.

## The Customization Gap
THT shops need a system that costs $500-1,500/month, deploys in 1-2 weeks, and works with barcode scanners at each manual station (insertion bench, wave solder, touch-up, inspection, test, pack). Operators scan the board's traveler barcode when they start and finish work at each station. The system tracks cycle time per operation, displays real-time WIP by station, alerts the shop manager when a board has been at a station beyond expected cycle time, and provides customer-facing order status without phone calls. No machine integration needed — just barcode-based station tracking for manual processes.

## Target Customer
Owners and shop foremen at THT assembly shops processing 15+ orders per week. Approximately 200-300 US shops. Target price: $500-1,500/month.

## Impact If Solved
Real-time WIP visibility replaces floor walks, saving the shop manager 1-2 hours per day. Customer status inquiries are answered by self-service portal instead of phone calls, saving 30-60 minutes per day. Bottleneck identification enables workload rebalancing, improving throughput by 10-15%.
