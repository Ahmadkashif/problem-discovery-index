# The Logic That Moved Away From Its Data

**Niche:** [[niches/edge-cdn-providers/edge-compute-placement/profile|Edge Compute Placement]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Edge functions routinely make a round trip back to the origin to fetch the state they need, which makes them slower than the origin logic they replaced, and nothing reports it.
**Tags:** #descriptive-statistics #graph-theory #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #data-integration
**Contested on:** Every serious competitor here is fighting to tell a customer whether moving a given piece of logic to the edge would actually improve anything — and whoever answers that takes the edge compute market, because the capability is universal and the reasoning is absent.

## The Problem
An edge function personalises a response. To do so it fetches the user's preferences from the origin, which is a round trip from the edge node to the origin region and back. The request now pays the user-to-edge latency, the edge-to-origin round trip, and the origin-to-edge return — which is more than the original path. The function works, the deployment is reported as successful, and the latency got worse in a way that is invisible because the edge compute dashboard reports the function's execution time and not the round trips it made.

## Why It's Still Broken
Edge compute metrics report execution duration, which is what the runtime knows, and the outbound fetches the function makes are a separate concern reported separately if at all. The function's author tested it locally where everything is near, and the round trip is only expensive in production geography. And the entire framing of edge compute as running code closer to the user encourages the assumption that closer is faster, without the qualification that it is only faster if the data is also closer.

## What a Fix Looks Like
Report the whole path, not the execution time. Instrument outbound fetches from edge functions and report them alongside execution duration, so a function whose execution is two milliseconds and whose fetch is ninety is visible for what it is — this is the single reporting change that would prevent most of these mistakes. Compare end to end against the origin-only path, which requires running both for a fraction of traffic and is easy at the edge, and is the only honest evaluation. Warn at deployment when a function makes an unconditional origin fetch, since that is a strong signal the placement is wrong and is statically detectable. Report the geography, since the function's cost depends on the distance between the edge node and the origin and is much worse for users far from the origin region — which is precisely the population the placement was meant to help. Surface the state the function depends on and whether an edge-local alternative exists, which is the remedy when one does. And make the cost visible per request rather than as an aggregate, because the aggregate hides the users for whom the placement is worst.

## Who Feels the Pain
Users whose requests got slower after a change intended to speed them up; teams whose edge deployment is reported as successful and is not; and providers whose edge compute customers conclude the product does not deliver.

## Impact If Fixed
Reporting outbound fetches alongside execution time is a small instrumentation change that makes the dominant failure mode visible. The static warning at deployment catches it before it ships, and the geographic breakdown shows that it is worst for exactly the users the edge was supposed to help.
