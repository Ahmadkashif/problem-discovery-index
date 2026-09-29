# The Churn Score Nobody Has Checked

**Niche:** [[niches/game-analytics-vendors/predictive-models-as-product/profile|Predictive Models as Product]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The studio has been targeting retention campaigns on a churn score for a year and nobody has compared it to who actually churned.
**Tags:** #quick-win #cross-validation #evaluation-metrics #confidence-intervals #descriptive-statistics #logistic-regression #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to ship churn and lifetime value scores that are actually true of a given studio's players, when the models are fitted generically across a whole customer base — and whoever makes them trustworthy takes the account.

## The Problem
A churn score arrives as a product feature and becomes load-bearing. Retention campaigns target it, forecasts use it, and segments are built on it. Nobody has ever taken a cohort of scored players, waited, and checked how many actually churned at each score level. The score may be well calibrated, badly calibrated or nearly uninformative for this game, and a year of decisions has been made without anyone establishing which.

## Why It's Still Broken
Nobody validates a feature — a number that arrives as part of a product is treated as a property of the data rather than as a claim requiring evidence, and nothing in the interface suggests otherwise. The check requires waiting. Neither vendor nor customer has owned it. And the campaigns appear to work because something always does.

## What a Fix Looks Like
Take one cohort and check it. Score a cohort, wait the prediction window, and compare predicted against actual by score band, which is the fix and takes one query and one wait. Plot calibration rather than reporting a single accuracy number, since a model can be accurate overall and badly wrong in the band being targeted. Check the high-score band specifically, as that is the one campaigns act on and where miscalibration costs most. Compare against a trivial baseline such as days since last session, because a sophisticated score that does not beat one is worth knowing about. Repeat quarterly rather than once, given how fast these populations shift. Ask the vendor what the model was trained on, which they will usually answer and nobody asks. Check lifetime value predictions against realised revenue the same way. Report the finding to the teams using the score, which is where the behaviour changes. Adjust the campaign thresholds to the calibration rather than to a round number. And stop using the score for anything it cannot support, which is the honest outcome if the check goes badly.

## Who Feels the Pain
Studios spending retention budget on the wrong players; analysts forecasting from unvalidated predictions; vendors whose feature is trusted more than it has earned; and the players who were targeted or ignored incorrectly.

## Impact If Fixed
A number that arrives as part of a product is treated as a property of the data rather than as a claim requiring evidence. One cohort, one wait and a calibration plot establishes whether a year of decisions rested on anything.
