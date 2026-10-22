# Dig Thresholds Informed by Every Prior Site

**Niche:** [[niches/geophysical-survey-firms/uxo-advanced-geophysical-classification/profile|UXO Advanced Geophysical Classification]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each munitions response site sets its dig threshold from its own training digs, as if the hundreds of classified and excavated anomalies at earlier sites with the same munitions and soils had never happened.
**Tags:** #tacit-knowledge-ml #k-nearest-neighbors #gaussian-mixture-models #bayesian-inference #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to cut digs of harmless debris while holding DoD's zero-missed-target line, and whoever delivers the shortest defensible dig list under DAGCAP accreditation takes the munitions response task order.

## The Problem
After inversion and library matching, a classifier ranks every anomaly, and the project team chooses where to stop digging. To be safe, they dig a training set, then everything above a conservative threshold, plus validation digs below it. The threshold choice — where experienced classification geophysicists apply judgement about site-specific munitions, clutter types and data quality — drives the cost of the whole site, and it is made largely from that site's data alone.

## Why Nobody Has Built This
Every site's ground truth is filed in its own report and QAPP. Contractors hold their own projects but not competitors'; DoD holds all of them but organises them by installation. Library matching uses signatures, not the outcome history of decisions.

## What to Build
A cross-site decision record: for every classified anomaly at past sites, its polarizability features, library match metrics, the classifier's rank, the team's decision, and the dig result. Use it to estimate, for a new site's munitions list and clutter environment, how many training digs are needed and where the threshold can sit with a stated probability of zero misses, and to show reviewers the evidence.

## Target Customer
Classification leads at DAGCAP-accredited contractors; USACE and Navy reviewers who must approve thresholds.

## Impact If Built
Fewer training and validation digs per site at the same safety standard — weeks of excavation on sites where debris is about 95% of what is dug.
