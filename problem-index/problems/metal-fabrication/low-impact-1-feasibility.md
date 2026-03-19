# Feasibility — Fabrication Quote Estimation from Drawing Features

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Problem:** [[problems/metal-fabrication/low-impact-1|Fabrication Quote Estimation from Drawing Features]]
**Problem type:** Low Impact

**Problem summary:** Generic ML regression models can predict costs from structured inputs, but don't understand fabrication drawing features — weld joint accessibility, distortion risk from asymmetric heat input, the difference between a weld that looks simple and one requiring multiple passes and repositioning — the geometric reasoning that separates experienced fabrication estimators from a spreadsheet.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
