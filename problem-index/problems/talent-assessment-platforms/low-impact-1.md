# Adverse Impact Measurement and Audit

**Industry:** [[talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Bias auditing has become a legal requirement in some jurisdictions and is generally conducted once a year on aggregate pass rates, which is the least informative form it could take.
**Tags:** #hypothesis-testing #confidence-intervals #bayesian-inference #gradient-boosting #causal-inference #evaluation-metrics #compliance #probability-distributions

## The Problem
Assessments that produce different pass rates across demographic groups create both legal exposure and real exclusion. US employment law has long addressed adverse impact through the four-fifths rule and related standards, and New York City's Local Law 144 introduced a specific requirement for annual independent bias audits of automated employment decision tools with published results — the first regime of its kind and a signal of the direction elsewhere.

The audits that result are typically thin. They compute selection rates by group at a single stage, annually, on aggregate data, and report ratios. That satisfies the requirement and tells almost nobody anything actionable.

The problems with the aggregate approach are well known in the technical literature. Disparity at one stage can be masked by aggregation across roles or locations with different applicant compositions. An instrument can show acceptable overall ratios while producing severe disparity in a specific role or region. And an annual cadence means a problem introduced by a configuration change persists for up to a year before anyone looks.

Small subgroup sizes make the statistics genuinely difficult, and the standard response — not reporting where numbers are small — is exactly where disparity is most likely to be both real and unexamined.

## What Already Exists
Established publishers have long-standing adverse impact analysis practices tied to legal defensibility requirements. Independent audit providers emerged specifically in response to Local Law 144. Fairness toolkits from the machine learning community — Fairlearn, AIF360 and others — implement a wide range of metrics. Some assessment platforms provide built-in adverse impact reporting. The legal framework around validation as a defence for disparate impact is well established in US case law.

## The Customisation Gap
Continuous monitoring rather than annual audit is the obvious improvement. Selection rates by group, by role, by location and by configuration version, computed continuously with appropriate statistical treatment of small samples, would catch a disparity introduced by a configuration change in weeks rather than a year.

Stage-level decomposition is the second gap. Adverse impact in a hiring funnel accumulates across screening, assessment, interview and offer, and measuring only the assessment stage attributes disparity to the wrong place in both directions. The client holds the funnel data and the vendor holds the assessment data, and neither analyses the whole.

Intersectional analysis is largely absent and is where disparity is frequently most severe, precisely because subgroup sizes are small and reporting conventions suppress them. Proper treatment of small samples — Bayesian estimation with pooling rather than suppression — is the technically correct answer and is not what audit practice currently does.

And the relationship between validity and fairness needs to be reported together. An instrument can be balanced and predict nothing, which is a fairness pass and a product failure; or predictive and disparate, which is a legal problem requiring a validity defence. Reporting the two separately, as the industry does, lets each hide behind the other.

## Impact If Solved
Bias auditing has become a compliance artefact conducted annually on aggregates, which is the form least likely to find anything. Continuous monitoring with stage-level decomposition catches problems while they are correctable, proper small-sample treatment brings intersectional disparity into view instead of suppressing it, and reporting validity alongside fairness stops an instrument passing as fair while predicting nothing at all.
