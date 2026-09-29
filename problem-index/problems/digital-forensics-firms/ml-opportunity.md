# Machine Learning Opportunities — Digital Forensics Firms

**Industry:** [[digital-forensics-firms|Digital Forensics Firms]]
**Derived from:** [[problems/digital-forensics-firms/high-impact|High Impact]], [[problems/digital-forensics-firms/low-impact-1|Low Impact 1]], [[problems/digital-forensics-firms/low-impact-2|Low Impact 2]], [[problems/digital-forensics-firms/worker-life-1|Worker Life 1]], [[problems/digital-forensics-firms/worker-life-2|Worker Life 2]]

---

## 1. Probabilistic Scope Determination Under Missing Evidence
#bayesian-inference #confidence-intervals #probability-distributions #graph-neural-networks #hypothesis-testing #gradient-boosting #evaluation-metrics #compliance

**Problem statement:** Regulatory notification, contractual obligations and public statements all turn on what the attacker accessed, and the evidence that would establish it was frequently never retained. The determination is made by expert inference under pressure toward certainty.

**ML task:** Given an evidence set, bound the set of systems and data the attacker could have reached and estimate access probability per system, using observed artefacts, known tooling behaviour and the firm's corpus of comparable intrusions
**Input data:** Available artefacts — execution traces, file system metadata, authentication records, network flow summaries, memory where captured; the attacker's tooling and its documented capabilities; the environment's topology and access paths; the firm's corpus of prior intrusions with what was eventually established; the specific evidence gaps present.
**Target:** Access to each system and data store, expressed as a probability with the evidence supporting or failing to exclude it.
**Evaluation metric:** Calibration against the cases where ground truth later emerged — through litigation, subsequent disclosure, attacker leak sites or follow-on investigation — which is the field's only available validation and is not currently collected systematically. The output must partition into established, probable with a stated probability, and cannot be excluded, because the third category is the honest one and currently appears in a limitations section readers skip. Both error directions carry real cost: over-scoping alarms people whose data was unaffected, under-scoping fails people whose data was.
**Scope:** This is more useful as a structured reasoning framework than as a black-box estimate, because the output must be defensible to lawyers, regulators and potentially a court — so the evidence chain behind each probability has to be inspectable. 2-3 ML engineers plus senior responders, 12 months.
**Data availability:** Case corpora exist inside firms and are unstructured. Ground truth is rare and must be deliberately collected when it emerges.

---

## 2. Timeline Reduction and Cross-Source Correlation
#change-point-detection #graph-neural-networks #gradient-boosting #bert #confidence-intervals #time-series-forecasting #evaluation-metrics #automation

**Problem statement:** A parsed timeline runs to millions of events, the investigation concerns dozens, and the sources disagree on format, identity and time. Reduction and correlation are manual and consume most examiner hours in a response.

**ML task:** Establish an environment baseline mid-incident, surface anomalous and pattern-matching events, correlate the same action across sources, and reconcile clock skew with the residual ordering uncertainty carried forward
**Input data:** Parsed events from endpoint telemetry, operating system artefacts, application and authentication logs, network records and cloud audit trails; retained historical data for baselining; known intrusion patterns from the corpus; events observable in multiple sources for skew estimation.
**Target:** The subset of events an experienced examiner marks as investigation-relevant, and correct grouping of multi-source records describing one action.
**Evaluation metric:** Recall on examiner-marked relevant events is the binding constraint — a filter that hides something is unusable in a forensic context, so the design must reduce what is read first while keeping everything available and auditable. Correlation accuracy against manually grouped actions. For clock reconciliation, the important output is the residual uncertainty rather than a point correction, because sequence is what is being established and an unstated misalignment can reverse a causal reading in a report used for a legal determination.
**Scope:** Baselines can be built from retained data even mid-incident and are what make anomaly surfacing possible at all. Everything must be reproducible and documented, since findings may be examined in litigation. 2-3 ML engineers plus forensic examiners, 9-12 months.
**Data availability:** Case data is held under client agreements that vary on secondary use and must be checked before any corpus is built.

---

## 3. Likelihood-Based Attribution With Deception Weighting
#bayesian-inference #confidence-intervals #gradient-boosting #graph-neural-networks #k-nearest-neighbors #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Attribution affects insurance coverage, sanctions exposure and public statements, rests on individually weak signals, and is expressed in verbal confidence language that is applied inconsistently and read variably by the lawyers and insurers who consume it.

**ML task:** Combine attribution signals as likelihood ratios estimated from the corpus, weighted by how easily each can be faked, producing a posterior with a stated range
**Input data:** Tooling, infrastructure, technique combinations, timing, targeting and language artefacts; actor profiles from intelligence sources; the corpus of prior cases with signal sets; known instances of deliberately planted indicators; confirmed attributions from arrests, government statements and leaks.
**Target:** The actor, where confirmation later exists, and the calibrated posterior where it does not.
**Evaluation metric:** Calibration against confirmed cases is the discipline the field lacks entirely — a stated 80% confidence should be right about 80% of the time, and nobody knows whether the verbal conventions come anywhere near that. Weight signals by fakeability explicitly: infrastructure is cheap to mimic, certain build artefacts are not, and a framework treating every signal as honest evidence is exploitable by an adversary who reads the literature. Report what the assessment does and does not support for the specific purpose at hand, since coverage, sanctions and public statement each need a different threshold.
**Scope:** The independence assumptions in combining signals must be stated, because they are frequently violated — actors reuse infrastructure across techniques — and an unstated assumption is how a weak case becomes a confident one. 2 ML engineers plus intelligence analysts, 9-12 months.
**Data availability:** Signal data is available from case work and intelligence vendors. Confirmed attributions are rare and constitute a small validation set.

---

## 4. Pre-Incident Readiness and Evidence Gap Assessment
#graph-neural-networks #gradient-boosting #bayesian-inference #confidence-intervals #time-series-forecasting #evaluation-metrics #compliance #data-integration

**Problem statement:** What can be established after an incident is decided before it, by log retention set on cost grounds, monitoring coverage set on deployment convenience and cloud audit configuration left at defaults — none of which was chosen with the notification decision in view.

**ML task:** Assess an organisation's evidence posture and identify which specific gaps would make a future scope determination unanswerable, naming the systems and data affected
**Input data:** Log retention configuration and actual retained volumes; monitoring coverage across the estate; cloud audit configuration; asset inventory and data location mapping; the firm's corpus of investigations with the gaps that proved decisive; access paths between systems.
**Target:** For each plausible intrusion entry point, whether scope could be determined for the systems and data reachable from it.
**Evaluation metric:** Validate against the corpus retrospectively: for past investigations, would this assessment have predicted the gaps that actually mattered. The useful output is specific rather than a score — this system's logs expire in seven days and it has access to this data store, so an intrusion discovered after a week could not be scoped for that data — because a named consequence changes a retention decision and a maturity rating does not.
**Scope:** This is the highest-value product the industry could sell and it is preventive rather than responsive, which is a different commercial motion for firms structured around incident retainers. It converts a storage cost decision into a notification exposure decision, which is the frame under which it would actually be funded. 2 ML engineers plus senior responders, 6-9 months.
**Data availability:** Configuration data comes from the client; the corpus of which gaps proved decisive sits in firms' case histories, unstructured.
