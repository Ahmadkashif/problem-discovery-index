# Challenge Testing Selected at Random Instead of by Risk

**Niche:** [[niches/hvac-contractors/equipment-performance-certification/profile|HVAC Equipment Performance Certification]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The programme retests a random sample of certified models and has decades of results showing exactly which submissions were most likely to fail.
**Tags:** #logistic-regression #gradient-boosting #binary-classification #anomaly-detection #evaluation-metrics

## The Problem
The certification programme's credibility rests on challenge testing: independently retesting certified equipment to confirm the manufacturer's claimed rating holds. Testing is expensive — a full test of a single system combination costs thousands of dollars and occupies a laboratory for days — so only a fraction of the certified population can ever be retested.

Selection is largely random within categories, with some rotation and some response to complaints. That is defensible and it is also the least informative allocation of a scarce, expensive resource.

The programme has decades of challenge results. It knows which manufacturers' claimed ratings have failed retest and by how much, in which product categories, at which points in a product cycle, and following which kinds of rating submission. Every one of those is a labelled outcome. The corpus sits in test records, used to enforce individual findings and never to decide where to look next.

## Why Nobody Has Built This
Random selection is procedurally safe. In a programme where members are also the certified manufacturers, being able to say that selection is impartial and unbiased is worth a great deal politically, and risk-based selection sounds like targeting. That governance concern is real — and it is a reason to design the model carefully, not a reason to allocate testing capacity by coin flip.

The results were also never stored as data. Challenge testing produces a pass or a finding on a specific model, filed against that certification. There is no dataset joining submission characteristics to retest outcomes, so the question of what predicts a failure has not been askable.

And the programme is judged on whether its process was followed, not on how many misstated ratings it caught — a metric nobody computes, since the denominator is unknown.

## What to Build
Risk-based test selection on the programme's own challenge history.

**Assemble the outcome set.** Every challenge test conducted, its result, the margin by which the rating held or failed, and the characteristics of the submission — manufacturer, category, rating margin above the minimum standard, time since last test, proximity to a standard change, whether the rating was claimed near a rebate or tax credit threshold.

**Model failure probability.** With a labelled history this size the model does not need to be exotic; it needs to be calibrated and explainable, because it will be scrutinized by the manufacturers it selects.

**Allocate by expected information, not just probability.** A category tested heavily last year and a category untested for five years carry different value at the same failure probability. This is a coverage-and-risk allocation, and treating it as one is the actual improvement.

**Screen the submissions themselves.** Claimed ratings that sit implausibly against the physics, against the manufacturer's own product line, or suspiciously just above a regulatory or incentive threshold are checkable before any equipment is tested. Ratings cluster at thresholds for reasons that are sometimes engineering and sometimes not, and the distribution says which.

**Publish the deterrence effect.** If risk-based selection works, claimed-versus-verified margins should tighten over time. That is measurable, and it is the argument that keeps the programme funded.

## Target Customer
VP of Certification or Chief Technical Officer at the certification body. The forcing function is external: minimum efficiency standards have tightened and the refrigerant transition is retiring entire catalogues, which means a flood of new ratings for new equipment with no track record, arriving exactly when testing capacity is most stretched.

## Impact If Built
Every efficiency rebate, tax credit, and code compliance decision in US HVAC rests on these ratings being true. Detecting the same number of misstatements with less testing — or more with the same — improves the integrity of the whole incentive structure, and the data to do it has been accumulating for decades in test files.
