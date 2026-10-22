# Retail Demand Forecasting Bent to One-Shot Holidays

**Niche:** [[niches/greeting-card-publishers/seasonal-card-programs/profile|Seasonal Card Programs]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retail forecasting suites handle promotions and seasonality for products that sell every week; seasonal cards sell once a year for a few weeks and then go back to the publisher.
**Tags:** #time-series-forecasting #gradient-boosting #loss-functions #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to put the right quantity of each seasonal design into each store before the holiday so that it sells through in the final days with the fewest cards returned or destroyed afterwards, and whoever forecasts the store-level seasonal curve best keeps the seasonal planogram.

## The Problem
Seasonal planners need store-level quantities for programs that are new designs every year, sold in a fixed window ending on the holiday, with a right of return. Their tools are spreadsheets and ERP planning modules that copy last year forward.

## What Already Exists
RELEX and Blue Yonder sell machine-learning demand forecasting and allocation to retailers and suppliers, with seasonal profiles, event uplift and store clustering. They are mature and widely deployed for weekly replenishment.

## The Customization Gap
The adaptation needs: forecasting at the level of a design attribute set (occasion, recipient, price) because every design is new; a holiday-relative time axis that aligns seasons falling on different weekdays and dates; stock-out correction of history using pocket-empty evidence; an explicit return and destroy cost in the allocation objective; and set and pull dates that come from merchandiser schedules. The engines can do much of this if configured by people who understand the card season.

## Target Customer
Card publishers already licensing a retail planning suite, or large enough to justify one, who want seasonal programs inside it rather than in spreadsheets.

## Impact If Solved
Seasonal planning moves onto the same engine as everyday replenishment, with return costs visible at the moment quantities are set.
