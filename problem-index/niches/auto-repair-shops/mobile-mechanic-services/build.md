# Van Inventory Management with Pre-Job Parts Matching

**Niche:** [[niches/auto-repair-shops/mobile-mechanic-services/profile|Mobile Mechanic Services]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool tracks what parts are in the van, matches them against upcoming jobs, and flags what to restock before tomorrow's route.
**Tags:** #recommendation #tabular-ml #automation #workflow-orchestration

## The Problem
A mobile mechanic's van carries $2,000-$5,000 in parts, but the inventory is tracked mentally. When a customer books a brake job on a 2019 Camry, the mechanic has to mentally recall whether the right pads and rotors are in the van — and if not, they need to detour to a parts store, burning 30-60 minutes and often arriving late to the job. Conversely, the van accumulates rarely-used parts that tie up cash. There's no system that connects what's in the van to what's scheduled.

## Why Nobody Has Built This
Traditional parts inventory systems assume a fixed parts room with shelves and bins. Van inventory is dynamic — parts get used, returned, swapped between vans, and restocked from different distributors depending on the day's route. The unit of tracking is "what's physically in this vehicle right now," which requires a fundamentally different UX than warehouse inventory management.

## What to Build
A mobile-first inventory system where the mechanic scans parts in/out of the van using barcode or photo recognition. The system cross-references van inventory against tomorrow's scheduled jobs (with VIN-decoded parts requirements) and generates a restock list organized by the most efficient pickup route. It tracks inventory value, flags slow-moving parts, and suggests optimal van-stocking based on the mechanic's most common repair types.

## Target Customer
Mobile mechanic operators running 1-5 vans who lose 3-5 hours per week on parts detours and carry $1,000+ in dead inventory per van.

## Impact If Built
Eliminates 3-5 hours/week of parts-run detours per van (worth $300-$600 in lost labor time), reduces dead inventory by 30-40%, and prevents 2-3 "wrong parts" job cancellations per month.
