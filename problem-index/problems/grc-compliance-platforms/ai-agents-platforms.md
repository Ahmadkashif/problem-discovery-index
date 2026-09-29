# AI Agents & Platform Opportunities — GRC & Compliance Platforms

**Industry:** [[grc-compliance-platforms|GRC & Compliance Platforms]]

---

## 1. Evidence-Based Control Platform
#ai-platform #causal-inference #survival-analysis #bayesian-inference #confidence-intervals #gradient-boosting #compliance #evaluation-metrics

**Concept:** A platform that asks what its own product buys. It scores control quality rather than control presence — whether an access review was a genuine review or a bulk approval, whether scanning covers the estate or a subset, whether multi-factor authentication is enforced or merely available — and relates that to observable incident outcomes across a large customer base, in partnership with insurers who hold claims data and a direct interest in the answer. It reports the sample bias in every result rather than burying it, because disclosed incidents are the largest and most embarrassing ones and any estimate is conditioned on that.

**Inputs:** Continuous control state with configuration detail across the customer base; organisation covariates for matching; disclosed breaches, insurance claims where a partner shares them, and customer-reported incidents.

**Outputs / Actions:** Per-control estimates of association with incident outcomes, matched on maturity, with effects that do not survive matching reported as not surviving it. A control quality score that distinguishes implemented from implemented well — the informative variable that binary certification discards. And the uncomfortable finding published if it is found: if some controls predict nothing, saying so would be the most valuable contribution this category could make, and would position the platform that says it as the one making evidence-based recommendations while competitors sell checklists.

**Why now:** Insurers have begun building this internally because they carry the losses, which means the analysis is going to be done by someone — and a platform holding control state plus an insurer holding claims can do together what neither can alone.

**Market:** Compliance platforms, cyber insurers pricing on certification, enterprise buyers gating purchases on it, and the security leaders currently allocating budget toward what gets certified rather than toward what works.

---

## 2. Evidence and Coverage Operations Agent
#ai-agent #change-point-detection #graph-neural-networks #time-series-forecasting #gradient-boosting #large-language-models #workflow-orchestration #worker-facing

**Concept:** An agent that makes continuous monitoring mean what it claims and removes the chasing from the compliance manager's week. It reports coverage as a first-class quantity — this control is passing across nine of your fourteen accounts — so partial coverage no longer looks like full coverage. It reconciles connected assets against independently discovered ones from cloud organisation structures, DNS, device inventories and code hosting, finding the accounts and repositories nobody connected. It monitors each integration's evidence volume against its own history, catching the silent degradation that error monitoring misses. And it forecasts which evidence items will still be outstanding at the audit date, two months out.

**Inputs:** Integration evidence streams and volumes; estate discovery sources; connected inventories; credential and permission changes; exception records with justification and expiry; each team's historical response time to evidence requests.

**Outputs / Actions:** Coverage-qualified control status. Discovered-but-unconnected estate. Integration degradation alerts that distinguish a legitimate resource change from a broken connection. An audit-period forecast that converts a crisis into a schedule. Requests routed with exactly what is needed, why, the deadline and a one-click path, in the tool the engineer already uses — and checked first against evidence that already exists elsewhere, which removes a share of requests entirely. Exception lifecycle surfaced, since an exception renewed four times is a permanent posture misdescribed as temporary.

**Why now:** The automated compliance model's credibility rests on evidence being continuous and complete, and it is quietly neither — a gap that auditors rarely probe and that persists through certification.

**Market:** Automated compliance platforms, enterprise GRC vendors, and the compliance managers who currently spend their week asking people for things with no authority and a fixed deadline.

---

## 3. Trust Centre and Questionnaire Agent
#ai-agent #large-language-models #bert #contrastive-learning #k-nearest-neighbors #confidence-intervals #automation #worker-facing

**Concept:** An agent for the largest unpriced cost in enterprise software sales. It matches incoming questions semantically to a maintained answer library — the same question in forty wordings is one question — and grounds each answer in the platform's own control state, configuration detail and policy documents, with the supporting evidence linked. Where the evidence does not support a confident answer it defers explicitly rather than producing plausible text, because these are contractual representations and a fluent wrong answer is worse than a blank. It maintains the library as a living artefact, flagging answers whose evidential basis has drifted since approval.

**Inputs:** Incoming questionnaires in customer formats; control state, configuration and policies; the approved answer library with each answer's evidential basis; control and policy change history; published trust centre content.

**Outputs / Actions:** Drafted answers with evidence links for approval rather than composition. Explicit deferral where evidence is insufficient. Library drift alerts that prevent slow decay into inaccurate representations. A measurement nobody currently takes: how often an answered representation is contradicted by the organisation's own control state, which is a live contractual risk created by doing this work at speed for the fortieth time. And a continuously-updated trust centre that customers self-serve — the structural fix, whose adoption depends on enterprise procurement accepting it, which is a coordination problem the platforms can push and an individual vendor cannot.

**Why now:** The promise of standardised frameworks was that an attestation would replace bespoke enquiry, and procurement asks anyway — so the cost has stayed and landed on the most expensive technical people at the least convenient moments.

**Market:** Every company selling software to enterprises, the compliance platforms already holding the evidence, and the enterprise procurement functions sending questionnaires that a trust centre would answer better.
