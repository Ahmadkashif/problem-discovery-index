# Machine Learning Opportunities — Ambulance Services

**Industry:** [[ambulance-services|Ambulance Services]]
**Derived from:** [[problems/ambulance-services/high-impact|High Impact]], [[problems/ambulance-services/low-impact-1|Low Impact 1]], [[problems/ambulance-services/low-impact-2|Low Impact 2]], [[problems/ambulance-services/worker-life-1|Worker Life 1]], [[problems/ambulance-services/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Paramedic's Read of Hidden Severity
#tacit-knowledge-ml #gradient-boosting #transformers #feature-engineering #evaluation-metrics #worker-facing

**Problem statement:** Experienced paramedics recognise, within minutes and before the vitals confirm it, which patients are septic, infarcting or about to decompensate. They cannot fully say how, and the read is never recorded as a prediction or graded against what the hospital found. The ML problem is to learn that read from the medic's own first-contact impression, the ePCR and the linked hospital outcome, and offer it to less experienced crews in time to change care and destination.

**ML task:** Binary and multi-label classification at first vital signs (ICU admission or death within 24 hours; sepsis, STEMI or stroke confirmed), producing calibrated probabilities, with the medic's impression as both a feature and a benchmark
**Input data:** NEMSIS v3.5 ePCR fields (dispatch determinant, age, vitals series, GCS, glucose, ETCO2, 12-lead interpretation, interventions, medications, scene and history); the narrative; a one-tap crew impression (stable, sick, critical) and suspected condition captured at first contact; hospital outcomes linked through a health information exchange, a hospital data-exchange feed or state trauma, stroke and STEMI registries.
**Target:** ICU admission or in-hospital death within 24 hours of arrival; confirmed sepsis, STEMI or stroke; and agreement between model and senior-medic impression.
**Evaluation metric:** Sensitivity at a fixed alert rate (for example, alerts on 10% of transports), plus AUROC and calibration on a temporally held-out year, because the agency's population and protocols drift. Missing a critical patient costs far more than an extra alert, so recall on the critical class is the binding metric. Compare against the medic's own impression and against existing triggers (qSOFA, shock index) to show the model adds signal.
**Scope:** The data collection challenge is the hardest part. The expert's read has to be captured at the patient's side, so the project starts by adding a one-tap or voice impression to the ePCR workflow at a partner agency and running it for months before any model exists. The labelling challenge is that hospital outcomes arrive late and linkage is patchy, and medics disagree with themselves: repeated ratings of the same de-identified vignettes are needed to measure intra-rater agreement as the ceiling. The medic's own interventions also change the outcome they predicted. The deployment challenge is speed. The risk must appear on the tablet as the first vitals are entered, offline if coverage drops, and faster than the senior medic's own read, or it will be ignored. 2 ML engineers, 1 clinical informaticist and a medical director at a partner agency, 9–12 months, with the outcome feedback loop delivered first and the model second.
**Data availability:** ePCR data is held by each agency under HIPAA and by its ePCR vendor under business associate agreements. NEMSIS public-release data (63.6 million activations in the 2025 release) supports pre-training of the structured model but has no hospital outcome. Linked outcomes need agency-hospital data agreements. The first-contact impression does not exist anywhere yet and must be collected. All development outside the agency runs on synthetic or de-identified records.

---

## 2. Level-of-Service and Medical-Necessity Classification from the ePCR
#bert #transformers #logistic-regression #evaluation-metrics #compliance #revenue-impact #quick-win

**Problem statement:** Coders read each ePCR to decide the HCPCS level (A0426–A0429, A0433, A0434) and whether the documentation supports medical necessity. Errors in either direction cost money: undercoding loses revenue, overcoding is recouped. Given the structured ePCR and narrative, predict the supportable level and flag runs whose documentation will not support the level or the necessity, with the sentences that decide it. This entry is the core of the two-week MVP: a PCS and medical-necessity checker on synthetic NEMSIS v3.5 ePCRs that assigns A0426–A0429 and prices each run from the CMS Ambulance Fee Schedule PUF.

**ML task:** Multi-class classification of level of service, plus binary classification of documentation sufficiency for medical necessity, with span extraction of supporting evidence
**Input data:** NEMSIS v3.5 fields (eResponse dispatch priority, eSituation complaint, eVitals, eProcedures, eMedications, eDisposition), the narrative, origin and destination type, loaded miles, PCS presence and date for scheduled runs; the CY2026 AFS PUF (base $284.56, RVUs 1.00–3.25, locality GPCIs) for pricing.
**Target:** The coder-final HCPCS level; a sufficiency label from audit outcomes (paid, denied, recouped) where available, otherwise from senior coder review; and the evidence spans.
**Evaluation metric:** Macro-F1 on level, with a confusion matrix focused on the A0427/A0426 and A0429/A0428 boundaries where the money and the audits concentrate. For sufficiency, precision on "will fail" flags matters most: a coder who receives too many false flags stops reading them. Report the dollar value of corrected claims at PUF prices as the business metric.
**Scope:** The MVP takes two weeks on synthetic data. Generate a few thousand NEMSIS-shaped ePCRs with narratives across levels, write the Medicare level-of-service rules as a rule layer, train a small transformer classifier for sufficiency, and price each run from the PUF. A production version needs a billing firm's historical claims with outcomes: 1 ML engineer and 1 senior ambulance coder, 4–6 months.
**Data availability:** The AFS PUF and the NEMSIS data dictionary are public. Real ePCR and claim outcomes sit with operators and billing firms under BAAs. CERT and RSNAT statistics give the error mix (46.7% insufficient documentation and 24.9% medical necessity in the FY2025 ambulance sample) but not claim-level labels.

---

## 3. RSNAT Packet Completeness and Affirmation Prediction
#large-language-models #logistic-regression #gradient-boosting #compliance #automation #workflow-orchestration

**Problem statement:** Before a request goes to the MAC, predict whether the RSNAT packet (PCS plus clinician documentation) will be provisionally affirmed, and extract the specific defects (unsigned PCS, missing credentials, date outside 60 days, notes that do not show other transport is contraindicated) so the PCS specialist fixes them first.

**ML task:** Document extraction and field validation by LLM over faxed and scanned PDFs, then binary classification of affirmation
**Input data:** Scanned PCS forms and clinician notes; the beneficiary's schedule of round trips; prior requests and MAC decision letters with non-affirmation reason codes; diagnosis and mobility descriptors.
**Target:** Provisionally affirmed versus not; non-affirmation reason category; extracted field values.
**Evaluation metric:** Field-level extraction accuracy on signature, credentials and dates (checked against human review), and recall on packets that will be non-affirmed, since a missed defect costs a 7-day cycle and possibly prepayment review after the fourth round trip.
**Scope:** 1 ML engineer and 1 PCS specialist, 3–4 months. Labels come from the operator's own decision letters, so a mid-size operator with a few thousand historical requests has enough. National affirmation was 72.4% of completed requests in FY2024, so the minority class is large enough to learn.
**Data availability:** Decision letters and packets are held by the operator or its billing firm. Supporting notes are PHI from third-party clinicians. MAC rules and the MLN booklet are public.

---

## 4. Call-Demand Forecasting for System Status Management
#time-series-forecasting #temporal-fusion-transformers #exponential-smoothing #gradient-boosting #evaluation-metrics #workflow-orchestration

**Problem statement:** Forecast 911 call demand by zone and hour, and interfacility demand by facility and hour, so dispatchers can post units and book scheduled transfers without leaving the county short of coverage at the next peak.

**ML task:** Hierarchical probabilistic time-series forecasting (zone × hour for 911; facility × hour for transfers), with quantile outputs feeding a coverage calculation
**Input data:** CAD incident history with timestamps and locations; hospital discharge and transfer request history; calendar, weather, events and school schedules; unit status logs.
**Target:** Calls per zone per hour (911) and requests per facility per hour (scheduled), as quantiles.
**Evaluation metric:** Pinball loss and interval coverage at the 80th and 95th quantiles, measured on held-out weeks. The operational test is how often the posting plan built from the forecast left a zone uncovered when a priority-1 call arrived, compared with the current static plan.
**Scope:** 1 data scientist, 3 months for a single county. Classical seasonal baselines (exponential smoothing) are strong, so the gain must be shown over them before a temporal fusion transformer or gradient-boosted model is justified.
**Data availability:** CAD data is held by the operator or the public safety answering point; scheduled requests by the operator. Neither is shared across agencies, so models are trained per system.

---

## 5. Critical Care Handoff Summary Extraction
#large-language-models #transformers #seq2seq #evaluation-metrics #data-integration #worker-facing

**Problem statement:** Turn a sending ICU's medication administration record, active orders, ventilator flowsheet and notes into a one-page transport summary of active infusions, time-critical doses, ventilator settings, lines, allergies and code status, each linked to its source, for bedside confirmation by the critical care transport nurse.

**ML task:** Structured information extraction and normalisation (drug, concentration, rate, dose units, timestamps) from semi-structured and unstructured hospital documents
**Input data:** HL7 or FHIR feeds where the sending hospital offers them, otherwise printed or PDF packets; medication vocabularies for normalisation.
**Target:** A structured summary with fields per infusion and setting, and a "changed in the last two hours" flag.
**Evaluation metric:** Field-level precision and recall on infusions and ventilator settings against nurse-confirmed summaries, with zero tolerance for a wrong concentration or rate presented as confident. Low-confidence fields must be shown as unverified, not filled.
**Scope:** 1 ML engineer and 1 critical care transport nurse, 4 months, using synthetic ICU packets first. Hospital interface work is the slow part.
**Data availability:** Hospital records are PHI held by the sending hospital, shared with the transport team for the handoff. Synthetic packets can be generated for development; real evaluation needs a hospital-based transport programme.
