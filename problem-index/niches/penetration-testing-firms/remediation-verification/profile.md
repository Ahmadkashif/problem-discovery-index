# Remediation Verification

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether a firm can demonstrate that its findings get fixed, that the fixes hold, and that the same weakness class stops recurring.

## Profile

**Market Size:** ~$600M
**Share of Parent Industry:** ~10%
**Digital Adoption:** Very low — a paid retest, once, on request
**Target Buyer:** Testing firm leadership, client security leadership, cyber insurers
**Automation Potential:** Moderate — linkage automates, the follow-up relationship does not

## What Makes This a Distinct Niche

This is the output-side half of assessment assurance. A firm delivers findings and leaves. What happens next — whether anything was fixed, whether the fix actually closed the weakness, whether the same class appeared again in the next release — occurs entirely inside the client and is never joined back.

It is a different business from its sibling. [[niches/penetration-testing-firms/coverage-measurement/profile|🎯 Coverage Measurement]] is instrumentable inside one engagement, answers the day the work ends, and improves the document the firm is already selling. Remediation verification lives after delivery, across a client boundary that closes at handover, returns nothing for a year, and improves a claim the firm has never been asked to make. Different data, different timeline, different buyer inside the same firm.

The contest is over whether a testing firm can produce evidence that its work results in things getting fixed. Every firm asserts it. None can show it. And a firm with thousands of engagements behind it cannot say which of its finding types are reliably remediated, which are perennially ignored, or which of its remediation advice produces a durable fix rather than one that regresses two releases later — despite that being the most commercially valuable question in the industry and the one its own archive would answer.

## Current Tools & Gaps

Retesting exists as a paid add-on: a confirmation pass on specific findings, usually once, within a defined window. It verifies that a fix was applied at a point in time and says nothing about whether it held or whether the class recurred elsewhere. Client-side vulnerability management platforms — Kenna, Nucleus, Vulcan and the module inside the larger suites — track findings to closure and are almost never connected back to the firm that raised them. Some mature clients maintain their own recurrence metrics and do not share them.

The gaps are structural. Nothing joins a finding to the commit, release or ticket that resolved it. Nothing detects that a remediated weakness has regressed. Nothing tracks class recurrence across releases, which is the measure that actually indicates whether an organisation learned anything. Firms cannot compare the durability of alternative remediation advice, so they recommend what they have always recommended. And no firm can answer the question a serious buyer would most like to ask: when your clients act on your findings, do the problems stay fixed.

## Problems

- [[niches/penetration-testing-firms/remediation-verification/build|🔨 Build: The Finding Followed Home]]
- [[niches/penetration-testing-firms/remediation-verification/buy|🛒 Buy: Vulnerability Management Turned Back Toward the Tester]]
- [[niches/penetration-testing-firms/remediation-verification/fix|🔧 Fix: The Same Finding Every Year]]
