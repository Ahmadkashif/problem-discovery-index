# Ad Decisioning Practice

**Niche:** [[niches/audio-adtech-networks/insertion-decisioning/profile|Insertion Decisioning]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Display and video ad decisioning optimises jointly across inventory, user and objective, and audio fills slots in priority order.
**Tags:** #convex-optimization #gradient-boosting #optimization-fundamentals #evaluation-metrics #confidence-intervals #dynamic-programming #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide which advertisement goes into which slot of which episode for which listener — and whoever optimises that properly extracts more value from the same inventory than anyone bidding harder can.

## The Problem
Ad decisioning is a developed engineering discipline. Publisher ad servers and exchanges optimise across guaranteed and non-guaranteed demand, forecast delivery, allocate impressions to meet commitments while maximising yield, apply frequency and competitive separation rules, and do it in milliseconds. The theory and the implementations are mature. Audio serving has the same infrastructure capability and asks it to apply a priority list.

## What Already Exists
Yield optimisation across guaranteed and non-guaranteed demand; delivery pacing against commitments; frequency and competitive separation logic; real-time candidate ranking; and forecast-aware allocation.

## The Customization Gap
The adaptation is to a linear listening experience with a finite tolerance. It requires: (1) position within a linear piece of content as a decision variable, since a display page has slots and an episode has a timeline where earlier is more heard — this positional dimension has no display analogue and is where the largest gains are; (2) exposure probability varying by position, so the value of a slot is not fixed and must be modelled rather than assumed; (3) listener tolerance as a scarce resource shared across shows and sessions, which display handles crudely as frequency and which matters far more in a linear medium; (4) host-read inventory competing for the same tolerance while being sold through a different process entirely; and (5) back-catalogue inventory where the same episode is served indefinitely, so a decision made today applies to listeners for years.

## Target Customer
Audio platforms and ad servers, publisher yield teams, and ad decisioning vendors for whom linear audio is an unserved format.

## Impact If Solved
The infrastructure is mature and audio asks it to apply a priority list. Position within a linear timeline as a decision variable has no display analogue, and listener tolerance shared across shows is a scarce resource display handles crudely.
