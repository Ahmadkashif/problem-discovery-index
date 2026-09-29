# Buy: Routing and Optimisation Stacks Adapted to a Contractor Workforce

**Niche:** [[niches/gig-delivery-platforms/dispatch-and-batching/profile|Dispatch, Routing & Batching]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fleet routing and dispatch products assume an employed driver who goes where they are sent; here every assignment is an offer that can be declined and the workforce chooses its own hours.
**Tags:** #convex-optimization #dynamic-programming #graph-theory #time-series-forecasting #evaluation-metrics #data-integration #automation #revenue-impact
**Contested on:** Whether dispatch infrastructure built for a directed fleet can serve a workforce that accepts or declines each assignment.

## The Problem

Routing and dispatch software is a substantial, mature category. Last-mile route optimisation, real-time dispatch, capacity planning and fleet telematics are sold to logistics operators and work well, and the regional and vertical delivery platforms that cannot build their own buy from it.

The category's foundational assumption is a directed fleet: a known set of drivers, on shift, who execute the route they are given. A gig delivery marketplace has none of that. Supply is stochastic and self-scheduling, every assignment is an offer with a decline probability, couriers appear and disappear mid-shift, and the optimiser's decision changes the supply it will have available in twenty minutes.

## What Already Exists

Route optimisation engines and VRP solvers, commercial and open-source. Real-time dispatch platforms for courier and field service fleets. Telematics and driver management. Demand forecasting products. Map and traffic services. Constraint solvers capable of the combinatorial core. For a platform below a certain scale, buying most of this is clearly right.

## The Customization Gap

**Assignment is an offer with a decline probability.** A VRP solver produces an assignment and assumes it executes. Here each assignment has an acceptance probability depending on the courier, the offer amount and the conditions, and the plan has to be robust to declines. That turns a deterministic assignment problem into a stochastic one with a very different solution structure, and no commercial routing product models it.

**Supply is endogenous and self-scheduling.** Fleet products take driver availability as an input. Here availability responds to earnings, incentives and the platform's own past behaviour, on a timescale of hours to weeks. Supply forecasting has to model courier response to conditions the platform controls, which is a feedback loop absent from the fleet model.

**Merchant readiness is a stochastic release time with no analogue.** Logistics dispatch assumes goods are available at the depot. Here the pickup becomes available at an uncertain time influenced by the platform's own dispatch decision, and sending a courier too early converts uncertainty into unpaid waiting. Modelling pickup readiness as a distribution and choosing dispatch timing against it is core to this domain and peripheral to fleet routing.

**Batching is a pay-model decision, not only a routing one.** Routing products batch to minimise distance. Here the combination changes what the courier is paid under a pay model with its own rules, so the batching objective has to include the pay consequence. The routing engine has no representation of driver compensation varying by route structure.

**Worker outcome is a constraint, and increasingly a legal one.** Fleet software optimises cost subject to service levels, with the driver's pay fixed by employment. Where minimum earnings standards apply per engaged hour, the assignment itself is constrained by the compensation it produces — a constraint type that does not exist in the bought products and cannot be bolted on after the solve.

## Target Customer

Regional and vertical delivery platforms — grocery, pharmacy, alcohol, restaurant aggregators outside the top tier — who license routing infrastructure and need to know which parts of the marketplace problem it does not cover. Also the routing vendors, for whom the gig marketplace pattern is a recognisable product extension as the model spreads beyond the majors.

## Impact If Solved

The combinatorial and geographic machinery gets bought and the marketplace-specific layer — decline probability, endogenous supply, stochastic pickup readiness, pay-aware batching, earnings constraints — gets built deliberately rather than discovered in production. For a mid-sized platform that is the difference between a dispatch system that works at 10,000 orders a day and one that degrades at 50,000.
