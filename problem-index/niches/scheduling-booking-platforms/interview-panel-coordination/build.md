# Five Calendars, One Day, In Sequence

**Niche:** [[niches/scheduling-booking-platforms/interview-panel-coordination/profile|Interview Panel Coordination]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A five-person interview panel is a small constraint satisfaction problem and is solved by a coordinator sending messages for three days, during which the candidate accepts another offer.
**Tags:** #convex-optimization #dynamic-programming #graph-theory #optimization-fundamentals #evaluation-metrics #confidence-intervals #workflow-orchestration #automation
**Contested on:** Every serious competitor here is fighting to place a multi-person interview panel across busy calendars in one pass, with the sequence and eligibility constraints satisfied — and whoever does that takes the talent acquisition account, because panel scheduling is the coordinator's entire week.

## The Problem
A candidate reaches the final stage on Monday. The coordinator needs five interviewers across a single day: two technical, one hiring manager, one cross-functional, one senior enough to decide. They check availability, hold four provisional slots, message the interviewers, and by Wednesday two have declined and one has a conflict that appeared since. They rebuild. The panel lands the following Tuesday, nine days after the candidate cleared the previous stage. The candidate accepts a competing offer on the Friday. Every constraint involved was knowable on Monday morning.

## Why Nobody Has Built This
Interview scheduling sits inside applicant tracking systems whose core competence is workflow and compliance rather than optimisation, and the scheduling module was built to display availability. The eligibility constraints — who can assess what, who is senior enough, who knows the candidate — live in spreadsheets because no system models them. The coordinator's labour is treated as the solution rather than as the cost, and it is cheap enough per requisition that it never surfaces as a problem, even though the aggregate is most of a person's week and the candidate withdrawals are attributed to the market.

## What to Build
Panel placement as a solved constraint problem. Model the constraints explicitly: interviewer eligibility by competency, seniority requirements, exclusions for prior relationships, sequence and precedence, duration, breaks, time zones for the candidate and each interviewer, and the deadline window. Solve for a complete panel in one pass rather than slot by slot, which is what makes it fast — and free solvers dispatch a problem of this size instantly. Optimise for candidate experience and speed rather than for interviewer convenience, since the scarce and losable party is the candidate; then balance interviewer load as a secondary objective. Produce two or three complete options and send them once, rather than negotiating piecewise, which is the change that collapses three days into an hour. Re-solve on a decline rather than restarting, preserving what is already agreed and changing as little as possible. Gather candidate availability and time zone through a proper interface rather than by email. And measure time-to-panel and withdrawal-during-scheduling, which are the numbers that justify the whole thing and which most recruiting functions do not track separately.

## Target Customer
Talent acquisition operations at companies hiring at volume, applicant tracking vendors whose scheduling modules are a competitive weakness, and the specialist interview coordination vendors already in this market.

## Impact If Built
The problem is well-formed, small, and solved by free tooling, and it is currently solved by a person sending messages for several days while the candidate is deciding between offers. One-pass placement with minimal-change repair is the entire product.
