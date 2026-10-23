# Plan Revisions Mapped to the Trusses They Touch

**Niche:** [[niches/building-material-dealers/truss-wall-panel-designers/profile|Truss & Wall-Panel Component Designers]]
**Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A revised plan set arrives and the designer spends hours finding what changed; a tool that finds the changes and the components they affect gives the hours back.
**Tags:** #tacit-knowledge-ml #object-detection #graph-neural-networks #transformers #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a house plan and its revisions into approved, buildable truss and wall-panel layouts with fewer designer hours, and whoever gets layouts approved with the fewest field fixes per designer-hour takes the account.

## The Problem
Builders revise plans after the truss order is designed: a moved wall, a raised ceiling, a new window. Each revision means comparing two PDF sets, finding the structural changes and redesigning the affected trusses and panels.

## Why Nobody Has Built This
Design software starts from the designer's model, not from the drawings, and drawing-comparison tools highlight pixels, not bearings and spans.

## What to Build
A revision engine that aligns two plan sets, extracts changes to walls, bearings, openings, ceiling heights and roof geometry, maps each to the affected components in the existing design (via the plate software's export), and drafts a revision list for the designer. It records which suggestions the designer accepts, building the first dataset of design judgement. A demo uses two public plan revisions and a synthetic truss layout.

## Target Customer
Design managers at dealer-owned component plants.

## Impact If Built
If revision handling falls from hours to under one per change (estimate), designers absorb plan churn without evening work and the plant sees fewer field fixes.
