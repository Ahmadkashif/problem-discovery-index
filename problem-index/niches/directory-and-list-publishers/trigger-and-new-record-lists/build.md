# A False-Trigger Rate Measured, Not Guessed

**Niche:** [[niches/directory-and-list-publishers/trigger-and-new-record-lists/profile|Trigger & New-Record Lists]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Trigger-list sellers compete on speed and quote no error rate, so a buyer cannot tell a fast list from a fast list full of shell companies.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #confidence-intervals #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver the new record first — the business that filed last week, the household that moved last weekend — with the fewest false triggers, and whoever delivers the freshest trigger at a measured false-trigger rate takes the account.

## The Problem
A payroll company buys a weekly new-business list and finds that many records are holding companies, re-registrations of existing firms or entities with no operating address. Its sales reps call them, waste days, and stop trusting the list — but have no number to compare against another vendor.

## Why Nobody Has Built This
The label — did this filing become a real operating business? — appears only months later in other sources, and nobody joins it back to the original trigger.

## What to Build
A classifier that scores each trigger as a genuine event, trained on later evidence: a new business that acquires a phone, a website, a storefront, employees or licences within months; a move confirmed by later address sources. Each weekly file ships with a measured false-trigger rate and latency per source, and buyers can choose a confidence threshold that trades volume for precision.

## Target Customer
Trigger-list compilers and the insurers, banks and B2B services firms that buy weekly triggers.

## Impact If Built
Buyers get a comparable quality figure, reps stop calling shells, and the compiler can charge for precision as well as speed.
