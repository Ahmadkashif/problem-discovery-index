# The Re-Order Decided on Last Week's Spreadsheet

**Niche:** [[niches/consumer-products-makers/seasonal-pos-demand-planning/profile|Seasonal Demand Planning From Retailer POS]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Fix (Pain Point)
**One-liner:** The re-order call for a hot seasonal item is made on a workbook rebuilt by hand every Monday, with data a week old.
**Tags:** #data-integration #quick-win #automation #worker-facing #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to set seasonal and new-item quantities from retailer point-of-sale data before the last re-order date, and whoever leaves a maker with the least unsold seasonal stock at season's end takes the account.

## The Problem
The planner exports each portal, pastes, maps item numbers and fixes week alignment before anyone can look at sell-through. For a hot seasonal item, the re-order call is made on a workbook rebuilt by hand every Monday, with data already a week old by the time the meeting starts.

## Why It's Still Broken
Portal exports change layout without notice, item numbers differ by retailer, and the maker has no data engineer. Each fix is a one-off macro that breaks next season.

## What a Fix Looks Like
Scheduled pulls from each portal, item mapping maintained once, and a daily sell-through view for seasonal items with each retailer's cut-off date beside it and an alert when an item runs ahead of plan.

## Who Feels the Pain
Demand planners, sales leads and the plant scheduler.

## Impact If Fixed
Re-order calls are made 3–4 days earlier (estimate), which matters when a retailer's last re-order date falls within ~2–3 weeks of first sell-through (estimate), and the planner gets back roughly a day a week.
