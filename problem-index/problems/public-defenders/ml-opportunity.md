# ML Opportunities — Public Defenders

**Industry:** [[public-defenders|Public Defenders]]
**Tags:** #bert #gradient-boosting #llm #lstm #multiclass-classification #binary-classification #regression #text-classification #time-series-forecasting #nlp #tabular-ml #tacit-knowledge-ml #compliance #worker-facing

---

## 1. Case Outcome Prediction from Case File Analysis (Primary Opportunity — Tacit Knowledge ML)

#bert #gradient-boosting #multiclass-classification #nlp #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced public defenders read a case file — police report, charges, criminal history, judge assignment, prosecutor assignment — and within minutes can predict the realistic outcome range (dismissal, reduced charge plea, full-charge plea, trial conviction, trial acquittal) with accuracy that takes 5-10 years of local practice to develop. This tacit knowledge — knowing that this combination of facts, this judge, and this prosecutor will likely produce outcome X — is the foundation of effective plea negotiation and case strategy, but it resides exclusively in the heads of senior defenders and is never systematically captured.

**ML task:** Multi-class classification — predict case disposition category (dismissed, diverted, reduced-charge plea, full-charge plea, trial acquittal, trial conviction) and estimated sentence range for plea/conviction outcomes.

**Input data:** Structured case data (charge codes, charge level, criminal history score, judge ID, prosecutor ID, custody status, co-defendants), extracted features from discovery text (police report narrative, evidence inventory, witness count and type, Miranda compliance indicators, search/seizure circumstances), and contextual features (court location, time-to-disposition benchmarks, current docket congestion).

**Target:** Multi-class disposition prediction with probability distribution across outcomes. Secondary target: sentence range prediction (minimum/maximum months) conditional on each disposition type.

**Model:** BERT encoder processes police report narratives and discovery text to extract legal issue signals (suppression indicators, witness reliability flags, evidence strength cues). These embeddings combine with structured features (judge ID encoded as learned embedding, prosecutor ID, charge severity, criminal history) in a gradient-boosted multi-class classifier.

**Evaluation:** Multi-class log loss as primary metric. Per-class F1, with emphasis on correctly identifying dismissal-likely cases (highest strategic value) and trial-winnable cases. Calibration quality critical — probability estimates must be trustworthy enough to inform client advice. Target: top-2 accuracy (correct disposition in top 2 predicted) of 75%+.

**Scope:** High difficulty. 12-18 months to production. Requires access to closed case records with full discovery, disposition, and sentencing data from a single large PD office. Data sensitivity is extreme — all training data involves attorney-client privileged information requiring ethics board review and robust anonymization. Team: 2 ML engineers, 1 NLP specialist, 1 senior public defender, 1 legal ethics consultant.

**Data availability:** Case dispositions and sentences are public court records. The challenge is linking these to the case file content (police reports, discovery) which is not public. A PD office partnership provides access to their closed files, but ethical constraints require that the model never be used in a way that could prejudice a current client. Data from 5-10 years of closed cases in a large urban office (50,000-100,000 cases) provides sufficient training volume.

---

## 2. Bail and Pretrial Release Outcome Prediction

#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** At arraignment, defenders argue for release conditions (ROR, supervised release, bail amount) with limited information about how the judge will decide. Better prediction of likely bail outcomes would enable defenders to prepare more targeted arguments and identify cases where judicial decisions are statistically anomalous.

**ML task:** Multi-output prediction — predict bail decision (released/detained) and bail amount for each case at arraignment.

**Input data:** Charge type and severity, criminal history, failure-to-appear history, community ties (employment, housing, family), judge ID, jurisdiction, current jail population (capacity pressure affects decisions), and day of week/time of day (judicial fatigue effects are documented).

**Target:** Binary release/detain prediction plus bail amount regression. Secondary: predicted conditions of release (GPS monitoring, drug testing, curfew).

**Model:** Gradient-boosted classifier for release/detain, gradient-boosted regressor for bail amount. Judge ID as a critical feature — individual judicial variation explains 30-50% of outcome variance, more than case characteristics.

**Evaluation:** AUC-ROC for release/detain classification. MAE for bail amount (within $500 for misdemeanors, $5,000 for felonies). Equity analysis: model must be audited for racial and socioeconomic bias in predictions.

**Scope:** Moderate. 4-6 months to MVP. Arraignment outcomes are public court records in most jurisdictions. Requires linking to defendant-level structured data. Team: 1 ML engineer, 1 data engineer, 1 legal domain expert. Equity audit adds 2-3 months.

**Data availability:** Strong. Bail decisions are public record. NYC's open data portal alone provides millions of arraignment records with outcomes. Challenge is linking to detailed defendant characteristics (community ties) which are typically only in defense files.

---

## 3. Sentence Range Estimation by Judge and Charge

#gradient-boosting #regression #tabular-ml

**Problem statement:** Defenders advise clients on whether to accept plea offers by comparing the offer to the likely trial outcome. This comparison requires accurate knowledge of how the specific assigned judge sentences specific charge types — knowledge that takes years to develop and varies enormously between judges.

**ML task:** Regression — predict sentence (in months) for a given judge, charge, criminal history, and case characteristics.

**Input data:** Judge ID, charge codes, criminal history score, plea vs. trial conviction, mitigating factors (employment, family, mental health treatment, veteran status), aggravating factors (victim injury, weapon use, prior violent offense), and jurisdiction-specific sentencing guidelines data.

**Target:** Predicted sentence in months with confidence interval. Secondary: predicted sentence components (incarceration, probation, fine, community service).

**Model:** Gradient-boosted regression with judge embeddings. Separate models for plea and trial outcomes, as the sentencing calculus differs. Quantile regression for confidence intervals rather than point estimates.

**Evaluation:** MAE in months. Target: within 3 months for felonies, within 1 month for misdemeanors. Confidence interval calibration: 80% of actual sentences should fall within the predicted 80% CI.

**Scope:** Moderate. 3-5 months to MVP. Sentencing data is public in most jurisdictions. Team: 1 ML engineer, 1 legal data specialist.

**Data availability:** Strong. Sentencing records are public court data. State sentencing commissions (US Sentencing Commission for federal, state equivalents) publish detailed sentencing data. The gap is linking to case-specific mitigating/aggravating factors, which requires parsing judicial orders or defense files.

---

## 4. Case Timeline and Hearing Prediction

#lstm #time-series-forecasting #tabular-ml

**Problem statement:** Defenders cannot predict when their cases will reach critical milestones (trial date, plea hearing, motion hearing), making workload planning impossible and forcing reactive rather than strategic case management.

**ML task:** Time-series forecasting — predict the date of next hearing and overall time-to-disposition for each open case.

**Input data:** Case filing date, charge type, court division, judge assignment, attorney assignment (PD vs. assigned counsel vs. private), number of co-defendants, complexity indicators (number of charges, discovery volume, expert witness needs), historical hearing schedule patterns for the assigned courtroom.

**Target:** Predicted next hearing date, predicted disposition date, and predicted number of remaining hearings.

**Model:** LSTM or gradient-boosted regression on temporal case features. Court-specific models account for local scheduling patterns, judicial calendaring preferences, and systemic delays (lab backlogs, interpreter availability, jail transport schedules).

**Evaluation:** MAE in days for next hearing (target: within 7 days). MAE in weeks for disposition date (target: within 4 weeks for misdemeanors, within 8 weeks for felonies).

**Scope:** Low-moderate. 3-4 months to MVP. Court scheduling data is publicly available in electronic filing systems. Team: 1 ML engineer.

**Data availability:** Strong. Court docket data is public and increasingly available through electronic court systems (Odyssey, eCourt). Historical hearing patterns for millions of cases are available in large jurisdictions.

---

## 5. Investigator Resource Allocation Optimization

#gradient-boosting #binary-classification #tabular-ml #regression

**Problem statement:** PD offices have 1 investigator for every 10-20 attorneys, meaning fewer than 5% of cases receive investigation. Determining which cases would most benefit from investigation is a critical resource allocation decision currently made on attorney request (squeaky wheel) rather than evidence-based triage.

**ML task:** Binary classification (would investigation change the outcome?) plus regression (expected outcome improvement from investigation).

**Input data:** Case characteristics (charge, evidence type, witness count, suppression potential), historical investigation outcomes (what happened when similar cases were investigated vs. not), attorney experience level (less experienced attorneys may miss investigation-worthy issues), and case complexity indicators.

**Target:** Binary: investigation-recommended (1) or standard-process (0). Regression: predicted disposition improvement (in reduced charge level or sentence months) if investigation is conducted.

**Model:** Gradient-boosted classifier trained on historical cases where investigation was and wasn't conducted, controlling for selection bias (cases selected for investigation are not random — they're pre-selected by attorney judgment, which must be modeled and adjusted for).

**Evaluation:** Precision@K where K = the office's monthly investigation capacity. The model must identify the K cases per month that would benefit most, measured by actual outcome improvement. Target: model-selected cases achieve 20%+ better outcomes than attorney-selected cases.

**Scope:** High difficulty due to causal inference challenge — the counterfactual (what would have happened without investigation?) is unobservable. Requires instrumental variable or propensity score approaches to estimate treatment effects. 6-9 months. Team: 1 ML engineer with causal inference experience, 1 PD domain expert.

**Data availability:** Moderate. Investigation records are internal PD data. Outcome data is public. The challenge is constructing valid comparison groups — cases that were similar but received different investigation treatment due to capacity constraints rather than case merit.
