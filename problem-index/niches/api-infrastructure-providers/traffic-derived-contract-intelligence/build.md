# The Specification Says Intent and the Traffic Says Reality

**Niche:** [[niches/api-infrastructure-providers/traffic-derived-contract-intelligence/profile|Traffic-Derived Contract Intelligence]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** OpenAPI specifications, interactive documentation and code generation are all mature and all describe what the API was meant to do, while consumers integrate against what it actually does.
**Tags:** #bert #graph-theory #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor that gets here is fighting to turn observed traffic into the API's real contract — what is actually used, actually returned and actually relied upon — and whoever does that holds the accurate specification while everyone else holds the intended one.

## The Problem
The specification says a status field is a string. In practice it takes one of six values, and consumers have hard-coded all six. It says a field is optional; in practice it is always present, and consumers have stopped checking. It documents a parameter that the implementation ignores, and does not document another that works and that a third of consumers use. Every one of these divergences is a trap: the specification is what the provider believes and enforces nothing, and the implementation is what consumers built against. The gateway has observed all of it, continuously, for years.

## Why Nobody Has Built This
The specification-first worldview is deeply embedded in the category's tooling — everything generates from the document, so the document is treated as truth — and reconciling against reality inverts that assumption. Payload inspection was avoided for performance and privacy reasons, which sampling and structural extraction address entirely. And the finding is uncomfortable in a specific way: a traffic-derived specification is an audit of the published one, and no team enjoys learning that their documentation has been misleading consumers for three years.

## What to Build
Derive the contract from observation and reconcile it with the document. Sample requests and responses and infer the actual schema: fields present and their frequency, types as they really occur, value ranges and effective enumerations, conditional presence and the conditions that govern it, and the parameters consumers actually send. Diff that against the published specification and classify each divergence — documented but unused, used but undocumented, type mismatch, wrong optionality, undocumented enumeration — which is a short and precise list per endpoint and is directly actionable. Track per-consumer usage so the contract is per relationship as well as global, which is what the deprecation niche needs. Detect drift in behaviour over time, since an implementation change that was not a specification change is exactly the silent break consumers experience. Propose specification updates rather than asserting them, since some divergences should be fixed in the implementation and others in the document, and that is a judgement. And keep it structural only, with no retention of values, which makes the whole capability defensible and is sufficient for every question it answers.

## Target Customer
Gateway and API management vendors, platform and API product teams, and the documentation and specification tooling vendors whose products all assume an authored source of truth.

## Impact If Built
The gateway holds a complete and continuously updated behavioural specification and publishes none of it, while every consumer integrates against reality and every tool generates from intent. The divergence list is short, precise and immediately actionable, and it is the foundation the deprecation and security niches build on.
