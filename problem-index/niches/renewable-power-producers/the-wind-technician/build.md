# A Pre-Climb Brief From the Fleet's Own Fixes

**Niche:** [[niches/renewable-power-producers/the-wind-technician/profile|The Wind Technician]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Senior technicians know what usually causes each fault on each turbine model, and no tool hands that knowledge to the crew before it climbs.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #feature-engineering #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get a stopped turbine running again on the first climb, and whoever has the highest first-time fix rate on technician callouts takes the account.

## The Problem
A fault code names a symptom. The cause is one of several, and the right one depends on the model, the turbine's history and the SCADA pattern before the trip. Juniors guess, climb, and often come back.

## Why Nobody Has Built This
Work orders are free text in many systems, OEM fault vocabularies differ by platform, and the people who know the patterns are too busy climbing to write them down. Field service vendors schedule work; they do not diagnose it.

## What to Build
For each ticket, a brief generated from the fleet's work-order history and SCADA: likely causes ranked by how often each resolved the same code on the same model, the trend before the trip that distinguishes them, the parts and tools each fix used, and the senior technicians' notes for that pattern, searchable in plain language. After the job, a voice note becomes a coded work order that improves the next brief.

## Target Customer
Regional O&M directors at IPPs and independent service providers running 500+ turbines.

## Impact If Built
Raising first-time fix rate from ~70% to ~85% (estimate) avoids ~1,500 repeat climbs a year on a 1,000-turbine fleet with ~10,000 callouts.
