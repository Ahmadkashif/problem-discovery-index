# The vMVPD That Counts by Billing Address

**Niche:** [[niches/broadcast-stations/retrans-subscriber-audit/profile|Retrans Subscriber Reporting & Fee Audit]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Fix (Pain Point)
**One-liner:** A virtual distributor reports subscribers by billing zip while the agreement counts subscribers who can receive the station in its market, and nobody at the station checks which rule produced the number.
**Tags:** #feature-engineering #descriptive-statistics #hypothesis-testing #quick-win #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche (contract audit firms, royalty-management vendors and in-house distribution finance teams) is fighting to test every distributor's reported subscribers, system by system, against an independent estimate of what each system should report, and whoever finds the shortfalls earliest and most completely takes the account.

## The Problem
Virtual distributors deliver local stations by the viewer's location, but report and pay on whatever geographic rule their systems use (estimate). Travelling subscribers, second homes and zip codes that straddle DMAs all move counts in ways no one examines.

## Why It's Still Broken
The station receives a total, not the method, and the contract language on counting is rarely translated into a test.

## What a Fix Looks Like
For each vMVPD agreement, write the counting rule as a checkable definition. Request the zip-level report the agreement allows, compare it with the station's DMA zip list each quarter, and raise discrepancies with evidence.

## Who Feels the Pain
Distribution finance staff, and stations in markets with large border populations.

## Impact If Fixed
A quarterly zip-level check closes a recurring leak without a full audit.
