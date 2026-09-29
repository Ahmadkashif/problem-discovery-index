# The Same Four People Do Every Interview

**Niche:** [[niches/scheduling-booking-platforms/interview-panel-coordination/profile|Interview Panel Coordination]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Interviewer load is distributed by who says yes, so a handful of willing people carry most of the hiring effort until they stop replying, and nobody measures it until they do.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #worker-facing #quick-win #automation
**Contested on:** Every serious competitor here is fighting to place a multi-person interview panel across busy calendars in one pass, with the sequence and eligibility constraints satisfied — and whoever does that takes the talent acquisition account, because panel scheduling is the coordinator's entire week.

## The Problem
A coordinator needs a technical interviewer on Thursday. They message the person who usually says yes. That person conducts eleven interviews this month, which is most of a working day, on top of their actual job. Nobody assigned this; it accumulated because they were reliable. Three months later they start declining, the coordinator's pool effectively shrinks, panels take longer, and the recruiting function concludes that interviewer availability has become a problem rather than that it always was one and they had been drawing on one person's goodwill.

## Why It's Still Broken
Interviewer load is not measured anywhere, because interviews are calendar events rather than assigned work and nothing aggregates them per person over time. The coordinator optimises for filling the panel today, which correctly means asking whoever is most likely to say yes, and that local optimisation produces the concentration. Interviewing is also usually uncompensated and unrecognised in performance terms, so there is no mechanism by which the load becomes anyone's concern until it is refused. And the pattern of who carries it frequently tracks the same lines as other uncredited work, which nobody has looked at here either.

## What a Fix Looks Like
Measure the load and distribute it deliberately. Interviews conducted per person per month, with hours including preparation and written feedback, which is a query over calendar and applicant tracking data and is the whole unlock. Explicit caps per interviewer per period, agreed with their manager, treated as a hard constraint in scheduling rather than as guidance. Rotation across the eligible pool as an objective rather than asking the reliable person again, which requires the eligibility data to exist and is the reason it should. Visibility of the load to managers, since interviewing is real work absent from every workload conversation. Track decline rates per interviewer over time, because a rising decline rate is the leading indicator of an exhausted pool and currently surfaces only as a coordination problem. And look at the distribution across demographic lines deliberately, since the concentration of uncredited supporting work has a documented pattern and this is an instance of it.

## Who Feels the Pain
The handful of people carrying most of the interviewing; coordinators working with a pool that is nominally large and effectively small; and candidates whose panels slip because the reliable people stopped replying.

## Impact If Fixed
The load measurement is a query over data every company holds and is consistently more concentrated than anyone expects. Caps and rotation convert a goodwill-dependent system into a managed one, and the demographic check is the part most likely to be skipped and most likely to matter.
