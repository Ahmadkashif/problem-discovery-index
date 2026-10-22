# Ten Years of Test Results in Ten Incompatible Workbooks

**Niche:** [[niches/contract-research-labs/joint-industry-consortia/profile|Joint Industry Programmes & Research Consortia]]
**Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Type:** Fix (Pain Point)
**One-liner:** Each year's programme results were recorded by a different engineer in a different workbook, so the consortium's most valuable asset — its long run of data — cannot be analysed as one.
**Tags:** #large-language-models #feature-engineering #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to produce pre-competitive test data no single member could afford to generate alone, and whoever turns each year's results into data members can drop straight into their own design and qualification decisions gets the renewals.

## The Problem
Column names change, units change, specimen identifiers are reused, and test conditions are written in notes rather than fields. When members ask for a trend across the programme's history, staff spend weeks reconciling workbooks.

## Why It's Still Broken
No one owns the programme's data model across years, and the engineer who knew what a column meant has moved on.

## What a Fix Looks Like
A one-time harmonisation: LLM-assisted mapping of every historical workbook's columns and notes into a single schema, reviewed by programme staff, with units normalised and specimen identities resolved; then a template that keeps new results in that schema from the day they are recorded.

## Who Feels the Pain
Programme engineers asked for cross-year analyses; members who cannot use history; directors whose renewal pitch depends on the long run of data.

## Impact If Fixed
The programme's history becomes queryable, cross-year analyses take hours rather than weeks, and the data asset members pay for is finally usable as one.
