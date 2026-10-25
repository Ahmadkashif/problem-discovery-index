# One Ledger of Price, Service and Evidence per Container

**Niche:** [[niches/waste-haulers/commercial-container-service/profile|Commercial Front-Load Container Service]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A commercial account's price history, its service history and the camera evidence for each lift sit in three systems, so neither the pricing team nor the billing team can see what the container actually earns and costs.
**Tags:** #gradient-boosting #cnns #feature-engineering #data-integration #revenue-impact #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to grow revenue per commercial container, but that splits into two contests with different winners: pushing the annual price increase through without losing the account, and billing what the truck actually serviced. Decomposed into contested sub-niches below.

## The Problem
A pricing analyst setting next year's increase sees rate history and cancellations. A billing clerk deciding on an overage sees a camera event and the contract. Neither sees the container's full economics: how often it overflows, how long the lift takes, how far it sits from the route's line, what the account has been credited, and how the customer responded to the last increase. So increases are set on averages and overages are billed without knowing whether the container is simply the wrong size.

## Why Nobody Has Built This
Billing, routing, camera and CRM systems are sold by different vendors, and at the majors each is owned by a different department. Camera data has only recently reached fleet scale, and the hauler's pricing team has never had stop-level service data to price with.

## What to Build
A per-container ledger joining contract terms, every price change and fee, every lift with its camera classification and service time, every credit and complaint, and route position. On top, two views: an account margin and price-response score for pricing, and a service-evidence record for billing and disputes. The two sub-niches below each use one half.

## Target Customer
VP of commercial sales or revenue management at regional haulers with 5,000–50,000 commercial containers.

## Impact If Built
Seeing cost to serve and price response per container lets a hauler target increases and right-size containers instead of charging overages; on a $50M commercial book, one point of better-placed yield is ~$0.5M a year (estimate).
