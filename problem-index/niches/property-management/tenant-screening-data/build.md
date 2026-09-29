# A Score That Decides Who Gets Housing and Has Never Been Validated Against Who Paid

**Niche:** [[niches/property-management/tenant-screening-data/profile|Tenant Screening Data & Scoring]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tens of millions of rental applications a year are approved or declined on a score whose developer almost never learns whether the approved tenants paid.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #evaluation-metrics #causal-inference

## The Problem
A tenant score is a prediction: will this applicant pay rent for the term of the lease without being evicted or leaving a balance. It is built from credit attributes, prior eviction filings, criminal records where permitted, and income verification, and it drives a decision that determines where a household lives.

The prediction is rarely checked. Screening bureaus sell the report at application time. What happens next — whether the tenant paid on time for two years, missed three months, was filed against, or left owing money — happens inside the property manager's accounting system and mostly does not come back.

This produces the classic broken loop, in an unusually stark form. Declined applicants never generate an outcome at all, so the training data is only ever the approved population, which is selected on the score being validated. Approved applicants generate outcomes that the bureau largely does not observe. The result is a model fitted on credit-bureau proxies for rent payment rather than on rent payment.

Eviction filings, the single most heavily weighted negative in most screening products, are a particularly poor label. A filing is not a judgment, most filings are for nonpayment that gets cured, and filing propensity varies enormously by landlord and jurisdiction — so the variable partly measures which landlord an applicant previously rented from rather than how that applicant behaved. Several states have restricted the use of filings for exactly this reason, which is removing a heavily weighted input from models whose replacement has not been built.

## Why Nobody Has Built This
The commercial structure separates the decision from the outcome. The bureau is paid per screen; the outcome accrues to the manager. Nothing in the transaction obliges the manager to report back, and rent ledger data is theirs.

Contributed rental payment data does exist and is growing, but it is voluntary, skewed toward large professionally managed portfolios, and generally used to enrich the file for the next applicant rather than as a label for validating the score.

And there is a defensive logic. Under FCRA, a score is a consumer report and its accuracy is legally contestable. A bureau that formally measured how well its score predicted actual payment, by subgroup, would be generating exactly the evidence a disparate impact claim would seek. The safest position has been not to measure — which is also why the models have not improved.

## What to Build
Outcome-linked scoring, with the selection problem treated as the modelling problem it is.

**Close the loop contractually.** Trade something managers want — better pricing, portfolio analytics, deposit programme integration — for de-identified lease outcome reporting. This is a commercial design problem before it is a technical one, and it is the entire foundation.

**Model the right target.** Not "was there an eviction filing" but the outcomes that matter economically: months of on-time payment, balance at move-out, and lease completion. These are different quantities with different drivers, and the current single score collapses them.

**Handle selection explicitly.** Only approved applicants have outcomes, and approval depended on the score. This is a well-understood structure — reject inference, and instances where managers approved despite a low score are the natural experiment. Those overrides happen constantly and are the most valuable rows in the dataset.

**Treat tenure as survival.** A lease is a duration with censoring, and default risk is not flat over its term. A hazard model says when risk concentrates, which is directly actionable for renewal and deposit decisions in a way a single score is not.

**Replace the eviction filing variable with something defensible.** Restrictions are spreading and the variable is contaminated by landlord filing propensity. Modelling filing propensity by landlord and jurisdiction, and adjusting for it, is both better prediction and the beginning of a defence.

**Measure subgroup performance and publish the methodology.** Doing this internally first, deliberately, with counsel, is far better than having it done externally by a regulator or a plaintiff. A bureau that can demonstrate a validated, outcome-linked model has a position no competitor asserting accuracy can match.

## Target Customer
Chief Data Officer or VP of Analytics at a tenant screening bureau. The commercial argument is direct: the inputs the industry has relied on are being legislated away, and the only durable replacement is a model built on what actually happened.

## Impact If Built
Tenant screening decides access to housing for tens of millions of households a year using models validated against credit proxies rather than rent payment. Closing the loop would improve the decisions in both directions — fewer families excluded by a filing that was cured, fewer losses for owners — and it is the only route to a screening product that survives the regulatory direction the category is moving in.
