# An Instrument That Establishes Something

**Niche:** [[niches/game-hosting-providers/the-support-engineer/profile|The Support Engineer]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The engineer's entire toolkit proves the infrastructure is fine, which is the one thing the complaint was not about.
**Tags:** #worker-facing #data-integration #change-point-detection #automation #evaluation-metrics #confidence-intervals #k-means-clustering #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to give the person handling lag complaints an instrument that can actually establish something, instead of a job that consists of being unable to prove anything — and whoever gives them that takes the account.

## The Problem
A support engineer receives a ticket describing lag. Their dashboards show the servers are healthy, which is almost always true and almost never relevant. They have no view of the player's connection, no history of that player's previous sessions, no way to see whether other players on the same route are affected, and no leverage with the access provider. They send a macro, the ticket closes, the player remains unable to play, and the engineer does this dozens of times a day.

## Why Nobody Has Built This
The tooling was built to operate infrastructure, not to resolve player complaints, and nobody re-scoped it. Client-side data requires the studio's cooperation. The support function is a cost centre. And the structural impossibility of the job is treated as its nature rather than as a problem.

## What to Build
Give the engineer the player's side and the population's side. Surface a client-side diagnostic capture with the ticket — path, jitter, loss, local conditions — which is the core and is the half of the picture the engineer has never had. Show the player's own session history so degradation is visible against their baseline rather than against an absolute. Cluster the ticket against others on the same route, region or access provider, since a cluster is diagnosable and a single ticket is not. Suggest the most likely responsible layer with confidence, which converts a guess into a starting point. Provide an evidence pack the player can use with their access provider, as that is the only party with standing where the fault usually is. Offer a mitigation the engineer can actually apply — region reallocation, a route change — because being able to do something is the difference in this role. Maintain a known-issues view so recurring routes are answered immediately. Track resolution rather than only closure, which is the metric change that redirects the whole function. Record what the diagnosis turned out to be, so the pattern library builds. And give the engineer language for the honest answer when the cause is outside anyone's control, which is frequently the truth and is currently unsayable.

## Target Customer
Game hosting providers, studio support organisations, outsourced support providers, and support tooling vendors.

## Impact If Built
The engineer's entire toolkit proves the infrastructure is fine, which is the one thing the complaint was not about. A client-side capture plus route-level clustering gives them the half of the picture they have never had.
