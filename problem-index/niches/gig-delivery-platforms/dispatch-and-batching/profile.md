# Dispatch, Routing & Batching

**Parent Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Category:** High Market Share
**Contested on:** Whether the assignment that maximises platform throughput and the customer promise also leaves the courier with work worth doing.

## Profile
**Market Size:** ~$18B — 20% of US gross order value
**Share of Parent Industry:** ~20%
**Digital Adoption:** Very high — the most technically sophisticated layer in the industry
**Target Buyer:** Platform dispatch and marketplace engineering leadership
**Automation Potential:** Fully automated; the contest is over the objective function, not the automation

## What Makes This a Distinct Niche

Dispatch is where these platforms are genuinely world-class. Assigning millions of orders to hundreds of thousands of couriers in real time, under stochastic demand, with merchant readiness uncertainty and traffic, is among the harder operations research problems solved at commercial scale, and it is solved well.

It is contested on what the objective is. The optimisation targets delivery time, order throughput and courier utilisation — quantities that serve the customer promise and the platform's unit economics. The courier's realised earnings per hour of engaged time is not in the objective, and batching is where this shows most sharply: combining orders raises platform throughput and courier utilisation while frequently lowering the courier's per-order pay and raising their total time, so a batched assignment can improve every metric the system optimises and leave the courier worse off.

This is distinct from offer construction because dispatch decides the assignment and the offer describes it. A well-constructed offer for a badly-constructed batch is still a bad job.

## Current Tools & Gaps

The platforms run continuous large-scale assignment with sophisticated demand forecasting, supply positioning, merchant readiness prediction and multi-order batching, refined against operational metrics with a strong experimentation culture. Third-party routing and optimisation vendors serve the smaller regional operators. The technical quality is high.

The gaps are in the objective and in the accounting. Courier-realised outcome is not an optimisation target and mostly not a reported metric. Batching decisions are made without a modelled cost to the courier of the added time. And the distributional question — whether assignment quality is even across couriers or concentrated — is not measured, so nobody knows whether the system systematically gives worse work to some cohorts.

## Problems
- [[niches/gig-delivery-platforms/dispatch-and-batching/build|🔨 Build: Courier-Realised Outcome in the Dispatch Objective]]
- [[niches/gig-delivery-platforms/dispatch-and-batching/buy|🛒 Buy: Routing and Optimisation Stacks Adapted to a Contractor Workforce]]
- [[niches/gig-delivery-platforms/dispatch-and-batching/fix|🔧 Fix: The Batch That Helps Everyone Except the Person Driving It]]
