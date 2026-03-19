# Feasibility — Weld Quality Assessment from Visual Inspection Images

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Problem:** [[problems/metal-fabrication/high-impact|Weld Quality Assessment from Visual Inspection Images]]
**Problem type:** High Impact

**Problem summary:** Certified welding inspectors who evaluate weld surface appearance for AWS D1.1 acceptance criteria — reading porosity, undercut, overlap, and surface cracking from visual examination — perform a judgment task that takes years to develop and is a production bottleneck in every shop that can't afford enough qualified inspectors to keep pace with welder output.

## Solution Approach
Stand up a focused pilot that integrates current systems, captures the missing signals, and adds analytics/ML once the data path is stable. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
