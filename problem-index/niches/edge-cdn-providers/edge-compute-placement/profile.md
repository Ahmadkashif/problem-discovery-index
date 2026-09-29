# Edge Compute Placement

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to tell a customer whether moving a given piece of logic to the edge would actually improve anything — and whoever answers that takes the edge compute market, because the capability is universal and the reasoning is absent.

## Profile
**Market Size:** ~$980M US edge compute
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** Low in substance — the runtimes are deployed and the placement decisions are guesses
**Target Buyer:** Application platform and architecture teams
**Automation Potential:** Very High — the request path and its timings are fully observable

## What Makes This a Distinct Niche
Every provider now offers edge compute and none can tell a customer whether moving a given piece of logic there would improve anything or merely relocate the cost. The question is genuinely answerable: the benefit depends on how many round trips the logic saves, how much data it must fetch to do its work, whether that data is available at the edge, and what the origin would have spent doing it — all of which are observable in the request path. Instead the decision is made on intuition and the results are mixed in a way nobody has characterised: some placements remove a round trip and are clearly good, some move computation away from the data it needs and are clearly bad, and many are neutral and are defended by whoever proposed them. The programming models also differ substantially between providers, which makes an experiment expensive and a mistake sticky.

## Current Tools & Gaps
Edge runtimes at every provider with differing programming models, key-value and state primitives at the edge, and templates for common patterns. The gaps: nothing estimates the benefit before the work is done, so the decision is a guess with a migration cost attached; nothing measures the benefit afterwards in a controlled way, so the guess is never corrected; data locality — whether the state the logic needs is at the edge — is the determining factor and is not modelled; cost comparison between edge and origin execution is difficult because the pricing models are not comparable; and portability between providers is poor enough that a placement decision is also a lock-in decision.

## Problems
- [[niches/edge-cdn-providers/edge-compute-placement/build|🔨 Build: Does Moving It to the Edge Help]]
- [[niches/edge-cdn-providers/edge-compute-placement/buy|🛒 Buy: Operator Placement From Distributed Query Processing]]
- [[niches/edge-cdn-providers/edge-compute-placement/fix|🔧 Fix: The Logic That Moved Away From Its Data]]
