# A Booking Layer Over an Incompatible Estate

**Niche:** [[niches/freight-tech-platforms/dock-scheduling-facility-ops/profile|Dock Scheduling & Facility Operations]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every large facility bought dock scheduling software and configured it its own way, so the carrier serving forty of them employs a person to book appointments across forty portals — and no vendor benefits from fixing that.
**Tags:** #data-integration #workflow-orchestration #large-language-models #evaluation-metrics #confidence-intervals #automation #graph-theory #worker-facing
**Contested on:** Every serious competitor in dock scheduling is fighting to let a carrier book an appointment at any facility without learning that facility's system — and whoever makes booking work across an incompatible estate takes the network.

## The Problem
A carrier's appointment clerk starts the day with thirty loads needing appointments. Eleven facilities use one portal, six another, four require email to a named person, three require a phone call during specific hours, and the rest use systems the clerk has bookmarked and remembers the quirks of. Each booking takes five to fifteen minutes. Appointments that cannot be obtained at a workable time push the load, which pushes the driver's week. This is a full-time role at any carrier of scale and it produces no value for anybody.

## Why Nobody Has Built This
Interoperability requires the incumbent scheduling vendors to expose their facilities' availability to a layer they do not control, which reduces them to a back end. None of them will do that voluntarily, and the facilities — who are their customers — have no strong incentive to demand it, because the cost of the fragmentation falls on carriers rather than on facilities. That asymmetry is the whole reason the problem persists: the party paying for the software is not the party paying for the incompatibility. Any solution must therefore work without the incumbents' cooperation at first and offer facilities something they actually want.

## What to Build
A federated booking layer that works through whatever interface a facility has. Where an API exists, use it. Where a portal exists, automate it. Where it is email, generate and parse the email. Where it is a phone call, queue it for a human with everything prepared. A carrier books once, in one place, for every facility. The directory itself — which facility uses what, what their rules are, what their actual dwell looks like — is the asset and accumulates with use. Facilities are brought on with the thing they want and cannot get: appointments tied to predicted truck arrival, so their grid reflects reality, and a no-show rate that falls because the carrier books against a schedule it can actually meet. Standardisation should be pursued in parallel, because the automation layer is a bridge rather than a destination, but waiting for a standard is waiting indefinitely.

## Target Customer
Carriers and brokerages bearing the booking cost, large shippers whose freight is delayed by appointment friction, and the facilities themselves once the value to them is demonstrated.

## Impact If Built
A carrier appointment clerk's day is pure friction cost and disappears. For facilities, appointments that correspond to when trucks will actually arrive reduce both no-shows and detention, which are their two largest appointment-related costs. The directory of facility behaviour built along the way is information the industry has never had in one place.
