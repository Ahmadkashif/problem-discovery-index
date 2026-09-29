# Demand Smoothing and Capacity Planning

**Niche:** [[niches/subscription-commerce/the-fulfilment-planner/profile|The Fulfilment Planner]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Utilities, airlines and appointment-based services all learned to shape demand rather than only to serve it, and subscription fulfilment takes the wave as given.
**Tags:** #convex-optimization #time-series-forecasting #optimization-fundamentals #evaluation-metrics #revenue-impact #confidence-intervals #markov-chains #automation
**Contested on:** Every serious competitor in this niche is fighting to smooth a demand wave that the business itself created — and whoever does that takes the cost out, because the peak is self-inflicted and the planner absorbing it has no authority over the thing causing it.

## The Problem
When capacity is expensive and demand is peaky, the mature answer is to shape the demand: time-of-use pricing in utilities, appointment scheduling in services, yield management in travel, and staggered billing cycles in every large recurring-billing industry from insurance to telecoms. Those industries learned that a peak they create themselves is the cheapest peak to remove. Subscription commerce inherited a clustered billing cycle from its sign-up flow and treats the resulting wave as a fact of the business.

## What Already Exists
Demand shaping through pricing and scheduling; appointment and slot-based capacity allocation; staggered billing cycle practice from utilities and telecoms; workforce scheduling against a demand profile; and queueing models relating utilisation to service quality.

## The Customization Gap
The adaptation is to a demand profile the company sets directly rather than influences. It requires: (1) recognising that the demand is fully controllable rather than merely shapeable, since the company chooses the billing date and this is a stronger position than any of the industries the practice comes from — which makes the optimisation a straightforward assignment problem; (2) subscriber preference respected in the assignment, since a delivery day matters to people and the levelling should offer rather than impose; (3) the migration of an existing base handled without disrupting revenue recognition, which is the finance objection and is a timing question rather than an amount one; (4) capacity modelled including quality effects, since errors and damage rise under peak pressure and the cost of the peak is more than labour; and (5) the third-party logistics contract renegotiated against a smoothed profile, since the peak surcharge is a large part of the cost and disappears with the peak.

## Target Customer
Fulfilment and operations leadership, subscription operators, and the capacity planning discipline for whom fully controllable demand is an unusually easy case.

## Impact If Solved
The demand is fully controllable rather than merely shapeable, which is a stronger position than any industry the practice comes from. Renegotiating the logistics contract against a smoothed profile captures a peak surcharge that disappears with the peak.
