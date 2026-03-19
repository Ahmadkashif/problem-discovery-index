# Feasibility — NPI First-Pass Yield Ramp Optimization

**Industry:** [[electronics-contract-mfg|Electronics Contract Manufacturing]]
**Problem:** [[problems/electronics-contract-mfg/high-impact|NPI First-Pass Yield Ramp Optimization]]
**Problem type:** High Impact

**Problem summary:** Process engineers who spend 3-6 months empirically tuning SMT parameters — reflow profiles, stencil aperture designs, placement machine settings, solder paste volumes — for each new customer program could ramp to stable yield in weeks if an ML model predicted optimal starting parameters from the BOM's thermal mass characteristics and component package types, eliminating the costly trial-and-error that currently costs ECMs 5-15% margin on every NPI.

## Solution Approach
Stand up a focused pilot that integrates current systems, captures the missing signals, and adds analytics/ML once the data path is stable. Layer on MES/SCADA/quality logs, apply SPC/ML for anomalies, and pilot on one line before scaling.

## Open Source Data
Safety standards and some process benchmarks are public; yields, scrap, and line telemetry stay proprietary.

## Worth Solving?
High — core outcome/financial impact justifies investment if change management is handled.
