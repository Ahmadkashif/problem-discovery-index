# Cloud Cost Optimisation From FinOps

**Niche:** [[niches/game-hosting-providers/fleet-cost-optimisation/profile|Fleet Cost Optimisation]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cloud cost management is a mature discipline with a vendor category, and game fleets run on an instance type somebody picked once.
**Tags:** #optimization-fundamentals #revenue-impact #evaluation-metrics #descriptive-statistics #confidence-intervals #automation #time-series-forecasting #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to serve the same concurrency for less money across regions, instance types and pricing models, on margins thin enough that the difference decides who wins the contract — and whoever optimises it takes the account.

## The Problem
Cloud cost optimisation became a named discipline with its own vendor category. Rightsizing recommendations, commitment and reservation planning, spot orchestration, idle resource reclamation, and cost allocation by team and service are all standard products. Organisations spending far less than a game hosting fleet run these tools routinely. Game hosting, where infrastructure cost is the dominant line and margins are thin, largely does not — because the tools do not understand what a session is.

## What Already Exists
Rightsizing and instance family recommendation; commitment and reserved capacity planning; spot and preemptible orchestration; idle resource reclamation; and cost allocation and showback.

## The Customization Gap
The adaptation is to a workload whose density limit is a player experience question. It requires: (1) utilisation bounded by playability rather than by resource saturation — a machine at sixty percent CPU may already be producing unacceptable tick rates, which is the substantive difference and invalidates standard rightsizing entirely; (2) preemption handling that must respect live sessions, so spot orchestration needs session-aware draining; (3) placement constrained by latency to players, which no cost tool models; (4) demand that is spiky and regionally specific, complicating commitment planning; and (5) a cost objective that trades directly against match quality through placement, coupling it to the matchmaking layer.

## Target Customer
Game hosting providers, studios running their own fleets, cloud cost vendors, and infrastructure consultancies.

## Impact If Solved
Cloud cost optimisation is mature with an established vendor category. Utilisation bounded by playability rather than saturation invalidates standard rightsizing, and that is what makes this a different product.
