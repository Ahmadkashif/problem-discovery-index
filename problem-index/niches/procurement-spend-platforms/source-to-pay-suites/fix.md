# The Process People Route Around

**Niche:** [[niches/procurement-spend-platforms/source-to-pay-suites/profile|Source-to-Pay Suites]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Employees buy on cards because the requisition process is slower than the thing they need, and procurement responds with policy rather than by measuring how long its own process takes.
**Tags:** #survival-analysis #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #quick-win #automation
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
Someone needs a piece of software for a project starting Monday. The requisition process requires a commodity code, a cost centre, a business justification, three approvals and a supplier onboarding if the vendor is new, and will take between one and four weeks depending on who is travelling. They put it on a card. Procurement's response is a policy reminder and a threshold reduction, which moves more spend onto smaller cards rather than into the process. Nobody has measured the end-to-end elapsed time of the process they are asking people to use, or compared it to the urgency of the requests it receives.

## Why It's Still Broken
Procurement measures its own performance in savings and in spend under management, not in cycle time, so the duration of its process is nobody's metric. Approval chains accumulate — each approval was added for a reason and none is ever removed, the same monotonic accumulation that afflicts claim edit libraries and CRM required fields — and the aggregate delay belongs to no individual approver. And the people bearing the cost are requesters across the business who have an easy alternative, which means the pressure never reaches procurement as a complaint, only as leakage.

## What a Fix Looks Like
Measure the cycle and publish it. End-to-end elapsed time from request to available, decomposed by stage — waiting for information, waiting for each approval, supplier onboarding, purchase order issue — with the distribution rather than the average, since the tail is what drives people to the card. Compare it to the urgency profile of incoming requests, which is knowable and which most procurement functions have never characterised. Then attack the specific stages: approval chains audited for approvals that have never resulted in a rejection, which is a query and typically finds several; supplier onboarding, which is frequently the longest stage and is largely a document collection exercise that could be pre-emptive; and information the requester cannot supply, which is the intake problem and belongs in that sub-niche. Report cycle time as a standing metric alongside savings, because a function that measures only what it saves and not what it costs the business in time is optimising half the equation.

## Who Feels the Pain
Employees who need something and choose the path that works; procurement teams blamed for leakage caused by their own cycle time; and the organisation, which pays uncontracted prices for the spend that routed around.

## Impact If Fixed
Cycle time decomposition is available from workflow timestamps every suite already records and is the diagnosis that adoption efforts currently lack. The approval audit is the fastest win — approvals that have never rejected anything are pure delay — and removing a few of them changes the calculation for the requester more than any policy reminder.
