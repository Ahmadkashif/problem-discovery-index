# Machine Learning Opportunities — Physical Therapy

**Industry:** [[physical-therapy|Physical Therapy]]
**Derived from:** [[problems/physical-therapy/high-impact|High Impact]], [[problems/physical-therapy/low-impact-1|Low Impact 1]], [[problems/physical-therapy/low-impact-2|Low Impact 2]], [[problems/physical-therapy/worker-life-1|Worker Life 1]], [[problems/physical-therapy/worker-life-2|Worker Life 2]]

---

## 1. Authorization Denial Risk Prediction
#ml-classification #revenue-impact #quick-win

**Problem statement:** Given a concurrent review request's attributes (payer, diagnosis, visits completed, functional progress, documentation quality), predict the probability of denial — allowing clinics to strengthen weak requests before submission and prioritize high-risk cases for extra documentation.

**ML task:** Binary classification
**Input data:** Authorization request features (payer, plan type, diagnosis codes, visits used, functional outcome change scores, key documentation phrases present/absent), historical authorization outcomes
**Target:** Binary: authorization_denied (yes/no); secondary: denial_reason prediction (multi-class)
**Evaluation metric:** AUROC; recall at 80%+ precision (catch denials before they happen)
**Scope:** Genuine quick win. Clinics process dozens of authorization requests weekly and have historical outcomes. A gradient-boosted model on structured features (payer + visit count + outcome score change) is a strong baseline. 3-4 week project.
**Data availability:** Any PT clinic tracks authorization submissions and outcomes. 500+ historical requests with outcomes is sufficient for a payer-specific model.

---

## 2. Home Exercise Adherence Estimation from Functional Progress
#ml-time-series #worker-facing

**Problem statement:** Given a patient's functional outcome trajectory (scores at each visit), visit frequency, and prescribed HEP complexity, estimate likely adherence to the home exercise program — distinguishing between "treatment isn't working" and "patient isn't doing the exercises."

**ML task:** Regression (estimated adherence score) with time-series input
**Input data:** Outcome measure scores over visits, visit frequency pattern, HEP complexity (number of exercises, difficulty level), patient demographics
**Target:** Estimated adherence score (0-100%); confidence interval
**Evaluation metric:** Correlation with ground-truth adherence data (from patients using tracked HEP apps); MAE
**Scope:** Medium-scoped project. The challenge is ground truth — you need a subset of patients with actual adherence data (from an app-based HEP) to train the model, then apply it to patients without tracking. 8-10 week project with a clinic that uses a tracked HEP platform for at least some patients.
**Data availability:** Outcome scores are in the EMR. Ground-truth adherence requires a clinic using a tracking-enabled HEP platform (MedBridge, PhysiTrack).

---

## 3. Medical Necessity Language Generation
#ml-nlp #worker-facing #compliance

**Problem statement:** Given a PT's clinical documentation (objective measurements, functional assessments, interventions), generate payer-appropriate medical necessity justification language that satisfies audit requirements — eliminating the need for the PT to manually craft compliance language.

**ML task:** Conditional text generation
**Input data:** Clinical note fields (objective findings, functional limitation scores, interventions performed, goals), payer-specific documentation requirements, patient diagnosis and treatment plan
**Target:** Generated medical necessity paragraph that satisfies the payer's documentation requirements
**Evaluation metric:** Clinician acceptance rate (approved without edits); audit pass rate on generated language; time-to-sign reduction
**Scope:** LLM with prompt engineering and payer-specific rule injection is a viable v1. Fine-tuning on a corpus of approved notes (notes that passed payer audits) produces higher-quality output. 6-8 week project for v1 with prompt engineering.
**Data availability:** Clinics have years of signed notes. Notes that were audited and approved are gold-standard training data. Notes that were denied on documentation grounds provide negative examples.

---

## 4. Outcome Measure Auto-Selection and Scheduling
#ml-recommendation #compliance #quick-win

**Problem statement:** Given a patient's diagnosis, body region, treatment plan, and payer requirements, automatically select the appropriate outcome measure(s) and schedule administration at clinically appropriate intervals.

**ML task:** Multi-label classification (which measures) + scheduling rule application
**Input data:** Patient diagnosis (ICD-10), body region, payer quality reporting requirements, treatment plan duration, historical measure usage by diagnosis
**Target:** Recommended measure set (e.g., Oswestry + NPRS for lumbar disc herniation) and administration schedule (eval, every N visits, discharge)
**Evaluation metric:** Match rate with clinician-selected measures; schedule adherence rate
**Scope:** Quick win — the mapping from diagnosis to appropriate measure is well-defined in clinical literature. A lookup table with rules covers 80% of cases; a classifier handles edge cases (multiple body regions, complex diagnoses). 2-3 week project.
**Data availability:** Clinical practice guidelines define measure-diagnosis mappings. Historical EMR data shows which measures clinicians actually used per diagnosis.

---

## 5. PTA Supervision Compliance Prediction
#ml-classification #compliance #automation

**Problem statement:** Given a PTA's caseload, scheduled visits, supervising PT's schedule, and payer-specific supervision rules, predict supervision compliance gaps 1 week in advance — flagging patients who will exceed their supervision visit threshold before the next scheduled PT visit.

**ML task:** Rule engine + scheduling simulation (more optimization than ML, but benefits from learned patterns)
**Input data:** PTA caseload with visit counts, supervising PT schedule, payer-specific supervision rules (Medicare: every 10th visit or 30 days), state-level supervision requirements
**Target:** List of patients at risk of supervision lapse in the next 7 days, with recommended PT visit slots
**Evaluation metric:** False negative rate (missed lapses) must be 0%; false positive rate < 10%
**Scope:** Quick win. The rules are deterministic — the challenge is aggregating rules across payers and states into a single monitoring system. A rules engine with scheduling simulation handles this. 3-4 week project.
**Data availability:** Visit counts, schedules, and payer information are all in the EMR. State supervision rules are published by state PT licensing boards.
