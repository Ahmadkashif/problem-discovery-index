# Clinical and Financial Ontologies That Already Encode the Rules

**Niche:** [[niches/synthetic-data-providers/regulated-domain-generation/profile|Regulated Domain Generation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medicine and finance spent decades formalising what codes mean and which combinations are valid, and generation vendors read none of it.
**Tags:** #graph-theory #bayesian-inference #evaluation-metrics #compliance #data-integration #probability-distributions #decision-trees #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to produce records a domain expert cannot tell are impossible — and whoever does that takes the account, because in a regulated domain a single implausible record ends the evaluation.

## The Problem
Clinical terminologies encode relationships between conditions, procedures, anatomy and substances in machine-readable form, with sex and age applicability, hierarchies, and explicit exclusions. Billing systems publish edits that declare which code pairs cannot be submitted together. Drug databases carry dosing ranges, interactions and contraindications. Financial reporting taxonomies declare which fields must reconcile. All of it is published, maintained and machine-readable, and it encodes exactly the impossibilities a generator keeps producing.

## What Already Exists
Clinical terminologies and ontologies with formal relationship models; procedural and diagnostic coding systems with published validity edits and mutually exclusive pairings; laboratory observation terminologies with reference ranges; drug knowledge bases with dosing, contraindication and interaction data; financial reporting taxonomies with declared calculation relationships; and terminology servers that make all of it queryable.

## The Customization Gap
The adaptation is turning reference knowledge into a generation constraint. It requires: (1) translating ontology relationships into generation-time constraints, which is a real engineering exercise because the sources are built for coding, validation and reimbursement rather than for sampling — but the knowledge is already there and extracting it is far cheaper than eliciting it; (2) distinguishing a hard constraint from a soft one, since an ontology's exclusion is absolute while a reference range is a distribution and treating both as hard produces a cohort with no abnormal results, which is clinically useless; (3) handling local coding practice, because real records are full of institution-specific usage that is technically invalid and genuinely present, and a generator that only produces canonically correct codes is unrealistic in the other direction; (4) versioning, since these systems update on a schedule and a dataset generated under last year's edition will be checked against this year's; and (5) covering the vertical's actual mix, since a health system's data spans clinical, billing, laboratory and pharmacy sources, each governed by a different terminology, and the impossible records are frequently the ones that cross between them.

## Target Customer
Generation vendors serving healthcare and financial verticals, health system and payer data teams, and clinical informatics functions.

## Impact If Solved
The impossibilities are already formally specified and freely published, and the category does not consume them. Distinguishing hard exclusions from soft reference ranges is the adaptation that keeps the rare-but-real cases the buyer came for.
