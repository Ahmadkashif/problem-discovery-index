# Machine Learning Opportunities — Diagnostic Imaging Centers

**Industry:** [[diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Derived from:** [[problems/diagnostic-imaging-centers/high-impact|High Impact]], [[problems/diagnostic-imaging-centers/low-impact-1|Low Impact 1]], [[problems/diagnostic-imaging-centers/low-impact-2|Low Impact 2]], [[problems/diagnostic-imaging-centers/worker-life-1|Worker Life 1]], [[problems/diagnostic-imaging-centers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Radiologist's Protocol Read
#tacit-knowledge-ml #transformers #bert #large-language-models #evaluation-metrics #feature-engineering #worker-facing #revenue-impact

**Problem statement:** Experienced radiologists and lead technologists read an order, its free-text indication and the patient's history and know which protocol, contrast choice and exam will answer the question, and when the order itself is wrong. The ML problem is to learn that read from the centre's own protocol history and its downstream outcomes, propose a protocol for every incoming order with a calibrated confidence, and abstain on safety-sensitive cases.

**ML task:** Multi-class protocol classification (top-k ranking over the group's protocol library) from order text and structured fields, plus a binary "order likely wrong or needs radiologist" flag; calibrated probabilities with an abstention threshold
**Input data:** Order CPT and ICD-10 codes, free-text indication and referral attachments (faxed, OCR'd), patient age and sex, eGFR and contrast-allergy flags, implant flags from screening, prior imaging list, referring physician and specialty, scanner and site; the protocol chosen; technologist in-scan changes; final report text; addenda, recalls and repeat orders for the same body part within 30 days.
**Target:** The protocol a senior radiologist would assign; whether the study was adequate (no protocol-attributable recall, repeat or "limited study" addendum); whether the order was changed to a different exam.
**Evaluation metric:** Top-1 and top-3 agreement with held-out senior-radiologist protocols, reported against the radiologists' own inter- and intra-rater agreement on a re-protocolled sample, which is the real ceiling. Coverage at a fixed precision (share of orders the model can auto-propose at ≥98% agreement) is the business metric. For contrast decisions, recall on "needs radiologist review" must be near 100%, because a wrong contrast call is a patient-safety event while an unnecessary escalation costs 30 seconds.
**Scope:** The data collection challenge comes first. The protocol decision is stored but its reasons are not, so the training set has to be rebuilt by joining orders, protocols, technologist notes and reports across the RIS and PACS, and new decisions need a near-zero-effort capture of "why" (a one-tap reason code) inside the existing protocolling screen. The labelling challenge is that radiologists disagree with each other and with themselves, and group and referrer preferences shift the "right" answer, so a re-protocolled sample of a few thousand orders with repeated reads is needed to measure agreement, and adequacy labels must be mined from report language and later orders. The deployment challenge is speed: the proposal must appear in the radiologist's worklist, accept with one keystroke, and be faster than the expert's glance. 2 ML engineers, 1 clinical informatics radiologist at ~20% time, 5–7 months to a shadow-mode model at one group, and value first as retrieval ("this referrer's last 20 shoulder orders were protocolled as arthrograms").
**Data availability:** Each centre or reading group holds years of orders, protocols and reports in its RIS and PACS. The data is PHI, held under the group's own record or business-associate agreements, so models are trained per customer or on de-identified extracts. Adequacy labels need text mining and a clinical review sample; no public dataset pairs orders with protocols at scale.

---

## 2. Authorization-Match Risk at Intake
#gradient-boosting #large-language-models #bert #feature-engineering #evaluation-metrics #automation #revenue-impact

**Problem statement:** Predict, for every scheduled advanced-imaging exam, whether the authorization on file will fail to cover the exam actually performed (wrong CPT variant, laterality, site, date window or units), and which fact is likely to be wrong, early enough to amend before the scan.

**ML task:** Information extraction from faxed orders and approval letters (document NER with a fine-tuned transformer or an LLM with schema-constrained output), then binary classification of denial risk with gradient-boosted trees and a reason code
**Input data:** OCR'd order and approval documents; payer, plan and radiology benefit manager; authorized CPT, units, dates and site; scheduled exam, protocol and date; protocol changes after authorization; historical claims with denial reason codes (CARC/RARC) and amendment outcomes.
**Target:** Denial for authorization mismatch within 60 days of service (yes/no) and the mismatched field.
**Evaluation metric:** Precision at the top 5% of daily scheduled exams (the queue an intake team can work), recall on dollar-weighted denials, and field-level extraction accuracy. Missed denials cost a technical fee, while false alerts cost a coordinator's phone call, so recall on high-value MRI and PET exams matters more than overall precision.
**Scope:** 1 ML engineer and 1 data engineer, 3–4 months at a multi-site operator. Most of the work is joining claims outcomes to the scheduled exam and the authorization document. Payer rule content (which CPT variants a benefit manager treats as amendable) is maintained as a rule table beside the model, not learned.
**Data availability:** The centre holds orders, authorizations, schedules and remittances. Denial codes are standard but noisy, and approval letters vary by payer, so extraction needs a few hundred labelled documents per major benefit manager.

---

## 3. Exam-Duration and No-Show Forecasting for Scanner Scheduling
#gradient-boosting #survival-analysis #logistic-regression #monte-carlo-methods #optimization-fundamentals #time-series-forecasting #automation

**Problem statement:** Predict each booked exam's probability of attendance and its actual table time from the protocol, patient and booking features. Then use those predictions to set slot lengths, overbooking and same-day waitlist fills that maximise completed exams per scanner hour without overtime.

**ML task:** Binary classification (no-show, late cancellation) and quantile regression or survival modelling of exam duration; Monte Carlo simulation of the day's schedule under predicted durations and attendance, feeding a slot-assignment optimiser
**Input data:** RIS booking history (lead time, reschedules, prior no-shows, channel, referral source), patient travel distance and weather, payer and authorization status, protocol, contrast, implant and sedation flags, scanner, coil and technologist; scanner logs with actual start and end times.
**Target:** Attendance; table time in minutes; completed paid exams per scanner hour and technologist overtime for the simulated schedule.
**Evaluation metric:** AUC and calibration for no-show (the published XGBoost benchmark cut no-shows from 19.3% to 15.9% with targeted calls, AJR); pinball loss for duration quantiles; for the schedule, completed exams per scanner hour and overtime minutes in a prospective A/B over weeks. Overbooking errors are asymmetric: an overrun into a contrast block costs more than an idle slot.
**Scope:** 1 data scientist and 1 engineer, 3 months to a model and simulator; adoption depends on schedulers trusting variable slot lengths, so start with recommendations shown at booking.
**Data availability:** Every RIS records bookings and outcomes; scanner DICOM headers and logs give true start and end times. Data is per operator and PHI, but features can be computed without identifiers.

---

## 4. Image-Quality and Positioning Checks at the Console
#cnns #transfer-learning #object-detection #semantic-segmentation #evaluation-metrics #compliance #worker-facing

**Problem statement:** Detect, before the patient leaves the room, images that will be judged inadequate: motion-degraded MRI series, incomplete coverage, mammograms with poor positioning (pectoral muscle not to nipple level, inframammary fold missing). That lets the technologist repeat a view in seconds instead of recalling the patient.

**ML task:** Image classification and landmark detection with CNNs fine-tuned from public pretrained weights; segmentation of the pectoral muscle and nipple for mammographic positioning metrics
**Input data:** DICOM images with technologist and radiologist quality ratings, recalls flagged "technical", and repeat-image logs; for mammography, the facility's positioning reviews done for MQSA quality programmes.
**Target:** Adequate versus repeat-needed per series or view, with the failed criterion.
**Evaluation metric:** Sensitivity for repeat-needed views at a false-alarm rate technologists will tolerate (one or two per shift); reduction in technical recalls per 1,000 exams in a pilot. Missed inadequate views cost a recall and a second visit, and false alarms cost a second look, so sensitivity leads.
**Scope:** 2 ML engineers, 4–6 months for one modality; regulatory status depends on intended use (quality feedback to technologists rather than diagnosis), which needs a regulatory view before claims are made.
**Data availability:** Images are plentiful at any operator; quality labels are sparse and must be collected from technologist and radiologist reviews. Public mammography datasets (CBIS-DDSM, VinDr-Mammo) help pretraining but lack positioning labels.

---

## 5. Ultrasound Auto-Measurement and Strain-Aware Exam Assignment
#cnns #semantic-segmentation #transfer-learning #gradient-boosting #optimization-fundamentals #evaluation-metrics #worker-facing

**Problem statement:** Sonographers spend much of each exam holding the transducer still while placing calipers and Doppler gates by hand, and fixed schedules stack the most physically demanding exams on one person. The ML problem is to propose standard measurements and view labels on the frozen image, and to predict each exam's duration and physical load so the day's exams can be assigned evenly across the team.

**ML task:** Segmentation and landmark detection with CNNs fine-tuned from pretrained weights (organ boundaries, nodule axes, intima-media interfaces, vessel centrelines for Doppler gate placement); view classification; gradient-boosted regression of exam duration and a strain score; an assignment optimiser balancing strain-weighted minutes per sonographer
**Input data:** Ultrasound DICOM images and cine clips with the measurements sonographers placed, stored as DICOM structured-report objects, which give labels at no extra cost; exam type, patient BMI and prior exam durations from the RIS; sonographer rosters; optional self-reported discomfort scores from a short end-of-shift check-in.
**Target:** Measurement values and caliper positions; view labels; exam duration in minutes; strain-weighted minutes per sonographer per day.
**Evaluation metric:** Agreement of automatic measurements with sonographer and radiologist measurements (Bland–Altman limits within the inter-observer range), and seconds of hold and keyboard time saved per exam in a timed pilot. For assignment, the spread of strain-weighted minutes across sonographers and the number of days with back-to-back high-strain exams. A wrong measurement that reaches a report is a diagnostic error, so every proposal stays a suggestion the sonographer confirms.
**Scope:** 2 ML engineers and 1 sonographer lead, 5–6 months for one exam family (thyroid or renal) on one vendor's system. Measurement tools used for diagnosis need FDA clearance unless provided by the ultrasound maker, so the realistic path is partnering with a cart vendor or a cleared software platform. The scheduling half is software alone and can ship in 2–3 months.
**Data availability:** Any centre's PACS holds years of ultrasound studies with structured-report measurements. Images are PHI, so training needs de-identified extracts or on-premises training. Strain labels do not exist and must start from exam type, duration and patient size, with discomfort check-ins added prospectively.
