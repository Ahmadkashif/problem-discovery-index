# Machine Learning Opportunities — HR Tech Platforms

**Industry:** [[hr-tech-platforms|HR Tech Platforms]]
**Derived from:** [[problems/hr-tech-platforms/high-impact|High Impact]], [[problems/hr-tech-platforms/low-impact-1|Low Impact 1]], [[problems/hr-tech-platforms/low-impact-2|Low Impact 2]], [[problems/hr-tech-platforms/worker-life-1|Worker Life 1]], [[problems/hr-tech-platforms/worker-life-2|Worker Life 2]]

---

## 1. Structural Attrition Diagnosis at Group Level
#survival-analysis #gradient-boosting #causal-inference #hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Attrition is reported after the fact as a turnover percentage. The structural conditions that produce it — pay compression against new-hire offers, manager spans that grew as the organisation flattened, job families with stalled promotion velocity, absent internal mobility — are measurable months earlier and are fixable by decisions someone can make. Individual flight-risk scoring, the obvious product, has failed on trust and legal grounds and discredited the whole area.

**ML task:** Survival modelling of tenure with group-level covariates, plus causal estimation of the effect of structural conditions on exit hazard
**Input data:** Longitudinal employment records — compensation over time, promotion events and timing, manager changes, internal moves, job family and level, location, tenure and exit; new-hire offer levels by role and market; span of control by manager over time; cross-employer comparisons from the vendor's base.
**Target:** Voluntary exit, with the group-level rate as the unit of interest rather than the individual event.
**Evaluation metric:** Calibration of predicted group rates at team, role and location level, with intervals wide enough to be honest about small groups. The intervention value is what should be reported: expected attrition cost avoided if a specific condition is corrected, which is what an HR leader takes to a budget conversation.
**Scope:** The ethical boundary must be architectural. Individual-level scores should not be computable from the deployed system, not merely discouraged, because a capability that exists gets used and the category has already demonstrated what happens then. Confounding is severe — pay compression correlates with tenure, tenure with attrition — and separating structural from demographic effects requires deliberate care, including checking that any proposed intervention target is not a proxy for a protected characteristic. 3 ML engineers plus an organisational psychologist and employment counsel, 6-8 months.
**Data availability:** Longitudinal records across millions of workers and thousands of employers, which is an unusually strong panel. New-hire offer data is the key input for pay compression and lives in the applicant tracking system rather than the HCM, which is a common integration gap.

---

## 2. Municipal and State Employment Rule Monitoring
#large-language-models #bert #transformers #word-embeddings #change-point-detection #transfer-learning #compliance

**Problem statement:** Remote work made every employer multi-jurisdictional while sick leave accrual, pay transparency, predictive scheduling and classification rules fragmented to city level. No vendor maintains machine-readable rules at municipal granularity, and employers discover new requirements through a claim.

**ML task:** Change detection over crawled municipal and state legal corpora, plus extraction of operative rules into a structured form (accrual rate, cap, carryover, eligibility threshold, notice period)
**Input data:** Municipal code repositories, state legislative trackers, ordinance adoption feeds, agency guidance; existing curated rule sets as extraction training pairs; employer workforce locations from the platform.
**Target:** A detected rule change with effective date, and a structured draft rule for review.
**Evaluation metric:** Recall against a manually tracked set of known enactments is the metric that matters — a missed ordinance is the failure mode with liability attached. False positives per jurisdiction per month is the operational constraint on reviewer capacity. Applicability determination should be evaluated separately, since that is where employers actually err.
**Scope:** Nothing publishes automatically; the output is a review queue for a compliance team, and the applicability layer — which employees does this rule cover, given work location, headcount thresholds and hours worked — is as valuable as the extraction. Configuration verification, checking that the accrual actually configured matches the applicable rule, requires no modelling and should ship first. 2 ML engineers plus an employment attorney, 5 months.
**Data availability:** Municipal code is public, machine-readable in aggregate through several repositories, and completely unmonitored for this purpose. Coverage is uneven — some jurisdictions publish only PDFs.

---

## 3. Benefits Enrolment Reconciliation and Feed Anomaly Detection
#change-point-detection #hypothesis-testing #descriptive-statistics #confidence-intervals #gradient-boosting #evaluation-metrics #data-integration

**Problem statement:** Enrolment elections travel to carriers by EDI and fail silently. Transmission is logged; enrolment is not verified. The failure surfaces when an employee's claim is denied, and premium reconciliation routinely reveals employers paying for terminated employees for years.

**ML task:** Anomaly detection over feed characteristics, plus systematic census reconciliation between platform and carrier records
**Input data:** Outbound 834 feeds with record counts and transaction types; carrier census returns and invoices; platform enrolment state per employee per plan; life events and terminations with dates; historical discrepancies and their eventual causes.
**Target:** A discrepancy between platform-believed and carrier-held enrolment, and separately a broken or degraded feed.
**Evaluation metric:** Detection latency in days from the causing transaction, and precision on flagged discrepancies since a false alarm costs a carrier phone call. The financial metric is recovered premium from terminated-but-billed employees, which is directly measurable and is what pays for the project.
**Scope:** Most of the value requires no machine learning at all — a monthly census comparison and an invoice reconciliation are queries, and their absence after thirty years of EDI is a product gap rather than a technical one. The anomaly layer adds early detection on the feed itself: a sharp drop in record count or a plan that stops appearing is visible immediately. 1-2 ML engineers plus a benefits operations lead, 3-4 months.
**Data availability:** Feeds and platform state are complete internally. Carrier census returns are inconsistently retained and sometimes not requested at all, which is the main obstacle and is a process change.

---

## 4. Job Architecture Induction from Title Strings
#bert #word-embeddings #k-means-clustering #k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #transfer-learning

**Problem statement:** Every HCM implementation requires mapping hundreds of free-text job titles into a job architecture the employer frequently does not have. Consultants do it by hand on a fixed go-live date, and the vendor has performed the same mapping for hundreds of employers without retaining what was learned.

**ML task:** Clustering and hierarchical classification of title strings into job families and levels, with transfer from prior confirmed mappings
**Input data:** Employer title strings with compensation, reporting relationships, department and tenure; prior confirmed job architecture mappings across the vendor's implementations; public job taxonomies as a weak prior; compensation survey structures where licensed.
**Target:** Job family and level per title string, as confirmed by the implementation consultant and the employer.
**Evaluation metric:** Top-1 and top-3 accuracy on held-out employers, reported separately for common titles and the long tail where consultants actually spend their time. Compensation coherence within an inferred level is a useful unsupervised check — a level containing a threefold pay range is probably wrong.
**Scope:** Compensation and reporting depth are stronger signals than the title text itself and are what make this tractable where string matching fails. The output is always a proposal for confirmation, because job architecture encodes decisions about pay and promotion that belong to the employer. Reporting structure validation — cycles, orphans, implausible spans — needs no modelling and prevents the most visible go-live failures. 2 ML engineers, 4 months.
**Data availability:** Prior mappings exist as consultant spreadsheets in project folders rather than as a curated corpus, so assembling the training set is the first task and is entirely internal.
