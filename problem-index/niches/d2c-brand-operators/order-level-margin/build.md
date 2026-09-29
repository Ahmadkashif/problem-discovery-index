# Revenue to the Penny, Margin to the Month

**Niche:** [[niches/d2c-brand-operators/order-level-margin/profile|Order-Level Margin]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every component of an order's true margin sits in a system the brand already runs, and none of them are joined, so a business with excellent revenue reporting makes every decision without knowing what anything earns.
**Tags:** #data-integration #revenue-impact #descriptive-statistics #evaluation-metrics #confidence-intervals #gradient-boosting #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to tell a brand what each order actually made after everything — and whoever does that takes the account, because every decision in the business is currently made on revenue while the margin varies from healthy to negative order by order.

## The Problem
A brand promotes its best-selling product heavily because it drives revenue. It is a heavy item shipped free, has the highest return rate in the range, is frequently bought with a discount code, and carries the lowest gross margin. Each order loses money once shipping both ways, the payment fee, the pick cost and the acquisition cost are counted. The brand has all seven numbers — in the commerce platform, the supplier invoices, the carrier statements, the payment processor, the warehouse system and the ad platforms — and has never put them in the same row.

## Why Nobody Has Built This
The data lives in six systems owned by three functions and nobody owns the join. Management accounts satisfy the statutory requirement at an aggregate level, which is what finance is measured on. Returns and shipping are treated as overheads rather than as attributable costs. Attributing advertising cost to an order requires the attribution work the category also lacks. And the aggregate margin is acceptable, which hides that it is an average of profitable and loss-making orders.

## What to Build
Put the components in one row. Build a per-order contribution model joining product cost, discount, actual shipping charged and incurred, payment fees, fulfilment cost, expected return cost and attributable acquisition cost, which is a data integration exercise rather than a modelling one and is the whole build — the difficulty is organisational, not technical. Estimate return cost per product from its own history rather than at a blended rate, since return rates vary by product enormously and the blended rate is what hides the loss-makers. Attribute acquisition cost per customer using the best available incrementality estimate, and state the assumption, since a rough attributable figure is far better than none. Rank products, channels, discount codes and customer segments by contribution rather than by revenue, which reorders most brands' priorities immediately and is the first output anybody should look at. Report the distribution of order margin, not the average, since the average is healthy in businesses whose worst quartile is deeply negative. Feed margin rather than revenue into the advertising optimisation, which the paid acquisition niche develops. Update continuously rather than monthly, so a decision can be made on it. And put contribution on the same dashboard as revenue, because what is reported is what gets managed.

## Target Customer
Finance and growth functions, brand leadership, and the commerce analytics vendors whose products report revenue.

## Impact If Built
Every component is in a system the brand runs and the difficulty is organisational rather than technical. Ranking products and channels by contribution rather than revenue reorders most brands' priorities on the first day, and the distribution of order margin shows what a healthy average conceals.
