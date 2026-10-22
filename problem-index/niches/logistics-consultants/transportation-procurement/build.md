# Mode-Shift Analysis Across the Whole Freight Book

**Niche:** [[niches/logistics-consultants/transportation-procurement/profile|Transportation Procurement & Bid Management]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Shippers bid parcel, LTL and truckload separately, so nobody decides which shipments belong in which mode, and the cheapest bid in the wrong mode still overpays.
**Tags:** #gradient-boosting #optimization-fundamentals #k-means-clustering #feature-engineering #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to lower a shipper's contracted freight cost, but truckload is won by designing awards carriers keep honouring when the market turns, and parcel and LTL by knowing what comparable shippers have been conceded. Decomposed into contested sub-niches below.

## The Problem
The parcel agreement is negotiated by one team in the autumn, the LTL bid runs in winter, and the truckload bid runs when contracts expire. Each optimises its own mode. But the freight is not fixed by mode: heavy multi-carton parcel shipments may be cheaper as LTL, a run of LTL shipments to one region may consolidate into a weekly truckload or pool distribution, and volume LTL quotes undercut both on some lanes. Mode is set by shipping-desk habit and order-size thresholds nobody has revisited.

## Why Nobody Has Built This
Each sourcing tool and benchmark is built per mode, and each sub-contest has its own specialists, so the cross-mode question falls between engagements. Answering it needs order-level data, carton counts and delivery requirements that sit in the ERP and WMS rather than in any freight system.

## What to Build
A model that takes order and shipment history, rates every shipment in every feasible mode under the shipper's current and proposed contracts, adds consolidation and pooling options by region and day, respects delivery-window and customer requirements, and returns mode rules — weight and carton thresholds, consolidation days by lane — with the cost of each rule. Run before the bids, it sets what each mode's bid should contain.

## Target Customer
Directors of transportation at shippers with mixed parcel, LTL and truckload spend, and the consultants who run their bids.

## Impact If Built
Mode assignment re-sized before procurement can reduce total freight cost by ~3–8% on mixed books (estimate), savings no single-mode bid can reach.
