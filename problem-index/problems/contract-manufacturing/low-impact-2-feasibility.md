# Feasibility — Automated Visual Inspection for Surface Defect Detection

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Problem:** [[problems/contract-manufacturing/low-impact-2|Automated Visual Inspection for Surface Defect Detection]]
**Problem type:** Low Impact

**Problem summary:** Generic computer vision models can detect anomalies in images, but don't know a specific part's acceptance criteria — which surface conditions are cosmetic defects vs. acceptable variation vs. functional defects, as defined in the OEM's workmanship standard for that specific part number — the product-specific classification logic that makes automated inspection useful rather than a source of false rejects.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
