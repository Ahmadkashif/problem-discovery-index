# Generated, Filed, Never Read

**Niche:** [[niches/software-supply-chain-security/sbom-consumption/profile|SBOM Consumption]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** SBOM generation is standardised, automated and increasingly mandated, and the documents are produced, filed and never read — because the tooling generates them and nothing consumes them.
**Tags:** #graph-theory #bert #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #data-integration
**Contested on:** Every serious competitor here is fighting to make a software bill of materials answer a question somebody actually has — and whoever does that takes the mandate, because the documents are generated, filed and read by nobody.

## The Problem
A serious vulnerability is published in a widely used library. A security team needs to know which of the two hundred vendor products they run contain it. They hold bills of materials for perhaps sixty of those products, in two formats, in a procurement folder, describing versions that may or may not be the ones deployed. Answering the question means opening files. They instead email two hundred vendors and wait a week, which is what every organisation does, and which is the exact situation the mandate was created to prevent.

## Why Nobody Has Built This
The regulation created a production obligation and no consumption obligation, so the entire tooling ecosystem formed on the generation side where the requirement is. Consumption requires ingesting documents in two formats with inconsistent component identifiers, normalising them, and resolving which product version is actually deployed — which is unglamorous integration work with no regulatory forcing function. The receiving organisations treat the documents as compliance artefacts to be retained rather than as data to be used, because that is what the requirement asked for. And nobody has asked whether any question has ever been answered from one.

## What to Build
Build the consumption side. Ingest received documents automatically from wherever they arrive, normalise the formats, and index them — which is the missing infrastructure and turns a folder into a queryable inventory. Resolve component identity across documents, since the same library is identified differently by different vendors and unmatched identifiers make the index useless; this is the entity resolution problem again and is the substantial analytical work. Join to what is actually deployed, so the index describes the versions in the estate rather than the versions a vendor documented at some point. Answer the questions directly: which products contain this component, which of our own products would require a customer notification, what is in this thing we are considering buying. Alert on publication, so that a new vulnerability produces the affected-product list automatically rather than a week of emails. Track document coverage and currency — which vendors have supplied one, for which versions, how old — which is the honest picture of what the organisation can actually answer and is currently unknown. Request them systematically as part of procurement rather than accepting whatever arrives. And feed the transitive depth question honestly, since many supplied documents cover only direct dependencies and the component that matters is frequently deeper.

## Target Customer
Security, procurement and compliance functions receiving these documents; the vendors obliged to produce them who would prefer the obligation to be useful; and the supply chain security vendors whose products stop at generation.

## Impact If Built
An entire production ecosystem exists with no consumption side, which means a regulatory mandate is satisfied and its purpose is not. Ingestion, normalisation and component identity resolution are the missing infrastructure, and the publication-triggered affected-product list is the capability the mandate was created to enable.
