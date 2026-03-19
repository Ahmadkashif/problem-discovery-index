# Feasibility — CAPA Root Cause Identification and Cycle Time Reduction

**Industry:** [[medical-device-mfg|Medical Device Manufacturing]]
**Problem:** [[problems/medical-device-mfg/high-impact|CAPA Root Cause Identification and Cycle Time Reduction]]
**Problem type:** High Impact

**Problem summary:** Quality engineers investigating CAPAs — the corrective and preventive action process that FDA inspectors scrutinize more than any other quality system element — spend 45-90 days per investigation manually cross-referencing complaints, production records, supplier data, and DHRs across disconnected systems to identify root causes that an ML system could surface in hours by detecting patterns across the entire complaint-production-supplier data landscape.

## Solution Approach
Stand up a focused pilot that integrates current systems, captures the missing signals, and adds analytics/ML once the data path is stable. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
