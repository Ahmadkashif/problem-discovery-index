# Lanes Awarded to Carriers Who Never Run Them

**Niche:** [[niches/logistics-consultants/truckload-bid-routing-guide/profile|Truckload Bid Design & Routing Guide Performance]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Every annual bid awards some lanes to carriers whose network does not touch them, because the lowest rate wins and nobody checks whether the carrier has ever hauled there.
**Tags:** #descriptive-statistics #k-nearest-neighbors #feature-engineering #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to design truckload awards that carriers keep accepting when the spot market turns, and whoever's routing guides hold the highest primary tender acceptance through the contract year takes the account.

## The Problem
In a soft market, carriers bid aggressively on lanes outside their networks to win volume. The award optimiser picks the lowest rate, and the routing guide makes that carrier primary. When the market tightens, those are the first lanes rejected, and the shipper learns which awards were speculative from its spot bill.

## Why It's Still Broken
Bid responses carry a rate, not evidence of operation. Checking each carrier's footprint across hundreds of lanes by hand is impractical in the bid window, so the check is skipped.

## What a Fix Looks Like
A pre-award screen that scores each bid for network fit: the carrier's own history on the shipper's freight near that origin and destination, its stated terminal and capacity footprint, and acceptance on similar lanes. Low-fit bids are flagged for a capacity commitment or a backup award before the routing guide is loaded.

## Who Feels the Pain
Transportation analysts handling rejections; directors whose savings evaporate in the first tight quarter; carriers who lose freight to bids that never move.

## Impact If Fixed
A screen that takes hours per bid removes the most predictable source of routing guide failure.
