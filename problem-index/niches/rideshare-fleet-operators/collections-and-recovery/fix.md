# Fix: The Escalation Runs on a Calendar, Not on Evidence

**Niche:** [[niches/rideshare-fleet-operators/collections-and-recovery/profile|Collections & Vehicle Recovery]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Day three a call, day seven a warning, day ten disablement, day fourteen recovery — applied identically to a driver who is ill and a driver who has disappeared.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #compliance #quick-win #revenue-impact
**Contested on:** Whether the operator will let the evidence they already have change the next step.

## The Problem

Arrears handling is a fixed ladder measured in days. It is applied to a driver with two years of perfect payments who missed one week, and to a driver three months in whose vehicle has not moved since the payment failed, in exactly the same way.

The two cases are not remotely alike and the operator can tell them apart in thirty seconds. The telematics shows whether the vehicle is moving and how much. The payment record shows whether this has happened before. The tenure is known. A driver working full hours who missed a payment has a cash-flow timing problem and will almost certainly cure. A vehicle that has not moved in four days is a different situation entirely and the ladder is too slow for it.

So the ladder is simultaneously too aggressive for the first case and too slow for the second, and the operator loses money at both ends.

## Why It's Still Broken

A fixed sequence is defensible, consistent and requires no judgement, which matters when collections is done by whoever has time. Introducing differentiation raises the question of who decides and on what basis, and without evidence that question has no good answer.

The evidence has never been produced. Nobody has tabulated arrears episodes against outcomes, so nobody knows that, say, drivers past twelve months' tenure cure at four times the rate of drivers under three months — a fact that would change every decision and that the fleet's own records contain.

And the ladder's failures are asymmetric in visibility. Recovering a vehicle from someone who would have paid looks like a closed case. Forbearing on someone who then disappears looks like a mistake with a name on it. The incentive on the person making the call runs toward escalation.

## What a Fix Looks Like

Segment the ladder on two facts the operator already has, and then measure.

**Is the vehicle moving?** Pull it from telematics on day one. A vehicle in normal use means the driver is working and the arrears is about cash flow — slow the ladder, offer a payment plan, keep them earning. A vehicle stationary for several days means something else has happened — accelerate, make contact urgently, and find out whether it is illness, an accident, a second job or an abandonment. The current ladder inverts the urgency in both cases.

**What is the payment history?** Tenure and prior arrears episodes. A first miss after long reliable payment is the strongest predictor of cure available and should visibly change the treatment — and telling the driver that their record is why they are being given room is worth more than the room itself.

**Then tabulate the outcomes.** Twelve months of arrears episodes, what was done, what was recovered. Cure rate by tenure band, by whether the vehicle kept moving, by intervention. This is a spreadsheet exercise on existing records and it will make the segmentation obvious, quantitatively, to anyone who doubts it.

**Prepare the responses.** Payment plans with defined terms, a short rate reduction, a vehicle swap to a cheaper class — written down, with eligibility, so they can be offered on the call instead of requiring the owner's approval and a day's delay.

**Set a disablement policy deliberately.** When it may be used, after what notice, never on a vehicle in motion, never where it would strand someone, and with the legal constraints of each operating state documented. Most operators have a capability and no policy, which is the worst configuration available.

## Who Feels the Pain

Drivers who lose a vehicle and their income over a timing problem that would have resolved, and drivers in genuine crisis who get a routine call on day three when something serious has happened. Collections staff, who apply a sequence they can see is wrong in both directions and have no authority to vary. And operators, who write off recoverable balances and recover vehicles into idle days.

## Impact If Fixed

The two obvious signals the operator already has start determining the response, which separates the cases that cure from the cases that do not at the point where it matters. Recoveries fall on the cases that would have paid and accelerate on the cases that will not. And the fleet's own arrears history becomes evidence rather than an unexamined pile of closed tickets.
