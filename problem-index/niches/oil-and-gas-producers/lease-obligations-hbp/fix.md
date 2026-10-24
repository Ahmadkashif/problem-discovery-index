# The Shut-In Payment Nobody Calendared

**Niche:** [[niches/oil-and-gas-producers/lease-obligations-hbp/profile|Lease Obligations & HBP Tracking]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Fix (Pain Point)
**One-liner:** A gas well is shut in for a pipeline outage or low prices, the lease's shut-in royalty clock starts, and nobody in land hears about it.
**Tags:** #change-point-detection #feature-engineering #workflow-orchestration #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep every signed lease in force until the operator chooses to release it, and whoever loses the fewest net acres to a missed rental, shut-in payment or continuous-development deadline takes the account.

## The Problem
Production shuts a well in; land is not told. Many leases require a shut-in royalty payment within a set period (often 60 or 90 days, estimate) to keep the lease alive without production. Missing it invites a claim that the lease terminated.

## Why It's Still Broken
Shut-in status is an operations event recorded in the production system, while the payment obligation sits in a land record, and no one connects them.

## What a Fix Looks Like
Watch monthly and daily production for wells going to zero, map each well to the leases it holds, compute the shut-in payment deadline from each lease's clause, and send land a task with the amount and payees before the deadline.

## Who Feels the Pain
Lease analysts, land managers and the legal team defending lease termination claims.

## Impact If Fixed
Automating a single alert removes one of the most common ways a producing lease is lost. With gas shut-ins frequent during price dips, an operator with ~500 gas wells (estimate) may face dozens of shut-in clocks a year.
