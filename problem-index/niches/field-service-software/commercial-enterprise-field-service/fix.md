# The Response Time Commitment Nobody Models

**Niche:** [[niches/field-service-software/commercial-enterprise-field-service/profile|Commercial & Enterprise Field Service]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** Service contracts promise response times, the organisation staffs to meet them by feel, and nobody has ever computed the probability of meeting a four-hour commitment in a given region with a given technician count.
**Tags:** #monte-carlo-methods #survival-analysis #confidence-intervals #evaluation-metrics #descriptive-statistics #hypothesis-testing #optimization-fundamentals #compliance
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A contract commits to a four-hour on-site response. The region has nine technicians covering a territory with a given density of covered machines. Whether the commitment is met depends on call arrival timing, technician availability, travel distance and job duration — a queueing problem with a computable answer. Instead, the service director staffs from last year plus a judgement, misses commitments in bad weeks, pays penalties or absorbs escalations, and over-staffs in regions where the risk was never real. Sales, meanwhile, sells response commitments without any figure for what each one costs to support.

## Why It's Still Broken
Nobody owns the question across the boundary it sits on: sales commits, operations staffs, finance sees the penalty. The modelling is unremarkable — arrival rates, service times and travel distributions feeding a simulation — and is nobody's job description in a service organisation. And the data required is spread across the contract system, the dispatch history and the geography, which is the usual reason a computable thing stays uncomputed.

## What a Fix Looks Like
Simulate it. Call arrivals by region and machine population, travel time distributions from actual dispatch history rather than from straight-line distance, and job durations from realised data feed a simulation that returns the probability of meeting each commitment level at each staffing level. That gives three things nobody currently has: a defensible staffing plan per region, a price for each response tier that sales can quote against, and an early warning when a region's machine population has grown past what its technician count can support. Report attainment continuously against the modelled expectation, so a miss is interpretable — bad luck in a heavy week, or a structural shortfall. None of this needs new data collection; it needs the dispatch history treated as a measurement of the service process rather than as a log.

## Who Feels the Pain
Technicians absorbing the gap between a commitment and a staffing level, usually by working late; service directors defending misses they could have predicted; and customers on contracts whose response tier was never supportable in their region.

## Impact If Fixed
Staffing to a modelled attainment probability rather than to last year's headcount corrects both over- and under-staffing, and the per-region commitment cost is the number that lets a service organisation price response tiers deliberately instead of giving them away. The simulation is a week of work on data already collected.
