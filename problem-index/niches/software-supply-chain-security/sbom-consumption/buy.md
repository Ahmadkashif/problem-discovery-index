# Master Data Management for Component Identity

**Niche:** [[niches/software-supply-chain-security/sbom-consumption/profile|SBOM Consumption]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reconciling the same entity across documents from different sources is master data management, mature for decades, and component identity across bills of materials is matched by string comparison.
**Tags:** #graph-theory #word-embeddings #k-nearest-neighbors #bert #evaluation-metrics #confidence-intervals #data-integration #compliance
**Contested on:** Every serious competitor here is fighting to make a software bill of materials answer a question somebody actually has — and whoever does that takes the mandate, because the documents are generated, filed and read by nobody.

## The Problem
Two vendors supply documents listing the same library. One identifies it by an ecosystem package name, one by a vendor-product-version triple, one by a file hash, and one by a name with a different capitalisation and a vendor prefix. Matching them is the same problem master data management has solved for customer and product records for decades. Component identity in this ecosystem is matched by comparing strings, which means an organisation querying their index for an affected component finds some of the instances and believes it has found all of them.

## What Already Exists
Master data management platforms with matching, survivorship and golden-record methodology; probabilistic record linkage; package identifier specifications designed for exactly this purpose and inconsistently adopted; the vulnerability identifier ecosystems and their mappings; and hash-based identity where artefacts are available.

## The Customization Gap
The adaptation is to software components with several competing identity schemes. It requires: (1) a resolution strategy across identifier types, treating package identifiers, vendor triples, hashes and names as several partial views of one entity rather than as alternatives — which is the core modelling decision and is what determines whether a query is complete; (2) version range reasoning, since a document states a version and a vulnerability affects a range, and matching requires comparing them correctly across ecosystems whose version semantics differ; (3) explicit handling of unmatched components, because the dangerous outcome is a query that silently misses an instance, and reporting unmatched entries is what makes the index's completeness visible; (4) transitive completeness assessment, since many documents cover only direct dependencies and a query over them will miss the deeper component — which the consumer must know; and (5) confidence on every match, since acting on a false match wastes effort and acting on the absence of a true one is a security failure, and the two errors have different costs.

## Target Customer
Supply chain security vendors building the consumption side, master data management vendors for whom this is an adjacent domain, and the security and procurement functions holding the documents.

## Impact If Solved
A mature reconciliation discipline addresses exactly the identity problem that makes a bill-of-materials index unreliable, and the field matches strings. Reporting unmatched entries is what turns a silently incomplete answer into a known one.
