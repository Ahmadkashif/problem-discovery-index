# Pay Setting & the Realised Rate

**Parent Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Category:** High Market Share
**Contested on:** Whether the requester is told what hourly rate their per-task price implies before they set it.

## Profile
**Market Size:** ~$570M — 19% of the US microtask and research-participant market
**Share of Parent Industry:** ~19%
**Digital Adoption:** None — the rate is computable and never computed
**Target Buyer:** Requesters; platform leadership; ethics boards and regulators
**Automation Potential:** Very high — it is arithmetic over data already held

## What Makes This a Distinct Niche

The requester estimates five minutes, the task takes fifteen, the platform knows this exactly, and neither party is told.

This is the market's central failure and it is mostly not malice. A requester setting $0.50 for a task they believe takes five minutes intends $6 an hour; if it takes fifteen they have set $2 and will never find out. Academic studies of effective hourly earnings on these platforms have repeatedly found medians substantially below relevant minimum wages, and this estimation gap is as much the mechanism as deliberate underpayment.

The niche is distinct because the correction is arithmetic. The platform holds the completion time distribution for every task type and could show a requester the implied rate at the moment they set the price — before anyone has worked on it.

## Current Tools & Gaps

Per-task pricing set by the requester at posting. Bonus mechanisms for voluntary additional payment. Time limits per task. Some platforms publish guidance on fair pay; the academic-focused ones have moved furthest, with pay floors introduced under ethics-board pressure. Worker-built browser extensions that estimate effective rates from community data.

The gaps are the implied-rate display, the after-the-fact correction and any floor. Nothing tells a requester what rate they have set. Nothing tells them afterwards what it turned out to be, though the platform knows. And the existence of worker-built tooling to approximate both is a direct measure of what the platforms have chosen not to provide.

## Problems
- [[niches/crowdsourcing-platforms/pay-setting-and-rate/build|🔨 Build: Implied Rate at the Moment of Pricing]]
- [[niches/crowdsourcing-platforms/pay-setting-and-rate/buy|🛒 Buy: Pricing and Estimation Tooling Adapted to Task Duration]]
- [[niches/crowdsourcing-platforms/pay-setting-and-rate/fix|🔧 Fix: Nobody Tells the Requester What It Turned Out To Be]]
