# Does Moving It to the Edge Help

**Niche:** [[niches/edge-cdn-providers/edge-compute-placement/profile|Edge Compute Placement]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every provider now offers edge compute and none can tell a customer whether moving a given piece of logic to the edge would actually improve anything or merely relocate the cost.
**Tags:** #graph-theory #optimization-fundamentals #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to tell a customer whether moving a given piece of logic to the edge would actually improve anything — and whoever answers that takes the edge compute market, because the capability is universal and the reasoning is absent.

## The Problem
A team moves their authentication check to the edge, expecting a latency improvement. The check needs to look up a session, which lives in a store in the origin region, so the edge function makes a round trip to the origin and then forwards the request — which is slower than the original arrangement and costs more. Meanwhile a redirect rule that could have been moved and would have removed an entire round trip stays at the origin, because nobody evaluated it. Both decisions were made by reasoning about what sounds like edge work, and both were checkable in advance from the request timings.

## Why Nobody Has Built This
Edge compute was launched as a capability and marketed with examples, and the reasoning about when it helps has been left to the customer's architects. The determining factor — whether the state the logic needs is available at the edge — is an application-specific question the provider has not modelled. Estimating the benefit requires understanding the request path, which the provider observes and has not turned into an analysis. And the cost comparison between edge and origin execution is genuinely difficult because the pricing models are not comparable, which has let everyone avoid the question.

## What to Build
Evaluate placement before the migration. Model the request path from the observed traffic: how many round trips a request involves, what each contributes to latency, and what the logic in question depends on — which is derivable from the timings and the request structure the provider already sees. Estimate the benefit of moving a given piece of logic, accounting for the round trips removed and the round trips introduced if the logic must fetch data it does not have locally, which is the calculation that distinguishes the good placements from the bad and nobody performs. Classify the common patterns honestly: routing, header manipulation, redirects, static personalisation and authorisation with a cacheable token are clear wins; anything requiring a consistent read of origin state is usually not; and stating this plainly is more useful than any example gallery. Model the cost side in comparable units, since the pricing structures differ and the customer cannot currently compare. Measure afterwards with a controlled comparison, running the logic at both locations for a fraction of traffic, which is straightforward at the edge and would correct the guesses. And report the result honestly including the neutral and negative cases, because a provider that only publishes wins will be believed once.

## Target Customer
Application platform and architecture teams evaluating edge compute, and the providers themselves, for whom customers making bad placement decisions is a slow poison in a growing product line.

## Impact If Built
The capability is universal and the reasoning is absent, which produces a mix of good, neutral and actively harmful placements that nobody has characterised. The data-locality question is the determining factor and is answerable in advance from the request path.
