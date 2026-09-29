# Build: Communication as the Default Behaviour of the Pipeline

**Niche:** [[niches/recruiting-tech-vendors/the-candidate-in-pipeline/profile|The Candidate in the Pipeline]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Make every status transition notify the candidate by default, expose an honest status view, and measure the silence that remains.
**Tags:** #workflow-orchestration #descriptive-statistics #evaluation-metrics #large-language-models #confidence-intervals #compliance #worker-facing #automation
**Contested on:** Whether communication will be the default rather than a configuration nobody enables.

## The Problem

An applicant tracking system is a state machine over candidates. Applied, screened, rejected, advanced, interviewed, offered, hired. Every transition is recorded with a timestamp.

The candidate is told about approximately one of them, sometimes. The acknowledgement email usually fires. After that, silence — through screening, through the weeks the requisition sits while the manager is busy, through the rejection that is recorded in the system and not sent, through the requisition closing with fifty candidates left in an intermediate state forever.

The system knows everything and sends nothing, because sending is a configuration option and the option is off.

## Why Nobody Has Built This

Defaults were set to off because employers were cautious about volume, about tone, about the legal implications of stating a reason, and about candidates replying. Each caution is small and the cumulative effect is silence.

Rejection specifically is avoided. A rejection email produces replies, occasional arguments and rare complaints, and the recruiter who sends it absorbs all of that, so it does not get sent. Nobody is measured on having sent it.

And the cost falls on the candidate and on the employer's reputation, both of which are diffuse and delayed relative to the recruiter's afternoon.

## What to Build

Communication as the system's default behaviour, with the honesty that makes it worth receiving.

**Notify on every transition, by default.** Application received, under review, not progressing, moved forward, interview scheduled, decision pending, decision made. Each transition already has an event; each should have a message unless the employer deliberately turns it off, which inverts the current configuration.

**Expose an honest status view.** Where the application is, what happens next, and by when. Not internal stage names but plain statements: "your application is with the hiring manager; we expect to decide by the 14th". Where the timeline slips, say so, which is more valuable than any other single message.

**Close the requisition properly.** When a requisition closes or is filled, every candidate still in an intermediate state is notified. This is a single automated action at close and it eliminates the largest population of permanently uninformed candidates in the industry.

**Give a reason where one exists.** Which stage, and the basis at a level that is truthful and general — did not meet a stated requirement, others had more directly relevant experience, the role was filled internally, the requisition was cancelled. The last two are extremely common and candidates never learn them, and they are the most reassuring things a rejected candidate can hear.

**Measure the silence.** Candidates who received no communication after the acknowledgement, time to rejection, share of rejections sent, share of requisitions closed with candidates left in limbo. These are counts over the event log, they are not reported anywhere, and they are the metric set this niche is about.

**Handle replies.** A candidate who replies to a rejection should reach something — an auto-response with the policy, a route for a genuine query. Fear of replies is a reason silence persists and a reply-handling path removes it.

## Target Customer

Employers competing for candidates, where experience affects pipeline quality measurably and where the worst performers are losing candidates they wanted. ATS vendors, who own the defaults and could change the industry's behaviour with a configuration change. And regulators, whose direction on transparency in hiring will reach this.

## Impact If Built

Candidates find out what happened, because notification is the system's default rather than an option nobody enabled. The population left permanently in limbo — the largest and most aggrieved group in hiring — disappears with a single action at requisition close. And the silence becomes a measured quantity that someone is accountable for.
