# The Fight: The Alarm That Went Silent

**Origin:** [[origins/electric-utilities/profile|Electric Utilities]]
**Outcome:** Not a competitor beaten — a system beaten by its own software, at a cost of roughly 50 million people losing power.

## Why This Origin's Fight Is Different

American Airlines had a rival. Electric utilities, as regulated monopolies, mostly do not. The fight here is not firm-versus-firm — it is **the fight to keep a computed model of the network faithful to the real network, in real time, and what happens when that fight is lost without anyone noticing it was being fought.**

**August 14 2003** is the case: an official bi-national task force report exists, which is rarer than it should be for events of this scale.

## What Happened, Mechanically

Ohio was hot, load was high, and several 345kV transmission lines operated by FirstEnergy sagged into trees and tripped over the afternoon — an unremarkable category of event that grids are built to absorb, provided operators see it and redistribute load in response.

The problem was that FirstEnergy's control-room operators **did not see it.** The energy management system in use, General Electric's **XA/21**, contained a software defect: a **race condition** in the alarm and event-processing subsystem, where two processes contended for access to a shared data structure. Under a high volume of near-simultaneous events, the condition triggered a loop that **silently disabled the alarm system** — it did not crash visibly, it simply stopped telling anyone anything was wrong.

Operators kept working a control room that looked calm. Lines kept tripping. Nobody redistributed load, because nobody knew redistribution was needed. The local, ordinary event that grids handle routinely instead cascaded across the northeastern United States and Ontario, cutting power to an estimated **50 million-plus people** — the largest blackout in North American history to that point.

GE's own post-incident code audit found the race condition; the company distributed a fix to more than 100 other utility customers within a day of confirming it.

## The Honest Correction

**This event is very commonly mischaracterised as a grid-overload or capacity failure — "too much demand for too little supply." The record does not support that.**

The physical trigger — trees, sagging lines, a hot afternoon — was ordinary and manageable on its own. The disqualifying failure was informational: **the control room lost situational awareness because its own alarm software silently stopped working**, and decisions that would have been routine with visibility became impossible without it. The blackout is a systems-failure case, not a capacity-shortage case, and an episode that tells it as the latter is teaching the wrong lesson.

## What Survives the Correction

The transferable point: **the most dangerous failure in a monitoring system is not the one that crashes loudly — it is the one that goes silent while looking fine.** An operator trusting a dashboard that has quietly stopped updating is worse off than an operator with no dashboard at all, because the no-dashboard operator knows to be careful.

Every FDE who ships a monitoring layer, an alerting pipeline or an "everything's green" status page is one race condition away from repeating this, at whatever scale their system operates.

**Sources:** U.S.–Canada Power System Outage Task Force, *Final Report on the August 14, 2003 Blackout* (April 2004); The Register, *Software bug blamed for blackout alarm failure* (Feb 2004) and *Tracking the Blackout bug* (April 2004); NBC News, coverage of the GE XA/21 root-cause finding.
