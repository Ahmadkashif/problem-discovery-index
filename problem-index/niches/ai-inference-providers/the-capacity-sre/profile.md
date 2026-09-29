# The Capacity SRE

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to make contention a policy the system executes rather than a decision a person makes at three in the morning — and whoever does that takes the account, because the arbitration is currently a human bottleneck with commercial consequences.

## Profile
**Market Size:** ~$260M US in loaded reliability cost and incident consequence
**Share of Parent Industry:** ~4% of category revenue equivalent
**Digital Adoption:** None — arbitration by hand under pressure
**Target Buyer:** Site reliability leadership at the providers
**Automation Potential:** High — the policy is expressible and the signals are present

## What Makes This a Distinct Niche
When capacity runs short, someone has to decide which customer gets degraded so another does not. At these providers that someone is a reliability engineer, in the moment, under pressure, with incomplete information about contractual commitments and no tooling that expresses priority. They are making a commercial decision — which relationship to damage — with an operations mandate and no policy to point at. It is the most consequential judgement in the business, it is made repeatedly by people who did not sign up to make it, and it is the single clearest instance of the industry's economics landing on an individual.

## Current Tools & Gaps
Monitoring dashboards, manual scaling, rate limit adjustments, and a chat channel. The gaps: no spike anticipation, so every event starts from surprise; no encoded priority policy, so arbitration is improvised; no visibility into which customers hold which commitments at the moment of decision; no record of what was decided and why; and no measurement of the human cost, so the automation is never prioritised.

## Problems
- [[niches/ai-inference-providers/the-capacity-sre/build|🔨 Build: Deciding in Real Time Who Gets Degraded]]
- [[niches/ai-inference-providers/the-capacity-sre/buy|🛒 Buy: Overload Management and Graceful Degradation]]
- [[niches/ai-inference-providers/the-capacity-sre/fix|🔧 Fix: A Commercial Decision With an Operations Mandate]]
