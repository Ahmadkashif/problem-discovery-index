# Changeover-Optimized Production Scheduler

**Niche:** [[niches/electronics-contract-mfg/high-mix-low-volume-ecms/profile|High-Mix Low-Volume EMS Providers]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Production scheduling tools (Aegis, SAP PP) sequence jobs by due date and priority, but HMLV EMS changeover time depends on feeder commonality between consecutive programs — two programs sharing 60% of feeders change over in 10 minutes, while two with no common feeders take 45 minutes — and no scheduler optimizes for this feeder-level similarity.
**Tags:** #reinforcement-learning #automation #revenue-impact

## The Problem
An HMLV EMS facility changes over its SMT lines 5-15 times per shift. Each changeover requires loading/unloading feeders, changing stencils, adjusting reflow profiles, and running first-article inspection. The time consumed by changeovers is 15-30% of total available production time. Changeover duration varies enormously based on feeder commonality: if consecutive programs share most of the same components (and thus feeders), the changeover is a partial swap taking 10-15 minutes; if they share nothing, it is a full changeover taking 30-45 minutes. Production schedulers sequence jobs by due date without considering feeder overlap, leaving 20-40% of potential changeover time savings on the table.

## What Already Exists
MES platforms (Aegis FactoryLogix, Cogiscan) track production schedules and feeder configurations. ERP production scheduling modules (SAP PP, Oracle Manufacturing) sequence jobs. Dedicated scheduling tools (Opcenter APS, PlanetTogether) optimize for due date, capacity, and priority constraints. None of these tools model feeder-level commonality between programs as an optimization variable.

## The Customization Gap
The scheduler must access the feeder configuration (which components in which feeder slots) for every active program, compute a changeover cost matrix (estimated changeover time between every pair of programs based on feeder overlap, stencil change requirement, and reflow profile difference), and optimize the production sequence to minimize total changeover time while meeting due date constraints. This requires integration with the placement machine's feeder database and the reflow oven's profile library — data sources that generic schedulers do not access.

## Target Customer
Production managers and scheduling coordinators at HMLV EMS providers with 3+ SMT lines and 50+ active programs. Approximately 200-300 US facilities.

## Impact If Solved
Total changeover time decreases by 20-35%, recovering 2-4 hours of productive SMT time per line per day. At $150-300/hour line rate, this represents $100-300K in annual capacity recovery per line. On-time delivery improves as schedule adherence increases.
