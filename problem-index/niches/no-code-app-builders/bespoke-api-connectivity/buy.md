# Specification Inference From Documentation and Traffic

**Niche:** [[niches/no-code-app-builders/bespoke-api-connectivity/profile|Bespoke API Connectivity]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** API management products have inferred specifications from live traffic for years, and language models read prose documentation accurately, and neither capability has been pointed at the builder trying to connect to an internal system.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #confidence-intervals #cross-validation #data-integration
**Contested on:** Every serious competitor here is fighting to get a non-engineer connected to an internal system nobody has written a connector for, in the session where they need it — and whoever does that takes the builder, because the alternative is a hand-rolled HTTP block and a lost afternoon.

## The Problem
Deriving a machine-readable description of an API from observed requests and responses is a feature of API gateways and management products. Reading a documentation page and producing a structured specification is something language models do reliably. Both capabilities are available and neither has been applied to the moment a non-engineer is staring at a wiki page trying to work out what to put in a header.

## What Already Exists
Traffic-based specification inference in API management tooling; language models with strong performance on structured extraction from technical prose; OpenAPI tooling for validation and generation; contract testing frameworks; and schema inference from JSON samples, which is trivial and well covered. HAR file capture from browsers provides traffic without any infrastructure at all.

## The Customization Gap
The adaptation is to partial, messy, single-user inputs. It requires: (1) working from very few examples, since the builder has three requests rather than a week of production traffic, which makes schema inference under-determined and demands explicit uncertainty rather than a confident wrong type; (2) confidence reporting per inferred element, so the builder is told what is known and what is guessed, which is the difference between a usable tool and one that fails mysteriously later; (3) active probing to resolve the uncertainty — issuing safe read requests to confirm pagination, filtering and error shape — which converts assumptions into facts cheaply and is the step that makes few-shot inference viable; (4) strict safety around probing, since inferring a write endpoint must never involve trying it, and the distinction between safe and unsafe operations has to be conservative by default; and (5) output shaped as business actions rather than as a specification, because the specification is an intermediate artefact and the builder must never see it.

## Target Customer
No-code and automation platform vendors, API management vendors with an adjacent opportunity, and internal developer platform teams supporting citizen builders.

## Impact If Solved
Two mature capabilities combine to address a moment neither was built for, and the few-shot setting is the only real adaptation. Safe probing is what turns uncertain inference into a working connection, and the safety boundary around writes is non-negotiable.
