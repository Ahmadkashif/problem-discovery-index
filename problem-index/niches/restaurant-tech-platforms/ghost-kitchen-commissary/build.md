# A Unit of Account for Shared Kitchen Capacity

**Niche:** [[niches/restaurant-tech-platforms/ghost-kitchen-commissary/profile|Commissary & Ghost Kitchen Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Shared kitchens sell time, consume equipment and labour, and have never defined what a unit of their capacity is, so every allocation of cost and every decision about who gets Tuesday morning is a negotiation.
**Tags:** #optimization-fundamentals #dynamic-programming #combinatorics-and-counting #evaluation-metrics #confidence-intervals #descriptive-statistics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in shared kitchen software is fighting to allocate capacity, labour and cost across brands sharing one kitchen in a way the tenants will accept as fair — and whoever makes the allocation defensible takes the facility.

## The Problem
A commissary rents to fourteen food businesses. One uses the combi oven for six hours and no other equipment; another uses three prep tables, the mixer and the walk-in all day. Both are billed by the hour. The facility does not know which is profitable, what its actual constraint is — usually one piece of equipment or one part of the cold chain rather than floor time — or how to price the Tuesday morning slot everyone wants against the Sunday night nobody does. When a tenant asks for more time, the answer comes from the calendar rather than from any understanding of what capacity remains.

## Why Nobody Has Built This
The segment is small, young and financially unstable, which has kept serious product investment away, and the operators that have built internal tools have built booking systems because booking is the visible transaction. Defining a capacity unit requires modelling the kitchen as a set of constrained resources with tenant-specific consumption patterns, which is production planning — a discipline that exists thoroughly in manufacturing and has never been brought into food service at this scale. The allocation question also has a political dimension: a facility that starts charging by actual resource consumption will redistribute cost between tenants, and some of them will pay more.

## What to Build
A resource model of the facility — stations, major equipment, cold and dry storage, loading and wash capacity — with each tenant's consumption measured rather than assumed. Consumption comes from booking plus observed use: equipment run time where it can be instrumented cheaply, station occupancy, storage footprint. From that, capacity is expressed per constrained resource rather than as floor hours, which immediately shows the facility what its actual bottleneck is and usually surprises it. Scheduling becomes an allocation against those constraints, and pricing can reflect scarcity — the Tuesday morning combi oven slot is genuinely worth more than Sunday night floor time and no facility currently prices it that way. For the multi-brand ghost kitchen case the same model allocates shared labour and overhead to brands by measured consumption, which is what turns per-brand profitability from an argument into a number.

## Target Customer
Commissary and shared-use kitchen operators, food business incubators, and multi-brand virtual restaurant companies allocating shared cost across brands.

## Impact If Built
A facility that knows its constrained resource can sell more of it and stop selling the wrong thing, which typically raises utilisation without capital expenditure. For multi-brand operators, measured per-brand cost is the difference between knowing which brands to keep and guessing, and the guessing has been expensive for that segment. Defensible allocation also changes the tenant relationship from a recurring argument into a published method.
