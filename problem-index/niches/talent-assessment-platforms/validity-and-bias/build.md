# Build: Continuous Validity and Fairness Monitoring

**Niche:** [[niches/talent-assessment-platforms/validity-and-bias/profile|Validity & Bias Measurement]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Monitor both properties continuously at the client — does the score predict outcomes here, and does it pass groups at different rates — rather than asserting one and auditing the other annually.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #evaluation-metrics #survival-analysis #compliance #logistic-regression
**Contested on:** Whether an instrument's validity can be monitored at a single client with the sample sizes a single client produces.

## The Problem

An assessment has two properties that matter and the industry treats them completely differently. Validity — does the score predict job performance — is asserted from the vendor's study and never revisited. Adverse impact — does the instrument pass groups at different rates — is increasingly audited, annually, on aggregate pass rates.

Neither is monitored. An instrument's validity can degrade as the role changes, as the applicant population shifts, as items leak, or as the labour market moves, and nothing detects any of that. Its adverse impact can vary by role, by location, by requisition and over time, and an annual aggregate figure conceals every one of those.

Both are computable from data that accumulates continuously inside the client's systems.

## Why Nobody Has Built This

Validation is slow, requires the client's performance data, and can produce a finding that invalidates a purchased instrument. The vendor does not want it, the buyer who selected the instrument does not want it, and the analyst who would run it reports to one of them.

Bias auditing has a legal driver and therefore exists, but in its minimum compliant form: annual, aggregate, conducted to produce a filed artefact rather than to detect a problem. The regulation specifies a floor and the floor has become the ceiling.

And nobody has connected the two, though the connection is the most important thing in the niche: a balanced instrument that predicts nothing is excluding people on a coin flip with a fairness certificate attached.

## What to Build

A monitoring layer at the client, running on accumulating hiring data.

**Join the records.** Assessment scores, hiring decisions, and for those hired, subsequent performance ratings, tenure, progression and any objective productivity measure. This join lives inside the client's systems and is the prerequisite for everything.

**Estimate validity with the range restriction handled.** The central methodological problem is that outcomes are observed only for people who were hired, who scored highly — so the observed correlation understates the true one and requires correction. Doing this properly, with stated assumptions, is what separates a credible local validation from a misleading one.

**Use multiple criteria, because performance ratings are bad.** Supervisor ratings are noisy, biased and frequently unrelated to output. Tenure, progression, objective productivity where it exists, and involuntary termination are each partial and together are far better than any one. Report against each rather than aggregating into a single validity claim.

**Monitor adverse impact continuously and by segment.** Pass rates by group, by role, by location, by requisition, with confidence intervals — because at small requisition sizes an apparent disparity is frequently noise and an annual aggregate hides real disparities that appear in specific roles.

**Report the two together.** The useful statement is: this instrument predicts tenure moderately and performance ratings weakly for this role, with balanced pass rates. Or: this instrument is balanced and predicts nothing, in which case it is excluding half your applicants for no reason. That second finding is the one the industry's current measurement regime cannot produce.

**Detect drift.** Validity and impact both change. Change-point detection on both series, against item exposure, population shifts and role changes, is what turns a study into monitoring.

## Target Customer

Large employers with assessment volume and performance data — the only party with both halves of the join — and their legal and assessment functions, who carry the exposure. Also the assessment vendors willing to be measured, for whom demonstrated local validity is a genuine differentiator in a market of asserted claims.

## Impact If Built

Validity becomes a measured, monitored property at the place the instrument is used rather than a claim inherited from a vendor's study. Adverse impact is detected where it actually occurs — in specific roles and requisitions — rather than averaged into an annual figure. And the combination that current practice cannot see, a fair instrument that predicts nothing, becomes visible.
