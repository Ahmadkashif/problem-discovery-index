# Machine Learning Opportunities — IDD Group Homes

**Industry:** [[idd-group-homes|IDD Group Homes]]
**Derived from:** [[problems/idd-group-homes/high-impact|High Impact]], [[problems/idd-group-homes/low-impact-1|Low Impact 1]], [[problems/idd-group-homes/low-impact-2|Low Impact 2]], [[problems/idd-group-homes/worker-life-1|Worker Life 1]], [[problems/idd-group-homes/worker-life-2|Worker Life 2]]

---

## 1. Per-Person Precursor Models for Behavioural Crises and Fatal Five Decline
#tacit-knowledge-ml #survival-analysis #hidden-markov-models #bayesian-inference #transformers #evaluation-metrics #worker-facing

**Problem statement:** Long-tenured DSPs recognise, in residents who cannot report symptoms, the pattern that comes before an assault, self-injury, aspiration, bowel obstruction, seizure cluster or sepsis. The ML problem is to learn each resident's precursor signature from brief staff observations and handover worry ratings, then warn the DSP on shift early enough to act.

**ML task:** Per-person time-to-event modelling with partial pooling across residents (hierarchical survival or a hidden-state model over the observation stream), plus language-model extraction of observation codes from free-text and spoken shift reports
**Input data:** Timestamped DSP observation logs (voice or tap: "pacing", "refused fluids", "coughing at meals"); shift-handover worry ratings per resident; behaviour data (ABC sheets); bowel, fluid, sleep and seizure logs; MAR and PRN administrations; medication changes; staffing roster per shift (who worked, how long they had known the resident); calendar disruptions (home visits, day programme closures).
**Target:** Hazard of a behavioural crisis (restraint, injury, police or crisis call) within 2–12 hours; hazard of an ER visit or admission for aspiration, dehydration, constipation or obstruction, seizure or sepsis within 72 hours.
**Evaluation metric:** Recall of events at a fixed alert budget per house per week, because alert fatigue kills adoption; median lead time between the first alert and the event; calibration per resident. Missing a crisis costs far more than a false alert, but a house that gets more than a few alerts a week will mute them, so the budget is a hard constraint. Compare against the experienced DSPs' own handover worry scores as the human baseline, and report how often the model fires when the worry score did not.
**Scope:** Collection is the hardest part and comes first. The expert's read has to be captured while she works, so the capture surface must replace paperwork: observation logs that draft the shift note, bowel and fluid records automatically. Labelling suffers from intervention bias, because precursors an experienced DSP defused leave no outcome, and from intra-rater drift in worry scores. Collect repeated ratings on a sample to estimate reliability, and have clinicians adjudicate outcome windows. Deployment must be faster than the DSP's own recall: a phone prompt naming the person's own history and the next step in the plan, never a dashboard. Plan on 2 ML engineers, a clinical lead (nurse or behaviour analyst) and an embedded implementation lead with one agency, 9–12 months. Value appears first as retrieval ("the last three times he paced and refused lunch"), before any hazard model is trusted.
**Data availability:** Outcomes (incidents, ER visits, admissions) already exist in agency incident systems and claims. Structured observation does not. It must be built prospectively over 6–12 months in pilot houses, and historical shift notes give only weak, after-the-fact labels. Records are protected health information held by the agency under its EHR vendor's business associate agreement.

---

## 2. ISP-Outcome Mapping and Audit-Risk Scoring for Shift Notes
#transformers #bert #large-language-models #gradient-boosting #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Classify each shift note by which individual service plan outcomes and support strategies it documents, and score each billed residential day for the probability that a state reviewer would find it unsupported.

**ML task:** Multi-label classification of note passages against the person's ISP outcomes (retrieval over the plan, then classification), plus a calibrated day-level audit-failure probability
**Input data:** Shift notes and DSP narratives; each resident's ISP outcomes and support strategies; attendance and leave records; the state's documentation standard; historical audit and review findings with day-level outcomes (supported, unsupported, recouped).
**Target:** Outcome labels per note passage; day-level supported/unsupported; reason codes (no outcome addressed, attendance mismatch, non-observable language).
**Evaluation metric:** Recall on days a reviewer would reject, measured on held-out audit samples; precision kept high enough that house managers do not chase false flags. Asymmetric: an unflagged bad day is recouped with possible extrapolation, while a false flag costs a few minutes of review.
**Scope:** A retrieval-plus-classification system tuned per state standard. 1 ML engineer and 1 billing compliance lead, 4–5 months for one state; each further state needs its rules encoded and a few hundred labelled audit days.
**Data availability:** Notes and ISPs sit in the agency's record system. Audit findings sit in the agency's compliance files and are often unstructured letters; the provider's own past reviews are the labels.

---

## 3. Critical Incident Classification and Unreported-Incident Detection
#bert #transformers #logistic-regression #feature-engineering #evaluation-metrics #compliance #data-integration

**Problem statement:** Classify incident narratives against the state's critical incident definitions and deadlines, and find incidents that should have been reported but were not, by linking emergency visits, injuries and PRN use to the incident log. Under the Access Rule, states must use claims and other data to find unreported incidents.

**ML task:** Multi-class classification of narratives (abuse, neglect, exploitation, restrictive intervention misuse, medication error at threshold, unexplained death, non-critical); record linkage between claims or ER notifications and incident reports, with a classifier for "should have been reported"
**Input data:** Incident narratives and categories; state definitions and timeframes; Medicaid claims or provider-held ER and hospital notifications; injury reports; PRN and restraint logs; investigation outcomes.
**Target:** Critical incident category and reporting deadline per narrative; unmatched ER visits or injuries likely to be unreported critical incidents.
**Evaluation metric:** Recall on true critical incidents and on unreported incidents confirmed by investigators. An OIG series of state audits found up to 99% of such incidents unreported (OIG group homes page), so recall dominates. Precision is reported as investigator hours per confirmed find.
**Scope:** A provider-side version (classify and route their own reports) is a 3–4 month build for 1 engineer with a compliance lead. A state-side version (claims linkage across all providers) is a state contract with a longer data-access path.
**Data availability:** Providers hold their incidents and ER notifications. States hold claims, MFCU and protective services data. The provider and state versions are separate products because the data sits in different hands.

---

## 4. Early-Tenure DSP Attrition and Call-Off Forecasting
#survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #worker-facing #workflow-orchestration

**Problem statement:** Predict which new DSPs are at risk of leaving in their first year and which shifts are likely to go uncovered, so the agency can intervene before mandating overtime.

**ML task:** Survival analysis of DSP tenure with time-varying covariates; shift-level call-off probability forecasting
**Input data:** HR and payroll records (hire date, wage, hours, overtime, mandated shifts), schedule and timeclock history, house assignment and resident support levels, training completion dates, supervisor, commute distance, incidents involving the DSP.
**Target:** Hazard of separation by week of tenure; probability that each scheduled shift is called off or no-showed.
**Evaluation metric:** Concordance index and calibration for separation risk; Brier score and coverage of call-offs at a fixed standby budget. A missed call-off produces a forced double; a false one costs a paid standby shift.
**Scope:** 1 data scientist with HR and scheduling exports, 3 months to a first model. The hard part is acting on the output fairly: risk scores must steer support (a mentor, a schedule change), never discipline.
**Data availability:** Agencies hold all of it in payroll, HR and scheduling systems, usually in three vendors' exports needing a join. NCI's State of the Workforce survey gives state benchmarks (37% average turnover, 64% of leavers under a year, 2024), not individual records.

---

## 5. Support-Need Drift Detection for Rate-Tier Reassessment
#gradient-boosting #logistic-regression #change-point-detection #large-language-models #evaluation-metrics #revenue-impact

**Problem statement:** Residential rates are tiered by each person's assessed support needs, often from a standardised assessment repeated every few years (estimate). Residents who age, develop dementia or acquire new medical needs drift above their funded tier long before reassessment. Detect drift from day-to-day records so the agency requests reassessment with evidence.

**ML task:** Ordinal classification of current support need from records, with change-point detection over time against the funded tier
**Input data:** Shift notes, staffing actually provided (one-to-one hours, overnight awake staff), incidents, falls, health events, medication changes, the last assessment's item scores and tier.
**Target:** Estimated current tier; probability that need exceeds the funded tier; the evidence passages supporting it.
**Evaluation metric:** Agreement with the next formal reassessment (weighted kappa), and the share of flagged residents whose reassessment raised the tier. Precision matters, because states scrutinise providers who request too many reassessments.
**Scope:** 1 data scientist and 1 clinical reviewer, 4 months per state assessment instrument. It overlaps with ageing residents with dementia, the fastest-drifting group.
**Data availability:** Agencies hold the records and the assessment results they received. Item-level assessment data may sit with the state or its assessment contractor.
