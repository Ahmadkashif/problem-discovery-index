# Schema Matching and Ontology Alignment

**Niche:** [[niches/web-data-extraction-firms/cross-source-normalisation/profile|Cross-Source Normalisation]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Schema matching and ontology alignment have decades of methods for reconciling heterogeneous representations of the same domain, and web extraction reconciles by hand or not at all.
**Tags:** #graph-theory #k-nearest-neighbors #large-language-models #evaluation-metrics #bayesian-inference #data-integration #word-embeddings #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn a thousand sites' worth of the same entity into one coherent dataset — and whoever does that takes the account, because that reconciliation is the work customers assume they are buying.

## The Problem
Determining that one source's field corresponds to another's, and that one taxonomy's category maps to another's, is the schema matching and ontology alignment problem, studied extensively with methods combining name similarity, structural context, instance data and now language models. There are evaluation campaigns and mature implementations. Web extraction firms, who face the largest instance of this problem anywhere, map by hand when they map at all.

## What Already Exists
Schema matching with name, structure and instance-based methods; ontology alignment with published evaluation campaigns and benchmark datasets; instance-based matching using value distributions; embedding-based semantic similarity for field and category names; and holistic matching across many schemas simultaneously.

## The Customization Gap
The adaptation is to a thousand sources, each small, all describing the same domain. It requires: (1) holistic matching across all sources at once rather than pairwise into a canonical schema, since the mass of sources is itself evidence — a field appearing in six hundred sites with a consistent value distribution is strongly identified, and pairwise matching throws that away; (2) instance-based matching as the primary signal, because site field names are frequently absent or meaningless while the values are highly informative; (3) taxonomy alignment at scale, which is the ontology alignment problem with a thousand small ontologies rather than two large ones and is where the volume helps rather than hurts; (4) continuous re-matching, since sites change their structure and a one-time alignment decays; and (5) confidence-aware output, since some mappings are certain and some are judgement, and delivering both as equally normalised is how trust is lost.

## Target Customer
Extraction firms, data teams building normalisation themselves, and the schema matching and ontology alignment research community, for whom this is an unusually large real instance.

## Impact If Solved
This industry faces the largest instance of a well-studied problem and solves it by hand. Holistic matching across a thousand sources uses the mass of sources as evidence, which pairwise mapping into a canonical schema discards.
