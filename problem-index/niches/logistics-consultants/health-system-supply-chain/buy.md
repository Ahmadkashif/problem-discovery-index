# Distribution Replenishment Adapted to Clinical Units

**Niche:** [[niches/logistics-consultants/health-system-supply-chain/profile|Health-System Supply Chains]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Replenishment logic from distribution and retail — par, two-bin kanban, RFID-triggered reorder — is installed in hospitals without the procedure-driven demand, expiry and recall rules clinical units need.
**Tags:** #time-series-forecasting #exponential-smoothing #survival-analysis #compliance #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to set par levels and replenishment that clinical units trust enough to stop keeping shadow stock, and whoever wins that trust captures the inventory savings everyone else only models.

## The Problem
Health systems copy distribution practice into the hospital: a consolidated service centre, fixed replenishment routes, par or two-bin bins in every supply room. The logic assumes steady demand and interchangeable stock. Clinical demand spikes with procedure schedules, and stock that expires or is recalled cannot simply be counted.

## What Already Exists
ERP materials management modules with par and kanban settings, point-of-use cabinets for high-value items, RFID and bin-scanning systems that trigger reorders, and case-cart picking for scheduled procedures.

## The Customization Gap
The clinical version needs: demand driven by the procedure schedule and census, not a moving average; expiry-aware replenishment that rotates short-dated stock to high-use units; lot and unique-device-identifier tracking so a recall finds every unit holding the lot; replenishment windows that avoid shift change and medication passes; and exception handling a nurse can use in seconds when the bin is empty mid-procedure.

## Target Customer
Health-system supply chain leaders standardising replenishment across hospitals, and the consultancies that design those programmes.

## Impact If Solved
Replenishment that follows clinical demand reduces both stockouts and expired write-offs, the two failures that drive clinicians to keep their own stock.
