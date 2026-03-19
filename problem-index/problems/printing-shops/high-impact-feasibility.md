# Feasibility — Print Job Estimating Accuracy and Speed

**Industry:** [[printing-shops|Printing Shops]]
**Problem:** [[problems/printing-shops/high-impact|Print Job Estimating Accuracy and Speed]]
**Problem type:** High Impact

**Problem summary:** Print estimators who quote jobs by mentally simulating the entire production process — calculating paper waste from sheet size and imposition, estimating ink coverage and press time from the artwork, predicting finishing complexity from the binding specification — take 30-90 minutes per quote using knowledge that took a decade to develop, and their departure leaves the shop unable to price work accurately.

## Solution Approach
Stand up a focused pilot that integrates current systems, captures the missing signals, and adds analytics/ML once the data path is stable. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
