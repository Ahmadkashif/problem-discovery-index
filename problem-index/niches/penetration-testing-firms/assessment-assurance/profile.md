# Assessment Assurance

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** High Market Share
**Contested on:** Whether a test report states what its clean results actually mean, or leaves the client to read two weeks of sampling as evidence of security.

## Profile

**Market Size:** ~$1.5B
**Share of Parent Industry:** ~25%
**Digital Adoption:** Very low — a findings list with no denominator
**Target Buyer:** Testing firm leadership, client security leadership, cyber insurers
**Automation Potential:** High for coverage instrumentation, moderate for outcome linkage

## What Makes This a Distinct Niche

A penetration test produces a list of what was found. It does not state what was looked at, how much of the attack surface was reached, at what depth, or what the absence of a finding in an area means — whether that area was tested thoroughly and is sound, tested lightly, or never reached at all.

Testers know exactly what their report means: two weeks of skilled effort against an estate that would take months to cover. Clients frequently read the same document as an assessment of whether the system is secure, and boards and insurers and customers receive it third-hand as exactly that. The gap between the two readings is this industry's central honesty problem, and it is structural rather than dishonest — nobody withholds the coverage information, it is simply never produced.

The same absence runs the other way. A firm delivers findings and leaves, and whether anything was fixed happens inside the client and never returns. So a profession whose entire value proposition is that its findings matter has no evidence that they get acted on, which of its finding types are remediated, or which of its remediation advice works.

### Contested sub-niches

- [[niches/penetration-testing-firms/coverage-measurement/profile|🎯 Coverage Measurement]]
- [[niches/penetration-testing-firms/remediation-verification/profile|🎯 Remediation Verification]]

## Current Tools & Gaps

Reports are documents — findings with severity, evidence, reproduction steps and advice, in a per-client format. Some firms include a methodology section naming the standards followed, usually PTES, OWASP or OSSTMM, which describes what the approach is meant to cover rather than what this engagement actually reached. Retesting is offered as a paid add-on, typically once, within a window, on the specific findings. Vulnerability management platforms on the client side track findings to closure and are rarely joined back to the firm.

The gaps define the niche. Nothing measures coverage, so no report can express confidence in a negative. Nothing distinguishes untested from tested-and-clean, which is the single most consequential ambiguity in the deliverable. Retesting confirms a specific fix and says nothing about whether the class recurred. Firms hold thousands of engagements and cannot state which finding types their clients actually remediate. And no firm can demonstrate, to a prospect or an insurer, that its work produces better security outcomes than a cheaper competitor's — which is why the market prices on day rate.

## Problems

- [[niches/penetration-testing-firms/assessment-assurance/build|🔨 Build: The Report With a Denominator]]
- [[niches/penetration-testing-firms/assessment-assurance/buy|🛒 Buy: Assurance Language From Audit and Clinical Testing]]
- [[niches/penetration-testing-firms/assessment-assurance/fix|🔧 Fix: A Clean Report Is Not a Clean System]]
