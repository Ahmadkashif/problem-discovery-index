# Free Shipping Priced by Nobody

**Niche:** [[niches/d2c-brand-operators/order-level-margin/profile|Order-Level Margin]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Free shipping above a threshold is a promotional decision made once, and the threshold was chosen by looking at competitors rather than by comparing the subsidy to the margin on the orders it produces.
**Tags:** #revenue-impact #confidence-intervals #hypothesis-testing #descriptive-statistics #causal-inference #evaluation-metrics #quick-win #convex-optimization
**Contested on:** Every serious competitor in this niche is fighting to tell a brand what each order actually made after everything — and whoever does that takes the account, because every decision in the business is currently made on revenue while the margin varies from healthy to negative order by order.

## The Problem
A brand offers free shipping above fifty dollars, because competitors do. Orders just above the threshold are the most common and carry the thinnest margin; some are negative once the shipping and the return probability are counted. Heavy products are subsidised more than light ones with no adjustment. Distant customers cost several times as much to serve as local ones and pay the same. The policy is a large, variable, unexamined cost applied uniformly, and it was set by imitation and never revisited against the margin it produces.

## Why It's Still Broken
Free shipping is a conversion lever and conversion is measured immediately while the shipping cost lands in a different line. The threshold was set once and is treated as a competitive necessity that cannot be changed. Per-order shipping cost is not attributed, so the subsidy's size is unknown. And testing it feels risky because the conversion effect is visible and the margin effect is not.

## What a Fix Looks Like
Measure the subsidy and set the policy against it. Attribute actual shipping cost per order — weight, distance, service, returns — which the carrier statements support and which immediately reveals how large and how uneven the subsidy is, and is the precondition for any decision here. Report margin by order value band, which shows whether orders just above the threshold are profitable and frequently shows that they are not. Test the threshold rather than inheriting it, since the conversion effect of moving it is measurable in a week and the margin effect is computable, and the two together settle a question currently answered by imitation. Vary the policy by product weight or category where the economics differ enough to justify it, which is a common and easily explained variation. Consider distance-based or membership-based structures, which several categories have moved to and which price the actual cost driver. Measure the threshold's effect on basket construction, since customers add low-margin filler items to reach it and that behaviour is frequently the worst part of the policy. Report the total annual subsidy as a line, so it is managed like the significant expense it is. And revisit it on a cadence, because carrier costs and the competitive norm both move.

## Who Feels the Pain
Brands subsidising their least profitable orders most heavily; finance functions with a shipping line they cannot explain; and growth teams optimising a conversion lever whose cost nobody has told them.

## Impact If Fixed
The subsidy is large, uneven and unmeasured, and the carrier statements contain everything needed to size it. Margin by order value band shows whether the orders the threshold creates are profitable, which is the question the policy was set without asking.
