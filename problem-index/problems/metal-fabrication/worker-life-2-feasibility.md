# Feasibility — Nesting Efficiency Feedback and Material Remnant Tracking

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Problem:** [[problems/metal-fabrication/worker-life-2|Nesting Efficiency Feedback and Material Remnant Tracking]]
**Problem type:** Worker Life

**Problem summary:** CNC operators and estimators who track material utilization manually — logging remnant sizes in notebooks or spreadsheets, estimating nesting efficiency after the fact — need automated remnant inventory and nesting outcome tracking that identifies which job types systematically waste material and which remnant pieces can be reused on upcoming jobs.

## Solution Approach
Ship a lightweight assistant that removes repetitive steps for frontline staff, with fast feedback loops and clear handoff to humans. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High for workers — improves retention and quality; commercial ROI is moderate but defensible as part of the platform.
