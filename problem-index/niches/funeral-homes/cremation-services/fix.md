# Retort Scheduling and Throughput Bottleneck

**Niche:** [[niches/funeral-homes/cremation-services/profile|Cremation Services]]
**Industry:** [[industries/funeral-homes|Funeral Homes]]
**Type:** Fix (Pain Point)
**One-liner:** Crematories schedule retort time on whiteboards with no optimization for body size, retort capacity, cool-down cycles, or family-requested timing — creating bottlenecks that delay cremations by days.
**Tags:** #automation #workflow-orchestration #regression #tabular-ml

## The Problem
A cremation retort takes 2-4 hours per cremation depending on body size, plus 1-2 hours for cool-down between uses. A crematory with 2 retorts can process 3-4 cremations per day maximum. During peak demand periods (winter months, pandemic surges), backlogs develop — bodies wait 5-7 days for cremation, straining cold storage and family patience. Scheduling is done on a whiteboard: the operator estimates time per cremation by gut feel, sequences them without optimization, and handles family timing requests (families who want cremation before a memorial service on Saturday) by bumping other cases.

## Why It's Still Broken
Retort scheduling is treated as simple enough to manage manually — "put the next one in when the current one is done." But the hidden complexity is in sequencing: larger bodies take longer and generate more heat (affecting cool-down time for the next cremation), some families have time-sensitive requests, and the operator must balance throughput against the 24-hour minimum hold period required by most states. No one has built scheduling optimization for this workflow because the market is small and the problem seems too simple to justify software.

## What a Fix Looks Like
A scheduling system that takes pending cremation cases (with body weight estimates, authorization status, and family timing preferences), retort specifications (capacity, cycle time, cool-down requirements), and produces an optimized daily schedule. The system sequences cremations to minimize cool-down waste (similar-sized cases back to back), flags cases where authorization is incomplete (can't schedule until signed), and accommodates family timing requests while maximizing daily throughput. Real-time tracking shows actual vs. estimated cycle times, refining future estimates.

## Who Feels the Pain
Crematory operators during peak periods who must explain multi-day delays to families, and year-round operators who know they're leaving capacity on the table but can't quantify how much.

## Impact If Fixed
Increases daily cremation throughput by 15-25% through scheduling optimization, reduces average cremation wait time from 3-5 days to 1-2 days during peak periods, and provides families with accurate timing commitments.
