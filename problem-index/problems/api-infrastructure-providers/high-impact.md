# Knowing What Depends on an API

**Industry:** [[api-infrastructure-providers|API Infrastructure Providers]]
**Type:** High Impact
**One-liner:** Every breaking change is a negotiation with counterparties the provider cannot enumerate, so nothing is ever removed — and the traffic flowing through the gateway would identify exactly who breaks and how.
**Tags:** #graph-neural-networks #gradient-boosting #dbscan #change-point-detection #feature-engineering #confidence-intervals #evaluation-metrics #data-integration

## The Problem
An API is a promise to consumers. Changing it risks breaking them, and the provider frequently does not know who they are — internally, because service ownership drifts and nobody maintains a dependency register; externally, because public APIs are consumed by anyone with a key and a use case nobody described.

The rational response is to never break anything. So versions accumulate. Fields that should have been removed years ago are still returned because something might parse them. Endpoints nobody can explain are maintained because deleting them is unbounded risk. Deprecation notices are published, ignored, and the deadline slips repeatedly until it stops being announced.

The cost is compounding. Every additional version is surface area to test, secure and operate. Migration guides are written and unread. Engineers maintain code paths whose purpose nobody remembers, and the fear of breaking an unknown consumer prevents the changes that would make the platform better.

The gateway sees every request. It knows which consumers call which endpoints, with which parameters, and — critically — which fields of the response they actually parse, if response bodies are inspected. It computes rate limits from this and answers none of the questions above.

## Why It's Unsolved
Gateways were designed as traffic control, so their data model is request-shaped: method, path, status, latency, consumer identity. That is enough for rate limiting and dashboards and insufficient for dependency analysis, which needs field-level detail and consumer behaviour over time.

Response inspection is the specific obstacle. Knowing which fields a consumer uses requires observing what they do with the response, which the gateway cannot see, or inferring it from their subsequent behaviour, which is indirect. Some providers instrument client libraries, which works where the library is theirs and not otherwise.

Consumer identity is also weaker than it looks. An API key identifies an application, not a team, an owner or a business criticality. When the endpoint is deprecated, the provider has a key and no idea who to tell.

And there is an organisational vacuum. API product management is a young discipline, frequently unstaffed, and the person who would own a deprecation programme often does not exist.

## What a Solution Looks Like
A dependency graph built from observed traffic rather than declared registration. Which consumers call which operations, with what frequency, with which parameter combinations, and whether their usage is growing or decaying. That alone converts deprecation from a guess into a list.

Field-level usage is the high-value extension. Knowing that a field is returned to eleven consumers and parsed by none makes removing it a decision rather than a risk, and inferring it — from client library instrumentation, from consumer request patterns, or from selection parameters where the API supports them — is the piece worth building.

Breaking change impact prediction: given a proposed change, which consumers would break and how severely. That is the question every API team asks before every release and answers by asking around.

Consumer criticality and reachability, so a deprecation notice goes to a human who can act rather than to an unmonitored address attached to a key.

And migration progress tracked automatically, since the current mechanism — publish a deadline and hope — has no feedback loop at all.

## Impact If Solved
The inability to enumerate consumers is why API surfaces only grow, and the accumulated versions are a permanent tax on every team maintaining them. Building the dependency graph from traffic the gateway already carries turns deprecation from an act of faith into a managed project, and unblocks the changes that fear currently prevents.
