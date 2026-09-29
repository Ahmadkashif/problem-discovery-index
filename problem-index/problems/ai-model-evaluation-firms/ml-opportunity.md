# Machine Learning Opportunities — AI Model Evaluation Firms

**Industry:** [[ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Derived from:** [[problems/ai-model-evaluation-firms/high-impact|High Impact]], [[problems/ai-model-evaluation-firms/low-impact-1|Low Impact 1]], [[problems/ai-model-evaluation-firms/low-impact-2|Low Impact 2]], [[problems/ai-model-evaluation-firms/worker-life-1|Worker Life 1]], [[problems/ai-model-evaluation-firms/worker-life-2|Worker Life 2]]

---

## 1. Behavioural Contamination Estimation
#hypothesis-testing #confidence-intervals #evaluation-metrics #entropy-cross-entropy-kl-divergence #large-language-models #transformers #bayesian-inference

**Problem statement:** Public benchmarks are plausibly inside the training corpora of the models they measure, the extent is unknowable because training data is undisclosed, and every published score is therefore an upper bound of unknown looseness. The field's own literature documents this clearly while commercial practice reports scores as though it were settled.

**ML task:** Inference of benchmark exposure from model behaviour — matched-difficulty performance comparison, exact-format reproduction testing, perplexity asymmetry analysis, and canary completion
**Input data:** Canonical benchmark items and freshly authored items matched on difficulty and format; model responses and token-level probabilities where available; benchmark publication dates against model training cutoffs; response formatting fidelity to the original item; embedded canary strings.
**Target:** A contamination estimate per benchmark per model, expressed as a bound with stated assumptions.
**Evaluation metric:** Validation against known-contaminated cases — deliberately fine-tuning a model on a held-out benchmark and measuring whether the estimator detects it, at what exposure level. This is the only rigorous validation available, since real contamination is unobservable by construction. Report the estimator's detection floor honestly: below some exposure level it cannot distinguish contamination from capability.
**Scope:** This produces a bound rather than a verdict, and framing it otherwise would be dishonest. Matched-difficulty freshly-authored items are the strongest single method and are expensive, since authoring them requires the same expertise as authoring the benchmark. Time-gated evaluation built from post-cutoff material is structurally sound and expires with each model generation, which makes it a rolling operational cost rather than a project. 3 ML engineers plus benchmark designers, 6-9 months, ongoing.
**Data availability:** Model responses are obtainable. Token probabilities are increasingly unavailable through commercial APIs, which removes perplexity-based methods for exactly the frontier models that matter most.

---

## 2. Judge Reliability Characterisation and Bias Correction
#hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #bayesian-inference #large-language-models #descriptive-statistics

**Problem statement:** LLM-as-judge is the dominant automated grading method and is deployed against a rubric with, at best, a small agreement check against human grades. Its consistency per criterion, its position and length and self-preference biases on that specific rubric, and where its errors concentrate are all measurable and rarely measured.

**ML task:** Estimation of judge reliability and systematic bias per rubric criterion, with correction applied to reported scores
**Input data:** Judge verdicts with repeated grading of identical items; human expert grades on a calibration subset; response length, formatting and position; the judge model's identity and version; per-criterion verdicts rather than aggregate scores; the responding model's identity, for self-preference testing.
**Target:** Judge agreement with expert consensus per criterion, and coefficients on the confounding factors.
**Evaluation metric:** Per-criterion agreement with expert consensus, reported separately rather than aggregated, since a judge can be reliable on factual criteria and unreliable on judgement-based ones and the average hides both. Bias magnitudes should be reported in units of the score itself — how many points of the reported result are attributable to length — which is what makes the finding actionable.
**Scope:** Judge drift is a live operational hazard, since commercial judge models are updated without notice; periodic re-grading of a fixed item set detects it and should run continuously. Self-preference — a judge favouring outputs from its own model family — is measurable directly and is the bias with the sharpest commercial implications. 2 ML engineers plus a measurement statistician, 4-5 months.
**Data availability:** Firms hold millions of graded items with judge, rubric, model and response attached, which is exactly the corpus needed. Repeated grading of identical items is cheap and is not routinely done.

---

## 3. Preference Data Debiasing and Adaptive Pair Selection
#logistic-regression #bayesian-inference #expectation-maximization #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics

**Problem statement:** Human preference anchors the field's most consequential measurements and the tuning of the models themselves. It is contaminated by length, formatting, confidence and position effects that are documented in the literature and uncorrected in commercial practice, and rater expertise is verified against style agreement rather than against error-detection ability.

**ML task:** Bradley-Terry style aggregation with explicit confound terms, joint with rater reliability estimation, plus adaptive selection of informative comparison pairs
**Input data:** Pairwise preference judgements with rater identity, response length, formatting features, presentation position and time spent; seeded items containing known factual errors as a rater capability probe; rater history; model identities.
**Target:** Model quality parameters adjusted for confounds, and per-rater error-detection ability.
**Evaluation metric:** Whether debiased rankings predict performance on independent objective measures better than raw preference does — the honest test, since the confound-corrected ranking should agree more closely with capability measured another way. For adaptive selection, ranking precision achieved per comparison collected against random pairing, which is where the cost saving is.
**Scope:** Length control is published and easy; formatting, confidence and position corrections are less studied and are the contribution. Seeded error items measure the capability that actually matters and are cheap to construct. Adaptive pair selection near the decision boundary is standard psychometrics, cuts collection cost substantially, and introduces a subtle bias of its own that must be modelled rather than ignored. Collecting multidimensional rather than scalar preference changes what can be corrected and is a data collection decision, not a modelling one. 2 ML engineers plus a psychometrician, 5 months.
**Data availability:** Preference datasets are large and generally lack the confound covariates — position, timing, formatting features — because they were not recorded. Instrumenting collection is the prerequisite.

---

## 4. Evaluation Variance Decomposition and Change Attribution
#hypothesis-testing #confidence-intervals #descriptive-statistics #change-point-detection #evaluation-metrics #large-language-models #workflow-orchestration

**Problem statement:** A score moves three points and an evaluation engineer spends hours establishing whether the model changed or the judge sampled differently, the parser broke on a formatting variation, items errored and were dropped, or a prompt template was edited. Every reported movement demands an explanation and most explanations are artefacts.

**ML task:** Decomposition of observed score variance into model sampling, judge sampling, parse failure, item coverage and configuration change components, with automatic attribution of run-to-run differences
**Input data:** Repeated evaluation runs with fixed and varied seeds; judge verdicts on repeated items; parse success and failure per item; item error and timeout logs; model, judge, harness and prompt template versions; item set composition per run.
**Target:** The variance attributable to each component, and for a given run-to-run difference, the changes that co-occurred.
**Evaluation metric:** Whether reported confidence intervals actually cover — running the same evaluation repeatedly with no changes should produce movements inside the stated interval at the stated rate, which is directly checkable and almost never checked. Attribution accuracy against engineer post-mortems on historical investigations.
**Scope:** Most of this requires no learning and its absence is a product gap: parse failures should be a reported category rather than silently scored incorrect, and a rising parse failure rate should alert on its own. Judge stability monitoring through periodic re-grading of a fixed set catches silent provider updates, which is a live and largely unmanaged hazard. 2 ML engineers, 3-4 months.
**Data availability:** Complete within any evaluation platform. Repeated-run data with controlled variation must be generated deliberately and is inexpensive.
