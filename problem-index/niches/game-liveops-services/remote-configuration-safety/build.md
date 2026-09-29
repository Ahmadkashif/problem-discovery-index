# Knowing What a Value Reaches

**Niche:** [[niches/game-liveops-services/remote-configuration-safety/profile|Remote Configuration Safety]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Thousands of values control a live game and nobody can say what any one of them touches.
**Tags:** #graph-theory #data-integration #workflow-orchestration #automation #evaluation-metrics #compliance #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell someone what a configuration value actually reaches before they change it in a live game — and whoever maps the blast radius takes the account.

## The Problem
Remote configuration is how a live game is operated: reward amounts, drop rates, prices, timers, feature flags, matchmaking parameters. There are thousands of them, they interact, and the relationship between a value and the systems it affects exists only in the head of whoever implemented it. Someone changes one to fix a problem, and something unrelated breaks for everyone at once, with no preview and no staging.

## Why Nobody Has Built This
Configuration is treated as data rather than as code, so none of the discipline applied to code was applied to it. The platforms sell a console and a key-value store. Mapping dependencies requires connecting configuration keys to game code, which nobody has instrumented. And it works most of the time.

## What to Build
Map the graph and gate the change. Build a dependency graph from configuration keys to the code paths and systems that read them, which is the core — the blast radius is knowable from the codebase and nobody has ever extracted it. Show the affected systems and player segments before a change is applied, since a preview at the moment of edit is what actually prevents the mistake. Record an owner and a documented intent per value, as an unowned value is one nobody can safely change. Validate ranges and known-bad combinations automatically, which catches a large share of incidents mechanically. Stage rollouts by player percentage rather than applying instantly to everyone, which is the single highest-value control and is absent from most consoles. Monitor key metrics automatically after a change with an automatic rollback path, because detection currently depends on someone noticing. Require review proportional to the blast radius rather than reviewing everything or nothing. Show the change history per value with its observed effects, which builds the institutional memory that currently walks out of the door. Flag values that have not been touched in a year and are still read, since those are where the surprises hide. And support a dry run against the live population, which is the closest thing to a test this layer can have.

## Target Customer
Live game operators, live ops platform vendors, backend and platform engineering teams, and games infrastructure providers.

## Impact If Built
The blast radius is knowable from the codebase and nobody has ever extracted it. A dependency graph with a pre-change preview and staged rollout applies to configuration the controls that code has had for a decade.
