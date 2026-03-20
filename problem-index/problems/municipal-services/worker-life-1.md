# Public Works Crew Route Inefficiency

**Industry:** [[municipal-services|Municipal Services]]
**Type:** Worker Life Changing
**One-liner:** Crew leaders get back 60-90 minutes per day currently lost to backtracking, idle drive time, and dispatches that ignore geographic clustering — time that translates directly to fewer unpaid overtime hours and less physical exhaustion.
**Tags:** #markov-decision-processes #dynamic-programming #policy-gradient-methods #gradient-boosting #linear-regression #feature-engineering #evaluation-metrics #optimization-fundamentals #worker-facing

## The Problem
Public works crews — street repair, water/sewer maintenance, sign installation, mowing, snow plowing — start each day with a work order list that was sequenced by priority or entry date, not geography. A three-person street patch crew might drive from the north end of town to the south, back north for a priority fill, then west for another — covering 80 miles in a day when a geographically optimized route would cover 35. Crew leaders manually resequence on the fly, but they lack real-time visibility into which jobs were added mid-shift, which were closed by another crew, or which require equipment they do not currently have on the truck. The result is 2-3 hours of windshield time per 8-hour shift, meaning the crew that is supposed to fill 15 potholes fills 9.

## Why It Matters to the Worker
Public works crew members are hourly employees, often starting at $16-22/hour, doing physically demanding work in heat, cold, and traffic. Every hour spent driving instead of working extends their day — many crews regularly hit 9-10 hour days not because there is too much work but because the routing wastes time. The exhaustion compounds: a fatigued crew working near traffic in the last hour of an extended shift is a safety risk. Crew leaders carry the mental load of resequencing on paper or in their heads while also supervising active work zones, which is a constant low-grade cognitive burden that degrades decision quality throughout the day.

## What a Solution Looks Like
A tablet-based routing app that ingests the day's work orders, clusters them geographically, sequences them accounting for equipment on the truck, time-of-day traffic patterns, and real-time additions/cancellations from dispatch. A reinforcement learning model continuously re-optimizes as the day progresses — when a new emergency work order drops in, it recalculates whether to divert now or batch it with a nearby cluster later. The crew leader sees a map with a suggested next-stop sequence and estimated completion time, not a spreadsheet of addresses.

## Impact If Solved
Crews complete 30-40% more work orders per shift at the same headcount, overtime drops by 15-20%, and vehicle fuel/maintenance costs decrease proportionally. For the individual worker, it means finishing the list by 3:30 instead of 5:15, going home to their family on time, and not carrying the stress of an impossible routing puzzle in their head all day.
