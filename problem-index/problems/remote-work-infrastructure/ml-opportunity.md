# Machine Learning Opportunities — Remote Work Infrastructure

**Industry:** [[remote-work-infrastructure|Remote Work Infrastructure]]
**Derived from:** [[problems/remote-work-infrastructure/high-impact|High Impact]], [[problems/remote-work-infrastructure/low-impact-1|Low Impact 1]], [[problems/remote-work-infrastructure/low-impact-2|Low Impact 2]], [[problems/remote-work-infrastructure/worker-life-1|Worker Life 1]], [[problems/remote-work-infrastructure/worker-life-2|Worker Life 2]]

---

## 1. Regulatory Change Monitoring With Exposure Linkage
#bert #large-language-models #change-point-detection #graph-neural-networks #gradient-boosting #confidence-intervals #compliance #evaluation-metrics

**Problem statement:** Employment, tax and benefit rules across sixty jurisdictions are maintained by specialists reading official sources in local languages, so guidance is current where attention has recently fallen and of unknown vintage elsewhere — and nobody can say which entries are stale.

**ML task:** Ingest official legislative, regulatory and case law sources across jurisdictions, detect and classify relevant changes, and link each change to the rule entries, determinations, clients and payroll calculations it affects
**Input data:** Official publication sources per jurisdiction with their formats and languages; the internal rule base with entry structure and verification dates; determinations and the rules they relied on; client engagements and payroll configurations dependent on each rule; historical changes and what they affected.
**Target:** Whether a published change is materially relevant to a maintained rule, and which downstream entries and engagements it affects.
**Evaluation metric:** Recall on material changes is the governing metric, because a missed change produces a wrong determination that surfaces years later as a liability — false positives cost a specialist a few minutes of review and are the acceptable side of the trade. Measure detection lead time against when the change was actually incorporated under the manual process, which for jurisdictions outside recent attention is frequently long. The exposure linkage is what converts a detected change into a remediation list and is where the operational value concentrates.
**Scope:** Multilingual legal text across heterogeneous publication formats is the hard engineering, and the output is a review queue rather than an automated rule update — legal judgement remains required and the system's role is to ensure it is applied to the right things in time. 3 engineers plus compliance specialists, 9-12 months.
**Data availability:** Official sources are public with highly variable structure; the internal rule base and its dependency structure exist and are rarely modelled explicitly.

---

## 2. Fact-Based Classification and Permanent Establishment Risk Assessment
#gradient-boosting #bayesian-inference #confidence-intervals #graph-neural-networks #hypothesis-testing #evaluation-metrics #compliance #bert

**Problem statement:** Classification tests apply to how an engagement actually operates — control, exclusivity, integration, tools, hours — and the platform generally sees only what the contract says, so an arrangement papered as contracting and operated as employment passes a paperwork check and fails the legal test.

**ML task:** Assess classification risk and permanent establishment exposure from structured engagement facts against each jurisdiction's test, producing a continuously updated risk position rather than a one-time determination
**Input data:** Structured engagement facts — control arrangements, exclusivity, integration into the client's organisation, equipment, working hours, duration, payment structure; role description and authority; client headcount and activity by country; jurisdictional tests and thresholds; historical disputes and their outcomes.
**Target:** Classification and permanent establishment risk, validated against the outcomes of actual authority challenges the platform has handled.
**Evaluation metric:** Dispute outcomes are the only empirical validation available and are scarce, so this must be reported as a risk position with explicit uncertainty rather than as a determination. The useful output is the distribution — which engagements sit near a threshold and which are clearly on one side — and the honest property is that the system will sometimes return uncomfortable answers about arrangements a client wants, which is the entire point of assessing facts rather than paperwork.
**Scope:** Capturing the facts is the precondition and requires asking questions the current onboarding does not, some of which clients will not want to answer accurately. Permanent establishment exposure should be monitored continuously as roles and headcount change rather than assessed once at onboarding, since the risk grows with the engagement. 2 data scientists plus tax and employment counsel, 9-12 months.
**Data availability:** Contract data is complete; operational facts are largely uncollected; dispute outcomes exist and are not structured for learning.

---

## 3. Payroll Verification and Retroactive Recalculation
#gradient-boosting #change-point-detection #hypothesis-testing #confidence-intervals #bert #evaluation-metrics #compliance #automation

**Problem statement:** Payroll errors across jurisdictions originate mostly in rule changes not tracked in time, and payroll engine errors are silent — a wrong contribution base produces a plausible number that nobody catches until an authority or an employee does.

**ML task:** Independently recompute payroll against the rule base, detect anomalies in payslip components against the employee's own history and comparable peers, and automate retroactive recalculation when rules apply retrospectively
**Input data:** Payslip components with gross, contributions, deductions and net; the rule base with rates, bases, caps and thresholds by jurisdiction; employee history and contract terms; peer distributions within jurisdiction and salary band; rule change effective dates including retrospective ones.
**Target:** Whether a computed payslip component is correct under the applicable rules.
**Evaluation metric:** Detection of known historical errors, and the false alarm rate — payroll teams operate to a hard cycle deadline and a noisy pre-payment check will be bypassed, so precision governs whether it is used at all. The consequential measure is errors caught before payment rather than after, since a correction across borders is slow and an employee's pay error is a direct personal harm rather than an accounting one.
**Scope:** Independent recomputation must genuinely be independent — reimplementing the same logic against the same rule interpretation reproduces the same errors, so the value comes from the anomaly detection against distributions as much as from the recomputation. Retroactive recalculation is well-defined, laborious and entirely automatable. 2 engineers, 6 months.
**Data availability:** Complete within payroll systems; peer distributions are available across the platform's own client base.

---

## 4. Output-Based Work Measurement as an Alternative to Activity Monitoring
#gradient-boosting #time-series-forecasting #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #worker-facing

**Problem statement:** Activity monitoring measures motion rather than work, is weakest for exactly the tasks that involve thinking, produces the predictable behavioural response of proxy optimisation, and is deployed widely on an evidence base that does not support it.

**ML task:** Derive output-based measures from the systems where work actually lands, and evaluate whether monitoring improves outcomes at all
**Input data:** Domain-specific delivery systems — version control and issue trackers for software, ticketing for support, pipeline systems for sales, delivery records for creative work; monitoring data where deployed; team-level outcome measures; attrition, engagement and trust survey data; deployment variation across teams.
**Target:** Team and individual contribution measured through delivered work; and separately, the causal effect of monitoring deployment on outcomes.
**Evaluation metric:** For the monitoring evaluation, comparison across teams with and without deployment on delivery outcomes and attrition — a straightforward study that is essentially never run, which is itself informative about why monitoring is deployed. For output measures, the honest constraint is that they are domain-specific and partial, and reporting them at team level with uncertainty is defensible while individual productivity scoring from them is not.
**Scope:** Output measurement requires integration per work domain, which is why the generic activity proxy persists despite being worse. Proportionality should be designed in: minimum necessary collection, retention limits, aggregate rather than individual reporting, and worker visibility of their own data — which is better practice and is increasingly what jurisdictions require. 2 engineers, 6 months per work domain.
**Data availability:** Delivery system data is rich and requires per-domain integration; the monitoring evaluation needs only data most deploying organisations already hold.
