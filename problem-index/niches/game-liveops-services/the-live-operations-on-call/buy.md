# Incident Response From Site Reliability Engineering

**Niche:** [[niches/game-liveops-services/the-live-operations-on-call/profile|The Live Operations On-Call]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Site reliability engineering built rotations, runbooks, severity levels and blameless review, and live ops on-call has a pager and a chat channel.
**Tags:** #workflow-orchestration #automation #worker-facing #evaluation-metrics #compliance #change-point-detection #confidence-intervals #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make one person responsible for a game running in every timezone on a holiday weekend into something survivable — and whoever does it takes the account.

## The Problem
Site reliability engineering turned on-call from an endurance test into a discipline: defined severity levels, runbooks per alert, rotations sized against measured load, escalation policies, automated mitigation, blameless post-incident review and explicit limits on paging volume. The practice is mature, the tooling is commercial, and it is the standard for anyone operating a service continuously. Live operations on-call — a structurally identical role — has adopted almost none of it.

## What Already Exists
Severity classification; runbooks bound to alerts; rotation and escalation management; automated mitigation and rollback; and blameless post-incident review.

## The Customization Gap
The adaptation is to incidents that are economic and social rather than technical. It requires: (1) severity defined by economic and player-experience impact rather than by availability — an event granting double rewards is not an outage and is more consequential than one, which is the substantive difference; (2) runbooks that encode design judgement rather than remediation steps; (3) mitigations that alter the game's economy, so rollback has player-facing consequences that a service rollback does not; (4) a community that is watching and discussing the incident in real time, requiring communication as part of the response; and (5) a responder who is a live operations manager rather than an engineer, which changes the tooling's whole vocabulary.

## Target Customer
Live game operators, live ops managers, incident response vendors, and outsourced live support providers.

## Impact If Solved
SRE turned on-call from endurance into discipline and the tooling is commercial. Severity defined by economic impact, runbooks encoding design judgement, and a watching community are what the borrowed practice does not cover.
