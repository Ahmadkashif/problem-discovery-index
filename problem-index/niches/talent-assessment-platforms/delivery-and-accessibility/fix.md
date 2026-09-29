# Fix: The Accommodation Request Nobody Answers in Time

**Niche:** [[niches/talent-assessment-platforms/delivery-and-accessibility/profile|Assessment Delivery, Proctoring & Accessibility]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A candidate who needs extra time emails the address in the invitation, receives nothing before the deadline, and takes the assessment without the adjustment or not at all.
**Tags:** #compliance #workflow-orchestration #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Whether a request for an adjustment will reach someone who can grant it before the deadline passes.

## The Problem

An assessment invitation arrives with a deadline of a few days. A candidate with a disability needs an adjustment — extra time, a screen reader compatible version, a break, a different format.

The invitation may mention accommodations, usually as a line directing them to contact the employer. They email. The address is a recruiting mailbox handling hundreds of messages. Nobody replies within the deadline. The candidate takes the assessment unadjusted and is measured on their disability, or does not take it and is recorded as having withdrawn.

This is a legal obligation being failed by a workflow gap. The employer intends to accommodate; the vendor supports accommodations; and the request has no path between them that operates on the timescale of the deadline.

## Why It's Still Broken

Accommodation sits between the vendor, who can technically grant it, and the employer, who owns the obligation, and the request arrives at whichever of them the invitation names — usually a general recruiting address with no routing.

The deadline does not pause, so a request that is eventually answered is answered too late. Nothing in the workflow connects a pending request to the assessment's expiry.

And the failure is invisible. A candidate who withdraws is a withdrawal; a candidate who took it unadjusted is a score. Neither is recorded as an accommodation failure, so nobody knows the rate.

## What a Fix Looks Like

Put the request in the assessment flow, route it, and pause the clock.

Add a request path inside the assessment invitation and the assessment itself — a form, not an email address — with the common adjustments listed so a candidate can select rather than compose. Findable before starting and during, since some needs only become apparent once the interface is open.

Pause the deadline automatically on request. The clock stops until the request is resolved. This single rule removes most of the harm and is a state change.

Route to someone accountable with an SLA. Whoever can grant it — vendor support for technical adjustments, the employer for process ones — with a defined response time and escalation if it is missed.

Grant the routine ones automatically. Extra time within a standard range, breaks, and screen-reader-compatible presentation should not require adjudication, documentation or a conversation. Most requests are routine and the deliberation adds nothing but delay.

Ask for documentation only where it is genuinely needed, and never as a default. Requiring medical evidence for fifteen extra minutes is a deterrent rather than a control.

Maintain equivalence and say so. An accommodated version must measure the same construct, and where the accommodated form's equivalence has not been established, that is a fact the employer should know.

And measure the rate. Requests made, granted, response times, and outcomes for accommodated candidates. Nobody has these numbers, and the first organisation to produce them will find out whether their process works.

## Who Feels the Pain

Candidates with disabilities, who face a process that fails silently and are recorded as withdrawals or as low scores. Recruiters who receive a request in a general mailbox and do not know what to do with it. Employers with a legal obligation being breached by a routing gap they are unaware of. And vendors, whose platform supports the accommodation that the workflow never reaches.

## Impact If Fixed

A request reaches someone who can act on it, and the deadline stops while it does. Routine adjustments get granted automatically rather than adjudicated late. And the accommodation failure rate — currently unknown and recorded as ordinary withdrawal — becomes a number someone is accountable for.
