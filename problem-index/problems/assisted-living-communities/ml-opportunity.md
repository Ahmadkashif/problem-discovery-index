# Machine Learning Opportunities — Assisted Living Communities

**Industry:** [[assisted-living-communities|Assisted Living Communities]]
**Derived from:** [[problems/assisted-living-communities/high-impact|High Impact]], [[problems/assisted-living-communities/low-impact-1|Low Impact 1]], [[problems/assisted-living-communities/low-impact-2|Low Impact 2]], [[problems/assisted-living-communities/worker-life-1|Worker Life 1]], [[problems/assisted-living-communities/worker-life-2|Worker Life 2]]

---

## 1. Forecasting True Care Need from the Move-In Assessment
#tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** An experienced wellness nurse reads, at the pre-move-in assessment, how much care a prospective resident will really need and whether the community can keep her safe, and that read sets the care fee and the admission decision. The ML problem is to capture the read and the evidence behind it, and predict delivered care minutes and the first adverse outcome over the first 180 days, so every nurse prices and places like the best one.

**ML task:** Regression of care minutes per day at 30, 90 and 180 days after move-in, plus time-to-event models for the first fall with injury, transfer to memory care or a nursing home, hospital admission and move-out; LLM extraction of functional, cognitive and behavioural cues from nurse notes and hospital documents as features
**Input data:** Assessment tool items (ADLs, medications, cognition, behaviours, fall history); nurse voice or text notes captured at the visit; hospital discharge summaries and physician reports; medication lists; prior-setting information (home, hospital, rehab); after move-in, caregiver task logs with timestamps, call-light response times, incident reports, level-of-care changes and, where installed, room-presence or sensor data.
**Target:** Delivered care minutes per day by horizon; 180-day probabilities and timing of the adverse events above; the gap between the assigned care level and predicted need.
**Evaluation metric:** Mean absolute error on care minutes against a time-and-motion sample (logged minutes alone are biased low). Concordance and calibration for the 180-day event models. The asymmetric cost is under-prediction: an under-assessed resident is unbilled care and a safety risk, while an over-assessed one is a lost move-in. Report error against the experienced nurse's own assigned level as the human benchmark.
**Scope:** The data collection challenge comes first: the expert's cues have to be recorded at the visit itself, through a short structured "what I noticed" step and voice notes, without stretching a 60–90 minute assessment (estimate), and delivered care has to be timed at least on a sample. The labelling challenge is that true need has no clean label: billed level is what is being corrected, logged minutes are noisy, outcomes reflect staffing and family choices, and nurses score differently under sales pressure, so labels need time-and-motion sampling and per-nurse reliability estimates. The deployment challenge is speed and law: the output must arrive before the family signs, must explain itself, and must support a care plan and price rather than deny admission, given fair-housing and state retention rules. A team of 2 ML engineers and 1 clinical informaticist working with a 10–20 community pilot would need 9–12 months; the first useful product is drift detection on residents already in the building.
**Data availability:** Assessment items and care logs sit in each operator's EHR or eMAR (Yardi, PointClickCare, August Health and others), under service agreements and, for communities that are HIPAA covered entities, business associate agreements. Nurse cues do not exist as data today and must be built. Time-and-motion samples must be paid for. Sensor vendors (Inspiren, SafelyYou) hold room-presence data that could stand in for care time where installed.

---

## 2. Fall and Exit Detection for Memory Care Nights
#cnns #object-detection #survival-analysis #evaluation-metrics #worker-facing #automation

**Problem statement:** Detect, in real time and without a person watching, a resident with dementia getting out of bed unsafely, lying on the floor or approaching an exit door. Rank alerts so one overnight caregiver covering 20–30 residents (estimate) goes to the right room first, and predict which residents are most likely to fall in the next 24 hours.

**ML task:** Video or depth-sensor event detection (pose and object detection for bed exit, floor, door approach) with temporal smoothing; a per-resident 24-hour fall-risk model from event history, sleep and activity patterns, medications and recent incidents
**Input data:** Privacy-preserving video, depth or radar streams from resident rooms and corridors; door contact sensors; call-light logs; staff badge or phone location; incident reports; medication changes (psychotropics, diuretics, sedatives); caregiver rounds.
**Target:** Event labels (bed exit, fall, on floor, exit approach) with timestamps; resident-level fall probability over 24 hours.
**Evaluation metric:** Recall of falls and exit attempts at a capped false-alert rate per caregiver per shift (for example, no more than one false alert per hour), since alarm fatigue kills adoption. Time from event to caregiver arrival is the operational outcome. A missed fall can mean a resident lying on the floor for hours; a false alert costs a walk down the hall.
**Scope:** Detection on video is a known computer-vision problem, and vendors have it in production (SafelyYou, Teton.ai, Inspiren's sensors). The open work is in two areas: tuning to rooms with low light, furniture, roommates and residents who sit on the floor deliberately, and alert ranking for a single caregiver. A team of 3 engineers on top of an existing sensor platform could ship ranking and 24-hour risk in 6 months. Building hardware and detection from scratch is a multi-year effort.
**Data availability:** Video and sensor data sit with the vendor that installed the hardware, and that is where training data lives; whether the vendor may reuse it is undetermined (subscription and consent terms unread). Incident labels come from the community's EHR. Public fall-detection datasets exist but are staged by young actors and transfer poorly to residents with dementia.

---

## 3. Inquiry-to-Move-In Propensity and First-Contact Attribution
#gradient-boosting #logistic-regression #large-language-models #evaluation-metrics #revenue-impact

**Problem statement:** Score each new inquiry for its likelihood of becoming a move-in within 60 days, so sales counselors call the right families first, and resolve which channel first introduced each family, so referral-agency fees of roughly a month's rent and care are paid only when owed.

**ML task:** Binary classification of 60-day move-in with calibrated probabilities; entity resolution across CRM records, call logs, web forms and referral-agency lead feeds to determine first contact
**Input data:** CRM inquiry records (source, timing, care type, stated urgency, prospect location), call recordings and transcripts, tour and follow-up history, referral-agency lead notifications with timestamps, web analytics, prior-move-in outcomes; names, phone numbers and addresses for matching.
**Target:** Move-in within 60 days (and care type); for attribution, the earliest verified contact channel per family.
**Evaluation metric:** Precision in the top decile of scored leads and lift over the counselor's own prioritisation. For attribution, precision of "duplicate lead" matches, because a wrong match denies an agency a fee it is owed and damages the relationship.
**Scope:** A standard propensity model on 2–3 years of CRM history per operator, built by 1–2 engineers in 3–4 months. Attribution is mostly data plumbing and matching rules, with an LLM reading call transcripts for "who told you about us." Aggregators of paid leads convert far worse than owned leads (Bild & Co. reports ~4% conversion on 32% of inquiries, search summary), so even simple scoring changes counselor time.
**Data availability:** Operators own their CRM data, held in vendor systems such as Aline (Sherpa, Enquire) and Yardi. Referral agencies hold the other half of the attribution record. Labels (move-ins) are clean and come quickly.

---

## 4. Street-Rate and Annual-Increase Pricing with Move-Out Risk
#time-series-forecasting #causal-inference #survival-analysis #gradient-boosting #revenue-impact

**Problem statement:** Recommend each vacant unit's street rate and each resident's annual increase from local demand, competitor supply, the building's care mix and the resident's own move-out risk, maximising revenue per occupied unit without triggering price-driven move-outs.

**ML task:** Demand forecasting of inquiries and move-ins by care type and unit type; causal estimation of the effect of rate changes and increases on conversion and 90-day move-out, using staggered increase timing across communities; survival modelling of length of stay by acuity
**Input data:** Rate sheets and concessions history, inquiries, tours and move-ins by unit type, move-outs with reasons, resident acuity and care fees, annual increase letters and dates, NIC MAP or competitor occupancy and asking rents, local demographics and new supply.
**Target:** Weekly move-ins by unit type at a given price; probability of move-out within 90 days of an increase, by size of increase; recommended rate and increase.
**Evaluation metric:** Out-of-sample forecast error on move-ins; for the causal piece, validation against holdout communities, since naive correlation confounds price with demand. The business test is a controlled pilot comparing revenue per occupied unit and move-outs.
**Scope:** 2 data scientists over 6 months for a 30-community operator. The hard part is causal identification: increases are applied to everyone at once in many chains, so variation has to come from differing increase sizes and timing across buildings. Antitrust scrutiny of shared-data rent algorithms in multifamily argues for using each operator's own data plus public market data, not pooled competitor rents (recalled).
**Data availability:** Operators hold their own rate, move-in and move-out data. NIC MAP sells market occupancy and rents (see the Pass 2 sweep). Move-out reasons are recorded inconsistently and need clean-up.

---

## 5. Incident and State Inspection Text Classification
#bert #transformers #large-language-models #evaluation-metrics #compliance #automation

**Problem statement:** Read caregiver incident notes and map each to the state-specific reportable categories and deadlines that apply. Separately, read public state inspection reports to predict which communities and which regulation areas are likely to be cited next.

**ML task:** Multi-label text classification of incident narratives into reportable categories (fall with injury, injury of unknown origin, elopement, abuse or neglect allegation, medication error), with jurisdiction-specific rule mapping; classification and clustering of citation narratives from state inspection reports; facility-level citation risk scoring
**Input data:** Free-text incident notes and structured incident fields; each state's reporting rules; public inspection and citation records where states publish them (California's CCLD reports are republished weekly by third-party sites such as ReadyRule, search summary); the community's own past surveys.
**Target:** Reportable categories, deadlines and recipients per incident; citation category labels; probability of a citation in a given regulation area at the next inspection.
**Evaluation metric:** Recall on reportable incidents at fixed precision. A missed reportable event is a citation risk and possibly a harmed resident, so recall matters more than precision. Citation-risk models are judged on ranking (AUC) and calibration across facilities.
**Scope:** A fine-tuned encoder or an LLM with retrieval over state rules can classify incident notes after a few thousand labelled examples. The rules library is the bigger job: 50 rulebooks, changing every year (18 states changed in 2025, NCAL). 2 engineers and a regulatory analyst could cover the ten largest states in 4–6 months.
**Data availability:** Incident notes belong to each operator. Inspection reports are public in many states but scattered across portals, PDFs and formats; 19 states publish no downloadable reports, by the Washington Post's 2023 count.
