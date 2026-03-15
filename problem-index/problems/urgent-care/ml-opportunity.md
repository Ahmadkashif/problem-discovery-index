# Machine Learning Opportunities — Urgent Care Centers

**Industry:** [[urgent-care|Urgent Care Centers]]
**Derived from:** [[problems/urgent-care/high-impact|High Impact]], [[problems/urgent-care/low-impact-1|Low Impact 1]], [[problems/urgent-care/low-impact-2|Low Impact 2]], [[problems/urgent-care/worker-life-1|Worker Life 1]], [[problems/urgent-care/worker-life-2|Worker Life 2]]

---

## 1. Waiting Room Triage Acuity Scoring from Visual and Behavioral Cues
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml #worker-facing

**Problem statement:** Experienced nurses and MAs can visually assess a waiting room patient — skin color, posture, respiratory rate approximation, level of distress — and immediately flag who needs to be seen urgently before any vitals are taken. This tacit pattern recognition can be captured as a multimodal triage model that combines entered chief complaint and demographic data with waiting room observation signals.

**ML task:** Multiclass classification (acuity tier: routine / priority / urgent / immediate) combining structured intake data with optional video-based behavioral distress signals
**Input data:** Chief complaint (text), age, presenting vital signs, time of day, day of week, and optionally ambient video frame features (posture, respiratory effort, skin appearance)
**Target:** Acuity class at intake, validated against final visit acuity and outcomes (escalation events, ED transfers, critical diagnoses)
**Evaluation metric:** Weighted F1 across acuity classes; recall on "urgent" and "immediate" classes must exceed 0.92 — false negatives are clinically unacceptable
**Scope:** A structured-data-only model (no video) using gradient boosting on intake features is buildable in 4-6 weeks with 6-12 months of historical visit data. Adding a vision component requires either a wearable (patient-worn accelerometer) or waiting-room camera with consent framework — significantly more complex and a 3-6 month project.
**Data availability:** Any urgent care EHR has chief complaint, demographics, and vital signs. The outcome label (was this patient actually high acuity?) is derivable from diagnosis, treatment performed, and transfer events. Centers with 10,000+ visits/year have sufficient volume for a robust model.

---

## 2. Patient Volume Demand Forecasting
#gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact

**Problem statement:** Predict daily and hourly patient visit volume for an urgent care center 24-72 hours out, using center-specific historical data enriched with external signals — enabling data-driven staffing decisions that eliminate the revenue loss from understaffed surges and the waste from overstaffed slow periods.

**ML task:** Time-series regression (predicted visit count per hour) with uncertainty bounds
**Input data:** 2-3 years of center visit history with timestamps, enriched with: day of week, US holidays, school calendar, weather forecast, CDC ILINet flu surveillance data, local event calendar
**Target:** Hourly visit count predictions with 80% and 95% confidence intervals for each forecast window
**Evaluation metric:** Mean Absolute Percentage Error (MAPE) <12% at 24-hour horizon; <18% at 72-hour horizon; calibration of confidence intervals (80% CI should contain true value 80% of the time)
**Scope:** A center-specific gradient boosting model (LightGBM) with time-series cross-validation is buildable in 3-4 weeks. Initial model uses center visit history + day/week/holiday features only; external signals (weather, flu surveillance) add 5-8% accuracy improvement and can be layered in. Multi-center operators can use transfer learning across locations.
**Data availability:** EHR systems log every visit with timestamps. Most centers have 3+ years of data. External enrichment data is freely available (NOAA weather, CDC ILINet, school district calendars).

---

## 3. Ambient Clinical Encounter Transcription and Chart Generation
#transformer #speech-recognition #seq2seq #nlp #worker-facing

**Problem statement:** Convert urgent care clinical encounter audio (physician-patient conversation during the visit) into a structured SOAP note draft in the center's EHR template format, ready for physician review and signature within 60 seconds of visit end.

**ML task:** Two-stage pipeline: (1) ASR — audio to transcript; (2) structured note generation — transcript to SOAP note in center's specific template
**Input data:** Consented clinical encounter audio (8-15 minutes), structured EHR template for the note format, patient context (age, sex, chief complaint, vital signs)
**Target:** Complete draft SOAP note with chief complaint, HPI, ROS, physical exam, MDM narrative, diagnosis (ICD-10), and discharge instructions — conforming to the center's documentation standards and CMS medical necessity language requirements
**Evaluation metric:** Physician acceptance rate (% of generated notes accepted with <3 edits); time-to-signature reduction vs. baseline; MDM quality rubric score (evaluated by clinical reviewer)
**Scope:** Off-the-shelf ASR (Whisper large, Deepgram Medical) handles transcription reliably. The chart generation stage can be prompt-engineered with a fine-tuned LLM in 6-8 weeks using 500+ note pairs (transcript → final signed note) for few-shot or fine-tuning. Clinical reviewers must validate outputs. Full deployment including EHR integration is a 3-4 month project.
**Data availability:** Signed historical notes are available in any EHR. Matched transcripts require prospective data collection — centers must begin recording encounters with consent. A pilot of 200 encounters is sufficient for prompt engineering; 1,000+ for fine-tuning.

---

## 4. ICD-10 Diagnosis Coding Accuracy and Specificity Improvement
#bert #text-classification #nlp #compliance #revenue-impact

**Problem statement:** Urgent care physicians often code diagnoses at low specificity (J06.9 — acute upper respiratory infection, unspecified) when the clinical documentation supports a more specific code that reimburses at higher rates and satisfies payer medical necessity requirements. Automatically suggest the highest-specificity appropriate ICD-10 code given the clinical note.

**ML task:** Multilabel classification (ICD-10 code suggestion) from clinical note text
**Input data:** Final signed clinical note text (HPI, exam, MDM), any ordered tests and results, prescribed medications
**Target:** Ranked list of ICD-10 codes appropriate for the encounter, with confidence scores and the specific note evidence supporting each code
**Evaluation metric:** Top-3 accuracy (correct code in top 3 suggestions); revenue uplift per encounter vs. baseline coding; payer rejection rate on suggested codes
**Scope:** Fine-tuned BioClinicalBERT or a specialized coding model (CodaMetrix) can achieve this. Training data requires pairs of (clinical note, accepted ICD-10 codes) — available from any center's billing history. 4-6 week project for a basic model; 3 months for production-quality with billing system integration.
**Data availability:** Every urgent care center has years of (note, code, billing outcome) records. The "correct" label is approximated by codes that were accepted by payers without modification — a proxy that works well at scale.

---

## 5. Antibiotic Stewardship Decision Support
#gradient-boosting #binary-classification #tabular-ml #compliance

**Problem statement:** Urgent care centers are significant contributors to antibiotic overprescription — particularly for respiratory infections where antibiotics provide no benefit but are frequently prescribed under patient pressure. A model predicting bacterial vs. viral etiology from clinical presentation data can support the provider in declining antibiotic requests with data-backed confidence.

**ML task:** Binary classification (bacterial vs. viral etiology likely) from clinical presentation features
**Input data:** Chief complaint, symptom duration, fever peak, presence of exudate, lymphadenopathy, cough character, rapid strep/flu test result, patient age, comorbidities
**Target:** Probability score for bacterial etiology, with confidence interval and primary feature drivers
**Evaluation metric:** AUC-ROC; sensitivity/specificity at clinically relevant thresholds; correlation with culture confirmation (when available) as ground truth
**Scope:** A well-established research problem with public datasets (PEACH, GRACE). A center-specific model calibrated to local pathogen prevalence is a 4-6 week project using 2-3 years of visit + rapid test + prescription data. Key constraint: ground truth (culture confirmation) is rarely available for outpatient URIs, so proxy labels (rapid test results + treatment response) must be used.
**Data availability:** Any urgent care EHR with rapid strep, rapid flu, and urinalysis results linked to diagnosis and prescription data has sufficient structured features. Culture results are rare but can be supplemented with public datasets.
