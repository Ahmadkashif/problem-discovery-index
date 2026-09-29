# Machine Learning Opportunities — Telehealth Platforms

**Industry:** [[telehealth-platforms|Telehealth Platforms]]
**Derived from:** [[problems/telehealth-platforms/high-impact|High Impact]], [[problems/telehealth-platforms/low-impact-1|Low Impact 1]], [[problems/telehealth-platforms/low-impact-2|Low Impact 2]], [[problems/telehealth-platforms/worker-life-1|Worker Life 1]], [[problems/telehealth-platforms/worker-life-2|Worker Life 2]]

---

## 1. Clinical Resolution Measurement and Clinician Feedback
#survival-analysis #causal-inference #gradient-boosting #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Platforms measure visit volume, wait time and satisfaction. Whether the symptom resolved, whether the patient returned, filled the prescription or presented to an emergency department is either in the platform's own data or obtainable, and is not examined — so no clinician ever learns whether a decision was right.

**ML task:** Estimate resolution and adverse downstream outcome rates per presentation, protocol and clinician, adjusting for case mix, and deliver individual feedback
**Input data:** Return visits for the same complaint within defined windows; prescription fill and refill data through pharmacy networks; downstream utilisation from claims for insured populations; referral completion; structured patient follow-up at three and fourteen days; presentation severity and comorbidity from intake; clinician and protocol identity.
**Target:** Symptom resolution without further care-seeking, and adverse downstream events.
**Evaluation metric:** Case-mix adjustment is the whole difficulty — a clinician who sees sicker patients will have worse raw outcomes, and an unadjusted comparison would be both wrong and professionally damaging. Report clinician-level estimates only with intervals wide enough to reflect the sample, and never rank on point estimates. The most informative single output needs no external data at all: return-visit rate for the same complaint, by protocol, which is computable today.
**Scope:** Patient follow-up response will be partial and its selection bias characterisable; report it rather than assuming representativeness. Individual clinician feedback should be framed as calibration rather than performance management, since this workforce has never received any and an enforcement framing will produce defensive documentation rather than better decisions. 2 data scientists plus a clinical lead, 9-12 months.
**Data availability:** Return visits are internal and immediate. Fill data and claims require integration and a lawful basis. Follow-up requires only a message.

---

## 2. Appropriateness Measurement Separated From Satisfaction
#gradient-boosting #hypothesis-testing #confidence-intervals #causal-inference #bert #evaluation-metrics #compliance #worker-facing

**Problem statement:** Satisfaction is an actively misleading quality proxy in medicine — a patient who wanted an antibiotic and received one rates the visit highly — and it is the metric that governs clinician standing on platforms whose commercial pressure already runs toward the satisfying answer.

**ML task:** Measure prescribing and referral appropriateness against clinical guidelines conditioned on documented presentation, and report it alongside satisfaction with the divergence made explicit
**Input data:** Structured presentation data from intake and notes; prescribing decisions including antibiotic and controlled substance classes; referral and escalation decisions; applicable clinical guidelines; patient satisfaction ratings; peer comparison within comparable presentation mixes.
**Target:** Guideline concordance given the documented presentation, adjudicated on a clinically reviewed sample.
**Evaluation metric:** Agreement with clinical reviewer adjudication on sampled cases, since guidelines admit legitimate exceptions and a rigid concordance measure would penalise appropriate clinical judgement. The output that matters is the divergence: identifying clinicians and protocols where satisfaction is high and appropriateness is low, and the reverse — the second group being clinicians making correct unpopular decisions who are currently penalised by the rating system. Controlled substance prescribing patterns warrant separate and careful treatment given the regulatory environment.
**Scope:** This measurement is defensive as well as clinical — the direct-to-consumer prescribing segment is under active regulatory scrutiny, and a platform able to evidence appropriateness is in a different position from one that cannot. It will also produce findings that are discoverable, which is the reason it is avoided. 1-2 data scientists plus clinical reviewers, 6-9 months.
**Data availability:** Prescribing and presentation data are complete internally; guideline encoding is the build.

---

## 3. State-Level Demand Forecasting and Licensure-Constrained Staffing
#time-series-forecasting #convex-optimization #gradient-boosting #confidence-intervals #optimization-fundamentals #evaluation-metrics #automation #compliance

**Problem statement:** Licensure makes the available clinician pool a subset of the workforce for every patient, demand varies by state and hour, and platforms staff from historical averages — producing simultaneous queues in some states and unpaid idle time in others.

**ML task:** Forecast demand by state and hour, solve staffing and routing under licensure and availability constraints, and value additional state licences as a capital decision
**Input data:** Historical visit volume by state, hour, day and season; respiratory season and epidemiological signals; weather events; employer enrolment cycles and marketing activity; clinician licensure portfolios, availability and credentialing status; realised wait times and abandonment.
**Target:** Visit demand per state-hour, and unserved demand attributable to licensure gaps.
**Evaluation metric:** Forecast accuracy at the horizon staffing decisions are actually made — typically one to four weeks — rather than day-ahead, which is the easy case. The operational measures are patient wait time and clinician paid-versus-idle time reported together, since improving one at the expense of the other is not an improvement; idle time in particular is currently borne by contractors and is invisible in platform metrics.
**Scope:** The licence portfolio decision is the higher-value and less obvious piece: the expected value of adding a licence is the persistent unserved demand it unlocks, and platforms currently decide this by intuition on a meaningful recurring expense. 1-2 data scientists, 4-6 months.
**Data availability:** Complete internally; epidemiological signals are public.

---

## 4. Adaptive Intake, Ambient Documentation for Short Encounters, and Loop Tracking
#transformers #large-language-models #bert #gradient-boosting #graph-neural-networks #evaluation-metrics #compliance #workflow-orchestration

**Problem statement:** Documentation consumes a large share of a short visit, intake questionnaires are generic rather than adaptive, the record rarely reaches the patient's own doctor, and the referrals, orders and authorisations that make care continuous are tracked by a coordinator with a spreadsheet.

**ML task:** Adaptive intake that branches on answers and retrieves external records; ambient documentation adapted to short video and asynchronous encounters; open-loop tracking with risk-based prioritisation and drafted prior authorisation submissions
**Input data:** Intake responses and branching outcomes; available external records through exchange networks; consultation audio where it exists and message threads where it does not; historical notes and coding; referrals, orders, authorisations and prescriptions with their closure events; payer authorisation criteria; laboratory and pharmacy interfaces.
**Target:** Note accuracy and completeness as judged by clinician acceptance; loop closure and the detection of overdue or failed loops.
**Evaluation metric:** For documentation, clinician edit rate and time saved, with clinically significant omissions counted separately and weighted heavily — a note that reads well and omits the safety-netting advice is a worse artefact than no note. For loop tracking, detection of loops that would otherwise have closed only when harm occurred: the unacknowledged abnormal result, the unbooked referral, the uncollected prescription. Prioritisation must be by clinical consequence rather than by age.
**Scope:** Ambient documentation is built for longer in-person consultations and needs adapting to thin audio and message-based encounters, a substantial share of which have no audio at all. Structured capture of the decision, its reasoning and the safety-netting advice is what makes later outcome evaluation possible and is not what billing-optimised notes provide. 3 engineers plus a clinical informaticist, 9-12 months.
**Data availability:** Internal data is complete; exchange network participation is the variable input and is improving under interoperability requirements.
