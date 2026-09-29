# Gaming Resistance

**Parent Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Category:** Contested Sub-Niche
**Contested on:** Whether the signals a ranking depends on can only be improved by actually being better, rather than by manipulating a proxy.

## Profile
**Market Size:** ~$2.18B — 60% of the ranking and allocation niche
**Share of Parent Industry:** ~16% of platform-intermediated gross services volume
**Digital Adoption:** Moderate — every platform fights manipulation reactively; almost none designs signals to be manipulation-resistant in the first place
**Target Buyer:** Platform trust & safety, marketplace integrity and search quality teams
**Automation Potential:** High, and adversarial — detection automates well, but the adversary adapts to whatever is deployed

## What Makes This a Distinct Niche

The other half of ranking asks whether a placement can be explained. This half asks whether a ranking survives being understood at all.

Every ranked signal on a freelance marketplace is under the deliberate control of the party being ranked, and the ones easiest to control are usually the most predictive in historical data. Response rate is gamed with autoresponders. Completion rate is gamed with tiny throwaway contracts. Ratings are gamed with reciprocal arrangements, with off-platform payment for on-platform five-star contracts, and with account networks. Recency is gamed by cycling activity. Each is a proxy that was honest when nobody was optimising against it.

What makes this a distinct market rather than a fraud sub-function is the design question underneath the detection: which signals are *inherently* costly to fake — meaning the cheapest way to move them is to deliver better work — and which are merely currently unfaked. That question is answerable in advance, from the platform's own record, and almost nobody asks it before shipping a feature into a ranker.

## Current Tools & Gaps

Platforms run fraud detection: velocity rules, device and network fingerprinting, graph analysis over account relationships, and manual review queues for flagged accounts. This machinery is reasonably mature and catches the crude cases — obvious rings, shared devices, implausible rating patterns.

Two gaps persist. The first is that detection is reactive by construction: a manipulation technique runs until it is noticed, which on a large platform can be quarters, and the accounts that used it keep the ranking benefit they accrued. The second, and larger, is that nobody scores the ranking features themselves for manipulability. A feature enters the model because it improved offline metrics, and its vulnerability is discovered in production by the people exploiting it. There is no equivalent of a threat model for the feature set.

## Problems
- [[niches/freelance-marketplaces/gaming-resistance/build|🔨 Build: Manipulability Scoring for Ranking Features]]
- [[niches/freelance-marketplaces/gaming-resistance/buy|🛒 Buy: Fraud and Graph Analytics Adapted to Reputation Manipulation]]
- [[niches/freelance-marketplaces/gaming-resistance/fix|🔧 Fix: Manipulation Found Late, Benefit Already Banked]]
