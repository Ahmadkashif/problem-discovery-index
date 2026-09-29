# Instrumentation Coverage Across Frameworks

**Industry:** [[mlops-platforms|MLOps Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Experiment tracking is a one-line integration for the frameworks a vendor supports and a bespoke engineering project for everything else, which is most of what a large organisation actually runs.
**Tags:** #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration #automation #large-language-models #transformers

## The Problem
Experiment tracking works beautifully in the demo. Import the library, add a line, and every metric, hyperparameter, artefact and system statistic is captured with lineage attached.

The demo uses PyTorch with a standard training loop. The organisation runs PyTorch, JAX, three versions of TensorFlow, a large amount of scikit-learn, XGBoost in a Spark job, an R model that a biostatistician maintains, a simulation written in C++, and a fine-tuning pipeline that calls a third-party API. Some of these have first-class integrations, some have community ones of varying quality, and several have none.

Where integration is missing, someone writes the instrumentation. It works until the framework updates. Where integration is partial, the captured metadata is inconsistent — one team's runs have full lineage and another's have a metric and a name — which makes cross-team comparison, the entire point of a central platform, impossible.

The result is a tracking platform that covers the workloads that were easy to cover, and a long tail of untracked work that is frequently the production-critical part.

## What Already Exists
MLflow, Weights & Biases, Comet and Neptune all provide integrations for major frameworks, autologging where the framework permits, and generic APIs for manual instrumentation. OpenTelemetry provides a standard for general observability. Container and environment capture is standard. Artifact stores handle model and dataset versioning.

## The Customisation Gap
Autologging depends on framework hooks, and where those do not exist the fallback is manual instrumentation with no enforcement of what gets recorded. Nothing validates that a run captured the metadata the organisation's policy requires, so lineage completeness is a matter of individual diligence.

Instrumentation generation is the unexploited opportunity. Training scripts follow recognisable patterns, and the vendor has seen millions of them; proposing the instrumentation for an unfamiliar script — what to log, where, with what names consistent with the organisation's existing runs — is a well-shaped code task on a corpus the vendor already holds.

Naming and schema drift is the quieter failure. The same concept is logged as `val_loss`, `validation_loss` and `eval/loss` by three teams, which makes the central platform a set of parallel silos. Reconciling metric semantics across runs is entity resolution over a vocabulary and is not attempted.

Environment reconstruction is the third gap: capturing enough to actually rerun a training job — not just the package list but the data snapshot, the hardware, the driver version — is inconsistently done and is what reproducibility claims rest on.

## Impact If Solved
A tracking platform is only as useful as its coverage, and partial coverage produces the specific failure of a system everyone half-uses. Generating instrumentation and enforcing metadata completeness turns a voluntary practice into infrastructure, which is what teams believed they were buying.
