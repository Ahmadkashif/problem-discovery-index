# Fix: Nobody Prices the Idle Day

**Niche:** [[niches/rideshare-fleet-operators/utilisation-and-turnover/profile|Fleet Utilisation & Turnover]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Fix (Pain Point)
**One-liner:** An operator can say what a vehicle rents for and not what a day of it sitting costs, so every decision about holding, repairing or waiting is made without the one number that should govern it.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #feature-engineering #workflow-orchestration #revenue-impact #quick-win #automation
**Contested on:** Whether the operator will compute the daily carrying cost of a vehicle and put it in front of the people making decisions about it.

## The Problem

A vehicle sits. Waiting for a renter, for a part, for a document, for an inspection, for someone to have time. Each wait is a decision made by someone in the office weighing an unclear trade-off: hold this car for the driver who says they will come Thursday, or give it to the person on the list today; do the brake job now or when the vehicle is back in; chase the registration renewal this afternoon or tomorrow.

Every one of those decisions has a correct answer that depends on the daily carrying cost — finance payment, insurance, depreciation, registration, parking, amortised maintenance — and almost no operator has computed it. A $38,000 vehicle financed over four years with commercial insurance typically carries somewhere between $40 and $70 a day before it earns anything, and the person deciding whether to wait until Thursday has never seen that number.

## Why It's Still Broken

Carrying cost is spread across accounts that are never joined per vehicle: the finance schedule is in one place, the insurance premium is a fleet-level policy, depreciation is an annual accounting entry, and parking is a facility cost. Computing a per-vehicle daily figure requires allocating four things nobody allocates.

It is also nobody's job. The owner thinks about the rate and the default rate. The fleet manager thinks about today's problems. The accountant closes the books annually. The daily cost of an idle asset falls between them.

And the number is uncomfortable once computed, because it converts a familiar operational annoyance into a visible loss with a dollar figure attached, which raises the question of why the process that produces it has not been fixed.

## What a Fix Looks Like

Compute the number and put it everywhere.

Allocate carrying cost per vehicle per day: finance or lease payment, insurance premium allocated per vehicle, depreciation on a realistic commercial-use schedule rather than a consumer one, registration and compliance fees, parking or facility cost, and amortised scheduled maintenance. This is an afternoon of accounting per fleet and it produces a figure between roughly $40 and $70 for a typical vehicle.

Put it on the screen. Every idle vehicle in the fleet view shows days idle and cumulative cost since it stopped earning. A vehicle that has been waiting eleven days for a $180 part is displaying $600 of loss next to the part order, and that display changes the decision about expedited shipping without anyone needing to be told.

Attribute idle days by cause and total them monthly. Awaiting renter, awaiting maintenance, awaiting parts, awaiting documents, awaiting recovery, held for a specific driver. The monthly total by category tells the operator where their utilisation is going, and it is almost always a surprise — the dominant category is rarely the one they would have guessed.

Use it in the decisions it should govern. Holding a vehicle three days for a preferred renter costs a known amount and is sometimes worth it. Expediting a part is usually cheaper than the idle days it saves and is usually not done. Deferring maintenance to keep a vehicle earning is sometimes right and is currently decided by instinct.

And use it to size the turnaround target. If a turnover takes six days and the carrying cost is $55, each turnover costs $330 in idle time; halving it across a fleet of two hundred vehicles with two turnovers a year is six figures. That arithmetic is what justifies fixing the process.

## Who Feels the Pain

Operators, who lose several percent of revenue annually to a cost they have never quantified. Fleet managers, who make trade-off decisions daily with no basis for them and get second-guessed either way. Drivers on the waiting list, who wait for vehicles that are sitting in the lot for reasons nobody is urgently resolving. And lenders, who are financing assets whose idle time is unmeasured.

## Impact If Fixed

Every holding, repair and scheduling decision gets made against the number that should govern it, by the people making them, without any new process. The dominant cause of idle days becomes visible and therefore fixable. And the operator finds out what their utilisation gap is actually worth — which is usually more than the pricing changes they spend their time on.
