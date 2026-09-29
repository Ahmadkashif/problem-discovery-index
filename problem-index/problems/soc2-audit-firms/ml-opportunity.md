# Machine Learning Opportunities — SOC 2 & Attestation Audit Firms

**Industry:** [[soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Derived from:** [[problems/soc2-audit-firms/high-impact|High Impact]], [[problems/soc2-audit-firms/low-impact-1|Low Impact 1]], [[problems/soc2-audit-firms/low-impact-2|Low Impact 2]], [[problems/soc2-audit-firms/worker-life-1|Worker Life 1]], [[problems/soc2-audit-firms/worker-life-2|Worker Life 2]]

---

## 1. Full-Population Testing and Exception Detection
#bayesian-inference #confidence-intervals #probability-distributions #hypothesis-testing #gradient-boosting #evaluation-metrics #automation #compliance

**Problem statement:** Testing samples twenty-five items because examining the whole population used to be impossible, and for most of the controls in a modern attestation it no longer is — compliance platforms hold the complete population of change tickets, access reviews and onboarding records continuously.

**ML task:** Test complete populations where the data is machine-readable, detect anomalies across the full record, and report honest bounds where sampling remains necessary
**Input data:** Complete control populations from compliance platform integrations — change approvals, access reviews, provisioning and deprovisioning, backup verifications, configuration states — with timestamps and actors; the control descriptions being tested; historical exception patterns.
**Target:** Whether each instance of the control operated as described, and which instances are anomalous.
**Evaluation metric:** Agreement with auditor judgement on a reviewed subset, and — more importantly — the temporal picture, since full-population testing reveals when a control operated and when it did not, surfacing the three-week gap that sampling averages away. Where sampling remains necessary, report the bound on population failure rate that a clean sample of a given size actually supports, rather than a binary conclusion, because the report format currently conveys coverage where the method supports inference.
**Scope:** Anomaly detection over a complete record is a different capability from sample verification: the useful finding is the change deployed without approval at two in the morning, the access review completed in four seconds, the offboarding three weeks late. This is also the most practical protection an auditor has when a finding is contested — a control that failed eleven times in a quarter is not a one-off. 2 ML engineers plus an audit methodology lead, 6-9 months.
**Data availability:** Excellent and recently so. This capability became possible when compliance platforms industrialised evidence collection, and the practice has not moved.

---

## 2. Scope Completeness Against Discovered Reality
#graph-neural-networks #bert #large-language-models #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #data-integration

**Problem statement:** The audited boundary is drawn in a document the client writes, and a boundary excluding a legacy platform, an acquired estate or a development environment with production data produces a report that is accurate about what it covers and silent about what it does not.

**ML task:** Reconcile the described system boundary against discovered reality, assess the materiality of exclusions through access and data paths, and traverse subservice carve-out chains
**Input data:** The client's system description; external attack surface discovery, cloud organisation structures, DNS, code repositories and identity data; network and access paths between systems; data location mapping; subservice organisations' own attestation reports and their control coverage.
**Target:** Systems and data present in the environment but outside the described boundary, ranked by materiality.
**Evaluation metric:** The output must be specific rather than a score — this system is excluded, it holds this data, it has a network path to these in-scope systems — because a named consequence supports an audit finding and a maturity rating does not. For carve-out traversal, measure whether the subservice report actually covers the controls the client relies on, a chain of inference the mechanism's design assumes readers perform and that in practice nobody does.
**Scope:** This is the audit equivalent of the coverage problem that recurs across every assurance product in this vault, and it is where an attestation's meaning is actually determined. Attack surface discovery tooling exists in the security market and is not part of the audit toolkit. 2 ML engineers, 6-9 months.
**Data availability:** Discovery is largely external and requires no client access; the description and the carve-out reports are supplied.

---

## 3. Auditor Quality Signals From Report Characteristics and Outcomes
#gradient-boosting #survival-analysis #bayesian-inference #confidence-intervals #causal-inference #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** The party paying selects the auditor, the party relying cannot observe quality, and the deliverable is identical either way — so rigour is a cost with no revenue attached and competition runs on price and speed.

**ML task:** Derive observable testing-depth characteristics from reports, and relate auditor identity and those characteristics to subsequent incidents involving in-scope controls
**Input data:** Attestation reports with population sizes, samples tested, testing approach, scope exclusions and exception disposition where disclosed; auditor identity; client characteristics; subsequent disclosed incidents with the controls involved; timing.
**Target:** Incidents involving controls that were in scope of a recent clean attestation.
**Evaluation metric:** Confounding is severe — clients who choose rigorous auditors differ in ways that also reduce incidents — so matched comparison on client characteristics is the minimum bar and effects that do not survive matching should be reported as not surviving it. Disclosed incidents are a biased sample and the bias must be stated. Even a crude result is more than the market has, and the derived testing-depth characteristics are valuable on their own as the comparison mechanism the report format currently prevents.
**Scope:** The structural fix is a reporting convention: population sizes, testing approach, scope exclusions and exception disposition presented as a structured appendix would let two reports be compared and costs nothing but willingness. The demand side is where it could actually start — a large enterprise buyer specifying minimum testing depth rather than the existence of a report would change what firms compete on. 2 ML engineers, 6-9 months.
**Data availability:** Reports are shared under non-disclosure and a corpus could be assembled by a large buyer, an insurer, or an intermediary rather than by a firm.

---

## 4. Evidence Handling and Workpaper Generation
#large-language-models #bert #gradient-boosting #transformers #evaluation-metrics #automation #workflow-orchestration #worker-facing

**Problem statement:** Fieldwork is delivered by junior staff at high utilisation against fixed fees in concentrated busy seasons, and a large share of it is requesting evidence, chasing clients, validating format and writing workpapers over a known set of facts.

**ML task:** Automate evidence request, receipt validation and matching to the control tested, and draft workpapers from the testing actually performed
**Input data:** Control descriptions and evidence requirements; compliance platform integrations supplying evidence directly; client-supplied documents in varied formats; testing performed and its results; workpaper templates and prior engagements; engagement budgets and actual hours.
**Target:** Correctly matched and validated evidence, and workpapers a reviewing manager accepts without substantive rework.
**Evaluation metric:** Reviewer acceptance without substantive edit, and hours returned per engagement. The more important secondary measure is where those hours go: the point is to move associate time from evidence handling to judgement work — assessing whether a control addresses the risk, examining the environment, following up exceptions — which is how the profession builds the senior auditors it needs and is what has thinned as platforms took over evidence collection.
**Scope:** Measuring testing depth per engagement and reporting it internally is the adjacent change that matters most: budget pressure currently resolves into less testing, invisibly, decided by the most junior person under deadline. Making it a measured quantity moves the trade to a partner making a stated choice. 2 ML engineers, 4-6 months.
**Data availability:** Complete within any audit firm's engagement records.
