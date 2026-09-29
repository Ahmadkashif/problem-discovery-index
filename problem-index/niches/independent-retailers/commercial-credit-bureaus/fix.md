# Analysts Know Which Trade Lines to Distrust and Fix Them by Hand

**Niche:** [[niches/independent-retailers/commercial-credit-bureaus/profile|Commercial Credit Bureaus]]
**Industry:** [[industries/independent-retailers|Independent Retailers]]
**Type:** Fix (Pain Point)
**One-liner:** A supplier's reporting quietly changes and the analyst who notices fixes it in the pipeline, leaving no record that it happened.
**Tags:** #anomaly-detection #tacit-knowledge-ml #data-integration #worker-facing #automation

## The Problem
Trade payment data comes from thousands of suppliers, each extracting from their own accounts receivable system on their own schedule with their own conventions. It is contributed voluntarily, which means it is inconsistent and it cannot be demanded.

The failures are specific and recurring. A supplier changes billing systems and its days-beyond-terms figures shift for reasons that have nothing to do with its customers. One contributor reports invoice date where others report due date, making every customer look thirty days better. A supplier stops reporting for two months and the gap reads as an absence of activity rather than an absence of data. A large contributor writes off a batch and a thousand files move at once.

Analysts catch these. They know that this contributor's data always looks strange in January, that this one's aging buckets have been unreliable since a migration, that this one reports only its problem accounts. The knowledge is precise and it is entirely in the analysts.

## Why It's Still Broken
Contributors are volunteers and the network is the moat, so the relationship posture is not to question them. That is right as far as it goes and it has bled into not writing down what is questionable either.

Corrections are made in the pipeline as rules, exclusions, and adjustments, and the rules accumulate. Each was added by someone who understood a specific contributor's problem, and the reasoning was not recorded, so nobody dares remove one. The pipeline slowly becomes an archaeological site.

And quality work is invisible when it succeeds. The function is staffed to keep up rather than to improve, because a correction prevented does not appear in any metric.

## What a Fix Looks Like
Make contributor behaviour an explicit, monitored object and the corrections a record.

**A behavioural profile per contributor.** Reporting cadence, volume, aging distribution, and the conventions they actually use — maintained as data, not as analyst knowledge. Deviation from a contributor's own profile is the strongest available signal and is far more sensitive than any population-level check.

**Corrections as structured records.** What was wrong, which contributor, what class of problem, what was done, who did it, and when — accumulating into a labelled dataset the business has been generating for years and discarding at every step.

**Detect definitional drift, not outliers.** The failures that matter are correct-looking numbers reported under a shifted convention. They sit inside every range and are visible only against that contributor's history.

**Prioritize by effect on published scores.** A contributor supplying a small share of a thick file matters less than one supplying most of a thin one. Triage should follow influence on the output, which is a computation about scores rather than about records.

**Expire the rules.** Every pipeline correction should carry a reason and a review date, so the exclusion added for a 2019 system migration does not silently suppress good data in 2026.

## Who Feels the Pain
Data analysts, doing skilled work that leaves no trace and cannot be handed over. The head of data quality, whose function's capability is a set of tenures. Contributors, occasionally queried about data that was fine. And the businesses being scored, whose file moved because a supplier changed software.

## Impact If Fixed
This is a business whose entire value is that its numbers are trusted by people making credit decisions. Quality currently rests on individuals recognizing patterns they cannot articulate, across a contributor base that only grows. Turning that recognition into a monitored, learning system is the cheapest available improvement to the accuracy of scores that determine whether hundreds of thousands of small businesses can buy inventory on terms.
