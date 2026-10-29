# Machine Learning Opportunities — Psychiatric Hospitals

**Industry:** [[psychiatric-hospitals|Psychiatric Hospitals]]
**Derived from:** [[problems/psychiatric-hospitals/high-impact|High Impact]], [[problems/psychiatric-hospitals/low-impact-1|Low Impact 1]], [[problems/psychiatric-hospitals/low-impact-2|Low Impact 2]], [[problems/psychiatric-hospitals/worker-life-1|Worker Life 1]], [[problems/psychiatric-hospitals/worker-life-2|Worker Life 2]]

---

## 1. Learning the Charge Nurse's Read of Who Will Escalate
#tacit-knowledge-ml #gradient-boosting #survival-analysis #transformers #causal-inference #evaluation-metrics #worker-facing

**Problem statement:** Experienced psychiatric charge nurses foresee which patients will need restraint or seclusion, assault someone or harm themselves in the next shift, and act on it through observation levels, room moves, early PRN medication and staff assignments, none of which is recorded as a prediction. The ML problem is to learn that read from her logged decisions and the outcomes that follow, and at each handover surface the one or two patients she has not flagged who resemble patients who later escalated.

**ML task:** Patient-shift discrete-time survival (hazard of a coercive or injurious event within 12 hours), calibrated into three tiers, with a text encoder over shift notes; uplift estimation for nursing interventions (observation level, PRN offered early, room move) from observational data
**Input data:** Legal status and hold dates, hearing dates, day of stay, diagnosis group, medication administration (scheduled doses refused, PRN use and timing), prior restraints and seclusions with times, digital 15-minute observation entries (location, behaviour, sleep), structured aggression scales where used (Brøset, DASA), nursing and technician note text, census and acuity mix, staffing grid and agency share, visits and phone calls, and the charge nurse's own one-tap worry rating and actions at handover
**Target:** Physical restraint, seclusion, emergency intramuscular medication, assault on staff or patient, or self-harm within 12 hours of handover; secondary target of the nurse's worry rating itself, to learn which of her cues the model can see
**Evaluation metric:** Recall of eventual events among patients the nurse did not flag, at a fixed alert budget of two per shift per unit, with precision and calibration reported by unit type (adult, adolescent, geriatric, detox) and by race and sex to check for biased flags. AUROC alone misleads because most shifts are quiet. Costs are asymmetric: a missed escalation can mean an injury or a restraint, while a false flag costs a closer look. A false flag must never be used to justify a restraint, and the hospital's policy has to say so.
**Scope:** The data-collection challenge comes first. Paper rounding sheets must become digital, and nurses must record worry ratings and actions at handover in seconds, or there is nothing to learn from. The labelling challenge is that the nurse's intervention prevents the event that would label it, so a patient she managed well looks like a false alarm. Uplift needs comparisons of similar patients on similar shifts, using propensity weighting or natural experiments such as a different charge nurse or staffing level. Nurses also drift after a bad night and on short-staffed weekends. The deployment challenge is that the alert must beat her own list, explain itself in nursing terms and fit on the handover screen. Team: 2 ML engineers, a clinical informaticist, a nurse lead and a privacy officer. Expect 9–12 months to a validated silent run on two units, then a stepped rollout. All demos run on synthetic records.
**Data availability:** All of it sits with the hospital under HIPAA, and detox units under 42 CFR Part 2 as well. HBIPS restraint and seclusion hours are public per facility (IPFQR) for benchmarking but not per event. Multi-facility chains (Acadia's 277 facilities, UHS's 182 US inpatient behavioral facilities) hold the largest corpora but are wary of new discoverable records after 2024's investigations. A synthetic unit simulator with scripted escalation trajectories can demonstrate the pipeline but not the signal.

---

## 2. Continued-Stay Review Packet Drafter (Two-Week MVP, Part 1)
#large-language-models #transformers #evaluation-metrics #automation #quick-win #revenue-impact

**Problem statement:** Before each concurrent review the utilization review coordinator must find, across a day's notes, the evidence for each payer criterion of psychiatric necessity. The task is to extract that evidence with citations, map it to the criteria, flag criteria with no current evidence, and draft a summary she can read to the reviewer.

**ML task:** Retrieval-augmented extraction and classification: an LLM labels note spans against a criteria schema (danger to self, danger to others, grave disability, failed less restrictive care, active medication change, legal status, discharge barriers), with span-level citations; a rules layer checks recency and payer-specific requirements; a drafting step writes the packet
**Input data:** Synthetic progress notes, nursing and technician notes, medication administration records, observation entries and social work notes for 30–50 synthetic patients over 7–14 days, written to a published criteria outline; for production, the hospital's EHR notes and each payer's licensed criteria
**Target:** For each patient-day, the criteria met with supporting spans; criteria unsupported or stale; a 200–300 word packet; in production, the reviewer's decision (days approved, peer-to-peer requested, denied)
**Evaluation metric:** Span-level recall of reviewer-annotated evidence at a fixed false-citation rate near zero (an invented citation is worse than a missed one, because the coordinator reads it aloud). Secondary: coordinator edit time per packet. In live use, the share of reviewed days denied, compared with the hospital's history by payer.
**Scope:** The two-week MVP needs one engineer and one clinician annotator. Week one: write the synthetic corpus with seeded evidence and contradictions (a 2 a.m. restraint only in the nursing note, a resolved symptom still copied forward), and build the schema and extraction. Week two: drafting, citation checking, and an evaluation on 200 annotated patient-days. Production adds EHR connectors, payer criteria under licence, Medicare recertification checks and audit logging: 2–3 engineers, 4–6 months.
**Data availability:** The MVP needs no real patient data. Real notes are hospital PHI under a BAA, and payer criteria (InterQual, MCG and payer-owned guidelines) are licensed content. The adjacent revenue cycle field is profiled at [[niches/medical-billing/denial-management-analytics-vendors/profile|🔍 Denial Management Analytics Vendors]].

---

## 3. IPFQR Peer Benchmark With Small-Facility Shrinkage (Two-Week MVP, Part 2)
#bayesian-inference #descriptive-statistics #hypothesis-testing #k-means-clustering #compliance #quick-win

**Problem statement:** CMS publishes each facility's IPFQR results, but a quality director cannot easily tell whether her restraint hours, follow-up rate or readmission rate are bad for a facility like hers, or just noisy because her unit is small. The task is a peer benchmark from the Provider Data Catalog that groups comparable facilities and reports each measure with honest uncertainty.

**ML task:** Hierarchical Bayesian estimation (beta-binomial for proportions, gamma-Poisson for restraint and seclusion hours) with peer groups formed by clustering on state, size (denominators), measure mix and, where joinable, ownership and freestanding status; percentile ranking and year-on-year change detection
**Input data:** CMS Provider Data Catalog "Inpatient Psychiatric Facility Quality Measure Data – by Facility" (1,410 facilities in the 2026 release: HBIPS-2 and -3 with numerators and denominators, SMD, TR-1, IMM-2, FAPH-7 and -30, MedCont, READM-30-IPF with confidence bounds), the state and national files, earlier releases for trend, and CMS provider-of-services files for facility type
**Target:** For each facility and measure, a shrunken estimate, a peer percentile with an interval, and a flag where the facility is credibly outside its peer range; a one-page summary for the quality director
**Evaluation metric:** Out-of-time accuracy: shrunken estimates from one release should predict the next release better than raw rates (lower mean squared error, especially for facilities with small denominators). Flags should agree with CMS's own "worse than national" readmission category where both apply.
**Scope:** One engineer, two weeks, public data only. Week one: download and clean the releases, build peer groups, fit the models. Week two: percentile intervals, change flags and the summary page. The FY2027 rule's IPF-PAI items can be added as fields when CMS publishes the specification.
**Data availability:** Fully public and free. In the 2024 data the restraint median was 0.05 hours per 1,000 patient hours against a 90th percentile of 0.63, readmission ran from 16.3% to 22.5% between the 10th and 90th percentiles, and FAPH-7 had a median of 35.5%. Facility-level ownership needs a join to other CMS files.

---

## 4. Seven-Day Follow-Up and Readmission Risk at Discharge
#logistic-regression #gradient-boosting #survival-analysis #causal-inference #revenue-impact

**Problem statement:** Only about a third of discharged patients at the median facility saw an outpatient clinician within seven days (FAPH-7 median 35.5%), and the facility median 30-day readmission rate was 19.1%. The task is to predict, at discharge planning, which patients will miss follow-up or return within 30 days, and which bridging actions (a scheduled appointment before discharge, a peer bridger, telehealth the next day, transport) change that.

**ML task:** Calibrated binary classification of no follow-up within 7 days and of readmission within 30 days; time-to-readmission survival; heterogeneous treatment-effect estimation for bridging actions
**Input data:** Diagnosis, length of stay, legal status at discharge, prior admissions, discharge medications and long-acting injectables, housing status, discharge destination, whether an appointment was booked and with whom, payer, distance to the provider, social work notes, and follow-up and readmission outcomes from claims or state health information exchange feeds
**Target:** Follow-up within 7 days (yes/no); readmission within 30 days (yes/no); days to readmission
**Evaluation metric:** Recall of non-follow-up at the number of patients the discharge team can call or bridge each week, and calibration. Recall matters more than precision, since a wasted call costs minutes and a missed patient risks a readmission or worse.
**Scope:** 1–2 data scientists, 3–4 months, at a hospital or chain that receives claims or HIE feeds. Outcomes after discharge are the hard part: many patients' follow-up is visible only in payer claims.
**Data availability:** Hospital records plus payer or HIE data under agreements. CMS's facility-level FAPH and readmission results are public for benchmarking.

---

## 5. Ligature-Risk Detection in Unit Photographs
#cnns #object-detection #semantic-segmentation #transfer-learning #compliance #automation

**Problem statement:** Joint Commission NPSG 15.01.01 requires psychiatric hospitals and units to assess their environment for features a patient could use for suicide and to mitigate them (search summary). Assessments are walked room by room with a checklist. The task is to detect potential anchor points (door hinges, handles, fixtures, exposed pipes, bed frames, furniture gaps) in photographs and rank them by the Behavioral Health Design Guide's risk levels.

**ML task:** Object detection and instance segmentation of fixture types, followed by a risk classifier that takes the fixture, the room type and the guide's level for that area
**Input data:** Photographs of patient rooms, bathrooms, corridors and day rooms taken during environmental rounds, fixture catalogues from ligature-resistant product makers, and prior assessment reports; training and demos use only consented images of empty rooms and synthetic renders, never patients
**Target:** Bounding boxes and masks for fixtures, each with a risk level and a mitigation suggestion
**Evaluation metric:** Recall of high-risk fixtures confirmed by a certified assessor, at a precision the assessor will tolerate. A missed anchor point in a patient bathroom is the costly error.
**Scope:** 1–2 engineers, 3–4 months. The hard part is data: labelled photographs of behavioral rooms are scarce, so synthetic rendering of fixtures in varied rooms and lighting is the starting point, with consented photographs from a partner hospital for validation.
**Data availability:** Few public images. Product catalogues and the Design Guide are published. Assessment reports are hospital work product, and photographs of secure units need the hospital's consent.
