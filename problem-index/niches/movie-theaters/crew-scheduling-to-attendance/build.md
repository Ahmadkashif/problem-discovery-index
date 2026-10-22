# Presale-Driven Labour Forecast by Station

**Niche:** [[niches/movie-theaters/crew-scheduling-to-attendance/profile|Crew Scheduling to Attendance]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A theatre knows days ahead how many people will arrive for each show, and still schedules its crew from last week's pattern.
**Tags:** #temporal-fusion-transformers #gradient-boosting #time-series-forecasting #monte-carlo-methods #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to staff each daypart to the attendance actually coming (box office, counter and auditorium turns) within minor-labour hour limits, and whoever cuts labour hours without late starts or lobby lines takes the account.

## The Problem
Managers write next week's schedule before the film slate's demand is clear, then call in or send home crew on the day. Overstaffed Tuesdays and understaffed opening Saturdays are both common.

## Why Nobody Has Built This
Workforce vendors forecast from point-of-sale history and don't see presales or showtimes; ticketing vendors don't schedule labour; circuits that built this in-house didn't sell it.

## What to Build
A forecast of arrivals, counter transactions and auditorium let-outs by 15-minute interval from showtimes, presale curves and film audience types, converted into required staff by station (box office, counter, ushers, kitchen, bar). It drafts a schedule within minor-hour and availability rules, updates as presales move, and recommends specific call-ins or early releases.

## Target Customer
VPs of operations at circuits of 20+ theatres; independent operators running dine-in sites.

## Impact If Built
Staffing to forecast rather than habit could cut labour hours ~3–5% while reducing lines and late starts on peaks (estimate), worth tens of thousands of dollars a year per theatre.
