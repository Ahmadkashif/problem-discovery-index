# Machine Learning Opportunities — Home Health Agencies

**Industry:** [[home-health-agencies|Home Health Agencies]]
**Derived from:** [[problems/home-health-agencies/high-impact|High Impact]], [[problems/home-health-agencies/low-impact-1|Low Impact 1]], [[problems/home-health-agencies/low-impact-2|Low Impact 2]], [[problems/home-health-agencies/worker-life-1|Worker Life 1]], [[problems/home-health-agencies/worker-life-2|Worker Life 2]]

---

## 1. Visit Schedule Optimization with Real-Time Rerouting
#ml-optimization #revenue-impact

**Problem statement:** Given a daily patient census (locations, visit windows, acuity, payer-mandated frequencies), clinician roster (certifications, availability, home base location), and real-time disruptions (cancellations, call-outs), produce and continuously optimize visit schedules that minimize drive time while satisfying all clinical and regulatory constraints.

**ML task:** Constrained optimization (vehicle routing problem variant) with online re-optimization
**Input data:** Patient addresses + visit requirements, clinician profiles + home locations, historical visit durations by patient acuity, real-time cancellation/call-out events
**Target:** Minimized total drive time subject to: visit window constraints, clinician-certification matching, continuity-of-care preferences, Medicare visit frequency rules
**Evaluation metric:** Total clinician drive minutes per day; constraint violation rate (must be 0%); patient continuity score
**Scope:** The VRP formulation is well-studied. The home health twist (clinical constraints, real-time disruption) makes it a medium-scoped project. A heuristic solver (OR-Tools, OptaPlanner) with learned visit duration predictions is a solid v1. 10-14 week project.
**Data availability:** Agencies have full scheduling history with addresses, timestamps, and clinician assignments. GPS data from EVV systems provides actual drive times.

---

## 2. OASIS Answer Pre-Population from Clinical Notes
#ml-nlp #worker-facing #quick-win

**Problem statement:** Given a patient's recent visit notes, medication list, prior OASIS assessments, and hospital discharge summary, pre-populate as many OASIS fields as possible — reducing the clinician's assessment from 100+ questions to only those requiring fresh bedside observation.

**ML task:** Information extraction + form auto-fill
**Input data:** Prior OASIS submissions (structured), recent clinical visit notes (unstructured), medication lists (structured), discharge summaries (semi-structured)
**Target:** Pre-filled OASIS field values with confidence scores; fields below confidence threshold flagged for clinician review
**Evaluation metric:** Auto-fill accuracy per field (must exceed 95% for fields marked as "confident"); clinician override rate
**Scope:** Quick win for structured-to-structured fields (prior OASIS → current OASIS with change detection). NLP extraction from visit notes for clinical status fields is the harder piece. Start with the 40-50 OASIS fields that can be reliably pre-filled from structured data alone. 6-8 week project for v1.
**Data availability:** Agencies have years of completed OASIS submissions paired with corresponding visit notes. Direct training data.

---

## 3. Patient Hospitalization Risk Prediction
#ml-classification #quick-win #revenue-impact

**Problem statement:** Given a home health patient's clinical trajectory (visit notes, vital signs, OASIS functional scores, medication changes), predict the probability of hospitalization in the next 14 days so that the agency can intervene proactively.

**ML task:** Binary classification with temporal features
**Input data:** OASIS scores over time, visit note features (extracted or structured), vital sign trends, medication change events, diagnosis complexity
**Target:** Binary: hospitalized within 14 days (yes/no)
**Evaluation metric:** AUROC; calibration (predicted probabilities should be reliable); recall at 80%+ specificity
**Scope:** This is a well-scoped ML problem with clear signal. Hospital readmission prediction in home health has published benchmarks. A gradient-boosted model on structured OASIS + claims features is a proven approach. 4-6 week project with access to 1,000+ patient episodes with hospitalization labels.
**Data availability:** Agencies track hospitalizations (it's a reportable quality metric). OASIS data + visit history provides the feature set. Claims data provides hospitalization labels.

---

## 4. EVV Discrepancy Auto-Resolution
#ml-classification #automation #quick-win

**Problem statement:** Given a set of EVV records, clinical visit notes, and payroll entries for the same visit, classify discrepancies as: legitimate (normal variance), data entry error (auto-correctable), or true exception (requires human review).

**ML task:** Multi-class classification
**Input data:** EVV timestamp + GPS, visit note completion timestamp, payroll time entry, historical discrepancy resolutions
**Target:** Discrepancy class: legitimate_variance | auto_correctable | human_review_needed
**Evaluation metric:** Accuracy; false auto-correction rate < 1% (errors in auto-correction cause payroll and billing problems)
**Scope:** Genuine quick win. The training data is the historical reconciliation decisions already made by billing coordinators. A decision tree or logistic regression on time-gap features, GPS distance, and visit type is sufficient. 3-4 week project.
**Data availability:** Any agency doing manual reconciliation has implicit labeled data — every reconciliation decision is a training example.

---

## 5. Referral-to-Admission Conversion Prediction
#ml-classification #revenue-impact

**Problem statement:** Given a hospital discharge referral's attributes (diagnosis, payer, referring hospital, patient demographics, referral completeness), predict the probability that the referral will convert to an admitted patient — allowing the agency to prioritize high-conversion referrals and allocate intake resources accordingly.

**ML task:** Binary classification
**Input data:** Referral attributes (diagnosis codes, payer, referring facility, patient demographics), referral document completeness score, historical conversion outcomes
**Target:** Binary: referral converts to admission (yes/no)
**Evaluation metric:** AUROC; precision at recall > 0.8
**Scope:** Small-scoped project. Agencies receive referrals and track which ones convert. A logistic regression on referral features is a strong baseline. 3-4 week project with 500+ referral records.
**Data availability:** Agencies maintain referral logs with outcomes. The data is immediately available.
