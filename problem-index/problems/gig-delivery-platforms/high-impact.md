# The Offer Shows a Number and Not What It Is Made Of

**Industry:** [[gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** High Impact
**One-liner:** A courier decides in seconds whether to accept work, on a guaranteed amount whose composition is undisclosed, an estimated time that omits waiting, and no statement of what it will actually net after costs.
**Tags:** #gradient-boosting #time-series-forecasting #confidence-intervals #causal-inference #evaluation-metrics #probability-distributions #compliance #worker-facing

## The Problem
An offer appears: a total amount, an estimated distance and time, a merchant and a destination. The courier has seconds to accept or decline, dozens of times a shift.

What the number is made of is not shown. Base pay, distance and effort components, promotional bonuses and — under pay models that have been the subject of public controversy and regulatory action — customer tips have all featured in these calculations at various times and in various markets, in proportions the courier cannot see. A model in which a larger tip reduces the platform's contribution rather than increasing the courier's total is the specific practice that drew enforcement attention, and its legacy is a durable and rational distrust of any undisclosed composition.

The time estimate omits the part that hurts. Waiting at a merchant for an order that is not ready is routine, frequently long, and largely uncompensated; so is the drive to the pickup and the idle time between offers. A delivery advertised as twenty minutes can consume forty-five, and the difference lands entirely on the courier's realised hourly rate.

And the realised rate is what nobody computes. Net earnings after fuel, maintenance, depreciation, insurance and the self-employment tax burden are what the work actually pays, and independent estimates vary so widely precisely because outsiders cannot compute them. The platform can, per market and per hour, and does not publish it.

The consequence is that accept-or-decline decisions — the only real economic choice in the job — are made on a number that systematically overstates what the work will yield, by an amount that varies with conditions the courier cannot observe.

## Why It's Unsolved
The asymmetry is the model rather than a defect. A marketplace that clears more orders when couriers accept more of them has no straightforward interest in showing which offers are poor value, and acceptance rate is in some systems itself an input to how much work a courier is subsequently offered — which makes declining costly in a way that is not disclosed either.

Contractor classification is the legal frame that makes it possible, and it remains genuinely contested. Different jurisdictions have reached different conclusions, some through legislation, some through litigation, some through negotiated frameworks with minimum standards, and the question is not settled. Under the classification as it stands, the obligations that would attach to an employer — disclosed pay composition, compensated waiting time, dismissal protections — largely do not apply.

There are real complications too. Waiting time is genuinely hard to attribute when a courier is free to decline, multi-app, or on a break, and a naive rule would be gameable. Net cost calculation depends on the vehicle, the market and the individual's tax situation, so a platform-computed figure would be an estimate rather than a fact.

And the platforms have demonstrated the computation is feasible: markets with minimum earnings standards or pay transparency requirements have compliance systems that do exactly this. The constraint has never been capability.

## What a Solution Looks Like
Disclose the composition. Base, distance, effort, promotion and tip shown separately on every offer, with any post-delivery tip adjustment explained. This is what regulation has been converging on and it is the minimum condition for the accept-or-decline decision to be informed.

Show the expected time honestly, including the wait. The platform knows the distribution of wait times at each merchant by hour from its own historical data, and presenting an estimate that includes it — with a range rather than a point — would change which offers couriers accept and would put pressure on the merchant relationships that generate the worst waits.

Estimate the net. A realised-earnings estimate per offer and per hour, net of mileage-based vehicle costs and with the tax burden flagged, is computable and would let a courier compare this work against alternatives on a true basis. It should be presented as an estimate with its assumptions stated.

Make acceptance rate consequences explicit. If declining affects future offer volume or tier status, say so and quantify it, because a hidden penalty on declining converts a free choice into a coerced one.

And compensate the wait, or show what it costs. Several jurisdictions now require some form of engaged-time compensation, and the platforms that comply have shown it is administrable.

## Impact If Solved
This governs the earnings of millions of people who are making economic decisions on numbers constructed to look better than they are. Composition disclosure, wait-inclusive estimates and net earnings computation are all within existing platform capability — as their own compliance systems in regulated markets demonstrate — and they change the fundamental transaction from an information asymmetry into a market. The alternative is that the same changes arrive as statute, jurisdiction by jurisdiction, which is the direction of travel.
