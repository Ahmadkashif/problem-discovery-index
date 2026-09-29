# Fix: The Real Finding Closed as Informative

**Niche:** Triage Operations
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The most expensive error in the system is a genuine vulnerability dismissed as a non-issue, and no platform measures how often it happens.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #compliance #revenue-impact
**Contested on:** Whether a qualified analyst's attention is spent on submissions that might be real, or spread evenly across a queue that is mostly not.

## The Problem

Triage makes two kinds of mistake. It can accept something that is not a real finding, which costs a payout and some embarrassment. And it can close a real vulnerability as informative, out of scope or a non-issue — which leaves the weakness in production, tells a researcher who was right that they were wrong, and produces no signal to anybody that it happened.

The second error is far more expensive and is completely invisible. When a submission is closed, the process ends. Nobody re-examines it. If the vulnerability is later exploited, or found by a subsequent test, nothing connects that event back to the submission that described it months earlier. The organisation experiences an incident and the dismissed report is not part of the investigation because nobody thought to look.

Researchers know this happens. Every experienced participant has a story about a finding closed as informative that they still believe was real, and the community's periodic public disputes about exactly this are the most damaging thing that happens to a programme's reputation.

And nobody has a number. No platform, no programme, publishes or internally tracks the rate at which valid findings are wrongly dismissed. It is the most important quality metric in the operation and it does not exist.

## Why It's Still Broken

**The error generates no feedback.** A wrongly closed submission produces silence. There is no complaint mechanism with teeth, no downstream event that points back, and no natural moment at which anyone discovers the mistake.

**Measuring it requires deliberate re-examination.** The only way to know the rate is to take a sample of closed submissions and have a second qualified analyst re-assess them blind. That costs scarce analyst time on work that produces no throughput, and it produces a number nobody wants.

**Volume pressure pushes toward closure.** An analyst working a large queue with a time target faces an asymmetry: closing a borderline submission is fast and its cost is invisible, while escalating is slow and its cost is immediate. The incentive structure quietly favours the expensive error.

**Researcher appeals are weak.** A researcher who disputes a closure is arguing with the party who closed it. Persistence risks reputation and programme invitations, so most accept and move on, which removes the last signal that might have surfaced the error.

**Nobody is accountable for it.** Triage quality is measured by throughput and time, which are the things that can be counted. The error that matters is not in anyone's objectives.

**The incident link is never made.** When a breach occurs, the investigation examines logs and systems. Searching closed bounty submissions for a description of the exploited weakness is not part of any standard incident process, and it should be.

## What a Fix Looks Like

**Sample and re-examine, routinely.** A small percentage of closed submissions re-assessed by a second analyst, blind to the original decision, on a continuous basis. This produces the missing number, costs a few per cent of triage capacity, and is the prerequisite for everything else. Annotation and assessment operations have run exactly this for years.

**Search closed submissions during every incident.** When a vulnerability is exploited or discovered by another channel, check whether anyone reported it. This is a five-minute step that belongs in every incident runbook and is in almost none, and each hit is both a serious finding about the triage process and a debt owed to a researcher.

**Give borderline cases somewhere to go.** A defined escalation for submissions an analyst is genuinely unsure about, with no throughput penalty for using it. The current structure penalises uncertainty, which is precisely backwards.

**Make appeals independent and cheap.** A researcher disputing a closure should reach someone other than the person who closed it, without cost to their standing. Tracking appeal outcomes also produces a second estimate of the error rate.

**Report the metric internally and treat it as the quality measure.** Throughput and time-to-triage are operational; wrongly-closed rate is quality. A triage operation managed on the first two and blind to the third is managing the wrong thing.

**Reopen and pay when it is found.** A programme that discovers it wrongly closed a valid finding should reopen and pay it. This is rare enough to be inexpensive and does more for a programme's standing in the researcher community than any amount of engagement.

## Who Feels the Pain

The organisation, which had the vulnerability described to it in writing, declined it, and remains exposed.

The researcher, told they were wrong when they were right, with no appeal that does not cost them — and this is the experience that most reliably drives capable people out of a programme.

The analyst, working under a throughput target with an incentive structure that makes the expensive error the cheap choice, and no feedback that would let them calibrate.

And the platform, whose reputation with researchers depends on exactly this and which has no measurement of it.

## Impact If Fixed

Sampling and re-examination produces the number, and the number is the whole fix — a rate that is currently unknown everywhere would immediately become a thing operations are managed against.

Searching closed submissions during incident investigation costs nothing, belongs in every runbook, and would occasionally reveal that the organisation was told about the breach months in advance.

And an independent, cost-free appeal path would restore the one signal that currently gets suppressed by the power asymmetry, in the place where suppressing it is most expensive.
