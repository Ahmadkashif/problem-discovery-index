# The Furniture Order Locked in the Dealer's File

**Niche:** [[niches/interior-design-firms/corporate-workplace-interiors/profile|Corporate Workplace Interiors]]
**Industry:** [[industries/interior-design-firms|Interior Design Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The designer's furniture plan and the dealer's order drift apart, and the difference is found on install day.
**Tags:** #feature-engineering #k-nearest-neighbors #evaluation-metrics #data-integration #workflow-orchestration #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to win the occupier's fit-out commission, but the contest splits in two: before a lease is signed, firms compete to produce a test fit and a credible budget for each candidate building fastest; after occupancy, they compete to prove with measured utilisation how much space and what mix the occupier needs. Different clocks, buyers and winners. Decomposed into contested sub-niches below.

## The Problem
The designer issues a furniture plan; the dealer's designer rebuilds it in CET Designer to produce the bill of materials and SIF order file. Revisions happen on both sides — a finish change here, a workstation count there — and nobody compares the order to the current plan line by line.

## Why It's Still Broken
The order data sits in the dealer's CET file and order system, which the interior designer does not see, and CET's manufacturer extensions encode configuration rules the designer's drawing tools do not.

## What a Fix Looks Like
Ingest the dealer's SIF or BOM export and the designer's current furniture schedule, match them by location and product, and report differences in count, model, finish and fabric before the order is released.

## Who Feels the Pain
Interior designers, dealer project managers, and occupiers who pay for re-orders and delayed move-ins.

## Impact If Fixed
Mismatches are caught before release rather than at install, avoiding re-orders that typically add weeks of lead time.
