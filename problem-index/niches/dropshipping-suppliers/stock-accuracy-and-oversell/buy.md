# Inventory Accuracy Practice

**Niche:** [[niches/dropshipping-suppliers/stock-accuracy-and-oversell/profile|Stock Accuracy & Oversell Prevention]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail has decades of inventory accuracy practice — cycle counting, shrink modelling, available-to-promise — and it all assumes you can go and look at the shelf.
**Tags:** #confidence-intervals #bayesian-inference #descriptive-statistics #evaluation-metrics #time-series-forecasting #automation #hypothesis-testing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to know an item is gone before a merchant sells it — and whoever shortens that interval most decides how much of the category's revenue is spent refunding customers.

## The Problem
Retail and distribution have worked on inventory record accuracy for decades: cycle counting programmes, shrink and error modelling, available-to-promise calculations that reserve against confirmed supply, and safety stock set from measured demand and lead-time variability. The methods are quantitative, tested and well documented. Dropshipping has the same problem in a harder form — the inventory belongs to someone else, in another country, observed through a file — and applies none of it, settling for a number in a feed and a buffer a merchant guessed.

## What Already Exists
Cycle counting and record accuracy measurement; shrink and error rate modelling; available-to-promise and capable-to-promise logic; safety stock calculation from demand and lead-time variance; and inventory reconciliation processes.

## The Customization Gap
The adaptation is to inventory you cannot count and do not own. It requires: (1) no physical verification of any kind, so record accuracy must be inferred from order outcomes rather than measured against a count — this inversion is the central adaptation and it is what makes rejected orders the most valuable signal in the system; (2) availability that other merchants are simultaneously consuming invisibly, since thousands of storefronts draw on the same pool and each sees only its own orders, which is a contention problem classical inventory practice never has; (3) safety buffers computed per item from observed variability rather than set once by a merchant, which is exactly what safety stock theory does and exactly what nobody applies here; (4) available-to-promise adapted to a probabilistic rather than confirmed supply, which changes the commitment from a guarantee to a stated likelihood; and (5) the accuracy metric being oversell rate rather than record variance, since that is the outcome anyone actually cares about.

## Target Customer
Dropshipping platforms, merchants and aggregators carrying oversell risk, and inventory software vendors for whom third-party unobservable stock is unserved.

## Impact If Solved
Every method assumes you can go and count, and here you cannot — so accuracy must be inferred from order outcomes, which inverts the practice and makes rejections the key signal. Safety stock theory is directly applicable and entirely unapplied.
