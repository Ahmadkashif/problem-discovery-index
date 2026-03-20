# Machine Learning Opportunities — Auto Repair Shops

**Industry:** [[auto-repair-shops|Auto Repair Shops]]
**Derived from:** [[problems/auto-repair-shops/high-impact|High Impact]], [[problems/auto-repair-shops/low-impact-1|Low Impact 1]], [[problems/auto-repair-shops/low-impact-2|Low Impact 2]], [[problems/auto-repair-shops/worker-life-1|Worker Life 1]], [[problems/auto-repair-shops/worker-life-2|Worker Life 2]]

---

## 1. Fault Diagnosis from Audio, Vibration, and OBD Signals
#cnns #lstms-and-grus #feature-engineering #loss-functions #evaluation-metrics #gradient-descent #backpropagation #probability-distributions #tacit-knowledge-ml

**Problem statement:** Master technicians diagnose engine, transmission, and drivetrain faults from sound and vibration patterns that they cannot articulate as explicit rules — a timing chain rattle sounds different from a valve tick, and a wheel bearing hum differs from a tire noise, but the distinctions are learned through thousands of hours of exposure. This tacit auditory and tactile knowledge is the most valuable and least transferable skill in the trade.

**ML task:** Multiclass classification (predict fault component from multi-modal sensor input)
**Input data:** 10-30 second audio recordings from engine bay, cabin, and undercarriage using smartphone microphones or dedicated sensors; OBD-II live data streams (RPM, engine load, coolant temp, fuel trim, misfire counts); vibration data from accelerometer placement; vehicle profile (year, make, model, mileage, prior repair history)
**Target:** Fault component classification across 50-100 common failure modes (e.g., timing chain tensioner, rod bearing, wheel bearing, CV joint, exhaust leak, vacuum leak), with confidence score and differential diagnosis ranking
**Evaluation metric:** Top-3 accuracy (correct fault in top 3 predictions) targeting 85%+; weighted by repair cost to penalize missing expensive failures. Recall critical for safety-related faults (braking, steering, suspension).
**Scope:** Requires partnership with 20-50 shops to collect paired audio/diagnosis data over 12-18 months. Target: 10,000-50,000 labeled diagnostic events. 3-4 person ML team, 12-18 month build. Data collection infrastructure (standardized recording protocols) is the hardest part. Model architecture: CNN for spectrogram features + LSTM for temporal patterns + tabular features from OBD data in an ensemble.
**Data availability:** Audio data must be collected fresh — no existing datasets of paired engine-sound/diagnosis data exist at scale. OBD data is available through standard interfaces but varies by vehicle manufacturer. The labeling challenge is significant: the confirmed repair (ground truth) may not perfectly match the audio-captured symptom if multiple faults coexist.

---

## 2. Repair Time Estimation by Vehicle and Condition
#gradient-boosting #decision-trees #linear-regression #feature-engineering #cross-validation #evaluation-metrics #expectation-variance-covariance

**Problem statement:** Book time (Mitchell/AllData labor guides) estimates repair duration for an average vehicle, but actual time varies 50-200% based on rust, mileage, prior repairs, and regional conditions. This variance drives flat-rate pay inequity.

**ML task:** Regression (predict actual labor hours for a specific job on a specific vehicle)
**Input data:** Job code, vehicle year/make/model/mileage, geographic region (rust belt vs. sunbelt), prior repair history on this vehicle, technician experience level, shop-specific efficiency factors
**Target:** Actual labor hours to completion
**Evaluation metric:** MAE in hours; secondary: percentage of estimates within 20% of actual
**Scope:** Trainable on 50,000-200,000 historical repair orders from shop management systems. 2-person team, 4-6 month build. Data is available — the challenge is cleaning inconsistent time tracking.
**Data availability:** Shop management systems (Tekmetric, Shop-Ware) contain repair orders with job codes, vehicle info, and clock-in/clock-out times. Data quality varies: some shops track actual time carefully, others estimate. Multi-shop aggregation needed for regional patterns.

---

## 3. Predictive Parts Failure from Vehicle Profiles
#gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #probability-distributions #maximum-likelihood-estimation #conditional-probability-and-bayes-theorem

**Problem statement:** Certain vehicles develop predictable failure patterns (e.g., 2012-2015 Honda Civics with timing chain stretch at 80-100K miles), but this knowledge is scattered across TSBs, forums, and individual technician experience.

**ML task:** Survival analysis / time-to-event prediction (predict when each major component will likely need replacement)
**Input data:** Vehicle year/make/model/engine, current mileage, maintenance history, driving conditions (urban/highway/mixed), climate zone, prior failure events for same model year
**Target:** Predicted mileage/time to failure for top 20 wear components (brakes, timing chain, water pump, alternator, etc.)
**Evaluation metric:** Concordance index (C-index) for survival predictions; calibration of predicted vs. actual failure distributions
**Scope:** Trainable on 1M+ repair orders aggregated across shop management platforms. 2-person team, 6-9 month build. Model enables proactive service recommendations during DVI.
**Data availability:** Repair order databases contain vehicle profiles and repair events. Aggregation across thousands of shops via management system APIs (Tekmetric, Shop-Ware, Mitchell) is feasible with data partnerships.

---

## 4. Customer Retention and Defection Prediction
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #conditional-probability-and-bayes-theorem

**Problem statement:** Shops lose 20-30% of customers annually but don't know which ones are at risk. A customer who skips a recommended service is 3x more likely to not return, but this signal is buried in repair order history.

**ML task:** Binary classification (will this customer return within 12 months?)
**Input data:** Visit frequency, service history, declined recommendations, average repair order value, communication engagement (text open rates, appointment confirmations), vehicle age and mileage, distance from shop
**Target:** Binary: returns within 12 months / does not return
**Evaluation metric:** AUC-ROC with emphasis on early identification (predicting defection 3-6 months before it happens)
**Scope:** Trainable on 10,000-50,000 customer histories. Lightweight model, 2-3 month build. Integrates with shop management CRM for automated retention outreach.
**Data availability:** Shop management systems contain full customer transaction history. Communication engagement data available from integrated messaging platforms. Low data engineering effort for single-shop deployment.

---

## 5. DVI Photo Analysis for Condition Assessment
#cnns #transfer-learning #loss-functions #evaluation-metrics #backpropagation #gradient-descent #matrix-algebra #optimization-fundamentals

**Problem statement:** Technicians take 20-40 photos during vehicle inspections, but service advisors lack the technical knowledge to interpret them. An automated system that grades component condition from photos would bridge this gap.

**ML task:** Multiclass classification (grade component condition: good/fair/poor/critical) from inspection photos
**Input data:** Inspection photos of tires, brakes, belts, hoses, fluid conditions, suspension components — captured in-shop under variable lighting with smartphone cameras
**Target:** Condition grade (4-class) per component with measurement estimates where applicable (tire tread depth in 32nds, brake pad thickness in mm)
**Evaluation metric:** Accuracy on condition grade; MAE on measurement estimates. Must not classify "critical" as "good" (safety constraint: penalize dangerous false negatives heavily).
**Scope:** Requires 50,000-100,000 labeled inspection photos. Transfer learning from automotive datasets feasible. 2-3 person team, 6-9 month build. Camera quality and lighting variation are primary challenges.
**Data availability:** DVI platforms already capture millions of photos daily. Labeling requires technician review — crowdsourcing not feasible due to technical expertise required. Partnership with DVI platform (AutoVitals, Bolt On) provides data access.
