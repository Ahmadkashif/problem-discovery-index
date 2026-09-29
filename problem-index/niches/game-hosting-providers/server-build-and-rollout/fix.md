# The Match That Ended Mid-Round

**Niche:** [[niches/game-hosting-providers/server-build-and-rollout/profile|Server Build & Rollout]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The deployment rolled through, ten thousand matches ended at once, and the players were most of the way through them.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #compliance #descriptive-statistics #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get a new game server build onto a live global fleet without disconnecting the people currently playing on it — and whoever does that cleanly takes the account.

## The Problem
A routine deployment terminates instances that are hosting live matches. Thousands of players are disconnected mid-game, lose their progress in that match, and in ranked modes take a penalty for leaving. Nothing about this is intended — the orchestrator did what it was told, and what it was told did not include the concept of a match in progress. It recurs on every deployment that someone forgets to guard.

## Why It's Still Broken
The orchestrator does not know what a match is — a scheduler that treats an instance hosting a live match exactly like an idle one will end that match every time, and the knowledge required to prevent it lives only in a script someone wrote. Termination grace periods are far shorter than a match. Nobody measures player-minutes lost to deployments. And the incident is absorbed by players rather than by the team.

## What a Fix Looks Like
Tell the scheduler what a session is, and count what deployments cost. Mark instances hosting live sessions as ineligible for termination, which is the fix and is a label plus a policy. Set termination grace periods to the actual match length rather than to a default of seconds. Stop allocating new sessions to instances scheduled for replacement, so the fleet drains ahead of the deployment. Deploy during the region's low period rather than at a globally convenient hour, which reduces the residual by a large factor. Measure and report player-minutes lost per deployment, as the number is what makes anyone fix the rest. Suppress ranked penalties for players disconnected by a deployment, since penalising players for the operator's action is indefensible and easy to detect. Notify the studio's community team before a deployment that will disconnect anyone. Test the drain path routinely rather than assuming it works. Give operators a single command that does the safe thing, because the unsafe one is currently the default. And treat an unplanned mid-match termination as an incident rather than as routine.

## Who Feels the Pain
Players disconnected mid-match and penalised for it; studios handling the complaints; operators who did not intend any of it; and the trust that erodes on every release.

## Impact If Fixed
A scheduler that treats an instance hosting a live match exactly like an idle one will end that match every time. Marking live sessions ineligible for termination is a label and a policy, not a project.
