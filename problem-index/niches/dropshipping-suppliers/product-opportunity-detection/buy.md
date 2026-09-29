# Demand Sensing Practice

**Niche:** [[niches/dropshipping-suppliers/product-opportunity-detection/profile|Product Opportunity Detection]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer goods companies run demand sensing on point-of-sale panels to see demand forming early, and dropshipping merchants read a bestseller list.
**Tags:** #time-series-forecasting #recurrent-forecasting #change-point-detection #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a merchant which product will work before they spend on advertising it — and whoever predicts that from the platform's own order flow owns the decision every merchant makes first.

## The Problem
Demand sensing is an established practice: consumer goods manufacturers buy point-of-sale panel data, combine it with their own shipments and external signals, and detect demand shifts weeks before conventional reporting. They pay substantially for panels that cover a fraction of the market. A dropshipping platform has something better than a panel — a complete census of transactions across its entire merchant base, updated continuously, with the product, price, destination and outcome attached — and uses it for billing.

## What Already Exists
Demand sensing platforms on retail point-of-sale panels; short-horizon forecasting with external signal integration; new product forecasting from analogues; trend detection and lifecycle classification; and cannibalisation and assortment effect modelling.

## The Customization Gap
The adaptation is from a manufacturer forecasting its own products to a platform advising thousands of independent merchants. It requires: (1) a census rather than a sample, which removes the panel projection error that most of the practice is built to manage and makes the problem cleaner than the one the tools solve; (2) forecasting a product with no history at all, since most candidates are new to the platform and analogue-based new product methods are the relevant technique rather than the exception; (3) supply-side competitive density as an output, which has no equivalent in manufacturer demand sensing because a manufacturer does not compete with thousands of sellers of its own item — this is the genuinely new dimension; (4) very short lifecycles measured in weeks rather than seasons, which changes the horizon and the update frequency entirely; and (5) the recommendation itself affecting the outcome, since acting on it changes the market — a reflexivity that no demand sensing system has had to handle.

## Target Customer
Dropshipping and sourcing platforms, merchants and aggregators, and demand sensing vendors for whom marketplace census data is an unserved and superior input.

## Impact If Solved
A census removes the panel projection error the whole practice is built to manage, making this cleaner than the problem the tools solve. Competitive density has no manufacturer equivalent, and the recommendation changing the market is a reflexivity demand sensing never faces.
