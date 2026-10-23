# Vendor-Managed Inventory Adapted to Utility Alliances

**Niche:** [[niches/electrical-distributors/utility-grid-supply/profile|Utility & Grid Supply]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** VMI software replenishes bins on usage; utility alliances replenish against work plans, storm reserves and multi-year transformer lead times.
**Tags:** #time-series-forecasting #exponential-smoothing #data-integration #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to keep a utility's or co-op's transformers, cable, meters and line hardware on the shelf under an alliance agreement through storms and multi-year lead times, and whoever posts the highest fill rate when the storm hits takes the account.

## The Problem
Generic VMI replenishes when usage draws a bin down. Utility materials demand is lumpy, driven by capital work plans, new-service connections and storms, and the longest-lead items need orders placed long before usage shows.

## What Already Exists
VMI and min/max replenishment in distributor ERPs, utility materials-management modules in SAP and Oracle, and EDI order and forecast transactions.

## The Customization Gap
Demand built from the utility's work-order backlog and capital plan rather than past usage; separate storm-reserve stock that normal usage cannot draw down; transformer ratings and kVA classes treated as substitutes only where engineering allows; allocation rules across several utilities during a regional event; and fill-rate reporting in the alliance's own terms.

## Target Customer
Distributors running utility alliances that already operate VMI for industrial customers.

## Impact If Solved
Existing replenishment tools start matching how utilities actually consume material, with fill rates of ~95%+ on planned work auditable in the alliance's own terms (estimate) and emergency expedites cut by ~a third (estimate).
