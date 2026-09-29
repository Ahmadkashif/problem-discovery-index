# Engineering-Facing Optimisation

**Parent Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to produce a recommendation an engineer will actually act on — specific, safe and verifiably right — and whoever does that takes engineering, because after two bad suggestions the feature is dead permanently.

## Profile
**Market Size:** ~$560M US engineering-facing optimisation and rightsizing
**Share of Parent Industry:** ~19% of category revenue
**Digital Adoption:** Low — the recommendations exist and are not read
**Target Buyer:** Platform engineering; the engineers must act for anything to change
**Automation Potential:** Very High, and entirely bounded by trust rather than by technique

## What Makes This a Distinct Niche
Every platform in the category generates rightsizing recommendations and engineers ignore them. The mechanism is specific and worth stating precisely: a tool observes an instance at eight percent processor utilisation and recommends downsizing it. The instance is a standby that exists to be idle, or holds a warm cache, or is sized for a quarterly peak, or is saturating a network interface the recommendation did not consider. The engineer knows this and the tool does not. The second time this happens the feature is dead, permanently, and no subsequent improvement in the recommendations will bring that engineer back. This makes the contest here unusual: it is not about generating more or better recommendations but about never generating a confidently wrong one, which is a precision problem with an extremely asymmetric loss and is the same shape as the refusal problem in contract review and conversational analytics.

## Current Tools & Gaps
Rightsizing recommendations from utilisation metrics, idle resource detection, storage class suggestions, and scheduling for non-production environments. The gaps: recommendations are derived from infrastructure metrics with no application context, which is the root cause of the wrong ones; there is no confidence or safety assessment, so a certain recommendation and a speculative one look identical; the engineer's rejection is not captured, so the same wrong suggestion returns next month; nothing verifies the outcome of an accepted recommendation, so nobody learns; and the recommendations address instance sizing, which is the smallest available lever, while architectural decisions with far larger effects are untouched.

## Problems
- [[niches/cloud-cost-management/engineering-facing-optimisation/build|🔨 Build: Downsizing the Standby]]
- [[niches/cloud-cost-management/engineering-facing-optimisation/buy|🛒 Buy: Selective Prediction and Safe Automation]]
- [[niches/cloud-cost-management/engineering-facing-optimisation/fix|🔧 Fix: The Rejected Recommendation That Returns]]
