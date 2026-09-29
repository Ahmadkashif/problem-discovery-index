# Continuous Profiling From Production Systems

**Niche:** [[niches/game-porting-studios/performance-optimisation/profile|Performance Optimisation]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Server engineering made continuous profiling with source-level attribution routine, and game porting profiles by hand at milestones.
**Tags:** #change-point-detection #evaluation-metrics #descriptive-statistics #data-integration #automation #confidence-intervals #graph-theory #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to find out why a stranger's game runs at half the required frame rate on constrained hardware — and whoever shortens that search takes the account.

## The Problem
Production software engineering made continuous profiling standard: always-on sampling profilers attribute CPU and memory cost to specific lines of source, flame graphs make the hierarchy legible, comparisons across versions isolate regressions to a change, and the whole thing runs automatically rather than as an investigation. Engineers diagnosing a slow service have far better instrumentation than engineers making a game hit frame budget.

## What Already Exists
Always-on sampling profilers; source-level cost attribution; differential flame graph comparison; automatic regression detection across versions; and allocation site attribution.

## The Customization Gap
The adaptation is to a hard real-time budget on fixed constrained hardware. It requires: (1) a per-frame budget rather than aggregate throughput, so the tail matters more than the mean and a single spike is a visible failure — this is the substantive difference and inverts the usual server emphasis; (2) GPU as well as CPU cost, with an entirely separate attribution problem; (3) fixed console hardware where the profiler must run within the same constrained budget; (4) cost driven substantially by content and assets rather than by code paths; and (5) a codebase the engineer did not write, so source attribution must be paired with structural understanding.

## Target Customer
Porting studios, platform holders, engine vendors, and profiling and observability vendors.

## Impact If Solved
Continuous profiling with source attribution became routine in server engineering and the tooling is mature. A hard per-frame budget on fixed hardware, with GPU cost and content as first-class, is what has to be rebuilt.
