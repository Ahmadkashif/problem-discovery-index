# Behaviour Coverage Measurement

**Parent Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to tell a team which behaviours that matter are actually verified — and whoever does that takes the quality function, because the universal metric reports lines executed and answers a different question.

## Profile
**Market Size:** ~$520M US attributable to coverage and quality measurement
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Low in substance — coverage tooling is universal and universally misinterpreted
**Target Buyer:** Quality engineering and engineering leadership
**Automation Potential:** High — behaviours are enumerable from requirements, code and usage

## What Makes This a Distinct Niche
Coverage tooling is universal, accurate and reports lines executed, which tells a team nothing about whether the behaviours that matter are actually verified. A line can be executed by a test that asserts nothing. A module can be at ninety percent coverage with the important conditional untested. A critical user journey can be uncovered entirely while the utility functions it calls are exhaustively covered. Everybody involved knows the metric is weak and it is reported anyway, because it is free, precise and the only number available — the same pattern as downloads, pass rates and cache hit ratios elsewhere in this vault. The contest is a measure of what is verified rather than what is executed, which requires enumerating the behaviours that matter, and that enumeration is the work nobody has done.

## Current Tools & Gaps
Line, branch and statement coverage in every language; coverage gates in pipelines; and mutation testing in a small minority. The gaps: coverage measures execution and is read as verification, which is the central misinterpretation; the behaviours that matter are not enumerated anywhere, so there is nothing to measure coverage against; risk is not weighted, so coverage of a payment path and of a logging utility count equally; user journeys and requirements are not connected to tests, so nobody can say whether a requirement is verified; and coverage gates produce tests written to raise the number rather than to verify anything.

## Problems
- [[niches/qa-test-automation-vendors/behaviour-coverage-measurement/build|🔨 Build: Lines Executed, Behaviours Unknown]]
- [[niches/qa-test-automation-vendors/behaviour-coverage-measurement/buy|🛒 Buy: Requirements Traceability, Which Regulated Industries Already Do]]
- [[niches/qa-test-automation-vendors/behaviour-coverage-measurement/fix|🔧 Fix: The Coverage Gate That Produces Empty Tests]]
