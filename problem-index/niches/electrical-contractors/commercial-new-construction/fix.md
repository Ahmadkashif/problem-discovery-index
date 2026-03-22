# Trade Coordination Conflict Resolution

**Niche:** [[niches/electrical-contractors/commercial-new-construction/profile|Commercial New Construction]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Electrical contractors discover conduit routing conflicts with HVAC and plumbing during installation — by which point the fix costs 5-10x what it would have cost to resolve during pre-construction coordination meetings that currently rely on overlaying paper drawings on a conference table.
**Tags:** #data-integration #workflow-orchestration #automation #compliance #cnns #object-detection #worker-facing

## The Problem
Commercial construction coordination meetings happen weekly during the pre-construction and rough-in phases. The electrical foreman, HVAC foreman, plumbing foreman, fire sprinkler contractor, and general contractor sit in a trailer and overlay their 2D drawings on a table or screen to identify routing conflicts. This process is manual, visual, and incomplete — participants focus on the most congested areas (mechanical rooms, ceiling plenums above corridors) but miss conflicts in less obvious locations. When a conflict is found in the field during installation, the last trade to arrive reroutes — which is often electrical, because conduit is typically the last MEP system installed in a ceiling plenum. Rerouting costs $2K-10K per instance (new conduit, additional supports, possibly new wire pulls), and the electrical contractor bears the cost because "they should have caught it in coordination." On a typical 50,000 SF commercial project, electrical contractors absorb $15K-40K in conflict-related rework.

## Why It's Still Broken
The coordination meeting process hasn't changed in 30 years because no one owns the problem. The GC runs the meeting but doesn't have the technical expertise to identify MEP conflicts in detail. Each trade contractor sees only their own drawings and relies on the GC to overlay them. Digital plan overlay tools (Bluebeam) help but still require someone to visually scan every sheet for conflicts — a task that takes hours and is error-prone when drawings are at different scales or use different reference grids. The conflict data from past projects (which areas had conflicts, which trade combinations conflict most frequently) is never captured or analyzed, so every project starts from zero.

## What a Fix Looks Like
A pre-construction coordination platform where each trade uploads their 2D routing drawings, the system auto-aligns them to the architectural floor plan grid, overlays all trades with color coding, and uses spatial analysis to flag potential conflict zones — areas where two or more trades' routing occupies the same ceiling plenum zone within 6 inches of clearance. The platform generates a conflict report organized by location (room/area), severity (definite overlap vs. tight clearance), and recommended resolution sequence (which trade should reroute, based on installation difficulty). Conflict history from previous projects trains a model to predict high-risk zones on new projects based on building type and program.

## Who Feels the Pain
Electrical foremen who arrive at a ceiling plenum to find HVAC ductwork already installed exactly where their conduit was supposed to run, project managers tracking change orders caused by coordination failures, and EC owners absorbing rework costs that eat their project margins.

## Impact If Fixed
Reduces electrical conflict rework costs by 60-80% ($10K-30K savings per project) by identifying conflicts during pre-construction when resolution is a drawing change, not a field rework. Saves 1-2 weeks of schedule delay per project from avoided field conflicts.
