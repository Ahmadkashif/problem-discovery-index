# Feasibility — Engineering Change Order Impact Assessment

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Problem:** [[problems/contract-manufacturing/low-impact-1|Engineering Change Order Impact Assessment]]
**Problem type:** Low Impact

**Problem summary:** Generic document analysis tools can read engineering change orders, but don't understand BOM structures, process qualification requirements, or the downstream impact of a material substitution on production tooling, test fixtures, and quality specifications — the manufacturing-specific reasoning that determines whether an ECO is a simple update or a multi-week re-qualification event.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
