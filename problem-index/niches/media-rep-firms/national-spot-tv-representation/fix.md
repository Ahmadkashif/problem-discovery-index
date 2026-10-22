# Share Reports That Arrive After the Quarter Is Sold

**Niche:** [[niches/media-rep-firms/national-spot-tv-representation/profile|National Spot TV Representation]]
**Industry:** [[industries/media-rep-firms|Media Representative Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The rep learns its station's share of an agency's market spend from a monthly pooled report, weeks after the buys that set it were placed and too late to change the next one.
**Tags:** #bayesian-inference #time-series-forecasting #feature-engineering #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to lift each represented station's power ratio, its share of the national dollars in its market against its share of the audience, and whoever proves that lift, market by market, keeps the station group when the rep contract comes up.

## The Problem
Pooled revenue reports such as Miller Kaplan's Market X-Ray show each station's share by advertiser, agency and category, after the month closes and the stations have reported. By then the quarter's buys are placed. AEs pricing next month's requests work from last quarter's share and their own sense of how buys went.

## Why It's Still Broken
The report is built from stations' booked revenue, which can't be reported until it is booked. Nobody combines the rep's own live orders with occurrence monitoring and last period's share into a running estimate.

## What a Fix Looks Like
A running share estimate per station, agency and market. It starts from the latest pooled report, updates with the rep's own orders as they land and with occurrence data as competitors' spots air, and shows its uncertainty. AEs see while the quarter is still selling whether a buyer is under-allocating to their station, and the estimate is reconciled to the pooled report when it arrives.

## Who Feels the Pain
National AEs pricing blind to current share; rep sales managers who discover a share loss a month late; station groups that hear about it at the quarterly review.

## Impact If Fixed
Share problems become visible while there is still inventory to price differently, using data the rep already has.
