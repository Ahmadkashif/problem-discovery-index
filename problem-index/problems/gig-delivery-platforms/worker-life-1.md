# The Courier Waiting Unpaid

**Industry:** [[gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Worker Life Changing
**One-liner:** Twenty minutes in a restaurant lobby for an order that was promised ten minutes ago, unpaid, with the clock running on an hourly rate that already assumed the order would be ready.
**Tags:** #time-series-forecasting #gradient-boosting #confidence-intervals #markov-decision-processes #evaluation-metrics #worker-facing #optimization-fundamentals #revenue-impact

## The Problem
Waiting is the defining unpaid activity of delivery work. A courier arrives at a merchant at the time the platform directed, the order is not ready, and they wait — sometimes five minutes, sometimes half an hour. They cannot leave without forfeiting the delivery and taking a completion-rate penalty; they cannot accept other work while holding this one; and they are not paid for the time.

The pattern is predictable and the platform has the data. Particular merchants are reliably late at particular hours. Dispatching a courier to arrive at the promised ready time rather than the realistic one systematically converts merchant delay into courier unpaid time, and it happens because the customer promise and the merchant relationship are the optimisation targets.

Other unpaid time accumulates alongside: the drive to the pickup, the wait between offers, the time spent parking and finding an apartment, the return trip from a delivery in an area with no onward demand.

The result is the gap between the advertised per-delivery rate and the realised hourly rate — a gap that the courier can feel and cannot quantify, since computing it requires tracking every minute and every mile against every payment, which almost nobody does.

## Why It Matters to the Worker
This is working time that is not compensated, and it is a large enough share to change what the job pays. Couriers with families, second jobs or medical needs are planning around an hourly rate that does not hold, and the variance is as damaging as the level — a shift that yields well one day and poorly the next makes household budgeting impossible.

The powerlessness of waiting is its own cost. Standing in a lobby with no information about how long, no ability to earn, no one to ask, and a completion metric that punishes leaving, is a position with no available action. Couriers describe it as the worst part of the job, ahead of traffic, weather or difficult customers.

The vehicle costs run underneath all of it. Fuel, maintenance, tyres, insurance and depreciation are real and are paid by the courier out of a gross figure that is presented as earnings, and the depreciation in particular is invisible until the vehicle needs replacing.

And there is nobody to raise it with. Support is a chat interface for order issues, and there is no mechanism through which a systematic pattern — this merchant is always late — becomes anyone's problem.

## What a Solution Looks Like
Predict the wait and dispatch against it. The platform can estimate merchant readiness by location and hour from its own arrival-to-pickup history, and timing the dispatch to the realistic ready time rather than the promise removes a large share of unpaid waiting without changing anything the customer sees.

Show the expected wait on the offer. A courier deciding whether to accept should see the wait estimate with its range, because an offer that pays well and involves twenty-five minutes of waiting is not the offer it appears to be.

Compensate engaged waiting, or make the cost visible. Several jurisdictions now require some form of engaged-time compensation and the platforms operating there have shown it is administrable. Where it is not required, showing cumulative unpaid waiting in the earnings summary at least makes it a known quantity rather than an ambient one.

Compute the realised rate. Net earnings per engaged hour after mileage-based vehicle costs, reported honestly with the assumptions stated, gives a courier the number the job actually pays — which is what they need to decide whether to keep doing it.

And route the pattern back. A merchant with systematically poor readiness should be visible to merchant operations as a courier-cost problem, not only as a customer-promise problem.

## Impact If Solved
Unpaid waiting is a direct, large and predictable subtraction from the earnings of millions of people, produced by a dispatch decision the platform makes with full knowledge of the expected delay. Wait-aware dispatch removes much of it at no cost to anyone but the merchant's schedule, offer-level disclosure makes the accept decision honest, and a realised hourly figure gives couriers the basis for every decision they make about this work.
