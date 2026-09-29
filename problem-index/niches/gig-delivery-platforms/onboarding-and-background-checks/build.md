# Build: Accuracy Measurement and Proportionate Adjudication

**Niche:** [[niches/gig-delivery-platforms/onboarding-and-background-checks/profile|Onboarding, Background Checks & Identity]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Measure how often screening excludes the wrong person, and set adjudication rules against the actual relationship between a record and delivery outcomes rather than against a conservative guess.
**Tags:** #descriptive-statistics #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #compliance #automation
**Contested on:** Whether the platform will measure the accuracy and the predictive value of screening decisions it currently makes on faith.

## The Problem

Screening decisions are made against an adjudication matrix — this record type, within this many years, disqualifies — and the matrix is set conservatively by legal judgement. Two things about it are unmeasured.

The first is accuracy. Background data in the US comes from county and state sources with known quality problems: records misattributed to people with similar names or dates of birth, sealed or expunged matters that continue to surface, and dispositions never updated so a dismissed charge reads as pending. The platform does not know what share of its exclusions are wrong, because a wrongly excluded applicant who does not dispute leaves no trace.

The second is predictive value. No platform has established whether the records it disqualifies on actually predict anything about delivery outcomes — safety incidents, theft, customer harm. The matrix encodes an intuition about risk that has never been tested against the platform's own incident record, and it excludes large numbers of people on that basis.

## Why Nobody Has Built This

Measuring accuracy requires knowing the truth about people you rejected, which is hard by construction. It is not impossible — dispute outcomes, re-application results and audit sampling all produce signal — but it requires deliberate effort against a population the platform has already turned away and has no further relationship with.

Measuring predictive value is methodologically harder and institutionally forbidding. It requires observing outcomes for people who were admitted with records, which exists where matrices differ by jurisdiction or have changed over time, but the legal department's view of running that analysis is usually unenthusiastic: a finding that a disqualifying category does not predict incidents creates pressure to admit those applicants, and a finding that it does is discoverable.

And nobody is accountable for exclusions. Supply growth is measured on completed onboardings, trust and safety on incidents. The people rejected are in neither team's numbers.

## What to Build

An accuracy and proportionality measurement programme with the adjudication matrix as its output.

**Measure accuracy directly.** Sample adverse decisions and audit them against primary sources — actual court records rather than the aggregator's report. This is the only way to see the misattribution and stale-disposition rate, it is a bounded ongoing cost, and it produces the number nobody has. Track dispute rates and outcomes by cohort too, and correct for the fact that disputes come disproportionately from the confident and the English-speaking, which means the raw dispute-success rate understates the error rate against everyone else.

**Measure predictive value where variation exists.** Adjudication matrices differ across jurisdictions and have changed over time, which creates natural comparisons: cohorts admitted with a record type under one rule set against the incident rates of cohorts without. Survival analysis on time-to-incident is the right frame. Where the record type does not separate the curves, the exclusion is costing supply and buying nothing.

**Rebuild the matrix on the evidence.** Recency weighting that reflects the observed decay of predictive value, relevance to the actual work rather than to a generic risk posture, and severity thresholds set where the data supports them. Fair-chance hiring laws in several jurisdictions already require individualised assessment for some categories, and the evidence base makes that assessment defensible rather than arbitrary.

**Instrument the funnel.** Application to decision by stage, by cohort, with the exclusion reasons. Most platforms cannot currently state how many applicants they reject for screening reasons, or how that varies by market and demographic — a number that is both a business metric and, increasingly, a regulatory one.

## Target Customer

Platform trust and safety jointly with supply growth, since the matrix is a trade between their objectives currently decided unilaterally by legal. Also the screening vendors, for whom accuracy measurement and evidence-based adjudication guidance is a real differentiator in a category competing on turnaround time and price.

## Impact If Built

The platform learns its own false-exclusion rate, which is currently unknown and is a live legal exposure as much as a moral one. Adjudication rules get set against evidence rather than against a conservative guess, which admits people the data says are fine and keeps out those it says are not. And a large, invisible population of people excluded from an income source by a records error gets a process that is measured.
