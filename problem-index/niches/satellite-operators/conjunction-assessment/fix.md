# Manoeuvre Coordination by Email to an Address in a Catalogue

**Niche:** [[niches/satellite-operators/conjunction-assessment/profile|Conjunction Assessment & Collision Avoidance]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Fix (Pain Point)
**One-liner:** When two active satellites are predicted to come close, their operators decide who moves by finding each other's contact details and emailing, sometimes hours before closest approach.
**Tags:** #workflow-orchestration #compliance #automation #large-language-models #quick-win
**Contested on:** Every serious competitor in this niche is fighting to tell an operator, before the manoeuvre deadline, which of its conjunction warnings are real, and whoever does it with the fewest false alarms and no missed events takes the operator's screening account.

## The Problem
If both objects can manoeuvre, both operators might move — into each other — or neither might. They need to agree who moves and share the planned trajectory. Contact lists are maintained loosely; replies depend on who is on shift in another time zone.

## Why It's Still Broken
There is no mandatory, machine-readable channel for manoeuvre intent between operators; national regulators require coordination but not a format; and the volume was low until mega-constellations made it constant.

## What a Fix Looks Like
A coordination workflow attached to each conjunction event: automatic notification of the other operator through a registered endpoint, structured exchange of planned manoeuvres and ephemerides, agreed rules for who moves by default, and a timestamped record for regulators and insurers.

## Who Feels the Pain
Flight dynamics analysts on shift; smaller operators facing large constellations; regulators reconstructing events afterwards.

## Impact If Fixed
Hours of uncertainty before an encounter reduced to minutes, and no more cases where both satellites move into the same space.
