# Six Brands, One Line, No Sequencing

**Niche:** [[niches/restaurant-tech-platforms/ghost-kitchen-commissary/profile|Commissary & Ghost Kitchen Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A multi-brand kitchen receives orders for six virtual restaurants into six separate ticket streams and the cooks sequence them by eye, so the line's throughput is set by whoever is shouting and every brand's delivery times suffer equally.
**Tags:** #dynamic-programming #optimization-fundamentals #time-series-forecasting #evaluation-metrics #workflow-orchestration #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in shared kitchen software is fighting to allocate capacity, labour and cost across brands sharing one kitchen in a way the tenants will accept as fair — and whoever makes the allocation defensible takes the facility.

## The Problem
Six virtual brands share a line and a kitchen display for each. Tickets arrive independently, each with its own promised delivery time and a driver already dispatched or about to be. The cooks work from whichever screen is loudest, meaning newest or most complained-about. Items that share equipment are cooked separately because nobody can see across brands. Orders sit finished while their drivers are ten minutes away and others are late because a driver arrived early. The line's effective capacity is well below what the equipment allows, and the loss is entirely in sequencing.

## Why It's Still Broken
Kitchen display systems model one restaurant, which is a reasonable assumption everywhere except here. Each brand may be on a different point of sale instance or a different marketplace integration, so consolidating the streams means crossing system boundaries no vendor has an incentive to cross. And the operators, mostly young companies under financial pressure, have solved it with more screens because more screens is what the market sells.

## What a Fix Looks Like
One sequence, across all brands, computed against the actual constraints. Consolidate every brand's tickets into a single ordered queue for the line, sequenced by promised time, driver arrival estimate, and cooking interdependence — batching items that share a fryer or an oven regardless of which brand they belong to is the single largest throughput gain available and is impossible without a consolidated view. Show the line what to start next rather than six lists of what is outstanding. Feed driver arrival estimates from the marketplaces, which provide them, so food is finished when transport is present rather than ten minutes before or after. Measure per-brand promised-versus-actual so that the allocation question and the operations question stay connected: a brand that is consistently late because its items collide with another's peak is a portfolio fact, not a kitchen failure.

## Who Feels the Pain
Cooks working from six screens with no priority; brands whose delivery times suffer for reasons inside someone else's order flow; and operators whose line capacity is materially below its equipment capacity for want of a queue.

## Impact If Fixed
Consolidated sequencing with batching typically lifts effective line throughput substantially at zero capital cost, which in a business whose economics depend on fitting more brands onto one line is the central lever. Aligning finish time to driver arrival also directly improves food quality at the customer, which is the segment's most persistent complaint.
