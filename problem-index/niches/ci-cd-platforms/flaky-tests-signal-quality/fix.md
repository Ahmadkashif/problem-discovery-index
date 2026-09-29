# Quarantine With No Way Out

**Niche:** [[niches/ci-cd-platforms/flaky-tests-signal-quality/profile|Flaky Tests & Signal Quality]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Flaky tests are quarantined so they stop blocking merges, the quarantine has no exit process, and coverage erodes silently as the quarantined set grows every quarter.
**Tags:** #descriptive-statistics #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to make a pipeline failure mean something again — and whoever does that takes the platform account, because once engineers learn to re-run rather than investigate, every other capability in the category is built on a signal nobody trusts.

## The Problem
A flaky test blocks merges, so it is quarantined: it still runs, its result no longer fails the build. This is a sensible immediate response. Nothing then happens. A year later the quarantine contains four hundred tests, some of which are not flaky at all and are failing consistently because the behaviour they test has been broken for months, and nobody knows which. The suite reports high coverage. The effective coverage — tests whose failure would actually stop a change — is substantially lower and nobody has computed it.

## Why It's Still Broken
Quarantine is an escape hatch and escape hatches rarely get a return path, because the urgency that motivated the quarantine disappears the moment it works. The owning team has no incentive to revisit a test that is no longer blocking them. Nobody reports the quarantined set's size or age. And the most dangerous case — a quarantined test that is now failing deterministically because of a real defect — is indistinguishable from an ordinary quarantined flake unless somebody looks at the pass rate.

## What a Fix Looks Like
Give quarantine a lifecycle. Time-box every entry, with an expiry that returns the test to blocking status or deletes it, so the decision is revisited rather than forgotten — which is the whole fix and is a policy the platform can enforce. Report the quarantined set continuously: size, age distribution, owner, and trend, which makes the erosion visible. Distinguish flaky from consistently failing within the quarantine by pass rate, since a quarantined test failing every time is a broken feature nobody knows about and is the highest-value finding here. Compute effective coverage — the proportion of the suite whose failure would actually block a change — and report it alongside nominal coverage, because the gap between the two is the honest picture. Require an owner and a reason at quarantine time, which costs nothing and makes the eventual review possible. And surface the quarantined tests relevant to a change, so an engineer touching that code knows the tests covering it are not enforcing anything.

## Who Feels the Pain
Teams whose test suite reports coverage it does not provide; engineers whose changes are not actually tested by the tests they assume are running; and organisations that discover during an incident that the relevant test has been quarantined since March.

## Impact If Fixed
Time-boxed quarantine with enforced expiry is a policy change that prevents the accumulation entirely. The flaky-versus-consistently-failing split within the existing quarantine is a single query and regularly finds real defects that have been hidden for months.
