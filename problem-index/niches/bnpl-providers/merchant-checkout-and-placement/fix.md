# The Widget Placed Once in 2021

**Niche:** [[niches/bnpl-providers/merchant-checkout-and-placement/profile|Merchant Checkout & Placement]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The merchant's developer integrated the component three years ago from a documentation example, the checkout has been redesigned twice since, and nobody has looked at the placement.
**Tags:** #evaluation-metrics #change-point-detection #descriptive-statistics #automation #quick-win #revenue-impact #workflow-orchestration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make the offer appear at the right moment in a checkout the provider does not control — and whoever does that wins the conversion that decides which provider a merchant keeps.

## The Problem
The integration was done once. Since then the merchant has redesigned the product page, changed the checkout flow, added a new payment step and moved to a different template. The instalment component is still where it was put, which may now be below the fold, after the payment selection, or on a page most customers no longer see. Conversion at this merchant is poor and the account manager is discussing it as a product problem. The cause is a placement that made sense in a checkout that no longer exists, and nobody is watching for that.

## Why It's Still Broken
Nobody monitors the placement after integration, because integration is treated as a project with a completion date rather than as a live configuration — the done-ness of the integration is the assumption that hides the drift. The provider cannot see the merchant's page. Conversion decline is attributed to the merchant's customers or to competition. And the merchant's developer has no reason to revisit an integration that is technically working.

## What a Fix Looks Like
Watch the placement, not just the integration. Detect placement and visibility from the rendered page where the component reports its own context, which is the fix and turns an invisible drift into a monitored property. Alert on a conversion change that coincides with a merchant site change, since the correlation is strong and the diagnosis is otherwise guesswork. Benchmark each merchant's conversion against comparable placements, so an underperforming integration is identifiable rather than assumed to be the merchant's audience. Give the account manager a specific finding — the component is now below the fold on mobile — rather than a conversion chart, which is the difference between a conversation and a fix. Provide a placement health score the merchant can see, which motivates the change from their side. Re-verify after any merchant site change, since that is when drift happens and the trigger is detectable. Offer to make the change where the platform permits, because the merchant's development queue is the practical obstacle. Handle the commerce platform case centrally, since one template fix reaches thousands of merchants. Report the revenue at stake per merchant, which is what gets the ticket prioritised on their side. And measure placement quality across the portfolio, because it is a large aggregate number that nobody currently manages.

## Who Feels the Pain
Merchants losing conversion to a component in the wrong place; account managers discussing product problems that are placement problems; and providers whose performance is judged on somebody else's stale integration.

## Impact If Fixed
Integration is treated as a project with a completion date, which is the assumption that hides three years of drift. A component that reports its own rendered context turns an invisible placement into a monitored property with a specific finding to act on.
