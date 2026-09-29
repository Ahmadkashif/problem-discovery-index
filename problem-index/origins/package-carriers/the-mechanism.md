# The Mechanism: What ORION Actually Optimises

**Origin:** [[origins/package-carriers/profile|Package Carriers]]
**Tags:** #combinatorics-and-counting #dynamic-programming #optimization-fundamentals #graph-theory #time-series-forecasting #automation #data-integration #workflow-orchestration

> A myth sits directly on top of this mechanism, and it has to be cleared before the mechanism can be explained honestly. Read the correction first.

## The Myth: "UPS Trucks Never Turn Left"

This story is not fabricated — NPR reported it accurately in **2007** — but it is **routinely misattributed to ORION**, which did not exist yet in any deployed form in 2007. What NPR described was a simpler, earlier heuristic: minimise left turns because they mean idling across oncoming traffic, burning fuel and risking a disproportionate share of intersection accidents. UPS reported saving over 4.5 million miles across 21 California facilities using this rule alone, and *Mythbusters* later confirmed the fuel saving independently (while noting it can add time).

**Left-turn avoidance is one input into a much larger optimisation, not the mechanism itself.** Treating it as the whole story — which most retellings of "why UPS trucks don't turn left" do — is exactly the kind of telegenic soundbite standing in for the real system that this vault exists to correct.

## What ORION Actually Computes

ORION is a **route sequencing and dynamic reoptimisation system**, not a turn-avoidance rule. Given a driver's set of stops for the day — each with an address, a delivery or pickup window, and a service-time estimate — it solves a large **vehicle-routing-style problem**: find the sequence of stops that minimises distance and time, subject to time-window constraints, using more than 250 million address data points and roughly 1,000 pages of underlying optimisation code. Unlike a one-time manifest printed each morning, ORION **re-solves as the day happens** — a new pickup request, a closed road, a driver running behind schedule all change the remaining optimal sequence, and the system recomputes rather than leaving the driver to reconcile a stale plan against reality by feel.

This is structurally the same class of problem this vault's airlines mechanism file describes for seat inventory — a constrained optimisation re-solved continuously against live data — applied to physical geography instead of fare buckets.

## Development Took a Decade, Not a Launch

R&D began in **2003**. Lab testing ran 2003–2009; telematics pilots began 2008; the system was prototyped at eight sites 2010–11 and reached beta at six sites in 2012. **Full-scale rollout began in October 2013** and was substantially complete across roughly 55,000 US routes by **2016–17**. Ten years from first research to national deployment is the honest timeline, and it is the same lesson this vault's airlines origin draws from SABRE-to-DINAMO: **the gap between building the infrastructure and deploying the optimisation on top of it is measured in years, sometimes decades, not quarters.**

## The Savings Figure — Read the Fine Print

**The widely repeated claim — "ORION saves $300–400 million and 100 million miles a year" — is a projected full-deployment figure, and it is routinely quoted as an achieved, current result.** As of December 2015, with the rollout still partial, cumulative savings were reported at **over $320 million** — a real number, but a cumulative one at partial deployment, not an annual run-rate. The $300–400M/year, 100M-mile, 10M-gallon, ~100,000-metric-ton-CO2 figures are what full deployment was projected to produce. The measured, driver-level effect once a route came online was more modest and more concrete: **an average of six to eight fewer miles driven per day per route** — a 2018 "dynamic ORION" update reportedly added a further two to four miles.

**The distinction matters for anyone citing this case: cumulative-to-date, projected-annual, and per-driver-daily are three different numbers, and conflating them is the single most common error in ORION retellings.**

## The Transferable Pattern

> **A route is not a distance-minimisation problem alone — it is a constraint-satisfaction problem wearing a distance-minimisation problem's clothes.** Time windows, driver hours, and real-time disruption dominate the solution as much as raw mileage does, and a system that only minimises miles without modelling the constraints will produce a route nobody can actually drive.

**Sources:** INFORMS, *UPS On-Road Integrated Optimization and Navigation (ORION) Project* and *Edelman Award: 'ORION' delivers success for UPS*; NPR, *UPS Takes Left Turns Out of Deliveries* (24 Jan 2007); The Conversation, *Why UPS drivers don't turn left*; GlobeNewswire, UPS 2016 Edelman Award release.
