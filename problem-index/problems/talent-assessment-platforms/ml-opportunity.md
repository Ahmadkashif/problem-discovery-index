# Machine Learning Opportunities — Talent Assessment Platforms

**Industry:** [[talent-assessment-platforms|Talent Assessment Platforms]]
**Derived from:** [[problems/talent-assessment-platforms/high-impact|High Impact]], [[problems/talent-assessment-platforms/low-impact-1|Low Impact 1]], [[problems/talent-assessment-platforms/low-impact-2|Low Impact 2]], [[problems/talent-assessment-platforms/worker-life-1|Worker Life 1]], [[problems/talent-assessment-platforms/worker-life-2|Worker Life 2]]

---

## 1. Automated Local Criterion Validation With Range Restriction Correction
#hypothesis-testing #confidence-intervals #bayesian-inference #cross-validation #causal-inference #gradient-boosting #evaluation-metrics #compliance

**Problem statement:** Instruments are bought on vendor-run validation studies and deployed for roles and populations they were never validated against, and the local check — does the score predict anything about the people we hired — is almost never performed.

**ML task:** Join assessment scores to post-hire outcomes automatically and estimate local criterion validity, corrected for range restriction, across multiple criteria and pooled hierarchically across deployments
**Input data:** Assessment scores for all applicants including those not hired; post-hire outcomes — tenure, promotion, involuntary exit, objective productivity where it exists, performance ratings; role, location and hiring cohort; selection ratio and cut score; comparable deployments across the vendor's client base.
**Target:** The relationship between score and outcome among hires, corrected to estimate the relationship in the applicant population.
**Evaluation metric:** Range restriction correction is not optional and is the most misunderstood element here — only high scorers are hired, so the uncorrected local correlation understates validity and a naive study will wrongly conclude a good instrument does not work. Report corrected and uncorrected figures with the correction's assumptions stated. Use several criteria separately rather than a composite, because performance ratings carry their own biases and tenure or promotion are less contaminated; a validity claim that holds only against manager ratings is a weaker claim and should be visible as such.
**Scope:** Sample accumulation takes years per role, which is exactly why this must be a standing automated report rather than a commissioned study — the evidence accrues whether or not anyone asked. Hierarchical pooling across clients with heterogeneity modelled is the honest form of validity generalisation. 2 data scientists with psychometric training, 9-12 months.
**Data availability:** Scores are held by the vendor; outcomes sit in the client's HR systems and require a data-sharing arrangement that is rarely part of the contract.

---

## 2. Continuous Adverse Impact Monitoring With Small-Sample Treatment
#bayesian-inference #hypothesis-testing #confidence-intervals #probability-distributions #gradient-boosting #evaluation-metrics #compliance #causal-inference

**Problem statement:** Bias auditing has become an annual compliance artefact computed on aggregate pass rates, which is the form least likely to detect anything — disparity concentrated in a role or region disappears in aggregation, and intersectional disparity is suppressed because subgroup counts are small.

**ML task:** Monitor selection rates by group continuously across role, location and configuration version, with Bayesian estimation and pooling for small subgroups, decomposed by funnel stage
**Input data:** Applicant demographics where lawfully collected; assessment scores and pass outcomes; subsequent funnel stages — interview, offer, hire — from the client's applicant tracking system; role, location and configuration version with change history; historical baselines.
**Target:** Selection rate ratios by group and intersection, at each funnel stage, with uncertainty.
**Evaluation metric:** Detection lead time on disparities introduced by configuration changes, against the current annual cadence — a problem that persists for up to a year is the failure mode being addressed. For small subgroups the measure is whether the Bayesian estimate with pooling produces actionable intervals where suppression currently produces nothing; reporting "too few to analyse" for the intersections where disparity is most likely is a methodological choice with consequences and should be replaced rather than defended.
**Scope:** Stage decomposition requires joining vendor assessment data to client funnel data, and without it disparity is attributed to the wrong stage in both directions. Fairness and validity must be reported together — an instrument can be perfectly balanced and predict nothing, which passes an audit and fails as a product. 1-2 data scientists, 6 months.
**Data availability:** Assessment data is complete; funnel and demographic data sit with the client and are governed by the same sharing arrangement as validation.

---

## 3. Item Compromise Detection and Validated Item Generation
#bert #large-language-models #transformers #bayesian-inference #change-point-detection #confidence-intervals #evaluation-metrics #hypothesis-testing

**Problem statement:** Items take months to develop and calibrate, circulate publicly within weeks, and a compromised item measures preparation access rather than the construct — while generative tooling has made both item production and item lookup dramatically cheaper.

**ML task:** Detect compromise from response-stream signals and retire items automatically; and generate candidate items through a pipeline that pilots, calibrates and screens them, including for differential item functioning
**Input data:** Item-level response data with timing; item parameter estimates over time; response pattern anomalies; item exposure counts; public availability signals where observable; the construct definition and existing calibrated item bank; demographic data for differential functioning analysis.
**Target:** Whether an item is compromised, and whether a generated item measures the intended construct with acceptable psychometric properties and no differential functioning.
**Evaluation metric:** For compromise, detection lead time against the current mechanism, which is generally someone noticing. For generation, the acceptance rate through the screening pipeline is the honest figure — most generated items should fail calibration, and a pipeline with a high acceptance rate is screening too loosely. Differential item functioning analysis must be mandatory rather than optional on generated content, since generated items carry whatever associations the generating model absorbed and an item that is harder for one group for construct-irrelevant reasons is a fairness failure at the item level.
**Scope:** The screening rather than the generation is where the work and the value are. The strategic question sits above this: formats whose answers can be looked up are increasingly measuring tool access rather than the construct, and the shift toward work samples and process-observable tasks changes what the industry sells. 2 engineers plus a psychometrician, 6-9 months.
**Data availability:** Response data is complete and is exactly what item response theory was built for.

---

## 4. Candidate Feedback Generation and Accommodation Validation
#large-language-models #bert #confidence-intervals #bayesian-inference #hypothesis-testing #gradient-boosting #evaluation-metrics #worker-facing

**Problem statement:** Candidates spend unpaid hours on assessments and receive a score they never see, criteria they are never told and a rejection with no reason — and accommodation processes depend on a candidate disclosing a disability to a prospective employer.

**ML task:** Generate meaningful candidate feedback from score profiles, and validate that accommodated assessment forms measure the same construct as the standard form
**Input data:** Candidate score profiles across constructs; normative distributions; the assessment's construct definitions; accommodated and standard form response data; historical feedback and candidate response to it; completion and abandonment patterns by candidate segment.
**Target:** Feedback a candidate finds informative and accurate, assessed by candidate response; and measurement equivalence between accommodated and standard forms.
**Evaluation metric:** For feedback, whether it is understood and actionable, measured by candidate survey — and it must avoid over-claiming: a score band with an honest indication of the gap is defensible, and a narrative inference about a person's character from a personality inventory is not. For accommodation, formal measurement invariance testing between forms, which is the established psychometric method and is frequently skipped when an accommodation is granted ad hoc.
**Scope:** Completion bias is a measurement problem as well as an equity one — candidates who abandon are not a random sample, and disclosure plus feedback measurably improves completion, which serves the employer's own interests. Automated scoring of speech and language must be tested for differential performance across accents, dialects and non-native speakers, given the documented risks and the industry's own retreat from facial analysis. 2 engineers plus a psychometrician, 6 months.
**Data availability:** Score and response data are complete; accommodation data is sparse because the process discourages requests.
