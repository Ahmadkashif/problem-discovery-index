# Machine Learning Opportunities — Skilled Nursing Facilities

**Industry:** [[skilled-nursing-facilities|Skilled Nursing Facilities]]
**Derived from:** [[problems/skilled-nursing-facilities/high-impact|High Impact]], [[problems/skilled-nursing-facilities/low-impact-1|Low Impact 1]], [[problems/skilled-nursing-facilities/low-impact-2|Low Impact 2]], [[problems/skilled-nursing-facilities/worker-life-1|Worker Life 1]], [[problems/skilled-nursing-facilities/worker-life-2|Worker Life 2]]

---

## 1. Learning the Floor's Read of a Resident's Decline
#tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #feature-engineering #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Experienced CNAs and charge nurses sense that a resident is deteriorating a day or two before vitals or labs show it, and that read decides whether the resident is treated in the building or sent to hospital. The ML problem is to capture the read as a signal, combine it with the resident's own baseline across routine streams, and predict acute transfer early enough to act.

**ML task:** Time-to-event prediction of acute hospital transfer or ED visit (72-hour and 7-day horizons) with per-resident baseline deviation features, plus extraction of change-of-condition concepts from nurse notes and CNA free text
**Input data:** CNA point-of-care ADL flowsheets (transfers, toileting, eating, meal percentage, behaviours) against the resident's rolling baseline; one-tap or voice "something's different" flags with timestamps and observer ID; vitals, weights, intake; new orders, antibiotics and psychotropics; lab results; nurse progress note text; MDS cognitive, functional and diagnosis items; staffing on the unit that day from payroll and PBJ.
**Target:** Hospital transfer, ED visit, or in-house treatment of an acute change within 72 hours and 7 days, with the reason for transfer; secondarily, whether a CNA's flag was followed by a confirmed acute condition.
**Evaluation metric:** Recall of transfers at a fixed alert budget (for example, no more than two alerts per unit per shift), because the binding cost is nurse attention, not compute. Calibration of the 7-day risk matters for prioritisation. Report lead time gained over the first nurse note documenting the change, and measure the model against the experienced aide's own flag as the human benchmark. A missed decline costs a hospitalisation and possibly a life; a false alert costs a focused assessment.
**Scope:** The data collection challenge comes first: the expert's read has to be recorded at the moment it happens, by the aide, without adding typing to a short-staffed shift. That means a voice or one-tap capture surface on existing point-of-care devices, piloted on a few units for months before any model. The labelling challenge is that transfers are a noisy label (some are unavoidable, some reflect a family's or physician's preference) and aides disagree with themselves across day and night shifts. Labels therefore need clinician adjudication of avoidability on a sample, and per-observer reliability estimates. The deployment challenge is that the alert must beat the experienced nurse's own sense and lead to a protocolised action, or alarm fatigue kills it within weeks. A team of 2 ML engineers, 1 clinical informaticist and a nurse champion per pilot building would need 9–12 months. Early value comes from surfacing accumulated soft signals across shifts before any prediction is trusted.
**Data availability:** ADL flowsheets, vitals, orders and notes sit in the facility's EHR (mostly PointClickCare and MatrixCare) and need a business associate agreement and EHR integration. The aide's soft read does not exist as data today and must be built. Transfers are recorded in the EHR and the MDS discharge assessment. Readmission outcomes after discharge need hospital or claims linkage.

---

## 2. Evidence-Linked MDS and PDPM Item Coding
#large-language-models #transformers #bert #evaluation-metrics #compliance #revenue-impact #automation

**Problem statement:** Suggest MDS item codes that drive PDPM and Medicaid case-mix (primary clinical category, Section GG function, SLP and nursing items, NTA comorbidities) from the chart inside each item's look-back window. Every suggestion must link to its supporting note, and items coded without support must be flagged.

**ML task:** Document-level and span-level extraction with multi-label classification against MDS items, constrained by RAI Manual look-back windows; ICD-10 to PDPM clinical category mapping
**Input data:** Hospital discharge summaries and history and physicals, therapy evaluations, nurse notes, CNA ADL flowsheets, medication administration records, physician orders, prior MDS assessments, and the RAI Manual item definitions as retrieval context.
**Target:** Item-level code suggestions with evidence spans and confidence; flags for coded items lacking support; projected PDPM component groups and case-mix index.
**Evaluation metric:** Item-level agreement with expert MDS nurse coders on a double-coded sample, reported separately for under-coding (lost revenue) and over-coding (audit risk). Precision on "unsupported item" flags matters most for compliance, and recall on missed NTA comorbidities matters most for revenue. Track case-mix change after deployment against audit outcomes, so the model is not simply raising scores.
**Scope:** Labels exist in volume as historical MDS assessments paired with charts, but historical coding is itself noisy and biased upward in places. A gold set of a few thousand assessments re-coded by senior MDS nurses is needed. 2 ML engineers and 1 MDS clinical lead, 6 months to a coordinator-facing tool. CMS's FY 2027 PDPM upcoding RFI makes the over-coding side a requirement, not an option.
**Data availability:** Charts and MDS are PHI held in the EHR. Training needs data from multiple facilities under BAAs, or an EHR vendor's partnership. Audit outcomes (TPE results, Medicaid case-mix review findings) are held by facilities and consultants.

---

## 3. Facility Staffing-Gap and Staffing-Star Forecasting from Public PBJ Data
#time-series-forecasting #gradient-boosting #recurrent-forecasting #evaluation-metrics #feature-engineering #quick-win #data-integration

**Problem statement:** Using only public CMS data, forecast each facility's next-quarter staffing hours per resident day by role, its weekend dips and contract-staff share, and its likely Five-Star staffing rating. Rank facilities by the gap between reported staffing and their residents' acuity.

**ML task:** Panel time-series forecasting at facility-day level with hierarchical aggregation to quarter; classification of the next staffing star
**Input data:** PBJ daily nurse staffing public use files (paid hours by job category, employee versus contract, MDS-derived daily census); Care Compare provider information (star ratings, turnover, case-mix-adjusted staffing, ownership, chain affiliation); CMS-2567 deficiency history; cost report wage data; county labour-market data from BLS.
**Target:** Daily and quarterly HPRD by RN, LPN and nurse aide; weekend versus weekday gap; contract share; next staffing star; "shortfall days" below a facility's own acuity-adjusted expected staffing.
**Evaluation metric:** MAE on quarterly HPRD by role, accuracy and macro-F1 on the next staffing star, and rank correlation of predicted versus realised shortfall across facilities. Backtest strictly on data available at each quarter's release date, because PBJ releases lag the quarter.
**Scope:** This is the most buildable entry. The data are public, facility-identified and free, with no PHI. A credible demo is two weeks for one engineer. A product for chains, REITs, lenders and MA plans takes 3–4 months with a data engineer and an analyst who knows the staffing star method.
**Data availability:** Fully public on data.cms.gov and Care Compare, refreshed quarterly and monthly. Cleaning is the work: census anomalies, facilities that change ownership, and PBJ audit failures (242 facilities failed one in CMS's June 2026 risk-based survey data).

---

## 4. Survey Deficiency Risk from Public Inspection, Staffing and Quality Data
#gradient-boosting #logistic-regression #bert #survival-analysis #evaluation-metrics #compliance #quick-win

**Problem statement:** Predict, for each facility, the probability of a harm-level (G or above) citation at its next standard survey or complaint investigation, the F-tags most likely to be cited, and the expected timing of the next survey given the state agency's backlog.

**ML task:** Binary and multi-label classification of next-survey outcomes; text classification of historical 2567 narratives into structured findings; survival modelling of time to next survey by state
**Input data:** CMS-2567 deficiency records and narrative text by facility and survey; survey dates and state agency; PBJ staffing and turnover; MDS-based quality measures from Care Compare; complaint counts; ownership changes; risk-based survey qualification status.
**Target:** Harm-level citation (yes/no) at the next survey; probability per F-tag group; days to next standard survey.
**Evaluation metric:** PR-AUC on harm-level citation, because these outcomes affect a minority of surveys (19.6% of facilities had an actual-harm citation in the last cycle, per CMS June 2026 data); top-decile lift for prioritising consultant visits; time-dependent concordance for survey timing. A false "low risk" costs more than a false "high risk", so recall at the top of the ranking matters most.
**Scope:** Public data again. The text side needs a classifier to turn narratives into consistent care areas and evidence types, with a few hundred hand-labelled findings. 1–2 engineers, 3 months. The model predicts surveyor behaviour as much as facility quality, which is useful to operators but must be explained honestly.
**Data availability:** Public and facility-identified. Mock-survey results and plans of correction that worked are held by consultants and operators, and would improve the model under data-sharing agreements.

---

## 5. Video-Based Fall Detection and Fall Review in Long-Stay Dementia Units
#cnns #object-detection #transfer-learning #evaluation-metrics #worker-facing #compliance

**Problem statement:** Detect falls and near-falls in residents' rooms from privacy-preserving video in real time, and support post-fall review of how the fall happened, for long-stay residents with dementia who cannot report it themselves.

**ML task:** Pose estimation and action detection on video (lying-on-floor, unassisted rising, bed and chair exits), with event classification and clip retrieval for human review
**Input data:** Wall-mounted camera video captured only on detected events and retained for review under resident or family consent; room layout; resident fall history and medications from the EHR; staff response times.
**Target:** Fall and near-fall events with timestamps; time on floor; likely mechanism (slip from bed, chair transfer, walking); staff response latency.
**Evaluation metric:** Event-level sensitivity for falls (missing a fall can mean hours on the floor) with false alarms per resident-night as the constraint. Measure ED transfers per fall before and after, and the MDS long-stay "falls with major injury" measure that enters SNF VBP from FY 2027.
**Scope:** Detection models exist, and SafelyYou has published memory-care evidence (8.3% of detected falls led to ED visits versus 24.5% in the control group). The hard parts are consent, privacy and state camera rules in a SNF; integration with nurse-call and the EHR; and staffing a 24/7 review function. Commercial vendors already serve this market, so the build case is integration and outcome measurement, not a new detector.
**Data availability:** Vendors hold large labelled video corpora. A facility holds none. Fall incident reports and MDS falls items are in the EHR.
