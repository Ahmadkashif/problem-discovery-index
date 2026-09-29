# The Decline Code Vocabulary Nobody Uses Consistently

**Niche:** [[niches/payment-processors/authorisation-performance/profile|Authorisation Performance]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** The decline code is drawn from a small standard vocabulary that thousands of issuers use differently, so the same code means a temporary problem at one bank and a permanent one at another.
**Tags:** #descriptive-statistics #gradient-boosting #evaluation-metrics #confidence-intervals #quick-win #revenue-impact #data-integration #hypothesis-testing
**Contested on:** This niche is not terminal — recovering a decline and preventing one are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
An issuer declines and returns a code. The code vocabulary is small and the reasons are many, so issuers map their internal reasons onto the available codes differently — a generic decline may mean insufficient funds at one issuer, a fraud suspicion at another and an expired credential at a third. The processor's retry logic reads the code and applies a rule. It retries the permanent declines, wasting attempts and irritating issuers, and gives up on the temporary ones, losing revenue. Everyone in the industry knows the codes are unreliable and the systems are built as though they were not.

## Why It's Still Broken
The code is the only structured information the issuer returns, so it became the input despite being known to be inconsistent — availability standing in for reliability, with no attempt to correct it. Correcting it requires observing outcomes per issuer per code, which needs the settlement join nobody makes. Issuers are not going to standardise. And the loss is spread across millions of transactions with no single visible failure.

## What a Fix Looks Like
Learn what each issuer's codes actually mean. Build an empirical mapping from issuer and code to observed outcome — how often a retry after this code from this issuer succeeds, and when — which is the fix, requires only the settlement join, and replaces a broken standard with measured behaviour. Treat the code as a noisy signal combined with other evidence rather than as a fact, since the transaction's own characteristics carry information the code does not. Report the mapping's confidence, since some issuer-code pairs have abundant data and others do not, and the retry policy should reflect that. Detect when an issuer's usage changes, because these mappings drift as issuers change their systems and a stale mapping is worse than a generic rule. Share the mapping across merchants, since it is a property of the issuer rather than of any merchant and the processor's network position is what makes it knowable. Feed it into the retry and routing decisions directly, which is where the value lands. Publish aggregate findings to the industry where it helps, since better collective behaviour reduces the issuer pushback that constrains everyone. Distinguish soft from hard declines empirically rather than by the standard's own classification, which is where most of the wasted retries come from. Use it in merchant reporting, so a merchant told why their approvals are low gets a real answer. And measure the recovered revenue, because the mapping is worth a measurable amount and the measurement is what funds maintaining it.

## Who Feels the Pain
Merchants losing revenue on temporary declines abandoned as permanent; issuers receiving pointless retries; and processors whose authorisation rate is limited by a vocabulary they treat as reliable.

## Impact If Fixed
The code became the input because it is the only structured field, despite being known to be inconsistent across thousands of issuers. An empirical issuer-by-code outcome mapping replaces a broken standard with measured behaviour and needs only the settlement join.
