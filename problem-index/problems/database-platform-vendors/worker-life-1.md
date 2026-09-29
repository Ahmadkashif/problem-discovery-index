# Support Engineer Reconstructing the Incident

**Industry:** [[database-platform-vendors|Database Platform Vendors]]
**Type:** Worker Life Changing
**One-liner:** Database support engineers stop reconstructing what happened during an incident from logs after the fact, because the state that would have explained it is captured while the incident is occurring.
**Tags:** #change-point-detection #gradient-boosting #bert #k-means-clustering #time-series-forecasting #evaluation-metrics #automation #worker-facing

## The Problem
A customer's database had an incident. It is over now — restarted, scaled up, or it recovered on its own — and they want to know why.

The support engineer reconstructs from what survived. Metrics at whatever resolution was retained, which is usually coarser than the event. Logs, if the relevant logging was enabled, which it frequently was not because it costs performance. Slow query logs with a threshold set high enough to have missed the queries that mattered. A description from the customer, who was busy fixing it.

The information that would have answered the question immediately — the active session list, the lock graph, the running query plans, the wait events at the moment of the incident — existed and was not captured, because capturing it continuously costs overhead and nobody enables it in advance.

So the engineer builds a plausible account from partial evidence. Often they are right. Sometimes the honest answer is that the data does not support a conclusion, which is unsatisfying for everyone and is what the escalation exists to avoid.

## Why It Matters to the Worker
Database support attracts genuinely deep engineers, and the work should be applying that depth. Instead a large share is forensics on insufficient evidence.

The interaction carries pressure of a specific kind. The customer had an outage, they are frightened it will recur, and they want certainty. Providing a hedged answer built on gaps is professionally uncomfortable and reads to the customer as evasion.

The repetition is the other frustration. The same failure modes arrive constantly — lock contention from a long-running transaction, plan regression after a statistics update, connection exhaustion, vacuum falling behind — and each is investigated from scratch because nothing matched the current incident against the previous thousand.

And the fix is known to everyone involved: capture the state during the incident. It is not enabled because it is off by default and nobody thinks about it until afterwards.

## What a Solution Looks Like
Automatic state capture on anomaly. When key indicators cross a threshold, the platform should snapshot active sessions, locks, running plans and wait events — a small, bounded cost incurred only during unusual conditions, which is exactly when the data is worth having.

Incident signature matching against the fleet. The same failure modes recur across thousands of customers with recognisable signatures, and matching a current incident to prior ones with their resolutions is the single largest reduction in investigation time available.

Retention shaped by relevance. High-resolution data around anomalies and coarse data otherwise gives the forensic detail where it matters without the storage cost of keeping everything.

Query-level attribution during the event, so the engineer can say which statement caused the lock pile-up rather than inferring it from a shape.

And a customer-facing narrative generated from the captured state, so the routine cases are explained without an escalation at all.

## Impact If Solved
Database incident investigation is forensics on evidence that was not collected, performed by deep engineers under customer pressure to be certain. Capturing state on anomaly is a small, bounded change that transforms the evidence available, and fleet signature matching turns the thousandth instance of a known failure into a lookup.
