# The Produce Manager's Order and Cull

**Industry:** [[grocery-stores|Grocery Stores]]
**Type:** High Impact
**One-liner:** A supermarket's fresh margin is decided each morning by a department manager who reads ripeness, weather and next week's ad by eye, and none of that judgement is recorded, so it cannot be graded, taught or kept when the manager leaves.
**Tags:** #tacit-knowledge-ml #cnns #transfer-learning #gradient-boosting #time-series-forecasting #survival-analysis #worker-facing #revenue-impact

## The Problem
A produce manager at a mid-size supermarket runs a department of 400 to 700 items, most of which lose value every day they sit. Every morning they walk the floor and the cooler with a handheld. They check what sold yesterday, what is on the back dock, what the ad features next week, and what the weather will do to the salad and watermelon trade. They write orders for two or three deliveries ahead. They cull: they pull the soft avocados, trim the lettuce, rotate the berries, and decide which items go to a markdown rack, which to the deli for cut fruit, which to the food bank and which to the dumpster. The meat, seafood, bakery and deli managers run the same loop with different clocks.

The things experienced managers know best are the least written down. That this shipper's bananas colour a day faster than the last one's. That a load of strawberries that looks fine on arrival will not last the weekend because the clamshells are sweating. That a 90-degree Saturday doubles the cut-watermelon trade at this store but not at the one across town. That a BOGO on one brand of salad kit pulls sales from the bagged lettuce next to it. That a case of peaches needs two days on the floor before anyone will buy it. This is tacit knowledge in the strict sense: pattern recognition built over hundreds of weeks that the manager cannot fully specify.

Fresh foods were 42% of grocery sales in 2024 (FMI), and fresh departments carry shrink rates several times the store average, roughly 4–8% of department sales against 2–3% for the store (estimate). The outcome of each call is known within days, in sales and in dumpster weight. What is not recorded is the call itself. Culls are entered as a monthly total, or not at all. Product condition at receipt is not captured. Overrides of the system's suggested order carry no reason code. With annual employee turnover at 48% in 2024 (FMI), the manager who made the good calls is often gone before anyone learns which calls were good.

## Why It's Unsolved
The data collection problem is that the expert's read happens in seconds, with their eyes and hands, in a cooler, during the busiest hour of their day. Asking a manager to photograph cases and type a reason for every cull or override is a tax with no visible return to them. Condition data does not exist in any system: the receiving record says a case arrived, not that it arrived two days riper than the last one. The forecasting tools that do exist learn from sales and orders, which are the consequences of the manager's judgement, not the judgement itself.

The labelling problem is that sales are a censored and noisy label. A sold-out item hides its true demand; a full display that sold well may have sold because it was full. Culls are the honest label for over-ordering, but culling is itself a judgement, and managers disagree with themselves: the same manager culls harder on Monday after a bad weekend than on Thursday before an ad. Ripeness and quality grades from photos need labels from people who disagree at the margin, so inter-rater and test-retest agreement has to be measured before any model is trusted.

The deployment problem is that the tool must be faster than the manager's walk. A recommendation that arrives after the order cut-off is ignored; one that contradicts what the manager can see on the shelf, without showing why, is overridden and then distrusted. The manager is also judged on shrink and in-stocks, so a system that records their calls feels like surveillance unless it visibly makes their numbers better.

## What a Solution Looks Like
A capture layer first and a model second. At receiving and during the morning walk, the manager photographs a few cases and displays on the handheld already in their hand; a vision model scores ripeness and defects per case and logs them against the delivery. Culls are logged by scanning the item and tapping a reason (ripe, damaged, date, overstock, quality at receipt), with weight read from the scale. Every override of a suggested order gets a one-tap reason drafted from what the system can see: weather, an ad, a local event, product condition.

On top of that record, learn the experienced manager's reads. Pair condition scores at receipt with days-to-sell and cull outcomes to estimate remaining shelf life per lot. Learn which overrides, by which managers, beat the forecast, and fold those patterns into the next suggested order. Show the new manager the experienced one's track record ("this store's managers added 30% to cut fruit on hot Saturdays, and it sold") so the judgement transfers with its evidence attached.

## Impact If Solved
For a 40-store regional chain doing ~$1.2B a year with ~42% in fresh, cutting fresh shrink by one point of department sales is worth ~$5M a year in margin (estimate), about a quarter of the ~$20M the chain nets at a 1.7% margin. Retaining a departing manager's documented reads also shortens the six to twelve months a new manager takes to run a department without heavy shrink (estimate).
