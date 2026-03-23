# Automated ONIX Metadata Cleanup and Enrichment

**Niche:** [[niches/independent-publishers/backlist-catalog-managers/profile|Backlist Catalog Managers]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Firebrand Title Management stores ONIX records but doesn't flag the 40% of backlist records that are missing descriptions, have wrong BISAC codes, or lack keywords — directly depressing discoverability and sales.
**Tags:** #bert #text-classification #nlp #automation #revenue-impact

## The Problem
A publisher's oldest backlist titles — often the most commercially valuable — have the worst metadata. Books published in the early 2000s may have ONIX records with no description, no keywords, outdated BISAC codes (the taxonomy changes every 5 years), no contributor bio, and no series information. This metadata goes to every retailer and library: Amazon, Barnes & Noble, Ingram, EBSCO. A book with no description on Amazon gets no organic search traffic. A book with the wrong BISAC code is shelved in the wrong category. A book missing series information doesn't show up in "books in this series" recommendations. The publisher knows the metadata needs updating but has 400 records to audit and fix — a 200+ hour project nobody has time for.

## What Already Exists
Firebrand Title Management, Consonance, and Bibliocloud manage ONIX metadata creation and distribution. These tools make it easy to enter and export metadata but don't analyze the existing catalog for quality issues. Data quality tools (Schematron-based ONIX validators) check for structural compliance but not content quality — they'll tell you a description field exists but not that it's only 15 words long (the minimum for Amazon to display it prominently). No tool auto-generates missing metadata components using the book's content, cover, and existing partial records.

## The Customization Gap
A backlist metadata enrichment tool needs to: (1) audit the entire catalog for metadata quality issues (missing descriptions, short descriptions, outdated BISAC codes, missing keywords, no series linkage, no contributor ORCID), (2) prioritize fixes by sales impact (a backlist title selling 200 copies/year with bad metadata is higher priority than one selling 10), (3) auto-generate draft descriptions, keywords, and BISAC suggestions using the book's existing metadata, cover text, and table of contents (or full text if available), (4) present proposed fixes for human review and approval, and (5) push corrected records to distribution partners via ONIX. The tool must understand publishing metadata standards deeply enough to generate records that actually improve discoverability, not just fill empty fields.

## Target Customer
Operations directors and metadata specialists at publishers with 200+ backlist titles and declining backlist discoverability.

## Impact If Solved
Enriching metadata for the worst 20% of backlist records (80 titles for a 400-title catalog) increases their collective sales by 15–30%, recovering $30K–$100K in annual revenue that was lost to invisibility. Reduces metadata audit and correction time from 200+ hours to 20 hours through automated analysis and draft generation.
