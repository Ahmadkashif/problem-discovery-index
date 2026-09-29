# Machine Learning Opportunities — Bug Bounty Platforms

**Industry:** [[bug-bounty-platforms|Bug Bounty Platforms]]
**Derived from:** [[problems/bug-bounty-platforms/high-impact|High Impact]], [[problems/bug-bounty-platforms/low-impact-1|Low Impact 1]], [[problems/bug-bounty-platforms/low-impact-2|Low Impact 2]], [[problems/bug-bounty-platforms/worker-life-1|Worker Life 1]], [[problems/bug-bounty-platforms/worker-life-2|Worker Life 2]]

---

## 1. Programme Effect: Overlap, Supply Curve and Time-to-Discovery
#causal-inference #survival-analysis #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** Programmes report spend, submissions and triage time, and cannot say whether the vulnerabilities they paid for were ones internal testing, a scanner or the next release would have surfaced anyway — so the budget is defended with a severity histogram.

**ML task:** Estimate overlap between bounty findings and what the organisation's other controls already covered; estimate the payout-to-attention supply curve across the platform's customer base; and measure time from vulnerability introduction to report
**Input data:** Submissions with technical detail and outcome; the customer's scanner coverage and output, internal testing scope, and backlog of known-deprioritised issues; code and release history giving vulnerability introduction dates; payout tables, scope breadth and researcher attention volume across many programmes.
**Target:** Whether a paid finding was already visible internally; the relationship between payout level and the volume and quality of attention; and the interval from introduction to report.
**Evaluation metric:** Overlap is the tractable proxy and should be reported plainly — a programme where most paid findings were already visible internally is buying attention rather than discovery, which is a legitimate purchase and a different one from what is claimed. The supply curve is validated by whether payout changes produce the predicted attention shift on held-out programmes. Time-to-discovery is the metric that substantiates the category's real claim, which is not that bounties find what nothing else would but that they find things sooner and continuously; compare against the same interval for internally-found issues.
**Scope:** The platform sees submissions and payouts; the organisation sees scanners, internal testing, backlog and releases. Joining them needs a customer willing to share, and nobody has framed the ask. Commercially this is awkward — a measurement layer that tells some customers their programme buys little would reduce spend — which is the same structure as every assurance business in this cluster. 2 ML engineers plus a causal specialist, 9-12 months.
**Data availability:** Platform side complete; customer side requires a data-sharing arrangement that has not been attempted.

---

## 2. Substance-Based Duplicate Detection
#contrastive-learning #bert #transformers #k-nearest-neighbors #dbscan #gradient-boosting #evaluation-metrics #confidence-intervals

**Problem statement:** Two researchers describing the same underlying vulnerability write completely different reports, and keyword matching cannot connect them. Missing a duplicate pays twice; wrongly calling one denies a researcher payment for original work, which is the most damaging thing a programme can do to its reputation.

**ML task:** Represent a submission by its technical substance — affected component, weakness class, mechanism, reachability path — and match against prior submissions across the programme's history
**Input data:** Submission text, reproduction steps, request and response evidence and attachments; affected asset and endpoint; the programme's full submission history including confirmed duplicate decisions; the platform's cross-programme corpus of duplicate pairs.
**Target:** Whether two submissions describe the same underlying vulnerability, labelled by confirmed triage decisions.
**Evaluation metric:** The two error types must be reported separately and weighted by their real costs, which are not symmetric: a missed duplicate costs a payment, a false duplicate costs a researcher their earnings and the programme its reputation. Set the operating point accordingly and surface candidates for human comparison rather than deciding autonomously. Measure on the hard cases — same vulnerability, different endpoint and framing — since near-identical reports are the easy case that keyword search already handles.
**Scope:** The platform holds the largest corpus of confirmed duplicate pairs in existence, which is the label set nobody has used. Surfacing the candidate original with its report turns a triager's judgement into a comparison, which is faster, more accurate and far more defensible when disputed. 2 ML engineers, 6-9 months.
**Data availability:** Excellent and unique to the platforms.

---

## 3. Validity Prediction and Severity Calibration
#gradient-boosting #bert #bayesian-inference #confidence-intervals #k-nearest-neighbors #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Most submissions are not actionable and every one must be read by an expensive person; separately, severity is judgement applied without external calibration, and it sets payment brackets, so every judgement call is a unilateral money decision.

**ML task:** Predict submission validity to order the triage queue, and produce a cross-programme reference severity range for comparable findings
**Input data:** Report structure, specificity and evidence quality; researcher history in the relevant technology area; scope match; scanner-output signatures; the platform's corpus of severity ratings across thousands of programmes with finding class and context.
**Target:** Triage outcome (valid, duplicate, out of scope, non-issue) and the distribution of severity ratings given to comparable findings elsewhere.
**Evaluation metric:** For validity, ranking quality rather than classification accuracy — nothing may be dropped, only ordered, because the low-prior report from an unknown researcher is occasionally the most important one, and a system that suppresses is a different and much worse product. For severity, report a range rather than a point, since the honest output is that this class of finding in this context is typically rated within these bounds — a programme rating well outside it is doing something unusual and both parties should see that.
**Scope:** The severity reference is the platform's natural role and its unique capability, and it converts a unilateral judgement into a discussion with a reference point — which is most of what researchers are asking for. Scanner-output detection at intake, returned with a request for validation rather than a rejection, removes a large share of volume without alienating anyone. 2 ML engineers, 6-9 months.
**Data availability:** Complete across the platform. Cross-programme severity data is the asset no individual programme has.

---

## 4. Scope Determination and Researcher-Programme Matching
#bert #large-language-models #contrastive-learning #gradient-boosting #k-nearest-neighbors #confidence-intervals #evaluation-metrics #worker-facing

**Problem statement:** Scope is prose interpreted after the researcher has done the work, by the party paying. And researchers choose where to spend time blind, using knowledge that circulates informally about which programmes are responsive and fair.

**ML task:** Classify a proposed target against a programme's scope policy before testing begins, and match researchers to programmes on demonstrated strength and programme behaviour
**Input data:** Scope policy text and its history; proposed target descriptions; past scope determinations and disputes; researcher submission history by technology area and outcome; programme responsiveness, severity ratings relative to the platform reference, duplicate rates, scope breadth and payment timeliness.
**Target:** In scope, out of scope, or genuinely ambiguous — with ambiguous escalated for a human decision before the work rather than after it.
**Evaluation metric:** For scope, the ambiguous class is the important output and its precision matters most: a confident wrong determination sends a researcher to spend a week on something that will not pay, which is exactly the harm being addressed. Measure the reduction in post-submission scope disputes as the outcome. For matching, whether researchers directed to a programme submit valid findings at a higher rate — and whether the transparency shifts attention toward programmes that treat people well, which is the competitive mechanism that would improve the others.
**Scope:** Programme quality transparency is largely a policy decision — the platform can measure all of it today — and it creates pressure the platform may not welcome, since its revenue comes from the programmes. That tension should be named rather than engineered around. 2 ML engineers, 6-9 months.
**Data availability:** Complete on the platform side.
