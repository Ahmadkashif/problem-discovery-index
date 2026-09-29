# Record Linkage and Master Data Management

**Niche:** [[niches/data-marketplace-brokers/schema-and-entity-resolution/profile|Schema & Entity Resolution]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Record linkage has seventy years of statistical foundation and master data management is a mature product category, and neither is aimed at reconciling external providers.
**Tags:** #bayesian-inference #k-nearest-neighbors #probability-distributions #hypothesis-testing #evaluation-metrics #data-integration #graph-theory #expectation-maximization
**Contested on:** Every serious competitor in this niche is fighting to make four providers covering the same entities into one coherent view without the buyer writing four pipelines and a resolution layer — and whoever does that takes the account, because every multi-source buyer builds this and nobody sells it.

## The Problem
Deciding whether two records describe the same entity is one of the oldest studied problems in applied statistics, with a formal probabilistic framework, established parameter estimation methods and strong open implementations. Master data management productised the operational side — golden records, survivorship rules, stewardship workflows — for enterprise data. The combination is exactly what a multi-provider buyer needs, and both were built assuming the buyer owns the sources.

## What Already Exists
Probabilistic record linkage with formal theory and parameter estimation; blocking and indexing techniques for scale; open linkage implementations with active development; master data management platforms with survivorship rules and stewardship; graph-based entity resolution for transitive matching; and clustering approaches for multi-source resolution.

## The Customization Gap
The adaptation is to sources the buyer cannot change and cannot inspect. It requires: (1) survivorship rules informed by measured per-field provider accuracy rather than by a configured preference order, since the buyer has no internal authority to appeal to and the disagreements are the only evidence available — this is the substantive change; (2) resolution across many sources simultaneously with transitive and conflicting evidence, where graph-based approaches apply and the pairwise framework struggles; (3) linkage on the identifiers providers actually supply, which are frequently weak and proprietary, rather than on the clean demographic fields the classical work assumes; (4) incremental resolution as sources refresh on different cadences, which enterprise master data management handles poorly and which is the normal condition here; and (5) resolution quality measured without ground truth, since no authoritative answer exists and the usual evaluation approach is unavailable.

## Target Customer
Data engineering teams, master data management vendors for whom external providers are an unserved case, and the record linkage research community.

## Impact If Solved
Both disciplines assume the buyer owns the sources, which is the one thing that is not true here. Survivorship driven by measured per-field provider accuracy replaces a configured preference order with evidence, which is the only authority available.
