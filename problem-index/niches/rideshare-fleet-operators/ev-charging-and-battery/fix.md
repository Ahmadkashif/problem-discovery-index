# Fix: Charging Time Is the Driver's, Charging Cost Is Whoever's

**Niche:** [[niches/rideshare-fleet-operators/ev-charging-and-battery/profile|EV Transition, Charging & Battery]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Forty minutes at a fast charger is unpaid time the rental rate never accounted for, and whether the electricity is the driver's cost or the operator's is frequently unclear until the first bill.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #worker-facing #quick-win #revenue-impact
**Contested on:** Whether the two new costs electrification introduces get allocated deliberately rather than by default.

## The Problem

Electrification moved a fleet's fuel cost from the driver's pump receipts to somewhere ambiguous, and introduced a time cost that did not previously exist.

The time is the sharper problem. A rideshare driver refuelling a petrol car loses five minutes. Charging on a public DC fast charger loses thirty to fifty, once or twice a shift, unpaid. For a full-time driver that is several hours a week of working time that the rental rate — set by analogy to petrol vehicles — never contemplated. Slow charging at home is cheap and slow; drivers without home charging, who are disproportionately the renting population, have no such option.

The cost is the murkier one. Some operators include charging, some exclude it, some provide a network card with a cap, some include home charging and not public. Drivers frequently do not understand which applies until a bill or a cap arrives, and operators frequently have not modelled what their inclusive offer actually costs at rideshare mileage.

## Why It's Still Broken

Electrification happened faster than the contracts adapted. Rental terms were written for petrol vehicles and amended minimally, so charging falls into a clause that was not designed for it.

The operator's own economics are unmodelled too. An inclusive charging offer at 60,000 miles a year with a heavy public fast-charging mix is a large and variable cost that most operators have not projected, which is why some have offered it and then withdrawn it — which is worse for everyone than not having offered it.

And the time cost is invisible because it falls on the driver, exactly as merchant wait time does in delivery. Nobody who sets the rate experiences it.

## What a Fix Looks Like

Allocate both costs deliberately and state them.

**Write the charging terms plainly.** What is included, at which networks, up to what limit, and what happens beyond it. A driver should know before signing whether a public fast-charge session is their cost or the operator's. This is a paragraph and it prevents most of the disputes.

**Model the inclusive cost before offering it.** From telematics: energy consumed per mile at this duty cycle, the public-versus-home split for drivers without home charging, and network pricing. That gives a per-mile charging cost to price into the rate. Operators offering inclusive charging without this projection are writing an uncapped variable exposure.

**Reflect charging time in the rate.** If a driver loses four hours a week to charging, the effective rate per productive hour is meaningfully higher than the headline implies, and an operator competing for drivers can either acknowledge that in the price or lose to one that does. At minimum, the rate should not be set by direct analogy to a petrol vehicle.

**Provision charging access properly.** A network account with the operator's negotiated rate, rather than the driver paying retail at whatever charger they find, is a large saving that only the operator can capture. Where depot or partner charging exists, it should be available with predictable access — a charger the driver can rely on being free is worth more than a marginally cheaper one that is occupied.

**Report charging behaviour back to the driver.** Cost per mile, where they charge, what it would be at cheaper alternatives nearby, and a note on the habits that degrade the battery. Drivers new to EVs frequently do not know that charging to 100% on DC fast repeatedly is expensive for everyone, and telling them is free.

**Track the cost per vehicle.** Energy per mile varies by vehicle, driver and season, and it is the second-largest variable cost in an EV fleet. Most operators cannot state it.

## Who Feels the Pain

Drivers, who lose several unpaid hours a week to charging and who may discover the cost allocation through a bill — disproportionately those without home charging, who are the same population most likely to be renting. Operators who offered inclusive charging without modelling it. And both parties in the disputes that follow terms nobody wrote clearly.

## Impact If Fixed

The two costs electrification introduced get allocated on purpose and stated in advance, which removes the most common new dispute in this business. The operator learns what charging actually costs at rideshare duty, which is necessary before it can be priced. And the driver's unpaid charging time enters the conversation about the rate instead of being absorbed silently.
