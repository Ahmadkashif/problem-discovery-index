# ATM Replenishment Forecasting That Ignores the Truck

**Industry:** [[armored-car-services|Armored Car Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** ATM cash forecasting is a sold product category, but the forecast is made for each machine in isolation and then handed to a carrier whose trucks, vault cut-offs and value limits decide what can actually be delivered.
**Tags:** #time-series-forecasting #gradient-boosting #temporal-fusion-transformers #optimization-fundamentals #dynamic-programming #data-integration #automation

## The Problem
An ATM owner pays twice for getting cash wrong. A machine that runs out loses withdrawals and fees, draws complaints and, for a bank, a visible service failure. A machine loaded too heavily ties up the owner's money, insures more cash than necessary and invites attack. Vendors have cited a Deloitte study saying institutions hold up to 40% more cash than they need. The forecast that sets the load is made per machine from its withdrawal history, paydays, holidays and local events.

The forecast then meets the truck. A carrier replenishes on scheduled route days, with cut-offs for orders at its vault, cassette configurations it must fill by denomination, and a limit on how much value one truck may carry on a route. An unscheduled visit to rescue a machine about to run dry costs an emergency fee (~$100–300, estimate) and breaks another route. A forecast that says "load ~$60,000 on Thursday" (illustrative) is useless if the truck serving that machine runs Tuesday and Friday and is already at its value limit on Friday.

## What Already Exists
Cash forecasting and optimisation software for banks and ATM fleets: Morphis's forecasting product, OptiCash (marketed by Printec, which claims up to 30% lower cash holdings and up to 90% fewer cash-outs), forecasting modules from ATM makers such as Hyosung, and the forecasting desks inside carriers' ATM managed services (Brink's lists cash forecasting and optimisation among its AMS services). Generic demand-forecasting platforms are also used by large banks' data teams.

## The Customisation Gap
The generic tools forecast demand; they do not plan a delivery. The ATM-and-carrier-specific logic is: replenishment allowed only on the carrier's route days for that site, with order cut-offs at its vault; cassette capacity and denomination mix (a machine can run out of $20s while full of $10s); the per-truck and per-route value limits set by the carrier's insurers; the cost of an unscheduled visit versus the cost of a cash-out, which differ by contract; deposit-taking machines whose cash should be recycled to dispensers rather than returned; and the owner's cost of funds, which turned idle cash from a rounding error into a line item when interest rates rose. The forecast needs to become a joint order-and-route plan, and the owner needs to see the trade-off it made.

## Impact If Solved
A replenishment plan that respects the truck would cut emergency visits and idle cash together — on a fleet of a few thousand machines, idle cash can run to hundreds of millions of dollars (estimate) — and would let an ATM owner hold its carrier to a measurable cash-out rate instead of arguing about each incident.
