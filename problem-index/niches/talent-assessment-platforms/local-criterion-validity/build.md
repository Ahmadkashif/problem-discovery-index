# Build: Local Validation With the Selection Problem Handled

**Niche:** [[niches/talent-assessment-platforms/local-criterion-validity/profile|Local Criterion Validity]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Join assessment scores to the employer's own outcome data and estimate whether the instrument predicts here, with range restriction and criterion bias handled honestly.
**Tags:** #causal-inference #bayesian-inference #maximum-likelihood-estimation #confidence-intervals #hypothesis-testing #survival-analysis #evaluation-metrics #compliance
**Contested on:** Whether a single employer's sample can support a credible validity estimate for a specific role.

## The Problem

An employer has been using an assessment for three years across two thousand hires. They cannot say whether it predicts anything.

The evidence is entirely available. Assessment scores for every applicant are in the vendor's system or the applicant tracking system. Performance ratings, tenure, promotions and terminations for everyone hired are in the HR system. The join is a key lookup, and it is not made.

When it is made, it is frequently made badly. The naive correlation between score and performance among hires is attenuated by range restriction — only high scorers were hired — and reads as evidence the instrument does not work. Or performance ratings are taken as ground truth when they carry their own biases, importing them into the validity conclusion.

## Why Nobody Has Built This

Incentives, principally. A negative finding invalidates a purchased instrument, embarrasses whoever chose it, and creates a problem for the vendor across their whole book. Nobody in the transaction is rewarded for establishing that the answer is no.

The methodology is also genuinely demanding. Range restriction correction, criterion contamination, small samples, and the noisiness of supervisor ratings all have to be handled competently, and an employer's HR analytics team usually has neither the psychometric training nor the mandate.

And the timeline defeats the procurement cycle: eighteen months to a usable sample, by which point the contract has renewed and the buyer may have moved on.

## What to Build

A validation capability that is honest about the methodology and structured to be repeatable.

**Build the join as infrastructure, not as a study.** Assessment scores, hiring decisions and outcomes linked continuously as they accumulate, so that the analysis is available whenever the sample supports it rather than commissioned as a project. The plumbing is the thing that makes repeated validation possible.

**Correct for range restriction explicitly and state the assumptions.** This is the single most important methodological step and the one most often skipped. The corrected estimate depends on assumptions about the unselected population that should be stated and varied, with the sensitivity reported.

**Use several criteria and report against each.** Supervisor performance ratings, first-year tenure, involuntary termination, promotion within a period, and objective productivity where it exists. Each is partial; agreement across them is informative; and the divergences are frequently the most interesting finding. Never collapse them into one validity number.

**Treat the criterion sceptically.** Performance ratings carry rater effects and potential demographic bias. Estimating validity against a biased criterion can produce an instrument that looks valid because it predicts the same bias. Checking whether the criterion itself shows group differences, and reporting validity against the less contaminated criteria separately, is a necessary step and almost never taken.

**Report with intervals and be willing to say inconclusive.** A single employer's sample for a single role is often too small. Reporting "we cannot tell from 140 hires" is the honest outcome and is more useful than a point estimate that will be over-read.

**Pool across employers where it is possible.** A consortium analysis across several employers using the same instrument for similar roles is far better powered than any one of them, and it is the structure the industry most obviously lacks. It requires a neutral party and an agreement, which is a business model rather than a technical problem.

## Target Customer

Large employers with assessment volume, an analytics function and legal exposure that makes an unvalidated instrument uncomfortable. Also the established test publishers, for whom demonstrated local validity is a differentiator against entrants asserting it, and any neutral party willing to run the cross-employer consortium.

## Impact If Built

An employer learns whether the instrument they have deployed for three years predicts anything about their own hires. The methodology gets handled properly, so the answer is credible in both directions. And the cross-employer pooling that would settle these questions with adequate power becomes possible for the first time.
