# Time Capture & the Unbilled Hour

**Industry:** [[legal-practice-software|Legal Practice Software]]
**Type:** High Impact
**One-liner:** The platform reconstructs the day's billable work from what actually happened on the machine and in the matter, so the lawyer edits a proposed timesheet instead of trying to remember Tuesday.
**Tags:** #transformers #bert #large-language-models #word-embeddings #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact #worker-facing

## The Problem
Small-firm lawyers lose a large fraction of their billable time — commonly estimated between fifteen and thirty per cent — simply by failing to record it. A six-minute call, a document reviewed between meetings, an email exchange that resolved a question, a court call that ran short. The work happened. The entry never got made, or got made three days later at half its true length because that is what the lawyer could defend from memory.

Every practice management vendor sells against this. The tools offered are a manual timer, a passive activity tracker, and a reconstruction view that shows the day's calendar entries, emails and documents so the lawyer can rebuild the timesheet. All three put the burden back on the lawyer at the end of a day when they are least willing to carry it.

The reconstruction view is the interesting one, because it is nearly the right idea. The platform already knows which documents were opened and edited, which emails were sent on which matter, which calls appear in the call log, which court dates were on the calendar and how long each application had focus. It presents that as a list of raw events and asks the lawyer to convert it into billable entries — which is the hard part, and the part it has not attempted.

## Why It's Unsolved
Converting activity into a defensible time entry requires three judgements the software has never made. Which matter does this activity belong to — often ambiguous, since one document may relate to two matters and email threads drift. What is the billable duration, which is not the same as elapsed time, because lawyers interleave work and because a four-minute task is conventionally billed at a tenth of an hour. And what is the narrative, which must describe the work in language that survives a client's scrutiny and, in insurance defence or fee-shifting contexts, an auditor's.

The narrative requirement is underrated. Time entries are read by paying clients and are routinely reduced. "Review documents — 2.4" gets written off; a specific, defensible description does not. Lawyers know this and it is part of why entry is slow.

The data is also sensitive in a way that constrains the design. Passive capture across a lawyer's machine touches privileged material, client confidences and the lawyer's own conduct, and any product that transmits that off-device faces an ethics objection before a technical one. This is the reason several credible attempts have stalled, and it argues for on-device inference rather than a cloud pipeline.

## What a Solution Looks Like
A system that watches activity locally, groups related events into work sessions, assigns each session to a matter with a confidence score, estimates the billable duration in the firm's own increment convention, and drafts a narrative in the language that firm actually uses. It presents the lawyer with a proposed timesheet at the end of the day: eleven entries, each editable, most correct. The lawyer confirms rather than reconstructs.

It learns from every edit — which matters get confused with each other, which narratives get rewritten, how this lawyer rounds — so accuracy climbs per user rather than staying at the vendor's average.

Privileged content stays on the device. What leaves is the entry the lawyer approved.

## Impact If Solved
Recovering even half of the routinely lost time is a direct increase in a small firm's revenue with no additional work performed, no new clients, and no rate increase. It is the only feature in the category that pays for itself arithmetically in the first month, which is why every vendor claims it and why solving it properly would end the switching contest.
