# Machine Learning Opportunities — MLOps Platforms

**Industry:** [[mlops-platforms|MLOps Platforms]]
**Derived from:** [[problems/mlops-platforms/high-impact|High Impact]], [[problems/mlops-platforms/low-impact-1|Low Impact 1]], [[problems/mlops-platforms/low-impact-2|Low Impact 2]], [[problems/mlops-platforms/worker-life-1|Worker Life 1]], [[problems/mlops-platforms/worker-life-2|Worker Life 2]]

---

## 1. Skew Detection by Direct Computation Comparison
#change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #entropy-cross-entropy-kl-divergence #feature-engineering #data-integration #revenue-impact

**Problem statement:** The dominant failure mode of deployed machine learning is a feature computed differently at serving than at training — a null handled as zero, a timezone difference, an aggregation window offset by a day. There is no error and no alert; the model simply performs worse until a business metric moves months later.

**ML task:** Distributional comparison and exact-value replay between training and serving feature computations, with impact weighting by model attribution
**Input data:** Training feature values as materialised for the training set; serving feature values logged at prediction time; feature definitions from both paths; model feature attributions; prediction distributions; ground truth outcomes where and when they arrive.
**Target:** A per-feature discrepancy between training and serving computation, and its estimated effect on model output.
**Evaluation metric:** Detection of injected synthetic skew — deliberately perturbing a feature in the serving path and measuring time to detection — is the only rigorous way to evaluate a detector for events that are rare, unlabelled and catastrophic. Alert precision matters enormously as a secondary metric, because naive drift detection has already trained teams to ignore these alerts.
**Scope:** Replay is the technique that makes this specific rather than statistical: recompute a sample of production requests through the training pipeline and compare values exactly, producing an attributable defect rather than a distributional score. Impact weighting by feature attribution is what makes the alert survivable — a drifted feature the model barely uses is noise. Ground truth latency means direct performance monitoring is unavailable in the actionable window, so input-side comparison is not a convenience but a necessity. 3 ML engineers plus a platform engineer, 6 months.
**Data availability:** Training features are held by the training platform. Serving features are frequently not logged at all, which is the single biggest obstacle and is a product change rather than a modelling one.

---

## 2. Training Job Duration and Failure Prediction
#gradient-boosting #survival-analysis #time-series-forecasting #confidence-intervals #evaluation-metrics #feature-engineering #optimization-fundamentals

**Problem statement:** Schedulers allocate GPUs knowing requested resources and nothing about duration, actual utilisation or the probability that a job fails in the first ten minutes. Researchers over-request defensively, platform engineers arbitrate by hand, and utilisation is poor for scheduling reasons rather than physical ones.

**ML task:** Regression on job duration and peak resource usage, plus early failure classification at submission time
**Input data:** Historical job submissions with configuration (model architecture, parameter count, dataset size, batch size, precision, distributed topology), requested and actual resource usage, realised duration, exit status and failure category; hardware type; submitter and team history; cluster state at submission.
**Target:** Realised wall-clock duration, peak memory and compute utilisation, and whether the job fails within a short initial window.
**Evaluation metric:** Quantile accuracy on duration rather than mean, since a scheduler needs an upper bound it can plan against. For early failure, precision at the threshold where a job would be rejected at submission — rejecting a valid job is far worse than allowing a doomed one, so the operating point must be conservative. The business metric is realised cluster utilisation against the pre-deployment baseline.
**Scope:** Cross-customer training is the vendor's structural advantage: a single organisation has thousands of jobs while the platform has hundreds of millions, and job configurations are similar enough across organisations that transfer works well. Idle reclamation requires no prediction at all — an allocation running far under its reservation is directly observable — and should ship first. 2 ML engineers, 4-5 months.
**Data availability:** Excellent. Job configuration, resource telemetry and exit status are captured by every platform as a matter of course and are used for billing rather than for scheduling.

---

## 3. Pipeline Failure Classification and Auto-Remediation
#large-language-models #bert #k-means-clustering #gradient-boosting #evaluation-metrics #change-point-detection #workflow-orchestration #automation

**Problem statement:** Training pipeline failures cluster into a handful of repeating modes — reclaimed spot instances, out-of-memory, late upstream data, dependency resolution, expired credentials, transient network faults in distributed runs — and each one wakes an engineer who reads a log and types a retry.

**ML task:** Multiclass classification of failure cause from log text and run context, with a remediation policy attached per class
**Input data:** Failure logs across runs and customers; run configuration and resource requests; cluster and infrastructure events; upstream data availability; dependency manifests; the engineer's eventual remediation action; whether the retry succeeded.
**Target:** Failure category and the remediation that resolved it.
**Evaluation metric:** Classification accuracy per category, weighted by how consequential a misclassification is — auto-retrying a job that failed for a genuine code reason wastes compute, while paging for a reclaimed spot instance wastes an engineer's night. Report auto-remediation success rate and, most importantly, the reduction in out-of-hours pages, which is the outcome the buyer cares about.
**Scope:** The classification is straightforward; the value is entirely in the cross-customer corpus, since the same failure signatures appear across thousands of organisations and no single team has enough examples to build this well. Distributed run diagnostics — collecting and aligning worker logs to identify the originating failure — is mechanical work currently done by hand at three in the morning and needs no learning at all. 2 ML engineers, 4 months.
**Data availability:** Logs are abundant and retained. The remediation action taken by the engineer is frequently not recorded in a structured form, which is the main labelling gap and is fixable with a small workflow change.

---

## 4. Instrumentation Generation and Metric Vocabulary Reconciliation
#large-language-models #bert #word-embeddings #k-means-clustering #transfer-learning #evaluation-metrics #data-integration

**Problem statement:** Tracking is a one-line integration for supported frameworks and a bespoke project otherwise, so coverage is partial and biased toward the easy workloads. Where instrumentation is manual, the same concept is logged under three different names by three teams, which turns a central platform into parallel silos.

**ML task:** Code generation of instrumentation for unfamiliar training scripts, plus entity resolution over metric names and semantics across runs
**Input data:** The vendor's corpus of instrumented training scripts across frameworks and organisations; the target script; the organisation's existing metric vocabulary and naming conventions; metadata completeness policies; historical manual instrumentation.
**Target:** Working instrumentation consistent with the organisation's conventions; and a canonical metric identity per logged name.
**Evaluation metric:** For generation, the proportion of instrumented scripts accepted without modification and the completeness of captured metadata against policy. For vocabulary reconciliation, precision on merges judged by the platform team — conflating two genuinely different metrics corrupts cross-team comparison, which is the reason the platform exists.
**Scope:** Training scripts follow recognisable patterns and the vendor has seen millions, which makes this an unusually well-supported code generation task. Environment reconstruction — capturing enough to actually rerun a job, including data snapshot, hardware and driver versions, not just the package list — is the part reproducibility claims rest on and is inconsistently done. 2 ML engineers, 4 months.
**Data availability:** The script corpus exists across customer repositories and its use for cross-customer training requires contractual permission that standard terms may not grant, which should be checked before anything is built.
