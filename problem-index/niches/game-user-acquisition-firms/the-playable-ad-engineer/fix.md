# Two Hundred Kilobytes Over Budget

**Niche:** [[niches/game-user-acquisition-firms/the-playable-ad-engineer/profile|The Playable Ad Engineer]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The playable is finished, it is slightly over the size limit, and the campaign starts tomorrow.
**Tags:** #worker-facing #quick-win #automation #workflow-orchestration #optimization-fundamentals #evaluation-metrics #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to let one engineer build a complete small game to a five-megabyte budget in six network-specific formats on a campaign deadline — and whoever makes that tractable takes the account.

## The Problem
The size limit is discovered at packaging, at the end, when the playable is complete. Being slightly over means cutting something — an animation, an audio track, a texture resolution — under time pressure, which produces worse decisions than the same cuts made earlier would have. It happens on most campaigns because nothing tracks the budget while the work is being done.

## Why It's Still Broken
The budget is checked at the end — a constraint that is only measured when the work is finished forces every adjustment into the worst possible moment, and nothing during development says how much room is left. Asset sizes are not visible during development. The pipeline reports total size and not composition. And the deadline is fixed.

## What a Fix Looks Like
Make the budget a live number during development. Report current size against budget on every build, which is the fix and takes an afternoon to wire up. Break the size down by asset and code so the engineer knows what is consuming it, since a total alone does not help. Alert when a change adds significantly, so the decision is made when the change is made. Set per-category sub-budgets at the start, which forces the trade-offs early where they are cheaper. Run automatic asset optimisation continuously rather than as a final pass. Keep a record of what past playables spent by category, which makes the initial budget realistic. Check against every target network's limit, as they differ and the tightest one governs. Build a library of pre-optimised common assets, which removes a recurring cost. Flag the highest-cost assets with their contribution, so the cut list is obvious. And make going over budget fail the build rather than produce a warning, which is what keeps it honest.

## Who Feels the Pain
Engineers cutting work under deadline; creative teams whose concept is compromised at the last minute; campaigns delayed by a rejection; and the quality of a format the industry spends heavily on.

## Impact If Fixed
A constraint that is only measured when the work is finished forces every adjustment into the worst possible moment. A live size number broken down by asset moves the decisions to when they are cheap.
