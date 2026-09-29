# The Fix That Shipped and Nobody Checked

**Niche:** [[niches/customer-support-platforms/support-signal-to-product/profile|Support Signal to Product]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A product team fixes something support complained about, ships it, and nobody checks whether the contacts stopped — so neither function learns whether the fix worked or whether the diagnosis was right.
**Tags:** #hypothesis-testing #change-point-detection #descriptive-statistics #evaluation-metrics #confidence-intervals #causal-inference #quick-win #automation
**Contested on:** Every serious competitor with a support corpus is fighting to turn it into a product defect and friction signal the product organisation actually acts on — and whoever closes that loop takes a use of the data nobody currently serves.

## The Problem
Support escalates a confusing checkout step generating substantial contact volume. Product agrees, redesigns it, and ships. The support team is told it is fixed. Nobody measures the contact volume on that step afterwards. In one plausible outcome the contacts fell by eighty percent and nobody celebrated or learned that this kind of change works. In another they fell by five percent because the actual cause was something adjacent, and support continues handling them while believing the issue is resolved — which is worse, because the escalation route is now closed.

## Why It's Still Broken
The two functions have no shared artefact that survives the handoff: support escalates, product ships, and the connection between the two ends at the release. Measuring requires knowing which contacts correspond to the issue, which requires the product-oriented classification this niche's build note describes. And neither function's metrics include it — product measures delivery, support measures volume, and the causal link between them is nobody's number.

## What a Fix Looks Like
Treat every support-driven product change as a hypothesis with a measurement. When an issue is escalated, record the expected effect: this change should reduce contacts in this cluster by roughly this much. When it ships, measure — contact volume for that cluster before and after, with the release date as the intervention and appropriate handling of seasonality and volume trend, which is an interrupted time series and is elementary. Report the result to both functions. Where the reduction did not occur, that is a finding rather than a failure: it means the diagnosis was wrong, which is valuable and is currently never discovered. Aggregate the results into something neither function has — a track record of which support-identified issues, fixed in which ways, actually reduced contacts, which is the evidence that makes support's next escalation credible and tells product which kinds of fix are worth making. And publish the total contact reduction attributable to product changes over a period, which is the number that would establish what this loop is worth and is currently unknown to everyone.

## Who Feels the Pain
Support teams whose escalations vanish into a roadmap with no feedback; product teams who cannot demonstrate the impact of friction work against feature work; and customers still contacting about something everyone believes was fixed.

## Impact If Fixed
Interrupted time series on contact volume around a release is elementary and closes the only loop that would let either function learn. The cumulative track record is what changes the relationship, because support's escalations currently carry no evidence of having been right before and product's friction work carries no evidence of having paid off.
