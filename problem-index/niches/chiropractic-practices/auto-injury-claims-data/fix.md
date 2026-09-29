# Contributed Data Quality Is Assumed, Never Measured

**Niche:** [[niches/chiropractic-practices/auto-injury-claims-data/profile|Auto Injury Claims Data & Medical Review Analytics]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Fix (Pain Point)
**One-liner:** The whole repository is contributed by hundreds of insurers on their own schedules with their own coding conventions and their own definitions of a reportable claim, and nobody characterizes how much each contributor's practice distorts the benchmarks built from it.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #change-point-detection #probability-distributions #evaluation-metrics #gaussian-mixture-models #data-integration #compliance #automation

## The Problem
The vendor's authority rests on completeness — a repository covering effectively the whole market. Completeness is a claim about coverage, not about comparability, and the two get conflated. Contributors differ in when they report, how they code closure and reserve fields, which claim types they submit, how they populate optional fields, and how consistently they do any of it over time. A large contributor changing its claims system alters the composition of the repository in ways that propagate into every benchmark computed from it, and the change registers as a market trend rather than as a data artifact. There is validation at ingest for format and referential integrity; there is nothing that characterizes contributor practice or measures its effect on published outputs.

## Why It's Still Broken
Data contribution is a relationship business — contributors are also customers, and telling one that its data is idiosyncratic is a commercially awkward conversation nobody is incentivized to start. Measuring the effect also requires a counterfactual, since there is no external ground truth for what the market actually looks like; the tractable approach is comparative, using overlap and consistency between contributors, and that is analytical work nobody has been assigned. Meanwhile the ingest pipeline reports green because it is checking the things a pipeline can check.

## What a Fix Looks Like
Contributor practice characterized as a measured, monitored property rather than assumed. Each contributor carries a profile: reporting lag distribution, field population rates, coding convention fingerprints, claim type mix, and how all of that has moved over time — with change detection on the profile itself, so a contributor's system migration is caught as a data event before it becomes a published trend. Benchmarks then carry composition metadata stating which contributors and what mix they rest on, and sensitivity analysis reports how much a given published figure would move if the largest contributors were reweighted. Where a benchmark is materially dependent on one contributor's practice, that is a fact the product should surface rather than hide. Contributors receive their own profile back as a service, which is what makes the awkward conversation into a valuable one — most of them do not know their coding practice is unusual either.

## Who Feels the Pain
Analysts investigating benchmark movements that turn out to be a contributor's system change; clients pricing and litigating against figures whose composition they cannot see; the research function whose published studies inherit unmeasured composition effects; and the vendor's authority, which is entirely a claim about data quality that it does not currently measure.

## Impact If Fixed
Protects the only thing the business actually sells. Composition transparency also converts a latent vulnerability into a differentiator — in a market where benchmarks are challenged in litigation, a vendor that can characterize its own data's composition and sensitivity is in a materially stronger position than one asserting completeness. And contributor profiling improves the input at source, which improves everything computed from it.
