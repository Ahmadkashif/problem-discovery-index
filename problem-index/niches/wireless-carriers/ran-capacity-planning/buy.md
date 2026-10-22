# RF Planning Tools Extended to Fixed Wireless Load

**Niche:** [[niches/wireless-carriers/ran-capacity-planning/profile|RAN Capacity Planning & Spectrum Deployment]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Planning tools model coverage and interference well, but treat traffic as an input, and the fastest-growing traffic on the network, fixed wireless homes, behaves differently from phones.
**Tags:** #time-series-forecasting #feature-engineering #monte-carlo-methods #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to predict, sector by sector, when mobile and fixed wireless demand will exhaust capacity and which fix — a new carrier, a sector split, a small cell or a cap on fixed wireless sales — buys the most relief per dollar, and whoever forecasts exhaustion earliest and most accurately takes the planning budget.

## The Problem
Fixed wireless households are stationary, stream heavily in the evening and sit at fixed signal quality, so their load per subscriber depends on where in the sector they are. Planning tools spread traffic by generic maps and don't know where FWA customers sit or how many more the sector can take.

## What Already Exists
Forsk Atoll, Infovista Planet and vendor capacity modules, with traffic maps, Monte Carlo capacity simulation and spectrum planning.

## The Customization Gap
The adaptation needs FWA subscribers placed at their actual addresses with measured signal quality, per-household load profiles by plan tier, simulation of each candidate address's marginal effect on mobile busy-hour throughput, and outputs expressed as "FWA homes this sector can still take at target mobile performance", feeding sales eligibility directly.

## Target Customer
RAN planning teams at carriers selling FWA at scale, and the planning tool vendors themselves.

## Impact If Solved
FWA sales continue where capacity allows and stop where they would degrade phone customers, decided by the same model engineering uses for capex.
