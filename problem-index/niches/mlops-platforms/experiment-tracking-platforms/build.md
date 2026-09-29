# An Interface That Spans Two Unrelated Contests

**Niche:** [[niches/mlops-platforms/experiment-tracking-platforms/profile|Experiment Tracking Platforms]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Vendors sell one tracking product to teams running ten thousand cheap sweeps and to teams running one sixty-day distributed job, and almost nothing that matters to either is shared with the other.
**Tags:** #data-integration #evaluation-metrics #workflow-orchestration #automation #descriptive-statistics #time-series-forecasting #graph-theory #compliance
**Contested on:** Not terminal — the contest differs by workload scale, and the decomposition is recorded in the profile.

## The Problem
A vendor demonstrates the same dashboard to a data science team and to a foundation model infrastructure team. The first asks how to find which of last quarter's four hundred runs used the feature set they are trying to reproduce. The second asks what happens to the ingest path when one thousand ranks each emit metrics every step, and whether the tool can tell them that rank 617 is running eleven percent slow. The product answers neither well, because it was built for the average of two workloads that have no average.

## Why Nobody Has Built This
The single-product positioning addresses a larger market and the interface genuinely is common — log a scalar, view a chart — which makes the divergence easy to miss until deployment. Large-scale training arrived recently enough that the incumbents' architectures predate it, and retrofitting an ingest path built for thousands of points per run to handle millions per minute is a rewrite rather than a feature. And the classical workload still pays most of the bills, which makes it the safe thing to optimise for.

## What to Build
Build the shared substrate honestly and the two front ends separately. What genuinely is common — identity, access control, artefact storage, lineage, the metadata model, integration with the code and data versions — should be one system and is usually the weakest part of both products, which makes it the real opportunity at this level. Model the lineage graph properly: run to code commit to data version to parent run to produced artefact to deployed model, queryable in both directions, since that is scale-independent and is what makes an audit or a rollback tractable. Separate the metric ingest path from the metadata path architecturally, because their volume characteristics differ by orders of magnitude and coupling them is what forces the compromise. Make the sweep and the distributed run first-class distinct objects rather than both being a bag of runs, since the questions asked of each have different shapes. Support organisational hierarchy over runs — project, team, initiative — which every organisation improvises with naming conventions. And be explicit with customers about which workload the product is strong at, because the alternative is being chosen for the one it is weak at and losing the account later.

## Target Customer
Data science and ML infrastructure organisations, and the tracking vendors currently serving both with one product.

## Impact If Built
The genuinely shared layer — identity, lineage, artefact provenance — is the weakest part of both products and the only part that legitimately generalises. Separating metric ingest from metadata is what removes the architectural compromise the single-product framing forces.
