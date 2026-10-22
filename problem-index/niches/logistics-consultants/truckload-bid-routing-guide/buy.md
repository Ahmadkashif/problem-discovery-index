# Tender and Visibility Data Adapted to Bid Design

**Niche:** [[niches/logistics-consultants/truckload-bid-routing-guide/profile|Truckload Bid Design & Routing Guide Performance]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** TMS tender logs and visibility platforms already record what each carrier accepted and ran; they report execution, and nobody turns them into a carrier behaviour profile for the next bid.
**Tags:** #feature-engineering #logistic-regression #k-nearest-neighbors #data-integration #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to design truckload awards that carriers keep accepting when the spot market turns, and whoever's routing guides hold the highest primary tender acceptance through the contract year takes the account.

## The Problem
Bid design treats every carrier's bid as equally reliable. The shipper's own history says otherwise: some carriers accept nearly everything on lanes near their terminals and reject in tight markets elsewhere; some brokers bid low and cover only when convenient.

## What Already Exists
TMS platforms log every tender, acceptance, rejection and reason; visibility platforms such as project44 and FourKites record pickups, deliveries and on-time performance by carrier and lane.

## The Customization Gap
For bid design, the data needs: joining tender logs to visibility events so acceptance and on-time delivery sit in one carrier-lane record; normalising for market conditions so a carrier's rejection rate is read against the contract-to-spot spread at the time; geographic generalisation so behaviour on similar lanes informs lanes with little history; and an export into the award model as a reliability-adjusted cost per carrier per lane.

## Target Customer
Consultants and shipper procurement teams who run annual truckload bids from a TMS with a visibility integration.

## Impact If Solved
Awards weighted by evidence of what carriers do, not only what they bid.
