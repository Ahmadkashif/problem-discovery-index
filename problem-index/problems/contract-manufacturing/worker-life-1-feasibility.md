# Feasibility — SPC Alarm Triage and Root Cause Suggestion

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Problem:** [[problems/contract-manufacturing/worker-life-1|SPC Alarm Triage and Root Cause Suggestion]]
**Problem type:** Worker Life

**Problem summary:** Process engineers responding to SPC out-of-control alarms need rapid triage — which alarms require immediate process intervention, which can wait for end-of-shift review, and what the most likely root cause is — rather than individually investigating every alarm as it fires during high-volume production.

## Solution Approach
Ship a lightweight assistant that removes repetitive steps for frontline staff, with fast feedback loops and clear handoff to humans. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High for workers — improves retention and quality; commercial ROI is moderate but defensible as part of the platform.
