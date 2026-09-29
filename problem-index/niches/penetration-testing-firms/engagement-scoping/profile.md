# Engagement Scoping & Estimation

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** Low Digitized
**Contested on:** Whether an engagement's size is set by what the attack surface actually contains, or by an asset list the client compiled by asking around.

## Profile

**Market Size:** ~$780M
**Share of Parent Industry:** ~13%
**Digital Adoption:** Very low — a questionnaire and a judgement call
**Target Buyer:** Engagement managers, scopers, sales engineers, firm leadership
**Automation Potential:** High — discovery and estimation are both derivable

## What Makes This a Distinct Niche

The engagement is scoped and priced before anyone has looked. A client is sent a questionnaire — how many external hosts, how many applications, how many user roles, how many APIs — and answers it by asking colleagues. The firm converts the answers into days using an internal rule of thumb, quotes, and books the work.

Everything downstream is determined at that moment. If the estate is twice what the questionnaire said, the engagement is half as thorough, and nothing in the process revisits the number. If the client forgot the acquired subsidiary's infrastructure, it will not be tested and will not appear as an exclusion, because nobody knew it existed. If the application has four hundred endpoints rather than the eighty in the specification, the tester discovers this on day two and works faster.

This is a distinct market because the buyer and the failure are both distinct. The buyer is the firm's commercial function rather than its technical one. The failure happens before testing starts and is invisible afterwards — a badly scoped engagement produces a report that looks exactly like a well scoped one. And the inputs that would fix it, unlike most problems in this industry, are largely available from outside the client's perimeter before anyone signs anything.

## Current Tools & Gaps

Scoping questionnaires, an internal day-rate calculator, and the judgement of an experienced scoper who has seen many estates. Some firms run a light discovery pass before quoting. Attack surface management platforms exist and are sold to defenders rather than to the firms quoting work against their estates. Proposal tooling handles the document.

The gaps are large and unusually tractable. Nothing verifies the client's asset count against what is externally discoverable, despite that being a commodity capability. Effort estimation is intuition, not a model, even though every firm holds hundreds of engagements with quoted days against actual coverage achieved. Nothing flags a scope as inadequate for its estate before the work is sold. Change between scoping and delivery — months in enterprise procurement — is never rechecked. And no firm has calibrated its own estimates against outcomes, so the same scoper makes the same systematic error for a decade.

## Problems

- [[niches/penetration-testing-firms/engagement-scoping/build|🔨 Build: Scope From Discovery, Not From a Questionnaire]]
- [[niches/penetration-testing-firms/engagement-scoping/buy|🛒 Buy: Attack Surface Management Pointed at the Quote]]
- [[niches/penetration-testing-firms/engagement-scoping/fix|🔧 Fix: The Asset List Is Wrong and Everyone Proceeds]]
