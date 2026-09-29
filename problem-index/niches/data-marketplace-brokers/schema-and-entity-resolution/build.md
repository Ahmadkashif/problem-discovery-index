# Four Pipelines and a Layer Nobody Sells

**Niche:** [[niches/data-marketplace-brokers/schema-and-entity-resolution/profile|Schema & Entity Resolution]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every data integration tool on the market will map one schema to another, and a buyer combining four providers covering the same entities still writes four bespoke pipelines and an entity resolution layer nobody sells.
**Tags:** #k-nearest-neighbors #bayesian-inference #graph-theory #evaluation-metrics #data-integration #probability-distributions #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to make four providers covering the same entities into one coherent view without the buyer writing four pipelines and a resolution layer — and whoever does that takes the account, because every multi-source buyer builds this and nobody sells it.

## The Problem
A company buys company data from four providers to get better coverage. Provider A identifies companies by their own internal key, B by a registration number, C by a proprietary identifier, D by name and address. The same company appears in all four with three spellings, two addresses and different industry codes. The team writes four loaders, then spends four months building a resolution layer that decides which records are the same entity and which provider's value to trust for each field. That layer is the actual project, it is rebuilt at every company doing this, and no vendor offers it because integration tools stop at mapping.

## Why Nobody Has Built This
Master data management platforms exist and are aimed at reconciling a company's own internal systems, where the buyer controls the sources and can change them — a materially different problem from reconciling external providers who will not change anything. Providers have no incentive to make themselves substitutable. The canonical model differs by domain, so a general product needs a per-domain investment. And each buyer believes their entity model is specific to them, which is partly true and mostly not.

## What to Build
Build the resolution layer as a product, per domain. Publish a canonical entity model for the common domains — companies, places, people, products, properties — since every buyer invents one and they converge on nearly the same thing, which makes this the reusable core rather than the custom part. Maintain identifier crosswalks between provider identifier schemes, which is the single most valuable artefact available here and is accumulable across customers even where the data is not. Provide probabilistic resolution with tunable precision and recall, since the right operating point differs by use — a marketing merge and a compliance merge want opposite errors — and a fixed threshold serves neither. Make merge policy declarative per field, so a buyer states which provider to trust for which attribute rather than hard-coding it, and can change it without rewriting a pipeline. Measure provider accuracy per field from disagreements, which the fix note develops and which makes merge policy evidence-based. Report marginal coverage contribution per provider, so a buyer can see that their fourth source adds two percent and stop paying for it — a measurement no incumbent will produce and which buyers want badly. Support incremental resolution as sources update, since a full rebuild on every refresh is what makes these pipelines fragile. And ship the loaders for common providers, because the schema mapping really is mechanical and doing it once serves everyone.

## Target Customer
Data engineering teams combining multiple providers, the sourcing functions buying them, and the marketplaces whose buyers stall at integration.

## Impact If Built
The resolution layer is the actual project in every multi-source data programme and no vendor sells it. Identifier crosswalks accumulate across customers even where data cannot, and marginal coverage contribution tells a buyer which provider to stop paying for.
