# Fixed Wireless Sales Caps Set by Spreadsheet

**Niche:** [[niches/wireless-carriers/ran-capacity-planning/profile|RAN Capacity Planning & Spectrum Deployment]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Whether an address can buy fixed wireless is often decided by a per-sector cap updated by hand, so carriers both turn away customers on sectors with room and oversell sectors without it.
**Tags:** #time-series-forecasting #feature-engineering #evaluation-metrics #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to predict, sector by sector, when mobile and fixed wireless demand will exhaust capacity and which fix — a new carrier, a sector split, a small cell or a cap on fixed wireless sales — buys the most relief per dollar, and whoever forecasts exhaustion earliest and most accurately takes the planning budget.

## The Problem
To protect phone customers, carriers limit FWA sales per sector. The limits are typically set when a sector is opened for sale and revised occasionally from utilisation reports. Sectors that gained capacity from a new carrier stay closed; sectors whose mobile traffic grew stay open. Each wrong "no" is a lost household and each wrong "yes" is a congested sector.

## Why It's Still Broken
Eligibility lives in a sales system owned by marketing, capacity lives in engineering tools, and nobody owns the job of reconciling them weekly. The cap is a single number, while the right answer depends on where in the sector the address sits.

## What a Fix Looks Like
Recompute address-level eligibility weekly from current busy-hour utilisation, scheduled capacity adds and the address's expected signal quality. Push it to the sales system automatically and log every change with its reason.

## Who Feels the Pain
FWA sales and marketing teams turning away demand, RAN engineers fielding congestion complaints, and phone customers on oversold sectors.

## Impact If Fixed
Sales go where capacity exists and stop where it doesn't, with no new hardware.
