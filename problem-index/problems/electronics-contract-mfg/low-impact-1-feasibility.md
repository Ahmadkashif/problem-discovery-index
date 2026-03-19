# Feasibility — BOM Scrubbing and AVL Cross-Reference

**Industry:** [[electronics-contract-mfg|Electronics Contract Manufacturing]]
**Problem:** [[problems/electronics-contract-mfg/low-impact-1|BOM Scrubbing and AVL Cross-Reference]]
**Problem type:** Low Impact

**Problem summary:** Component search and cross-reference tools like Octopart and SiliconExpert exist for general electronics sourcing, but none of them understand an ECM's facility-specific AVL (Approved Vendor List), customer-specific component restrictions, or the form-fit-function equivalence criteria that determine whether an alternative component can actually be substituted on a specific PCBA without engineering change approval.

## Solution Approach
Adapt a horizontal tool with industry-specific templates, rules, and integrations so teams stop working around generic software. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
