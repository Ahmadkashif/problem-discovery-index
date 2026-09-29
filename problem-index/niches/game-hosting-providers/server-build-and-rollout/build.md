# Shipping Without a Maintenance Window

**Niche:** [[niches/game-hosting-providers/server-build-and-rollout/profile|Server Build & Rollout]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Updating a game server fleet means taking the game down, because nobody built the machinery to drain sessions instead.
**Tags:** #workflow-orchestration #automation #optimization-fundamentals #evaluation-metrics #data-integration #compliance #change-point-detection #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to get a new game server build onto a live global fleet without disconnecting the people currently playing on it — and whoever does that cleanly takes the account.

## The Problem
A game server holds a live session with real players in the middle of a match. Replacing the binary underneath them is unacceptable, so the standard approach is a maintenance window: announce downtime, disconnect everyone, replace the fleet, bring it back. This costs playtime, annoys players, constrains release cadence, and is unnecessary — the sessions are finite and drain naturally within minutes if the orchestration understands them.

## Why Nobody Has Built This
Container orchestration assumes stateless or restartable workloads and has no concept of a session that must be allowed to finish. Each studio builds its own partial version of drain logic. Maintenance windows are an accepted norm nobody has challenged. And the work is unglamorous infrastructure with no product owner.

## What to Build
Make the orchestrator session-aware and roll out regionally. Drain by session rather than by instance — stop allocating to a server, let its matches finish, then replace it — which is the core and removes the need for a window entirely. Run old and new versions concurrently with matchmaking routing by version, since coexistence is what makes a gradual rollout possible at all. Roll out region by region rather than globally, so a regression affects a fraction rather than everyone. Check client and server version compatibility automatically before allocating, as the mismatch is a common and entirely preventable failure. Roll back automatically on session-level regression signals rather than on infrastructure metrics, because the symptom appears in match quality before it appears in CPU. Bound the drain so a stuck session cannot hold a machine indefinitely. Pre-warm the new version before draining the old, which keeps capacity flat through the transition. Report the rollout's progress and cost in player-minutes rather than in pods. Handle the emergency case where an immediate replacement is genuinely required. And make the drain semantics a first-class part of the orchestration rather than a script each studio writes.

## Target Customer
Game hosting and multiplayer platform vendors, studios operating multiplayer titles, orchestration tooling providers, and cloud infrastructure teams.

## Impact If Built
Sessions are finite and drain naturally within minutes, so the maintenance window is a choice rather than a constraint. Session-aware draining with version coexistence removes announced downtime from the release process.
