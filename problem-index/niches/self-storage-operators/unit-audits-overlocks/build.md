# A Mismatch Queue From Locks, Gates and the Ledger

**Niche:** [[niches/self-storage-operators/unit-audits-overlocks/profile|Unit Audits, Overlocks & Facility Walks]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Stores with smart locks and gate logs already know which doors disagree with the ledger, but nothing reads the three records together, so the manager still walks every door.
**Tags:** #hidden-markov-models #change-point-detection #feature-engineering #evaluation-metrics #worker-facing #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to make every door match the ledger, and whoever recovers the most rent lost to ledger-door mismatches per store takes the account.

## The Problem
A unit marked vacant had its door opened twice last week. A unit marked rented has not been entered in 14 months, and its autopay failed. An overlocked unit shows motion inside. Each is visible in the lock vendor's cloud, the gate system or the ledger, but no one joins them. The manager finds these on the walk, weeks later, or not at all.

## Why Nobody Has Built This
The three records belong to three systems: lock vendor, access-control vendor and facility software. They are integrated only for the basic task of opening the door. Lock vendors sell hardware and access; facility software sells rent collection. The mismatch is nobody's product.

## What to Build
A per-unit state model. A hidden Markov model infers each unit's true state (in use, being emptied, dormant, vacant but occupied, overlock breached) from daily door, gate and motion events, and compares it with the ledger status. Change-point detection flags a unit being emptied ahead of a move-out. The output is a short daily queue of doors to check, ranked by rent at risk, with the evidence and a one-tap result the manager records at the door. Confirmed results become labels.

## Target Customer
VPs of operations at operators with smart locks across much of their portfolio; lock and access-control vendors adding analytics.

## Impact If Built
If a 600-unit store carries ~3–8 rent-losing mismatches at any time (estimate) at ~$100–150 a month each, finding them a month sooner recovers ~$4,000–14,000 a year per store. The manager's walk shrinks to a queue.
