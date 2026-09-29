# Facility Adherence Is Never Measured

**Niche:** [[niches/freight-tech-platforms/dock-scheduling-facility-ops/profile|Dock Scheduling & Facility Operations]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Facilities measure carrier on-time arrival obsessively and nobody measures whether the facility honoured the appointment it issued, so the accountability in dock scheduling runs in exactly one direction.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #revenue-impact #quick-win #worker-facing
**Contested on:** Every serious competitor in dock scheduling is fighting to let a carrier book an appointment at any facility without learning that facility's system — and whoever makes booking work across an incompatible estate takes the network.

## The Problem
A carrier arrives at a 10:00 appointment at 09:52 and is unloaded at 14:30. The facility's scorecard records the carrier as on time, which it was. Nothing records that the facility honoured its appointment four and a half hours late. The carrier's driver loses the afternoon and possibly the next day's load, the carrier bills detention and argues about it, and the facility's own operations team has no report telling it that its 10:00 slot routinely runs to the afternoon. Carriers know exactly which facilities do this and price it in privately; the facility does not know it is being priced.

## Why It's Still Broken
Scorecards were built by shippers to manage carriers, so they measure carriers. There is no counterpart because nobody was in a position to demand one — the carrier has less power in the relationship and raising it reads as complaining. The measurement itself is straightforward given appointment times and gate timestamps, both of which exist, and the reason it is not computed is that no party with access has wanted to compute it. Visibility platforms are the natural place and have the same commercial reluctance, since facilities are their customers.

## What a Fix Looks Like
Compute adherence from data that already exists and give it first to the party that can act. For every appointment: scheduled time, arrival time, start of service, completion, and the gap between appointment and service start. Report it back to the facility by door, by shift and by day of week, framed as an operations diagnostic rather than an accusation — because most facilities genuinely do not know, and a facility that discovers its Tuesday afternoon slots run two hours late has a fixable staffing problem. Then publish it to carriers in aggregate, which is what changes the incentive: a facility whose adherence is visible competes for capacity in a tight market on something other than rate. Carriers already hold this information informally; making it explicit costs nothing and rebalances a relationship that currently measures only one side.

## Who Feels the Pain
Drivers losing half a day inside a fence, frequently unpaid; carriers whose capacity is consumed by facilities that do not honour their own appointments; and facility operations teams who would fix the problem if anyone showed it to them.

## Impact If Fixed
Adherence measurement is arithmetic on existing timestamps and is the missing half of a scorecard system the industry has run for decades in one direction. Its first effect is diagnostic and internal — facilities find fixable patterns — and its larger effect is on the capacity market, where a facility that treats drivers well should be able to demonstrate it.
