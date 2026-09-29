# A Pipeline That Survives the Project

**Niche:** [[niches/game-porting-studios/build-and-toolchain/profile|Build & Toolchain Management]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same multi-platform build pipeline is rebuilt from scratch on every project and discarded at the end.
**Tags:** #workflow-orchestration #automation #data-integration #evaluation-metrics #compliance #descriptive-statistics #quick-win #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to keep several platforms' builds working across every project, every SDK update and every client engine version — and whoever makes that reliable takes the account.

## The Problem
Each project brings a client engine, a set of target platforms, a matrix of configurations and a build pipeline someone assembles from the last project's scripts. It breaks when an SDK updates, when the client changes their engine, when a devkit is reimaged. Engineers block on it. The knowledge of how it works lives with whoever set it up, and at project end the whole thing is discarded rather than becoming infrastructure.

## Why Nobody Has Built This
Build engineering has no client-facing value so it is never funded as a product. Each project's engine and platform mix looks different enough to justify starting over. Console SDK licensing complicates shared infrastructure. And the person who would build it is always on a project.

## What to Build
Make the pipeline a reusable asset rather than a per-project artefact. Build a standard multi-platform pipeline parameterised by engine and target rather than written per project, which is the core and converts recurring setup into configuration. Manage SDK versions explicitly with pinning and controlled upgrade, since an unmanaged SDK update is the commonest way a project loses a day. Make builds reproducible so a failure can be diagnosed rather than re-run hopefully. Cache aggressively across configurations and projects, which is where most build time goes. Detect and report breakage with enough context to fix rather than a raw log. Manage devkit and build machine capacity as a shared resource with visibility, as contention is a silent tax across concurrent projects. Keep the pipeline configuration with the project but the machinery central, which is what makes it survive project close. Support the client's own build process where they have one, since fighting it is a permanent cost. Report build health and queue times, which is how the investment gets justified. And treat it as the studio's infrastructure rather than as each project's chore.

## Target Customer
Porting and co-development studios, build engineering teams, publishers with multi-platform pipelines, and build infrastructure vendors.

## Impact If Built
The same pipeline is rebuilt and discarded on every project, and it blocks engineers each time it breaks. A parameterised central pipeline with managed SDK versions turns recurring setup into configuration.
