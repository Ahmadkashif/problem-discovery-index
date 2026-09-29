# The Traceability Matrix Maintained by Hand

**Niche:** [[niches/qa-test-automation-vendors/non-web-and-regulated-testing/profile|Non-Web & Regulated Testing]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A spreadsheet links every requirement to its tests, is updated by hand, is wrong within a fortnight of any change, and is the artefact the audit depends on.
**Tags:** #graph-theory #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to bring modern test automation to software that runs on hardware and must produce regulatory evidence — and whoever does that takes those industries, because the category's tooling assumes a browser and they do not have one.

## The Problem
The traceability matrix has eleven hundred rows linking requirements to design elements to tests. It is maintained by a quality engineer who updates it when told about changes. Requirements change, tests are renamed, code is refactored, and the matrix drifts — silently, because nothing verifies it. Before an audit it is reconciled by hand over several weeks, which is when the gaps are found: requirements with no test, tests linked to requirements that no longer exist, and links that were correct before a refactor.

## Why It's Still Broken
The matrix lives in a document or a requirements tool and the tests live in a repository, and the link is a string somebody typed. Nothing checks that a referenced test exists, that a requirement still exists, or that the test actually exercises what the requirement describes. Maintaining it is a role rather than a mechanism, which makes it as accurate as the communication into that role. And the audit reconciliation, though expensive, works, which removes the pressure to make it continuous.

## What a Fix Looks Like
Make the links live and verified. Declare the link in the test itself rather than in a separate matrix, so it moves with the code and cannot refer to a test that no longer exists — this is the structural fix and turns maintenance into a compile-time property. Validate continuously that every referenced requirement exists, every requirement has at least one test, and every test's link resolves, which is a build step and turns a fortnightly drift into an immediate failure. Detect stale links after a refactor by checking that the test still exercises the code implementing the requirement, which requires the coverage join and catches the subtle case. Generate the matrix from the verified links rather than maintaining it, which removes the artefact as a thing to maintain while keeping it as a thing to produce. Report coverage against requirements continuously, so a requirement without a test is visible the day it appears rather than during the audit. And keep the history, since demonstrating that the traceability was maintained throughout is a stronger position with an auditor than producing a correct matrix at the end.

## Who Feels the Pain
Quality engineers maintaining a matrix by hand; teams reconciling it for weeks before an audit; and organisations whose regulatory evidence rests on a spreadsheet nobody verifies.

## Impact If Fixed
Declaring links in the tests makes them verifiable at build time and eliminates drift structurally. Continuous validation turns the pre-audit reconciliation into a build failure on the day the gap appears, which is both cheaper and a better compliance position.
