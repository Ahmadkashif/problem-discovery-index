# History: Fleet Managers

**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Primary Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**Secondary Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**Origin Parent:** *(none)* — see below
**Episode Tier:** 1
**Transferable Pattern:** The same continuous-location instrumentation that produces an asymmetric hold over a contractor produces a materially milder version over an employee — not because the technology differs, but because employment law was already standing in the room before the sensor arrived.

> **Origin Parent — omitted.** No industry in `origins/` names fleet managers as a child in its `legacy.md`. The nearest kin in this vault is [[origins/railroads/profile|Railroads]] — PTC's continuous, mandated telemetry is the same regulatory logic `origins/railroads/legacy.md` already draws out for [[history/owner-operator-trucking|owner-operator trucking's]] ELD mandate — but that link runs through the neighbouring industry in this same batch, not through this one directly, and stretching it further would overstate the connection. Recorded as absent rather than manufactured.

## Before

A company running a fleet of service vans, delivery trucks or utility vehicles managed it on paper and by odometer: a **Driver Vehicle Inspection Report (DVIR)** filled in by hand, maintenance scheduled on a fixed mileage or calendar interval regardless of how the vehicle was actually driven, fuel purchases reconciled against receipts at the end of the month, and vehicle assignment done by a coordinator who kept the match of driver to vehicle to route in their head. A breakdown was the first hard evidence that a maintenance interval had been wrong for that particular vehicle, and by then it was a roadside repair bill rather than a scheduled one.

Large regulated trucking fleets had one precursor tool decades ahead of everyone else: **Qualcomm's OmniTRACS satellite tracking system, in commercial use from 1988**, gave long-haul carriers continuous position and two-way messaging with drivers years before consumer GPS existed. It was expensive, satellite-based, and built for national truckload carriers — never a plausible purchase for a ten-van HVAC company or a municipal public-works department, which is exactly the market this industry's modern telematics vendors went on to serve.

## The Origin Event — Two Waves, Not One

This industry's technology arrived in two separate waves, and conflating them misdates the story. The first, OmniTRACS above, was a 1980s satellite solution for an elite tier of large trucking operators. The second — the one this vault's wave assignment actually points to — is the **cellular-and-GPS telematics wave of the 2010s**, which took the same continuous-location, continuous-diagnostics idea and made it cheap enough for any fleet, of any size, in any trade. **Geotab, founded in 2000 by Neil Cawse, launched its flagship MyGeotab platform in 2012.** **Samsara, founded in 2015 by Sanjit Biswas and John Bicket — both previously founders of Meraki, sold to Cisco in 2012 — reached unicorn status by March 2018 and IPO'd on the NYSE in December 2021**, having generalised from fleet telematics into a broader "connected operations" platform for physical industries.

The mechanism is identical to Uber's in this same batch: a device that reports its own location and status continuously, cheaply, at fleet scale. What differs entirely is the customer and the employment relationship on the other end of the data.

## What Became Cheap

Continuous vehicle location, engine diagnostics and driver behaviour scoring — harsh braking, rapid acceleration, idling, speeding — for a fleet of any size, replacing the odometer-interval maintenance schedule and the DVIR clipboard with a system that knows, in real time, what condition a specific vehicle is actually in and how it is actually being driven.

## The Trade-Off

This is the same instrumentation this batch's gig and delivery files describe as an asymmetric hold, run instead on a **W-2 employee driving a company-owned vehicle** — and the brief for this batch is right that it is worth naming precisely rather than assuming it is the same story twice. A fleet manager sees exactly what a rideshare platform sees: continuous position, speed, braking, idling, route adherence. What is different is not the sensor, it is the **legal environment the sensor lands in**. An employee already has wage-and-hour law, workers' compensation, anti-discrimination protections and, in some fleets, a union — none of which a gig contractor has — so a driver-behaviour score used for coaching or discipline here is constrained by employment law in a way an independent contractor's deactivation is not. The instrumentation is the same shape Wave 8 names everywhere else in this batch. The recourse available to the person being instrumented is not, and that difference is the entire reason this file has no Prop 22 fight in it.

Commercial auto insurers have also begun pricing policies directly against telematics behaviour scores, which sharpens the trade further: the same data used to coach a driver can now also lower or raise the employer's insurance cost, giving the fleet a direct financial reason to monitor more closely that has nothing to do with the driver's own interests.

## The Binding Constraint

Regulated fleets carry a second, non-optional driver: DOT and FMCSA compliance — hours-of-service for CDL-holding employees, drug testing consortia, CDL verification, DVIR retention — with real penalties for lapses. This is the same compliance logic [[history/owner-operator-trucking|owner-operator trucking's ELD mandate]] describes, but the party bearing the administrative burden is different. An owner-operator absorbs a compliance failure personally, in lost operating authority or a fine against their own business. A fleet manager administers compliance on behalf of an employer that carries the liability, which is why this industry's own hub note names documentation burden and audit anxiety, rather than income loss, as the compliance officer's defining daily experience.

This vault's hub note sizes the industry at roughly **$30 billion** across vehicles, telematics and maintenance management in the US, and observes that no platform yet synthesises telematics, maintenance history, driver behaviour and compliance data into a single predictive system — each of Samsara, Geotab, Verizon Connect and Fleetio does one or two of those well, but a fleet coordinator still assembles the full picture themselves. That gap, not a competitive fight between vendors, is the industry's actual unresolved problem, and it is worth being clear that it is a product-completeness gap rather than a withheld capability: nobody in this market is choosing not to build the synthesis, in the way a gig platform chooses not to disclose pay composition. The data exists in enough separate systems that stitching it together has simply not yet been anyone's job to finish.

## What's Still Open

- [[problems/fleet-managers/high-impact|🔴 Predictive Maintenance Optimization]]
- [[problems/fleet-managers/worker-life-2|🟢 Compliance Officer Documentation Burden]]
- [[problems/fleet-managers/low-impact-1|🟡 Driver Behavior Monitoring and Coaching]]
- [[niches/fleet-managers/preventive-maintenance-scheduling/profile|Preventive Maintenance Scheduling]]
- [[niches/fleet-managers/dot-compliance-tracking/profile|DOT Compliance Tracking]]
- [[niches/fleet-managers/commercial-auto-underwriting/profile|Commercial Auto Underwriting]]
- [[niches/fleet-managers/mixed-fuel-ev-fleets/profile|Mixed-Fuel & EV Fleets]]

## The Transferable Pattern

> **Two industries can run the identical sensor and produce two entirely different stories, because the story is decided by who has recourse, not by what the sensor measures.** Before writing "this is surveillance," check whether the person being watched is an employee or a contractor — the technology answer is the same and the accountable-party answer is not.

An FDE who has already reasoned through [[history/gig-delivery-platforms|gig-delivery-platforms]] or [[history/rideshare-fleet-operators|rideshare-fleet-operators]] in this same batch should resist the temptation to reuse that analysis wholesale here. The mechanism transfers; the stakes and the legal remedy available to the person being measured do not, and proposing a Prop-22-shaped fix for an employed fleet driver would be solving a problem this industry does not have.

**Sources:** Wikipedia, *Geotab* (founded 2000, MyGeotab launched 2012), *Samsara* (founded 2015, unicorn March 2018, IPO December 2021); FMCSA and industry trade sources on OmniTRACS-era satellite fleet tracking (commercial deployment from 1988); `origins/railroads/legacy.md` (ELD/PTC regulatory parallel); this vault's `industries/fleet-managers.md`.
