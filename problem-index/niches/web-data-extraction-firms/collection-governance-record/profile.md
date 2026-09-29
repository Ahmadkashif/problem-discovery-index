# Collection Governance Record

**Parent Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to maintain a continuous, queryable account of what is being collected, from where, under what permission and for whose purpose — and whoever does that takes the account, because it is the evidence that makes the whole business defensible.

## Profile
**Market Size:** ~$340M US
**Share of Parent Industry:** ~17% of category revenue
**Digital Adoption:** Very Low — reviewed once, never revisited
**Target Buyer:** Legal and compliance functions, and the firms' own leadership
**Automation Potential:** High — the record assembles from request logs

## What Makes This a Distinct Niche
Robots parsers, rate limiters and legal review processes all exist. What no firm maintains is a continuous, queryable record joining them: what is being collected right now, from which hosts, under what stated permissions, for which customer, for what declared purpose, and whether any of those four have changed since the collection was approved. The review happens at onboarding and then the world moves — sites add terms, robots directives change, laws take effect, customers repurpose data for model training. The firms hold complete request logs and have built almost nothing that reasons about them, which leaves the sector's defining commercial risk entirely unmanaged.

## Current Tools & Gaps
Robots parsers, per-host rate limiting, legal review at onboarding, and contractual customer representations about purpose. The gaps: no linkage between the approval and the traffic it authorised; no re-evaluation when a site's terms or directives change; no record of declared purpose usable at query time; no per-host collection inventory, so nobody can answer what is being collected from where; and no ability to stop a collection that has become impermissible.

## Problems
- [[niches/web-data-extraction-firms/collection-governance-record/build|🔨 Build: No Continuous Record of What Is Being Collected]]
- [[niches/web-data-extraction-firms/collection-governance-record/buy|🛒 Buy: Policy Engines and Continuous Control Monitoring]]
- [[niches/web-data-extraction-firms/collection-governance-record/fix|🔧 Fix: Approved Once, Never Revisited]]
