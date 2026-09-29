# Mining What the Firm Has Already Built

**Niche:** [[niches/saas-implementation-partners/pattern-extraction/profile|Pattern Extraction]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of configurations of the same platform exist and nobody has ever compared two of them.
**Tags:** #data-integration #k-means-clustering #graph-theory #evaluation-metrics #dimensionality-reduction #automation #descriptive-statistics #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to find out what hundreds of past implementations of the same platform actually have in common — and whoever extracts that takes the account.

## The Problem
The firm has configured the same platform hundreds of times. Each configuration is expressed in platform metadata — objects, fields, workflows, rules, layouts, integrations — and is retrievable. Nobody has ever extracted them into a comparable form and asked what they have in common. The consultant designing the next one therefore works from personal experience and whatever documents they can find, which is a small and arbitrary sample of the firm's actual history.

## Why Nobody Has Built This
Configuration lives in client tenants under client contracts, which is assumed to be an absolute barrier. Metadata differs enough between engagements to make naive comparison useless. No partner has framed this as an analysis problem. And the work is unbillable.

## What to Build
Extract, normalise and cluster the configurations the firm has already delivered. Extract configuration metadata from past engagements into one comparable representation, which is the core and is entirely mechanical once the contractual position is settled. Normalise across versions and client naming so unlike expressions of the same pattern are recognised as such. Cluster configurations to surface the recurring shapes and their frequency, which is what turns a pile into a catalogue. Record the variations within each pattern, since the variation is what a consultant needs to know. Relate patterns to client characteristics — industry, size, maturity — as that is the retrieval key that matters. Include the requirements and integration artefacts alongside the configuration, because the pattern is not only the end state. Handle confidentiality by abstracting to the pattern level, which is usually permitted and always assumed not to be. Make it queryable from a new engagement's requirements rather than browsable. Report how much of a typical engagement is covered by known patterns, which sizes the reuse opportunity concretely. And run the extraction continuously as engagements complete rather than once.

## Target Customer
Implementation partners and systems integrators, delivery leadership, platform vendors with partner programmes, and data mining and analytics vendors.

## Impact If Built
Hundreds of configurations of the same platform exist in a retrievable form and nobody has compared two of them. Extraction into a normalised, clustered catalogue is mechanical once the contractual position is settled.
