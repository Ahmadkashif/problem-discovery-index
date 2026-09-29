# Machine Learning Opportunities — Privacy Tech Vendors

**Industry:** [[privacy-tech-vendors|Privacy Tech Vendors]]
**Derived from:** [[problems/privacy-tech-vendors/high-impact|High Impact]], [[problems/privacy-tech-vendors/low-impact-1|Low Impact 1]], [[problems/privacy-tech-vendors/low-impact-2|Low Impact 2]], [[problems/privacy-tech-vendors/worker-life-1|Worker Life 1]], [[problems/privacy-tech-vendors/worker-life-2|Worker Life 2]]

---

## 1. Consent Comprehension and Design Risk Measurement
#causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #cnns #gradient-boosting #evaluation-metrics #compliance

**Problem statement:** Consent interfaces are optimised for acceptance and measured on it, while the standard they must satisfy is informed, specific and freely given — and comprehension is measured by nobody. Regulators have ruled repeatedly on interface mechanics, producing an adaptation cycle rather than a change in substance.

**ML task:** Estimate comprehension from a sampled user panel, and score interface configurations automatically against the accumulated body of regulatory decisions
**Input data:** Rendered consent interfaces with layout, relative prominence, click-depth asymmetry between accept and reject, default states, bundling and pre-selection; interaction telemetry including dwell time and expansion of detail; sampled post-hoc survey responses on what users believe they agreed to; the recorded consent; the corpus of published regulatory decisions and the designs they concerned.
**Target:** Whether a user's belief about what they agreed to matches what was recorded, and whether a configuration resembles designs regulators have found non-compliant.
**Evaluation metric:** Comprehension is measured against the sampled survey and must be reported as an estimate with its sampling error, not as a score. For design risk, calibrate against actual enforcement outcomes where the design is known, and report which specific properties drive the assessment so a customer can act on it. The two numbers should be reported together with acceptance rate — a platform reporting all three changes what customers can buy on, and is the only party in the chain with an interest in the second and third.
**Scope:** The incentive conflict is explicit rather than implicit: vendors compete partly on acceptance rates, and a vendor optimising for informed choice reports lower acceptance and loses deals. This is very likely a product for a new entrant or for a regulator-facing service rather than for an incumbent. 2 ML engineers plus a survey methodologist, 6-9 months.
**Data availability:** Interface and interaction data is held by the vendors. Comprehension data does not exist and must be collected, which is cheap and has not been done because the finding would be unwelcome.

---

## 2. Context-Based Personal Data Classification
#bert #transformers #gradient-boosting #graph-neural-networks #dbscan #confidence-intervals #evaluation-metrics #data-integration

**Problem statement:** The foundational record of where personal data lives is a survey plus a partial scan, and classification by pattern matching cannot tell a national identifier from any other nine-digit number, or a customer name column holding companies from one holding people.

**ML task:** Classify fields and documents as personal data using surrounding schema, table relationships, sample values and downstream usage, across structured, semi-structured and unstructured stores
**Input data:** Schemas, sample values and table relationships; query and pipeline usage of each field; document and object stores including ticketing systems, support transcripts and shared drives; existing labelled classifications and their corrections; jurisdictional definitions of personal and special-category data.
**Target:** Whether a field or document contains personal data of a given category, as adjudicated by a privacy reviewer.
**Evaluation metric:** Precision and recall reported separately per data category, since the costs differ sharply — missing special-category data is a materially worse error than missing an email address, and an aggregate score hides it. Coverage must be reported as a first-class number: a scan reaching forty percent of the estate should say so, and presenting a partial scan as an inventory is the same failure that runs through every assurance product in this cluster. Measure specifically on the unstructured estate, where the real exposure sits and where tooling designed for databases performs worst.
**Scope:** Context beats pattern and is what makes the long tail tractable. 2-3 ML engineers, 6-9 months.
**Data availability:** Access to customer data stores under contract, with all the handling constraints that implies — a classification system operating on personal data is itself a processing activity and must be designed accordingly.

---

## 3. Data Flow Inference From Observed System Behaviour
#graph-neural-networks #change-point-detection #gradient-boosting #bert #dbscan #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** A data map is a graph of movements and is compiled by asking people to describe them. The movements are observable — in query logs, pipeline definitions, integration configurations, network egress, application code and browser behaviour — and reconciling observed against declared is the capability that would turn a survey into a measurement.

**ML task:** Infer the personal data flow graph from system behaviour, reconcile it against the declared register, and detect what actually leaves to third parties
**Input data:** Query and access logs; pipeline and transformation definitions; integration configurations; network egress and cloud flow data; application code and dependency graphs; rendered browser behaviour on the organisation's own properties including tag loading sequence relative to consent state; the declared processing register and vendor list.
**Target:** The set of actual data movements, including destinations absent from the register.
**Evaluation metric:** The operative measure is discrepancy volume — how many flows and destinations the inference finds that the register does not contain — which is the number that would most change how these records are read. For browser-side observation, the specific check is consent-conditioned behaviour: whether a tag fires before consent and whether rejecting actually stops it, which are common failures, are precisely what enforcement has turned on, and are almost never detected by the organisation itself. Report confidence per inferred flow, since an inferred edge asserted without evidence is no better than a declared one.
**Scope:** Browser-side observation is straightforward and immediately valuable; server-side flows are the harder half and share their machinery with item 2, which makes these one programme. Subcontracting chains — a vendor's own processors, disclosed contractually and never verified — are only detectable from observed behaviour. 3 ML engineers, 9-12 months.
**Data availability:** Logs, configurations and egress data exist inside customers; browser behaviour is observable externally with no access required.

---

## 4. Deletion Reach and Coverage Verification
#graph-neural-networks #gradient-boosting #confidence-intervals #large-language-models #change-point-detection #evaluation-metrics #compliance #worker-facing

**Problem statement:** Fulfilment is orchestrated across connected systems and routed to engineers for everything else — warehouses with no deletion path, immutable backups, logs never meant to be queried by person, training sets and the models fitted on them — and recorded as complete with the coverage unstated.

**ML task:** Derive the set of systems a person's data actually reached from the flow graph, verify deletion where verification is possible, and report coverage explicitly
**Input data:** The inferred flow graph from item 3; identifier propagation through derived tables, views and exports; system deletion capabilities and retention configurations; backup and log architectures; third-party processor request mechanisms; historical fulfilment records and the scripts used.
**Target:** The set of locations holding the subject's data, and confirmed removal from each.
**Evaluation metric:** Coverage reported as a partition — reached, partially reached, excluded with reason — rather than as a binary confirmation, which is the current practice and overstates the position. Verification where possible is the stronger claim: re-querying after deletion is checkable for many stores and is rarely done. Measure recurring engineering hours per request across a year, because that is the number that justifies building deletion as a platform capability and is recorded nowhere.
**Scope:** Model unlearning is unsolved in the general case and should be handled as stated policy — retention limits on training data, retraining cadence, documented limitations — rather than improvised per request by an engineer. The honest coverage report is uncomfortable and is the precondition for prioritising the architectural fix. 2 ML engineers plus data platform engineering, 6-9 months.
**Data availability:** Depends on the flow graph from item 3; fulfilment history exists as tickets and scripts.
