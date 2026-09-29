# Coverage Measurement

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether an engagement can state how much of the attack surface it actually reached, by what technique and at what depth, from evidence produced while the testing happened.

## Profile

**Market Size:** ~$900M
**Share of Parent Industry:** ~15%
**Digital Adoption:** Very low — no denominator is computed
**Target Buyer:** Testing firm leadership, client security leadership, cyber insurers
**Automation Potential:** Very high — the evidence is in the tester's own traffic

## What Makes This a Distinct Niche

This is the input-side half of assessment assurance: at the end of two weeks, what did this engagement actually examine, and what is a clean result in each area worth.

It is separable from its sibling in every dimension. [[niches/penetration-testing-firms/remediation-verification/profile|🎯 Remediation Verification]] is about what happened to findings after delivery — a corpus problem across a client boundary that returns nothing for a year. Coverage is a measurement problem inside a single engagement, computable from the tester's own proxy logs and tool output, answerable the day the work ends, and immediately testable: run a longer engagement on the same estate and see whether the areas marked thin were where the additional findings came from.

The contest is over whether a denominator can be constructed at all. Counting hosts is trivial and close to meaningless. What matters is reachable states, parameter combinations, authenticated roles, business logic paths and the techniques attempted against each — and none of those has a natural total. Every serious attempt has to make defensible modelling choices about what the surface is, and whoever makes them credibly enough that clients and insurers accept the output has established the measure the whole industry reports against.

## Current Tools & Gaps

Testers work through intercepting proxies that log every request they make, run tooling that records what was scanned, and increasingly map findings to MITRE ATT&CK techniques. All of the raw material for coverage measurement is already produced and is discarded at engagement end.

Adjacent tooling is closer than it looks. Attack surface management platforms enumerate external assets continuously and give a partial denominator. API specifications, where they exist, enumerate endpoints and parameters precisely. Code coverage instrumentation solves the identical problem for software testing and is universally understood by the audience these reports reach.

The gaps: nothing aggregates the tester's own traffic into a coverage statement. Nothing distinguishes an endpoint that was fuzzed from one that was requested once. ATT&CK mapping records techniques that produced findings and not techniques attempted without success, which is the distinction that turns a taxonomy into a coverage measure. Nobody estimates what the enumeration itself missed. And no firm has calibrated what a clean result at a given depth is actually worth, despite every firm holding the repeat-engagement data that would answer it.

## Problems

- [[niches/penetration-testing-firms/coverage-measurement/build|🔨 Build: Coverage From the Tester's Own Traffic]]
- [[niches/penetration-testing-firms/coverage-measurement/buy|🛒 Buy: Code Coverage Instrumentation, Pointed Outward]]
- [[niches/penetration-testing-firms/coverage-measurement/fix|🔧 Fix: Untested and Tested-Clean Look Identical]]
