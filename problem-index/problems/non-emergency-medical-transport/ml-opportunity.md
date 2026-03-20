# Machine Learning Opportunities — Non-Emergency Medical Transport

**Industry:** [[non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Derived from:** [[problems/non-emergency-medical-transport/high-impact|High Impact]], [[problems/non-emergency-medical-transport/low-impact-1|Low Impact 1]], [[problems/non-emergency-medical-transport/low-impact-2|Low Impact 2]], [[problems/non-emergency-medical-transport/worker-life-1|Worker Life 1]], [[problems/non-emergency-medical-transport/worker-life-2|Worker Life 2]]

---

## 1. Patient Mobility and Trip Time Assessment from Profile Data
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #probability-distributions #tacit-knowledge-ml

**Problem statement:** Experienced NEMT dispatchers read a patient's name, address, facility destination, appointment type, and any prior trip notes — then instantly estimate the correct vehicle type, required equipment, expected load/unload time, and total trip duration. This judgment integrates dozens of implicit signals: a dialysis patient at a specific clinic means a wheelchair and 12-minute load time because that building has no ramp and uses a side entrance; a patient listed as "ambulatory" but going to an oncology center likely needs extra time because chemo fatigue slows them; a bariatric patient at a second-floor walk-up means a stretcher crew. New dispatchers lack this internalized knowledge and consistently under-estimate trip times by 20-40%, causing cascading late arrivals across entire routes.

**ML task:** Multi-output regression — predict (a) required vehicle/equipment type, (b) pickup dwell time in minutes, (c) dropoff dwell time in minutes, and (d) total trip duration including transit.

**Input data:** Patient profile fields (mobility classification, weight category, equipment flags, address), facility characteristics (type of medical facility, floor level, entrance accessibility, historical dwell times at that location), appointment type (dialysis, oncology, primary care, PT), time of day, day of week, weather conditions, historical trip records for this patient and facility combination. Sources: dispatch software trip logs, GPS breadcrumb data with timestamps, driver-reported actual times.

**Target:** Continuous values — pickup dwell minutes, dropoff dwell minutes, total trip minutes. Secondary classification target: vehicle type and equipment configuration.

**Evaluation metric:** Mean Absolute Error (MAE) on trip duration predictions, with asymmetric loss weighting — under-prediction penalized 2x over-prediction because underestimating trip time causes late arrivals for subsequent patients. Vehicle type accuracy measured by F1-score per class.

**Scope:** Requires 6-12 months of historical trip data with GPS-derived actual timestamps (not driver-reported). A 100-vehicle operator generates ~500 trips/day, yielding 90K-130K labeled examples in 12 months. Feature engineering is the main effort: extracting facility-level dwell time patterns, patient-level trends, and time-of-day effects. Gradient-boosted model (XGBoost/LightGBM) is the right starting point — no deep learning needed. A 2-person ML team can build an MVP in 8-10 weeks. The core challenge is data collection: most operators don't currently capture granular dwell time breakdowns, so the first deployment requires instrumenting the driver app to separately log "arrived at pickup," "patient loaded," "departed pickup" as distinct timestamps.

**Data availability:** GPS breadcrumb data exists in most dispatch systems but is rarely parsed into dwell-time segments. Patient profiles exist in scheduling software. Facility characteristics must be bootstrapped from historical patterns (cluster facilities by average dwell time) and enriched over time. Labeling is implicit — the model learns from actual trip durations — but ground truth quality depends on GPS accuracy and driver compliance with status updates.

---

## 2. Patient No-Show Prediction
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #bias-variance-tradeoff

**Problem statement:** 15-20% of scheduled NEMT trips result in patient no-shows, wasting driver time, creating route gaps, and stressing dispatchers who must re-sequence on the fly. Predicting which patients are likely to no-show allows proactive overbooking, pre-positioned backup routes, and targeted patient reminder outreach.

**ML task:** Binary classification — predict whether a scheduled trip will result in a no-show.

**Input data:** Patient history (prior no-show rate, trip frequency, days since last trip), appointment characteristics (type — dialysis patients rarely no-show vs. follow-up appointments which no-show at 25%+), temporal features (day of week, time of day, weather forecast, holiday proximity), facility type, distance from patient home, whether this is a recurring standing order or a one-time trip, and communication features (whether a reminder call was made, whether the patient confirmed). Sources: dispatch system trip records with outcome codes, patient contact logs.

**Target:** Binary label — no-show (1) or completed trip (0).

**Evaluation metric:** AUC-ROC as primary ranking metric; optimize operating point for recall at 70%+ (catch most no-shows) while keeping false positive rate under 30% to avoid over-correcting on patients who would have shown up. Precision-recall trade-off matters because acting on a false positive (e.g., overbooking) has lower cost than missing a true no-show (wasted vehicle time).

**Scope:** Straightforward tabular classification. Most NEMT operators with 12+ months of data have 50K-200K trip records with no-show labels already coded for Medicaid billing purposes. Feature engineering around patient behavioral patterns and temporal effects is the main ML work. A single ML engineer can deliver a production model in 4-6 weeks. Integration into dispatch software to surface risk scores alongside trip assignments is the deployment bottleneck.

**Data availability:** High — no-show outcomes are already tracked in billing systems because Medicaid requires documentation of attempted trips. Patient history and trip characteristics are in scheduling databases. Weather data is freely available. The main gap is reminder call/confirmation data, which is often tracked informally.

---

## 3. Trip Duration Prediction by Patient, Facility, and Conditions
#gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #confidence-intervals #bias-variance-tradeoff #gradient-descent

**Problem statement:** Route optimization engines require accurate trip duration estimates, but NEMT trip times are far more variable than standard logistics due to patient-specific factors (mobility level, cognitive state, equipment needs), facility-specific factors (parking, entrance accessibility, elevator wait times), and condition-specific factors (weather affecting wheelchair loading, traffic patterns near hospital campuses at shift change). Current systems use static time estimates that are wrong by 20-40% on individual trips.

**ML task:** Regression — predict door-to-door trip duration in minutes for a specific patient-facility-time combination.

**Input data:** Patient mobility classification and historical trip durations, facility ID with historical average dwell times, route distance and estimated drive time from mapping API, time of day (hospital campus traffic peaks at 7-8am and 3-4pm), day of week, weather conditions (rain adds 3-5 minutes to wheelchair loading), vehicle type assigned, whether trip is shared-ride (adds intermediate stops). Sources: GPS trip logs with timestamps, dispatch records, weather APIs, mapping APIs.

**Target:** Continuous — total trip duration in minutes from dispatch to completion.

**Evaluation metric:** MAE with emphasis on reducing large under-predictions (>15 minutes off) that cause cascading delays. Percentile-based metrics (P90 prediction accuracy) matter more than mean accuracy because route optimization needs reliable upper bounds.

**Scope:** This model shares significant feature overlap with the patient mobility assessment model (#1) but focuses on total trip duration including transit time rather than dwell time alone. It serves as the prediction engine feeding the route optimizer. Data requirements are identical. Can be built as an extension of model #1 or as a standalone model. 2-person team, 6-8 weeks, with the mapping API integration being the main engineering (not ML) effort.

**Data availability:** Same as #1 — GPS data exists but needs parsing. The additional requirement here is real-time traffic and weather data integration, both readily available through commercial APIs.

---

## 4. Reinforcement Learning Route Optimizer with Dynamic Re-Planning
#markov-decision-processes #dynamic-programming #policy-gradient-methods #gradient-boosting #evaluation-metrics #optimization-fundamentals #expectation-variance-covariance #workflow-orchestration

**Problem statement:** Given a set of trip requests with predicted durations, vehicle fleet with heterogeneous capabilities, and hard constraints (appointment windows, mobility compatibility, Medicaid shared-ride rules, maximum detour limits), find the route assignment that maximizes on-time performance and fleet utilization — and re-optimize in real time as no-shows, cancellations, and add-ons arrive throughout the day.

**ML task:** Sequential decision-making — assign trips to vehicles and sequence stops to maximize a composite reward (on-time arrivals, fleet utilization, compliance with broker rules) subject to constraints that change dynamically.

**Input data:** Trip requests with predicted durations (from models #1 and #3), vehicle positions and capacities in real time, driver hours-of-service status, no-show probability scores (from model #2), broker-specific rules (max shared-ride time, max detour miles), and real-time traffic conditions. The state space is the current assignment of all trips to all vehicles with their sequencing; the action space is reassigning or re-sequencing trips.

**Target:** Composite reward signal — weighted combination of on-time performance (primary), total fleet miles (secondary), driver overtime avoidance (tertiary), and compliance constraint satisfaction (hard constraint, not reward).

**Evaluation metric:** On-time pickup percentage (target: 95%+), total fleet deadhead miles, trips completed per vehicle per day. Compare against current dispatcher performance and against classical VRP solver baselines.

**Scope:** This is the hardest ML problem in the NEMT stack. Classical VRP solvers can handle the static morning plan, but real-time re-optimization as the day unfolds is where RL adds value. Requires models #1-3 as prerequisite prediction engines. A 3-4 person team (ML engineer, optimization engineer, backend engineer, domain expert) over 4-6 months for an MVP that handles re-optimization for a single metro area fleet. The RL agent needs a simulation environment built from historical trip data to train before deployment. Transfer across operators requires retraining the prediction models but the RL policy structure can be shared.

**Data availability:** Training requires a simulation environment, not direct labeled data. The simulation is built from historical trip records (which operators have) plus the prediction models. The RL agent trains in simulation and is validated against historical dispatcher decisions. The cold-start problem is real — a new operator needs 3-6 months of data for the prediction models before the RL optimizer can be calibrated.
