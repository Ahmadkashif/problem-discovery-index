# One Tract Record From Runsheet to Lease Release

**Niche:** [[niches/oil-and-gas-producers/mineral-title-lease-administration/profile|Mineral Title & Lease Administration]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Title research, lease terms and division-order decimals for the same tract live in three places, and the links between them are in people's heads.
**Tags:** #large-language-models #transformers #graph-theory #feature-engineering #data-integration #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor here is fighting to keep the operator's right to drill and produce intact. Two contests with different winners sit inside it. Before a well, the contest is building drilling title from county records, won by whoever's ownership schedules need the fewest corrections after first production. After the lease is signed, it is keeping leases alive, won by whoever loses the fewest net acres to a missed obligation. Decomposed into contested sub-niches below.

## The Problem
A tract's runsheet, the title opinion built from it, the leases taken on it, the units it was pooled into and the decimals paid from it are created by different people at different times. When a lease is amended or an heir appears, each record is updated separately, if at all, and inconsistencies surface as suspended revenue, top leases or title failures.

## Why Nobody Has Built This
Land software was built around lease records and accounting software around decimals. Title work is done by outside landmen and attorneys whose output is a PDF opinion, not data.

## What to Build
A tract graph that links each recorded instrument, ownership interest, lease, unit and decimal, with the document and clause behind each link. Extraction models populate it from runsheets, opinions and leases, and a change to any node, such as a new probate order, shows which leases, units and owner decimals it affects.

## Target Customer
VPs of land and division-order managers at operators with thousands of tracts.

## Impact If Built
If ~10% of division-order changes today trace to stale land records (estimate), linking the records could cut suspense created by title mismatches by a similar share, and give an acquirer's diligence team one auditable record per tract.
