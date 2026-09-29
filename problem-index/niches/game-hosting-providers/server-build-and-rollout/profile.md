# Server Build & Rollout

**Parent Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Category:** ⚡ Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to get a new game server build onto a live global fleet without disconnecting the people currently playing on it — and whoever does that cleanly takes the account.

## Profile
**Market Size:** ~$200M US
**Share of Parent Industry:** ~7% of category revenue
**Digital Adoption:** Medium — partial
**Target Buyer:** Platform engineering
**Automation Potential:** Very high — packaging, rollout and drain

## What Makes This a Distinct Niche
Shipping a server build is different from shipping a service: sessions are stateful, long-lived and cannot be interrupted without visibly harming a player mid-match. Builds must reach dozens of regions, coexist with the old version while matches finish, and be reversible. Most teams handle this with a maintenance window — an outage announced in advance — because the drain-and-replace machinery was never built. It is entirely mechanical work and it is where a great deal of avoidable downtime comes from.

## Current Tools & Gaps
A build pipeline, an image registry, a fleet orchestrator and a maintenance window. The gaps: no session-aware draining; no version coexistence; no regional staged rollout; no automatic rollback on regression; and no compatibility checking between client and server versions.

## Problems
- [[niches/game-hosting-providers/server-build-and-rollout/build|🔨 Build: Shipping Without a Maintenance Window]]
- [[niches/game-hosting-providers/server-build-and-rollout/buy|🛒 Buy: Progressive Delivery From Cloud Native Operations]]
- [[niches/game-hosting-providers/server-build-and-rollout/fix|🔧 Fix: The Match That Ended Mid-Round]]
