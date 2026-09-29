# Meta-Learning and Experiment Analysis Machinery

**Niche:** [[niches/synthetic-data-providers/generation-corpus-intelligence/profile|Generation Corpus Intelligence]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated machine learning solved configuration selection from dataset characteristics years ago, and generation vendors still tune by hand on every new schema.
**Tags:** #bayesian-optimization #gaussian-processes #transfer-learning #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #automation
**Contested on:** Every serious competitor in this niche is fighting to turn the accumulated record of generation runs and their outcomes into a certification standard the field lacks — and whoever assembles it defines how the category is judged, which is worth more than any individual product in it.

## The Problem
Meta-learning is a solved shape of problem: characterise a dataset with a set of features, look up what worked on similar datasets, warm-start the search there. Automated ML systems do exactly this in production and it works well. Generation vendors, facing a new customer schema, start their configuration search from defaults and a person's recollection — which is the problem meta-learning was invented to remove, applied to an adjacent task that nobody has connected to it.

## What Already Exists
Automated machine learning with meta-learning warm starts from dataset characterisation; Bayesian and multi-fidelity hyperparameter optimisation; experiment tracking platforms holding configuration-to-outcome histories; multi-objective optimisation machinery for exactly the shape of a two-property trade-off; and surrogate modelling for expensive evaluations.

## The Customization Gap
The adaptation is to a multi-objective target where one objective is adversarial and the datasets are enterprise schemas. It requires: (1) meta-features for relational schemas rather than for single tables, since the characterisation the existing systems use is table-level and the properties that determine generation difficulty — relational depth, cardinality skew, constraint density, temporal structure — are not in it; (2) genuine multi-objective treatment producing a frontier rather than a scalarised score, because collapsing privacy and utility into one number is exactly the error the category already makes; (3) privacy evaluation as an expensive objective, since running attacks per configuration is costly and multi-fidelity methods are the natural fit and are unused here; (4) transfer across customers without moving data, since the meta-features and outcomes can be shared where the data cannot, which makes federated meta-learning unusually appropriate; and (5) surfacing the recommendation with its evidence to the solutions engineer rather than automating them out, because their judgement about what a customer cares about is the part the system does not have.

## Target Customer
Generation vendors, their solutions and research organisations, and the automated ML community for whom this is an adjacent unserved application.

## Impact If Solved
Configuration selection from dataset characteristics is solved and unused here. Relational meta-features plus multi-fidelity treatment of the expensive privacy objective is the adaptation, and outcomes transfer across customers even where the data cannot.
