# Roaming Settlements Reconciled by Spreadsheet

**Niche:** [[niches/wireless-carriers/rural-regional-carriers/profile|Rural & Regional Mobile Carriers]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Monthly roaming settlements worth a large share of a rural carrier's revenue are checked by one finance person in a spreadsheet, so missed and mis-rated usage goes unrecovered.
**Tags:** #autoencoders #feature-engineering #evaluation-metrics #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche (drive-test contractors, crowdsourced-data vendors and coverage engineering consultants) is fighting to prove, road by road, the coverage and quality a rural network delivers to the national carriers' roaming customers and on the FCC's map, and whoever produces the most credible road-level proof takes the account.

## The Problem
Roaming usage flows through clearinghouse records and is settled monthly at agreed rates. Records are dropped, rated at the wrong tier, or disputed. The rural carrier compares settlement files with its own switch records in spreadsheets, catches the obvious gaps and lets the rest go.

## Why It's Still Broken
Settlement assurance tools target large carriers with many partners. The rural carrier has few partners but a lot of revenue at stake with each, and no staff to build reconciliation.

## What a Fix Looks Like
Automated matching of network usage records to clearinghouse and settlement files by partner, day and site, with anomaly flags for unexplained drops in recorded roaming traffic and rate mismatches against the agreement, plus a dispute pack generated for each flag. The matched records double as the carrier's proof of how much of each partner's traffic its network carried, site by site, which is half of the case it makes at renewal.

## Who Feels the Pain
Rural carrier finance staff and CEOs, who see roaming revenue move without knowing why.

## Impact If Fixed
Revenue that is earned but never billed gets recovered, at the cost of a small software subscription.
