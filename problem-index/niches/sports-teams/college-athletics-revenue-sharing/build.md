# Cap Allocation Tied to Retention Risk

**Niche:** [[niches/sports-teams/college-athletics-revenue-sharing/profile|College Athletics Departments Under Revenue Sharing]]
**Industry:** [[industries/sports-teams|Sports Teams & Clubs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A department divides its revenue-share cap by sport and position on precedent, without an estimate of which athletes are likely to enter the portal and what keeping them would cost.
**Tags:** #survival-analysis #gradient-boosting #optimization-fundamentals #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to help an athletic department spend its revenue-sharing cap on athletes who will stay through their agreements, and whoever's schools lose the fewest revenue-share dollars to athletes who leave before their agreement ends takes the account.

## The Problem
The cap is a fixed pool across all sports, with Title IX questions over how it is shared. Football and men's basketball take most of it. Within them, general managers set amounts by position and status, then react when a starter's agent reports a better offer elsewhere.

## Why Nobody Has Built This
Revenue sharing started in July 2025, so there is one season of history. Portal entries are public, but offers and payments are confidential, and coaches distrust models of their players.

## What to Build
A department-side model of each athlete's risk of entering the portal, from playing time, depth-chart position, coaching changes, prior transfers and public portal patterns. It is joined to the cap ledger and an optimiser that shows where a dollar is least likely to leave with an athlete before the agreement ends, within the cap and the department's Title IX policy. It is advisory only, with the general manager deciding.

## Target Customer
General managers and deputy athletic directors at Power Four and other revenue-sharing departments.

## Impact If Built
If a department with a ~$20M cap cuts the share paid to athletes who leave before their agreements end from ~15% to ~10% (estimate), it keeps ~$1M a year of cap for athletes who stay.
