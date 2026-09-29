# Three Thousand Connectors and Not the One You Need

**Niche:** [[niches/no-code-app-builders/integration-and-connectors/profile|Integration & Connectors]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Connector marketplaces are enormous and the integration a given customer needs is always the internal system with a bespoke API, so the builder rebuilds authentication by hand in a generic HTTP block.
**Tags:** #large-language-models #transformers #bert #graph-theory #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor here is fighting to make the connection to whatever system the customer actually has work and keep working — and that contest splits between getting connected and staying connected, which is why this niche is not terminal and is decomposed below.

## The Problem
A builder needs their app to read from the company's inventory system. It is an internal service with a documented API, used by nobody outside the company. There is no connector and never will be, because writing one is a week of engineering for a single customer. The builder opens the generic HTTP block, works out the authentication scheme, handles token refresh, implements pagination, discovers that errors come back as HTTP 200 with a body field, and eventually gets it working. They have written a connector by hand inside a product bought to avoid writing connectors, and the result is undocumented, unmonitored and known only to them.

## Why Nobody Has Built This
The connector model is per-system and hand-built, which economically excludes the tail by definition, and the marketplace's size has always been the marketing answer to a question about coverage. Generating a connector from a specification has been possible in principle for years and was never commercially attractive while the head of the distribution was still being covered. And the tail is invisible to vendors: nobody reports which connections customers attempt and fail to find, so the demand for the long tail has never appeared in any roadmap discussion as a number.

## What to Build
The common layer both sub-niches need: connectors as generated artefacts rather than authored ones. An API description — an OpenAPI document, a GraphQL schema, a published reference page, or observed traffic where nothing else exists — as the input, and a working, typed, authenticated connector as the output, produced in minutes rather than in a sprint. Authentication handled as a small set of known patterns rather than as bespoke code each time, since nearly every API uses one of a handful. Pagination, rate limiting, retry and error semantics inferred from the specification and confirmed by probing, which is where hand-built integrations fail. A test harness that exercises the generated connector against the real system before the builder commits to it, which is the difference between a plausible connector and a working one. And an instrumented record of what customers try to connect to and cannot, which is the demand signal the whole category is missing and which tells a vendor which parts of the tail are actually a head.

## Target Customer
No-code and automation platform vendors, integration platform vendors, and the internal platform teams at large organisations who maintain private connector libraries by hand.

## Impact If Built
The long tail is excluded by the economics of hand-built connectors, and generation changes those economics rather than improving coverage incrementally. The failed-connection demand signal is the second output and is the first evidence any vendor would have about where the tail actually is.
