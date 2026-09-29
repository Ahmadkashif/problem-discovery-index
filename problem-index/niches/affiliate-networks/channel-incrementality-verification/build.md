# A Performance Channel Nobody Verified

**Niche:** [[niches/affiliate-networks/channel-incrementality-verification/profile|Channel Incrementality Verification]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Merchants pay commission on sales the network attributes, almost never with a holdout, so the channel reports a return that is definitionally close to infinite and close to unfalsifiable.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #revenue-impact #bayesian-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a merchant whether affiliate produced any sales at all — and whoever runs that test credibly decides whether the channel's reported return survives contact with evidence.

## The Problem
The affiliate report says the channel returned twelve to one. That number is computed by taking sales the network attributed to the channel and dividing by commission paid. Since commission is paid only on attributed sales, the ratio is a restatement of the commission rate and cannot be low. It is presented to a finance function as a performance measure, compared against other channels whose measurement is less flattering, and used to allocate budget. No holdout has been run. The channel's entire claim rests on a calculation that is structurally incapable of producing a bad answer.

## Why Nobody Has Built This
The networks are paid on attributed sales and have no reason to test whether those sales were incremental — the conflict is total and it explains the absence entirely. Merchants accept the figure because it is favourable and because running a test requires deliberately foregoing a channel they have been told is their best. The channel's advocates within the merchant benefit from the number. And no independent party has had access to run the test.

## What to Build
Build the verification the channel has never had. Run holdouts by suppressing affiliate tracking for a shopper sample and measuring what happens to total sales, which is the whole method, is cheap, and is the test the category has structurally avoided for twenty years. Measure by partner type separately, since the answer for a content publisher and for a checkout extension will differ enormously and a single channel-level number conceals the thing that matters. Run geo-based tests where shopper-level suppression is impractical, which extends the method to merchants who cannot randomise individuals. Report incremental rather than attributed return as the headline, and show both so the gap is visible — that gap is the finding and is what changes behaviour. Account for the substitution to other channels, because sales that move to paid search when affiliate is suppressed are not incremental to the business either and a naive holdout will overstate. Run continuously rather than once, since the answer changes with partner mix and seasonality and a one-off number is quickly stale. Keep the measurement independent of the network, which is a structural requirement rather than a preference given the conflict. Give merchants the design rather than only the result, so the test is reproducible and defensible internally. Feed the findings into commission policy, connecting to the attribution work, since the remedy for a non-incremental partner type is a different rate rather than a smaller budget. And publish aggregate findings across merchants, because the category's credibility problem is collective and a single merchant's result changes nothing.

## Target Customer
Merchant measurement and finance functions, independent measurement vendors, and the networks who conclude that a verified channel is worth more than an unfalsifiable one.

## Impact If Built
Return on spend computed from attributed sales divided by commission on those sales is a restatement of the commission rate and cannot be low. A shopper-level suppression test is cheap and settles it, and doing it by partner type is where the answer stops being a single number.
