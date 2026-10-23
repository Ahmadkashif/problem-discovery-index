# The Split Package Nobody Sees Lost

**Niche:** [[niches/plumbing-and-hvac-distributors/commercial-plumbing-mechanical-supply/profile|Commercial Plumbing & Mechanical Project Supply]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** A house quotes the whole package, wins the fixtures and loses the PVF, and records the job as won.
**Tags:** #k-nearest-neighbors #logistic-regression #feature-engineering #data-integration #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to win the mechanical or plumbing contractor's material package on a commercial job, but contractors routinely split that package, and the two halves are won differently: the equipment and fixtures go to whoever re-selects the engineer's schedule in its own lines and gets the substitutions approved, and the pipe, valves and fittings go to whoever holds the lowest firm price across a release schedule that runs for months while copper and PVC move. Decomposed into contested sub-niches below.

## The Problem
When the first fixture release ships, the job is marked won. Months later the PVF manager notices that the copper and cast-iron releases never came: the contractor bought them elsewhere on a better hold. Nobody records which half was lost or why, so the next quote repeats the same price and terms.

## Why It's Still Broken
Win and loss are recorded per quote, not per package line group, and the PVF and fixture desks often quote the same job separately without a shared record.

## What a Fix Looks Like
Split every commercial quote into package halves at creation, track releases per half against the quoted quantities, and flag a half as likely lost when its expected releases don't arrive within the job's schedule. Ask the outside salesperson one question when the flag fires: price, hold terms, availability or relationship.

## Who Feels the Pain
PVF managers pricing blind, commercial sales managers reporting inflated hit rates, and quote desks re-quoting contractors they never win PVF from.

## Impact If Fixed
If ~20–40% of "won" commercial jobs are partial wins (estimate), measuring which half was lost tells the house whether its problem is selection or price, and stops ~5–10% of quote-desk effort going to halves it never wins.
