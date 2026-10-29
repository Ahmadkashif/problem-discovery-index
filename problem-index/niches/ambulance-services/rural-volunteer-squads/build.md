# Uncovered-Hour Forecast and Roster Matcher for Volunteer Crews

**Niche:** [[niches/ambulance-services/rural-volunteer-squads/profile|Rural, Volunteer & Nonprofit Squads That Bill]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A squad chief fills the roster by group text and finds the gaps when a page goes unanswered, when the gaps are predictable from who is available, when calls come and when people say yes.
**Tags:** #time-series-forecasting #logistic-regression #optimization-fundamentals #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to keep a staffed ambulance in service for a district that runs a few hundred to a couple of thousand calls a year, and whoever leaves the fewest hours a month with no crew in service takes the account.

## The Problem
Volunteer and paid-on-call crews sign up for shifts around jobs and families. The chief knows that Tuesday afternoons and holiday weekends are thin, and that some members say yes to a page and others never do. Uncovered hours are found too late, and the neighbouring district's ambulance comes from twenty miles away.

## Why Nobody Has Built This
Scheduling apps are built for paid shifts with guaranteed staff. The squads are small, spend little and are rarely sold to, and their data sits in a paging app and a calendar.

## What to Build
A roster tool that forecasts uncovered hours from sign-ups, past page acceptance by member and time of day, and the call pattern. It asks specific members for specific gaps days ahead, ranking by who is likely to say yes, and tracks hours with no crew in service as the headline measure for the board and the county.

## Target Customer
Volunteer and combination squad chiefs, ambulance district boards and rural hospitals running small services.

## Impact If Built
If a squad with 60 uncovered hours a month (an estimate) cut them by a third, 20 more hours a month would be covered by its own crew instead of mutual aid from the next district.
