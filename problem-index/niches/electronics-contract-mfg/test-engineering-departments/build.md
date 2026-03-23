# Test Failure Root Cause Classifier

**Niche:** [[niches/electronics-contract-mfg/test-engineering-departments/profile|Test Engineering Departments]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automatically classifies ICT/FCT test failures by root cause category (component defect, process defect, test artifact) — test engineers manually investigate each failure, and 30-50% of failures turn out to be test artifacts (intermittent probe contact, marginal test limits) rather than real product defects.
**Tags:** #gradient-boosting #multiclass-classification #tacit-knowledge-ml #automation

## The Problem
When a board fails an ICT or FCT test step, the test engineer must determine: is this a real component defect (wrong value, open, short), a process defect (solder joint issue, placement error), or a test artifact (intermittent probe contact on the fixture, test limit set too tight, measurement noise)? An experienced test engineer recognizes patterns — a failure that occurs only on pin 3 of a specific connector across multiple boards is likely a fixture probe issue, while a resistance measurement that is consistently 5% high suggests a component lot variation rather than a defect. This pattern recognition takes years to develop and is the most time-consuming part of test engineering because every failure must be investigated before the board can be dispositioned.

## Why Nobody Has Built This
Test failure data (test step, measured value, limit, pass/fail) is logged by ICT/FCT systems, but the root cause classification is recorded informally (if at all) in the test engineer's notes. Building a classifier requires labeled training data: historical failures with confirmed root cause categories. This labeled data does not exist in structured form — it exists in the test engineer's memory and in scattered investigation notes. A data labeling effort is required before any model can be trained.

## What to Build
A failure classification system that ingests test failure data (test step, measured value, limit, board serial, time), correlates with production data (component lot, SMT machine, reflow profile, fixture maintenance history), and classifies each failure into root cause categories (component defect, process defect, test artifact — with sub-categories). Initial model trained on retrospective labeling by experienced test engineers. Deployed as a recommendation system: when a failure occurs, the model suggests the most probable root cause with supporting evidence, and the test engineer confirms or corrects — building the training dataset iteratively.

## Target Customer
Test engineering managers at EMS providers with 3+ test engineers and 50+ active test programs. Approximately 200-300 US EMS facilities at this scale. Average contract value: $40-80K/year.

## Impact If Built
Test failure investigation time decreases by 40-60%. Test artifact identification becomes immediate (rather than requiring physical investigation), eliminating unnecessary rework on boards that passed actual quality criteria. Test engineer productivity doubles — each engineer can support 2x the program portfolio.
