# The Database Support Engineer

**Parent Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to capture the state that explains an incident while the incident is happening — and whoever does that takes the support organisation, because reconstruction after the fact is most of what database support does.

## Profile
**Market Size:** ~$890M US attributable to database support and escalation operations
**Share of Parent Industry:** ~4% of category revenue
**Digital Adoption:** Low — reconstruction is done from logs and memory
**Target Buyer:** Vendor support leadership; the beneficiary is the support engineer
**Automation Potential:** Very High — the state exists during the incident and is discarded

## What Makes This a Distinct Niche
Database support has a specific and difficult shape: the incident is over by the time the ticket arrives, the state that would explain it was transient, and the evidence available is a log, a metric graph at one-minute resolution, and a customer's recollection. The support engineer's day is spent reconstructing what happened — which query was blocking, what the plan was at the time, what the lock graph looked like, what the connection state was — from artefacts that mostly do not contain it. The engines expose all of that information while an incident is occurring and retain none of it afterwards, because capturing it continuously would be expensive. This is a distinct contested surface because the remedy is a capture design rather than an analysis: decide what to snapshot and when, triggered by the conditions that indicate an incident, and the reconstruction problem largely disappears.

## Current Tools & Gaps
Slow query logs, periodic statistics snapshots at coarse intervals, general logs, and diagnostic collection scripts the customer runs afterwards. The gaps: the highest-value state — active sessions, the lock graph, running query plans, wait events — is available live and is not sampled at incident-relevant resolution; capture is not triggered by conditions, so the interesting moments are exactly the ones not covered; customers run diagnostic collection after the event, when the state is gone; escalations to engineering are frequently requests for help reconstructing rather than for engineering judgement; and the same incident pattern is diagnosed repeatedly across customers with nothing connecting the instances.

## Problems
- [[niches/database-platform-vendors/database-support-engineer/build|🔨 Build: Reconstructing From What Was Not Recorded]]
- [[niches/database-platform-vendors/database-support-engineer/buy|🛒 Buy: Flight Recorder Patterns From Other Systems]]
- [[niches/database-platform-vendors/database-support-engineer/fix|🔧 Fix: The Diagnostic Script Run After the State Is Gone]]
