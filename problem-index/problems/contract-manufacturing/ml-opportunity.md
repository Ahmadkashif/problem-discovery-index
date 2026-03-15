# ML Opportunities — Contract Manufacturing

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Tags:** #gradient-boosting #gaussian-process #cnn #regression #anomaly-detection #tabular-ml #computer-vision #nlp #revenue-impact #compliance

---

## 1. First-Pass Yield Prediction and Process Optimization (Primary Opportunity)

**ML Task:** Regression (yield rate prediction) + Bayesian optimization (parameter recommendation)
**Input data:** MES production records — process parameters per lot (temperatures, pressures, speeds, cycle times), incoming material lot characteristics (incoming inspection measurements, lot codes), machine state features (calibration age, tooling hours, maintenance recency), environmental conditions (ambient temperature, humidity where relevant)
**Target:** First-pass yield rate per production lot (continuous regression target); units failing inspection vs. total units produced
**Model:** Gradient boosting regression baseline; Gaussian process for uncertainty quantification and parameter optimization; SHAP values for process engineer interpretability
**Evaluation:** MAE on yield prediction; yield improvement on hold-out programs using recommended parameters vs. historical defaults
**Scope:** Per-production-lot at setup and mid-run; parameter optimization recommendation before each new program setup
**Data availability:** MES (Rockwell FactoryTalk, Siemens Opcenter, Plex) + quality inspection records; requires 2+ years of production history with parameter logging enabled

---

## 2. Automated Visual Defect Detection and Classification

**ML Task:** Object detection + multiclass classification (defect type: scratch / pit / crack / dimension / cosmetic)
**Input data:** Part inspection images under controlled illumination; labeled examples of accept/reject conditions per part number with defect category annotations; OEM workmanship standard translated to defect taxonomy
**Target:** Binary accept/reject per unit + defect type classification for rejects
**Model:** Fine-tuned CNN (EfficientNet or ResNet) for classification; PatchCore or EfficientAD for anomaly detection baseline on new part numbers with limited labeled defects
**Evaluation:** Recall on actual defects (miss rate); precision (false reject rate); comparison to human inspector agreement rate on boundary samples
**Scope:** Inline inspection station; real-time inference per unit at inspection conveyor speed
**Data availability:** Requires image capture infrastructure at inspection station; labeled training data from OEM workmanship standards + historical rejected parts with defect documentation

---

## 3. SPC Alarm Root Cause Classification

**ML Task:** Multiclass classification (root cause: machine drift / material lot change / tooling wear / operator setup / measurement artifact / unknown)
**Input data:** SPC alarm type and pattern (which rules triggered, trending direction), simultaneous alarm co-occurrence across parameters, recent machine maintenance events, material lot change events, operator shift change, tooling hours, historical root cause records for prior alarms on the same machine
**Target:** Root cause category from historical corrective action records matched to corresponding alarms
**Model:** Gradient boosting classifier; feature engineering on alarm timing and co-occurrence patterns
**Evaluation:** Top-1 accuracy on historical alarm-to-root-cause pairs; reduction in mean time-to-root-cause attribution
**Scope:** Real-time alarm triage at SPC system level; inference per alarm within seconds
**Data availability:** SPC system alarm logs + corrective action records (from quality management system); machine maintenance logs

---

## 4. Quote Cost Model from Program Actuals

**ML Task:** Regression (per-operation cost: setup hours, cycle time, yield rate, rework rate, material cost)
**Input data:** Historical program records — quoted vs. actual hours per operation, actual yield and rework rates, material waste rates; program characteristic features (part complexity class, material type, tolerance class, production volume, tooling type, customer sector)
**Target:** Actual cost per operation type (separate models for setup, cycle time, yield, rework)
**Model:** Gradient boosting regression per cost element; program similarity search (cosine similarity on feature vectors) for reference program retrieval
**Evaluation:** MAE of cost estimate vs. actuals on held-out programs; reduction in quote error rate (actual margin vs. quoted margin)
**Scope:** Quote workflow integration; one estimate per quote request with confidence intervals
**Data availability:** ERP (Epicor, Infor, Plex) historical program cost records; requires systematic actual cost capture at operation level

---

## 5. Production Schedule Feasibility Prediction

**ML Task:** Binary classification (will this schedule achieve on-time delivery: yes/no) + regression (predicted completion date)
**Input data:** Work center capacity utilization by time period, program priority and due dates, historical cycle time variation, setup time distributions, current WIP levels, planned maintenance schedule, material arrival schedule
**Target:** On-time delivery outcome per program per period; actual completion date vs. scheduled date
**Model:** Gradient boosting on schedule feature set; simulation-based approaches for complex multi-program scheduling scenarios
**Evaluation:** Precision/recall on late delivery prediction; lead time for actionable prediction (must identify risk 2+ weeks before due date)
**Scope:** Weekly scheduling review; flags at-risk programs with identified constraint
**Data availability:** ERP/MES scheduling and actual completion records; 12+ months of historical schedule vs. actual data
