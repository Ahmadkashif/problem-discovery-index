# The Random Holdout That Stops Being Random

**Niche:** [[niches/life-insurance-carriers/accelerated-underwriting-programmes/profile|Accelerated Underwriting Programmes]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** The random holdout that measures slippage gets waived when producers complain or volumes spike, and the estimate quietly loses its validity.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #compliance #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to issue more applicants without fluids, exams or an APS while keeping audited mortality slippage inside the pricing load, and whoever proves the highest straight-through rate at a slippage the reinsurer will sign off takes the account.

## The Problem
A holdout sends a random share of accelerated-eligible cases through full underwriting. Producers dislike it because their client faces a blood draw a neighbour avoided, so exceptions creep in for large cases, favoured agencies and busy months. Post-issue audits get skipped when the APS cannot be retrieved. The remaining sample is no longer random, and slippage estimates built on it are biased in an unknown direction.

## Why It's Still Broken
Nobody monitors the holdout as a statistical instrument. Exceptions are granted case by case in new-business operations, while the slippage study is run by actuaries a year later from whatever was collected.

## What a Fix Looks Like
Log every holdout and audit selection with the random draw that triggered it and every exception with a reason. Report monthly on compliance with the design and on the characteristics of excepted cases. Then reweight or flag segments where exceptions break randomness.

## Who Feels the Pain
Programme actuaries signing slippage assumptions; reinsurers pricing the programme; chief underwriters defending eligibility expansions.

## Impact If Fixed
A small operational discipline protects the one number the whole programme is priced on.
