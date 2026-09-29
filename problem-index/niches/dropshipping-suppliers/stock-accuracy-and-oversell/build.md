# Sold Something That Was Not There

**Niche:** [[niches/dropshipping-suppliers/stock-accuracy-and-oversell/profile|Stock Accuracy & Oversell Prevention]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The merchant's storefront says in stock because a file said so at four this morning, and the item sold out at a supplier they have never met at nine.
**Tags:** #change-point-detection #time-series-forecasting #confidence-intervals #bayesian-inference #evaluation-metrics #automation #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to know an item is gone before a merchant sells it — and whoever shortens that interval most decides how much of the category's revenue is spent refunding customers.

## The Problem
The merchant spends four hundred dollars a day advertising one product. The supplier runs out at nine in the morning. The feed refreshes at four the next morning. In between, the merchant takes nineteen orders, all of which must be cancelled and refunded, with the advertising spend already gone and the marketplace penalising the cancellation rate. The window between the stock change and the platform learning about it is where the entire loss happens, and the platform does not measure that window, publish it, or vary anything according to it.

## Why Nobody Has Built This
Polling frequency is set by supplier tolerance and infrastructure cost, both of which push toward less often, and nothing pushes the other way because the cost of staleness lands on merchants. Stock is modelled as a number, so there is nowhere to put uncertainty. Merchants respond with crude buffers, which makes the symptom quieter and the problem permanent. And oversell rate is nobody's metric.

## What to Build
Shorten and manage the window explicitly. Model stock as a distribution over what is probably available given the last observation, its age and the item's observed depletion rate, which is the foundation — the current point-estimate model has no way to express the thing that actually matters. Poll adaptively, allocating request budget to items by volatility and by the revenue at risk, since request capacity is the scarce resource and spreading it evenly wastes almost all of it. Learn each item's depletion pattern, because an item that goes from forty to zero within a day and one that moves twice a month need entirely different treatment and this is directly learnable. Use order outcomes as observations, since a rejected order is the strongest and most immediate evidence available and is currently thrown away. Reconcile the three disagreeing sources — feed, platform record, fulfilment reality — with a stated resolution rule rather than letting the most recent write win. Publish a per-listing confidence and let merchants set their own risk tolerance, which converts a hidden exposure into a managed one. Gate advertising automatically when confidence falls, which prevents the most expensive failure mode directly. Predict stockouts ahead of them from depletion rate, so merchants can rotate before rather than refund after. And report oversell rate and detection latency as headline platform metrics, because the contest is only decidable if it is scored.

## Target Customer
Dropshipping platforms, merchants advertising heavily against dropshipped stock, and ecommerce aggregators managing oversell risk at scale.

## Impact If Built
The loss happens entirely inside the window between the stock change and the platform learning of it, and nobody measures that window. Modelling stock as a distribution and spending request budget by volatility and revenue at risk is what makes the window shrink where it matters.
