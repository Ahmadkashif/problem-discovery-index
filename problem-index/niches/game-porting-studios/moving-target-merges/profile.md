# Moving-Target Merge Management

**Parent Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Category:** ⚡ Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to keep a port synchronised with a codebase that ships every fortnight without redoing the platform work each time — and whoever automates that merge takes the account.

## Profile
**Market Size:** ~$100M US
**Share of Parent Industry:** ~5% of category revenue
**Digital Adoption:** Medium — manual
**Target Buyer:** Build and tools engineers
**Automation Potential:** Very high — merge, conflict and impact automation

## What Makes This a Distinct Niche
A port diverges from the source the moment work begins, and the source keeps moving. Every client patch must be merged into a codebase that now has platform-specific changes throughout it, conflicts must be resolved by someone who understands both sides, and the merge itself frequently breaks the platform work. It is repetitive, mechanical, high-friction engineering that recurs every fortnight for the length of the project and is performed by hand.

## Current Tools & Gaps
Version control, a merge tool and an engineer who knows the platform changes. The gaps: no isolation of platform changes from shared code; no automated conflict classification; no impact analysis of an incoming merge; no regression check scoped to the merge; and no record of recurring conflict hotspots.

## Problems
- [[niches/game-porting-studios/moving-target-merges/build|🔨 Build: Merging Without Redoing the Port]]
- [[niches/game-porting-studios/moving-target-merges/buy|🛒 Buy: Fork Management From Open Source Maintenance]]
- [[niches/game-porting-studios/moving-target-merges/fix|🔧 Fix: The Merge That Undid the Platform Work]]
