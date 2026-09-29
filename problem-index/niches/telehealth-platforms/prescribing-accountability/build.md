# Build: Case-Mix-Adjusted Prescribing Analytics

**Niche:** [[niches/telehealth-platforms/prescribing-accountability/profile|Prescribing Pattern Accountability]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compute the platform's prescribing rates by presentation against clinical benchmarks, adjusted for case mix, with clinician-level outlier detection and a governance process attached.
**Tags:** #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #causal-inference #compliance #gradient-boosting
**Contested on:** Whether case mix can be adjusted well enough that an outlier finding is defensible against the clinician it names.

## The Problem

A telehealth platform writes a large number of prescriptions and has no characterisation of them. It cannot say what share of its visits for a sore throat end in an antibiotic, how that compares to guideline-concordant practice, whether that rate differs between its clinicians by more than case mix explains, or whether it has moved since the compensation structure changed.

The absence matters in three directions. Clinically, an outlier clinician is only discovered when a complaint arrives. Commercially, a payer or employer asking about prescribing appropriateness receives an assurance rather than a number. And in regulatory terms, a platform under scrutiny about its prescribing is in a materially weaker position if it has never looked.

## Why Nobody Has Built This

Because the number might be bad, and once computed it exists. A platform whose prescribing for a given condition runs well above clinical norms would hold that finding in writing, in a segment where federal enforcement has already occurred. The legal calculus around creating that record is not straightforward and the path of least resistance is well worn.

The methodological obstacle is real as well. A raw prescribing rate is not evidence of anything — telehealth populations are self-selected, present differently, and a platform serving people who could not get a same-day appointment elsewhere has a genuinely different case mix. Producing a defensible comparison requires adjustment, and doing it badly produces a finding that the named clinician can dismantle, which is worse than no finding.

And the governance is undefined. Nobody has decided what happens to an outlier, so nobody wants to identify one.

## What to Build

A measurement programme with the adjustment done properly and the governance designed first.

**Define the presentation cohorts.** Prescribing rate is only meaningful within a presentation — upper respiratory symptoms, urinary symptoms, dermatological complaints, behavioural health presentations, each with its own guideline-concordant expectation. Cohort definition from structured intake and encounter data is the foundation and requires clinical input rather than data engineering.

**Benchmark externally.** Guideline-concordant rates from professional bodies, published in-person benchmarks from the ambulatory literature, and payer data where a contract permits. Without an external anchor the platform can only compare clinicians to each other, which detects outliers and cannot detect a whole platform that is out of line.

**Adjust for case mix seriously.** Patient age, comorbidities, symptom duration and severity, prior treatment, geography, time of day, and whether the patient had other access to care. Hierarchical modelling with clinician as a random effect and heavy shrinkage, so that a clinician with 200 encounters is not compared as though they had 5,000. The output should be a posterior with an interval, and most clinicians should be indistinguishable from the mean — that is the correct result and it makes the genuine outliers credible.

**Look for structural drivers, not only individual ones.** Does the rate differ by time of day, by queue length, by compensation structure, by whether the visit was synchronous or asynchronous, by subscription tier? A prescribing rate that rises with throughput pressure is a finding about the business model, and it is the more important one.

**Design the governance before running it.** What threshold triggers review, who reviews, what evidence standard applies, what the clinician is told and when, what appeal exists, and what is retained. Deciding this first is what makes the programme survivable and fair; deciding it during the first outlier case is what ends it and damages someone.

**Start with the platform-level number.** Aggregate rates by presentation against benchmark, with no clinician attribution at all, is the first deliverable. It answers the question that matters most, creates far less individual jeopardy, and is what a regulator or payer will ask for.

## Target Customer

Platform legal, compliance and medical leadership — driven by regulatory exposure rather than by clinical enthusiasm, which is the honest account of why this gets built. Also payers and employers contracting for virtual care, who are beginning to ask for prescribing appropriateness reporting and currently receive assurances.

## Impact If Built

The platform can state what it prescribes and how that compares, which is the question it will be asked and currently cannot answer. Genuine clinical outliers become visible before a complaint arrives. And structural drivers — a prescribing rate that moves with throughput or with compensation — get surfaced as facts about the business model rather than as suspicions about individuals.
