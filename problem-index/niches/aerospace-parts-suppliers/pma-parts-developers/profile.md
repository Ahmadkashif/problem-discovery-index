# PMA Parts Developers & Reverse-Engineering Teams

**Parent Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to get a high-demand part through FAA Parts Manufacturer Approval before the OEM's aftermarket price moves, and whoever turns a teardown into an accepted test-and-computation package in the fewest months takes the account.

## Profile
**Market Size:** ~$300M a year in engineering, testing and certification spend on new PMA development by US independent parts makers (estimate)
**Share of Parent Industry:** ~0.4% of the two codes' receipts in development spend; the PMA parts themselves sell for much more (estimate)
**Digital Adoption:** Medium-low — CAD and metrology are digital; the substantiation package is assembled by hand from tests, analyses and reports
**Target Buyer:** VP Engineering or PMA programme manager at independent replacement-part makers
**Automation Potential:** Medium for package assembly and part selection; low for the engineering judgement behind equivalence

## What Makes This a Distinct Niche
A PMA lets an independent maker produce a replacement for an OEM part under FAA approval, usually at a lower price. HEICO, the largest, has ~20,000 PMA parts and adds ~400–550 a year; its Flight Support Group was 70% of FY2025 sales. Each PMA starts with picking a part where demand and OEM price justify the work, then reverse engineering (teardown, dimensional and material analysis), then a test-and-computation package proving equivalence that FAA engineers or designees review, then a production quality system. The engineers doing this work are served by CAD and PLM tools built for designing new parts, not for proving a copy equals an original. Installation and repair of PMA parts belong to [[industries/aircraft-mro-shops|Aircraft MRO Shops]] and distribution to the queued aviation parts distributors; this niche is design, approval and production.

## Current Tools & Gaps
CAD, CMM and CT scanning, materials labs, PLM and document control. The gaps: part selection from scattered demand and price signals, no structured library of past substantiation arguments, and package assembly by hand. The engineering consultancies that help are logged in Pass 2 below.

## Problems
- [[niches/aerospace-parts-suppliers/pma-parts-developers/build|🔨 Build: A Substantiation Workbench for Teardown to Approval]]
- [[niches/aerospace-parts-suppliers/pma-parts-developers/buy|🛒 Buy: PLM Adapted to Equivalence, Not Design]]
- [[niches/aerospace-parts-suppliers/pma-parts-developers/fix|🔧 Fix: Picking the Next PMA From a Spreadsheet]]
