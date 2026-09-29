# In-Sample Fit Presented as Accuracy

**Niche:** [[niches/marketing-attribution-vendors/validation-and-ground-truth/profile|Validation & Experimental Ground Truth]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The deck says the model explains ninety-four percent of the variance, the client hears that it is ninety-four percent accurate, and neither number says anything about whether the channel contributions are right.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #compliance #quick-win #bayesian-inference #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to make experiments the ground truth and every model an interpolator between them — and whoever does that credibly makes their own error rate visible and resets the terms the whole category competes on.

## The Problem
Every vendor presentation includes a fit statistic. A model that explains almost all of the variance in a revenue series is easy to produce — revenue is highly autocorrelated and seasonal, and a model with a trend and a few seasonal terms will get most of the way there before any marketing variable is included. The statistic says essentially nothing about whether the channel contributions, which are the product, are correct. Clients read it as accuracy because it is the only number offered that looks like one, and vendors present it because it is impressive and because the honest alternative requires validation nobody does.

## Why It's Still Broken
The statistic is available, familiar and flattering, and no client has the statistical background to challenge it — a measure that is easy and impressive fills the space where a hard and honest one should be. Every vendor presents one, so omitting it looks like weakness. The correct number requires experimental comparison. And nobody has been penalised, because the model's failures are never established.

## What a Fix Looks Like
Report something that can be wrong. Show out-of-sample and out-of-time performance rather than in-sample fit, which is the fix, is a standard modelling practice the category has simply not adopted in its reporting, and immediately reduces the flattering number. Report uncertainty on the channel contributions themselves, since those are the product and a point estimate implies a precision the model does not have. Show the contributions under alternative reasonable specifications, which reveals how much of the answer is a modelling choice and is the honest disclosure the mix modelling work develops. Compare against a naive baseline — last year's allocation, a simple seasonal model — because a skill score against a baseline is meaningful where a variance statistic is not. Present experimental comparisons where any exist, even unflattering ones, since a vendor showing where their model missed is more credible than one showing a fit statistic. Explain what the fit statistic does and does not mean, in one sentence, which most clients have never been told. Stop leading with it, because whichever number is at the top of the deck becomes the basis of trust. Give clients a checklist of what to ask any vendor, which is the fastest route to changing the norm. Standardise reporting through an industry body, since no vendor can drop the statistic alone. And publish the error distribution, because the category will only develop a validation norm when one participant makes theirs visible.

## Who Feels the Pain
Clients reallocating budget on a statistic that cannot be wrong; honest vendors competing against flattering numbers; and the category, whose central claim is unfalsifiable as presented.

## Impact If Fixed
An easy, impressive statistic fills the space where a hard, honest one belongs, and revenue's own seasonality supplies most of the fit before any marketing variable enters. Out-of-sample performance and a skill score against last year's allocation are standard practice the category simply has not adopted.
