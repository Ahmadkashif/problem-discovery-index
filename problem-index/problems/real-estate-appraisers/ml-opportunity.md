# Machine Learning Opportunities — Real Estate Appraisers

**Industry:** [[real-estate-appraisers|Real Estate Appraisers]]
**Derived from:** [[problems/real-estate-appraisers/high-impact|High Impact]], [[problems/real-estate-appraisers/low-impact-1|Low Impact 1]], [[problems/real-estate-appraisers/low-impact-2|Low Impact 2]], [[problems/real-estate-appraisers/worker-life-1|Worker Life 1]], [[problems/real-estate-appraisers/worker-life-2|Worker Life 2]]

---

## 1. Market-Calibrated Adjustment Development via Hedonic Regression
#gradient-boosting #regression #causal-inference #tabular-ml #revenue-impact

**Problem statement:** Derive market-supported dollar adjustments for standard property attributes (GLA, bedroom/bath, garage, condition, age) from local MLS sales data, replacing rule-of-thumb adjustment tables with statistically-calibrated market values.

**ML task:** Hedonic regression — attribute-level implicit price estimation from comparable sales; causal inference techniques to isolate individual attribute values from confounded sales data
**Input data:** MLS sold data for the submarket: sale price, GLA, bedroom count, bathroom count, garage type, lot size, age, condition code, location within submarket. Rolling 24-month window updated monthly.
**Target:** Adjustment rate per attribute with confidence interval; matched-pair evidence for the top-5 most-used adjustments; comparison to FNMA CU market adjustment norms for the submarket
**Evaluation metric:** Agreement rate between model adjustments and FNMA CU adjustment norms on held-out appraisals; CU flag rate for appraisals using model-derived adjustments vs. rule-of-thumb; revision request rate for market-calibrated vs. manual adjustments
**Scope:** Hedonic regression on MLS data is well-established econometric methodology. MLS data access is the primary requirement (each market requires separate MLS API or data agreement). CoreLogic or Black Knight national MLS data aggregation provides the scale path. 4-6 month development for a market-calibrated adjustment tool integrated with TOTAL. The causal inference component (isolating attribute values from correlated property features) is the methodological differentiator vs. naive regression.
**Data availability:** MLS data is the training input — available through RETS/RESO API agreements in each market. CoreLogic and Black Knight have national aggregated MLS data under data licensing agreements. The hedonic model is retrained monthly as new sales occur.

---

## 2. Comparable Sale Ranking by Multi-Attribute Similarity
#gradient-boosting #ranking #tabular-ml #quick-win

**Problem statement:** Rank candidate comparable sales by their overall similarity to the subject property, weighted by local market adjustment rates, to guide comp selection.

**ML task:** Learning-to-rank — candidate comp ordering by overall similarity score incorporating adjustment magnitude estimates per attribute difference
**Input data:** Appraisal datasets with comp selections and appraiser-assigned quality rankings. Features: per-attribute difference between subject and each candidate comp, estimated adjustment magnitude per difference (from market calibration model), distance, time since sale.
**Target:** Ranked candidate comp list with similarity score and estimated total adjustment magnitude per candidate; top-3 recommendation with rationale
**Evaluation metric:** Agreement rate between top-ranked candidates and appraiser's final selected comps; reduction in total gross adjustments for appraisals using ranked vs. unranked comp selection; CU flag rate for appraisals using ranked comp selection
**Scope:** Quick win — the ranking model is straightforward once adjustment magnitudes are available from the hedonic regression (opportunity #1 above). Appraisal datasets with comp selections provide training labels. Gradient boosting ranker on attribute difference features: 3-4 week project.
**Data availability:** UCDP submission data contains comp selections for every FNMA-submitted appraisal. A Fannie Mae or CoreLogic data partnership provides the training labels. MLS data provides the candidate pool.

---

## 3. CU Risk Scoring Before Submission
#gradient-boosting #binary-classification #tabular-ml #compliance #quick-win

**Problem statement:** Predict which appraisal reports will receive high CU risk scores (≥ 2.5) before they are submitted, enabling the appraiser to address flagged issues proactively.

**ML task:** Binary classification (CU flag: yes/no) and regression (estimated CU score) from appraisal report features
**Input data:** Historical UCDP submissions with CU scores. Features: net/gross adjustment percentages, adjustment outlier flags vs. market norms, market commentary consistency score, comp recency and proximity, subject property characteristics.
**Target:** Predicted CU risk score and specific flag predictions per appraisal before submission; recommended remediation for each predicted flag
**Evaluation metric:** AUC on CU flag prediction; revision request reduction for appraisals flagged and corrected pre-submission vs. control; time saved by avoiding post-submission revisions
**Scope:** Quick win — Fannie Mae publishes some CU scoring criteria. Historical UCDP submission data with CU outcomes provides training labels. Gradient boosting on report features: 3-4 week project with sufficient labeled submissions. A CoreLogic or a la mode data partnership provides the scale.
**Data availability:** UCDP submission data with CU scores exists at CoreLogic and similar data aggregators. Individual appraisers have their own submission history. The feature set comes from the appraisal report fields — all structured data in TOTAL.

---

## 4. Automated Market Conditions Commentary Generation
#llm #text-generation #tabular-ml #quick-win

**Problem statement:** Generate FNMA-compliant market conditions commentary from current MLS statistics for the subject's submarket — eliminating the manual data gathering and writing task for the required market conditions section.

**ML task:** Conditional text generation — market conditions narrative from structured MLS statistics inputs (median price, DOM, list-to-sale ratio, inventory, month-over-month trends)
**Input data:** High-quality market conditions commentary sections from accepted appraisal reports, paired with the MLS statistics that supported them. Fine-tuning corpus: 2,000-5,000 paired statistics-commentary sets.
**Target:** FNMA-format market conditions commentary reflecting current MLS statistics; directionally consistent with the comparable sales price trend in the report
**Evaluation metric:** Internal consistency between generated commentary and comp sale price trend; reviewer acceptance rate (is the generated commentary used without significant revision?); time saved per report vs. manual writing
**Scope:** Quick win — LLM fine-tuning on appraisal market commentary is a bounded NLP task with clear input-output structure. a la mode's TOTAL has the report library for training data. 4-6 week project with fine-tuned LLM integration.
**Data availability:** a la mode (TOTAL) has market commentary sections from millions of appraisal reports. A data partnership with a la mode provides both training corpus and distribution channel.

---

## 5. Property Condition and Quality Classification from Inspection Photos
#cnn #multiclass-classification #computer-vision

**Problem statement:** Classify property condition and quality rating (FNMA C1-C6 condition scale, Q1-Q6 quality scale) from inspection photos to provide an objective starting point for the appraiser's condition/quality assessment.

**ML task:** Multiclass classification — condition tier (C1-C6) and quality tier (Q1-Q6) from property inspection photos
**Input data:** Appraisal inspection photos with FNMA condition and quality ratings assigned by the appraiser. UCDP submission data includes condition and quality codes — matching these to the inspection photos from the same appraisals provides labels.
**Target:** Predicted condition and quality tier from photos; specific photo evidence supporting the classification; flag when photo evidence is inconsistent with appraiser-assigned rating
**Evaluation metric:** Agreement rate between model prediction and appraiser-assigned rating on held-out appraisals; inter-rater agreement rate between experienced appraisers (sets ceiling for model performance); CU flag rate for condition/quality inconsistencies with model-reviewed vs. unreviewed assignments
**Scope:** FNMA's own AI efforts (Appraisal Modernization) have invested in this direction for desktop appraisals. For traditional appraisals, the model serves as a consistency check. 12-18 month development for a production-quality condition/quality classifier across the full C1-C6/Q1-Q6 spectrum.
**Data availability:** UCDP submission data matched to appraisal photos provides the training signal. Property photo archives from a la mode and AMC platforms have millions of labeled inspection photos. Fannie Mae's Collateral Underwriter data is the most comprehensive source but access requires a formal data partnership.
