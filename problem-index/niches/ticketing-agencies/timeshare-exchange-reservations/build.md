# Match Odds for Every Ongoing Search

**Niche:** [[niches/ticketing-agencies/timeshare-exchange-reservations/profile|Timeshare Exchange & Vacation-Club Reservations]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An owner who places an ongoing search for a summer week in a popular destination waits months without knowing whether it will ever match.
**Tags:** #survival-analysis #gradient-boosting #monte-carlo-methods #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to confirm owners' first-choice exchanges without devaluing the weeks they deposit, and whoever confirms the most first-choice requests per deposited week keeps the developers' affiliations and takes the account.

## The Problem
When no deposited week matches a request, the owner places an ongoing search and waits for one to arrive. Some searches match in days; others, such as school-holiday weeks at beach resorts, rarely match at all. The owner cannot tell which kind they have placed, so they call the exchange repeatedly, and an unmatched search becomes an owner complaint to the developer.

## Why Nobody Has Built This
Exchanges hold years of deposit and request history but treat matching as an inventory process, not a forecast. Publishing odds would expose which destinations are oversubscribed, an uncomfortable message for developers selling those resorts.

## What to Build
A time-to-match model for each open request, using historical deposit flows by resort, unit size and week, competing requests, the member's trading power and flexibility. Show the owner the odds and the alternatives that would raise them, and give developers a monthly report on match rates for their owners.

## Target Customer
Member operations leaders at exchange companies and owner-services leaders at developers choosing an affiliation.

## Impact If Built
Fewer repeat calls, more owners steered to requests that will match, and a reported first-choice match rate the exchange can sell to developers.
