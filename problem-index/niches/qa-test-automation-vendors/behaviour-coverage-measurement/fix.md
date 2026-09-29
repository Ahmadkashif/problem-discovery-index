# The Coverage Gate That Produces Empty Tests

**Niche:** [[niches/qa-test-automation-vendors/behaviour-coverage-measurement/profile|Behaviour Coverage Measurement]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A pipeline blocks changes that reduce coverage, so developers write tests that execute code and assert nothing, and the number goes up while the suite gets worse.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #quick-win #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to tell a team which behaviours that matter are actually verified — and whoever does that takes the quality function, because the universal metric reports lines executed and answers a different question.

## The Problem
The pipeline enforces a coverage threshold. A developer's change drops it below the line. The fastest way through is to add a test that calls the new function and asserts nothing, or asserts that it does not throw. The gate passes. Over two years this produces a suite in which a meaningful proportion of tests assert nothing at all, a coverage figure that is technically accurate and substantively meaningless, and a team that has learned that testing is a compliance exercise. Everybody involved knows this is happening.

## Why It's Still Broken
The gate was introduced to prevent coverage declining, which is a reasonable intent, and it measures the thing that is easy to measure rather than the thing it wants. Assertion-free tests are trivially detectable — a test with no assertion is a syntactic property — and nothing checks for them. The behaviour is also rational for the developer under the incentive they are given, so exhorting people not to do it does not work. And the resulting number satisfies whoever asked for the gate, which removes the pressure to look closer.

## What a Fix Looks Like
Measure the quality of the tests the gate produces. Detect assertion-free and trivially-asserting tests statically, which is straightforward and produces a count most teams would find uncomfortable — this alone changes the conversation. Gate on assertion quality as well as on coverage, so a test that executes a line without checking anything does not satisfy the threshold, which removes the cheapest path through. Prefer mutation-based gating for the code that matters, since a mutation score cannot be raised by an assertion-free test and is therefore not gameable in the same way — applied incrementally to changed code, it is affordable. Report the trend in assertion density alongside coverage, which shows whether the suite is getting stronger or merely larger. Exempt the code where testing genuinely adds little, explicitly and with a reason, since a blanket gate forces pointless tests on generated code and configuration and generates cynicism. And review what the gate produced after a quarter, because a gate that is producing empty tests is achieving the opposite of its intent and nobody has checked.

## Who Feels the Pain
Developers writing tests they know are worthless to pass a gate; teams whose suite is large and assertion-free; and organisations whose quality metric has been satisfied by exactly the behaviour it was meant to prevent.

## Impact If Fixed
Detecting assertion-free tests is a static check that produces an immediately uncomfortable and immediately actionable number. Gating on assertion quality removes the cheap path through, and incremental mutation scoring on changed code is affordable and is not gameable the same way.
