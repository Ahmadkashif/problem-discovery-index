# Mid-Market BIM Clash Detection for Electrical

**Niche:** [[niches/electrical-contractors/commercial-new-construction/profile|Commercial New Construction]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Navisworks and BIM 360 solve clash detection for $100M+ projects with full 3D models — mid-market commercial electrical work ($500K-5M scope) needs lightweight clash detection that works from 2D plans without a full BIM model.
**Tags:** #cnns #object-detection #semantic-segmentation #automation #data-integration #workflow-orchestration #evaluation-metrics

## The Problem
On commercial construction sites, electrical conduit routes through ceiling plenums, wall cavities, and utility chases where they share space with HVAC ductwork, plumbing pipes, and fire sprinkler lines. When two trades install in the same space without coordination, the result is a field conflict — conduit must be rerouted, supports must be relocated, and the schedule slips. On a typical mid-market commercial project, 5-15 field conflicts involve electrical conduit, costing $2K-10K each in rework labor and materials. Large projects solve this with BIM clash detection (Navisworks), but BIM requires all trades to build 3D models at a combined cost of $50K-100K per project — uneconomical for projects under $10M total value.

## What Already Exists
Autodesk Navisworks and BIM 360 Glue provide automated 3D clash detection when full models exist. Trimble's MEP tools handle 3D coordination for large projects. Procore manages 2D drawings and RFIs but has no spatial clash detection capability. Bluebeam Revu allows overlay of 2D drawings from multiple trades for visual inspection but doesn't automate conflict identification.

## The Customization Gap
Mid-market commercial projects have 2D plans, not 3D models. The opportunity is a lightweight clash detection system that works from 2D plan overlays: (1) digitize electrical routing from the electrical plans using CNN-based symbol and path recognition; (2) digitize HVAC ductwork, plumbing, and fire sprinkler routing from their respective 2D plans; (3) overlay the routes with elevation data (typically annotated on plans as "Top of Pipe" or "Bottom of Duct") and flag spatial conflicts where electrical conduit routes intersect other trades within a configurable clearance zone. The system doesn't need BIM-level precision — it needs to catch the 80% of conflicts that are obvious 2D overlaps (conduit run through duct space, panel location behind a plumbing stack) so they can be resolved via RFI before installation begins.

## Target Customer
Mid-market commercial electrical contractors ($2-15M revenue) working on projects where BIM is not mandated or budgeted. Also general contractors who want to reduce change orders caused by trade coordination failures on their mid-market projects.

## Impact If Solved
Eliminates 50-70% of field conflicts involving electrical conduit on mid-market projects, saving $10K-50K per project in avoided rework. Reduces schedule delays caused by trade conflicts by 1-2 weeks per project. At $200-500/month subscription, pays for itself on the first project.
