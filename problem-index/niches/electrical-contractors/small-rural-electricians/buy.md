# Material Procurement Optimizer

**Niche:** [[niches/electrical-contractors/small-rural-electricians/profile|Small & Rural Electricians]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Rural electricians drive 1-2 hours round trip to the supply house — a tool that consolidates material lists across upcoming jobs, checks supply house inventory before driving, and suggests order batching saves 3-5 hours per week in windshield time.
**Tags:** #gradient-boosting #feature-engineering #automation #data-integration #time-series-forecasting #workflow-orchestration

## The Problem
For urban electricians, the supply house is a 15-minute drive — running out of 12/2 Romex on a job means a quick trip. For rural electricians, the nearest electrical distributor (Graybar, WESCO, Rexel, or a local independent) is often 30-60 minutes away. A forgotten item means a 1-2 hour round trip that wipes out the job's profit margin. Rural electricians compensate by over-stocking their trucks, tying up $5-15K in rolling inventory that may include slow-moving items they bought "just in case" months ago. The alternative is ordering materials for delivery, but small orders don't meet minimum free-shipping thresholds, and 2-3 day delivery means the job waits. Neither approach is efficient.

## What Already Exists
Electrical distributors have B2B portals (Graybar.com, Rexel's e-commerce platform) with inventory and pricing, but these are designed for counter staff, not field electricians. Supply house apps exist but only show that distributor's inventory — not comparative pricing across distributors. Truck inventory management tools exist for larger fleets (eTool Tracker) but are overkill for a one-person shop.

## The Customization Gap
The gap is between the job estimate (which specifies materials needed) and the supply house run (which happens ad hoc). A procurement optimizer would: (1) extract material lists from upcoming job estimates (auto-generated from the build tool or manually entered); (2) consolidate materials across the next 3-5 days of scheduled jobs into a single procurement list; (3) check real-time inventory at the electrician's preferred supply house(s) via B2B portal APIs or screen scraping; (4) recommend order batching — "Order these 15 items for pickup Wednesday, estimated total $1,847, all in stock at Graybar Springfield" — or flag items that need to be ordered for delivery with lead time estimates; (5) track truck inventory — when the electrician loads materials, deduct from the procurement list; when they return unused materials, add them back to truck inventory. A gradient-boosted model trained on the electrician's historical material usage predicts commonly needed consumables (wire nuts, connectors, boxes) to suggest restocking before they run out.

## Target Customer
Rural electricians making 3-5 supply house trips per week, each 1-2 hours round trip. Also small shops (2-3 person) in suburban/rural areas where supply house distance creates procurement inefficiency.

## Impact If Solved
Reduces supply house trips from 3-5 per week to 1-2 through batching and advance inventory checking, saving 3-6 hours per week of drive time. Reduces truck inventory carrying cost by 30-40% through demand-driven stocking instead of "just in case" over-buying. Eliminates the "forgot one item" return trip that kills job profitability on rural service calls.
