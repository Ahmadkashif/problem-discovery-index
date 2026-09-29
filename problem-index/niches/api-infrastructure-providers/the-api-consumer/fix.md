# The Status Page That Says Everything Is Fine

**Niche:** [[niches/api-infrastructure-providers/the-api-consumer/profile|The API Consumer]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A consumer's error rate against a provider is twelve percent and the provider's status page is green, because the status page reflects the provider's own view of their own aggregate.
**Tags:** #descriptive-statistics #hypothesis-testing #change-point-detection #confidence-intervals #evaluation-metrics #quick-win #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to give the developer integrating against somebody else's API the visibility and control they have over their own systems — and whoever does that takes the integration layer, because the consumer currently operates blind against a dependency they cannot change.

## The Problem
An engineering team sees errors from a provider climbing. They check the status page: all systems operational. They spend three hours investigating their own code, their network and their client library. The provider's incident is regional, or affects one endpoint, or affects requests with a particular parameter, or is simply not yet acknowledged because the provider's own alerting threshold has not been crossed. The status page is honest and useless, because it reports a global aggregate assessed by the party with the least incentive to declare an incident.

## Why It's Still Broken
Status pages are a communication artefact owned by the provider, and declaring an incident has commercial and service-level consequences, which reliably delays acknowledgement — this is not malice, it is an incentive working as incentives do. They also report at the granularity of a service rather than an endpoint or a region, so a partial failure is invisible by design. And the consumer has no alternative reference, so they treat the page as ground truth even when their own telemetry contradicts it.

## What a Fix Looks Like
Trust your own telemetry and use theirs as a hint. Alert on the consumer's own observed error and latency profile per provider and per endpoint, which is ground truth for the only thing that matters — whether this integration is working for this consumer — and is available immediately. Compare against the provider's declared status and report the divergence explicitly, since "our error rate is twelve percent and their page is green" is the fact the engineer needs in the first minute and it ends the three hours of self-investigation. Consume status pages programmatically where they publish an interface, rather than having someone open a browser. Where multiple consumers can share signal — through a vendor or a community aggregation — do so, because the earliest reliable indication of a provider incident is several unrelated consumers seeing it simultaneously, which is exactly the cross-tenant aggregation the connector-reliability niche describes. Record incident history per provider from the consumer's own observations, which produces the real reliability record for renewal conversations. And distinguish provider failure from consumer failure in the alert itself, since that determines who is woken up.

## Who Feels the Pain
Engineers debugging their own systems during somebody else's incident; on-call rotations paged for failures they cannot fix; and companies whose reliability is determined by providers whose real performance they have never measured.

## Impact If Fixed
The consumer's own telemetry is ground truth and is already collected, and reporting the divergence from the provider's status page ends the most common wasted investigation in integration operations. The per-provider incident history is the evidence every renewal conversation lacks.
