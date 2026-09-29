# Drift Alerts That Fire on Nothing

**Niche:** [[niches/mlops-platforms/drift-and-degradation-detection/profile|Drift & Degradation Detection]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Monitoring products alert whenever an input distribution moves, most movements are harmless, and every team that deploys drift monitoring has muted it within a month.
**Tags:** #hypothesis-testing #change-point-detection #confidence-intervals #evaluation-metrics #descriptive-statistics #entropy-cross-entropy-kl-divergence #quick-win #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to tell a model owner that their model has stopped working before a business metric does — and whoever does that takes the account, because that is the question the whole category was bought to answer.

## The Problem
Drift monitoring is switched on across two hundred features. The first week produces sixty alerts: a marketing campaign shifted the traffic mix, a new country launched, a categorical value was added upstream, and a public holiday changed the daily pattern. The model is fine throughout. By week three the alerts go to a channel nobody reads. When a real degradation happens in month five, its alert is indistinguishable from the noise and is ignored along with everything else. The tool worked exactly as designed and the organisation is now less protected than before it was installed.

## Why It's Still Broken
Firing on any distribution change is the simplest thing to implement and the easiest to explain in a demo. The vendor's success metric is drift detected, which is a number that grows. Distinguishing harmful drift from harmless drift requires connecting to model performance, which is the hard problem the category exists to avoid. And the customer's experience of muting the alerts is not reported back to anyone who would change the product.

## What a Fix Looks Like
Alert on impact, not on movement. Weight every drift signal by the model's sensitivity to that feature, so a large shift in an input the model barely uses does not page anybody — this alone removes a large share of the noise and needs only the feature importances the training run already produced. Apply multiplicity control across the monitored feature set, since the false alarm rate compounds with the number of features and almost no product accounts for it. Suppress correlated alerts by grouping features that moved together and reporting the group with its likely common cause, because one upstream change producing forty alerts is the most common flood. Model seasonality explicitly, as a chart that fires every Monday is worse than no chart. Estimate the predicted performance impact of the observed drift and put that number in the alert, which converts a statistical statement into a decision the recipient can act on. Track which alerts led to action and retire the classes that never do, which is a straightforward inventory nobody keeps. And report the alert precision as a product metric, since the current design is optimised for recall at a cost that has already made the tool inert in most deployments.

## Who Feels the Pain
Model owners who muted the monitoring and no longer have it when it matters; the teams who bought a product now providing negative value; and the vendors whose renewal conversations are about a channel nobody reads.

## Impact If Fixed
Weighting drift by the model's own feature importances removes most of the noise using data the training run already produced. Putting a predicted performance impact in the alert turns a statistical observation into something a recipient can act on.
