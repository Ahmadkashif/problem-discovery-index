# Dialling in Arrival Order

**Niche:** [[niches/lending-marketplaces/the-loan-consultant/profile|The Loan Consultant]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The best lead of the day is worked at four in the afternoon because that is where it sat in the queue.
**Tags:** #worker-facing #quick-win #evaluation-metrics #automation #descriptive-statistics #workflow-orchestration #gradient-boosting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell a licensed consultant which lenders will actually approve the person they are calling — and whoever supplies that turns a dialling job back into an advisory one.

## The Problem
Leads arrive continuously and are dialled in the order they arrive. Contact rates collapse within minutes of a form submission, and they vary enormously by time of day and by lead source. A high-value borrower who submitted at nine in the morning may be called hours later, by which point they have already spoken to two competitors. The consultant has no way to know which of the forty leads in front of them is worth calling first.

## Why It's Still Broken
The dialler was configured as a queue because arrival order is the obvious default, and nobody revisited it once the floor was busy — a working process with no visible failures rarely gets re-examined. Prioritisation needs a value estimate nobody produces. Consultants are measured on calls made, which arrival order maximises. And contact rate decay is known anecdotally and reported nowhere.

## What a Fix Looks Like
Prioritise on what is already known. Rank the queue by lead value and contact likelihood rather than by arrival time, which is the fix and uses source, profile and time-of-day data the marketplace already has. Call the fresh leads first, since contact rate decay is steep, well established and currently ignored by the default ordering. Report contact rate by minutes elapsed, which will demonstrate the cost of the current order within a week. Vary attempt cadence by lead type, because a business lead and a consumer lead behave differently and are treated identically. Respect the consent window explicitly in the cadence, as it is a compliance boundary and is currently managed by the individual. Show the consultant why a lead is prioritised, since unexplained ordering is ignored. Measure consultants on outcomes per lead worked rather than on calls made, which is what makes prioritisation stick. Hold back the leads nobody will reach rather than burning attempts, because attempt budget is finite. Route by consultant strength where the floor is large enough, since some are better with particular borrower types. And review the queue policy monthly, as source mix changes and a fixed policy decays.

## Who Feels the Pain
Consultants working good leads too late; borrowers who have already committed elsewhere by the time the call comes; and marketplaces paying for leads that go cold in a queue.

## Impact If Fixed
Arrival order was the obvious default and a process with no visible failures rarely gets re-examined. Ranking by value and freshness uses data already held and recovers the leads currently going cold in the queue.
