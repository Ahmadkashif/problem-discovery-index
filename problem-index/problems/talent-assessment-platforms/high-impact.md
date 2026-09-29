# The Instrument's Validity Is Asserted by the Vendor and Established Nowhere

**Industry:** [[talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** High Impact
**One-liner:** A test is bought on a validation study run by its seller and deployed for a role it was never validated against, and nobody ever checks whether the score predicted anything about the people hired.
**Tags:** #hypothesis-testing #confidence-intervals #bayesian-inference #causal-inference #gradient-boosting #evaluation-metrics #compliance #cross-validation

## The Problem
An assessment vendor demonstrates validity: their instrument correlates with job performance in a study, published as a technical manual or a white paper. A client buys it, configures it for a role, and applies it to candidates.

The gap between those two things is large. The validation population is not this client's applicant pool, the criterion measure is not this client's performance data, and the role is rarely the same role. Established publishers handle this with validity generalisation arguments, which are a legitimate psychometric tradition and are still an argument that a relationship observed elsewhere transfers here.

The check that would settle it is local criterion validation: join assessment scores to what actually happened to the people hired — performance ratings, tenure, progression, whatever the organisation records — and measure the relationship. It is rarely done. Sample sizes take years to accumulate for any one role, performance ratings are noisy and carry their own biases, and the organisational appetite for a study that might invalidate a purchased system is limited.

Range restriction makes it harder in a way that is frequently misunderstood. Only high scorers are hired, so the observed correlation among hires understates the true relationship, and a naive local study will find weak validity even for a good instrument. Correcting for this is standard psychometric practice and is beyond most in-house teams, which means the honest local study is harder than it looks and the dishonest conclusion — that the test does not work — is easy to reach.

Meanwhile the newer entrants in this market frequently assert validity from machine-learned models trained to predict a proxy — interview outcomes, existing employee scores, manager ratings — which measures agreement with existing selection decisions rather than prediction of job performance. That distinction is the whole question and it is routinely blurred in vendor materials.

## Why It's Unsolved
The buyer cannot evaluate the claim. Talent acquisition leaders are not psychometricians, vendor technical manuals are long and technical, and the procurement process compares features and price. There is no independent certification that distinguishes a well-validated instrument from a confidently-marketed one.

Criterion data is genuinely poor. Performance ratings are the usual criterion and are known to be unreliable, compressed, and affected by the same biases the assessment is supposed to avoid — so a local validation study may be measuring agreement with a biased rating rather than prediction of performance.

Sample sizes are unforgiving. Meaningful validation for a single role requires hundreds of hires with outcome data, which most organisations accumulate over years if at all, and pooling across roles or clients raises the question of whether the pooled relationship applies to any of them.

And the incentives point away. The vendor has no reason to fund a study that could fail; the client has no reason to discover that a system they selected does not work; and the recruiter who uses the score daily has no way to know either.

## What a Solution Looks Like
Make local validation a product feature rather than a research project. A platform that automatically joins assessment scores to available outcome data — tenure, progression, performance where recorded — and reports the relationship with range restriction corrected and honest intervals, turns validation from a study nobody commissions into a standing report.

Use better criteria than performance ratings where possible. Tenure, promotion, involuntary exit and objective productivity measures where they exist are all less contaminated than a manager's annual rating, and reporting against several criteria separately is more informative than one composite.

Pool across clients with the heterogeneity modelled. A vendor can aggregate validation evidence across many deployments using a hierarchical model that reports both the pooled relationship and how much it varies by context — which is the honest form of validity generalisation and is more useful than a single published coefficient.

Distinguish prediction from imitation explicitly. A model trained to reproduce existing hiring decisions should be described as such, because it will faithfully reproduce whatever those decisions contained, including their biases. That distinction should be a labelling requirement.

And publish. A vendor that reports local validity across its deployment base, including the weak results, would be the only one able to substantiate its claims — and the regulatory direction is moving toward requiring exactly this kind of disclosure.

## Impact If Solved
This industry's product is a prediction, and whether the prediction holds is checked almost nowhere. Automated local validation makes the evidence a standing feature rather than a study nobody funds, better criteria reduce the contamination that makes local studies untrustworthy, and distinguishing instruments that predict performance from models that imitate past decisions addresses the most consequential ambiguity in the current market — one that determines whether a tool opens opportunity or automates the pattern it inherited.
