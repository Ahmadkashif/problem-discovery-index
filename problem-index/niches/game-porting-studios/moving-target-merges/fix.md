# The Merge That Undid the Platform Work

**Niche:** [[niches/game-porting-studios/moving-target-merges/profile|Moving-Target Merge Management]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The client's refactor landed on top of three weeks of platform work and nobody noticed until the frame rate halved.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #change-point-detection #data-integration #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep a port synchronised with a codebase that ships every fortnight without redoing the platform work each time — and whoever automates that merge takes the account.

## The Problem
A merge resolves cleanly at the text level and silently reverts the substance of platform work. The client refactored a system the port had optimised; the merge takes their version, the optimisation is gone, and nothing fails to compile. It is discovered later by a performance regression or a certification failure, and by then several more merges have landed on top of it.

## Why It's Still Broken
The merge tool resolves text and knows nothing about intent — a clean merge is not a correct merge, and there is no check between the merge succeeding and the work being silently undone. Platform changes are not marked as such. No performance check runs after a merge. And the detection happens at the next milestone.

## What a Fix Looks Like
Mark the work and check it after every merge. Tag platform and optimisation changes explicitly so a merge touching them is flagged for review, which is the fix and is a convention rather than a tool. Run a performance smoke test after every merge, since a halved frame rate is detectable in minutes and currently is not. Diff the merged result against the port's intended state in the areas that matter, rather than trusting the merge outcome. List which of the port's changes an incoming merge touches, before applying it. Require review of any merge that touches tagged code, which is a small fraction of merges. Keep the port's substantive changes as a reviewable set so they can be re-applied deliberately. Record every silent revert found, as the pattern identifies the files that need restructuring. Notify the engineer who made the original change, because they will spot a regression nobody else can. Check certification-relevant behaviour after merges too, since those regress the same way. And make the post-merge check automatic rather than something someone remembers.

## Who Feels the Pain
Engineers redoing work they finished weeks ago; studios losing schedule to invisible regressions; producers explaining a slip with no visible cause; and the frame budget, which quietly refills.

## Impact If Fixed
A clean merge is not a correct merge, and there is no check between the merge succeeding and the work being silently undone. Tagging platform changes and running a performance smoke test after every merge catches it the same day.
