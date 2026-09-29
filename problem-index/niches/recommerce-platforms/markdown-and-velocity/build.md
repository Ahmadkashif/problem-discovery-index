# A Calendar Applied to One-of-a-Kind Inventory

**Niche:** [[niches/recommerce-platforms/markdown-and-velocity/profile|Markdown & Velocity]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Markdown runs on a schedule — a percentage at thirty days, more at sixty — applied to inventory where every unit is different and the schedule is wrong for almost all of them.
**Tags:** #survival-analysis #gradient-boosting #convex-optimization #confidence-intervals #time-series-forecasting #revenue-impact #evaluation-metrics #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to move each unique unit at the right moment for the right price rather than on a schedule — and whoever does that recovers the margin, because a markdown calendar applied to one-of-a-kind inventory is wrong for almost every item on it.

## The Problem
Three items hit thirty days on the same morning. One has had four hundred views and twelve saves and is one browse away from selling at full price; it is discounted fifteen percent and sells that afternoon, giving away margin that was not needed. One has had six views in a month and will not sell at any price the platform would accept; it is discounted fifteen percent and holds sixty more days of storage before anybody admits it. One is a winter coat listed in March; it is discounted twice through spring and removed in June, a month before the demand it would have found. The calendar treated all three identically and all three signals were sitting in the item's own engagement data.

## Why Nobody Has Built This
Markdown schedules came from retail, where they apply to a style with many units and a defined season, and were carried across to unique inventory without revisiting the assumption. The engagement data exists in the storefront analytics and not in the merchandising system. Storage cost is not attributed per item, so the trade-off between a discount and another month of holding cannot be computed. And a schedule is operationally simple where a per-item decision is not.

## What to Build
Decide per item from its own signals. Predict the probability of selling at the current price over the next period from the item's views, saves, click-through, comparable items' behaviour and seasonality, which is a well-posed problem with continuous evidence per item and is the core of the build. Optimise the markdown against the storage cost and the expected value trajectory rather than against a calendar, so the discount is taken when it changes the outcome and not when a date arrives. Identify the items that will not sell at any acceptable price and route them out early, since ninety days of storage on a doomed item is pure loss and the signal is clear within weeks. Hold back the items that are selling themselves, which is the margin recovery half and is invisible to a schedule. Incorporate seasonality explicitly, since seasonal mispricing is systematic and predictable and the calendar makes it worse. Consider withdrawal and relisting for items whose season is coming, which is a cheaper option than a markdown and is not in the rule set. Measure markdowns causally with a holdout, since the belief that a markdown caused a sale is untested and some share would have sold anyway. And report margin recovered against the schedule baseline, because that is what justifies the build.

## Target Customer
Merchandising and warehouse operations, platform finance, and the resale-as-a-service providers running inventory for brands.

## Impact If Built
A retail markdown schedule assumes many units and a season and is applied to unique inventory where it is wrong in both directions. Per-item sell-probability from engagement signals identifies both the items giving away margin and the ones consuming storage for nothing.
