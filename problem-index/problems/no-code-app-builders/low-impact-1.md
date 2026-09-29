# Integration Connector Coverage

**Industry:** [[no-code-app-builders|No-Code App Builders]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Connector marketplaces run to thousands of integrations and the one that matters is always the internal system with a bespoke API, so the builder falls back to a generic HTTP block and rebuilds authentication by hand.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #data-integration #automation

## The Problem
No-code platforms compete on connector count, and the counts are large. Hundreds or thousands of pre-built integrations covering the well-known SaaS applications.

The distribution of what people actually need does not match. A given company's important systems include its ERP, a legacy internal service, an industry-specific vendor, a partner's API and a database that predates everyone currently employed. The long tail is where the work is, and the marketplace covers the head.

So the builder uses the generic HTTP request block. That means reading API documentation, implementing authentication, handling pagination, parsing responses, managing rate limits and writing error handling — which is programming, performed by someone who chose this platform specifically because they do not program.

Depth is the second failure. Existing connectors are frequently shallow, covering the common operations and omitting the specific endpoint needed. A builder discovers this halfway through and falls back to HTTP for one step, ending with a hybrid that is harder to maintain than either approach.

## What Already Exists
Connector marketplaces at Zapier, Make, Workato, Power Platform and every no-code vendor are extensive and improving. Generic HTTP and webhook blocks are universal. OAuth handling is built in for supported providers. API specification standards like OpenAPI are widely published. Some platforms offer connector SDKs for partners to build their own.

## The Customisation Gap
Connector generation from a specification is the obvious missing capability. Where an OpenAPI specification exists — which is increasingly common, including for internal services — generating a usable connector with authentication, pagination and typed operations is largely mechanical and is not offered. The builder reads the spec and implements it by hand instead.

Where no specification exists, inference from example requests and responses is tractable and would cover the legacy internal systems that constitute most of the gap.

Authentication is the sharpest single obstacle, because it is where non-programmers reliably stop. Recognising the auth pattern from documentation and configuring it correctly is a well-bounded problem that would remove the most common point of abandonment.

Failure handling is the quieter gap. Generic HTTP blocks fail in ways the builder did not anticipate — rate limits, transient errors, schema changes — and no platform proposes the retry, backoff and error branch that a developer would add reflexively. Apps built this way are fragile in predictable, fixable ways.

## Impact If Solved
Connector coverage determines whether a no-code app can touch the systems that matter, and the marketplace covers precisely the systems that were already easy. Generating connectors from specifications and examples opens the long tail, and automatic failure handling addresses the fragility that generic HTTP blocks introduce.
