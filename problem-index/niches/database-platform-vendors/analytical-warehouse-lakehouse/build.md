# The Query That Cost Four Hundred Dollars

**Niche:** [[niches/database-platform-vendors/analytical-warehouse-lakehouse/profile|Analytical Warehouse & Lakehouse]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An analyst runs a query, it scans a large table, and they find out what it cost when somebody reviews the monthly bill — by which time they have run it forty times.
**Tags:** #gradient-boosting #graph-theory #optimization-fundamentals #descriptive-statistics #confidence-intervals #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to make a large query cheap and a hundred concurrent users fast without locking the customer's data into a format they cannot leave — and whoever does that takes the data platform account, because cost at scale and openness are the two things that decide it.

## The Problem
An analyst writes a query joining two large tables with a filter the engine cannot push down. It scans several terabytes and costs a meaningful amount. They do not know this: the interface returns results, not a price. They iterate on it eleven times during the afternoon, then schedule it to run daily. Six weeks later a platform engineer investigating the warehouse bill finds it, rewrites it to use a partition filter, and reduces the cost by two orders of magnitude. Every piece of information needed to warn the analyst — the scan estimate, the table statistics, the pricing — was available to the engine before the query ran.

## Why Nobody Has Built This
Consumption pricing means the vendor's revenue is the customer's cost, and surfacing a price before execution reduces it, which is the same commercial conflict that recurs across this vault. The query plan contains the scan estimate and is shown to people who read query plans, which is not the analyst population. Cost feedback also requires a mapping from plan estimates to money that varies by pricing model and is not exposed. And the analyst is not the buyer, so their experience has not shaped the interface.

## What to Build
Price the query before it runs and help the analyst avoid the expensive version. Show an estimated cost and scan volume before execution, derived from the plan the engine already produces, with a confirmation step above a threshold — which is the single highest-value change available here and is an interface decision rather than a technical one. Explain why a query is expensive in terms an analyst understands: this filter cannot use the partitioning, this join produces an intermediate result of this size, this column is not clustered — rather than showing a plan. Suggest the cheaper equivalent, since the common cases are a small enumerable set of rewrites and the engine can identify them. Recognise repeated and equivalent queries across users and offer the cached or materialised result, since the same expensive question is asked by several people and nothing connects them. Report cost per query, per user and per dashboard continuously, so the expensive scheduled query is visible the week it starts rather than in a quarterly review. And let a team set a budget with a warning rather than discovering the overrun, which is an ordinary control that consumption platforms have been slow to offer.

## Target Customer
Data platform and analytics engineering teams, warehouse and lakehouse vendors competing on efficiency rather than on consumption, and the query tooling vendors sitting between the analyst and the engine.

## Impact If Built
The information needed to prevent an expensive query exists before it runs and is shown to nobody, which makes this an interface and incentive problem rather than a technical one. Pre-execution cost with an explanation addresses the analyst's actual difficulty, which is that they cannot tell an expensive query from a cheap one.
