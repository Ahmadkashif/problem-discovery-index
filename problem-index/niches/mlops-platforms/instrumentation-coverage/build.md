# One Line for the Supported, a Project for the Rest

**Niche:** [[niches/mlops-platforms/instrumentation-coverage/profile|Instrumentation Coverage]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Experiment tracking is a one-line integration for the frameworks a vendor supports and a bespoke engineering project for everything else, which is most of what a large organisation actually runs.
**Tags:** #data-integration #automation #workflow-orchestration #evaluation-metrics #graph-theory #descriptive-statistics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make tracking work on the training code an organisation actually runs rather than on the frameworks the vendor supports — and whoever does that takes the account, because the unsupported code is where the important models live.

## The Problem
A platform team rolls out a tracking product. The three teams using current frameworks are integrated in a morning. The credit risk models, which are the ones the regulator asks about, run in a pipeline written in a different language against a scheduler the vendor does not support, and integrating them is quoted as a quarter of engineering work that never gets prioritised. Two years later the platform has excellent visibility into the projects that needed it least, and the organisation's answer to what produced the model currently making lending decisions is still a person's memory.

## Why Nobody Has Built This
Vendors build adapters where their users are, which is where the newest frameworks are, and each additional adapter has worse economics than the last. The long tail is genuinely long and genuinely heterogeneous. Selling into the legacy estate means engaging teams who did not ask for the product and see it as overhead. And the coverage gap is invisible in the vendor's own metrics, which count runs tracked rather than runs that exist.

## What to Build
Capture passively from what is already there. Derive runs from the orchestrator rather than from the training code, since almost every pipeline runs under a scheduler that already knows when a job started, what parameters it received, what it read and what it wrote — which yields most of the value with no code change and is the central insight of this build. Parse the artefacts a job already produces: log files, output metrics, model files, evaluation reports, since untracked pipelines are usually verbose and the information is sitting in text nobody reads. Reconstruct lineage from storage access patterns, which gives inputs and outputs without instrumentation. Offer a minimal instrumentation tier that captures parameters and metrics with a few lines in any language, rather than an all-or-nothing adapter, because a partially tracked critical model is worth far more than an untracked one and the current products do not offer that trade. Report organisational coverage — models known to exist against models tracked — which is the number that gets the legacy work prioritised and which no vendor wants to compute. Prioritise the gap by risk rather than by ease, since the untracked estate is disproportionately the regulated one. And accept degraded fidelity honestly, marking derived runs as such, because a partial record with a known confidence is useful and a fabricated complete one is not.

## Target Customer
Platform engineering in large organisations, regulated industries with legacy modelling estates, and the tracking vendors whose coverage stalls at the frameworks they support.

## Impact If Built
Deriving runs from the orchestrator gets most of the value with no code change, which is the opposite of how every vendor approaches integration. Reporting organisational coverage is the number that would get the legacy estate prioritised and the one nobody computes.
