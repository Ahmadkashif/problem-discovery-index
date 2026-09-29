# The Operational Half, Automated

**Niche:** [[niches/conversion-optimization-firms/experiment-operations/profile|Experiment Operations]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The thinking is the hypothesis and the analysis, and the time goes on everything between.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #change-point-detection #data-integration #compliance #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to run a continuous programme of tests without the setup, quality assurance and monitoring consuming the capacity, and whoever automates that takes the account.

## The Problem
Every test requires the same operational sequence: configure, instrument, quality-assure across devices, launch, watch for anomalies, check the traffic split behaved, apply the stopping rule, conclude, implement, archive. None of it is the hypothesis or the analysis, all of it is done by hand, and in most teams it is the constraint on how many tests can run rather than the traffic being the constraint.

## Why Nobody Has Built This
Platforms automate launching and reporting and leave the surrounding process to a checklist. Quality assurance of variants is manual by default. The checks that matter statistically — sample ratio, anomaly detection — are not run because nothing runs them. And the operational load is absorbed by the team.

## What to Build
Automate the sequence and make the statistical checks mandatory. Automate test configuration from a structured hypothesis so setup is generated rather than assembled, which is the core and removes the largest repetitive block. Quality-assure variants automatically across the devices and browsers that matter, which currently happens inconsistently and is where launch defects originate. Check for sample ratio mismatch continuously and halt the test when it appears, since a mismatched split invalidates the result and is the single most informative automated check available. Monitor for anomalies during a test — tracking failures, broken renders, traffic shifts — and alert rather than discovering them afterwards. Apply the stopping rule automatically rather than relying on someone to hold it, which is where the discipline breaks. Generate the result and the archive entry from the test's own record. Track the implementation of winners, which frequently does not happen and is invisible. Maintain the test register so the programme's history is queryable. Measure operational time per test, which is the number that shows where the capacity goes. And make the automated path the only path, since a manual bypass reintroduces everything.

## Target Customer
Conversion optimisation firms and in-house experimentation teams, testing platform vendors, programme operations, and workflow tooling providers.

## Impact If Built
The operational sequence rather than the traffic is what limits how many tests a team runs, and none of it is the hypothesis or the analysis. Generated setup with mandatory statistical checks removes the block and the malpractice together.
