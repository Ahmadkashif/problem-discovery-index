# Stormwater Modeling Integration for Civil 3D Workflows

**Niche:** [[niches/engineering-consultants/civil-site-engineering/profile|Civil/Site Engineering Firms]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Stormwater modeling tools exist but live outside the Civil 3D design environment — engineers manually transfer grading, drainage areas, and pipe networks between the design model and the hydrology tool, introducing errors and doubling the effort.
**Tags:** #data-integration #automation #workflow-orchestration #quick-win

## The Problem
Stormwater management design is a two-tool workflow: the engineer designs the site grading, drainage areas, and pipe network in Civil 3D, then exports parameters to a separate hydrology tool (HydroCAD, StormCAD, EPA SWMM) for detention sizing and hydraulic calculations. When the grading changes — which happens 5-10 times per project — every drainage area must be redelineated and the hydrology model rerun. The engineer manually copies revised areas, runoff coefficients, and pipe sizes between tools, a process that takes 2-4 hours per iteration and is the primary source of stormwater calculation errors.

## What Already Exists
HydroCAD, Bentley StormCAD, and Autodesk Storm and Sanitary Analysis (SSA) all perform stormwater modeling. SSA is the closest to an integrated solution since it runs inside Civil 3D, but its hydrologic engine is limited (no SCS Type III storm support in many versions, poor detention pond routing options) and it doesn't auto-detect drainage area changes from Civil 3D surface modifications. Bentley products have strong hydrology but require Bentley licensing and a separate modeling environment.

## The Customization Gap
The gap is bidirectional live linkage between the Civil 3D surface model and the hydrology engine. When an engineer modifies grading in Civil 3D, the stormwater model should auto-update drainage areas, recalculate runoff, and flag whether detention sizing still complies with the municipality's release rate criteria. This requires: (1) automatic drainage area delineation from Civil 3D surfaces, (2) a hydrology engine that supports jurisdiction-specific methods (Rational, SCS, Modified Rational — with the correct rainfall data by county), and (3) a feedback loop that flags pipe undersizing or detention inadequacy before the engineer exports the plan set. No current tool delivers all three in a Civil 3D-native workflow.

## Target Customer
Civil engineers at site development firms who perform 20+ stormwater designs per year and currently spend 15-25% of project hours on hydrology model setup and iteration.

## Impact If Solved
Reduces stormwater design iteration time by 50-60%, saving 8-15 hours per project. Eliminates 80% of stormwater calculation transfer errors, which currently cause 5-10% of municipal review rejections.
