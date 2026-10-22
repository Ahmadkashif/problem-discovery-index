# Requirements Ordered by a Grid Nobody Revisits

**Niche:** [[niches/life-insurance-carriers/life-underwriting-new-business/profile|Individual Life Underwriting & New Business]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Labs, exams and APS are ordered from an age-and-amount grid set years ago, so carriers pay for evidence that rarely changes a decision and skip evidence that would.
**Tags:** #logistic-regression #causal-inference #evaluation-metrics #feature-engineering #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to place each applicant in the right risk class faster, but writing it produces two contests with different winners: issuing more cases with no fluids or APS while holding mortality slippage, and turning the referred cases' medical records into a defensible class in days. Decomposed into contested sub-niches below.

## The Problem
Each requirement costs money and time: paramedical exams, blood and urine profiles and especially APS retrieval, which can add weeks and is a leading cause of applicants walking away (estimate). The grid was set on protective-value studies that predate prescription histories, medical-claims data and EHR retrieval.

## Why It's Still Broken
Changing the grid needs a protective-value study, the reinsurer's agreement and actuarial sign-off. Nobody owns the question between new-business operations, underwriting and pricing.

## What a Fix Looks Like
Measure, from the carrier's own cases, how often each requirement changed the class given the data already in hand. Then order evidence case by case where its expected protective value exceeds its cost and delay, and re-run the analysis every year.

## Who Feels the Pain
Applicants waiting weeks for a policy; producers losing placed cases; case managers chasing doctors' offices; underwriters reading files that never mattered.

## Impact If Fixed
Fewer, better-targeted requirements cut cycle time and per-case acquisition cost, and lift placement rates, with no change to mortality.
