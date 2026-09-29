# Build: Panel Assembly as a Constrained Optimisation

**Niche:** [[niches/recruiting-tech-vendors/interview-coordination/profile|Interview Scheduling & Coordination]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Treat panel scheduling as a constraint problem over interchangeable qualified interviewers rather than a search across five named calendars.
**Tags:** #convex-optimization #dynamic-programming #graph-theory #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Whether interviewers can be modelled as interchangeable within a competency without the process losing quality.

## The Problem

Panel scheduling fails because it is posed wrongly. The coordinator is told to schedule these five people, so they search five calendars for a common slot, find none in the next week, and begin negotiating by message.

The real problem is different. The panel needs someone to assess system design, someone to assess coding, a hiring manager, and a culture interviewer — and for three of those four there are several qualified people. Posed as "find a slot where one qualified person for each competency is available", the problem usually has a solution tomorrow. Posed as "find a slot where these five specific people are free", it does not.

Nobody poses it the first way, because the interviewer pool per competency is not modelled anywhere.

## Why Nobody Has Built This

The interviewer pool is not data. Who is qualified to assess what lives in the hiring manager's head, and building the competency-to-interviewer mapping is an organisational exercise nobody has undertaken.

Named panels are also a norm. The manager names the people, the coordinator schedules them, and substituting someone feels like a downgrade — which it is not, if the pool is defined properly, but it requires the manager to trust the pool.

And coordination is treated as administrative work rather than as an optimisation problem, so the tooling is a calendar rather than a solver.

## What to Build

An interviewer pool model and a solver over it.

**Model the interviewer pool by competency.** Who can assess what, at what level, with what training and calibration status. This is the prerequisite and it is an organisational artefact worth having for its own sake — it makes interviewer development, load balancing and calibration possible, none of which is manageable today.

**Solve, do not search.** Given required competencies, candidate availability, interviewer availability, ordering constraints, load limits and time zones, find the earliest feasible schedule over the qualified pool. This is a modest constraint satisfaction problem and it finds slots that no calendar search will.

**Optimise for the candidate's time, not the panel's convenience.** Earliest completion, fewest separate sessions, reasonable hours in the candidate's zone. A candidate in employment taking three separate half-days is the experience that loses them, and the solver should weight it.

**Re-solve on cancellation automatically.** A cancellation is a constraint change, not a restart. The solver finds the nearest feasible alternative — frequently a substitution rather than a reschedule — and proposes it within minutes.

**Balance interviewer load explicitly.** Interviews per person per week as a constraint, with the distribution visible. Concentration is extreme in most organisations and it is the direct cause of the non-responsiveness that makes scheduling hard in the first place.

**Measure coordination delay.** Time from decision to interview to interview completed, by stage, with the causes attributed — waiting on interviewer availability, waiting on candidate, cancellation and reschedule. This is the largest controllable component of time to hire and it is rarely decomposed.

## Target Customer

Talent operations leadership at organisations running panel interviews at volume, where coordination delay is measurable and candidates are lost in it. Also ATS vendors, for whom panel scheduling is a persistent customer complaint their calendar features do not solve.

## Impact If Built

Panels get scheduled in hours rather than days, because the problem is posed over a pool rather than over five names. A cancellation triggers a substitution rather than a restart. Interviewer load stops concentrating on the same few people. And the largest controllable part of time to hire becomes measured and attributable.
