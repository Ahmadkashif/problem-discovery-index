# Program-Specific Tribal Knowledge Loss

**Niche:** [[niches/electronics-contract-mfg/high-mix-low-volume-ecms/profile|High-Mix Low-Volume EMS Providers]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** When a process engineer leaves, the undocumented knowledge of how to run 50-200 customer programs — which components need slower placement, which reflow zone needs 3 degrees hotter on this board, which test points have intermittent contact issues — leaves with them, causing yield drops across every program they managed.
**Tags:** #tacit-knowledge-ml #data-integration #worker-facing

## The Problem
Each customer program at an HMLV EMS provider accumulates process knowledge over months or years of production: specific component placement adjustments (component X on pad Y requires 0.2mm offset to compensate for pad design error in the customer's Gerber), reflow profile tweaks (zone 4 needs +3C on this board because the ground plane near U7 acts as a heat sink), test fixture workarounds (test point TP12 has marginal pad size — increase probe force by 20g), and rework techniques (BGA U3 must be reballed before rework due to the customer's non-standard pad finish). This knowledge exists as handwritten notes, sticky notes on machines, informal conversations between engineers, and undocumented MES parameter overrides. When an engineer leaves, this knowledge is lost and must be rediscovered through defects and yield drops.

## Why It's Still Broken
MES platforms capture the current parameter settings but not the reasoning behind parameter deviations from standard. Process engineers make adjustments in real time during production and do not have a convenient mechanism to document the why — they would need to stop production, navigate to a documentation system, and write a process note. The effort-to-value ratio discourages documentation in the moment. Over time, the cumulative undocumented adjustments across hundreds of programs become the engineer's most valuable knowledge — and the company's most fragile asset.

## What a Fix Looks Like
A lightweight process knowledge capture system embedded in the production workflow — when an engineer changes a parameter in the MES or placement machine, the system prompts for a brief reason (dropdown + optional text), stores the deviation with context (program, component, date, yield before/after), and builds a searchable knowledge base per program. When a different engineer runs the same program, all historical deviations and their rationale are displayed. When a new program with similar BOM characteristics is launched, relevant deviations from similar programs are suggested.

## Who Feels the Pain
NPI directors who see yield drop 5-10% across multiple programs when an experienced process engineer departs. Production managers who field quality complaints during the 3-6 month relearning period. Process engineers who inherit programs and must rediscover knowledge that someone else already developed.

## Impact If Fixed
Post-departure yield recovery time drops from 3-6 months to 2-4 weeks. Cross-training between engineers becomes practical because program knowledge is accessible, not personal. Institutional process knowledge becomes a company asset rather than an individual liability — reducing single-person dependency risk across the program portfolio.
