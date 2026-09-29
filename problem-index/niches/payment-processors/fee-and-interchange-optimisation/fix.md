# The Downgrade Nobody Explains

**Niche:** [[niches/payment-processors/fee-and-interchange-optimisation/profile|Fee & Interchange Optimisation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** The merchant's effective rate crept up over a year, the statement shows a blended number, and nobody can say which transactions downgraded or why.
**Tags:** #descriptive-statistics #evaluation-metrics #compliance #quick-win #revenue-impact #data-integration #confidence-intervals #automation
**Contested on:** Every serious competitor in this niche is fighting to get transactions qualifying at the interchange rate they are entitled to — and whoever does that returns money merchants are currently paying for data they had and did not send.

## The Problem
A merchant's effective processing rate was a certain number last year and is higher now. Their volume mix has not obviously changed. The statement reports a blended rate and a set of fees. There is no line saying that a share of transactions failed a qualification condition, which one, or what would fix it. The merchant asks their account manager, who explains that the mix changed. Somewhere in the transaction detail is a specific cause — an integration change that stopped sending a field, a settlement job running later, a new card product in the mix — and the statement is constructed so that it cannot be found.

## Why It's Still Broken
Statements report what was charged rather than what could have been charged, and a rate that could have been lower has no line in an accounting document — the reporting model has no representation for a counterfactual, which is why the problem is invisible. Blended pricing is simpler to sell and removes the visibility entirely. Explaining a downgrade helps the merchant reduce what they pay. And most merchants lack the volume to notice a small drift.

## What a Fix Looks Like
Report the qualification, not just the charge. Show a qualification breakdown on every statement — how many transactions qualified at each rate and how many downgraded, with the reason — which is the fix, is derivable from data the processor holds, and makes a hidden drift visible immediately. Explain each downgrade cause in terms the merchant can act on, since a reason code is only useful if it names the integration field or the timing. Alert on a change in qualification rate, because a regression is usually caused by a specific change and catching it in the month it happens rather than the year after is the difference between a small loss and a large one. Quantify the recoverable amount, which is the number that gets an engineering ticket written. Offer the fix as a service, since most merchants cannot make the integration change themselves and the processor can. Report the true interchange even under blended pricing, which is an honesty position that would differentiate any processor willing to take it. Give the merchant a benchmark against comparable merchants, so they know whether their qualification rate is good. Monitor after a merchant makes a change, confirming the fix worked. Keep the analysis current as schedules change. And measure the aggregate downgrade cost across the portfolio, because a processor that recovers it for its merchants has a retention argument that price competition cannot match.

## Who Feels the Pain
Merchants paying a rate that crept up for a reason nobody will name; account managers explaining a mix shift they have not verified; and processors whose retention rests on a price their merchants cannot decompose.

## Impact If Fixed
The statement has no representation for a rate that could have been lower, so the loss is invisible by construction. A qualification breakdown with named causes is derivable from data the processor already holds and turns a year-long drift into a ticket.
