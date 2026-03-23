# Reserve Funding Adequacy Alerts and Board Reporting

**Niche:** [[niches/hoa-management/reserve-study-and-capital-planning/profile|Reserve Study & Capital Planning]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Fix (Pain Point)
**One-liner:** Community boards review reserve fund balance once a year during budget season — by which time 12 months of underfunding have compounded, capital projects have been deferred, and the gap between reserve balance and reserve study projections has grown without anyone noticing until the annual financial review reveals a $200,000 shortfall.
**Tags:** #automation #compliance #data-integration #quick-win

## The Problem
A reserve study projects that the community should have $1.2M in reserves by year-end 2026 to maintain adequate funding for upcoming capital replacements. The actual reserve balance at year-end is $950,000 — a $250,000 shortfall from deferred assessment increases and an unexpected capital expenditure. The board learns about this shortfall at the January budget meeting — too late to address in the current fiscal year. The shortfall compounds: next year's projection assumed $1.2M as the starting balance, and every future year's projection is now wrong. By the time the roofing replacement arrives in 2029, the reserve fund is $400,000 short, triggering a special assessment.

## Why It's Still Broken
Reserve study projections live in a PDF document. Actual reserve balances live in the management platform's financial module. No connection exists between the two — the community manager would have to manually compare the reserve balance to the study's projected balance each month, which they don't do because it's not part of any standard workflow. The annual budget review is the only touchpoint where projected vs. actual reserve status is examined.

## What a Fix Looks Like
A reserve monitoring tool that: (1) stores the reserve study's annual projected balances as targets; (2) tracks the actual reserve balance monthly from the management platform's financial data; (3) calculates the variance between projected and actual balance each month; (4) alerts the community manager and board treasurer when the variance exceeds a threshold (e.g., 10% below projected); (5) generates a quarterly reserve status report for the board showing: projected vs. actual balance, variance trend, and assessment adjustment recommendation if the gap is growing.

## Who Feels the Pain
Community managers and board treasurers at associations with $250K+ in reserve funds who currently have no ongoing visibility into whether actual reserves track the study's projections — approximately 80,000-100,000 associations nationally.

## Impact If Fixed
Reserve funding shortfalls are detected quarterly instead of annually — enabling corrective action (assessment adjustment, deferred project acceleration) 9 months earlier. Special assessment frequency decreases because shortfalls are addressed gradually rather than discovered as crisis-level gaps. Board confidence in reserve adequacy improves because they see a data-driven status report every quarter, not a PDF from 3 years ago.
