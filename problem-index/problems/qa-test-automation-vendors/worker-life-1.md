# Test Engineer Repairing Rather Than Designing

**Industry:** [[qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Worker Life Changing
**One-liner:** Test automation engineers spend their weeks repairing tests broken by interface changes rather than designing the tests that would find the defects nobody has thought of.
**Tags:** #bert #gradient-boosting #large-language-models #k-means-clustering #graph-theory #evaluation-metrics #automation #worker-facing

## The Problem
A test automation engineer's week is repair. The suite ran overnight, forty tests failed, and each must be triaged: is this a real defect, a flaky test, or a test broken by a change that did not alter behaviour.

The last category dominates. A component library upgrade changed class names. A redesign moved elements. A field was renamed. Someone added a wrapper element. Each requires opening the test, understanding what it was verifying, finding the new way to reach the element, and repairing it — for dozens of tests, after every significant frontend change.

The triage itself is the slow part. Distinguishing a real defect from a structural break requires understanding both the test's intent and the change that occurred, and the failure output gives neither.

Meanwhile the work the engineer was hired for — designing test strategy, identifying risk areas, building the right coverage for a new feature, thinking about what could go wrong — happens in whatever time remains, which is little.

## Why It Matters to the Worker
Test automation engineering is a specialism with a low reputation that its practitioners generally find unjustified. Being seen as the people who maintain a fragile suite rather than as engineers who ensure quality is a persistent professional frustration, and the repair-dominated reality reinforces exactly that perception.

The position is also structurally powerless. The test engineer does not control the frontend changes that break the suite, and the developers making those changes bear none of the cost. That asymmetry produces a familiar dynamic where the test team is seen as an obstacle and the suite is seen as their problem.

And the work is visibly Sisyphean. The engineer repairs forty tests knowing the next redesign will break them again, and knowing that the suite's eventual abandonment is the historical norm.

## What a Solution Looks Like
Triage automated. Classifying a failure as a genuine defect, a flaky test or a structural break is the single largest time consumer and is determinable from the application change, the failure mode and the historical behaviour of the test.

Repairs proposed with evidence rather than applied silently. Where a change is confidently cosmetic, the fix should be drafted with the change shown; where it is not, the test should fail loudly and reach a human. Silent healing is what makes the current generation of these features dangerous.

Ownership shifted upstream. A change that breaks tests should surface to the developer making it, in the pull request, rather than to the test engineer overnight — which puts the cost where the decision was made and is the only durable fix for the asymmetry.

Test intent captured so repairs are possible at all. A test that records what behaviour it verifies, rather than only which selector it clicked, can be repaired meaningfully; one that records a selector cannot.

And maintenance cost measured per test, so the suite can be curated rather than allowed to collapse under its own weight.

## Impact If Solved
Test engineers are specialists spending their weeks on structural repair, which is why automated testing has a poor reputation and why suites are abandoned. Automating triage and moving the breakage cost to the developer who caused it addresses both the workload and the organisational dynamic that produces it.
