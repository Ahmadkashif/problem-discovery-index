# Premium Interactions Nobody Tests

**Niche:** [[niches/payroll-platforms/regular-rate-premium-calculation/profile|Regular Rate & Premium Calculation]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Each premium is configured and verified on its own, and the defects are in the combinations — a differential on an overtime hour on a seventh consecutive day in a state with daily overtime — which nobody constructs a test for.
**Tags:** #combinatorics-and-counting #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #compliance #automation #quick-win
**Contested on:** Every serious competitor in wage calculation is fighting to compute the regular rate and every premium correctly for every jurisdiction an employer operates in — and whoever can prove a configuration matches the law takes the account.

## The Problem
An implementation verifies that overtime is calculated correctly, that the night differential is applied correctly, and that the meal premium triggers correctly. Each check passes. A nurse works a night shift that crosses midnight, exceeds the daily threshold, falls on her seventh consecutive day, and includes a missed meal period. What she should be paid is determined by how four rules interact, and no test was constructed for that combination because nobody enumerated the combinations. She is underpaid by a small amount, as is everyone on that pattern, every week.

## Why It's Still Broken
Verification is organised around features because implementation is organised around features, and the interactions belong to no feature. Enumerating combinations by hand is infeasible, which is why the generative approach in this sub-niche's buy note exists. And the affected patterns are frequently concentrated in specific populations — night shift, healthcare, seven-day operations — so the error affects a subset that is small enough not to be noticed and consistent enough to accumulate.

## What a Fix Looks Like
Enumerate the combinations that actually occur and test those. The employer's own timesheet history contains the shift patterns its people work, which is a far better test population than anything an analyst would construct: extract the distinct pattern signatures — crossing midnight, consecutive days, differential eligibility, threshold proximity, premium triggers — and generate a test case for each observed combination. That is a small, tractable set rather than a combinatorial explosion, because real workforces exhibit a limited number of patterns. Compute the expected result independently from the jurisdictional rules and compare against what the engine produced for the actual periods. Report divergence with the affected employees, the pattern, and the cumulative amount. Run it against historical periods first, which converts a testing exercise into a finding with a remediation list. And prioritise the patterns by headcount, since the population working the unusual combinations is exactly the one whose underpayment has gone unnoticed longest.

## Who Feels the Pain
Employees on night, weekend and seven-day patterns underpaid by small consistent amounts; payroll specialists who suspect the interactions are wrong and cannot enumerate them; and employers whose exposure concentrates in the workforces with the most demanding schedules.

## Impact If Fixed
Deriving test cases from observed timesheet patterns turns an intractable combinatorial problem into a bounded one, and running it retrospectively produces a remediation list rather than a testing report. The populations affected — shift workers in healthcare, manufacturing and continuous operations — are the ones least likely to have noticed and most likely to be owed.
