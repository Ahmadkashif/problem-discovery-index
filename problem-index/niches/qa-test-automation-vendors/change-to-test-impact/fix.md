# Interface Changes Are Invisible to Code Coverage

**Niche:** [[niches/qa-test-automation-vendors/change-to-test-impact/profile|Change-to-Test Impact]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Test impact analysis works from code coverage, most end-to-end test breakage comes from markup and styling changes, and coverage instrumentation does not see any of it.
**Tags:** #graph-theory #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #automation #data-integration
**Contested on:** Every serious competitor here is fighting to model the relationship between an application change and the tests it affects — and whoever does that takes the category, because that relationship is its central object and is modelled nowhere.

## The Problem
A team adopts test impact analysis to shorten their pipeline. It works well for unit tests, where coverage instrumentation relates code to tests precisely. It is useless for the end-to-end suite, which is where the duration actually is, because those tests break when a component is renamed, a class changes or a layout is restructured — none of which appears in code coverage. The team runs the full end-to-end suite on every change, which is the suite that takes forty minutes, and the impact analysis addresses the eight-minute one.

## Why It's Still Broken
Coverage instrumentation was built to measure code execution and the interface is data rather than code from its perspective. The relationship that would help — which interface elements a test depends on and which elements a change touches — is entirely obtainable, since the test's selectors state its dependencies and the diff states what changed, and nobody has joined them. Impact analysis products were built by teams whose reference case was unit testing. And the end-to-end suite's duration is experienced by developers rather than owned by anyone.

## What a Fix Looks Like
Build the interface-level dependence relationship, which is simpler than the code one. Extract each test's interface dependencies from its selectors and interactions, which is a parse of the test and produces the set of elements, attributes and text it relies on. Extract what an interface change touches from the diff — components, identifiers, classes, structure, text — which is equally mechanical. Intersect them to select the end-to-end tests a change could affect, which is the impact analysis the category needs and which nothing performs. Handle indirection, since selectors are frequently constructed dynamically and a page object layer sits between the test and the markup, which requires following the abstraction and is the main engineering difficulty. Combine with the historical relationship, which covers the cases the static analysis misses. Validate in shadow mode as the CI selection niche describes, reporting how often a skipped test would have failed, since that is the evidence a team needs before trusting the selection. And use the same relationship for repair classification, since a test whose only dependency was renamed is a different case from one whose element disappeared.

## Who Feels the Pain
Teams whose impact analysis helps the fast suite and not the slow one; developers waiting forty minutes for tests unrelated to their change; and vendors selling selection that does not cover the case where selection is worth most.

## Impact If Fixed
The interface dependence relationship is simpler than the code one and is derivable from the tests and the diff, and it covers precisely the suite where the duration is. Validating in shadow mode is what makes a cautious team willing to skip anything.
