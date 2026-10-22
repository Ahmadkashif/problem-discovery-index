# Store-Level Seasonal Curve Forecasting With Return Costs Priced In

**Niche:** [[niches/greeting-card-publishers/seasonal-card-programs/profile|Seasonal Card Programs]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Seasonal quantities are set from last year's sell-through plus a planner's hunch, with no model of how each store's demand piles into the last three days and no price on the cards that come back.
**Tags:** #gradient-boosting #time-series-forecasting #loss-functions #monte-carlo-methods #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to put the right quantity of each seasonal design into each store before the holiday so that it sells through in the final days with the fewest cards returned or destroyed afterwards, and whoever forecasts the store-level seasonal curve best keeps the seasonal planogram.

## The Problem
A seasonal program ships to thousands of stores weeks before the holiday. Demand is flat for most of the window and then spikes: the day before Mother's Day can carry a large share of the season's units (estimate). Planners set quantities per store from last year, adjusted for store changes and their sense of the season. They cannot see whether last year's sales were capped by empty pockets, and the cost of overshipping is booked weeks later as returns and destroys in a different department's budget.

## Why Nobody Has Built This
Each holiday gives one data point per store per year, which defeats ordinary forecasting. The holiday's weekday moves, Easter moves by weeks, and Valentine's Day follows the Christmas pull by days. Forecasting vendors sell to retailers, whose seasonal problem is broader; the card-specific version has a handful of buyers.

## What to Build
A quantile model of daily seasonal demand by store and design that pools across holidays, years and similar stores, corrects last year's sales for stock-outs, and simulates the season to choose quantities that balance a sold-out pocket against a returned card at the publisher's own costs. In season, it recommends replenishment and reallocation from slow stores to fast ones while there is still time to ship.

## Target Customer
Seasonal planning directors at card publishers with mass and drug accounts; also gift wrap and party goods programs with the same shape.

## Impact If Built
Fewer returns and destroys with the same or higher sell-through on the peak days. Each percentage point of seasonal returns avoided is margin recovered directly (estimate), and each prevented stock-out protects the retailer's view of the department at renewal.
