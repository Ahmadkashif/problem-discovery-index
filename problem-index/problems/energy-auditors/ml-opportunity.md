# Machine Learning Opportunities — Energy Auditors

**Industry:** [[energy-auditors|Energy Auditors]]
**Derived from:** [[problems/energy-auditors/high-impact|High Impact]], [[problems/energy-auditors/low-impact-1|Low Impact 1]], [[problems/energy-auditors/low-impact-2|Low Impact 2]], [[problems/energy-auditors/worker-life-1|Worker Life 1]], [[problems/energy-auditors/worker-life-2|Worker Life 2]]

---

## 1. Energy Savings Prediction from Building Characteristics (Tacit Knowledge Calibration)
#gradient-boosting #gaussian-processes #feature-engineering #cross-validation #evaluation-metrics #bayesian-inference #confidence-intervals #probability-distributions #bias-variance-tradeoff #tacit-knowledge-ml #revenue-impact

**Problem statement:** Experienced energy auditors mentally adjust modeled savings predictions based on building archetypes, construction vintages, and micro-climate patterns they have internalized over hundreds of audits — corrections that are never recorded and cannot be transferred to junior auditors or modeling software. The ML task is to learn these correction factors from historical audit-to-outcome data, producing calibrated savings estimates with uncertainty quantification.

**ML task:** Regression with uncertainty estimation (point prediction + prediction intervals)
**Input data:** Structured audit records (building vintage, square footage, insulation levels, HVAC specs, blower door results, duct leakage, window types, climate zone), weather-normalized pre-retrofit utility consumption, proposed retrofit measure specifications. Sources: utility weatherization program databases (DOE WAP, state energy offices), BPI GoldStar contractor records, Ekotrope/TREAT project archives.
**Target:** Actual weather-normalized energy savings (kBtu/year or % reduction) measured 12 months post-retrofit, paired with the original model-predicted savings to learn the correction function.
**Evaluation metric:** Mean Absolute Percentage Error (MAPE) on held-out post-retrofit outcomes, with secondary focus on calibration of prediction intervals (90% intervals should contain 90% of actuals). Overestimation is costlier than underestimation — asymmetric loss weighting with 1.5x penalty on over-prediction.
**Scope:** Requires partnership with 3-5 utility weatherization programs to access paired pre/post data. Initial dataset target: 5,000+ completed retrofits with 12-month post-period utility data. Gradient-boosted trees (XGBoost/LightGBM) for point estimates, Gaussian Process or conformal prediction for uncertainty bands. 2-person ML team, 6-9 month build cycle including data acquisition and cleaning. The hardest part is not modeling but data harmonization across programs with different schemas.
**Data availability:** DOE WAP evaluations are partially public but aggregated. Individual program data requires MOUs with state energy offices and utility program administrators. BPI GoldStar contractors have project-level data but no standard export format. Data labeling is straightforward (utility bills are ground truth) but linking audit records to post-period bills requires address matching and utility data-sharing agreements that take 3-6 months to execute.

---

## 2. Retrofit Measure Prioritization and Sequencing
#gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #optimization-fundamentals #bias-variance-tradeoff #revenue-impact

**Problem statement:** Given a building's current condition and a set of possible retrofit measures, determine the optimal order and combination of measures that maximizes energy savings per dollar spent, accounting for measure interactions (e.g., air sealing before insulation, right-sizing HVAC after envelope improvements).

**ML task:** Learning-to-rank with budget constraints
**Input data:** Building characteristics (same as Opportunity 1), measure cost estimates by local market, measure interaction matrices (known physics-based interactions), historical project data showing which measure combinations produced the best outcomes.
**Target:** Ranked list of measure packages with predicted savings, cost, and ROI for each package — optimized for total savings within a given budget constraint.
**Evaluation metric:** NDCG@k on measure rankings compared to expert-recommended sequences; secondary metric is actual savings achieved by top-ranked package vs. expert-selected package in A/B deployment.
**Scope:** Can bootstrap from physics-based interaction models (BEopt, EnergyPlus parametric runs) and refine with field outcome data. 2-person team, 4-6 months. The ranking model can launch with physics priors and improve as outcome data accumulates.
**Data availability:** Physics-based simulation data is freely generatable. Field outcome data by measure combination is sparse — most programs report total savings, not per-measure attribution. Requires careful experimental design or Shapley-value-style attribution from programs that vary measure combinations across similar buildings.

---

## 3. Utility Bill Disaggregation for Pre-Audit Screening
#cnns #lstms-and-grus #time-series-forecasting #backpropagation #loss-functions #gradient-descent #activation-functions #feature-engineering #data-integration

**Problem statement:** Before an auditor visits a building, disaggregate monthly or interval utility bill data into end-use categories (heating, cooling, baseload, water heating) to pre-screen buildings for the most promising retrofit opportunities and focus the auditor's field time on confirmed problem areas.

**ML task:** Time-series decomposition / multi-output regression
**Input data:** 12-36 months of monthly utility bills (gas and electric), local weather data (heating/cooling degree days), building metadata (vintage, square footage, fuel types) where available. Sources: utility Green Button data, program intake forms.
**Target:** Estimated annual consumption by end use (heating kBtu, cooling kWh, baseload kWh, water heating kBtu) with confidence scores.
**Evaluation metric:** Mean Absolute Error per end-use category, validated against sub-metered buildings from RECS (Residential Energy Consumption Survey) and RBSA (Regional Building Stock Assessment) datasets. Heating/cooling split accuracy is most critical — errors there misallocate auditor attention.
**Scope:** Strong prior work in NILM (non-intrusive load monitoring) at the appliance level; this is a coarser task (end-use, not appliance) using monthly rather than second-level data, which is easier but less precise. 1-2 person team, 3-4 months to MVP. Models can launch with the public RECS/RBSA calibration data and improve per utility territory as program data accumulates.
**Data availability:** RECS microdata is public with end-use estimates. RBSA covers the Pacific Northwest with sub-metered data. Green Button Connect enables automated utility data access in participating territories. The main gap is labeled ground truth for non-metered buildings — transfer learning from sub-metered datasets to monthly-only buildings is the key technical challenge.

---

## 4. Audit Quality Scoring and Anomaly Detection
#gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #descriptive-statistics #probability-distributions #bias-variance-tradeoff #compliance

**Problem statement:** Utility program administrators currently review 10-100% of submitted audits manually for quality control — checking for data consistency, reasonable values, and proper protocol adherence. An automated quality scoring system flags audits with likely errors or protocol deviations before they enter the review queue, focusing QA staff time on genuinely problematic submissions.

**ML task:** Anomaly detection + binary classification (pass/fail prediction)
**Input data:** Completed audit records with all field measurements, photos, and model outputs. Historical QA outcomes (pass, fail with reason codes, revision requests). Sources: utility program QA databases, BPI quality management systems.
**Target:** Per-audit quality score (0-1 probability of passing QA) plus flagged fields with anomaly explanations (e.g., "reported R-49 attic insulation in 1955 home with no documented retrofit — verify").
**Evaluation metric:** Recall on true QA failures at 80%+ (must catch real problems), with precision above 50% (fewer than half of flags should be false alarms, or reviewers will ignore the system). F2 score as primary composite metric, weighting recall over precision.
**Scope:** Isolation Forest or autoencoder for unsupervised anomaly detection on field values; gradient-boosted classifier for pass/fail prediction trained on historical QA outcomes. Requires access to 2,000+ audits with QA disposition labels. 1-2 person team, 3-5 months. The interpretability requirement (must explain *why* a field is flagged) adds complexity — SHAP values on the GBM provide per-feature attribution.
**Data availability:** Utility programs with formal QA processes (BPI GoldStar, HPwES) have structured QA records but rarely share them externally. A partnership with 2-3 large utility programs (each contributing 500-1,000 labeled audits) would provide sufficient training data. The labeling is already done — QA reviewers produce pass/fail/revision dispositions with reason codes as part of their existing workflow.
