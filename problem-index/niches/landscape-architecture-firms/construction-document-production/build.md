# Continuous Set Coordination Checking

**Niche:** [[niches/landscape-architecture-firms/construction-document-production/profile|Construction Document Production & Quantity Takeoff]]
**Industry:** [[industries/landscape-architecture-firms|Landscape Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The last week before every landscape deadline is spent checking that plans, schedules, details, specifications and the estimate still agree, by eye.
**Tags:** #large-language-models #transformers #object-detection #graph-theory #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to keep the plan, plant schedule, details, specifications and estimate in sync through every revision so the bid set goes out without coordination conflicts, and whoever eliminates the manual coordination pass takes the account.

## The Problem
Design changes land late: a walk moves, a bed is deleted, a paver changes, a detail is replaced. Each change breaks references somewhere — a plant count, a schedule line, a callout to a detail that no longer exists, a specification section that still names the old product, an estimate line nobody updated. The coordination pass is done manually by the most junior people at the worst time, and what it misses becomes RFIs and change orders.

## Why Nobody Has Built This
Each tool checks itself: the plant add-on reconciles its own schedule, the specification software checks its own sections. Nothing reads across the whole set — CAD, PDFs, specification documents and spreadsheets — and building BIM-style coordination for site work has been uneconomic for a small market.

## What to Build
A checker that reads the full set as a graph of references — plan objects, schedule entries, detail callouts, specification sections, estimate lines — and reports every broken or inconsistent link after each save or issue, with a change log since the last milestone and the principal's redlines tracked as items until picked up.

## Target Customer
Production managers and project landscape architects at firms of 10–200 people; multidisciplinary firms' site design groups.

## Impact If Built
The coordination pass shrinks from days to an hour of resolving flagged items, and a large share of coordination RFIs disappear from construction.
