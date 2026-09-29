# Fix: The Asset List Is Wrong and Everyone Proceeds

**Niche:** Engagement Scoping & Estimation
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The tester discovers on day two that the estate is twice the size the contract assumed, and the engagement carries on at the original size because changing it is harder than not.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #revenue-impact #workflow-orchestration
**Contested on:** Whether an engagement's size is set by what the attack surface actually contains, or by an asset list the client compiled by asking around.

## The Problem

Day two of a ten-day engagement. The scope said forty hosts and one application with eighty endpoints. Initial enumeration finds a hundred and ten hosts, two applications nobody mentioned, and an API with four hundred endpoints. The estate is several times the size the contract was written against.

What happens next is almost always nothing. The tester mentions it to the engagement manager. The engagement manager may mention it to the client. The contract is signed, the days are booked, the client's budget for this quarter is spent, and the next engagement starts in eleven days. Raising it formally means a change order, a procurement cycle, a rescheduling, and an awkward conversation about whose fault the original number was.

So the tester does the only thing available: works faster and covers less of each thing. Ten days that would have given reasonable depth across forty hosts now give shallow depth across a hundred and ten. The report looks the same. It lists findings. It does not say the estate was three times the scoped size, because the report has no field for that, and the tester who raises it in the debrief sounds like they are managing expectations.

The client receives what they believe is an assessment of their estate, priced for an estate a third the size, and nobody has told them.

## Why It's Still Broken

**Changing scope mid-engagement is procedurally expensive.** Change orders in enterprise procurement take weeks. The engagement is ten days. The mechanism does not fit the timeline, so the informal accommodation is the only practical response.

**Nobody wants to have the conversation.** It implies the client's asset inventory was wrong, which is embarrassing for them, or that the firm's scoping was wrong, which is embarrassing for the firm. The path of least resistance is for both parties to proceed.

**The tester has no standing.** Scope is a commercial matter handled by an engagement manager. A tester who escalates is stepping outside their role, and the answer is usually to do their best with the time available.

**The consequence is invisible.** A report from an under-scoped engagement is indistinguishable from one from a well-scoped one. There is no measurement that would reveal the difference, which is the same absence that [[niches/penetration-testing-firms/coverage-measurement/profile|🎯 Coverage Measurement]] addresses.

**Fixed-price competition punishes honesty.** In a market where bids are compared on price, a firm that revisits scope looks like a firm that quotes low and upsells, which is a reputation nobody wants.

**The client's budget really is fixed.** Often there is genuinely no more money this quarter. Raising it produces an answer of "do what you can", which is what would have happened anyway — so people skip to it.

## What a Fix Looks Like

**Write a scope variance protocol into every engagement.** Agreed at signing: if discovered surface exceeds the scoped estimate by more than a defined margin, a short, pre-agreed conversation happens on day two with three named options — extend, descope explicitly to what the days can cover properly, or proceed at reduced depth with that recorded in the report. Pre-agreeing the protocol removes all the awkwardness, because nobody is improvising a difficult conversation under time pressure.

**Make explicit descoping the default response.** If the days cannot cover the estate, agreeing on day two which parts will be covered properly is far better than spreading the same effort thinner across everything. A thorough assessment of sixty per cent with a clear statement of what was excluded beats a shallow pass over all of it, and clients choose it readily when offered.

**Record variance in the report, always.** Scoped surface, discovered surface, and what was covered. One table. This is the field that currently does not exist and whose absence lets an under-scoped engagement pass as a full one.

**Run discovery before signing.** Most of this is preventable. A passive discovery pass during scoping catches the majority of the variance before anyone commits, which is the subject of the build in this niche.

**Give the tester a formal escalation path.** A defined, expected, non-confrontational route to flag scope variance on day two, so it does not depend on an individual's willingness to make a fuss.

**Track variance as a firm metric.** Scoped versus discovered, per scoper and per client type. Firms that measure it discover systematic under-scoping patterns they can correct, and today nobody looks.

## Who Feels the Pain

The client, who paid for an assessment of their estate and received a thin pass over part of it, and was not told.

The tester, holding the knowledge that the engagement cannot do what it was sold to do, with no authority to change it and no field in which to record it.

The engagement manager, caught between a client with a fixed budget, a booked schedule, and a technical reality that does not fit either.

And the firm's reputation, eventually, when something surfaces in the part of the estate that ten days could never have reached.

## Impact If Fixed

A pre-agreed variance protocol converts the industry's most avoided conversation into a routine one, at the cost of a paragraph in the engagement letter.

Explicit descoping produces a materially better assessment from the same budget, because depth on a defined subset is worth more than uniform shallowness — and it gives the client an accurate statement of what was and was not examined.

And recording variance in the report closes the gap that lets an under-scoped engagement look identical to an adequate one, which is the mechanism by which the whole problem stays invisible.
