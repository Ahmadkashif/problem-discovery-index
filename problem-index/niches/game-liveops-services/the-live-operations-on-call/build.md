# A Runbook for Incidents That Are Not Technical

**Niche:** [[niches/game-liveops-services/the-live-operations-on-call/profile|The Live Operations On-Call]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The on-call person is paged for an event that is granting the wrong reward, not for a server that is down, and there is no procedure for that.
**Tags:** #worker-facing #workflow-orchestration #automation #change-point-detection #evaluation-metrics #large-language-models #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to make one person responsible for a game running in every timezone on a holiday weekend into something survivable — and whoever does it takes the account.

## The Problem
Live operations incidents are frequently not technical. An event is granting far more currency than intended. A configuration change has made a progression step impossible. A bug is being exploited at scale. The on-call person must decide, alone and at speed, whether to disable the event, roll back the value, compensate players, or wait — decisions with economic and community consequences that no infrastructure runbook covers and that they are not authorised to make.

## Why Nobody Has Built This
Incident tooling was built for availability, which is the one failure mode live ops has largely solved. Economy and design incidents require judgement, so nobody wrote procedures. Authority for out-of-hours economic decisions is undefined in most teams. And the role is small enough that no vendor has built for it.

## What to Build
Write the judgement down and pre-authorise the response. Build runbooks for the recurring non-technical incident classes — reward misconfiguration, exploit at scale, progression blocker, event failure — which is the core and is the difference between a decision and a panic. Pre-authorise a defined set of mitigations so the on-call person can act rather than escalate, since the escalation path at three in the morning is the actual failure mode. Detect economic anomalies automatically — grant rates, currency inflow, completion rates far outside the expected band — because the on-call person currently learns from the community. Provide one-click mitigations for the common cases: disable event, revert value, pause a reward. Estimate the impact of the incident so far, as the compensation decision depends on knowing the scale and it is usually guessed. Draft the player communication automatically, which is a task nobody at that hour does well. Record every incident with what was done and what it cost, so the runbook improves rather than the knowledge staying with one person. Route by the incident class rather than to a single generalist, which spreads the load. Support follow-the-sun handover for teams that can staff it. Define the authority limits explicitly, which is what lets someone act. And measure the on-call load and report it, since an unmeasured burden is never staffed.

## Target Customer
Live game operators, live ops platform vendors, outsourced live support providers, and incident response tooling vendors.

## Impact If Built
Infrastructure runbooks cover the one failure mode live ops has already solved, and none of the ones it actually gets paged for. Pre-authorised mitigations for economy and event incidents turn an escalation at three in the morning into an action.
