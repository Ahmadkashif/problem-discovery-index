# The Signing Ceremony Nobody Monitors

**Niche:** [[niches/crypto-exchanges/custody-and-key-operations/profile|Custody & Key Operations]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** Approvals are collected, the transaction is signed, and nothing is watching for the pattern that means something is wrong.
**Tags:** #change-point-detection #graph-theory #quick-win #automation #evaluation-metrics #compliance #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to prove continuously that customer assets exist, are controlled, and are not encumbered — without revealing the operational detail that would help an attacker — and whoever proves it best takes the institutional accounts.

## The Problem
Withdrawals from cold storage require a ceremony: specified approvers, a policy check, signatures assembled, the transaction broadcast. The controls are preventive and strong. What is absent is detection — nobody is watching whether the approvals are arriving at unusual hours, from unusual locations, in unusual combinations, for destinations that have never been used, at a frequency that has changed. Every major custody compromise involved the legitimate signing path being used illegitimately, and the pattern was visible in retrospect.

## Why It's Still Broken
Custody security was designed as prevention, so the assumption was that a completed ceremony is a valid one — and a control that succeeds by definition never gets a detection layer. Ceremony logs live in operational systems rather than in monitoring. The volume is low, which makes anomalies look like normal variation to anyone not modelling them. And the team that runs ceremonies is the team that would be monitored.

## What a Fix Looks Like
Monitor the ceremony as behaviour. Log every ceremony with its full context — approvers, timing, location, destination, amount, policy path — which is the fix and is data being produced and discarded. Baseline the normal pattern, since the volume is low enough that the baseline is learnable and unusual is genuinely unusual. Alert on destination addresses never used before, because that is the single most informative signal and is a one-line check. Flag approver combinations that have not occurred before, as compromise usually shows first in who is approving. Watch timing and location shifts, since ceremonies follow human routines and deviations are meaningful. Separate monitoring from operations, because the team being watched cannot own the watching. Require a second channel confirmation for anomalous ceremonies, which converts detection into prevention at the moment it matters. Rehearse the response to a detected anomaly, since an alert with no practised response is a delay. Review the ceremony record periodically with fresh eyes, as patterns emerge over months that no single alert catches. And measure detection coverage against the known compromise patterns from other exchanges, which are public and specific.

## Who Feels the Pain
Security teams relying entirely on prevention; custody operators whose actions are unreviewed; institutional depositors trusting an unmonitored path; and every exchange whose predecessors lost funds through a legitimate signing path.

## Impact If Fixed
Prevention was the whole design, so a completed ceremony was assumed valid and detection was never added. Ceremony context is already logged, and baselining destination, approver and timing patterns catches the exact shape every major compromise took.
