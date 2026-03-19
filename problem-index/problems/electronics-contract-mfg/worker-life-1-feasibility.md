# Feasibility — SMT Operator Changeover Time Between Product Runs

**Industry:** [[electronics-contract-mfg|Electronics Contract Manufacturing]]
**Problem:** [[problems/electronics-contract-mfg/worker-life-1|SMT Operator Changeover Time Between Product Runs]]
**Problem type:** Worker Life

**Problem summary:** SMT operators who execute product changeovers — swapping feeder reels, changing stencils, loading new placement programs, and adjusting reflow profiles — spend 45-90 minutes on each changeover for short-run programs, and as production shifts toward higher-mix lower-volume, the ratio of changeover time to production time increasingly dominates their shift.

## Solution Approach
Ship a lightweight assistant that removes repetitive steps for frontline staff, with fast feedback loops and clear handoff to humans. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High for workers — improves retention and quality; commercial ROI is moderate but defensible as part of the platform.
