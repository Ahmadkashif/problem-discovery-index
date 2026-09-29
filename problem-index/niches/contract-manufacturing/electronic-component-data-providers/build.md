# Obsolescence Forecasts That Are Scored Against What Happened

**Niche:** [[niches/contract-manufacturing/electronic-component-data-providers/profile|Electronic Component Data Providers]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The database predicts years-to-end-of-life on millions of parts, manufacturers eventually announce the actual date, and nobody compares the two.
**Tags:** #survival-analysis #time-series-forecasting #gradient-boosting #evaluation-metrics #cross-validation #confidence-intervals #feature-engineering #causal-inference #data-integration #revenue-impact

## The Problem
Lifecycle status and years-to-end-of-life are among the most consequential fields the database carries. Design engineers select parts against them, contract manufacturers plan last-time buys against them, and a wrong forecast means either a redesign mid-programme or a warehouse full of parts that did not need buying. The forecasts are produced from lifecycle heuristics and analyst judgment. Every one of them eventually resolves, because manufacturers announce end-of-life and the date becomes a fact. The resolved outcomes are recorded — as the part's new status — and never joined back to what was predicted. So a company whose product is prediction, over millions of items with automatic resolution, has no accuracy record and cannot say whether its forecasts are better than a rule of thumb.

## Why Nobody Has Built This
Forecasts are stored as current-state fields rather than as versioned predictions, so recovering what was forecast for a given part three years ago means reconstructing from change logs that were kept for audit rather than for analysis. Resolution is also messier than it looks: manufacturers announce end-of-life with varying notice, sometimes reverse it, and sometimes a part becomes unobtainable long before any announcement — so the ground truth needs defining rather than assuming. And nobody has asked, because the segment competes on coverage breadth rather than on demonstrated accuracy.

## What to Build
Forecasts recorded as versioned, resolvable predictions with the evidence and method that produced them, and scored automatically as manufacturers announce. Ground truth is defined explicitly and more than one way — announced end-of-life, last-time-buy date, and observed market unobtainability — because those diverge and subscribers care about different ones. The resulting record supports what the business has never had: accuracy and bias decomposed by component category, manufacturer, technology node, and forecast horizon, so systematic error becomes visible rather than anecdotal. It supports calibrated uncertainty published alongside the point forecast, which matters far more to a last-time-buy decision than a slightly better midpoint. And it directs analyst effort at the categories where the house is measurably weak, which is not where effort currently goes.

## Target Customer
Chief data officers and heads of content at component data providers running 300-1,500 analysts, and the component engineering and supply chain leaders at contract manufacturers who commit purchasing decisions to these forecasts with no accuracy history available.

## Impact If Built
Creates the differentiator this segment lacks. Coverage is converging across vendors and is increasingly table stakes; demonstrated forecast accuracy by category is not, and it can only be built by the party that made the predictions. It also directly improves the highest-stakes decision the subscriber makes with the product, which is how much inventory to buy before a part disappears.
