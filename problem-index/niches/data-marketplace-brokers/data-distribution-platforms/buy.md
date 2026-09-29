# Catalogue and Entitlement Infrastructure

**Niche:** [[niches/data-marketplace-brokers/data-distribution-platforms/profile|Data Distribution Platforms]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software marketplaces and content licensing platforms solved catalogue structure, entitlement and metered delivery years ago, and data marketplaces rebuilt the listing page.
**Tags:** #data-integration #compliance #workflow-orchestration #automation #graph-theory #evaluation-metrics #revenue-impact #quick-win
**Contested on:** Not terminal — the contest differs by whether the platform is delivering data or finding it, and the decomposition is recorded in the profile.

## The Problem
Running a marketplace where a catalogue is searchable on structured attributes, entitlements are enforced at delivery, usage is metered against a licence, and the terms attached to an item travel with it is a solved problem in software distribution, media licensing and API marketplaces. Data marketplaces implemented the catalogue as a list of descriptions and the licence as a document attached to a transaction.

## What Already Exists
Package registries with structured metadata, dependency declarations and versioning; software marketplaces with entitlement enforcement and metered billing; content licensing platforms with rights management travelling alongside assets; API marketplaces with quota and usage enforcement; and digital rights expression languages for machine-readable permissions.

## The Customization Gap
The adaptation is to an item whose value depends on properties nobody has measured and whose licence constrains use rather than distribution. It requires: (1) catalogue attributes that are verifiable rather than self-declared, since a package's version is a fact and a dataset's coverage claim is currently an assertion — closing that gap is what distinguishes a data catalogue from a listings page; (2) rights expressed machine-readably over use rather than over copying, because the permitted-use question here is whether a buyer may train a model or resell a derivative, which the rights languages were not designed to express and which is the live commercial question; (3) entitlement enforcement that survives the data leaving the platform, which is the hard part and where digital rights machinery mostly fails; (4) metering on derived use rather than on download, since a dataset downloaded once may be used for years across many purposes; and (5) versioning of datasets that change continuously rather than being republished, which the package model handles badly.

## Target Customer
Data marketplaces, cloud platforms, brokers, and the rights management and marketplace infrastructure communities.

## Impact If Solved
Marketplace machinery is mature and assumes verifiable catalogue attributes and rights over copying. Expressing permitted use — may this train a model — machine-readably is the live commercial question and no existing rights language answers it.
