# Selling Next Month on Last Month's Downloads

**Niche:** [[niches/audio-adtech-networks/inventory-and-yield/profile|Inventory & Yield]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Fix (Pain Point)
**One-liner:** The sales team commits to an impression volume based on last month's figure, the show's audience moved, and the month ends in a make-good or an unsold slot.
**Tags:** #time-series-forecasting #confidence-intervals #evaluation-metrics #descriptive-statistics #quick-win #revenue-impact #workflow-orchestration #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to forecast and price a perishable back-catalogue-heavy inventory that dynamic insertion created — and whoever does that properly stops publishers selling next month on last month's downloads.

## The Problem
A campaign is sold for a volume the publisher believes they can deliver. The estimate came from last month's total with an adjustment. This month the release schedule slipped, a strong episode from last month is no longer driving back-catalogue downloads at the same rate, and a seasonal dip arrived a fortnight early. The campaign under-delivers. The publisher issues make-goods from next month's inventory, which compresses that month, and the problem propagates. Alternatively they were cautious, delivered early, and left slots unsold that could have been revenue. Both outcomes recur monthly and are treated as the weather.

## Why It's Still Broken
The commitment is made by a salesperson from a number produced by a spreadsheet, and neither party in that exchange owns forecast accuracy — the error has no owner and therefore no correction. The propagating make-good hides the original error inside next month's numbers. Seasonality is known informally and not encoded. And the alternative requires a forecast nobody has built.

## What a Fix Looks Like
Forecast before committing. Produce a slot-level availability forecast with an interval and commit against the conservative end, which is the fix and converts a monthly apology into a reliable delivery — committing to a lower number you meet is worth more commercially than a higher one you miss. Separate new-episode and back-catalogue supply in the forecast, since they move independently and a combined number cannot be reasoned about. Encode the release schedule, because a slipped episode is a known and knowable supply reduction that currently surprises everyone. Encode seasonality explicitly rather than relying on someone remembering that August is quiet. Track committed against forecast availability continuously, so an emerging shortfall is visible in week one rather than at month end. Flag oversell at the point of commitment rather than at delivery. Account for make-goods as committed inventory in future months, which is the propagation mechanism and is frequently untracked. Measure forecast error and feed it back, which is how the forecast improves and which nobody does. Give the sales team a number they can commit to confidently, since their incentive is to promise high and the fix is to make the honest number reliable enough to sell. And report delivery accuracy to clients, because a publisher who consistently delivers what they sold is worth a premium in a category where most do not.

## Who Feels the Pain
Advertisers receiving make-goods instead of the campaign they bought; publishers giving away future inventory to cover past shortfalls; and sales teams committing to numbers nobody has forecast.

## Impact If Fixed
The forecast error has no owner because the salesperson and the spreadsheet each own half of it, and make-goods hide it inside the following month. A slot-level interval committed at the conservative end turns a monthly apology into a delivery record worth a premium.
