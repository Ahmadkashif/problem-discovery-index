# A Queue That Never Empties

**Niche:** [[niches/web-data-extraction-firms/the-maintenance-engineer/profile|The Maintenance Engineer]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Maintenance engineers hold a queue of broken extractions that never empties, fixing selectors against sites that will change again, with no way to know which of the working extractions are quietly wrong.
**Tags:** #worker-facing #evaluation-metrics #descriptive-statistics #automation #workflow-orchestration #gradient-boosting #confidence-intervals #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to turn an unending repair queue into prioritised, mostly-automated work — and whoever does that takes the account, because this queue is where the industry's engineering capacity goes.

## The Problem
An engineer's queue holds a hundred and forty broken extractions. Some serve a customer's core product; some serve a trial that ended. Some will be fixed in four minutes and some need an afternoon. Forty of them are the same site redesign appearing forty times. Meanwhile an extraction that is returning wrong values with the right shape is not in the queue at all, because nothing detected it, and it is the one doing actual harm. The engineer works from the top, or from whoever escalated most recently, and the queue is the same length tomorrow.

## Why Nobody Has Built This
Maintenance is treated as operational cost rather than as a product surface, so it receives no engineering investment. Prioritisation needs customer impact data that lives in a different system. Automated repair looked infeasible when extractors were hand-written selectors and has only recently become straightforward — the assumption has not updated. And the engineers who would build the tooling are the ones drowning in the queue.

## What to Build
Make the queue smaller and ordered by what matters. Prioritise by customer impact — which customers consume this, how central it is to their use, what a day of absence costs them — which is a join the firm can make and immediately turns an arbitrary order into a rational one. Group related breakages, since one redesign produces many failures and presenting them as one item with a shared fix removes a large share of the ticket count outright. Automate the repair of the mechanical cases, which the automated repair niche develops and which is most of them. Surface suspected silent breakage in the same queue, ranked, because that is the highest-value work and is currently invisible to the person best placed to do it. Estimate effort per item, so an engineer can clear the quick ones deliberately rather than discovering their size one at a time. Accumulate per-site knowledge — this site changes quarterly, this one uses a rendering pattern that needs a particular approach, this one has a regional variant that breaks separately — which is the expertise that currently leaves with the person. Report queue depth, age and inflow as a capacity signal, since a queue that never empties is a staffing fact nobody has stated numerically. And report time-to-repair by customer impact, because that is the service level customers actually experience.

## Target Customer
Extraction operations teams, the engineers in the queue, and the firms whose engineering capacity is consumed by it.

## Impact If Built
The queue is ordered by who complained and excludes the work that matters most. Grouping related breakages removes a large share of the ticket count immediately, and surfacing suspected silent breakage puts the highest-value work in front of the person who can do it.
