# Demand Sensing and Assortment Planning

**Niche:** [[niches/online-marketplaces/unmet-demand-intelligence/profile|Unmet Demand Intelligence]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail has decades of assortment planning and lost-sales estimation for exactly the question of what customers wanted and could not buy, and marketplaces do not ask it.
**Tags:** #time-series-forecasting #probability-distributions #descriptive-statistics #evaluation-metrics #revenue-impact #confidence-intervals #hypothesis-testing #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to turn every search that found nothing and every listing that expired into a map of where supply and demand fail to meet — and whoever does that takes the market, because that map is the operating instruction for a matching business.

## The Problem
Estimating the demand you did not capture is a well-developed retail discipline. Lost sales estimation corrects observed sales for stockouts, since observed demand is censored by availability. Assortment planning decides what to stock from demand signals rather than from last season's sales. Space allocation trades shelf against expected return. All of it exists because retailers learned that optimising on what sold is optimising on what you happened to have, and marketplaces are making exactly that error at a larger scale.

## What Already Exists
Lost sales and censored demand estimation; assortment planning and range optimisation; demand transference modelling for substitution when a first choice is unavailable; space and allocation optimisation; and demand sensing from search and browse signals in retail.

## The Customization Gap
The adaptation is to an assortment the platform does not own. It requires: (1) the remedy being seller recruitment rather than a purchase order, which changes what the output has to look like — an assortment plan here is a supply acquisition brief and nobody produces one; (2) censoring by discoverability as well as by availability, since inventory can exist and be unfindable, and separating the two is the distinctive analytical problem here; (3) demand transference on heterogeneous items, where a buyer's second choice is a similar-but-different item rather than a different pack size, which is harder and is what the similarity representation enables; (4) per-micro-market analysis, since a marketplace is hundreds of small assortments and aggregate demand sensing is useless for acquisition; and (5) speed, since marketplace demand moves with fashion and a seasonal planning cycle is the wrong cadence.

## Target Customer
Marketplace supply acquisition and analytics functions, and the retail planning discipline for whom this is a familiar problem in an unfamiliar structure.

## Impact If Solved
Retail learned that optimising on what sold optimises on what you happened to stock, and marketplaces are making that error at scale. Censoring by discoverability as well as availability is the distinctive analysis, and an assortment plan here is a supply acquisition brief nobody currently writes.
