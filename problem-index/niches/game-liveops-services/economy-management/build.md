# The Economy as a System, Not a Spreadsheet

**Niche:** [[niches/game-liveops-services/economy-management/profile|Economy Management]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An economy with millions of participants and complete telemetry is balanced by hand in a spreadsheet.
**Tags:** #time-series-forecasting #monte-carlo-methods #causal-inference #confidence-intervals #evaluation-metrics #descriptive-statistics #optimization-fundamentals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep a currency economy with millions of participants in balance when it is tuned by hand and the drift that ruins it compounds invisibly for a quarter — and whoever makes the economy legible takes the account.

## The Problem
A live game economy is a dynamic system: stocks of currency and items, flows in from rewards and purchases, flows out through sinks, and a population whose behaviour responds to all of it. Designers manage it as a set of numbers in a sheet, tuned against intuition and adjusted when something obviously breaks. The telemetry to model it properly is complete and already collected, and the modelling is not difficult — it simply has no owner and no tooling.

## Why Nobody Has Built This
Live ops platforms sell execution rather than analysis, so the config console has no model behind it. The designers who would use it are not modellers and the modellers are pointed at monetisation. The consequence of drift arrives slowly enough to be blamed on content or competition. And nothing in the standard dashboard set would reveal it, so nobody knows there is a gap.

## What to Build
Model the stocks and flows before touching the design. Construct the economy's balance sheet — currency and item stocks held by the population, and every faucet and sink with its measured throughput — which is the core and does not exist in any team's tooling today. Report a price level and a currency stock per capita as standing metrics, since an economy with no measured price level cannot be said to be managed at all. Show the distribution rather than the mean, because the average player's balance conceals a hoarding tail and an exhausted majority that need opposite interventions. Attribute inflow and outflow to specific events and systems, as designers currently cannot say which feature is the leak. Forecast the stock and price level forward under the current configuration, which converts drift from a discovery into a prediction. Simulate a proposed change before it ships, which is the whole prize and is feasible from the same telemetry. Alert on divergence from the forecast rather than on threshold breaches, since drift has no threshold. Model player cohorts separately, as a new player and a three-year veteran inhabit different economies. Keep a history of parameter changes joined to the economy's response, which is how the model calibrates. And report it in the designer's language rather than in economic terminology, which determines adoption entirely.

## Target Customer
Live game operators, live ops platform vendors, economy design teams, and games consultancies.

## Impact If Built
An economy with no measured price level cannot be said to be managed at all, and none of these games report one. A balance sheet of stocks and flows built from telemetry already collected makes the drift a forecast rather than a discovery.
