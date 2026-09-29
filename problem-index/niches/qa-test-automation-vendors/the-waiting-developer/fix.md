# A Pass That Conveys No Information

**Niche:** [[niches/qa-test-automation-vendors/the-waiting-developer/profile|The Waiting Developer]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The suite passes and the developer learns nothing, because nothing tells them whether any of the tests that passed actually exercised what they changed.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make a test result mean something to the developer receiving it — and whoever does that takes the engineering organisation, because a suite that is disbelieved provides no value regardless of what it costs.

## The Problem
A developer changes the discount calculation and the suite passes. They do not know whether any test exercised the discount calculation. They assume so, because there are eleven thousand tests and the coverage report says eighty-four percent. In fact the affected branch is covered by a test that exercises it incidentally and asserts nothing about the discount, so the change is unverified and the green result said otherwise. The developer had the information they needed — which tests touched the changed code and what they asserted — available and unpresented.

## Why It's Still Broken
A pass is reported as a property of the suite rather than as a statement about the change, because that is what the runner produces. Relating a change to the tests that exercised it requires per-test coverage, which most toolchains can produce and few collect because it is more expensive than aggregate coverage. Nobody has asked for the question to be answered at the moment it is asked. And a green result feels like information, which is why its emptiness goes unnoticed.

## What a Fix Looks Like
Report the pass as a statement about this change. Show which tests exercised the changed code, which is per-test coverage joined to the diff and is the answer to the developer's actual question. Show what those tests assert about it, distinguishing a test that exercises a line from one that verifies its result, which is the distinction between coverage and verification and is where the false assurance lives. Say plainly when a change is unverified — no test exercises this, or the tests that do assert nothing about it — which is far more useful than a green tick and is the report that would change behaviour. Suggest what to test, from the change's structure and from the behaviours the coverage analysis identifies as unverified. Report this in the review as well as to the author, since the reviewer is also assuming the suite covered it. And measure how often changes ship unverified, which is a number every organisation would find informative and none has.

## Who Feels the Pain
Developers reading a green result as assurance it does not provide; reviewers making the same assumption; and organisations whose escaped defects are in code the suite passed over without verifying.

## Impact If Fixed
Per-test coverage joined to the diff answers the question a developer is actually asking and is producible by most toolchains. Stating plainly that a change is unverified is more useful than a pass and is the report that would change what gets tested.
