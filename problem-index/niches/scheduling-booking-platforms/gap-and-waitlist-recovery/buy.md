# Inventory Recovery From Travel and Events

**Niche:** [[niches/scheduling-booking-platforms/gap-and-waitlist-recovery/profile|Gap & Waitlist Recovery]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines, hotels and ticketing have spent decades on perishable inventory — standby lists, last-minute pricing, upgrade allocation — and an empty appointment slot is the same object.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #dynamic-programming #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to refill a slot in the hours after it is released, to the right customer, without spamming everyone — and whoever does that takes the operator, because the recovered slot is pure margin on capacity already paid for.

## The Problem
An appointment slot is perishable inventory with a fixed expiry, zero marginal cost, and a known population of potential buyers. Revenue management has studied exactly this for decades: when to discount, whom to offer to, how to run a standby list, how to value a unit as expiry approaches. Every technique is published and several are commercial products. Scheduling platforms leave the slot empty.

## What Already Exists
Revenue management and dynamic pricing literature; standby and upgrade allocation mechanisms; last-minute inventory marketplaces; propensity-to-accept modelling from marketing; sequential offer mechanisms with holds and expiries from ticketing; and survival methods for modelling the time remaining to fill. All mature, much of it free.

## The Customization Gap
The adaptation is to a small business with named, repeat customers. It requires: (1) a ranked, relationship-aware candidate set rather than an anonymous market, since the right recipient is a specific known client and the ranking should use their own history; (2) restraint on discounting, because a client who learns that waiting produces a cheaper slot will wait — the cannibalisation risk is far higher with repeat local customers than with anonymous travellers, and the sensible default is a non-price offer; (3) offer fatigue as an explicit modelled cost, so a client is not contacted about every gap, which is the mechanism by which naive implementations destroy their own response rates; (4) a fill-probability model over the remaining time, which determines whether to offer at all and how hard, and is straightforward given historical fill outcomes; and (5) operator control over who is offered what, since the relationship belongs to them and an automated offer to the wrong client is a relationship cost they will not accept twice.

## Target Customer
Scheduling and vertical platform vendors, and the larger multi-site operators for whom recovered capacity is a measurable revenue line.

## Impact If Solved
A sophisticated discipline exists for exactly this inventory and has never been applied to it, largely because the unit is small and the buyer is a salon. Offer fatigue and discount restraint are the two adaptations that keep the mechanism working past its first month.
