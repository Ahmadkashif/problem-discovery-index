# Back-Fill Matching for Released Block Time

**Niche:** [[niches/general-hospitals/perioperative-or-block-scheduling/profile|Perioperative Services & OR Block Scheduling]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a surgeon releases a block, the minutes are posted to the OR desk and taken by whoever calls first, not matched to the waitlisted cases that fit the time, the room and the equipment.
**Tags:** #optimization-fundamentals #dynamic-programming #gradient-boosting #monte-carlo-methods #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn released and unused OR block minutes into staffed, completed cases, and whoever fills the most released minutes without adding overtime takes the account.

## The Problem
Released time arrives as an irregular supply: 180 minutes in Room 6 next Thursday. Demand is a waitlist of cases with different durations, equipment needs (robot, fluoroscopy), implant-vendor reps, anaesthesia requirements, pre-admission testing status and payer authorisations. The OR scheduler matches them by phone, and most released time goes unfilled or is filled with a case that overruns.

## Why Nobody Has Built This
Waitlists are rarely structured. Surgeons' offices keep their own, and pre-op readiness and authorisation status live in other systems. Analytics vendors stop at reporting utilisation and nudging release. Matching needs readiness data most hospitals have not joined.

## What to Build
A matching engine that keeps a structured, readiness-scored waitlist from surgeon-office bookings, pre-op clinic status and authorisation status. For each released slot, it ranks cases by fit using predicted duration distributions, equipment and staff constraints, and expected contribution margin. It sends offers to surgeon offices in ranked order with a response clock and simulates overtime risk before confirming.

## Target Customer
Perioperative directors at hospitals with 10+ ORs and block utilisation below ~75%.

## Impact If Built
Filling an extra ~20–30% of released minutes (estimate) adds several cases a week per suite, worth hundreds of thousands to millions of dollars a year in contribution margin.
