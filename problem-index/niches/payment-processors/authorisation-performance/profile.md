# Authorisation Performance

**Parent Industry:** [[industries/payment-processors|Payment Processors]]
**Category:** High Market Share
**Contested on:** This niche is not terminal — recovering a decline and preventing one are different contests with different winners, and they are stated separately in the sub-niches below.

## Profile
**Market Size:** ~$36B US
**Share of Parent Industry:** ~30% of category revenue
**Digital Adoption:** Low — configuration where prediction belongs
**Target Buyer:** Payments product and merchant leadership
**Automation Potential:** Very High — the outcome record exists

## What Makes This a Distinct Niche
The single number that decides whether a merchant stays is the authorisation rate. A percentage point of it is worth more to a large merchant than any pricing negotiation, and the processor controls part of it through decisions it currently makes with static configuration. This is the largest concentration of contested value in the category because the competitive frontier has moved from price to authorisation performance and because every decision inside it is a prediction the industry treats as a setting.

It is also **not terminal**. Two contests live here. Recovering a decline asks what to do after an issuer says no — retry or not, when, how often, whether to refresh the credential — which is a prediction problem over decline codes, issuer behaviour and timing, with the answer arriving in a settlement file. Preventing the decline asks how to present the transaction in the first place — which route, which network, which token, which authentication path, what data to include — which is a routing, infrastructure and network relationship contest decided before any decline occurs. One is modelling, the other is partnership and plumbing. The two contests are stated in the sub-niches.

## Current Tools & Gaps
Static retry schedules, routing rules configured per merchant, network tokens where enabled, account updater services, and authorisation rate reporting. The gaps: retry logic set by convention; routing decided by cost rather than by approval likelihood; outcomes in settlement files nobody joins to decisions; issuer behaviour treated as uniform; and the whole apparatus configured rather than learned.

### Contested sub-niches
- [[niches/payment-processors/decline-recovery/profile|🎯 Decline Recovery]]
- [[niches/payment-processors/routing-and-network-optimisation/profile|🎯 Routing & Network Optimisation]]

## Problems
- [[niches/payment-processors/authorisation-performance/build|🔨 Build: Prediction Treated as Configuration]]
- [[niches/payment-processors/authorisation-performance/buy|🛒 Buy: Decision Optimisation Practice]]
- [[niches/payment-processors/authorisation-performance/fix|🔧 Fix: The Decline Code Vocabulary Nobody Uses Consistently]]
