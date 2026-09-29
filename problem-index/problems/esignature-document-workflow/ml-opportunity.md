# Machine Learning Opportunities — E-Signature & Document Workflow

**Industry:** [[esignature-document-workflow|E-Signature & Document Workflow]]
**Derived from:** [[problems/esignature-document-workflow/high-impact|High Impact]], [[problems/esignature-document-workflow/low-impact-1|Low Impact 1]], [[problems/esignature-document-workflow/low-impact-2|Low Impact 2]], [[problems/esignature-document-workflow/worker-life-1|Worker Life 1]], [[problems/esignature-document-workflow/worker-life-2|Worker Life 2]]

---

## 1. Envelope Completion Prediction and Stall Diagnosis
#survival-analysis #gradient-boosting #logistic-regression #bert #confidence-intervals #feature-engineering #cross-validation #evaluation-metrics #revenue-impact

**Problem statement:** A meaningful share of agreements sent for signature never complete, after the commercial negotiation is finished — the most expensive place to lose a deal. The platform observes the whole funnel, including highly diagnostic behaviour like an envelope opened six times and never signed, and reports it identically to one nobody opened.

**ML task:** Survival modelling of time to completion with competing risks (signed, declined, abandoned), plus classification of stall cause from behavioural traces
**Input data:** Envelope metadata — routing depth and order, signer roles, agreement type and value, page count, send timing; recipient behaviour with page-level dwell, open counts, forwarding events and device; whether each signer has signed with this sender before; document content features for terms that historically trigger review; historical outcomes.
**Target:** Completion within a horizon, and the stall cause where one can be established from subsequent sender action.
**Evaluation metric:** Calibration of completion probability at send time is what makes the pre-send warning useful — a poorly calibrated warning is ignored within a week. For diagnosis, precision per cause class, since each triggers a different and costly remedy. The business metric is recovered completion rate under intervention, which needs a holdout to measure honestly.
**Scope:** Page-level dwell before abandonment is the sharpest available signal about which clause is the obstacle and is collected by every platform without being used. Much of the stall happens outside the system — the recipient forwarded it to their legal team — which caps achievable diagnosis and should be acknowledged rather than modelled around. Signer authority prediction, whether this person can sign this agreement at this value, is separable and is the single highest-value fix. 2-3 ML engineers, 5-6 months.
**Data availability:** Excellent — envelope and behavioural traces are complete across millions of transactions and many industries. Stall cause labels do not exist and must be derived from sender remedial actions, which is noisy.

---

## 2. Template Clause Drift Detection Against the Approved Library
#bert #word-embeddings #large-language-models #dbscan #k-means-clustering #evaluation-metrics #compliance

**Problem statement:** Clause libraries hold approved language and templates hold copies of it, and nothing compares the copies against the library. Legal updates a limitation clause in the two templates it knows about, and the version sales sends four hundred times a month still carries language the company believes it retired.

**ML task:** Semantic clause matching and divergence detection between template text and the approved library, plus near-duplicate template clustering
**Input data:** Template corpus with version history and send volumes; approved clause library with effective dates; executed documents as sent; clause-level edit history; legal approval records.
**Target:** Templates containing clauses that materially diverge from the current approved language, ranked by exposure.
**Evaluation metric:** Recall on materially divergent clauses as adjudicated by counsel — a missed retired indemnity is the failure with consequence, while a flagged trivial rewording costs a moment. Weight by send volume, since the same stale clause carries very different exposure in a rarely used template than in the one sales sends daily.
**Scope:** Divergence is semantic rather than textual, since clauses are lightly edited when pasted, so an entailment-style comparison is required rather than diffing. Usage weighting is the prioritisation that makes the output actionable and requires only a join the platforms have never made. Inducing the template that should exist, from clusters of documents users edited the same way repeatedly, is the constructive complement. 2 ML engineers plus contract counsel, 4-5 months.
**Data availability:** Templates, send volumes and executed documents are all held by the platform. Approved clause libraries with effective dates exist at sophisticated customers and are absent at most, which limits where this can be deployed initially.

---

## 3. Risk-Based Identity Assurance Selection
#gradient-boosting #logistic-regression #graph-neural-networks #confidence-intervals #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Verification strength is a global setting, almost always the weak one, because every stronger option reduces completion rate. High-value transactions therefore carry the same assurance as policy acknowledgements, at a time when business email compromise makes email control an inadequate proof of identity.

**ML task:** Risk scoring per envelope and per signature attempt, driving a step-up decision, with the attack pattern component modelled relationally across customers
**Input data:** Envelope value, type and counterparty; the sender organisation's historical signing patterns; signer history and email domain age; routing anomalies; device, network and geolocation at signature attempt; timing relative to holidays and business hours; confirmed fraud events across the platform's customer base.
**Target:** Confirmed fraudulent or repudiated signature.
**Evaluation metric:** Precision at the step-up threshold, since every step-up costs completion and false positives are paid for in lost revenue. Report the completion cost per prevented fraud, which is the trade-off the customer is actually making and currently makes blindly with a global setting. Recall on confirmed fraud is the secondary measure and is limited by how few events are ever confirmed.
**Scope:** Cross-customer attack pattern signal is the platform's unique advantage and the reason this cannot be built by any individual company. Step-up at signature attempt rather than at send is the architectural change that matters, since the risk signals — device, network, timing — are only observable then. Confirmed fraud labels are extremely scarce, so the practical approach is anomaly detection against the organisation's own signing patterns supplemented by the few confirmed cases. 2-3 ML engineers plus a fraud specialist, 5-6 months.
**Data availability:** Behavioural and envelope data is complete. Fraud confirmation is rare, late and under-reported because organisations do not publicise it, which is the binding constraint on supervised approaches.

---

## 4. Executed Agreement Term Extraction and Obligation Calendaring
#large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance #automation

**Problem statement:** Executed agreements become PDFs that someone reads to type parties, dates, terms, renewal mechanisms and notice periods into a register, incompletely, under deadline pressure that has already passed. The omitted field is usually the notice period, which is the one that later causes an unwanted auto-renewal.

**ML task:** Structured extraction of agreement metadata and obligations from executed documents, with dated obligation generation
**Input data:** Executed agreement PDFs with their template lineage where known; historical manually entered register records as labels; clause libraries; counterparty history; the sending organisation's standard terms.
**Target:** The register fields as ultimately confirmed, and the set of dated obligations with their trigger dates.
**Evaluation metric:** Field-level accuracy with notice period, renewal mechanism and effective date weighted most heavily, since those are both the highest-consequence and the most frequently omitted. Auto-renewal events prevented is the business metric and is directly countable.
**Scope:** Template lineage makes this substantially easier where the document came from a known template — most fields are in known positions — and the hard cases are third-party paper. Notice period and renewal mechanism should route to human review regardless of confidence, because the cost asymmetry justifies it. Flagging non-standard terms before signature rather than after is a separable and more valuable use of the same extraction. 2 ML engineers plus a contract administrator, 4-5 months.
**Data availability:** Executed documents are complete in the platform. Manually entered register records exist in customer systems, often spreadsheets, and must be obtained per customer to serve as labels.
