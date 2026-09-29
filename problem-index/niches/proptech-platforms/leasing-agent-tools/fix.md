# Nobody Measures the Middle of the Funnel

**Niche:** [[niches/proptech-platforms/leasing-agent-tools/profile|Leasing Agent Tools]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Operators measure leads at the top and leases at the bottom and nothing in between, so a property that is losing prospects to slow response looks identical to one whose pricing is wrong.
**Tags:** #descriptive-statistics #survival-analysis #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #automation #quick-win
**Contested on:** Every serious competitor in leasing software is fighting to answer, qualify and book a prospect before they lease somewhere else — and whoever gets time-to-first-response and tour-booking rate best takes the account.

## The Problem
A property reports 340 leads and 18 leases. The regional manager concludes the marketing is producing poor-quality leads, or that the agent is not closing, and acts accordingly. The actual picture — 340 enquiries, 61 receiving a response within four hours, 44 booked tours, 29 tours attended, 18 leases — is not available, because nothing between the lead and the lease is timestamped and reported. Every diagnosis of a leasing problem in this industry is made from two numbers with a black box between them.

## Why It's Still Broken
The CRM records a lead and the ledger records a lease, and the intermediate events — first response, qualification, tour booked, tour attended, application started — are either not captured or captured inconsistently because they depend on an agent logging them. Agents log them when they have time, which is not when they are busy, which is exactly when the failures happen. And the reporting that operators are used to seeing comes from marketing systems focused on lead volume and cost per lead, which is the top of the funnel by construction.

## What a Fix Looks Like
Timestamp the stages and let them come from systems rather than from agents. First response is derivable from the communication channel, not from a log entry. Tour booking is a calendar event. Tour attendance can be captured by the self-guided tour system or by a single tap. Application start is a system event. From those, report the conversion and the elapsed time at each stage, by property, by agent, by lead source and by time of day — and the time-of-day breakdown alone usually locates the problem, since the losses concentrate in the hours when nobody was available. Compare against the operator's own portfolio rather than an industry benchmark, because the useful question is which of my properties is losing prospects at which stage. The diagnosis then names a specific intervention instead of producing a conversation about lead quality.

## Who Feels the Pain
Leasing agents blamed for a conversion rate whose composition nobody knows; marketing directors buying more leads to fix a response problem; and owners paying for vacancy caused by a queueing failure that no report shows.

## Impact If Fixed
Stage-level measurement is derivable from system events already occurring and turns an unexplained conversion rate into a located problem. Operators who instrument it for the first time typically find the largest loss at first response rather than anywhere the organisation was looking, which redirects both spend and effort immediately.
