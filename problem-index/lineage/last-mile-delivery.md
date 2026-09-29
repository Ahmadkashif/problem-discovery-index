# Lineage: Last-Mile Delivery

**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** ORION — UPS's On-Road Integrated Optimization and Navigation, which each morning gives a driver an optimised sequence for the stops already assigned to the route; fully deployed to about 55,000 US drivers in 2016
**Builder:** UPS
**Builder in vault:** [[origins/package-carriers/profile|Package Carriers]]
**Verification:** partial — see Sources

## The Problem That Came First

A delivery route is a list of addresses nobody chose the order of.

By the time a parcel reaches the driver, the hard network decisions — which hub, which truck, which route — are made. What remains is the last one: in what sequence to visit a hundred and more stops before the day ends, with some customers needing a morning slot and some pickups fixed at the end. The number of possible orders explodes with every stop, so a driver runs it from memory and habit.

And at a carrier's scale, habit is expensive. A few surplus miles per driver per day, multiplied across tens of thousands of drivers and every working day of the year, is a line on the income statement.

## What Got Built

A system that sequences one driver's day.

INFORMS' description of the project is plain: "every morning ORION provides UPS drivers with an optimized sequence in which the (pre)assigned packages are delivered." It does not decide which packages go on which truck. It takes the day's assignment as given and answers only *in what order*, subject to the route's service commitments.

It could not exist on its own. ORION sits on **Package Flow Technology**, a data foundation UPS launched in 2003 so that every package's destination and commitments were known before the truck was loaded. PFT was built explicitly to allow optimisation in pickup and delivery. By December 2015 more than 35,000 of UPS's 55,000 US drivers were using ORION, averaging about 160 customers a day each; full deployment came in 2016. The project won the 2016 Franz Edelman Award.

## Who Built It, And Why Them

UPS's own Operations Research group — and only a carrier of that size could justify it.

The first optimisation algorithms worked in the lab and failed on the road. INFORMS records that UPS "went back to the drawing board and had to rethink and relearn everything it had known about creating effective and efficient routes", blending "its 108-year-old practices with 21st century technology." It then field-tested ORION with a growing number of drivers for about three years before committing to full rollout.

**Why UPS:** the arithmetic. Full deployment was estimated at $250 million; by December 2015 ORION had already saved more than $320 million, with $300–400 million a year expected at full scale, and around 10 million gallons of fuel a year. A $250 million, decade-long research programme pays back only when the saving is multiplied across 55,000 routes. No delivery company a hundredth of the size could have funded the same work — which is why, for everyone smaller, route optimisation arrived later as software sold by someone else.

## What It Cost

The driver's knowledge of the route became an input rather than the plan. ORION needed years of field testing because a sequence that is optimal on paper can be wrong at a loading dock the driver knows is locked until ten; the system had to learn to accommodate the route's informal constraints, and the driver lost some of the discretion that used to be the job.

It also fixed the problem's scope. ORION sequences a day already assigned in the morning. A re-plan in the middle of the day — the failed attempt, the new pickup, the closed road — is a harder, separate problem.

## What You Still Touch

The delivery that arrives in a sequence that seems arbitrary from your doorstep is a solver's answer to a question UPS spent over a decade learning to ask. Every smaller operator's route-planning app sells a scaled-down version of it.

- [[problems/last-mile-delivery/low-impact-1|🟡 Dynamic Route Reoptimization During Delivery]] — the mid-day re-plan ORION's morning sequence leaves open
- [[problems/last-mile-delivery/high-impact|🔴 Delivery Success Prediction and Failed Attempt Prevention]]
- [[problems/last-mile-delivery/worker-life-1|🟢 Address Intelligence and Access Note Capture for Drivers]] — the driver's local knowledge, which the solver still needs
- [[niches/last-mile-delivery/route-optimization-vendors/profile|Route Optimization Vendors]]
- [[niches/last-mile-delivery/ecommerce-parcel-dsps/profile|E-Commerce Parcel DSPs]]

**Sources:** INFORMS, *UPS On-Road Integrated Optimization and Navigation (ORION) Project*, read via the Internet Archive snapshot of 12 May 2021 (live page, UPS's own ORION story page and the INFORMS Edelman winners list all returned 403 to direct fetch) — morning-sequence description, PFT launched 2003, 35,000 of 55,000 drivers as of December 2015, full deployment 2016, ~160 customers per day, ~3 years of field testing, $250 million cost, $320 million saved by December 2015, $300–400 million expected annually, 10 million gallons of fuel, 2016 Edelman Award, both quotations. This vault's `origins/package-carriers/the-fight.md` and `history/last-mile-delivery.md` (vault material, not independent corroboration) date the research programme from 2003. WebSearch was unavailable this session (session cap reached). ⚠️ **Not established:** the names of the individual UPS project leads — commonly given in press accounts, not in the source read, so not asserted; the Interfaces journal article (INFORMS PubsOnline) returned 403. The "no left turns" heuristic is deliberately omitted: per the vault's origins note it predates ORION and is not its core.
