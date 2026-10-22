# The Roster Spreadsheet Rebuilt Every Month

**Niche:** [[niches/health-insurance-carriers/provider-data-network-adequacy/profile|Provider Data, Directories & Network Adequacy]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Large groups send monthly rosters in their own spreadsheet layouts, and a plan analyst maps each one by hand before any change reaches the directory.
**Tags:** #large-language-models #transformers #data-integration #automation #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to keep each directory entry matching what the provider's office would say on the phone, within the No Surprises Act's 90-day verification cycle, and whoever's directory passes a regulator's secret-shopper sample with the fewest wrong listings takes the account.

## The Problem
A health system with 2,000 clinicians sends its roster as a spreadsheet with its own columns, abbreviations and conventions for adds, terms and moves, and the layout changes when its staff changes. The plan's analyst compares it with last month's, maps the columns, and keys or uploads the differences. Delays push updates past the two-business-day window.

## Why It's Still Broken
Plans cannot force hundreds of groups onto one template, and industry roster standards have been adopted slowly. Delegated-credentialing agreements make the group the source of truth, but the format is the group's choice.

## What a Fix Looks Like
Read each roster as it arrives, whatever the layout: map the columns, detect adds, terms and changes against the current record, and queue only conflicts and low-confidence rows for the analyst. Send the group an automatic acknowledgement listing what was applied and what was rejected and why, so errors are fixed at source.

## Who Feels the Pain
Provider data analysts; group administrators who see their changes ignored; members using stale listings; compliance staff explaining late updates.

## Impact If Fixed
Roster changes applied within days rather than weeks, analysts working exceptions rather than whole files, and fewer late updates to explain to regulators.
