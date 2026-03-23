# Automatic Per-Load P&L from Connected Data Sources

**Niche:** [[niches/owner-operator-trucking/per-load-profitability-tracking/profile|Per-Load Profitability Tracking]]
**Industry:** [[industries/owner-operator-trucking|Owner-Operator Trucking]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool automatically calculates per-load profit by connecting rate confirmations, ELD mileage, fuel card charges, and toll data — every operator flies blind on their most important metric.
**Tags:** #data-integration #automation #revenue-impact #quick-win

## The Problem
An operator completes a load and deposits the check. Did they make money? They think so, because the rate exceeded their mental cost estimate. But without allocating actual fuel consumed (from the fuel card, apportioned to this load's miles), actual tolls (from the toll transponder or EZPass statement), deadhead cost to pickup, maintenance reserve ($0.15-$0.20/mile), insurance allocation, and HOS opportunity cost (hours consumed that could have been used for another load), they genuinely don't know. An operator running 200 loads/year might have 40 loads that actually lost money after true cost allocation — and they never find out until the annual tax return shows lower profit than expected.

## Why Nobody Has Built This
Each cost component lives in a different system: revenue in rate confirmations (PDF or email), fuel in the fuel card portal, tolls in the transponder account, miles in the ELD, and maintenance in shop invoices. Building a per-load P&L requires: (1) ingesting all these data sources, (2) matching expenses to specific loads (the fuel purchased at mile 400 of a 700-mile haul belongs to that load), and (3) allocating fixed costs (insurance, ELD subscription) across loads by mile or hour. This is a data integration problem, not an ML problem — but it's hard because every operator uses a different combination of fuel card, ELD, and toll system.

## What to Build
A per-load P&L engine that connects to: (1) rate confirmations (photo/PDF upload with OCR, or load board API), (2) ELD provider (miles per load via API), (3) fuel card (purchases geo-matched to loads via timestamp and location), (4) toll transponder (charges matched to load routes), and (5) user-configured fixed cost allocations (insurance $/month, maintenance reserve $/mile). Output: a per-load profit card showing gross revenue, itemized costs, net profit, and profit-per-hour. Portfolio view: load history sorted by profitability, with lane-level and broker-level aggregation.

## Target Customer
Any owner-operator who wants to know their true per-load profit — currently 90%+ of the 350,000 US OOs who lack this visibility.

## Impact If Built
Operators who track per-load profitability consistently improve their load selection by 15-25% over 6 months, translating to $10,000-$25,000/year in additional net income from avoiding unprofitable loads and prioritizing high-profit lanes.
