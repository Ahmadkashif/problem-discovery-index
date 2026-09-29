# Assertions That Lock In Current Behaviour

**Niche:** [[niches/qa-test-automation-vendors/ai-generated-and-self-healing/profile|AI-Generated & Self-Healing Tests]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A generated test asserts that the page contains the text it currently contains, which means a defect present at generation time becomes the expected behaviour forever.
**Tags:** #descriptive-statistics #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #automation #cross-validation
**Contested on:** Every serious competitor here is fighting to make a test that writes and repairs itself trustworthy enough to rely on — and whoever does that takes quality engineering, because a suite that heals past a regression is worse than no suite and the category has already failed this promise twice.

## The Problem
A suite is generated against the running application. It asserts the current text, the current element positions, the current response values. Among the behaviours it captures is a rounding error in a total, a mislabelled field and an off-by-one in a paginated count — all present on the day of generation and all now enshrined as expected. When somebody fixes the rounding error, the test fails, and the fix is questioned because the test says the old behaviour was correct. The suite has become a mechanism for preserving defects.

## Why It's Still Broken
Asserting current behaviour is the only oracle available without a specification, and it produces an immediately impressive suite, which is what the tooling is judged on. The assertions are also not labelled, so a team cannot tell which of their tests encode a requirement and which merely record a snapshot. And the failure is delayed: the suite looks correct until somebody tries to change something, at which point the accumulated snapshot assertions resist every improvement.

## What a Fix Looks Like
Label the assertions and constrain what is recorded. Distinguish assertions derived from intent — documentation, requirements, naming, prior tests — from those recording current behaviour, and mark them in the test itself, so a failing snapshot assertion is understood as a change rather than as a defect. Assert less: a generated test that checks that a total is numeric and positive is more durable and nearly as useful as one that checks it equals a specific figure recorded on a Tuesday. Prefer properties and invariants where they can be inferred, since these survive change and are what a maintainer would have written. Require review of generated assertions before they become blocking, which is the practice that would prevent enshrining defects and is skipped because the volume makes review feel impractical — which is an argument for generating fewer and better. Flag assertions that look like they may be recording a defect, such as an unusual value or an inconsistency between related assertions, which is detectable and is currently nobody's check. And re-derive rather than repair when intent changes, since a snapshot assertion repaired to match new behaviour is simply a new snapshot.

## Who Feels the Pain
Teams whose generated suite resists every fix; developers arguing with a test that asserts a defect is correct; and organisations whose large generated suite verifies that the application still does what it did on the day of generation.

## Impact If Fixed
Labelling assertion provenance costs nothing and changes how every failure is interpreted. Asserting less produces a more durable suite, and flagging assertions that may encode defects is a check nobody performs at the moment when it is cheapest.
