# Fix: The Delay Was the Manager's and the Metric Is the Recruiter's

**Niche:** [[niches/recruiting-tech-vendors/the-recruiter/profile|The Recruiter]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The shortlist sat with the hiring manager for nineteen days and the requisition's time-to-fill number belongs to the recruiter.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #hypothesis-testing #quick-win #worker-facing #automation
**Contested on:** Whether time to fill will be decomposed by who was holding the process.

## The Problem

Time to fill is the headline recruiting metric. It runs from requisition open to offer accepted and it is reported by recruiter.

Within that elapsed time, the recruiter controls a minority of the days. Sourcing and screening are theirs. Manager review of the shortlist, interview availability, debrief scheduling, decision latency, offer approval and compensation sign-off are not, and in most organisations they are the larger part.

Every transition is timestamped in the applicant tracking system, so the decomposition is available. It is never computed, so a recruiter whose requisition aged because a manager took three weeks to review six resumes appears, in the only report leadership sees, to be slow.

## Why It's Still Broken

Time to fill is a single number, it is comparable across organisations, and leadership likes it. Decomposing it produces a more complicated report that says the delay is in the business rather than in recruiting, which is a harder message for a recruiting leader to deliver.

The stage timestamps are also not surfaced as durations. They are in the event log and the reporting layer presents stage counts and a total, so the decomposition requires someone to write the query.

And the manager is a stakeholder rather than a user of the recruiting metrics, so nothing they do appears in any recruiting report.

## What a Fix Looks Like

Decompose the number. It is a query over timestamps that already exist.

Attribute every day to a holder: recruiter, hiring manager, scheduling, candidate, approvals, external. From the stage transitions and the assignment of each stage. Report time to fill as a stacked breakdown rather than a total.

Report manager responsiveness. Median days to review a shortlist, to give interview feedback, to make a decision — by manager, with the distribution. This is the single most useful report in recruiting operations and essentially nobody produces it. It also, more than anything else, changes manager behaviour, because managers who see their own number against their peers respond.

Set expectations as service levels with both sides. The recruiter delivers a shortlist in five days; the manager reviews in three. Once both are stated and measured, the conversation about an ageing requisition becomes factual.

Show it live on the requisition. Days held by each party, updating, visible to both. A manager looking at a requisition that shows nineteen days with them acts on it.

Adjust the recruiter's metric. Time to fill net of days held by others, or the recruiter-held portion reported separately, so the number reflects what they control.

And escalate on threshold. A stage held beyond a defined period notifies the manager's manager automatically. This is uncomfortable, it works, and it is a rule.

## Who Feels the Pain

Recruiters, held accountable for delay caused by people they cannot direct, and conducting the same fruitless chasing daily. Candidates, sitting in silence during the nineteen days and frequently leaving for a faster process. Hiring managers, genuinely unaware of their own latency because nobody has ever shown it to them. And the organisation, losing candidates to a delay it has never attributed.

## Impact If Fixed

Time to fill becomes attributable, which is a query over existing timestamps and which reframes every conversation about an ageing requisition. Manager responsiveness becomes visible, which is what changes it. And the recruiter is measured on the part of the process they actually control.
