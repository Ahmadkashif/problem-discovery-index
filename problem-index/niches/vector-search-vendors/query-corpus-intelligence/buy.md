# Meta-Learning and Configuration Transfer

**Niche:** [[niches/vector-search-vendors/query-corpus-intelligence/profile|Query & Corpus Intelligence]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated machine learning built meta-learning to warm-start configuration from dataset characteristics, and vector vendors have the ideal corpus for it and ship a quickstart example.
**Tags:** #bayesian-optimization #gaussian-processes #transfer-learning #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #dimensionality-reduction
**Contested on:** Every serious competitor in this niche is fighting to turn what they see across every deployment — queries, returned sets, corpora, outcomes — into empirical answers about chunking, embedding and configuration, and whoever does that stops competing on cost per vector.

## The Problem
Choosing a configuration for a new dataset by looking up what worked on similar datasets is exactly what meta-learning does, and it is a mature technique with published methods and production deployments. A vector vendor has thousands of corpora with configurations and outcomes attached, which is a better meta-learning corpus than most of the research was conducted on, and uses it to write a documentation example.

## What Already Exists
Meta-learning with dataset meta-features and warm-started search; Bayesian optimisation with transfer across related tasks; multi-fidelity optimisation for evaluating candidates cheaply before committing; collaborative filtering approaches to configuration recommendation; and the automated ML systems that productised all of it.

## The Customization Gap
The adaptation is to a corpus the vendor can characterise without reading it. It requires: (1) meta-features computable from metadata and aggregate statistics rather than from content, since the vendor frequently cannot inspect customer documents and privacy-preserving characterisation is a hard constraint the research does not consider — solving it is the enabling piece; (2) the objective as retrieval quality rather than model accuracy, which requires the quality measurement the category also lacks, making these two builds mutually reinforcing; (3) multi-objective treatment across quality, latency and cost, since a configuration recommendation that ignores the budget is not actionable; (4) transfer across deployments without moving data, where meta-features and outcomes aggregate even when corpora cannot, making a federated approach unusually natural here; and (5) recommendations delivered with their evidence and comparable deployments named in aggregate, because this buyer will not accept an opaque suggestion about their production configuration.

## Target Customer
Vector search vendors, their customers, and the automated ML community for whom this is an adjacent corpus nobody is using.

## Impact If Solved
The vendors hold a better meta-learning corpus than most of the research used and ship a quickstart. Privacy-preserving corpus meta-features are the enabling piece, and the recommender and the quality measurement each make the other possible.
