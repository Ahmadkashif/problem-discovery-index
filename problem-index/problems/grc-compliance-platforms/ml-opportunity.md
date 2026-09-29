# Machine Learning Opportunities — GRC & Compliance Platforms

**Industry:** [[grc-compliance-platforms|GRC & Compliance Platforms]]
**Derived from:** [[problems/grc-compliance-platforms/high-impact|High Impact]], [[problems/grc-compliance-platforms/low-impact-1|Low Impact 1]], [[problems/grc-compliance-platforms/low-impact-2|Low Impact 2]], [[problems/grc-compliance-platforms/worker-life-1|Worker Life 1]], [[problems/grc-compliance-platforms/worker-life-2|Worker Life 2]]

---

## 1. Relating Control Quality to Incident Outcomes
#causal-inference #survival-analysis #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Frameworks are consensus documents produced by committee and never validated against incident data, while a large apparatus of procurement, insurance and budget allocation treats certification as an assurance signal. The platforms hold continuous control state across tens of thousands of organisations and use it to render dashboards.

**ML task:** Estimate the relationship between control implementation quality and observable security incidents, controlling for organisational maturity
**Input data:** Continuous control state with configuration detail across the customer base; organisation covariates — size, sector, technology estate, security spend proxies; observable incidents from disclosure requirements, public breach reporting, insurance claims where a partner will share, and customer-reported incidents; time.
**Target:** Incident occurrence and severity, as a function of control quality.
**Evaluation metric:** The sample bias must be stated in every result, not buried: disclosed incidents are the largest and most embarrassing ones, so any estimate is conditioned on a non-random observation process. Confounding is severe — organisations that implement controls well differ systematically in ways that also reduce incidents — so matched comparison on maturity proxies is the minimum bar, and effects that do not survive matching should be reported as not surviving it. Report per control, because the valuable finding is likely to be that some predict nothing.
**Scope:** Control quality rather than presence is the informative variable and the one the binary certification framing discards: the platform can see whether an access review was genuine or a bulk approval, whether scanning covers the estate or a subset, whether multi-factor authentication is enforced or merely available. Insurers hold claims data and a direct interest, which makes them the natural partner for the outcome half. 3 ML engineers plus a causal specialist and an insurance partner, 12-18 months.
**Data availability:** Control state is complete and unique to the platforms. Incident outcomes are scarce, sensitive and biased, and this is permanent rather than temporary.

---

## 2. Framework Mapping From Implemented Controls
#bert #transformers #contrastive-learning #word-embeddings #large-language-models #graph-neural-networks #evaluation-metrics #compliance

**Problem statement:** Organisations pursue several overlapping frameworks and reconcile them with hand-maintained crosswalks that go stale at every revision, while the mapping that matters — from this organisation's actually-implemented controls to each framework's requirements — is left to the customer.

**ML task:** Map an organisation's own control set to framework requirements with a confidence and a rationale, and generate revision diffs expressed in the organisation's terms
**Input data:** The organisation's implemented controls with configuration and exceptions; framework requirement text across versions; published crosswalks and community mappings; historical auditor acceptance and challenge of specific mappings; enterprise customers' bespoke contractual requirements.
**Target:** Whether an auditor accepts that a given control satisfies a given requirement.
**Evaluation metric:** Auditor acceptance is the ground truth and it exists in every platform's audit history. Confidence must be reported rather than implied: some mappings are unambiguous and some are arguable, and treating them identically hides where certified coverage rests on an interpretation that could be rejected. Measure revision handling by whether the diff correctly identifies which of the organisation's controls and evidence are affected — a notification that a revision occurred is what exists today and is not the same thing.
**Scope:** Customer contractual requirements are the unserved case: enterprise buyers impose bespoke security terms that overlap the frameworks heavily and are mapped by nobody, so the same requirement is satisfied repeatedly without anyone recognising it. 2 ML engineers, 6-9 months.
**Data availability:** Framework text is public; the organisation's controls are in the platform; auditor acceptance history is in the platform and is the label set nobody has assembled.

---

## 3. Coverage Estimation and Integration Health
#change-point-detection #time-series-forecasting #graph-neural-networks #gradient-boosting #confidence-intervals #evaluation-metrics #data-integration #compliance

**Problem statement:** Continuous monitoring reports a control passing over whatever the platform can see, and an integration connected to one cloud account in an organisation with fourteen reports on one account — with nothing in the interface distinguishing full coverage from partial.

**ML task:** Estimate what share of the estate each control is actually evaluated over, detect silent integration degradation, and reconcile connected assets against independently discovered ones
**Input data:** Integration evidence volumes over time per source; cloud organisation structures, DNS records, device inventories and code hosting for independent estate discovery; connected account and resource inventories; credential and permission change events; exception records with justification and expiry.
**Target:** Coverage as a fraction of the discoverable estate, and whether an integration's evidence stream is consistent with its own history.
**Evaluation metric:** Detection lead time on historical integration failures, against the current mechanism, which is noticing during an audit. False alarms must be rare enough that alerts are read, which means modelling legitimate change — a deprecated resource, a planned account closure — rather than thresholding volume. For coverage, the measure is how much estate the reconciliation finds that nobody had connected, which is the number that would most change how these reports are read.
**Scope:** Making coverage a first-class reported quantity, so passing on partial coverage looks different from passing on full coverage, is a presentation decision as much as a technical one and would surface a great deal of currently invisible risk. Exception lifecycle belongs here too: an exception renewed four times is a permanent posture misdescribed as temporary. 2 ML engineers, 4-6 months.
**Data availability:** Complete within the platform, plus public and customer-authorised discovery sources.

---

## 4. Grounded Questionnaire Response From the Evidence Corpus
#large-language-models #bert #transformers #contrastive-learning #k-nearest-neighbors #confidence-intervals #evaluation-metrics #automation

**Problem statement:** Every enterprise customer sends a security questionnaire covering ground the certification already covers, the answers are contractual representations, and they are produced at speed by the most expensive technical people on a deal deadline.

**ML task:** Match incoming questions semantically to a maintained answer library and to the platform's own control and policy evidence, generating grounded answers with the supporting evidence linked
**Input data:** Incoming questionnaires in customer formats; the organisation's control state, configuration detail and policy documents; a curated library of previously approved answers with their evidential basis; changes to controls and policies over time.
**Target:** An answer the organisation's security lead would approve, supported by specific evidence.
**Evaluation metric:** Approval rate without edit is the productivity measure, and the safety measure is more important: the rate at which a generated answer is contradicted by the organisation's own control state. A fluent wrong answer on a contractual document is worse than a blank, so the system must defer explicitly where the evidence does not support a confident answer rather than producing plausible text. Measure library drift too — answers whose evidential basis has changed since approval, which is how a library decays into inaccurate representations.
**Scope:** The structural fix is a continuously-updated trust centre that customers self-serve, and its adoption depends on enterprise procurement accepting it — a market coordination problem the platforms are far better placed to push than any individual vendor. Measuring how often answered representations diverge from actual control state is a risk nobody currently quantifies. 2 ML engineers, 6-9 months.
**Data availability:** Control state and policies are in the platform; the answer library exists in spreadsheets and past responses.
