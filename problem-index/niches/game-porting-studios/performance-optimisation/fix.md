# Three Weeks to Find the Frame Cost

**Niche:** [[niches/game-porting-studios/performance-optimisation/profile|Performance Optimisation]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The frame spike was a known anti-pattern for that platform and it took three weeks to find because nobody had written the pattern down.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #change-point-detection #automation #confidence-intervals #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to find out why a stranger's game runs at half the required frame rate on constrained hardware — and whoever shortens that search takes the account.

## The Problem
A large share of porting performance problems are recurring. The same platform-specific anti-patterns appear across project after project: a particular allocation behaviour, a synchronisation pattern, a texture format, a shader construct that is cheap on one architecture and expensive on another. Each project rediscovers them from scratch, at the cost of weeks, because the knowledge lives with whichever engineer hit it last and was never recorded.

## Why It's Still Broken
Nobody wrote them down — expertise that exists only as individual memory is rediscovered by every new project at full cost, no matter how many times the studio has seen it. Post-project reviews do not happen. The engineers who know are on the next project. And documenting feels like overhead against a deadline.

## What a Fix Looks Like
Write the patterns down and check for them first. Maintain a per-platform anti-pattern catalogue with signatures and fixes, which is the fix and is a document that pays for itself in one project. Capture each project's findings at close in a consistent format, which is an hour of work per project. Check new codebases against the catalogue before profiling, since a scripted check catches several of them immediately. Record the measured cost of each pattern, as the magnitude determines priority. Keep the fixes alongside the patterns, because the diagnosis is only half of what the next engineer needs. Share it across the studio rather than within a team, which is where the duplication currently occurs. Note which engine versions and platforms each applies to, so the catalogue stays usable as both move. Include content and asset patterns, which are frequently the larger share and the more overlooked. Make consulting the catalogue a standard first step rather than an optional resource. And review it after each project rather than letting it decay, which is what separates a living catalogue from a wiki nobody opens.

## Who Feels the Pain
Engineers rediscovering known problems at full cost; studios losing weeks per project to the same causes; producers whose schedules absorb it; and clients paying for expertise the studio already had.

## Impact If Fixed
Expertise that exists only as individual memory is rediscovered by every new project at full cost, no matter how many times the studio has seen it. A per-platform anti-pattern catalogue pays for itself on the first project that consults it.
