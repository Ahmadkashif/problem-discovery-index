# Machine Learning Opportunities — Contract Lifecycle Platforms

**Industry:** [[contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Derived from:** [[problems/contract-lifecycle-platforms/high-impact|High Impact]], [[problems/contract-lifecycle-platforms/low-impact-1|Low Impact 1]], [[problems/contract-lifecycle-platforms/low-impact-2|Low Impact 2]], [[problems/contract-lifecycle-platforms/worker-life-1|Worker Life 1]], [[problems/contract-lifecycle-platforms/worker-life-2|Worker Life 2]]

---

## 1. Back Catalogue Obligation Extraction at Scale
#large-language-models #bert #transformers #word-embeddings #transfer-learning #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** A company's binding obligations sit in thousands of executed agreements nobody has read since signature. Every CLM implementation manages new contracts and declares the back catalogue out of scope, which is precisely where the surprises come from — in diligence, in a pricing decision, in a regulatory response.

**ML task:** Clause identification and structured extraction across a heterogeneous executed estate, with calibrated confidence driving a review triage
**Input data:** Executed agreements across counterparty paper and own templates; existing manually captured metadata as partial labels; clause libraries and playbook definitions; counterparty identity and agreement value; amendments and side letters that modify the base agreement.
**Target:** Presence, location and operative content of the high-consequence clause set — change of control, exclusivity, most-favoured-nation, auto-renewal and notice, indemnity and liability caps, data commitments, termination rights.
**Evaluation metric:** Recall on the high-consequence clause set is the binding constraint, since a missed exclusivity clause is a material misstatement of the company's position. Report calibration explicitly — a legal team will accept an honest 80% confidence flagged for review and will discard the entire dataset after finding two confident errors. Amendment reconciliation should be evaluated separately because it is where silent errors concentrate.
**Scope:** The precision requirement is unusual and shapes everything: the deliverable is a searchable estate with honest uncertainty, not a perfect dataset. Prioritising a small high-consequence clause set makes the project affordable, and targeting review at high-value agreements and low-confidence extractions is what keeps the cost defensible. Amendments and side letters modifying base agreements are the most commonly botched aspect and must be handled as first-class objects. 3 ML engineers plus contract counsel, 6-8 months.
**Data availability:** Executed estates are large and held by customers. Labelled clause data exists in the more mature CLM deployments and in academic corpora such as CUAD, which is a useful starting point but far narrower than production requires.

---

## 2. Playbook Achievability from Executed Outcomes
#hypothesis-testing #logistic-regression #gradient-boosting #bert #confidence-intervals #descriptive-statistics #evaluation-metrics

**Problem statement:** Playbooks state what positions are acceptable, are authored from senior counsel's judgement, and drift from what the company actually signs. Nobody compares the stated position against the executed reality, so a company can operate for years on guidance it abandoned in practice.

**ML task:** Comparison of extracted executed terms against playbook positions, plus estimation of acceptance probability per position conditional on counterparty and deal characteristics
**Input data:** Playbook positions and fallbacks with effective dates; extracted terms from executed agreements; negotiation history including initial position, rounds and final term; counterparty industry, size and prior relationship; deal value and urgency; which lawyer negotiated.
**Target:** The final executed position relative to the playbook's stated preference, and whether a given position was ultimately conceded.
**Evaluation metric:** Calibration of achievability estimates against held-out negotiations — a junior lawyer deciding whether to hold a position needs a trustworthy probability, not a ranking. Report per-position drift rates as a descriptive deliverable, since that report alone is new to almost every legal department and requires no prediction at all.
**Scope:** Confounding is substantial: positions are conceded on deals that mattered commercially, so raw acceptance rates understate what is achievable in ordinary negotiations. Conditioning on deal urgency and value is essential and imperfect. Cross-customer benchmarking is the platform's unique asset and is a considerably better market signal than the published-agreement benchmarks legal publishers sell, which cover only filed public contracts. 2 ML engineers plus legal operations, 5 months.
**Data availability:** Negotiation history is captured well in CLM deployments where negotiation happens in the system and is absent where it happens over email attachments, which is still common.

---

## 3. Clause Absence Detection in Third-Party Paper
#large-language-models #bert #transformers #word-embeddings #gradient-boosting #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** Automated contract review checks the terms that are present. The risky term in a counterparty's paper is frequently the one that is absent — no limitation of liability, no termination for convenience, no data protection terms, no cap on renewal increases — and an absent clause appears in no extraction output.

**ML task:** Modelling the expected clause set for an agreement type and context, and detecting significant omissions; plus contextual risk scoring of findings
**Input data:** Agreement type, counterparty, value, subject matter and data involved; the company's own executed agreements of the same type; the vendor's cross-customer corpus of comparable agreements; playbook requirements; regulatory context; historical findings and how senior counsel prioritised them.
**Target:** Omissions that counsel subsequently raised in negotiation, and the priority they assigned to each finding.
**Evaluation metric:** Recall on omissions counsel considered material — a missed absent liability cap is the failure this exists to prevent. For risk calibration, agreement with the priority experienced counsel assigned, since the current tooling's failure is listing everything equally rather than missing things.
**Scope:** Defining the expected clause set is the substantive work and comes from three sources: the company's own agreements, its playbook, and what is typical for this agreement type across the vendor's corpus. Contextual risk — value, data sensitivity, regulatory exposure — is what turns a list into a prioritised one and is where every experienced lawyer already operates instinctively. 2-3 ML engineers plus in-house counsel, 5-6 months.
**Data availability:** Cross-customer agreement corpora exist inside the vendors and are subject to confidentiality terms that must be checked carefully before any cross-customer modelling.

---

## 4. Legal Request Classification and Risk-Based Routing
#gradient-boosting #bert #large-language-models #word-embeddings #cross-validation #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** A routine NDA on the company's own template and a master agreement with an uncapped indemnity arrive in the same inbox as attachments with a sentence of context. Legal operations distinguishes them by opening and reading, and the defensive response — escalate everything — makes legal the bottleneck the business complains about.

**ML task:** Classification of request type and required review level from the attached document, plus prediction of whether senior review will change anything
**Input data:** Attached agreements with extracted type, counterparty, value, paper ownership and present or absent clauses; requester and business unit; historical routing decisions; which agreements senior counsel actually edited and how substantially; turnaround times and escalation history; existing agreements with the same counterparty.
**Target:** The review level ultimately required, measured by whether senior counsel materially changed the document.
**Evaluation metric:** The critical measure is missed-escalation rate — a dangerous agreement routed to self-service is the failure that ends the programme, so recall on genuinely high-risk agreements must be very high and the threshold set accordingly. Report the proportion of volume safely self-served at that recall, which is the efficiency actually delivered.
**Scope:** Duplicate and existing-relationship detection needs no modelling and catches a surprising share of requests concerning counterparties the company already has agreements with. The self-service path only works if legal trusts it, which means the model must be tuned conservatively and its errors must be visible rather than silent. 2 ML engineers plus legal operations, 4-5 months.
**Data availability:** Routing history and edit history are captured in CLM deployments. Requests arriving by email outside the system are invisible, which is a meaningful share at most companies and biases the training data toward the already-governed flow.
