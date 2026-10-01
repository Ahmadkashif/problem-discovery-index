# The Same Fund Under Four Names

**Niche:** [[niches/financial-data-vendors/private-markets-data/profile|Private Markets Data]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A fund appears as its legal name, its marketing name, a feeder vehicle and a pension's abbreviation, and the database holds four partial records.
**Tags:** #graph-theory #graph-neural-networks #k-nearest-neighbors #evaluation-metrics #data-integration #quick-win
**Contested on:** Not terminal as stated — competitors are fighting either to find and resolve every private financing round and valuation first, or to hold accurate cash-flow-level performance for the most private funds; different sources, buyers and winners, stated separately in the sub-niches.

## The Problem
Pension disclosures abbreviate, GPs rebrand, continuation vehicles inherit assets, and parallel and feeder funds share a strategy. Duplicate and split entities corrupt performance aggregation and peer groups.

## Why It's Still Broken
Entity resolution is done record by record when a researcher notices, and false merges are feared more than duplicates.

## What a Fix Looks Like
Graph-based resolution over names, managers, vintages, commitments and co-investors; merge proposals with evidence for researcher approval; separate handling of fund families so parallel vehicles are linked, not merged.

## Who Feels the Pain
Researchers, and clients whose benchmarks double-count or miss funds.

## Impact If Fixed
Cleaner entity graphs improve every downstream aggregate at once.
