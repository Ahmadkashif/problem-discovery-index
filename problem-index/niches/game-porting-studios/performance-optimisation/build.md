# Shortening the Search for the Bottleneck

**Niche:** [[niches/game-porting-studios/performance-optimisation/profile|Performance Optimisation]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The frame budget is missed by half and the work is hypothesis and measurement in someone else's code.
**Tags:** #change-point-detection #evaluation-metrics #graph-theory #descriptive-statistics #confidence-intervals #optimization-fundamentals #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to find out why a stranger's game runs at half the required frame rate on constrained hardware — and whoever shortens that search takes the account.

## The Problem
Making a game hit frame budget on a constrained platform is a search problem. The profiler says where time goes at the system level; establishing why, in a codebase the engineer did not write, for hardware the original team never targeted, is judgement and iteration. The studio's most experienced people spend the largest and least predictable part of the project on this, and each project's learning stays with whoever did it.

## Why Nobody Has Built This
Profilers report cost and not cause, and closing that gap requires connecting runtime measurement to source structure. Every project is different, so nobody amortises the tooling. The expertise is the studio's product, so systematising it feels like commoditising itself. And there is no record of past projects to learn from.

## What to Build
Attribute cost to causes and rank the work by expected gain. Attribute frame cost to source-level constructs — specific draw call patterns, allocation sites, synchronisation points, asset properties — rather than to systems, which is the core and is where the search actually happens. Compare the target platform's profile against the source platform's to isolate what changed, since the difference is far more informative than the absolute and is rarely examined systematically. Maintain a library of the causes found on past projects with their signatures, which is the studio's real expertise and currently walks around in people's heads. Rank candidate optimisations by expected gain against effort, as the sequencing determines whether the schedule holds. Detect the known anti-patterns for each target platform automatically, which catches a meaningful share before anyone profiles. Measure continuously across builds so regressions are caught immediately rather than at the next milestone. Relate asset properties to frame cost, because a large share of the fix is content rather than code and is frequently missed. Record what was tried and what it yielded, which turns each project into evidence. Support the memory budget with the same treatment, since it constrains as hard as frame time. And present it as a ranked hypothesis list for an expert to work through rather than an answer, which is what a skilled engineer will actually use.

## Target Customer
Porting and co-development studios, platform holders and their developer relations, engine vendors, and performance tooling providers.

## Impact If Built
Profilers report cost and not cause, and the search for the cause is the least estimable part of every project. Source-level attribution plus a cross-platform profile diff turns an open search into a ranked list.
