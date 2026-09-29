# Machine Learning Opportunities — Field Service Software

**Industry:** [[field-service-software|Field Service Software]]
**Derived from:** [[problems/field-service-software/high-impact|High Impact]], [[problems/field-service-software/low-impact-1|Low Impact 1]], [[problems/field-service-software/low-impact-2|Low Impact 2]], [[problems/field-service-software/worker-life-1|Worker Life 1]], [[problems/field-service-software/worker-life-2|Worker Life 2]]

---

## 1. Diagnosis Prediction from Customer Symptom Description
#bert #transformers #word-embeddings #gradient-boosting #feature-engineering #cross-validation #evaluation-metrics #tacit-knowledge-ml #revenue-impact

**Problem statement:** Dispatch decisions — which technician, what parts, how long — are made from a two-sentence customer description. Good dispatchers infer the likely fault from that description plus the address history and cannot explain how. Getting it wrong produces a return visit, and first-time fix rate is the number that determines whether a service business is profitable.

**ML task:** Multiclass classification over failure categories from short free text plus structured context, with calibrated probabilities rather than a single prediction
**Input data:** Customer symptom text as captured by the call taker; equipment make, model, age and install date; the address's prior service history; season and outdoor temperature; property type; trade; and the technician's eventual diagnosis notes plus parts consumed as the outcome.
**Target:** The failure category actually found, derived from technician notes and parts used. Return visit within a defined window as a secondary label for whether the dispatch was adequate.
**Evaluation metric:** Top-3 accuracy matters more than top-1, because the operational use is deciding what to put on the truck rather than announcing a diagnosis. Calibration is essential — a confidently wrong prediction that sends a technician without the right part is worse than an honest spread. Report the downstream metric too: modelled effect on first-time fix rate.
**Scope:** Extracting a clean diagnosis label from free-text technician notes of highly variable quality is the largest single task and should be treated as its own extraction project before any prediction is attempted. Parts consumed is a useful but incomplete proxy that misses diagnostic-only visits. 3 ML engineers plus a trade expert per vertical, 6-8 months for the first trade, much faster thereafter.
**Data availability:** Very strong on volume — millions of visits across brands and trades. Weak on label quality; notes are written in a truck under time pressure and a large share say nothing useful. Symptom text is often paraphrased by the call taker rather than captured verbatim, which loses signal.

---

## 2. Technician–Job Capability Matching
#gradient-boosting #k-nearest-neighbors #feature-engineering #evaluation-metrics #confidence-intervals #cross-validation #tacit-knowledge-ml

**Problem statement:** Matching the right technician to a job is the second half of the dispatch decision and rests on knowledge of who is genuinely good at what — by equipment brand, by failure class, by property type. It exists only in the dispatcher's head, and the platform's own outcome history could measure it.

**ML task:** Outcome prediction conditional on assignment — estimating completion time, first-time-fix probability and callback risk for a given technician, job type and equipment combination
**Input data:** Historical assignments with technician identity, equipment make and model, predicted and actual failure category, job duration, parts used, return visit occurrence, customer satisfaction where captured, and technician certifications and tenure.
**Target:** Job outcome — resolved on first visit, duration, and whether a return was required.
**Evaluation metric:** Predictive accuracy on held-out assignments, and separately a counterfactual estimate of first-time fix improvement under model-suggested versus actual assignments. The counterfactual is the number that matters and requires care, since assignments were never random.
**Scope:** The ethical and practical constraint dominates the design. Capability must be represented as demonstrated outcomes on specific equipment and failure classes, never as a global ranking of people, both because it is more accurate and because a workforce will reject the latter. Small per-technician sample sizes require hierarchical pooling with honest uncertainty. 2-3 ML engineers, 5-6 months, with explicit involvement from operations leadership on how the output is surfaced.
**Data availability:** Present in every platform and never analysed. Selection bias is severe — good technicians get the hard jobs, so raw outcome comparisons are misleading and the analysis needs to condition on job difficulty properly.

---

## 3. Empirical Price Book Construction and Price Sensitivity
#gradient-boosting #linear-regression #logistic-regression #descriptive-statistics #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Flat-rate price books are licensed as national artefacts and customised by hand over weeks, then left to drift. Every input that should set a price — actual labour time, actual material cost, local wage rates, and customer willingness to pay — varies locally and is observable in the platform's own data across thousands of contractors.

**ML task:** Two linked models — a regression on realised task duration by market, equipment and conditions, and a classification of quote acceptance as a function of price, task, market and ticket size
**Input data:** Completed jobs with task codes, realised labour time, parts and material cost from invoices, technician, market, equipment make and age; quoted prices with accept or decline outcomes; local wage indices; supply house pricing; contractor and market attributes.
**Target:** Realised duration and material cost per task per market; and the probability a quote at a given price is accepted.
**Evaluation metric:** For duration, quantile accuracy rather than mean, since pricing should reflect the distribution and not the average. For acceptance, calibration across the price range is the whole point — the model must be trustworthy at prices outside the observed range only with explicit extrapolation warnings.
**Scope:** The acceptance model is the genuinely novel piece and rests on decline data, which most platforms capture inconsistently because a declined quote is often just abandoned rather than recorded. Fixing that capture is a prerequisite and is a product change, not a modelling one. Endogeneity is real — prices were not set randomly — and the honest approach is to exploit natural variation across contractors in similar markets. 2 ML engineers plus a pricing analyst, 5 months.
**Data availability:** Job costing data is strong. Decline data is the weak link and the reason nobody has measured price sensitivity in this industry despite it being the most valuable question in it.

---

## 4. Equipment Data Plate Reading and Model-Level Enrichment
#cnns #object-detection #semantic-segmentation #transfer-learning #feature-engineering #evaluation-metrics #large-language-models

**Problem statement:** Equipment records are the foundation for diagnosis, parts and warranty and are unpopulated on a large fraction of assets, because capturing them means typing a seventeen-character model number off a faded plate in a dark mechanical room for no immediate benefit to the technician.

**ML task:** Text detection and recognition on manufacturer data plates under adverse conditions, followed by structured parsing of make, model, serial and manufacture date using brand-specific formats
**Input data:** Technician photographs of data plates across brands, eras and conditions; confirmed equipment records where a technician did type the values, as labels; published manufacturer serial and model format specifications; the vendor's cross-contractor service history keyed by model.
**Target:** Correctly parsed make, model, serial and manufacture date, with a confidence per field.
**Evaluation metric:** Exact-match accuracy per field, with model number weighted most heavily since a single wrong character orders the wrong part. Precision must dominate recall — an unread field prompts a retake, a misread field causes a failed job. Report accuracy stratified by plate condition, because average accuracy hides the cases that matter.
**Scope:** Generic OCR performs adequately on clean plates and fails on exactly the degraded ones where the value is. Brand-specific layout priors and format validation against known model syntaxes recover most of that gap and are more valuable than a larger general model. Guided capture in the app — framing, glare warnings, retake prompts — is worth more than several points of model accuracy. 2 ML engineers, 4 months.
**Data availability:** Photograph volume is large and unlabelled; labels come from records where the technician typed the values, which biases toward legible plates. Deliberate collection of hard cases is necessary and cheap to organise through the technician app.
