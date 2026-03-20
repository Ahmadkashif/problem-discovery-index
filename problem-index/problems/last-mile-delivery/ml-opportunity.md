# Machine Learning Opportunities — Last-Mile Delivery

**Industry:** [[last-mile-delivery|Last-Mile Delivery]]
**Derived from:** [[problems/last-mile-delivery/high-impact|High Impact]], [[problems/last-mile-delivery/low-impact-1|Low Impact 1]], [[problems/last-mile-delivery/low-impact-2|Low Impact 2]], [[problems/last-mile-delivery/worker-life-1|Worker Life 1]], [[problems/last-mile-delivery/worker-life-2|Worker Life 2]]

---

## 1. First-Attempt Delivery Success Prediction
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #bias-variance-tradeoff #revenue-impact

**Problem statement:** Predict which stops will fail on first attempt to enable proactive interventions (pre-delivery notification, alternate delivery options) before the driver arrives.

**ML task:** Binary classification (first-attempt delivery failure: yes/no) from stop and address features
**Input data:** Delivery attempt records: address type (residential/commercial/apartment), prior delivery attempts at this address, delivery time-of-day, package type, customer notification opt-in status, seasonal and day-of-week indicators
**Target:** Failure probability per stop; recommended intervention (notify recipient, locker routing, access instruction lookup)
**Evaluation metric:** Recall on failed first attempts (did we flag them pre-delivery?); false positive rate (unnecessary interventions on stops that would have succeeded); reduction in first-attempt failure rate for DSPs using the model
**Scope:** Any DSP with 6+ months of delivery history has training data. Gradient boosting on 8-10 stop features: 3-4 week project. Route4Me or Onfleet integration.
**Data availability:** Delivery attempt records with outcome are in any delivery management system. Address type data from geocoding APIs. Prior delivery history per address is in the DSP's delivery history.

---

## 2. Stop Time Prediction for Route Planning
#gradient-boosting #linear-regression #feature-engineering #cross-validation #evaluation-metrics #descriptive-statistics #bias-variance-tradeoff #quick-win

**Problem statement:** Predict per-stop service time (from parking to package placed) accurately for route planning, replacing uniform time estimates with address-specific predictions that reflect actual time variability.

**ML task:** Regression — service time in minutes from address and package features
**Input data:** Historical stop records with GPS-measured service time (time from vehicle stop to driving away), address type, package count and weight, access complexity flag, time-of-day, driver ID (driver-specific variance)
**Target:** Service time estimate per stop; uncertainty range for high-variability address types; daily route completion probability given the stop sequence
**Evaluation metric:** MAE between predicted and actual service times; reduction in route completion failures (drivers who run out of time) vs. uniform-estimate routing; customer ETA accuracy improvement
**Scope:** Quick win — service time data is in any GPS-tracked delivery operation (time at each address is measurable from vehicle GPS). Gradient boosting on address + driver features: 2-3 week project.
**Data availability:** Telematics platforms (Samsara, Verizon Connect) log per-stop arrival and departure times. Address type and package data are in the delivery management system.

---

## 3. Driver Performance Efficiency Analysis
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #descriptive-statistics #hypothesis-testing

**Problem statement:** Decompose per-driver delivery efficiency into specific behavior categories (parking decisions, address navigation, recipient interaction speed, vehicle loading sequence) to enable targeted performance coaching.

**ML task:** Multiclass classification — per-stop time decomposition into behavior categories; driver performance benchmarking vs. peer group on each component
**Input data:** Per-stop time series from GPS (drive time, parking time, walk time estimate from GPS precision, total stop duration); stop sequence adherence; address complexity controls (apartment vs. house, prior failure history)
**Target:** Per-driver efficiency score by behavior component; outlier stops with specific behavior diagnosis; coaching recommendation per gap
**Evaluation metric:** Stops per day improvement after targeted coaching vs. general performance feedback; driver retention rate for coached vs. non-coached groups
**Scope:** GPS data at 1-second resolution allows walk time and parking decision inference. Any telematics-equipped fleet has the data. 6-8 week project to build the behavior decomposition model.
**Data availability:** Samsara and similar telematics platforms provide per-second GPS traces. The behavior decomposition requires inference from position data — an intermediate modeling step before the performance analysis.

---

## 4. POD Photo Quality Classification
#cnns #transfer-learning #loss-functions #backpropagation #gradient-descent #evaluation-metrics #compliance #quick-win

**Problem statement:** Assess proof-of-delivery photo quality in real time at driver submission — flagging photos that lack address visibility, package clarity, or adequate lighting before submission.

**ML task:** Binary classification per photo quality criterion: address number visible (yes/no), package visible and identifiable (yes/no), adequate lighting (yes/no), adequate framing (yes/no)
**Input data:** POD photos labeled by quality criterion (adequate evidence vs. insufficient). Supervision from claims records: photos associated with successful claim disputes vs. claims where evidence was deemed insufficient.
**Target:** Real-time quality flag per submitted photo; specific failure criterion with driver guidance for retake
**Evaluation metric:** Insufficient-evidence claim rate before vs. after quality check implementation; driver retake rate (how often do drivers need to retake?); photo quality score improvement over time as drivers adapt
**Scope:** Quick win — image quality classification is well within standard CNN capability. A labeled dataset of 5,000-10,000 POD photos (adequate vs. insufficient per criterion) trains a fast mobile-deployable model. 4-6 week project. Onfleet or FedEx/UPS scan app integration.
**Data availability:** DSPs have POD photo archives. Claims records provide the evidence adequacy labels for photos involved in disputes. Prospective labeling by operations managers covers the training set quickly.

---

## 5. Package Theft Pattern Detection and High-Risk Area Flagging
#gradient-boosting #dbscan #logistic-regression #feature-engineering #evaluation-metrics #descriptive-statistics #conditional-probability-and-bayes-theorem

**Problem statement:** Identify delivery zones and time windows with elevated package theft risk from "delivered but not received" claim patterns, enabling routing decisions (locker redirect, carrier hold) for high-risk addresses.

**ML task:** Anomaly detection — geographic clusters of above-expected DBNR (delivered but not received) claims; binary classification (high theft risk: yes/no) per address from claim history and location features
**Input data:** DBNR claim records by address and date. Features: address location, time of delivery (day/evening), package visibility from street, neighborhood crime density proxy (from public data), seasonal patterns.
**Target:** High-risk flag per address for routing decision (proceed with standard delivery / notify recipient / locker redirect); geographic risk heat map for operations planning
**Evaluation metric:** Reduction in DBNR claim rate for high-risk addresses with proactive intervention vs. standard delivery; false positive rate (unnecessary reroutes for addresses that would not have been stolen from)
**Scope:** DBNR claim frequency by address is in the delivery management system. Geographic clustering (DBSCAN) identifies risk zones. Classification on address features: 3-4 week project. Note: interventions for high-risk areas require careful implementation to avoid geographic discrimination concerns.
**Data availability:** DBNR claims by address are in the delivery management system. Crime data by geography is available from public police department datasets.
