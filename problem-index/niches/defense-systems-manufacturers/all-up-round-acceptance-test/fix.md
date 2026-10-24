# The Failure Retested Until It Passes

**Niche:** [[niches/defense-systems-manufacturers/all-up-round-acceptance-test/profile|All-Up-Round Assembly & Acceptance Test]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** Intermittent test failures that clear on retest are logged as "retest OK" and shipped, and the same signature returns later in the field or in another round.
**Tags:** #change-point-detection #k-nearest-neighbors #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get finished rounds through acceptance test the first time, and whoever raises first-pass yield at all-up-round acceptance test takes the account.

## The Problem
Under rate pressure, a round that fails a test and then passes on retest is often accepted after a review, and the failure is recorded as no fault found. Intermittent faults (a marginal connector, a harness chafe, a thermal issue) are exactly the ones that do this.

## Why It's Still Broken
Each retest decision is made round by round, with no view of how often the same test step and signature has cleared on retest elsewhere. Retest acceptance keeps the line moving, and nothing in the workflow counts its cost.

## What a Fix Looks Like
Track every retest-OK event by test step, signature, configuration and build attributes. Flag any signature that has cleared on retest more than a set number of times across rounds, and require a root-cause review before more rounds with that signature are accepted. Report retest-OK rates by station each week.

## Who Feels the Pain
Test engineers pressured to accept retests, quality managers answering field-failure investigations, and programme offices whose fielded rounds show the same faults.

## Impact If Fixed
Turning repeated retest-OK events into root-cause reviews catches intermittent faults while they cost a rework of a few thousand dollars, not a failed flight test or a field return costing a million dollars or more (estimate).
