# Feasibility — DHR Assembly from Disconnected Systems

**Industry:** [[medical-device-mfg|Medical Device Manufacturing]]
**Problem:** [[problems/medical-device-mfg/low-impact-1|DHR Assembly from Disconnected Systems]]
**Problem type:** Low Impact

**Problem summary:** Device History Records — the complete production documentation package that FDA requires for every manufactured lot — are assembled by quality technicians who manually pull records from MES, ERP, LIMS, and quality systems and compile them into a single document, a 2-4 hour task per lot that generic document management cannot automate because it doesn't understand the DHR structure or the cross-system record linkages.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
