# One Lost-Energy Ledger Across Every OEM

**Niche:** [[niches/renewable-power-producers/fleet-asset-performance-om/profile|Fleet Asset Performance & O&M]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An owner with five turbine makers and three inverter vendors cannot say, in one consistent set of categories, how many megawatt-hours each plant lost last month and why.
**Tags:** #feature-engineering #gaussian-processes #time-series-forecasting #descriptive-statistics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to recover the most lost energy per dollar of operations and maintenance", but wind and solar lose energy in different ways, to different vendors, on different data: wind is won on avoiding crane-dependent drivetrain failures, solar on clearing the many small inverter, tracker and string losses. Decomposed into contested sub-niches below.

## The Problem
Each OEM's supervisory system labels downtime with its own codes, each service contract defines availability differently, and curtailment, grid outages and weather are excluded from some figures and not others. The asset performance team rebuilds a fleet loss waterfall in spreadsheets every month, and the categories never quite match.

## Why Nobody Has Built This
Asset performance vendors normalise data inside their own platforms but follow each contract's definitions, because availability guarantees are what owners argue over. Expected output per interval needs a good power-curve or irradiance model per asset, and the event codes need mapping per turbine platform.

## What to Build
A fleet ledger that computes expected energy for every turbine and inverter in every interval from met and irradiance data, compares it with metered output, and assigns each lost megawatt-hour to one owner-defined cause (equipment fault by component, scheduled maintenance, grid outage, curtailment by type, icing, soiling, performance degradation), with the contract-specific availability numbers derived from the same base.

## Target Customer
Vice presidents of asset performance at IPPs running mixed-OEM fleets over ~2 GW.

## Impact If Built
At a 5 GW fleet losing ~4% of potential output to controllable causes (estimate), seeing losses by cause in one ledger and recovering a quarter of them is worth ~$7–9M a year at ~$45/MWh.
