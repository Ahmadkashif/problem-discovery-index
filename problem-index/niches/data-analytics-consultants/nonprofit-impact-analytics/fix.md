# Beneficiary Data Linkage Across Programs

**Niche:** [[niches/data-analytics-consultants/nonprofit-impact-analytics/profile|Nonprofit Impact Analytics]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Nonprofits cannot tell how many unique individuals they serve because the same person appears as "John Smith" in workforce development, "Johnathan Smith" in housing, and "J. Smith" in food assistance — with no common identifier across programs.
**Tags:** #data-integration #tabular-ml #quick-win

## The Problem
A community action agency reports serving 15,000 individuals across 8 programs. But when an analytics consultant attempts to deduplicate across programs, the actual number of unique individuals is 8,500 — many participants access multiple programs. The overcounting matters: cost-per-individual metrics are inflated, funder reports overstate reach, and the organization cannot identify multi-program participants who might benefit from coordinated case management. The deduplication is manual because each program uses a different database with no shared identifier — names are spelled differently, addresses change, phone numbers vary, and some programs collect SSN while others do not.

## Why It's Still Broken
Nonprofits serve vulnerable populations who may not have consistent identification (homeless individuals, undocumented immigrants, people with name changes). Creating a universal beneficiary ID requires either collecting government ID (which many beneficiaries resist or lack) or implementing a probabilistic matching system that links records based on name similarity, date of birth, and partial address. Program staff are not trained in data quality practices — they enter names inconsistently and do not follow standard data entry protocols. Past deduplication efforts produce false matches (linking two different "Maria Garcia" records) that damage trust in the data.

## What a Fix Looks Like
A beneficiary matching tool designed for nonprofit data quality realities that: (1) accepts exports from multiple program databases with different schemas, (2) performs probabilistic matching on name (with common nickname resolution — "John" = "Johnathan" = "Jon"), date of birth, partial address, and phone number, (3) presents potential matches for human review with confidence scores (high confidence auto-links, low confidence requires staff confirmation), (4) assigns a cross-program beneficiary ID that persists across data refreshes, (5) handles sensitive populations appropriately (configurable matching rules for populations that may share addresses or have name variations), and (6) produces a deduplicated beneficiary roster with program participation history.

## Who Feels the Pain
Analytics consultants who spend 2-3 weeks per engagement on manual beneficiary deduplication, and nonprofit executives who report inflated service numbers to funders because they cannot deduplicate across programs.

## Impact If Fixed
Produces accurate unique beneficiary counts — typically 30-40% lower than undeduplicated counts — enabling honest impact reporting. Identifies multi-program participants for coordinated case management, improving outcomes. Saves 2-3 weeks of consultant time per engagement on deduplication work.
