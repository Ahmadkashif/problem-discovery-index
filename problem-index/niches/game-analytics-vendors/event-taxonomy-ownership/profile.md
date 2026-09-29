# Event Taxonomy Ownership

**Parent Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Category:** 🟠 Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to keep an event schema coherent as a game changes for years, when the schema was designed early by whoever was available and nobody owns it — and whoever takes ownership takes the account.

## Profile
**Market Size:** ~$180M US
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** Low — unowned
**Target Buyer:** Data platform leadership
**Automation Potential:** High — schema governance and evolution

## What Makes This a Distinct Niche
Every analysis depends on events the game team chose to send, the schema was designed early by whoever was free, and it drifts silently as the game changes. New features ship with events named by whoever implemented them. Old events keep firing with meanings that have shifted. Nobody owns the taxonomy, so it accumulates inconsistency until an analysis produces something obviously wrong. The whole analytics stack rests on this layer and it is the least governed part of it.

## Current Tools & Gaps
An event list in a spreadsheet, a naming convention document somebody wrote, and code review. The gaps: no schema registry; no review of new events; no deprecation process; no detection of semantic drift; and no ownership anywhere in the organisation.

## Problems
- [[niches/game-analytics-vendors/event-taxonomy-ownership/build|🔨 Build: A Taxonomy That Survives the Game]]
- [[niches/game-analytics-vendors/event-taxonomy-ownership/buy|🛒 Buy: Schema Governance From Data Engineering]]
- [[niches/game-analytics-vendors/event-taxonomy-ownership/fix|🔧 Fix: Four Events That Mean the Same Thing]]
