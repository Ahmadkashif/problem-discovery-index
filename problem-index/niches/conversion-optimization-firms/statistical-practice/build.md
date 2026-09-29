# Making the Correct Path the Easy One

**Niche:** [[niches/conversion-optimization-firms/statistical-practice/profile|Experiment Design & Statistical Practice]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform makes launching, peeking and stopping trivial, and each of those is where the error comes from.
**Tags:** #hypothesis-testing #confidence-intervals #probability-distributions #evaluation-metrics #bayesian-inference #descriptive-statistics #automation #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to run experiments whose conclusions their data actually supports, against tooling that makes the opposite easy — and whoever makes good practice the fast path takes the account.

## The Problem
The bad practices are not ignorance; they are the path of least resistance. The platform shows a running significance figure, so people look. Looking and stopping when it crosses inflates the error rate. Segmenting after the fact until something is significant is one click. Launching without a power calculation is the default because the platform does not ask. Practitioners frequently know all of this and the workflow defeats them.

## Why Nobody Has Built This
Platforms optimise for ease of launching and declaring, which is what customers ask for. Correct sequential methods exist and are not the default anywhere. Power analysis requires an effect size estimate nobody wants to commit to. And a platform that reports fewer wins sells worse.

## What to Build
Put the guardrails in the workflow rather than in a training course. Require a power analysis and a minimum detectable effect before a test can launch, which is the core and prevents the largest category of worthless tests outright. Use properly sequential methods so continuous monitoring is valid rather than forbidden, since prohibiting looking does not work and correct sequential designs exist. Fix the stopping rule at design time and hold it, which is what early stopping violates. Require segments to be specified in advance, and correct for the ones examined. Report the effect with an interval rather than a point uplift, which is the honest output and changes how results are discussed. Warn when a test cannot detect an effect worth having, which is most low-traffic tests and is knowable before launch. Report the false positive rate the workflow implies, so the practitioner sees what their choices cost. Refuse to declare a winner where the data cannot support one, which is the guardrail with teeth. Make the correct path faster than the incorrect one, because that is the only mechanism that changes behaviour at scale. And report null results in the same format as wins, so the record is not selected.

## Target Customer
Conversion optimisation firms and in-house experimentation teams, testing platform vendors, product and marketing leadership, and statistical tooling providers.

## Impact If Built
The bad practices are the path of least resistance rather than ignorance, and the workflow defeats practitioners who know better. Power requirements and valid sequential methods in the tool make the correct path the fast one.
