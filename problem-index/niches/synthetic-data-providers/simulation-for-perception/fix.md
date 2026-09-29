# Rare Events Generated Without a Target Distribution

**Niche:** [[niches/synthetic-data-providers/simulation-for-perception/profile|Simulation for Perception]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Simulation exists to cover the rare and dangerous cases, and what gets generated is whatever the scenario author thought of, against no measured distribution of what actually occurs.
**Tags:** #probability-distributions #monte-carlo-methods #evaluation-metrics #object-detection #descriptive-statistics #survival-analysis #confidence-intervals #quick-win
**Contested on:** Every serious competitor in this sub-niche is fighting to close the gap between rendered imagery and the real sensor stream so that a model trained on synthetic frames holds up in deployment — and whoever closes it takes the account, because the simulator is only worth what the transfer is worth.

## The Problem
The stated reason to simulate is coverage of the cases real collection cannot reach: the child stepping out from behind a parked van, the debris on the carriageway, the failure mode that appears once in ten million miles. What is generated is a scenario library written by engineers listing the cases they imagined, weighted by nothing, validated against nothing. The team reports twelve thousand rare scenarios covered. Nobody can say what fraction of real rare events that represents, whether the relative frequencies resemble reality, or which categories are absent entirely — which is the question the coverage claim is pretending to answer.

## Why It's Still Broken
The real distribution of rare events is, by construction, poorly characterised — that is what makes them rare — so there is no obvious reference to measure against. Scenario counts are easy to report and grow monotonically, which makes them a satisfying metric. Incident and near-miss data that would characterise the tail sits with fleet operators, insurers and regulators rather than with simulation vendors. And the absent category is invisible: nobody misses the scenario nobody thought of.

## What a Fix Looks Like
Build the target distribution and measure coverage against it. Assemble the reference from the sources that exist — crash and incident databases, near-miss reports, disengagement records, insurance claims, regulatory investigations — which is imperfect and is enormously better than a scenario list weighted by nothing. Report coverage as a fraction of that reference with named gaps, rather than as a count, so a team learns what is missing instead of how much was made. Weight generation by real frequency where it is known and by consequence where it is not, since uniform generation across imagined scenarios spends most of the budget on cases that do not occur. Mine the customer's own fleet data for near-misses and unusual conditions and feed them back as scenarios, which is the highest-value input available and is specific to their operating domain. Run an explicit gap analysis for categories with no scenarios at all, since the absent category is the dangerous one and finding it is a review exercise rather than a technical one. Track which generated scenarios the model still fails on after training, which is the only feedback that closes the loop. And stop reporting scenario counts as coverage, since the number grows without the coverage improving and it is the metric that has allowed this to persist.

## Who Feels the Pain
Perception and safety teams whose coverage claims are not evidence; the regulators and assessors receiving them; and the public in the operating domain where an absent category is an untested one.

## Impact If Fixed
Scenario counts grow without coverage improving. Building a reference distribution from incident and near-miss data — imperfect but real — turns a count into a measurement and makes the absent categories findable.
