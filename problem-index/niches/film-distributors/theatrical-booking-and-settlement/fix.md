# Grosses Reconciled After the Invoice Goes Out

**Niche:** [[niches/film-distributors/theatrical-booking-and-settlement/profile|Theatrical Booking & Settlement]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** The distributor invoices film rent on the exhibitor's reported gross and only notices it differs from the box office report when the producer's auditor asks.
**Tags:** #feature-engineering #gaussian-mixture-models #data-integration #automation #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to settle every engagement at the terms actually agreed within days of the run ending, and whoever settles fastest with the fewest write-downs keeps exhibitors booking its films and producers trusting its statements.

## The Problem
Exhibitors report grosses on their own statements, and the distributor also receives theatre-level box office reports. The two should agree. When they don't (a missed show, a comp-ticket policy, a late-reported day), the difference is small per engagement and rarely checked before settlement.

## Why It's Still Broken
The two sources come in different formats on different days, and the booker reconciling them is also negotiating the next release.

## What a Fix Looks Like
Automatic matching of exhibitor-reported grosses to box office reports by theatre and day, with every discrepancy over a threshold flagged before the settlement is agreed, and a summary per circuit of how often and how much its statements differ.

## Who Feels the Pain
Bookers and distribution accountants; producers whose participation rests on film rent; auditors who find the gap later.

## Impact If Fixed
Small shortfalls that add up across a wide run are caught while they can still be settled, and the distributor can show a producer its theatrical receipts were checked.
