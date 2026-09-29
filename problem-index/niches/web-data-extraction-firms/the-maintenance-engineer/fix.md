# Forty Tickets From One Redesign

**Niche:** [[niches/web-data-extraction-firms/the-maintenance-engineer/profile|The Maintenance Engineer]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** One site deploys one redesign and forty extractions break, arriving as forty independent tickets that forty times report the same underlying change.
**Tags:** #k-means-clustering #dbscan #automation #evaluation-metrics #descriptive-statistics #worker-facing #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn an unending repair queue into prioritised, mostly-automated work — and whoever does that takes the account, because this queue is where the industry's engineering capacity goes.

## The Problem
A retailer redeploys its site. Forty extractions across a dozen customers break — product pages, category listings, search results, regional variants. Each raises its own ticket. Three engineers pick up different tickets from the same site without realising it, each independently works out what changed, and each writes a fix for their own extraction. The same diagnosis is performed three times and the same structural change is handled forty times. The queue shows forty items where there is one event and one fix that would have covered most of them.

## Why It's Still Broken
Tickets are generated per extraction because extractions are the unit the system monitors. Nothing groups by target, even though the target is the obvious common cause. The duplication is invisible in a queue sorted by time. And each engineer's fix works, so the waste never surfaces as a failure.

## What a Fix Looks Like
Group by cause rather than by symptom. Cluster breakages by target host and time window, which catches the overwhelming majority of correlated failures with a trivial rule and is the fix — one event should produce one item. Detect the site change directly rather than inferring it from failures, by monitoring page structure independently, so the event is identified before the forty tickets arrive. Present the group with one diagnosis and a shared repair, applying the fix across all affected extractions where the structure is common. Assign the whole group to one engineer, since the second and third diagnoses are pure waste. Detect near-miss extractions on the same site that have not broken but are now fragile, since a redesign frequently breaks some and weakens others. Report the event to affected customers once rather than as forty incidents, which is also a better customer experience. Track events rather than tickets as the maintenance metric, because ticket counts overstate the work and understate the structure of it. And record the site's change history, since a site that redeploys monthly should be handled differently from one that has been stable for three years.

## Who Feels the Pain
Engineers repeating a colleague's diagnosis; teams whose queue metrics overstate the work by a factor; and customers receiving forty incident notifications about one third-party deployment.

## Impact If Fixed
One event produces forty tickets and three independent diagnoses. Clustering by target host and time window is a trivial rule that collapses the majority of correlated failures, and monitoring page structure directly identifies the event before the tickets arrive.
