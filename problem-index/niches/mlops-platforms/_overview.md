# Niche Analysis — MLOps Platforms

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Training–Serving Consistency | 🔵 High Market Share | $680M | None — both computations are held and never compared | ML engineering and platform teams |
| 2 | Experiment Tracking Platforms | 🔵 High Market Share | $820M | High | Research teams; separately, ML infrastructure teams |
| 3 | Feature Coverage & Lineage | 🟠 Low Digitized | $290M | Low — the guarantee holds for a minority of features | Data and ML platform teams |
| 4 | Instrumentation Coverage | 🟠 Low Digitized | $240M | Low — one line for supported frameworks, a project for the rest | Platform engineering |
| 5 | The On-Call ML Engineer | 🟣 Underserved Audience | $180M | None — paged to read logs | ML engineering, and the leaders losing them |
| 6 | The Cluster Arbitrator | 🟣 Underserved Audience | $210M | None — scheduling by negotiation | Platform and ML infrastructure teams |
| 7 | Drift & Degradation Detection | ⚡ Highly Automatable | $310M | Low — a separate category because the platforms did not extend | Model owners and the business functions they serve |
| 8 | Run Corpus Intelligence | ⚡ Highly Automatable | $230M | None — millions of runs, shipped as a chart | The vendors themselves |

## Why These Niches

The category solved recording and has not solved concluding. Training–serving skew is the most common expensive failure in applied machine learning, the platforms hold both the training computation and the serving computation, and none of them compares the two — which makes it the largest contested surface in the industry and the one a buyer would switch for.

Experiment tracking **failed the filter as one niche**. A team running ten thousand cheap sweeps is fighting over comparison, reproducibility and search efficiency across a large population of runs. A team running one distributed training job for sixty days across a thousand accelerators is fighting to notice a diverging loss curve at hour forty and to recover from a node that degraded silently rather than failing. Different techniques, different buyers, different failure modes, different competitive alternatives. Decomposed below.

The two underdigitised areas are coverage problems, and both have the same shape: a guarantee that holds inside a boundary and is silently absent outside it. Feature stores deliver consistency for features defined in them, which is a minority of what any real model uses. Tracking integrates in one line for the frameworks a vendor supports and becomes a bespoke project for everything else, which is most of what a large organisation runs.

The two underserved constituencies are the ML engineer paged at unsociable hours for a pipeline failure the platform recorded and did not diagnose, and the platform engineer arbitrating cluster access between researchers using a scheduler that knows nothing about duration or likely outcome.

The automation niches are the degradation detection that became a separate industry because the training platforms declined to extend into it, and the corpus of millions of training runs that would answer empirically what the field currently answers with folklore.

## Niches
- [[niches/mlops-platforms/training-serving-consistency/profile|🔵 Training–Serving Consistency]]
- [[niches/mlops-platforms/experiment-tracking-platforms/profile|🔵 Experiment Tracking Platforms]]
  - [[niches/mlops-platforms/classical-ml-experimentation/profile|🎯 Classical ML Experimentation]]
  - [[niches/mlops-platforms/large-scale-training-runs/profile|🎯 Large-Scale Training Runs]]
- [[niches/mlops-platforms/feature-coverage-and-lineage/profile|🟠 Feature Coverage & Lineage]]
- [[niches/mlops-platforms/instrumentation-coverage/profile|🟠 Instrumentation Coverage]]
- [[niches/mlops-platforms/the-on-call-ml-engineer/profile|🟣 The On-Call ML Engineer]]
- [[niches/mlops-platforms/the-cluster-arbitrator/profile|🟣 The Cluster Arbitrator]]
- [[niches/mlops-platforms/drift-and-degradation-detection/profile|⚡ Drift & Degradation Detection]]
- [[niches/mlops-platforms/run-corpus-intelligence/profile|⚡ Run Corpus Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Experiment Tracking Platforms** is not: it names the product every vendor sells rather than a contest, and the two workloads inside it share an interface and nothing else. Classical ML experimentation is won on making a large population of cheap runs comparable, reproducible and searchable, and is bought by data science organisations whose alternative is a spreadsheet and a naming convention. Large-scale training is won on observing and surviving a single run that costs more than the platform does, and is bought by ML infrastructure teams whose alternative is a bespoke stack of custom telemetry. The scale, the failure modes, the buyers and the alternatives are all different. Decomposed into two contested sub-niches.

Two candidates were rejected. *LLM and prompt observability* was rejected because its contest — evaluating and tracing non-deterministic generative applications — belongs to the LLM application tooling industry covered separately in this vault, and restating it here would duplicate it. *Model registry* was rejected as a storage and versioning feature inside every platform rather than a market anybody competes for on its own.
