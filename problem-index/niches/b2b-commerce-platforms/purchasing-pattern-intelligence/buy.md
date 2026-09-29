# Demand Forecasting Practice

**Niche:** [[niches/b2b-commerce-platforms/purchasing-pattern-intelligence/profile|Purchasing Pattern Intelligence]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Supply chain has decades of intermittent-demand forecasting practice aimed at the warehouse, and nobody has pointed the same methods at the individual customer account.
**Tags:** #time-series-forecasting #exponential-smoothing #recurrent-forecasting #survival-analysis #evaluation-metrics #confidence-intervals #gradient-boosting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to predict what a business customer will order next from the cleanest repeat-purchase record in commerce — and whoever does it accurately enough to act on owns the reorder before the customer initiates it.

## The Problem
Forecasting sparse, lumpy, intermittent demand is a well-developed discipline in supply chain, with established methods, error metrics suited to intermittency, and hierarchical reconciliation across product and location. Every distributor runs it — aggregated to the warehouse, for the purpose of deciding what to stock. The same data disaggregated to the customer account, for the purpose of deciding what to offer, is not forecast at all, despite being the version that produces revenue rather than inventory efficiency.

## What Already Exists
Intermittent demand forecasting methods; hierarchical forecasting with reconciliation; safety stock and service level optimisation; seasonality and promotion modelling; and forecast accuracy measurement designed for sparse series.

## The Customization Gap
The adaptation is from replenishment to selling. It requires: (1) forecasting at the customer-part level rather than the warehouse-part level, which is far sparser and is exactly where intermittent-demand methods are strongest — the methods fit better here than where they are currently used; (2) an objective of offer timing rather than stock cover, which changes the loss function entirely, since being early is an opportunity and being late is a lost order, not a stockout; (3) event-driven patterns alongside periodic ones, because a large share of B2B purchasing follows projects rather than calendars and classical methods assume the latter; (4) the prediction being surfaced to a person or a storefront rather than to a purchasing system, which is a delivery problem the supply chain stack never had to solve; and (5) reconciliation between the two views, since the account-level forecast should inform the warehouse one and currently does not.

## Target Customer
Distributors running supply chain forecasting already, B2B commerce platforms, and forecasting vendors for whom customer-level demand is an unserved application of methods they own.

## Impact If Solved
Intermittent-demand methods fit the customer-part series better than the warehouse series they are currently applied to. The loss function changes from stock cover to offer timing, and the account forecast should reconcile back into the replenishment one.
