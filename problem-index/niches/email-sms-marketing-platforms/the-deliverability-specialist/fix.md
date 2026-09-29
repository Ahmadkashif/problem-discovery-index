# The Incident Nobody Wrote Down

**Niche:** [[niches/email-sms-marketing-platforms/the-deliverability-specialist/profile|The Deliverability Specialist]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The same provider blocked a sender for the same reason last year, it took three weeks to diagnose then and three weeks again, and nobody recorded either.
**Tags:** #tacit-knowledge-ml #workflow-orchestration #evaluation-metrics #descriptive-statistics #quick-win #automation #compliance #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to turn a craft practised by a few hundred people into a system anyone can operate — and whoever does that makes the scarcest expertise in the channel available to everyone who needs it.

## The Problem
A specialist spends three weeks diagnosing a placement collapse: checking authentication, examining list acquisition, correlating with a campaign change, testing hypotheses, eventually finding that a segment acquired through a particular source was driving complaints. They fix it. The account recovers. Nothing is written down beyond a support ticket closed with resolved. Eleven months later the same pattern occurs at a different customer of the same platform, and a different specialist spends three weeks on it. Across a platform's customer base this repeats constantly, and the platform has all the data from every one of those incidents.

## Why It's Still Broken
Incidents are handled as support tickets and closed, which records that something was resolved and not what it was or how — the ticket model captures the transaction rather than the knowledge. Writing a proper postmortem is unpaid work at the end of an exhausting episode. Nobody is responsible for the platform's accumulated diagnostic knowledge. And the repetition is invisible because each incident belongs to a different customer.

## What a Fix Looks Like
Record the incident, not just the resolution. Capture a structured postmortem for every placement incident — symptoms, provider, timeline, hypotheses tested, cause, remediation, recovery time — which is the fix, takes twenty minutes, and is the difference between a platform that learns and one that re-solves. Match new incidents against the history automatically, so a specialist starts from the three most similar past cases rather than from nothing. Report recurring causes across the customer base, which reveals patterns no individual incident shows and frequently points at something the platform itself should change. Record what did not work, since ruling out hypotheses is most of the diagnostic time and is never written down. Track recovery times by cause, which answers the question every affected customer asks first. Feed the corpus into the automated diagnosis, which is what makes the expert system in the build note credible rather than theoretical. Detect provider behaviour changes from clusters of similar incidents, which is genuinely valuable in the first days and is currently noticed through community chatter. Share anonymised findings with the practitioner community, since the knowledge accumulated collectively and the community is how it improves. Make the postmortem part of closing the case rather than an optional extra. And measure repeat incidents, because a platform seeing the same cause monthly has a product problem rather than a support problem.

## Who Feels the Pain
Specialists re-diagnosing problems their colleagues solved; customers waiting three weeks for an answer the platform already had; and platforms whose most valuable operational knowledge closes with a ticket.

## Impact If Fixed
The ticket model records that something was resolved rather than what it was, so the same cause is re-diagnosed across customers indefinitely. A twenty-minute structured postmortem matched against history turns three weeks of work into starting from the three most similar past cases.
