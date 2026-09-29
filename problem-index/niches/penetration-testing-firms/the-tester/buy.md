# Buy: Resourcing Tools That Model the Whole Job

**Niche:** The Tester
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Professional services resourcing software schedules billable engagements precisely and has no concept of the unbilled write-up that follows every one of them.
**Tags:** #evaluation-metrics #confidence-intervals #time-series-forecasting #convex-optimization #workflow-orchestration #worker-facing #revenue-impact
**Contested on:** Whether the write-up is work the schedule makes room for, or unpaid evening labour squeezed between back-to-back engagements.

## The Problem

Testing firms resource their work with professional services automation — the same category used by consultancies and agencies — which books people onto billable projects, tracks utilisation, and optimises for keeping everyone assigned.

The software does exactly what it is designed to do, and what it is designed to do produces this industry's defining working pattern. An engagement is a booked block of billable days. The write-up that follows is not billable, so it is not a booking, so the scheduler sees a free resource the moment the engagement ends and assigns the next one. The report then happens in the gap the scheduler believes does not exist.

Every firm knows this. Some deliberately leave a day or two between engagements, which the utilisation report immediately flags as idle time, and the practice erodes under commercial pressure over a few quarters.

The tooling is not neutral here. It defines what the firm can see, and it cannot see two thirds of a delivery task, so the firm manages a model of the work that omits a third of the work.

## What Already Exists

Professional services automation: Kantata, Projectworks, Scoro, Accelo, Productive, Float and Resource Guru. Resource scheduling, skills matching, utilisation tracking, pipeline forecasting and margin reporting — mature and widely deployed.

Testing-specific delivery platforms: the engagement management products used by testing firms, which handle findings, report generation and client delivery, and which sit alongside rather than inside the resourcing tool.

Adjacent practice worth borrowing: capacity planning in engineering organisations, which has largely accepted that unplanned work and overhead must be budgeted explicitly rather than assumed away; and clinical rostering, which models documentation time as scheduled work because regulators require it.

## The Customization Gap

**Non-billable delivery work has no first-class representation.** PSA models billable project time and generic overhead. It has no concept of a delivery task that is required, engagement-specific, substantial and unbillable — which is precisely what a report is. Modelling it is a small data-model change with a large behavioural effect.

**Utilisation is the wrong headline metric.** Every product in the category makes utilisation the primary number, which structurally penalises any firm that schedules write-up time. A delivery-completion metric — engagements fully delivered on time including the report — would drive better behaviour and does not exist anywhere.

**Review capacity is unmodelled.** Peer and quality review is a real constraint that lands on senior testers who are themselves mid-engagement. No resourcing tool represents a reviewer's capacity as distinct from their delivery capacity, so review queues silently form.

**Write-up effort is not predicted.** Firms could estimate it from finding count and complexity using their own history, and none do, so even a firm that wants to schedule it has to guess.

**Skills matching is coarse for this domain.** Cloud, mobile, embedded, application, network and specific technology depth are real specialisms, and generic skills tagging in PSA products does not express them well enough to match testers to engagements properly.

**The delivery platform and the resourcing tool do not talk.** The system that knows how many findings an engagement produced is not the system that decides when the tester is next booked, which is exactly the join that would let write-up time be scheduled realistically.

## Target Customer

The PSA vendors could add a non-billable delivery task type and a delivery-completion metric with modest effort, and professional services firms with heavy documentation obligations — legal, audit, engineering consulting — have the same shape of problem, which makes it more than a one-vertical feature.

The testing delivery platform vendors are the more likely route, since they already hold the engagement and finding data and could extend into resourcing for this specific industry.

Buyers are firm operations and practice leadership.

## Impact If Solved

Scheduling the write-up is the entire fix, and the reason it does not happen is that the tooling cannot represent it. A data-model change makes the invisible third of the work visible in the system that allocates people.

Replacing utilisation with delivery completion as the headline metric would remove the structural pressure that erodes every firm's attempt to leave write-up time in the schedule.

And modelling review capacity separately would clear a bottleneck that currently lands on the most experienced people in the firm, who are also the ones most likely to leave over it.
