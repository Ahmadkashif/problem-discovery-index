# The Turn Scheduled as the Dependency Graph It Is

**Niche:** [[niches/proptech-platforms/unit-turn-makeready/profile|Unit Turn & Make-Ready Sequencing]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A unit turn is a small project with hard dependencies, parallelisable steps and a daily cost, and it is run by a site manager phoning five vendors in sequence and finding out about delays when the next one shows up.
**Tags:** #dynamic-programming #optimization-fundamentals #combinatorics-and-counting #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in turn operations is fighting to get a vacant unit from move-out to rent-ready in the fewest days across five vendors who do not talk to each other — and whoever cuts days-vacant most takes the account.

## The Problem
A resident moves out on the first. Inspection happens on the third because the site manager was showing units. Repairs are scheduled for the sixth, the painter is booked for the ninth on the assumption repairs finish, the flooring vendor for the eleventh. The repair vendor does not turn up on the sixth; nobody knows until the painter arrives on the ninth to a unit that is not ready and leaves, and his next slot is the sixteenth. The unit rents on the twenty-fourth instead of the twelfth. Twelve days of rent, and every step of the failure was visible in advance to someone who was not looking.

## Why Nobody Has Built This
Turn management modules were built as checklists because a checklist is what a site manager asked for, and nobody has modelled the dependency structure because it varies by unit condition and by which vendors are used. Vendors are small businesses with no scheduling systems to integrate with, so any solution has to work through text messages and confirmations rather than through calendars. And duration is unknown at the start because scope is unknown, which makes a schedule feel futile — the answer to that is to predict the scope, which nobody has tried.

## What to Build
Scope and duration predicted from the move-out inspection, then scheduled as a dependency graph. The inspection's photographs and findings, combined with the unit's own history, tenancy length and the operator's realised turn outcomes for comparable units, predict which work will be needed and how long each step takes — with an interval, so the schedule can be built to a confidence rather than to an optimistic point. Dependencies are explicit, so the steps that can run in parallel do. Vendor confirmation is a text message with a reply, which is the integration this vendor population actually supports, and non-confirmation escalates rather than sitting. Each step's completion is confirmed with a photo, which both verifies and starts the next step automatically. When something slips, the whole graph re-plans and the affected vendors are notified, which is the difference between a nine-day slip and a one-day one.

## Target Customer
Multifamily and single-family rental operators, turn-services companies whose product is exactly this coordination, and the platform vendors whose turn modules are checklists.

## Impact If Built
Days vacant is one of the most direct revenue levers in rental housing and a substantial share of it is coordination slack rather than work. Operators who schedule turns properly typically recover several days per turn, which across a portfolio is a large revenue number obtained without touching rent, leasing or occupancy strategy.
