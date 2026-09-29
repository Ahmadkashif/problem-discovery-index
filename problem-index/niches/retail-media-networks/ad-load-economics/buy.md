# Long-Horizon Experimentation Practice

**Niche:** [[niches/retail-media-networks/ad-load-economics/profile|Ad Load Economics]]
**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Large platforms run long-horizon holdouts to measure what short-term revenue costs them later, and retail media measures the week.
**Tags:** #causal-inference #hypothesis-testing #survival-analysis #confidence-intervals #evaluation-metrics #bayesian-inference #time-series-forecasting #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to put a number on what advertising load costs in basket size and return visits over a year — and whoever measures that tells the category how much of its profit engine is borrowed from next year.

## The Problem
Measuring long-run effects of short-run changes is established practice at large consumer platforms. They maintain long-term holdout populations, run experiments for months, use surrogate metrics validated against long-run outcomes, and explicitly trade immediate engagement or revenue against retention. The methods — long-term holdouts, surrogate index construction, variance reduction over long horizons — are published and understood. Retail media, whose entire question is a short-run gain against a long-run cost, measures campaign windows.

## What Already Exists
Long-term holdout population design; surrogate metric construction validated against long-run outcomes; variance reduction for small effects; sequential analysis over extended horizons; and multi-horizon decision frameworks.

## The Customization Gap
The adaptation is to a physical-and-digital retail relationship with infrequent purchase occasions. It requires: (1) outcomes measured in trips and baskets rather than in sessions, where the natural frequency is weekly or monthly rather than daily — which lengthens every experiment and reduces power dramatically compared with a high-frequency platform; (2) cross-channel behaviour, since a shopper degraded online may shop in store and the effect is invisible in digital metrics alone — this is the specific trap and it makes online-only measurement misleading; (3) surrogate metrics validated against retail outcomes, since the published surrogates were built for engagement products and will not transfer; (4) seasonality and promotional cycles far stronger than platform usage patterns, which demands designs robust to them; and (5) a governance structure in which the experiment's owner is not the party whose revenue it may reduce.

## Target Customer
Retailer measurement and executive teams, retail media networks seeking credibility, and experimentation vendors for whom long-horizon retail measurement is unserved.

## Impact If Solved
The methods exist at platforms with daily frequency, and retail's weekly trip cadence lengthens every experiment and cuts the power. Cross-channel behaviour is the specific trap that makes online-only measurement of this effect misleading.
