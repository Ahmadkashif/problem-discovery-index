# Machine Learning Opportunities — Data Labeling Services

**Industry:** [[data-labeling-services|Data Labeling Services]]
**Derived from:** [[problems/data-labeling-services/high-impact|High Impact]], [[problems/data-labeling-services/low-impact-1|Low Impact 1]], [[problems/data-labeling-services/low-impact-2|Low Impact 2]], [[problems/data-labeling-services/worker-life-1|Worker Life 1]], [[problems/data-labeling-services/worker-life-2|Worker Life 2]]

---

## 1. Latent Truth and Annotator Reliability Estimation
#bayesian-inference #expectation-maximization #maximum-likelihood-estimation #confidence-intervals #hypothesis-testing #evaluation-metrics #tacit-knowledge-ml

**Problem statement:** Annotation quality is assured by majority vote, which is meaningful for bounding boxes and near-useless for expert judgement where three qualified people routinely disagree without any of them being wrong. The industry's most expensive product is delivered with its weakest quality signal, and majority vote systematically selects the conventional answer on exactly the hard cases that make the data valuable.

**ML task:** Joint latent variable estimation of item truth, item difficulty and per-annotator reliability from a disagreement matrix, with behavioural covariates
**Input data:** Every annotation event with annotator identity, item, response, time on task, revision history, reference material consulted; reviewer verdicts; the annotator's full history across projects; item metadata and source; guideline version in force at annotation time.
**Target:** Latent item label with posterior uncertainty, plus per-annotator reliability parameters that vary by task type rather than being global.
**Evaluation metric:** On tasks where a defensible external answer exists — a held-out expert panel, a verifiable computation, a downstream measurable outcome — compare recovered labels against it and against majority vote, which is the honest baseline. Report calibration of the posterior explicitly, since the deliverable is uncertainty rather than a label. Track separately how the advantage over majority vote scales with item ambiguity, because that is where the entire value sits.
**Scope:** The statistical machinery is decades old and well understood; the obstacle is data pooling across customers, which contracts generally prohibit. A version confined to reliability estimation across one customer's projects is still valuable and is where this starts. Separating irreducible ambiguity from annotator error is the genuinely novel modelling contribution and requires items with deliberately varied difficulty. 2-3 ML engineers plus a measurement statistician, 5-6 months.
**Data availability:** Excellent in volume and fragmented by contract. Behavioural signals (time, revisions) are captured by every annotation tool and almost never used. Downstream model performance attributable to specific batches — the only real validation — is rarely returned by customers.

---

## 2. Guideline Ambiguity Detection
#large-language-models #bert #word-embeddings #hypothesis-testing #k-means-clustering #evaluation-metrics #confidence-intervals

**Problem statement:** Most annotation disputes trace to a guideline clause that two careful people read differently. The cost lands on the contributor as a rejection and on the delivery manager as an escalation, and the underlying rule is never identified or fixed.

**ML task:** Attribution of disagreement to specific guideline clauses, combined with retrieval linking annotated items to the rules that govern them
**Input data:** Guideline documents with version history; annotation disagreements and their items; contributor dispute submissions with free-text reasoning; reviewer rejection reasons; item content; agreement rates before and after each guideline revision.
**Target:** A ranked list of guideline clauses generating disproportionate disagreement, with representative disputed items attached.
**Evaluation metric:** Agreement rate improvement following clarification of flagged clauses, measured as a before-and-after on comparable items — the intervention is the test. Precision on flagged clauses as judged by the guideline authors, reported alongside, since a flagged clause that turns out to be clear costs author time.
**Scope:** The mapping from item to governing clause is the hard part and is best handled by retrieval over the guideline conditioned on item content, rather than by asking annotators to cite clauses, which they will not do reliably. Contributor dispute text is the richest signal here and is currently discarded after adjudication. Guideline revisions should be treated as interventions and measured, which requires only that revision timestamps be joined to agreement series. 2 ML engineers, 4 months.
**Data availability:** Guidelines and their versions exist. Dispute text exists and is typically stored in a support system disconnected from the annotation pipeline, which is the main integration obstacle.

---

## 3. Screening Signal Validation and Adaptive Item Rotation
#logistic-regression #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #change-point-detection #feature-engineering

**Problem statement:** Expert workforce assembly is the binding constraint on the industry's most valuable contracts. Screening tests are authored on a subject expert's intuition, never validated against the outcome they exist to predict, and leak to contributors within weeks of deployment.

**ML task:** Predicting subsequent measured annotation quality from screening signals, plus statistical detection of compromised test items
**Input data:** Applicant claimed credentials and verification results; screening test responses and per-item timing; subsequent annotation quality as estimated by the latent-truth model; task type; cohort and entry date; item response patterns over time.
**Target:** Measured downstream annotation reliability on the task type the applicant was screened for.
**Evaluation metric:** Predictive validity of each screening signal against downstream quality, reported per signal so that credentials which predict nothing can be identified and dropped. For item compromise, detection of a difficulty shift or response-time collapse against a synthetic leak injected into a live pool, which is the only honest way to measure a detector for a rare adversarial event.
**Scope:** The fairness dimension is not optional here. A screening pipeline filtering on credential proxies rather than demonstrated ability excludes competent people without conventional backgrounds, and this population is precisely who the work could serve well — so any signal that predicts poorly should be removed on both accuracy and equity grounds, and the analysis should check for disparate impact explicitly. Adaptive item selection from a large rotating pool is standard practice in professional testing and requires an item bank the vendor must build. 2 ML engineers plus an assessment psychometrician, 5 months.
**Data availability:** Applicant and screening records are complete. The join to downstream quality requires the latent-truth model to exist first, which makes this the second project rather than the first.

---

## 4. Batch Quality Change Attribution
#change-point-detection #gradient-boosting #hypothesis-testing #confidence-intervals #k-means-clustering #causal-inference #evaluation-metrics

**Problem statement:** Quality degradation is discovered when a customer complains with six examples, and the delivery manager works backwards by hand through a pipeline that records guideline revisions, contributor cohorts, review coverage and item difficulty separately and joins none of them.

**ML task:** Change point detection on batch-level quality series with attribution to concurrent pipeline changes
**Input data:** Per-batch consensus rates, review pass rates, time-per-task distributions and dispute rates; contributor composition and tenure mix over time; guideline version changes with timestamps; review sampling rate; item source and difficulty distribution from the customer's sampling; customer-flagged examples.
**Target:** A detected shift in batch quality, with an attributed cause among the concurrent changes.
**Evaluation metric:** Detection lead time against the date the customer eventually complained — the operational benchmark that matters. Attribution accuracy validated against delivery manager post-mortems on historical escalations, which exist as written records and form a natural evaluation set nobody has assembled.
**Scope:** Attribution is confounded by design: changes co-occur, cohorts onboard when volume rises, review coverage drops when deadlines compress. Honest attribution means reporting candidate causes with evidence rather than a single answer, and the delivery manager remains the decision maker. The monitoring layer itself requires no learning and delivers most of the value — the absence of continuous batch quality tracking is a product gap rather than a technical one. 2 ML engineers, 4 months.
**Data availability:** All inputs exist in the pipeline and live in separate systems. Historical escalations with their eventual diagnoses are recorded in customer communications and project retrospectives and are the best available labels.
