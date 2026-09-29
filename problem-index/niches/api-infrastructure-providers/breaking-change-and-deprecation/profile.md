# Breaking Change & Deprecation

**Parent Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to tell a provider exactly which consumers a proposed change would break, before it ships — and whoever does that takes the platform, because the inability to answer it is why nothing is ever retired.

## Profile
**Market Size:** ~$610M US attributable to API lifecycle, versioning and deprecation management
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** None — deprecation is announced into silence
**Target Buyer:** API product management and platform engineering
**Automation Potential:** Very High — every call that would break is flowing through the gateway now

## What Makes This a Distinct Niche
An API is a contract with counterparties the provider frequently cannot enumerate. Someone proposes removing a field, tightening a validation, changing a default. The question is who breaks, and the honest answer is that nobody knows, so the change is not made. Repeat that for a decade and the organisation has eleven versions it cannot retire, endpoints nobody can explain, fields kept alive for consumers who may have disappeared, and a maintenance burden that compounds. The remarkable part is that the answer is flowing through the gateway continuously: every consumer that uses the field in question is making a request containing it right now. The category computes rate limits and latency percentiles from that traffic and answers none of the questions that would let an organisation change anything.

## Current Tools & Gaps
Versioning conventions, deprecation headers, sunset announcements, developer portal notices, and analytics reporting call volumes per endpoint. The gaps: analytics are per endpoint rather than per field, and the breaking changes that matter are almost always field-level; consumer identity is often resolvable and rarely resolved, so the provider knows a key called an endpoint and not who owns that key; migration progress is not tracked, so deadlines are extended indefinitely on the basis of anxiety; nothing distinguishes a consumer who will break from one who merely receives the field and ignores it; and the safe default — never remove anything — is unmeasured, so its accumulating cost never competes with the risk of acting.

## Problems
- [[niches/api-infrastructure-providers/breaking-change-and-deprecation/build|🔨 Build: Who Breaks If We Change This]]
- [[niches/api-infrastructure-providers/breaking-change-and-deprecation/buy|🛒 Buy: Impact Analysis From Compiler and Package Ecosystems]]
- [[niches/api-infrastructure-providers/breaking-change-and-deprecation/fix|🔧 Fix: Deprecation Announced Into Silence]]
