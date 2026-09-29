# Pricing One Unique Unit at Scale

**Industry:** [[recommerce-platforms|Recommerce Platforms]]
**Type:** High Impact
**One-liner:** Every item is a single unit with its own condition, and pricing it correctly determines whether the platform makes money on an item that cost real labour to process and may sell for twenty dollars.
**Tags:** #gradient-boosting #survival-analysis #cnns #confidence-intervals #time-series-forecasting #evaluation-metrics #hypothesis-testing #k-nearest-neighbors #revenue-impact

## The Problem
A managed recommerce platform receives an item, inspects it, grades it, photographs it, lists it and stores it. That processing cost is largely fixed per item and is incurred before anyone knows what the item will sell for.

Then it must be priced. The item is one unit. Its condition is specific. Comparable sales may be thin or absent, and where they exist they were for items in different condition at a different time of year.

Both errors are expensive. Priced high, it occupies a slot in the warehouse for months, accruing storage cost and eventually being marked down anyway from a worse position. Priced low, the platform gives away margin on an item whose processing already consumed most of it.

The decision is repeated thousands of times a day, at a cost ceiling of pennies per decision, on items with a median value low enough that any manual pricing is uneconomic. The largest platforms handle it with rules — a percentage of estimated retail adjusted by condition band and category — which is crude in exactly the categories where the margin is.

Markdown compounds it. An item that has not sold gets reduced on a schedule, and the schedule is uniform across items with very different demand characteristics.

## Why It's Unsolved
Comparables are genuinely thin. A specific style, size, colour and condition combination may have sold twice in the past year on this platform, which is not enough to price from directly and is exactly the situation for most of the long tail.

Condition is the dominant price variable and is recorded as a coarse grade. The difference between two items in the same grade can be a factor of two in price, and the grade cannot express it.

Demand is seasonal, category-specific and fashion-dependent in ways that make historical prices decay quickly. A style that sold well eighteen months ago may be worth substantially less now for reasons no attribute captures.

And the decision cost ceiling is real. Any approach requiring human attention per item is uneconomic for the majority of inventory, which pushes toward rules — and rules are least accurate where the value is highest.

## What a Solution Looks Like
Price prediction from attributes and images rather than from comparables. Learning a mapping from what an item is and looks like to what items like it realised turns a thin-comparables problem into a regression over a rich feature space, and photographs carry condition information no grade band expresses.

Time-to-sell modelled jointly with price. The real objective is not the highest price but the best combination of price and holding cost, which means predicting the sale probability curve at each price point and choosing against carrying cost — a survival problem that the category treats as a pricing lookup.

Markdown as an optimisation rather than a schedule. Given a predicted demand curve and a storage cost, the optimal reduction path differs enormously between a coat in September and the same coat in March, and a uniform schedule is wrong for both.

Intake decisions informed by the same model. Whether to accept an item at all is the earliest and highest-leverage application, and platforms currently accept broadly and discover the mistake after processing.

Honest uncertainty, so that genuinely uncertain items can be routed to a human or listed with a wider price test rather than priced confidently wrong.

## Impact If Solved
Unit economics are the persistent difficulty in managed recommerce, and they are decided by a pricing rule applied to an item whose processing cost is already sunk. Predicting price and time-to-sell jointly from images and attributes addresses the core economic problem, and it rests on a condition-to-price dataset no one outside these platforms holds.
