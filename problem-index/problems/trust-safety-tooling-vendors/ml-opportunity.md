# Machine Learning Opportunities — Trust & Safety Tooling Vendors

**Industry:** [[trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Derived from:** [[problems/trust-safety-tooling-vendors/high-impact|High Impact]], [[problems/trust-safety-tooling-vendors/low-impact-1|Low Impact 1]], [[problems/trust-safety-tooling-vendors/low-impact-2|Low Impact 2]], [[problems/trust-safety-tooling-vendors/worker-life-1|Worker Life 1]], [[problems/trust-safety-tooling-vendors/worker-life-2|Worker Life 2]]

---

## 1. A Shared Per-Segment Benchmark
#evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #bert #transformers #transfer-learning #compliance

**Problem statement:** Every vendor reports accuracy on its own undisclosed test set, so buyers compare self-administered exams — and the failures that produce most documented moderation harm, in lower-resource languages and specific communities, are invisible inside an aggregate figure.

**ML task:** Construct a held-out evaluation service where vendors submit models rather than receiving data, and publish per-segment performance against panel-adjudicated ground truth
**Input data:** Content spanning languages, dialects, communities, modalities and harm categories in documented proportions; labels from expert panels rather than single annotators, with inter-annotator agreement recorded; submitted models run against held-out content.
**Target:** Per-segment precision and recall against the panel distribution, with the agreement ceiling reported.
**Evaluation metric:** Everything reported per language, per dialect, per content type and per category with confidence intervals, never aggregated — because the aggregate is the mechanism by which the consequential failures stay invisible. Ground truth must be a distribution of expert judgement rather than a single label, with inter-annotator agreement published as the ceiling, since a benchmark asserting one right answer on genuinely contested content measures conformity rather than accuracy and would encode one set of judgements as truth.
**Scope:** The evaluation-service structure resolves the real obstacle, which is that a harmful content benchmark contains harmful content and cannot be freely distributed — models come to the data, not the reverse. The remaining obstacles are commercial and coordinative: no vendor gains from a comparison that might rank them lower. Regulatory reporting regimes now require platforms to publish accuracy statistics, which makes a regulator or standards body the natural convenor. 3 ML engineers plus policy and legal capacity, 12-18 months.
**Data availability:** Must be constructed deliberately, with all the handling controls that implies. This is the field's defining gap and it is a coordination problem wearing a technical one's clothes.

---

## 2. Cost-Derived Operating Points and Policy-to-Configuration Mapping
#bayesian-inference #confidence-intervals #probability-distributions #evaluation-metrics #gradient-boosting #bert #large-language-models #compliance

**Problem statement:** A threshold determines the balance between missing harmful content and removing legitimate speech, those costs are not commensurable and differ by category and platform, and the threshold is set by trial until the review queue is manageable.

**ML task:** Derive per-category operating points from stated relative costs under a review capacity constraint, and map a customer's written policy to the classifier configuration meant to implement it
**Input data:** Per-category score distributions and precision-recall behaviour; the customer's stated relative costs of misses and false positives per category, even as an ordering; review capacity; the customer's policy document; historical configuration and its outcomes; appeal and reversal data.
**Target:** An operating point per category that maximises harm reduction subject to capacity, and a configuration traceable to specific policy provisions.
**Evaluation metric:** The honest framing is maximising harm reduction subject to available review capacity, which produces a markedly different configuration from tuning each category until the queue looks manageable — and the comparison between the two should be reported, because it shows a customer what their current staffing-driven configuration is costing. Routing by distance from the threshold rather than by binary comparison puts human attention where the classifier is least certain, which is where the errors are; measure the error rate by confidence band to demonstrate it.
**Scope:** The exercise of stating relative costs is valuable independently of the model, because it surfaces decisions the organisation has been making implicitly. Policy-to-configuration mapping makes the translation explicit, versioned and reviewable, where it currently lives in a solutions engineer's interpretation. 2 ML engineers plus a policy specialist, 6-9 months.
**Data availability:** Score distributions are the vendor's; policy and cost judgements come from the customer and mostly do not exist in stated form.

---

## 3. Description-Based Detection and Novelty Clustering
#large-language-models #transfer-learning #contrastive-learning #dbscan #change-point-detection #bert #confidence-intervals #evaluation-metrics

**Problem statement:** New abuse patterns, coordinated campaigns and emergent terminology appear faster than labelled data can be produced, and the weeks a supervised pipeline needs are exactly when a new harm does its damage.

**ML task:** Build usable detectors from a written description of a newly-observed harm, and surface clustered content that fits no existing category so patterns are visible before anyone has named them
**Input data:** Policy-team descriptions of observed harms; a small number of confirmed examples; the platform's content stream; embedding space coverage of existing categories; account coordination and propagation signals; historical emergent harms with the lag before detection.
**Target:** Detection of the described harm, and identification of coherent clusters outside the existing taxonomy.
**Evaluation metric:** Detectors built from descriptions must be evaluated before deployment with particular care, because a fluent model will classify confidently against a description in ways that surprise its author — measure false positive rate on adjacent legitimate content specifically, not on a random sample. For novelty, the measure is time from a harm first appearing to a policy person seeing a coherent cluster of it, against the historical lag. Coordination signals should be evaluated separately, since they detect campaigns regardless of content and are therefore resistant to the terminology evasion that defeats content models.
**Scope:** Few-shot performance from descriptions is the capability that recently changed and is unevenly exploited; it compresses response time from weeks to hours, which is the single most consequential improvement available here. Per-customer light adaptation on the platform's own examples is the difference between a generic classifier and a usable one and should be routine rather than a professional services engagement. 3 ML engineers, 9-12 months.
**Data availability:** Content streams sit with customers; emergent harm descriptions come from policy teams and are not currently captured in a form a model can consume.

---

## 4. Active Learning and Annotation Exposure Reduction
#transformers #cnns #large-language-models #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #worker-facing

**Problem statement:** Every harm classifier rests on labelled examples produced by people who see a deliberately concentrated density of the worst material, in a workforce even less visible than the moderators downstream.

**ML task:** Select the examples that most improve the model so far fewer need human labelling, pre-label so annotators confirm rather than label from scratch, and model cumulative per-annotator exposure with the category concentration accounted for
**Input data:** Unlabelled content pools; current model uncertainty and decision boundaries; annotator labels with disagreement recorded; per-annotator exposure history by category; guideline versions; agreement rates.
**Target:** Model performance per labelled item, and the volume of human exposure required to reach a given performance level.
**Evaluation metric:** Performance per labelled example against random sampling is the headline — active learning's direct benefit here is measured in human exposure avoided, which should be the reported outcome rather than an efficiency figure. For pre-labelling, measure correction rate and ensure it does not induce automation bias, where annotators accept a model's label without examining the item, which would degrade the training data in a way that compounds.
**Scope:** Recording disagreement rather than forcing consensus produces better models — a label distribution supports a calibrated classifier where a forced single label supports an overconfident one — and simultaneously removes the pressure on annotators to apply guidelines literally. Documenting who labelled a model's training data, under what guidelines and with what agreement rates, published alongside the model, is basic transparency that also makes the resulting biases traceable. 2 ML engineers plus occupational health input, 6-9 months.
**Data availability:** Complete within any annotation operation, and exposure records are generally not treated as health data.
