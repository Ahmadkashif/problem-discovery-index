# Build: Continuous Safeguarding Rather Than a One-Time Check

**Niche:** [[niches/online-tutoring-platforms/vetting-and-safeguarding/profile|Tutor Onboarding, Vetting & Safeguarding]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Replace a check at the door with continuous monitoring of the conditions that matter — record updates, contact patterns, and the signals that indicate a relationship is moving off-platform.
**Tags:** #gradient-boosting #large-language-models #evaluation-metrics #confidence-intervals #compliance #change-point-detection #automation #graph-theory
**Contested on:** Whether the signals that precede a safeguarding problem can be detected without surveilling ordinary teaching.

## The Problem

Safeguarding in this industry is largely a background check performed once, at onboarding, plus a recording nobody watches. Both are real measures and neither addresses the shape of the risk.

Background checks capture what is on record at the moment they run. Records change. A tutor screened two years ago may have a new one, and continuous re-screening — standard practice in several adjacent industries — is inconsistently applied here.

The recording is a deterrent and a source of evidence after the fact. It is not monitoring, because nobody watches it, and the assumption that it is monitoring has substituted for building any.

And the pattern that concerns safeguarding professionals most — a relationship moving off-platform, into private messaging, with contact outside sessions and a growing separation from the parent — is detectable in platform behaviour and is not monitored at all, though it is prohibited in every terms of service in the industry.

## Why Nobody Has Built This

Cost and caution. Continuous re-screening costs money per tutor per year across a large contractor base. Behavioural monitoring costs engineering and raises a genuine tension: a system watching for concerning patterns in interactions between adults and children can easily become surveillance of ordinary teaching, generate false positives that destroy innocent tutors' livelihoods, and feel intrusive to families.

That tension is real and it has been resolved by doing very little, which is the worst available resolution. The concerning patterns here are behavioural and structural — contact frequency outside sessions, attempts to exchange external contact details, session scheduling changes, requests to disable recording — rather than requiring any analysis of teaching content at all.

There is also no external forcing function in the consumer segment. Districts impose standards; parents have no way to compare, so nobody competes on it.

## What to Build

Continuous monitoring of the structural signals, with the content of teaching left alone.

**Re-screen continuously.** Subscribe to record-update monitoring rather than running a point-in-time check, so a new record surfaces when it occurs. This is a purchased service, it is the single most effective measure available, and it is a procurement decision more than an engineering one.

**Monitor the structural signals, not the teaching.** Attempts to exchange phone numbers, emails or external platform handles in messages. Contact outside scheduled sessions. Sessions scheduled outside normal hours. Requests to disable recording or to use an external video service. A tutor whose relationship pattern with one student diverges sharply from their pattern with all the others. These are metadata and message-level signals, they are what the prohibited-contact rule is actually about, and they require no analysis of what is taught.

**Separate the response from the detection.** A flag is a prompt for human review by a trained safeguarding reviewer, never an automated action. The base rate of genuine safeguarding concern is very low, so even a good classifier produces mostly false positives, and the review process — with training, supervision, escalation paths and documented decisions — is the actual safeguard.

**Make reporting easy and visible.** A clear route for a student or a parent to report a concern, findable during a session, with a stated response time. Many safeguarding systems fail at this most basic point, and it is the channel through which real concerns most often arrive.

**Publish the standard.** What checks are performed, how often they are refreshed, what monitoring exists, what the reporting route is, and what happens on a report. A platform that publishes this creates the comparison that currently does not exist and lets careful operators be recognised as such.

**Design the privacy posture explicitly.** Session recordings of minors, message monitoring, retention limits, access controls, and a clear statement to families about what is watched and what is not. Being specific about the limits is what makes the monitoring acceptable rather than intrusive.

## Target Customer

Platform trust and safety leadership, and the district and school segment, where safeguarding standards are procurement requirements with audits attached. District contracting is what drives this work at most platforms and it raises the standard for the consumer segment alongside it.

## Impact If Built

The check at the door becomes continuous, which is the difference between knowing who someone was two years ago and knowing who they are. The pattern that safeguarding professionals actually watch for gets monitored rather than merely prohibited. And a published standard lets parents distinguish careful platforms from careless ones, which is the only mechanism by which the floor rises.
