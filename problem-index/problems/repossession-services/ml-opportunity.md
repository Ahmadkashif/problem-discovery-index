# Machine Learning Opportunities — Repossession Agencies

**Industry:** [[repossession-services|Repossession Agencies]]
**Derived from:** [[problems/repossession-services/high-impact|High Impact]], [[problems/repossession-services/low-impact-1|Low Impact 1]], [[problems/repossession-services/low-impact-2|Low Impact 2]], [[problems/repossession-services/worker-life-1|Worker Life 1]], [[problems/repossession-services/worker-life-2|Worker Life 2]]

---

## 1. Learning the Veteran Agent's Address-and-Hour Read
#tacit-knowledge-ml #gradient-boosting #survival-analysis #bayesian-inference #feature-engineering #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** An experienced recovery agent reads an assignment and "knows" which of the borrower's addresses to work and at what hour, and when to leave a car that is right there because the attempt will end in an objection. The ML problem is to learn that read from the agency's own attempts and outcomes, rank each open file's address-hour windows by the chance the car is present and the attempt completes peacefully, and surface the reasoning to less experienced agents.

**ML task:** Probability that the vehicle is present at address *a* in hour-of-week window *w* (binary classification per address-window, calibrated), time-to-recovery survival modelling per file, and a secondary attempt-risk classifier (objection or incident if attempted now)
**Input data:** Assignment records (address list and type — residence, prior residence, employer, reference, skip-trace result; vehicle; lender; days since default); the agency's attempt log (address, timestamp, GPS trace, reason for leaving, photos); licence-plate hit and scan timestamps on the agency's own assignments; borrower employment pattern where the assignment carries it; neighbourhood, parking and access features (gated, garage, apartment lot); prior objections and incidents at the address; final outcome and where the car was actually recovered.
**Target:** Vehicle present and recovered at address-window (1/0) for attempted windows; days to recovery per file with censoring for closed-unrecovered files; attempt ended in objection or incident (1/0).
**Evaluation metric:** Recoveries per attempt-hour on a held-out period, comparing model-ranked plans with the agency's own plans — the metric the agency is paid on. For the presence model, top-k precision of the recommended window per file and calibration (Brier score), measured out of time. For the risk classifier, recall on incidents matters more than precision: a missed hostile address is a safety event, while a false flag moves an attempt to daylight. Report agreement with the veteran's own choices against their test-retest consistency as the ceiling.
**Scope:** The data collection challenge comes first: the expert's reasoning has to be captured while they work, in a truck at night, so the field app must log address, time, GPS and a one-tap leave reason with no typing, and past decisions must be reconstructed from GPS traces and status updates. The labelling challenge is that outcomes are confounded and experts disagree with themselves: an attempt that succeeded at 4 a.m. does not prove 4 a.m. was best, unattempted windows have no label, and the same agent picks differently after a bad week — so the model needs inverse-propensity weighting for which windows were tried, Bayesian pooling across agents and neighbourhoods, and repeated expert ratings on a sample. The deployment challenge is speed: the ranked plan must be ready before the night's route is set and explain itself in the agent's terms, or it will be ignored. 1 ML engineer and 1 product engineer with two or three agencies, 6–9 months; the first useful product is retrieval ("this car was scanned at the employer lot on three Thursdays") before any classifier is trusted.
**Data availability:** No dataset exists until agencies log attempts in a structured way; RDN and field apps hold status updates, not decisions. A single three-truck agency produces a few thousand attempts a year (estimate), so pooling across agencies is needed, which raises the question of whose data it is: assignment details belong to the lender, so a pooled model must train on agency-owned attempt features and outcomes.

---

## 2. Camera Hit Verification Against the Assignment
#cnns #object-detection #transfer-learning #evaluation-metrics #compliance #automation

**Problem statement:** A licence-plate match is not a vehicle match. Plates are misread, transferred between vehicles or cloned, and a hit on the wrong car sends a truck to take a car the lender has no claim to. Verify each camera hit by comparing the vehicle in the image with the assignment's make, model, colour and body style before a driver or agent acts.

**ML task:** Vehicle detection and make/model/colour classification from camera frames, plus a match score between the classified vehicle and the assignment record, with an abstain option routed to human confirmation
**Input data:** Camera frames attached to hits (often night, infrared, partial views); plate read and confidence; assignment vehicle description and VIN-decoded attributes; driver confirmations and rejections as labels.
**Target:** Match / mismatch / uncertain per hit.
**Evaluation metric:** Precision on "match" at a fixed abstain rate is the binding metric — a false match risks a wrongful repossession, while an abstention costs the driver a glance. Report recall on true matches separately so the system does not quietly reject good hits, and break results down by lighting and camera type.
**Scope:** Public vehicle make/model datasets give a starting point; the domain gap to night-time infrared crops from moving cars is large, so fine-tuning on the network's own confirmed hits is needed. 1–2 computer vision engineers, 4–6 months, most of it data curation. Best built by or with a camera network.
**Data availability:** The camera networks hold the images and the hit dispositions; agencies hold confirmations only for their own hits. Labels are a by-product of drivers' confirm/reject taps if the app records them.

---

## 3. Assignment Recoverability Scoring for Skip Pricing
#logistic-regression #gradient-boosting #survival-analysis #evaluation-metrics #revenue-impact #data-integration

**Problem statement:** Agencies are paid a flat fee on recovery and absorb the cost of files that will never close. Predict, at the moment an assignment is offered, the probability it will be recovered within 30, 60 and 90 days and the expected attempt-hours, so an agency can decide whether to accept, how to schedule it, and when to ask the client for a skip or close fee.

**ML task:** Calibrated probability of recovery by horizon (discrete-time survival), plus regression on expected attempt-hours to close
**Input data:** Assignment fields (address count and freshness, skip-trace hit, vehicle age and type, days since last payment, voluntary or involuntary, prior agency on the file, lender); agency coverage and distance from the addresses; recent hit activity on the plate; the agency's historical outcomes and attempt-hours by file type.
**Target:** Recovered by day 30/60/90 (censored at close-out); attempt-hours spent.
**Evaluation metric:** Calibration (Brier score and reliability curves) over discrimination — the score is used as a price input, so a file the model calls 60% must close about 60% of the time. Measure the business result as recovery fee earned per attempt-hour on accepted files versus a baseline acceptance rule.
**Scope:** A modest tabular model; the work is joining assignment exports with the agency's attempt log and closing outcomes. 1 data scientist, 3 months for one agency, longer for a pooled model. A logistic baseline with a handful of features will capture most of the signal.
**Data availability:** Each agency holds its own assignment history and outcomes; forwarders and RDN hold far more but under client agreements. Labels are clean: the file closed recovered or it did not.

---

## 4. Condition Reports and Property Inventories from Photos
#large-language-models #transformers #object-detection #cnns #compliance #automation

**Problem statement:** Turn the photos a lot clerk takes of a recovered car into a structured condition report and a draft personal property inventory, flag regulated items, and generate the state-required notice to the debtor inside the state's clock.

**ML task:** Exterior damage detection and localisation; interior item detection and classification; multimodal language-model drafting of the inventory and notice from detected items, file data and state rules
**Input data:** Walk-around and interior photos; recovery method (wheel-lift, flatbed, keys); assignment and borrower address; state rule tables (notice timing, storage period, release conditions); client templates.
**Target:** Damage list by panel with severity; item list with category and special-handling flag (firearm, medication, cash, documents); notice letter populated and dated.
**Evaluation metric:** Recall on property items is the binding metric — an item missing from the inventory becomes a complaint — with precision secondary. For damage, recall on pre-existing damage visible before the hook. Track the share of notices sent inside the state deadline.
**Scope:** Off-the-shelf multimodal models already describe photos well; the work is the state rule tables, the regulated-item list and the review step. 1 ML engineer and 1 engineer with a compliance adviser, 3–4 months.
**Data availability:** Agencies and RDN's property module hold photos and past inventories; labels exist wherever clerks typed inventories against photos. State rules must be compiled and maintained by hand.

---

## 5. Camera Route Planning by Hot-List Density
#time-series-forecasting #gaussian-processes #markov-decision-processes #optimization-fundamentals #worker-facing #revenue-impact

**Problem statement:** Camera drivers choose which lots and streets to scan, and at what hours, by habit. Forecast where and when open assignments' vehicles are likely to be scannable, and plan each shift's route to maximise expected confirmed hits per hour.

**ML task:** Spatio-temporal forecasting of hit intensity by area and hour; sequential route planning under uncertainty that updates as hits arrive
**Input data:** Open assignment addresses and vehicle types; the agency's historical scans and hits by location and hour; parking-lot geometry and access; day of week, weather and pay-cycle timing.
**Target:** Expected confirmed hits per area-hour; a route.
**Evaluation metric:** Confirmed hits and recoveries per driving hour against drivers' own routes in an A/B or switchback test, with fuel cost netted. Watch for concentration: a planner that sends every driver to the same dense lots overstates its gain.
**Scope:** Forecasting is tractable with an agency's own scan history; route planning can start as a greedy coverage heuristic before any learned policy. 1 data scientist and 1 engineer, 4 months.
**Data availability:** Agencies see their own scans and hits through the camera vendor's app; the full scan history of every plate belongs to the camera network, which could build a far better version and has not exposed it to agencies.
