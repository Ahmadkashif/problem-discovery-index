# A Route Planner Built Around Start Dates and Wind

**Niche:** [[niches/outdoor-advertising-companies/posting-and-structure-maintenance/profile|Static Posting & Structure Maintenance]]
**Industry:** [[industries/outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The start-of-period posting crunch is a scheduling problem with hard deadlines, weather windows and material dependencies, and it is planned on a whiteboard.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #worker-facing #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to post every contracted face by its start date with proof the buyer accepts, because each late or wrong posting becomes a makegood that wipes out that face's margin for the period, and whoever posts on time with zero rejected proofs keeps the renewal.

## The Problem
In the days around a period start, a market may have hundreds of faces to post. Each has a contract start date, a vinyl that may or may not have arrived from the printer, an access constraint (a gate, a landlord's hours, a lane closure on a busy road) and a structure type that dictates crew size. Wind rules out bulletin vinyl installs on some days. Operations managers sequence it by experience, and when a vinyl is late or the wind picks up, the plan falls apart and makegoods follow.

## Why Nobody Has Built This
Generic route optimisers handle stops and time windows, not vinyl dependencies, wind limits by structure height or the economics of which late posting costs most. Billboard software vendors serve small operators who post a few faces a day.

## What to Build
A planner that takes contracts, vinyl tracking from printers, structure attributes, access notes, crew skills and a wind and precipitation forecast, and produces daily crew routes that minimise expected makegood cost. It replans during the day as vinyls arrive or weather changes, and tells sales which contracts will start late before the advertiser notices.

## Target Customer
Operations directors at operators with multiple crews per market; independents through their software vendor.

## Impact If Built
Fewer late postings in the crunch, fewer wasted trips, and sales warned early enough to manage the client rather than apologise.
