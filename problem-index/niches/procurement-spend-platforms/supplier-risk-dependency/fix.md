# Criticality Assessed by Spend

**Niche:** [[niches/procurement-spend-platforms/supplier-risk-dependency/profile|Supplier Risk & Dependency]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Suppliers are monitored, reviewed and managed in proportion to how much is spent with them, which is a proxy for importance that is wrong in exactly the cases that matter.
**Tags:** #descriptive-statistics #graph-theory #evaluation-metrics #hypothesis-testing #confidence-intervals #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in supplier risk is fighting to tell a company which single supplier failure would actually stop its operations — and whoever maps dependency rather than scoring suppliers takes the account.

## The Problem
A company's supplier management effort is allocated by spend: the top fifty get relationship management, quarterly reviews and risk monitoring; the rest get a purchase order. Among the rest is a small firm supplying a specialised component with no qualified alternative, a certifying body whose approval every product requires, a software vendor whose service underpins a production process, and a logistics provider with the only refrigerated capacity on a route. Each could stop operations. None is monitored, because each is cheap. This misallocation is nearly universal and follows directly from using spend as the criticality proxy.

## Why It's Still Broken
Spend is the one supplier attribute every organisation has to hand, it produces a ranking without any work, and it is correlated with importance often enough to seem reasonable. The alternative requires the dependency data that this niche's build note assembles, which nobody has. And the failures that expose the error are rare enough to be treated as bad luck rather than as a predictable consequence of the allocation rule.

## What a Fix Looks Like
Compute a criticality measure that is not spend, even crudely, and reallocate attention to it. Even without a full dependency graph, a substantial improvement is available from questions the organisation can answer quickly: is this supplier single-sourced, is there a qualified alternative, what is the qualification lead time, what does the supplier's output feed, and what is the revenue behind it. Applied across the supply base — which is a survey rather than a modelling exercise for the parts that matter — that produces a criticality ranking that is materially different from the spend ranking, and the difference is the point. Monitor, review and relationship-manage on that basis rather than on spend. Report both rankings side by side, because the contrast is what makes the case: the list of suppliers that are critical and unmonitored is usually short, specific and immediately actionable. And treat the small critical suppliers accordingly in commercial terms as well, since a single-source supplier that is financially fragile and is paid on ninety-day terms is a risk the buyer created.

## Who Feels the Pain
Companies disrupted by suppliers nobody was watching; supply chain teams whose risk register describes their largest suppliers rather than their most important ones; and the small critical suppliers themselves, who are simultaneously indispensable and treated as tail spend.

## Impact If Fixed
The criticality survey is a bounded exercise and produces a ranking that differs sharply from spend, which immediately redirects monitoring to where failures would actually hurt. The commercial observation is the second half: single-source critical suppliers are frequently small, financially fragile and on the worst payment terms the buyer offers, which is a self-inflicted exposure that the same analysis reveals.
