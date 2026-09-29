# Attributing the Slip

**Niche:** [[niches/game-porting-studios/the-producer-explaining-the-slip/profile|The Producer Explaining the Slip]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The date slipped because the client kept shipping, and the producer has no way to demonstrate that.
**Tags:** #worker-facing #workflow-orchestration #evaluation-metrics #data-integration #descriptive-statistics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to let the person between a fixed date and a moving codebase explain the slip with evidence rather than apology — and whoever gives them that takes the account.

## The Problem
A port runs against a codebase the client is still developing. Every patch means a merge, the merge invalidates completed verification, and the rework is absorbed silently into a schedule that was priced without it. When the date slips, the producer explains it to a client who sees a fixed-price contract and a missed date. There is no record separating work that was in scope from work created by the client's own changes, so the conversation is impressions against impressions.

## Why Nobody Has Built This
Rework caused by merges is not tracked separately from planned work, so there is nothing to point at. Raising it reads as blaming the client. Fixed-price contracts discourage variation conversations. And the producer's role is to absorb this, which is why nobody has built for it.

## What to Build
Measure the cost of the moving target and show it continuously. Attribute every hour to planned work, rework caused by client changes, or scope variation, which is the core and turns an argument into a report. Measure verification invalidated by each merge specifically, since that is the largest and least visible cost of the moving target. Link each client patch to the work it created, which is the evidence the conversation needs. Maintain a running variation register against the contract rather than reconstructing one at the end. Forecast the date continuously from actual progress rather than from the original plan, so the slip is visible early. Share the schedule and its drivers with the client rather than presenting a status, which changes the relationship from reporting to joint management. Warn before the date is at risk, as the conversation is survivable in advance and not afterwards. Quantify the cost of the client's patch cadence, which frequently changes it once anyone sees the number. Keep the record across the project so the final conversation rests on accumulated evidence. And give the producer the numbers rather than the argument, since the numbers make the argument unnecessary.

## Target Customer
Porting and co-development studios, producers and production leadership, publishers commissioning ports, and project management tooling vendors.

## Impact If Built
There is no record separating in-scope work from work created by the client's own changes, so the slip conversation is impressions against impressions. Attributing hours and invalidated verification to specific patches turns it into a report.
