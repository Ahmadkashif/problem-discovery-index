# Testing the Same Level for the Ninth Time

**Niche:** [[niches/game-porting-studios/cross-platform-verification/profile|Cross-Platform Verification]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The client patched a tutorial script and the whole regression pass runs again on four platforms.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #data-integration #worker-facing #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to verify every change on every platform when verification means people playing the game and the client keeps shipping updates — and whoever automates that takes the account.

## The Problem
Each client patch triggers a full regression pass because nobody knows which parts of the game the change could have affected. Testers replay content they have already verified, on every platform, to establish that a change to an unrelated system did not break it. Most of that work is unnecessary and nobody can say which part, so all of it happens. It is the single largest avoidable cost in a porting project.

## Why It's Still Broken
Nobody knows what a change touches — a full pass is the only safe response to an unknown blast radius, and computing the blast radius has never been anyone's job. The client's changelog is prose. Test coverage is not mapped to systems. And the pass is billable.

## What a Fix Looks Like
Establish what the change touched and test that. Map the client's changes to the systems and content they affect, which is the fix and is derivable from the diff rather than from the changelog. Maintain a mapping from test cases to the systems they exercise, which is a one-time effort per project and enables everything else. Run a reduced pass scoped to the affected areas plus a fixed smoke set, which is the standard approach everywhere else. Ask the client for structured change information rather than prose notes, since they can supply it and are never asked. Track what the reduced passes missed, so the scoping is calibrated rather than hopeful. Prioritise the platforms where divergence has historically occurred rather than treating all four as equal. Batch client patches into scheduled integration points instead of responding to each, which is a commercial conversation worth having. Record test time by cause so the cost of the moving target is visible to both parties. Keep a full pass at defined milestones rather than continuously. And show the client the cost of their patch cadence, which frequently changes it.

## Who Feels the Pain
Testers replaying content they verified last week; studios burning schedule on avoidable passes; producers watching dates slip for no work done; and clients paying for it without knowing.

## Impact If Fixed
A full pass is the only safe response to an unknown blast radius, and computing the blast radius has never been anyone's job. Mapping the client's diff to affected systems scopes the pass and makes the moving-target cost visible.
