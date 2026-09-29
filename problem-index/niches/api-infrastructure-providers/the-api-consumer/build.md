# Blind Against a Dependency You Cannot Change

**Niche:** [[niches/api-infrastructure-providers/the-api-consumer/profile|The API Consumer]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A product depending on six third-party APIs carries the operational risk of all six and has visibility into none of them, discovering behaviour changes through its own outages.
**Tags:** #change-point-detection #time-series-forecasting #descriptive-statistics #graph-theory #evaluation-metrics #confidence-intervals #worker-facing #data-integration
**Contested on:** Every serious competitor that takes this seriously is fighting to give the developer integrating against somebody else's API the visibility and control they have over their own systems — and whoever does that takes the integration layer, because the consumer currently operates blind against a dependency they cannot change.

## The Problem
A company's product calls a payments provider, an identity service, a mapping API, a messaging gateway, a data enrichment service and a tax calculator. On Thursday the enrichment service starts returning an empty array for a category it previously populated. No error, no announcement, no status page entry. The company's product silently degrades for eleven days until a customer complains. The engineering team debugs their own code first, as anyone would, and finds nothing. The provider, asked, confirms a change made in a release nobody outside noticed.

## Why Nobody Has Built This
The category's customers are providers, and a product built for consumers has no natural distribution through the same channel. General observability covers outbound calls as a dimension and stops at latency and error rate, which does not catch a silently changed response shape. Contract monitoring from the consumer side requires baselining the provider's behaviour, which nobody has framed as a product. And the risk is diffuse until it is acute: most integrations are fine most of the time, and the cost arrives all at once.

## What to Build
Consumer-side dependency observability. Baseline each provider's actual behaviour from the consumer's own traffic — response shape, field presence, value distributions, latency and error profile — and detect drift, which catches the silently changed response the day it happens rather than eleven days later. Track usage against known limits and project when a limit will be reached, since the consumer usually discovers a quota by hitting it. Verify status independently, because a provider's status page is their own assessment and the consumer's own error rate is the ground truth — and the divergence between the two is itself worth reporting. Assemble a dependency register across all providers with criticality, contractual terms, observed reliability and the blast radius if each fails, which is the view no consumer currently has and which the obligation-monitoring niche in contract lifecycle describes from the commercial side. Watch provider changelogs and deprecation notices automatically, since the email arrives at an address nobody monitors. And measure actual delivered reliability against what was promised, which is the input to every renewal conversation and is never assembled.

## Target Customer
Engineering teams whose products depend materially on third-party APIs, platform teams managing an integration portfolio, and the observability vendors for whom the consumer side is an unserved direction.

## Impact If Built
Consumers carry the operational risk of dependencies they cannot control and have no instrumentation for them, which is an asymmetry the whole category has left unaddressed. Response-shape drift detection catches the failure class that latency and error monitoring structurally cannot see.
