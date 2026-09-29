# The Sample Ratio Nobody Checked

**Niche:** [[niches/conversion-optimization-firms/experiment-operations/profile|Experiment Operations]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The split was meant to be fifty-fifty and the variant got forty-six percent, which invalidates the whole test.
**Tags:** #quick-win #hypothesis-testing #automation #evaluation-metrics #descriptive-statistics #confidence-intervals #change-point-detection #data-integration
**Contested on:** Every serious competitor in this niche is fighting to run a continuous programme of tests without the setup, quality assurance and monitoring consuming the capacity, and whoever automates that takes the account.

## The Problem
A test configured for an even split delivers an uneven one. The cause is usually mechanical — the variant failed to load for some users, a redirect dropped traffic, a bot filter behaved differently between arms — and whatever it is, the groups are no longer comparable and the result is invalid. The check that detects this is a single statistical test on the traffic counts, it takes seconds, and it is not run in most programmes.

## Why It's Still Broken
The check is not in the workflow — a test that is invalid for a mechanical reason reports a result exactly like a valid one, and nothing computes the one number that would reveal it. Platforms display the split without testing it. Practitioners may not know the check exists. And a mismatch usually accompanies an interesting result, which discourages looking.

## What a Fix Looks Like
Run the check automatically and halt on failure. Test the observed split against the configured split continuously and alert on a significant mismatch, which is the fix and is a standard calculation taking seconds. Halt the test rather than warning, since a mismatched test cannot produce a valid result and continuing wastes traffic. Diagnose the common causes — variant load failure, redirect loss, bot filtering, assignment errors — which are a small set and are usually identifiable quickly. Check at the start and continuously, as the mismatch frequently appears only at volume. Report the split in every result so a reader can see it was checked. Exclude any test with an unresolved mismatch from the reported results rather than including it with a caveat. Check ratios within segments too, where the mismatch is sometimes confined. Record how many tests failed the check, which is usually a striking share and makes the case for everything else. Add it as a launch gate so a mismatch found early stops the test before traffic is wasted. And treat a mismatch as an invalidation rather than an anomaly.

## Who Feels the Pain
Clients acting on results from invalid tests; analysts who suspected something and had no check; the reported uplift figures, contaminated by tests that never should have concluded; and the traffic, spent on a test that could not produce an answer.

## Impact If Fixed
A test that is invalid for a mechanical reason reports a result exactly like a valid one, and nothing computes the number that would reveal it. A continuous ratio check that halts on failure is seconds of computation per test.
