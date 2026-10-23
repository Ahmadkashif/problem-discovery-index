# One Visitor Estimate Fused From Every Feed

**Niche:** [[niches/visitors-bureaus/visitor-volume-spend-reporting/profile|Visitor Volume & Spend Reporting]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Bureaus pay for four or five measures of the same visitors and then pick one by hand, when the sources could be combined statistically into a single estimate with its uncertainty.
**Tags:** #bayesian-inference #time-series-forecasting #maximum-likelihood-estimation #change-point-detection #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to produce one monthly visitor count and spend figure reconciled across device panels, card data, hotel data and lodging-tax receipts, and whoever's number survives the city budget hearing takes the account.

## The Problem
Panel visits are up, hotel room nights are down, card spend is flat, and tax receipts for the month will not arrive for another two months or so (estimate). The research manager has to report something by the board meeting.

## Why Nobody Has Built This
Each data vendor wants its own number to be the answer. Economic impact modellers produce annual figures, not monthly nowcasts. Bureaus rarely have a statistician.

## What to Build
A state-space model in which true visitor volume and spend are hidden series, and each feed is a noisy, biased, lagged measurement of them. Tax receipts anchor the level when they arrive. Panel changes are detected as structural breaks. Output: monthly estimates with intervals, a source-by-source bias table, and a drafted explanation of the month. Offered source-neutrally, ideally through a state office to many bureaus.

## Target Customer
Research directors at large bureaus and state tourism offices.

## Impact If Built
One defensible number each month, with its uncertainty, in place of a hand-picked figure.
