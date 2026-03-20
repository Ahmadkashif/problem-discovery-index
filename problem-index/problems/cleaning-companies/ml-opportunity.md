# Machine Learning Opportunities — Cleaning Companies

**Industry:** [[cleaning-companies|Cleaning Companies]]
**Derived from:** [[problems/cleaning-companies/high-impact|High Impact]], [[problems/cleaning-companies/low-impact-1|Low Impact 1]], [[problems/cleaning-companies/low-impact-2|Low Impact 2]], [[problems/cleaning-companies/worker-life-1|Worker Life 1]], [[problems/cleaning-companies/worker-life-2|Worker Life 2]]

---

## 1. Facility Cleaning Time Estimation from Walkthrough Assessment
#gradient-boosting #decision-trees #linear-regression #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #tacit-knowledge-ml

**Problem statement:** Experienced commercial cleaning estimators walk a facility and intuitively know the labor hours required — reading floor type, traffic patterns, fixture density, window count, and specialty requirements in a way that produces estimates within 5-10% of actual labor needs. New estimators relying on square footage alone miss by 20-40%. This tacit knowledge — the ability to "see" labor hours in a space — is the most commercially valuable skill in the cleaning business.

**ML task:** Regression (predict labor hours per cleaning visit for a facility)
**Input data:** Structured facility data (total sq ft, sq ft by area type: office/restroom/lobby/kitchen/warehouse, floor type by area, fixture counts, employee headcount, cleaning frequency), estimator walkthrough notes, optional walkthrough photos for automated feature extraction, geographic region (labor productivity varies)
**Target:** Labor hours per cleaning visit, broken down by task category (general cleaning, restrooms, floor care, trash, specialty)
**Evaluation metric:** MAPE on predicted labor hours targeting <10%; MAE in absolute hours. Asymmetric loss: underprediction (margin destruction) penalized 2x overprediction (lost contract).
**Scope:** Requires 1,000-5,000 completed commercial contracts with actual cleaning time data and facility characteristics. 2-person team, 6-9 months. Data collection challenge: most companies don't track actual cleaning time by facility in structured form.
**Data availability:** Facility characteristics available from proposals and contracts. Actual cleaning time requires GPS/check-in data or time-tracking integration. Multi-company dataset needed for sufficient coverage of facility types. Companies may be reluctant to share competitive bidding data.

---

## 2. Post-Cleaning Quality Assessment from Photos
#cnns #logistic-regression #transfer-learning #loss-functions #evaluation-metrics #backpropagation #gradient-descent

**Problem statement:** Quality inspection is subjective and inconsistent when done by humans. A computer vision system that grades cleaning quality from standardized post-cleaning photos would enable consistent, scalable quality monitoring.

**ML task:** Binary classification per area (meets standard / does not meet standard), with sub-classifications for specific deficiencies (floor not mopped, trash not emptied, surfaces not wiped, restroom not restocked)
**Input data:** Post-cleaning photos taken at standardized angles in standardized areas (restroom mirror shot, floor overview, desk area, kitchen counters), lighting normalization
**Target:** Pass/fail per area with deficiency type labels
**Evaluation metric:** Accuracy on pass/fail; recall on fail cases (must catch quality issues) targeting 90%+. False positive rate below 15% to maintain crew trust.
**Scope:** Requires 20,000-50,000 labeled post-cleaning photos across facility types. Transfer learning from indoor scene datasets. 2-3 person team, 6-9 months. Lighting variation and camera angle consistency are primary challenges.
**Data availability:** Photos can be collected prospectively through existing inspection workflows. Labeling requires supervisor review — moderate effort. Standardizing photo capture protocol across multiple companies is the key challenge.

---

## 3. Client Churn Prediction
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #bias-variance-tradeoff

**Problem statement:** Commercial cleaning contracts are typically month-to-month or annual. Clients rarely complain before canceling — they simply solicit competitive bids and switch. Early warning of churn risk enables proactive retention.

**ML task:** Binary classification (will this client cancel within 90 days?)
**Input data:** Quality inspection scores over time, complaint frequency, communication patterns (response time to invoices, requests), contract tenure, pricing relative to market rate, service change requests, seasonal patterns
**Target:** Binary: cancels within 90 days / retains
**Evaluation metric:** AUC-ROC with emphasis on early detection; precision-recall at threshold where company can realistically act on top 10-20% of flagged accounts
**Scope:** Trainable on 2,000-5,000 client-contract records with retention outcomes. 1-person team, 2-3 months. Feature engineering from CRM and quality data.
**Data availability:** CRM and invoicing systems contain contract and communication data. Quality inspection scores from inspection platforms. Challenge: defining cancellation date for contracts that gradually reduce scope before terminating.

---

## 4. Crew Performance and Efficiency Modeling
#gradient-boosting #linear-regression #feature-engineering #cross-validation #evaluation-metrics #expectation-variance-covariance #regularization

**Problem statement:** Crew cleaning speed and quality vary significantly, but separating skill differences from site difficulty differences requires modeling both simultaneously.

**ML task:** Regression with crew and site random effects (predict cleaning time controlling for site difficulty to isolate crew efficiency)
**Input data:** Cleaning time per visit by crew, site characteristics, crew composition (experience levels, team size), day of week, time of shift
**Target:** Expected cleaning time for this crew at this site, plus crew efficiency score (deviation from expected across all sites)
**Evaluation metric:** MAE on cleaning time; stability of crew efficiency scores across different sites (should be consistent if the model properly controls for site difficulty)
**Scope:** Requires 6+ months of GPS/check-in time data from 50+ crews across 100+ sites. 1-person team, 3-4 months. Mixed-effects modeling or hierarchical gradient boosting.
**Data availability:** GPS check-in/check-out data from workforce management tools. Site data from contracts. Requires consistent time tracking across the operation.

---

## 5. Dynamic Route Optimization for Multi-Schedule Operations
#markov-decision-processes #dynamic-programming #optimization-fundamentals #gradient-descent #evaluation-metrics #feature-engineering #workflow-orchestration

**Problem statement:** Assigning 50-200 client sites with varying schedules (daily, 3x/week, weekly) to crews while minimizing drive time and balancing workloads is a combinatorial problem that companies solve manually.

**ML task:** Combinatorial optimization with learned drive-time and cleaning-time models
**Input data:** Client site locations and schedules, crew base locations, cleaning time estimates per site, drive time matrices (time-of-day adjusted), crew certifications and site requirements
**Target:** Weekly crew-to-site assignment minimizing total drive time subject to schedule, capacity, and qualification constraints
**Evaluation metric:** Total weekly drive hours vs. current baseline; workload balance (variance in hours across crews); schedule compliance rate
**Scope:** Classic VRP (Vehicle Routing Problem) variant. 2-person team, 4-6 months. Well-studied problem class with available solver libraries (OR-Tools, OptaPlanner). Customization for cleaning-specific constraints is the key effort.
**Data availability:** Client locations and schedules from CRM. Crew data from HR systems. Drive times from mapping APIs. Clean implementation data available.
