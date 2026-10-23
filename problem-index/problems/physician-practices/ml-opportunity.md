# Machine Learning Opportunities — Physician Practices

**Industry:** [[physician-practices|Physician Practices]]
**Derived from:** [[problems/physician-practices/high-impact|High Impact]], [[problems/physician-practices/low-impact-1|Low Impact 1]], [[problems/physician-practices/low-impact-2|Low Impact 2]], [[problems/physician-practices/worker-life-1|Worker Life 1]], [[problems/physician-practices/worker-life-2|Worker Life 2]]

---

## 1. Learning the Physician's Sense of Alarm From the Visit Record
#tacit-knowledge-ml #gradient-boosting #transformers #survival-analysis #causal-inference #evaluation-metrics #worker-facing

**Problem statement:** Experienced primary care physicians detect that a routine-looking patient is seriously ill and show it only through behaviour: an urgent order, a shortened recheck, red-flag language in the conversation. The ML problem is to learn that signal, joined to outcomes that occur outside the practice, and predict which visits precede a serious event early enough to change the visit.

**ML task:** Visit-level time-to-event prediction (discrete-time survival over 14-day and 12-month horizons) with calibrated risk tiers, plus attribution of each flag to its history, utilisation and transcript drivers
**Input data:** Structured EHR history (problem list, medications, lab trends, vitals), utilisation (visit counts for the same complaint, recent emergency visits), the physician's own behaviour at the visit (orders placed, urgency flags, recheck interval against the practice norm, visit length), ambient transcript features (hedged and red-flag phrases, safety-netting instructions), and outcome feeds from claims, health information exchange admit/discharge alerts and cancer registries
**Target:** Composite serious event (unplanned emergency visit or admission within 14 days; new diagnosis of cancer, stroke, myocardial infarction or sepsis within 12 months after a related presenting complaint)
**Evaluation metric:** Recall on events the treating physician did not escalate, at a fixed flag rate the group agrees to (for example under 3% of visits). Report lead time gained over the physician's own escalation, precision at that rate, and calibration by clinic and payer. AUROC alone is misleading because events are rare (~1% of visits, estimate). Costs are asymmetric: a missed cancer is years of life, while a false flag costs minutes and, cumulatively, trust.
**Scope:** The data-collection challenge comes first. The expert's alarm is never charted as a judgement, so the model must infer it from orders, intervals and transcript language, and outcomes must be linked from claims and HIE feeds the practice rarely sees. A value-based group with claims access is the natural first site. The labelling challenge is that escalation prevents the outcome that would label it. Escalated patients who did well look like false positives, so evaluation compares escalated and non-escalated patients with similar early trajectories, and a sample of non-events gets chart review. Physicians also disagree with themselves across days and after recent misses. The deployment challenge is speed. The flag must appear in the pre-visit summary or during the visit, with a reason, and stay silent on the easy cases. Team: 2 ML engineers, a primary care physician lead and a data engineer for claims linkage. Expect 9–12 months to a validated silent run in one 20–50 physician group, then a stepped rollout by clinic.
**Data availability:** EHR data and ambient transcripts sit with the practice under HIPAA. Outcome linkage needs claims (ACO or MA risk contracts provide it) or HIE alerts. MIMIC-IV covers hospital care only. A demo can be built on Synthea synthetic patients with injected delayed-diagnosis trajectories, which shows the pipeline but not real signal.

---

## 2. Prior Authorization Requirement, Approval and Packet Assembly
#large-language-models #transformers #gradient-boosting #evaluation-metrics #automation #revenue-impact

**Problem statement:** For each order, predict whether the patient's plan requires authorization and whether a request with the current chart evidence would be approved. Then assemble the packet: the payer's criteria for that code, each matched to cited evidence in the chart, with gaps flagged before submission.

**ML task:** Binary classification of authorization required and of approval likelihood, plus retrieval-augmented extraction that maps policy criteria to chart passages and generates the submission
**Input data:** Order (CPT/HCPCS, ICD-10, site of service, ordering specialty), payer, plan and product; payer medical policy PDFs and radiology benefit manager guidelines (published on payer websites); chart notes, imaging and lab reports, medication history; the practice's past requests with outcomes, denial reasons and peer-to-peer results; CMS-0057-F denial reasons from 2026
**Target:** Required (yes/no); approved on first submission (yes/no, with reason class); a criterion-by-criterion evidence table and draft letter accepted with light edits
**Evaluation metric:** Precision on "not required", since a wrong answer creates a technical denial that rarely overturns. Calibration of approval probability. For packets, criterion-level extraction F1 against a staff-built gold set, the share of packets sent with light edits, and first-pass approval rate against staff-built packets in a randomised holdout.
**Scope:** 2 engineers and a prior-authorization lead from a specialty practice, 4–6 months for one specialty's top ten codes and top five payers. The policy-parsing layer is reusable across practices, while outcome models are practice-specific. Policy versions change, so each criterion needs an effective date.
**Data availability:** Public payer policies and synthetic patients make a credible two-week demo: Synthea records (FHIR, Apache-2.0) plus five payers' policies for knee MRI or a biologic. Real outcomes need a practice or vendor partner under a BAA.

---

## 3. E/M Level and Risk-Adjustment Support From the Ambient Note
#bert #large-language-models #logistic-regression #evaluation-metrics #compliance #revenue-impact

**Problem statement:** From the visit transcript and note, predict the office E/M level the documentation supports under the 2021 medical-decision-making rules, and identify chronic conditions assessed in the visit but missing from the claim or documented too weakly to survive a risk-adjustment audit.

**ML task:** Multi-class classification of E/M level (99212–99215, plus the G2211 add-on), multi-label extraction of MDM elements (problems, data, risk) and of HCC-relevant diagnoses with MEAT evidence spans
**Input data:** Ambient transcripts, signed notes, problem lists, orders, prior-year diagnoses, final claims, coder audit results and payer or RADV audit outcomes
**Target:** Supported E/M level with MDM element rationale; list of supported and unsupported HCC diagnoses with evidence
**Evaluation metric:** Agreement with certified coders on a blinded sample (weighted kappa), and the share of model-suggested levels and HCCs that survive audit. Over-coding costs more than under-coding, because an audit takeback carries penalties and extrapolation.
**Scope:** 2 ML engineers and a certified coder, 4–6 months. Ambient vendors already ship coding suggestions, so the defensible edge is audit-outcome learning. The model must also refuse to suggest a level the transcript does not support.
**Data availability:** Practice-owned under HIPAA. Coder audits exist in most groups, while payer audit outcomes are scattered. Public data: CMS E/M guidelines and synthetic transcripts.

---

## 4. No-Show Prediction and Template Overbooking
#gradient-boosting #optimization-fundamentals #monte-carlo-methods #evaluation-metrics #revenue-impact #quick-win

**Problem statement:** Predict each booked appointment's probability of a no-show or late cancellation, and set overbooking and reminder intensity per template slot so the schedule is full without overrunning the day.

**ML task:** Binary classification per appointment, calibrated, feeding a stochastic scheduling optimisation evaluated by Monte Carlo replay of past clinic days
**Input data:** Appointment history (lead time, visit type, day and hour, prior no-shows, confirmations, reminder responses), patient distance and payer, weather, provider
**Target:** No-show or same-day cancellation (yes/no); recommended overbook level per slot; expected overtime minutes
**Evaluation metric:** Calibration and AUROC for no-shows. For the schedule, kept visits per session and overtime minutes against the current template in replay. Overbooking a patient who arrives costs a long wait, so overtime is penalised.
**Scope:** 1 data scientist, 2–3 months to a model, longer to win the physicians' agreement on overbooking. Fairness review is needed, because no-show features correlate with income and race.
**Data availability:** Every PM system holds years of appointments. Public Kaggle no-show datasets support a demo.

---

## 5. Referral Routing and Leakage Prediction
#graph-neural-networks #survival-analysis #gradient-boosting #data-integration #revenue-impact

**Problem statement:** For each outbound referral from a primary care group, predict whether it will be completed, where the patient will actually go, and how long it will take. For each inbound referral to a specialty group, predict whether it converts to a kept first visit.

**ML task:** Link prediction on a referral graph (patients, physicians, practices, payers), plus time-to-completion survival modelling
**Input data:** Referral orders and faxed packets, scheduling outcomes, claims showing where specialty care occurred, network and payer rules, distance and wait times
**Target:** Completed within 30/60/90 days (yes/no); destination practice; time to completion
**Evaluation metric:** Concordance for time to completion; top-k accuracy for destination; recall on referrals that will lapse, since a lapsed cardiology or oncology referral is a safety event, not just lost revenue.
**Scope:** 2 data scientists, 4–6 months. Claims are needed to see completions outside the network, which suits ACOs and health-system groups. Tennr and similar vendors own the intake side.
**Data availability:** Referral orders and scheduling data are practice-owned. Out-of-network completions need claims under a value-based contract. A demo can use CMS's public physician shared-patient data with synthetic referrals.
