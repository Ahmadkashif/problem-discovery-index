# Machine Learning Opportunities — Crowdsourcing Platforms

**Industry:** [[crowdsourcing-platforms|Crowdsourcing Platforms]]
**Derived from:** [[problems/crowdsourcing-platforms/high-impact|High Impact]], [[problems/crowdsourcing-platforms/low-impact-1|Low Impact 1]], [[problems/crowdsourcing-platforms/low-impact-2|Low Impact 2]], [[problems/crowdsourcing-platforms/worker-life-1|Worker Life 1]], [[problems/crowdsourcing-platforms/worker-life-2|Worker Life 2]]

---

## 1. Completion Time Prediction and Realised Rate Disclosure
#gradient-boosting #probability-distributions #confidence-intervals #time-series-forecasting #hypothesis-testing #evaluation-metrics #worker-facing #compliance

**Problem statement:** Requesters set per-task pay from an estimate that is systematically low because they wrote the instructions and do not experience the ambiguity, the platform records exactly how long every task really takes, and neither party is shown the implied hourly rate.

**ML task:** Predict the completion time distribution for a new task from its characteristics and from comparable historical tasks, and surface the implied hourly rate at posting and at acceptance
**Input data:** Historical submission durations with task characteristics — instruction length and complexity, item type, interface interactions required, number of decisions per item; requester history; worker speed distributions; abandonment events and their timing; qualification test durations.
**Target:** The distribution of completion time for a task, and the realised hourly rate it implies at a given payment.
**Evaluation metric:** Calibration of the predicted distribution, particularly the upper quantiles — the workers most harmed are those on the slow side of a task that was underestimated, and a model accurate at the median and wrong in the tail reproduces the problem. Measure the intervention outcome directly: the proportion of requesters who raise payment when shown the implied rate, which evidence from platforms with pay guidance suggests is substantial, since the gap is mostly ignorance rather than intent.
**Scope:** Multitasking makes raw duration an overestimate for some workers, so the estimator should use the distribution across many workers rather than any individual's time, and should not be repurposed into per-worker speed monitoring. Task discovery ranked by a worker's expected rate given their own speed is the same model pointed at the other side of the market. 1 data scientist, 3-4 months.
**Data availability:** Complete and precise. This is the clearest case in the cluster of a decisive fact being computed and withheld.

---

## 2. Joint Worker Reliability and Item Difficulty Estimation
#expectation-maximization #bayesian-inference #confidence-intervals #hypothesis-testing #probability-distributions #evaluation-metrics #compliance #gradient-boosting

**Problem statement:** Quality control uses majority agreement and approval thresholds, which conflate an unreliable worker with a genuinely ambiguous item and systematically penalise minority perspectives — while the requester receives a single agreement number that diagnoses nothing.

**ML task:** Jointly estimate worker reliability and item difficulty from the response pattern, producing aggregated labels with uncertainty and separating the two sources of disagreement
**Input data:** All worker responses per item with worker identity; item characteristics; gold-standard items and their outcomes; task instructions; worker history across tasks; worker language and locale where lawfully usable for disparity analysis.
**Target:** The true label per item and a per-worker reliability estimate, validated against expert adjudication on a sample of contested items.
**Evaluation metric:** Aggregation accuracy against expert adjudication, compared against majority voting — the baseline that production platforms actually use. The essential second measurement is disparity: whether reliability estimates differ systematically by worker locale or language on culturally-dependent items, which is a documented effect and which a quality system that equates disagreement with error will convert into exclusion. Gold items that competent workers consistently fail should be flagged rather than trusted.
**Scope:** These methods are decades old in the research literature and substantially absent from production platforms, which is the notable fact. The item-difficulty output is what the requester actually needs, since it identifies their own task design problems rather than blaming the workforce. Consequences should be graduated to match the reliability of the estimate. 1-2 data scientists, 4-6 months.
**Data availability:** Complete — redundant labelling is standard practice and the response matrices already exist.

---

## 3. Instruction Ambiguity Detection Against the Requester's Own Data
#bert #large-language-models #transformers #k-means-clustering #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing

**Problem statement:** Most unusable crowd data is caused by instructions that do not resolve the edge cases in the requester's own dataset, and the person who wrote them is least able to see it — so the response is to tighten quality thresholds, which treats a design problem as a workforce problem.

**ML task:** Analyse instructions against the actual item distribution to identify unresolved cases before launch, and cluster observed disagreements by the ambiguity that produced them
**Input data:** Task instructions and decision rules; the requester's uploaded item set; historical disagreement patterns linked to instruction text; worker questions and forum discussion where accessible; comparable tasks and their instruction revisions.
**Target:** Items the instructions do not determine, confirmed by expert review; and for disagreement clustering, the specific instruction gap responsible.
**Evaluation metric:** Precision on flagged ambiguous items, since a checker that flags a third of a dataset will be ignored, and recall measured against the disagreements that actually materialise when the batch runs — which is a clean prospective test. The downstream measure is the reduction in unusable batches, since a repeated batch is a direct budget loss and is common.
**Scope:** Running this before any money is spent is the intervention with the best return in this industry, because the fix is an edited sentence rather than a rejected workforce. Automatic pilot design — selecting a small item set spanning the edge cases and reporting where interpretations diverged — is the operational form. Worker questions should be treated as signal about the task rather than as support overhead. 2 engineers, 4-6 months.
**Data availability:** Instructions and item sets are uploaded by the requester; disagreement data accumulates in every batch.

---

## 4. Rejection Legitimacy and Requester Behaviour Scoring
#gradient-boosting #bayesian-inference #confidence-intervals #hypothesis-testing #change-point-detection #evaluation-metrics #compliance #worker-facing

**Problem statement:** Rejection withholds payment for completed work and damages future earning access, frequently without a reason, often in bulk for systematic causes the worker did not create, with no independent appeal.

**ML task:** Detect batch-level rejection events distinguishable from individual quality decisions, estimate the probability that a rejection was legitimate given the submission and task specification, and score requester behaviour
**Input data:** Rejection events with timing, volume and pattern; the submissions rejected and the task specification; the requester's rejection rate relative to comparable tasks; payment speed and message responsiveness; appeal outcomes; worker history across other requesters.
**Target:** Whether a rejection was legitimate, adjudicated on a reviewed sample including appeals and platform investigations.
**Evaluation metric:** Recall on illegitimate bulk rejections is the priority, because those affect many workers at once for a cause none of them created and are the clearest injustice in the system. Precision matters for requester scoring, since an unfair reputational score has its own consequences. A worker's history across other requesters is the key discriminator — someone with consistent quality elsewhere who is rejected wholesale by one requester is evidence about the requester.
**Scope:** The decisive fixes here are policy rather than model: requiring a stated reason, decoupling payment from qualification standing, and providing appeal adjudicated by the platform rather than by the rejecting requester. The model's role is to trigger review on batch events before consequences apply, and to surface requester behaviour that workers currently maintain their own review sites to approximate. 1-2 data scientists, 4-6 months.
**Data availability:** Complete inside every platform, including the cross-requester worker histories that make the discrimination possible.
