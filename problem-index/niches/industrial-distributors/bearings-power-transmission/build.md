# An Installed-Base Map of Every Plant's Rotating Equipment

**Niche:** [[niches/industrial-distributors/bearings-power-transmission/profile|Bearings & Power Transmission Distribution]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A BPT distributor sells a plant the same bearings for twenty years without a record of which machine each one goes into.
**Tags:** #graph-theory #large-language-models #cnns #feature-engineering #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep the plant's rotating equipment turning, but that splits into two contests with different winners: putting the exact replacement on the machine inside the downtime window, and calling the failure before it stops the line. Decomposed into contested sub-niches below.

## The Problem
A plant has hundreds of motors, pumps, gearboxes, fans and conveyors, each with bearings, seals, belts and couplings. The distributor's invoice history shows what the plant bought; the plant's maintenance system, if it is kept up, shows work orders. Neither records the component-level bill of materials for each machine. So every breakdown starts with identification from scratch, every reliability programme starts with a weeks-long asset survey, and the distributor cannot stage critical spares because it doesn't know what is critical.

## Why Nobody Has Built This
Asset surveys are manual walk-downs that go stale. The plant owns the asset list and rarely shares it in usable form; the distributor owns the sales history but not the machine context. Manufacturers publish machine and motor bills of materials inconsistently, and nobody has had an incentive to join the three.

## What to Build
A component-level installed-base graph per plant: machines, positions and the parts in them, built from three sources. Purchase history is mapped to machines through the work orders and requests that triggered each sale. Nameplate photos and OEM documents are read to propose bills of materials. Technicians confirm proposals during routine visits. The graph flags critical positions with long lead times and no stock, and it feeds both breakdown identification and reliability routes.

## Target Customer
BPT distributors with reliability services or onsite reps at mid-size and large plants; reliability managers at those plants.

## Impact If Built
If ~60–80% of a plant's critical rotating positions are mapped to their components (estimate), breakdown identification on those positions becomes a lookup taking ~1–2 minutes instead of ~15–30, critical spares can be staged ahead of failure, and the distributor holds a plant record a competitor can't replicate at re-bid.
