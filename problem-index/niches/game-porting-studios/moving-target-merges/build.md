# Merging Without Redoing the Port

**Niche:** [[niches/game-porting-studios/moving-target-merges/profile|Moving-Target Merge Management]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every client patch is merged by hand into a codebase that has been changed throughout.
**Tags:** #automation #workflow-orchestration #graph-theory #data-integration #evaluation-metrics #descriptive-statistics #sets-and-logic #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to keep a port synchronised with a codebase that ships every fortnight without redoing the platform work each time — and whoever automates that merge takes the account.

## The Problem
Porting work touches code throughout the project, not just in an isolated platform layer. When the client ships, the incoming changes conflict with that work, and resolving them requires understanding both the client's intent and the port's. The merge takes days, breaks things, and invalidates verification. It recurs every fortnight, is largely mechanical, and consumes engineers who should be doing the actual port.

## Why Nobody Has Built This
Version control merges text and has no notion of why a change was made. Each project's divergence is unique. Nobody has treated the merge as a recurring engineered process rather than as a chore. And the effort is billable.

## What to Build
Structure the divergence so merges become mechanical. Isolate platform changes behind a defined boundary wherever possible, which is the core — a port structured to minimise contact with shared code turns most merges into a fast-forward. Classify incoming conflicts by whether they touch platform work, which lets the straightforward majority be resolved automatically. Analyse an incoming merge's impact before applying it, so the team knows what it will cost rather than discovering during. Run a scoped regression check immediately after merge rather than waiting for the next full pass. Record recurring conflict hotspots, since the same files conflict repeatedly and restructuring them once pays permanently. Maintain the port's changes as a reviewable set rather than as accumulated divergence, which is what makes them portable across client versions. Automate the merge for patches that do not touch platform code at all, which is a large share. Report merge cost per patch, which feeds directly into the commercial conversation. Support batching patches into scheduled integration points rather than merging continuously. And keep the platform work re-appliable, because a client version jump is otherwise a rewrite.

## Target Customer
Porting and co-development studios, build and tools engineering, publishers managing external development, and version control tooling vendors.

## Impact If Built
A port structured to minimise contact with shared code turns most merges into a fast-forward, and nobody structures it that way. Conflict classification plus scoped regression makes the fortnightly merge mechanical.
