# The Haircut Typed Into a Cell

**Niche:** [[niches/oil-and-gas-producers/inventory-spacing-type-curves/profile|Inventory, Spacing & Type-Curve Planning]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Fix (Pain Point)
**One-liner:** The spacing adjustment that decides an infill well's economics is a percentage in a spreadsheet with no reason attached.
**Tags:** #large-language-models #evaluation-metrics #feature-engineering #tacit-knowledge-ml #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to rank an operator's undrilled locations and set their spacing so the wells drilled land on the forecasts that funded them, and whoever's location forecasts come closest to realised 24-month production takes the account.

## The Problem
For a child well, the engineer cuts the analog curve by 10%, 20% or 30% for interference from older wells nearby. The number is typed into a cell. The next engineer, or the same engineer a year later, cannot tell whether it reflected distance, bench, parent age, a bad pad last quarter or a management target.

## Why It's Still Broken
Writing a reason takes time during a planning crunch, nothing in the tools prompts for it, and haircuts are politically sensitive because they lower a location's value and its rank.

## What a Fix Looks Like
Make the haircut a structured field: the drivers chosen from a short list (distance, bench, parent months on production, completion size, recent results) and a one-line reason drafted from the planning session for the engineer to confirm. Show the engineer, at the moment of entry, the last ten similar haircuts and how those wells performed.

## Who Feels the Pain
Reservoir engineers inheriting acreage, planning managers reconciling budgets, and acquirers trying to understand a seller's inventory.

## Impact If Fixed
A reasoned haircut on every infill location costs about a minute each, ~5 hours a year for a 300-location plan (estimate), and makes the spacing judgement gradable. Within two years that shows whether the team's haircuts run too deep or too shallow.
