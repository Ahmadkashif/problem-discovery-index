# Ownership and Control Inference Beyond the Published Lists

**Niche:** [[niches/customs-brokers/sanctions-screening-data-providers/profile|Sanctions & Restricted Party Screening Data]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Sanctions attach to entities a designated party owns or controls, the authorities publish almost none of those relationships, and the industry's answer is analysts researching ownership one company at a time.
**Tags:** #graph-neural-networks #graph-theory #bert #transformers #contrastive-learning #probability-distributions #confidence-intervals #evaluation-metrics #compliance #data-integration

## The Problem
Screening against a published list is the easy part and is not where the exposure lies. Sanctions regimes extend to entities owned or controlled by designated parties, frequently at thresholds that make indirect and aggregated ownership decisive, and the authorities publish the designations rather than the ownership graph. Establishing that a supplier is majority-owned through three intermediate holdings by a designated person is research: corporate registries in many jurisdictions, in many languages, with varying disclosure and frequent deliberate obscuring. Analysts do it entity by entity, prioritized by prominence, which means coverage is deep on well-known networks and thin on exactly the structures built to avoid attention.

## Why Nobody Has Built This
Ownership data is fragmented across national registries with inconsistent availability, formats, and languages, and much of the relevant structure sits in jurisdictions that disclose little. Inference across partial information is also a probabilistic exercise, and the industry has been reluctant to publish probabilistic conclusions in a domain where a false positive blocks legitimate trade and a false negative is a criminal exposure — so the safe posture has been to assert only what a researcher directly verified. That posture is defensible per entity and produces systematically incomplete coverage in aggregate.

## What to Build
An ownership and control graph maintained as a modelled asset rather than as a set of verified assertions. Registry data, filings, litigation records, procurement disclosures, and trade records are ingested and resolved into a graph where ownership paths carry explicit confidence, aggregated up chains as the regimes actually compute them. Where a path is inferred rather than documented, the system says so and says on what basis — which is what makes probabilistic output usable in a compliance function rather than dangerous. Control is modelled separately from ownership, since regimes attach to both and control frequently exists without an ownership path at all. The highest-value output is prioritization: which entities in a client's counterparty set have ownership structures that warrant human research, ranked by inferred exposure, which is how a research team of a few hundred can cover a universe of millions rather than working alphabetically through the prominent ones.

## Target Customer
Heads of research operations and content at screening data providers running 300-1,500 analysts, and the trade compliance leaders at importers and brokers who screen against published lists and carry the ownership exposure themselves.

## Impact If Built
Addresses the part of sanctions compliance that actually produces enforcement actions, which published-list screening does not touch. The ownership graph is also the strongest possible moat in this segment — the lists are public and identical for every vendor, and what a provider knows about ownership is the only thing that differentiates one screening product from another.
