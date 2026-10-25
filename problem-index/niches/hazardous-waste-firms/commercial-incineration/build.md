# A Committed-Tons Ledger With Deferral Forecasts

**Niche:** [[niches/hazardous-waste-firms/commercial-incineration/profile|Commercial Hazardous Waste Incineration]]
**Industry:** [[industries/hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An incinerator network knows its practical capacity to the ton and does not know, at any moment, how many tons it has promised or which promises it is about to break.
**Tags:** #time-series-forecasting #survival-analysis #gradient-boosting #optimization-fundamentals #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to guarantee generators a burn slot for the streams only a hazardous waste incinerator can take, and whoever honours the most committed tons through a capacity crunch takes the account.

## The Problem
Practical capacity is a planning number; real capacity moves with outages, feed-limit constraints and the mix of waste on site. Promises are made monthly or per project. When the two diverge, the plant defers loads, and the generator learns only when its pickup is cancelled and its own storage clock keeps running.

## Why Nobody Has Built This
Operators treat capacity as an operations matter and commitments as a sales matter. Outage and feed history sit in plant historians that commercial systems never read, and the number of operators is small enough that each built its own partial tools.

## What to Build
A ledger joining contracts, approved profiles and scheduled pickups to each unit's capacity forecast, built from outage history, maintenance plans and the burn rate of the waste mix in storage. It forecasts the probability that each commitment is deferred in the next 30–90 days, proposes re-routing to sister units or alternative outlets, and gives sales a live "can we take this" answer before a new promise.

## Target Customer
National accounts directors and network planners at Clean Harbors, Veolia and independent incinerator operators.

## Impact If Built
Cutting deferred tons by half on a network deferring ~3% of ~550,000 burned tons (estimate) keeps ~8,000 tons a year on schedule, ~$6–8M of revenue at ~$800 a ton (estimate), and keeps the generators whose loads are the hardest to place elsewhere.
