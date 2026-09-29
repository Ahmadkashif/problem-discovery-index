# The Reach Number That Counts One Person Nine Times

**Niche:** [[niches/programmatic-ad-platforms/identity-and-addressability/profile|Identity & Addressability]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The campaign reports four million people reached, which is really eleven million partial identifiers belonging to an unknown smaller number of humans, presented without a caveat.
**Tags:** #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #quick-win #bayesian-inference #revenue-impact
**Contested on:** This niche is not terminal — assembling a legitimate deterministic graph and performing well with no identifier at all are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A brand campaign reports reach and frequency. Behind those numbers is a set of identifiers, some of which are cookies that reset weekly, some device identifiers, some hashed emails, some nothing at all — and the same person appears as several of them. Reach is therefore overstated and frequency understated, systematically, by an amount nobody quantifies. The advertiser plans the next campaign against the inflated reach and wonders why a channel that supposedly reached four million people moved nothing. The error is not random and is not small, and the report contains no indication that it exists.

## Why It's Still Broken
Reach is reported as a count because counting is what the system can do, and a count carries an implicit claim of exactness nobody intended. Overstated reach flatters every party in the chain. Deduplication across identity types requires the probabilistic machinery the category avoided. And nobody has been asked to state an uncertainty, so nobody does.

## What a Fix Looks Like
Report reach as an estimate with an interval. Estimate the duplication rate across identifier types from panels, authenticated subsets and identifier churn behaviour, which is measurable on a sample and is the input the whole fix rests on — the platform does not need to resolve every identity to correct the aggregate. Publish reach with a confidence interval rather than as a single number, which is the honest form and immediately changes how planners use it. Report frequency as a distribution, since a mean frequency over misattributed identifiers is the most misleading number in the standard report and the distribution shows the over-exposed tail that actually wastes money. Measure identifier churn directly, as a cookie lifespan of days is the dominant driver of inflation and is directly observable. Reconcile against an authenticated subset where one exists, which gives a calibration point most platforms have and do not use. State addressable coverage alongside reach, so the advertiser knows what share of delivery was even identifiable. Correct frequency capping for the same duplication, because capping on fragmented identifiers is why a person sees an advertisement forty times and is the most common complaint about the medium. Show planners the corrected figures next to the historical ones, since continuity matters and an unexplained drop in reported reach will be rejected. Standardise the disclosure across the industry, because a single honest platform is competitively punished for it. And test corrected reach against panel or survey measurement, which is the only external validation available.

## Who Feels the Pain
Advertisers planning against inflated reach; audiences seeing the same advertisement dozens of times despite a frequency cap; and platforms whose headline metric is systematically wrong in a knowable direction.

## Impact If Fixed
Reach is reported as a count because counting is what the system can do, and the count carries an exactness nobody intended. A duplication rate estimated on a sample corrects the aggregate without resolving every identity, and it fixes frequency capping at the same time.
