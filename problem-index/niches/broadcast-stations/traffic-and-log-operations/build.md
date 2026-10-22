# A Log Optimiser That Learns the Traffic Director's Moves

**Niche:** [[niches/broadcast-stations/traffic-and-log-operations/profile|Traffic, Log Building & Continuity]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Traffic systems place spots by fixed rules and leave the conflicts to a person, whose choices about what to move and what to bump are the real placement logic and are never captured.
**Tags:** #dynamic-programming #optimization-fundamentals #gradient-boosting #feature-engineering #worker-facing #automation #revenue-impact
**Contested on:** Every serious competitor in this niche (traffic-system vendors, order-exchange and document-extraction services, and hubbed traffic centres) is fighting to turn every order, copy instruction and late change into an on-air log that runs without a missed spot, wrong copy or separation conflict, and whoever drives discrepancies toward zero with the fewest traffic staff takes the account.

## The Problem
Each day's log leaves the system's placement engine with conflicts and unplaced spots. The traffic director resolves them by hand using unwritten rules: which advertisers tolerate moves, which agencies audit, which spots can slide to the next break.

## Why Nobody Has Built This
Placement engines belong to the traffic vendors, who optimise for general rules across thousands of stations. The station-specific costs of each kind of move live only in the director's head. Hubbed traffic centres have made the problem bigger without making it visible.

## What to Build
A constrained optimiser that resolves the day's conflicts with the fewest weighted moves and preemptions. The weights are learned from the traffic director's historical edits and the makegood and credit outcomes that followed. Each proposed move comes with a reason, and the director approves in bulk.

## Target Customer
Group traffic hubs and large-market stations running 2,000 or more spots a week (estimate).

## Impact If Built
Fewer makegoods and credits, less time in log editing, and the senior traffic director's judgement preserved when they leave.
