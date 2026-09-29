# A Shared Object That Is Not Quite Native

**Niche:** [[niches/data-marketplace-brokers/in-ecosystem-data-sharing/profile|In-Ecosystem Data Sharing]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Zero-copy sharing makes an external dataset appear inside the buyer's platform, and it behaves like a native table until it does not — at which point the difference surfaces in production.
**Tags:** #data-integration #graph-theory #compliance #evaluation-metrics #workflow-orchestration #automation #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this sub-niche is fighting to make external data appear inside the buyer's own platform with governance and lineage intact and nothing copied — and whoever does that takes the account, because the buyer has already chosen the platform and is choosing between its marketplace and friction.

## The Problem
A team builds a pipeline over a shared dataset that presents as an ordinary table. In production they discover it cannot be materialised into their own storage tier without a licence question, that queries against it are billed differently and more expensively than native ones, that their catalogue's lineage graph terminates at the share boundary so downstream impact analysis is blind, and that a row-level access policy they assumed applied does not traverse the share. Each difference is documented somewhere. Together they mean the abstraction leaked in four places after the team had built on it.

## Why Nobody Has Built This
Making a share fully equivalent to a native object is genuinely hard across account and organisational boundaries, particularly for governance policies that must be evaluated in the provider's context and enforced in the consumer's. The differences are individually small and documented, so each looks acceptable. Platform teams prioritise the sharing primitive's reach over its fidelity. And the consumer discovers the gaps one at a time, which never produces a single loud complaint.

## What to Build
Close the abstraction, and where it cannot be closed, surface it loudly. Make lineage traverse the share in both directions, so a consumer can trace a column to its provider origin and a provider can see which consumer assets depend on a field they are about to change — this bidirectional graph is the largest missing piece and is what makes both governance and change management possible. Propagate governance policies across the boundary with clear semantics about whose policy applies where, since the current ambiguity is a compliance exposure rather than an inconvenience. Publish a capability matrix stating exactly how a shared object differs from a native one, which is a documentation artefact that would prevent most of the late surprises and costs a day to write. Report consumption cost to the provider as well as the consumer, since a provider who cannot see that a consumer's query pattern is expensive cannot help them fix it. Give shares versioned, pinnable state so a consumer can build against a stable view, which the fix note develops. Support cross-cloud sharing properly, because the duplication it currently forces undermines the whole zero-copy proposition. And make the share's terms — permitted use, retention, redistribution — machine-readable and carried with the object rather than living in a contract.

## Target Customer
Cloud data platforms, the providers choosing which ecosystems to publish into, and the enterprises consuming shared data inside their own governance perimeter.

## Impact If Built
Bidirectional lineage across the share boundary is the largest missing piece and unlocks both impact analysis and change management. A published capability matrix costs a day and prevents most of the late surprises consumers currently discover in production.
