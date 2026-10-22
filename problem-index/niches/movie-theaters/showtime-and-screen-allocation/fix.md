# The National Drop Applied to Every Town

**Niche:** [[niches/movie-theaters/showtime-and-screen-allocation/profile|Showtime & Screen Allocation]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Fix (Pain Point)
**One-liner:** When a buyer covers more theatres than they know, every theatre gets the national week-over-week drop, and the towns that behave differently lose money both ways.
**Tags:** #linear-regression #time-series-forecasting #feature-engineering #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to forecast each film's next-week demand by theatre and daypart well enough to set screens and showtimes before the mid-week publishing deadline, and whoever gets the holdover calls right most often takes the account.

## The Problem
A film that drops 50% nationally may drop 30% in a town where its audience is strong and 70% where it isn't. Buyers covering hundreds of screens apply the national figure to theatres they don't know well, so films leave too early in some towns and stay too long in others.

## Why It's Still Broken
Theatre-level history is in the ticketing system, but nobody has time on Monday to compute each theatre's past deviation from national trends by genre and audience, and spreadsheets don't keep that memory between releases.

## What a Fix Looks Like
A simple per-theatre adjustment: for each theatre and film type, the historical ratio of local to national hold, shrunk toward the national figure when history is thin, shown next to each film on the booking sheet. It is a regression a programming analyst can run weekly, not a platform.

## Who Feels the Pain
Buyers stretched across many theatres; general managers who watch their local favourite leave after one weekend.

## Impact If Fixed
A local adjustment column on Monday's sheet corrects the worst-placed holdovers within weeks of deployment, at almost no cost.
