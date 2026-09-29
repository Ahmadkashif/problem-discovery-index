# Recommendations With Outcomes Attached

**Niche:** [[niches/agtech-platforms/digital-agronomy-advisory/profile|Digital Agronomy & Advisory]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An agronomist makes thousands of recommendations over a career, every one of them is followed by a measurable outcome, and no system anywhere joins the two.
**Tags:** #causal-inference #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #bayesian-inference #tacit-knowledge-ml #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
An agronomist recommends a fungicide application on a particular field at a particular growth stage. The application is made, the season completes, the yield is recorded. The recommendation and the outcome exist in the same platform and are never joined. Multiply by a thousand recommendations a season and a twenty-year career, and the agronomist's expertise — which is real and is built from watching fields — has developed with no systematic feedback on which of their recommendations actually paid. It is a professional judgement exercised continuously in an environment where the ground truth arrives every autumn and is never fed back.

## Why Nobody Has Built This
Attribution is genuinely hard: an outcome follows a recommendation but also follows the weather, the soil, the hybrid and everything else that happened that season, and a naive join produces a misleading answer. That difficulty is real and has been used as a reason to do nothing rather than as a reason to do it carefully, which would mean the randomised approach the row crop niche describes. In retail agronomy there is a further disincentive that ought to be named: an outcome-attached recommendation record would show which product recommendations paid for the grower, and the employer sells those products.

## What to Build
A recommendation record with an outcome joined, analysed with appropriate caution about what can be concluded. Every recommendation is stored with its field, its timing, its conditions and its rationale; the outcome is attached at harvest. Where a randomised trial was run, the effect is estimable directly. Where it was not, comparison across comparable fields and comparable seasons — within the agronomist's book and across the platform — supports an observational estimate whose limitations are stated rather than hidden. The agronomist's own view is the primary product: which of my recommendation types have been followed by good outcomes, where is my judgement well calibrated, and where does the evidence not support what I have been advising. That is a professional development instrument rather than an evaluation, and it should be built and presented as one. Aggregated across a platform, it is also the beginning of a genuine evidence base for practice, which agriculture largely lacks below the level of published research.

## Target Customer
Independent consulting firms, retail agronomy organisations willing to measure, agronomy platform vendors, and the growers who ultimately pay for advice one way or another.

## Impact If Built
Expertise without feedback plateaus, and this profession exercises judgement continuously against an outcome it never sees quantified. Attaching outcomes to recommendations is the mechanism by which agronomic practice could improve from evidence rather than from consensus, and the data to do it is generated every season and discarded.
