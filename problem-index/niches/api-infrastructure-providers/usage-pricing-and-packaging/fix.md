# Nobody Plots Usage Against the Tier Boundaries

**Niche:** [[niches/api-infrastructure-providers/usage-pricing-and-packaging/profile|Usage Pricing & Packaging]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A histogram of consumer usage with the tier boundaries drawn on it takes ten minutes and would tell most API businesses that their pricing is wrong in a specific and fixable way.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to tell an API business what to charge for, at what tier, with what overage behaviour — and whoever answers that takes the commercial side of the category, because metering is solved and the pricing decision is guessed at by everybody.

## The Problem
A pricing page offers tiers at ten thousand, a hundred thousand and a million calls. Nobody has ever plotted where consumers actually sit. If they had, they would see a dense cluster between six and nine thousand — consumers on the entry tier who will never reach the next one and are therefore permanently at the same revenue — a second cluster just above a hundred thousand paying for a million-call tier they use a tenth of, and a handful of consumers in the millions on bespoke arrangements that nobody can compare to anything. The boundaries were round numbers chosen before the business had customers, and the customers have since arranged themselves around them.

## Why It's Still Broken
Pricing analysis is nobody's standing job: product owns the page, finance owns the revenue, engineering owns the data, and the histogram requires all three to care simultaneously. Revenue reporting is by tier and by total, which shows what was earned and not how consumers are distributed within it. And a finding that the pricing is wrong implies a pricing change, which is disruptive, so there is a quiet preference for not looking.

## What a Fix Looks Like
Plot the distribution and read it. A histogram of consumer usage with the boundaries marked, on a log scale given the skew, which takes an afternoon and is immediately legible to anyone. Identify bunching below each boundary, which is revenue left on the table and usually indicates a boundary set too high. Identify consumers well below their tier's ceiling, who are paying for headroom and are a churn risk at renewal because they know it. Identify the consumers who hit the limit and what happened next — upgraded, throttled, churned — which is the overage behaviour's actual effect and takes one join. Break the distribution down by consumer segment, since a solo developer and a partner integration should not be read from the same histogram. Add cost to serve as a second dimension where it can be computed, which identifies the consumers whose usage pattern is expensive regardless of volume. And repeat it quarterly, because the distribution moves and the pricing does not.

## Who Feels the Pain
API businesses whose revenue per consumer has been flat for two years for a reason they have not looked at; consumers paying for headroom they will never use; and product teams arguing about pricing with no picture of their own customers.

## Impact If Fixed
The histogram takes an afternoon and is almost always immediately informative, which makes its absence the most avoidable gap in this niche. Joining it to what happened at the limit converts a picture into a specific change to the overage behaviour.
