# Documentation Drift from Behaviour

**Industry:** [[api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** OpenAPI specifications, interactive documentation and code generation are all mature and all describe what the API was meant to do, while consumers integrate against what it actually does.
**Tags:** #bert #word-embeddings #large-language-models #hypothesis-testing #change-point-detection #evaluation-metrics #data-integration

## The Problem
API documentation is generated from a specification, and the specification is written by hand or annotated in code. Either way it describes intent.

Behaviour diverges immediately and quietly. A field documented as required is optional in practice. An enum has a value the specification does not list, added by someone fixing a bug. An endpoint returns a status code no document mentions in a case nobody anticipated. A rate limit behaves differently from its description under burst. A field is documented as a string and is sometimes null.

Consumers integrate against reality, because reality is what their code encounters. They discover the divergences by failing, they work around them, and their integration then depends on undocumented behaviour — which means the provider can break them by fixing the divergence, which is a genuinely perverse situation.

Nobody validates the specification against traffic, though the gateway carries every request and response and could compare them continuously.

## What Already Exists
OpenAPI is the dominant specification format with a large ecosystem. Interactive documentation portals are standard. Client SDK generation from specifications works well. Contract testing tools (Pact, Spring Cloud Contract) verify provider and consumer agreement in CI. Schema validation at the gateway is available and enforces the specification on request.

## The Customisation Gap
Contract testing validates against a specification in a test environment. It does not observe production, where the divergences live, and it only covers the interactions someone wrote a test for.

Continuous conformance checking against live traffic is the missing capability and is straightforward: compare observed requests and responses against the specification, and report where reality differs — undocumented fields, unlisted enum values, nullability violations, status codes not in the specification. That report would be new to essentially every API team.

Specification induction from traffic is the constructive version. Where no specification exists, or where it is badly out of date, generating one from observed behaviour produces something more accurate than the document, and is particularly valuable for the internal APIs that were never specified at all.

Behavioural change detection is the third gap and matters most: an API whose observed behaviour shifts between releases has changed its contract whether or not anyone versioned it, and detecting that at deployment is the check nobody runs.

## Impact If Solved
Consumers integrate against behaviour, so behaviour is the contract, and the document describing it is unverified. Continuous conformance checking makes documentation trustworthy and — more importantly — makes accidental contract changes visible at the moment they ship rather than when a consumer breaks.
