# The Broken Aggregation Found at the Distributor

**Niche:** [[niches/contract-packagers/commercial-drug-packaging-serialisation/profile|Commercial Drug Packaging & Serialisation]]
**Industry:** [[industries/contract-packagers|Contract Packagers]]
**Type:** Fix (Pain Point)
**One-liner:** A case is reworked on the line, the aggregation is never updated, and the mismatch surfaces weeks later when a wholesaler scans it.
**Tags:** #graph-theory #evaluation-metrics #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a sponsor's bulk batch into serialised, QA-released commercial packs without a labelling deviation, and whoever releases the most lots right first time at the lowest cost per serialised pack takes the account.

## The Problem
Manual rework — opening a case to replace a damaged unit, pulling extra samples, re-palletising — is where aggregation data and physical goods drift apart. Downstream trading partners verify identifiers, and a mismatch triggers a query back through the sponsor to the packager, who must find the lot, the shift and the rework record.

## Why It's Still Broken
Rework happens off the main line, often with handheld scanners whose events are uploaded later, and nothing checks the lot hierarchy as a whole before shipment.

## What a Fix Looks Like
A pre-shipment consistency check run on every lot: every container's contents scanned or inferred, every decommissioned serial accounted for, and any rework without matching events flagged before the pallet leaves.

## Who Feels the Pain
Serialisation coordinators answering sponsor queries; sponsors answering wholesalers; QA reopening closed lots.

## Impact If Fixed
Data errors caught in the plant rather than in the supply chain, and fewer post-shipment investigations.
