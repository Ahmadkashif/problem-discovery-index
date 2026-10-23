# Machine Learning Opportunities — General Hospitals

**Industry:** [[general-hospitals|General Hospitals]]
**Derived from:** [[problems/general-hospitals/high-impact|High Impact]], [[problems/general-hospitals/low-impact-1|Low Impact 1]], [[problems/general-hospitals/low-impact-2|Low Impact 2]], [[problems/general-hospitals/worker-life-1|Worker Life 1]], [[problems/general-hospitals/worker-life-2|Worker Life 2]]

---

## 1. Reading Nurse Concern From the Documentation Trail
#tacit-knowledge-ml #gradient-boosting #survival-analysis #lstms-and-grus #evaluation-metrics #feature-engineering #worker-facing

**Problem statement:** Experienced ward nurses detect deterioration before vital signs change and show it by checking more often, charting more and escalating, a judgement they cannot specify and that leaves with them. The ML problem is to learn that signal from documentation behaviour plus physiology, and predict rapid response activation, unplanned ICU transfer, sepsis onset or death early enough, and precisely enough, to add to the nurse's own read rather than repeat it.

**ML task:** Hourly time-to-event prediction (discrete-time survival over 12- and 24-hour horizons) with calibrated risk tiers, plus attribution of each alert to its documentation and physiological drivers
**Input data:** EHR flowsheet metadata (assessment and vitals timestamps against ordered frequency, off-schedule entries, row counts per hour), nursing note text and timing, PRN administrations and holds, rapid response and physician page logs, vitals, labs, medication administration record, unit, shift and nurse-tenure fields; public research sets (MIMIC-IV, eICU, the restricted CONCERN dataset on PhysioNet) for pretraining
**Target:** Composite deterioration event (rapid response call, unplanned ICU transfer, cardiac arrest, death) and sepsis onset under a stated definition, at 12 and 24 hours
**Evaluation metric:** Lead time gained over the nurse's own first escalation, at a fixed alert rate the unit agrees to (for example no more than 5% of patients flagged per shift). Report precision at that rate and calibration by unit, alongside AUROC. Recall on deteriorations that the nurses did not escalate matters most, since those are the cases the model can add. Compare against the Epic Sepsis Model's external benchmark (AUC 0.63, 33% sensitivity, alerts on 18% of hospitalisations). Asymmetric costs: a missed deterioration can be a death, while an extra alert costs minutes and, cumulatively, trust.
**Scope:** The data-collection challenge comes first. The expert's read is never charted as a judgement, so the model infers it from behaviour, which differs by unit, EHR build and staffing level. Features must be normalised against what each unit's flowsheets require, or the model learns policy rather than concern. The labelling challenge is that the expert's action prevents the outcome that would label it. Escalated patients who were rescued look like false positives, so evaluation needs counterfactual care: compare escalated and non-escalated patients with similar early trajectories, and audit a sample of non-events by chart review. Nurses also disagree with themselves across shifts and after recent bad outcomes. The deployment challenge is precision and workflow: a badge on the patient list, validated on the hospital's own population before go-live, with a "why", and quiet enough not to deskill new nurses. Team: 2 ML engineers, 1 clinical informatics nurse and a hospitalist lead, 9–12 months to a validated silent run at one hospital, then a stepped-wedge rollout by unit. The CONCERN trial (35.6% lower mortality risk across ~60,000 patients) shows the signal is real.
**Data availability:** Every hospital has the flowsheet audit trail inside its EHR, but extracting timestamps at row level needs EHR-analyst time and a data use agreement or BAA. MIMIC-IV and eICU are free with credentialing; the CONCERN dataset is restricted access. Outcome labels (rapid response, ICU transfer, death) are structured. Sepsis labels must be computed.

---

## 2. Clinical Denial Prediction and Appeal Win Modelling
#gradient-boosting #large-language-models #bert #logistic-regression #evaluation-metrics #revenue-impact #workflow-orchestration

**Problem statement:** Predict, before the claim drops, which inpatient claims a given payer will deny on medical necessity, inpatient status or DRG validation. For denials received, predict which appeals will win at which level, and draft the appeal from the chart, the payer's policy and the contract.

**ML task:** Binary classification of denial risk per claim and payer, plus appeal-outcome classification per denial and level, plus retrieval-augmented generation of appeal letters with cited chart evidence
**Input data:** 837I claims and 835 remittances with CARC/RARC codes; denial letters (PDF or portal text); payer medical policies and contract clauses; chart documents (H&P, progress notes, discharge summary, labs); prior appeals with outcomes and levels; MCG or InterQual criteria met at admission
**Target:** Denied (yes/no, with reason class) per claim; overturned (yes/no) per appeal and level; a draft letter accepted with minimal edits
**Evaluation metric:** AUROC and precision at the top decile for denial risk, where the action is pre-bill review. For appeals, expected recovered dollars per reviewer hour, comparing model-prioritised worklists against arrival order. For letters, the share sent with only light edits and the overturn rate against human-written letters in a randomised holdout. A missed high-dollar denial costs more than a needless pre-bill review.
**Scope:** The labels exist but are scattered. Remittances carry the denial; appeal outcomes sit in denial-management tools or spreadsheets; contracts are PDFs. 2 ML engineers, 1 denial-management nurse and a revenue integrity analyst, 6 months for one hospital's top five payers. The models drift as payers change behaviour, so monitoring per payer is part of the product.
**Data availability:** Hospital-owned and PHI under the hospital's control; vendors work under BAAs. Public demo data: synthetic claims (Synthea), CMS medical policies and LCDs, and payer policy PDFs published on payer websites.

---

## 3. Surgical Case-Duration Distributions and Block Release Forecasting
#bayesian-inference #gradient-boosting #monte-carlo-methods #optimization-fundamentals #evaluation-metrics #revenue-impact

**Problem statement:** Predict the full distribution of each booked case's duration from surgeon, procedure combination, patient and team features. Forecast which blocks will go unused far enough ahead to release and back-fill them.

**ML task:** Quantile or hierarchical Bayesian regression of case duration (log-normal with surgeon and procedure random effects), plus classification of block under-utilisation two to three weeks out, plus simulation-based schedule evaluation
**Input data:** OR case logs (wheels-in/out, incision/close, turnover), scheduled versus actual durations, CPT combinations, surgeon, anaesthesia type, patient BMI, ASA class and age, first-case flags, team composition; block schedules and release histories; add-on and waitlist queues
**Target:** P20/P50/P80 case duration in minutes; probability a block will be under 70% utilised; recommended release date
**Evaluation metric:** Mean absolute error and calibration of the P80 against the scheduler's current estimate, measured on overtime minutes and same-day cancellations rather than error alone. For blocks, precision at the release threshold, since releasing time a surgeon would have used is politically costly.
**Scope:** Well-posed and data-rich; the hard part is adoption and block politics. 1–2 data scientists, 3–4 months to a model, plus months of OR committee work to change booking policy. Simulation (Monte Carlo replay of past days) is how the committee is convinced.
**Data availability:** Every hospital's OR system holds years of timestamped cases. Public datasets are thin, so demos use synthetic case logs.

---

## 4. Next-Day Discharge and Unit Census Forecasting
#time-series-forecasting #temporal-fusion-transformers #gradient-boosting #recurrent-forecasting #evaluation-metrics #workflow-orchestration

**Problem statement:** Predict each inpatient's probability of discharge tomorrow and its barrier (medical readiness, post-acute placement, payer authorisation, transport). Roll the predictions up into unit-level census forecasts for the next 24–72 hours, for staffing and bed placement.

**ML task:** Patient-level binary classification of next-day discharge with barrier attribution, aggregated with a multi-horizon time-series model of admissions, transfers and census by unit
**Input data:** ADT events, orders (discharge order, therapy, imaging), case-management notes, post-acute referral status (CarePort/Aidin events), MA authorisation status, ED boarding queue, scheduled surgical admissions, day of week and season
**Target:** Discharged within 24 hours (yes/no) with barrier class; census by unit at 7 a.m. and 3 p.m. for the next three days
**Evaluation metric:** AUROC and calibration for discharge; mean absolute error in beds by unit for census, compared with the charge nurse's own forecast at the morning huddle. Under-forecasting census is costlier than over-forecasting, because it leads to unsafe ratios or agency call-ins.
**Scope:** 2 data scientists, 4–6 months. The barrier attribution is what case managers act on, and the census forecast is what the staffing office buys. Qventus and LeanTaaS iQueue sell versions of this, so a newcomer differentiates on barrier precision and post-acute integration.
**Data availability:** All in the EHR and referral platforms under BAA. Public demos can use MIMIC-IV ADT tables.

---

## 5. Concurrent CDI Query Prioritisation and Autonomous Inpatient Coding
#transformers #bert #large-language-models #evaluation-metrics #compliance #revenue-impact #automation

**Problem statement:** While the patient is still in the hospital, find the records where documentation does not support the true severity: an unstated CC/MCC, an unspecified diagnosis or a missing linkage. Prioritise those for a compliant CDI query. After discharge, assign ICD-10-CM/PCS codes and the MS-DRG automatically for the cases a model can code with confidence.

**ML task:** Multi-label classification of clinical documentation against ICD-10 codes and CC/MCC flags; ranking of open records by expected DRG impact; extraction with evidence spans for auditability
**Input data:** Physician progress notes, H&P, discharge summaries, labs, medications, vitals, radiology reports; final coded abstracts and DRGs; CDI query history with physician responses; payer DRG-validation audit outcomes
**Target:** Code set and DRG per discharge; query opportunity per open record with expected DRG shift; auto-code confidence
**Evaluation metric:** DRG-level agreement with expert coders on a blinded sample, reported at the auto-code threshold. Query precision (the share of queries that physicians agree with) and audit defensibility (the share of DRG shifts that survive payer review) matter more than raw recall. A leading or unsupported query is a compliance risk, and an upcoded DRG that a payer reverses costs more than the missed shift.
**Scope:** Mature competition (AKASA, Solventum, Iodine, Fathom, CodaMetrix, SmarterDx), so value lies in payer-audit outcome learning and evidence quality. 3 ML engineers and 2 coding/CDI experts, 6–9 months to production quality on a hospital's own data.
**Data availability:** Coded abstracts and notes are in every hospital's HIM system under HIPAA. MIMIC-IV notes with ICD codes are the public benchmark. Payer audit outcomes are scattered across denial tools.
