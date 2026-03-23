# Tool and Parts Inventory Loss Across Service Vehicles

**Niche:** [[niches/fleet-managers/hvac-plumbing-service-fleets/profile|HVAC/Plumbing Service Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Service companies lose $2,000-$8,000 per vehicle per year in missing tools, misplaced parts, and unreturned equipment that migrates between vans with no tracking.
**Tags:** #automation #data-integration #worker-facing #revenue-impact

## The Problem
A plumbing company with 20 vans has $200,000+ in tools and equipment distributed across those vehicles. Tools get borrowed between technicians ("I need your pipe threader for this job"), left at job sites, or placed in the wrong van after a vehicle swap. Parts purchased for a specific job end up in a different van's stock. Over a year, 5-10% of tool and parts inventory simply disappears — not stolen, but migrated to unknown locations. When a technician needs a specific tool, they buy a new one rather than spending 30 minutes figuring out which van it's in, creating duplicate purchases.

## Why It's Still Broken
Tool tracking requires a system that's faster for the technician than ignoring it. Barcode scanning exists but adds a step every time a tool is picked up or put down — technicians won't comply. GPS tool tracking (like Milwaukee One-Key) works for power tools but not hand tools, fittings, or consumable parts. The fundamental challenge is that tracking must be zero-friction for field workers who are under time pressure and penalized for slow job completion, not for slow tool tracking.

## What a Fix Looks Like
A photo-based van inventory system where each technician photographs their van's tool/parts loadout weekly (takes 2-3 minutes). Image recognition identifies tools and parts from the photos and maintains a per-van inventory. When a tool appears in Van B that was last seen in Van A, the system flags the migration. When a tool disappears entirely, it's flagged as missing before a duplicate is purchased. The weekly photo audit is fast enough for technician compliance and detailed enough for meaningful tracking.

## Who Feels the Pain
Trades company owners who budget $10,000-$20,000 per year for tool replacements that are largely duplicates of tools that exist somewhere in the fleet, and technicians who waste 15-30 minutes per week looking for tools they know the company owns but can't locate.

## Impact If Fixed
Reduces annual tool and parts loss by 50-70% ($5,000-$15,000 per year for a 20-van fleet). Eliminates 15-30 minutes per technician per week of tool-hunting time, recovering 1-2 billable hours per technician per month.
