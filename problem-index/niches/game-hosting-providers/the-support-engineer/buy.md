# Diagnostic Tooling From Telecoms Support

**Niche:** [[niches/game-hosting-providers/the-support-engineer/profile|The Support Engineer]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Telecoms support agents run line tests and see the customer's connection from their console, and game support agents see a server dashboard.
**Tags:** #worker-facing #data-integration #automation #workflow-orchestration #evaluation-metrics #change-point-detection #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to give the person handling lag complaints an instrument that can actually establish something, instead of a job that consists of being unable to prove anything — and whoever gives them that takes the account.

## The Problem
Telecoms and broadband support faced an identical problem — a customer reporting a connection that feels bad, with the fault potentially anywhere along a path — and solved it with instruments. Agents run line tests from the console, see the customer's equipment status and history, compare against a neighbourhood baseline, and follow a decision tree that narrows the cause before escalation. The agent can establish something. Game support agents handling structurally identical complaints have none of it.

## What Already Exists
Remote line and connection testing from the agent console; customer equipment and history views; neighbourhood and area comparison baselines; guided diagnostic decision trees; and structured escalation with evidence.

## The Customization Gap
The adaptation is to a path the provider does not own any part of. It requires: (1) no ownership of the access line at all, so the diagnostic must be built from application-level telemetry rather than from network equipment — this is the substantive difference and it removes the line test entirely; (2) a fault that is often about jitter and loss rather than throughput, which consumer connection tests do not measure meaningfully; (3) comparison baselines built from other players on the same route rather than from a physical neighbourhood; (4) an escalation target with no commercial relationship to the provider; and (5) a game client as the only available measurement point, requiring the studio's cooperation.

## Target Customer
Game hosting providers, studio and outsourced support organisations, access providers, and support tooling vendors.

## Impact If Solved
Telecoms gave agents instruments that establish something, which is why their support function works. Owning no part of the path removes the line test, so the diagnostic has to be rebuilt from application telemetry and route-mates.
