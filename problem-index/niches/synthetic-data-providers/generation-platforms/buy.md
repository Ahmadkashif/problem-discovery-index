# Pipeline and Orchestration Machinery

**Niche:** [[niches/synthetic-data-providers/generation-platforms/profile|Generation Platforms]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The data engineering ecosystem already solved orchestration, lineage, versioning and artefact management, and generation vendors rebuild thin versions of all four.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #compliance #graph-theory #change-point-detection
**Contested on:** Not terminal — the contest differs by data modality, and the decomposition is recorded in the profile.

## The Problem
Every generation vendor needs scheduled runs, source connectors, artefact storage, dataset versioning, lineage and an evaluation step that gates promotion. All six are mature, well-understood products in the data engineering ecosystem with large communities and good implementations. Vendors build their own, badly, because generation was the hard part and the surrounding machinery looked like plumbing — with the result that customers get a platform whose orchestration is worse than the one they already run.

## What Already Exists
Workflow orchestrators with dependency graphs, retries, backfills and scheduling; data versioning and lineage tooling with column-level tracking; artefact and model registries; feature and dataset catalogues; data quality frameworks with assertion-based gating; and the connector ecosystem covering warehouses, lakes and operational stores.

## The Customization Gap
The adaptation is to generation as the transform. It requires: (1) the generator as a first-class lineage node, so the graph records that this dataset came from this source snapshot through this model version with this configuration and this privacy setting — which is exactly what an auditor asks and what generic lineage tools do not model; (2) evaluation results as a gate, so a run that fails its fidelity or privacy thresholds does not promote, which turns evaluation from a report into a control and is the single highest-value adaptation; (3) reproducibility guarantees strong enough to regenerate a dataset identically years later, which requires pinning more than orchestrators normally pin; (4) source drift detection, since the generator's validity depends on the source distribution it was fitted to and nothing currently watches for that; and (5) running inside the customer's environment, because the source data frequently cannot leave and a hosted orchestrator is not an option.

## Target Customer
Generation vendors, data platform teams, and the orchestration and lineage vendors for whom generation is an unserved node type.

## Impact If Solved
Generation vendors rebuild mature infrastructure badly. Treating the generator as a lineage node and evaluation as a promotion gate is the adaptation that makes synthetic data auditable, and it is available from existing tooling.
