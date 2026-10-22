# Broadband Data Collection & Availability Filings

**Parent Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to produce a semiannual availability filing reconciled to the current Fabric that survives the challenge process, and whoever delivers it with the fewest engineer-hours and the fewest sustained challenges takes the account.

## Profile
**Market Size:** ~$150M a year in engineer, regulatory and consultant time spent on BDC filings and challenges by fixed providers (estimate)
**Share of Parent Industry:** ~0.05% of industry receipts (estimate)
**Digital Adoption:** Medium — the filing is digital; the reconciliation behind it is spreadsheets and GIS by hand
**Target Buyer:** Regulatory manager or consulting engineer who certifies the filing
**Automation Potential:** Very high — address matching, change detection and challenge drafting are mechanical

## What Makes This a Distinct Niche
Every facilities-based provider files availability for each Fabric location twice a year on FCC-set dates (the June 30, 2026 data was due September 1, 2026, the same day as Fabric challenges for the December revision). The same national map decided BEAD eligibility and is used in every subsidy challenge, so the filing has commercial consequences beyond compliance. The work is identical in shape across thousands of filers and recurs on a fixed calendar, which makes it the most mechanical regulatory task in the industry.

## Current Tools & Gaps
The FCC BDC system and specifications; CostQuest Fabric licences; GIS; network mapping tools that export passings; consultants who file for small providers. Gaps: matching addresses and passings to Fabric IDs by hand each cycle; no diff against the prior filing; Fabric challenges missed because nobody noticed missing locations; and challenge responses assembled from scratch. This niche is the filing itself; the location obligations of subsidy programmes are the separate [[niches/wired-broadband-providers/subsidy-buildout-compliance/profile|Subsidy & Buildout Compliance]] niche.

## Problems
- [[niches/wired-broadband-providers/bdc-availability-filings/build|🔨 Build: Availability Claim Validator Against Plant and Speed Tests]]
- [[niches/wired-broadband-providers/bdc-availability-filings/buy|🛒 Buy: Address Matching Tools Adapted to the Fabric]]
- [[niches/wired-broadband-providers/bdc-availability-filings/fix|🔧 Fix: The Challenge Response Assembled in a Week]]
