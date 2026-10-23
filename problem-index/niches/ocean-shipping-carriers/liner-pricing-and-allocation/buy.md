# Airline Revenue Management Adapted to Liner Slots

**Niche:** [[niches/ocean-shipping-carriers/liner-pricing-and-allocation/profile|Container Liner Pricing & Allocation]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines and air cargo carriers have run overbooking and bid-price revenue management for decades; liner shipping's version of the problem has different units, contracts and cancellation behaviour.
**Tags:** #gradient-boosting #survival-analysis #optimization-fundamentals #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to fill each sailing with the highest-paying cargo that actually turns up, and whoever earns the highest net revenue per available slot across a season of sailings takes the account.

## The Problem
Liner desks face the airline problem — fixed perishable capacity, cancellations and no-shows, a mix of contract and spot demand — without the tools airlines built for it. Overbooking and acceptance decisions are made per desk on judgement.

## What Already Exists
Passenger and air-cargo revenue-management suites (PROS, Accelya, Sabre and airline in-house systems) forecast demand and no-shows, set overbooking levels and compute bid prices for accepting a booking.

## The Customization Gap
Liner cargo is booked in TEU and FEU with weight, reefer plugs, dangerous-goods and out-of-gauge limits, so capacity is multi-dimensional rather than one seat count. Most volume is under annual contracts with minimum quantity commitments that shippers rarely meet in full, and index-linked contracts tie price to Drewry, Xeneta or SCFI benchmarks. Empty-container repositioning makes the value of a slot depend on the backhaul. Rolled cargo damages relationships far more than an air cargo offload. The model has to learn no-show behaviour by customer and forwarder, and encode protected accounts.

## Target Customer
Revenue-management and pricing teams at container lines that want proven RM mathematics rather than a bespoke build.

## Impact If Solved
A tested overbooking and acceptance engine in months rather than a multi-year in-house programme. A 1–2% revenue lift (estimate) would be ~$100–200M a year on a carrier with ~$10B of freight revenue (estimate), with slot value that accounts for weight, equipment and backhaul.
