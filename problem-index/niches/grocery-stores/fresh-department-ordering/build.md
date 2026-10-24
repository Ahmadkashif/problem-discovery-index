# Override Grading Inside the Order Screen

**Niche:** [[niches/grocery-stores/fresh-department-ordering/profile|Fresh Department Ordering]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Managers override suggested fresh orders every day, and no tool records why or checks later whether the override beat the forecast.
**Tags:** #gradient-boosting #causal-inference #large-language-models #evaluation-metrics #tacit-knowledge-ml #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each fresh item's store order before the truck is cut, and whoever cuts the most shrink at an unchanged in-stock rate takes the account.

## The Problem
An ordering system suggests 12 cases of strawberries; the manager orders 18 because a heat wave is coming and the berries look good. Sometimes the manager is right and the system learns nothing; sometimes the manager is wrong and the system is blamed for the shrink. Over a year, thousands of overrides per store carry the department's tacit knowledge, and none of it is kept.

## Why Nobody Has Built This
Vendors want fewer overrides, because overrides weaken their pilot numbers, so they discourage them rather than learn from them. Asking for a reason slows the manager, and grading needs a counterfactual most vendors do not compute.

## What to Build
At the order screen, each override gets a one-tap reason drafted from context (weather, ad, event, condition, supplier). A week later the system estimates shrink and lost sales under the suggested and placed orders and scores the override. Managers see their own hit rate by reason. Overrides with a proven record, such as "hot Saturday, cut fruit, this store", become features in the next forecast.

## Target Customer
Fresh ordering vendors who need adoption without fighting managers, and chains whose pilots stall on override disputes.

## Impact If Built
If a quarter of overrides are shown to beat the forecast and folded in, and the rest are cut by half, a department could cut shrink by ~0.5 points of sales (estimate), ~$25,000 a year per store on ~$5M of fresh sales.
