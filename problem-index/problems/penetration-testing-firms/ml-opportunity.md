# Machine Learning Opportunities — Penetration Testing Firms

**Industry:** [[penetration-testing-firms|Penetration Testing Firms]]
**Derived from:** [[problems/penetration-testing-firms/high-impact|High Impact]], [[problems/penetration-testing-firms/low-impact-1|Low Impact 1]], [[problems/penetration-testing-firms/low-impact-2|Low Impact 2]], [[problems/penetration-testing-firms/worker-life-1|Worker Life 1]], [[problems/penetration-testing-firms/worker-life-2|Worker Life 2]]

---

## 1. Coverage Measurement and Residual Finding Estimation
#bayesian-inference #confidence-intervals #probability-distributions #gradient-boosting #graph-neural-networks #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** A time-boxed test is reported as an assessment. A clean report and a report from an engagement that ran out of time before reaching the interesting half look identical, and buyers read the absence of findings as evidence of security.

**ML task:** Instrument what an engagement reached and attempted, and estimate the expected number of remaining findings given that coverage, the technology stack and the firm's historical yield on comparable systems
**Input data:** Per-engagement records of components reached, attack classes attempted and deferred, time allocation; the target's technology stack and surface characteristics; the firm's historical engagements with duration, coverage and findings; longer engagements against comparable systems as the reference for what fuller coverage yields.
**Target:** Findings not discovered within the engagement window — estimable from the relationship between duration, coverage and yield across the firm's corpus.
**Evaluation metric:** Validate against engagements where longer or repeat testing subsequently found what a shorter one missed, which exists in any firm's history and has never been analysed. The honest output is a statement of form: a fortnight on this stack typically surfaces about half of what a month would. Report intervals; the estimate is a projection from historical yield curves and pretending otherwise would replace one false assurance with another.
**Scope:** Coverage definition is the hard part — code coverage is measurable and means little about security; attack class coverage against named components is the workable form and requires agreeing a taxonomy. Testers largely track this informally already in notes and in their heads. The obstacle is commercial: the first firm to report coverage honestly looks worse than competitors who say nothing. 2 ML engineers plus a practice lead, 6-9 months.
**Data availability:** Engagement records exist as reports and notes rather than as structured coverage data, and the instrumentation must start being captured.

---

## 2. Environment-Aware Severity and Cause Clustering
#graph-neural-networks #gradient-boosting #bayesian-inference #confidence-intervals #bert #k-nearest-neighbors #evaluation-metrics #worker-facing

**Problem statement:** Severities are assigned by testers who cannot see the environment, so the client's security engineer re-prioritises eighty findings by hand against actual architecture — and the same finding classes recur annually because instances are fixed and causes are not.

**ML task:** Re-score findings against reachability, authentication context, data sensitivity and compensating controls from the client's own architecture data, and cluster findings by underlying systemic cause
**Input data:** Findings with tester severity and technical detail; the client's asset inventory, network and identity architecture, data classification; existing controls; the client's engagement history across years; code and dependency structure where available.
**Target:** A severity a client security engineer would defend to a product team, and the systemic cause behind a group of findings.
**Evaluation metric:** Agreement with the client's own re-prioritisation, which they currently perform manually and which is the ground truth this is replacing. For clustering, the practical test is whether the cause-level view makes a systemic fix arguable — measure remediation rate on cause-level items against instance-level ones, since the whole point is that eighty findings are usually a much smaller number of real issues.
**Scope:** Cause clustering directly addresses the recurrence problem that drives security engineers out of these roles. It requires the client's engagement history, which means the firm must retain findings across years in a structured form — most do not. 2 ML engineers, 6-9 months.
**Data availability:** Findings exist in reports. Client architecture data requires access the client can grant and often has not been asked for.

---

## 3. Remediation Outcome and Recurrence Tracking
#survival-analysis #gradient-boosting #causal-inference #confidence-intervals #time-series-forecasting #evaluation-metrics #compliance #data-integration

**Problem statement:** A firm delivers findings and leaves. Whether they were remediated, whether the fix worked, and whether the class recurred all happen inside the client and never return — so a firm with thousands of engagements cannot say which of its remediation advice actually works.

**ML task:** Track remediation status and retest outcomes across engagements, estimate time-to-remediation by finding class and client characteristics, and predict recurrence
**Input data:** Findings with class, severity and remediation advice; remediation status and retest results; client sector, size and security maturity; time between engagements; the same client's subsequent findings; the advice given in each case.
**Target:** Whether a finding was remediated, how long it took, and whether the class recurred at the next engagement.
**Evaluation metric:** The finding that matters is which remediation advice is associated with non-recurrence, controlling for client and finding class — this is the firm's first real evidence about the quality of its own recommendations and is likely to be uncomfortable for some standard advice. Report recurrence rates by finding class publicly within the firm; a class that recurs at a high rate across many clients indicates the advice is wrong, not that the clients are negligent, and the current framing assumes the opposite.
**Scope:** The data requires asking clients for remediation status as a standard part of the engagement rather than as a separate retest sale. Most would agree if framed as included assurance, and nobody asks. Causal claims about advice quality need care — clients who remediate well differ systematically — so matched comparison is the minimum bar. 2 ML engineers, 6-9 months once the loop is established.
**Data availability:** Does not currently exist anywhere in the industry. Establishing the loop is the project.

---

## 4. Attack Surface Discovery and Engagement Estimation
#graph-neural-networks #gradient-boosting #bert #change-point-detection #confidence-intervals #k-nearest-neighbors #evaluation-metrics #feature-engineering

**Problem statement:** Engagements are scoped and priced from a client-compiled asset list that is incomplete for structural reasons, and the real surface is discovered after the contract — producing either uncovered scope or an over-priced engagement, both of which damage trust.

**ML task:** Discover the external attack surface passively before quoting, estimate engagement effort and expected finding yield from measured surface characteristics, and detect drift since the last engagement
**Input data:** Passive external discovery — subdomains, certificate transparency, cloud asset fingerprints, public code and configuration exposure; endpoint counts, technology stack, authentication complexity and integration counts; the firm's historical engagements with realised days and findings; the client's surface at the previous engagement.
**Target:** Days consumed and findings produced, and the set of assets that were not in the client's inventory.
**Evaluation metric:** Estimation error against realised engagement days on held-out engagements, with intervals — and specifically the rate at which scoping missed material assets, which is the failure that produces the coverage problem in item 1. For drift, precision on assets genuinely new since the last engagement, since a list full of false changes will be ignored.
**Scope:** The tooling for external discovery is a mature adjacent category sold to defenders, and using it at scoping time rather than after contract is a workflow change more than a technical one. Estimating expected finding yield turns the commercial conversation from days into expected value, which changes what the client thinks they are buying. Drift detection between annual engagements is the basis for continuity in a model that currently produces disconnected snapshots. 2 ML engineers, 4-6 months.
**Data availability:** Discovery data is obtainable passively. Historical engagement effort exists in time records and is rarely joined to surface characteristics.
