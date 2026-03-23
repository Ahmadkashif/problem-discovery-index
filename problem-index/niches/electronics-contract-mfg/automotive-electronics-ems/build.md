# Predictive Process Capability Monitoring

**Niche:** [[niches/electronics-contract-mfg/automotive-electronics-ems/profile|Automotive Electronics EMS]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product predicts Cpk degradation trends and alerts before a process characteristic drifts below the automotive threshold (Cpk 1.67) — current SPC tools only report the current Cpk value, reacting to problems rather than preventing them.
**Tags:** #gradient-boosting #time-series-forecasting #tacit-knowledge-ml #compliance

## The Problem
IATF 16949 requires SPC monitoring of critical process characteristics (solder paste volume, component placement accuracy, reflow peak temperature) with Cpk > 1.67 for critical characteristics and > 1.33 for significant characteristics. Current SPC systems calculate and display the current Cpk value and trigger alerts when it drops below threshold. By the time Cpk crosses the threshold, the process has been producing boards with elevated defect risk for hours or days. An experienced process engineer reads SPC trend charts and recognizes early drift patterns — a gradual shift in mean, increasing variance, or cyclical patterns correlated with equipment wear — that predict Cpk degradation days before it reaches the alert threshold. This predictive judgment is the difference between proactive process adjustment (zero defects shipped) and reactive containment (sorting suspect boards after the fact).

## Why Nobody Has Built This
SPC software vendors (InfinityQS, WinSPC, Minitab) focus on statistical charting and control limit calculation — they display data, they do not predict. Adding predictive capability requires time-series forecasting models that account for equipment wear patterns, environmental factors (seasonal temperature/humidity variation), material lot changes, and operator behavior — variables that interact in complex ways. The training data (historical process parameter measurements with Cpk outcomes) exists in SPC databases but has not been used for prediction because SPC vendors view their product as a monitoring tool, not a prediction tool.

## What to Build
A predictive Cpk monitoring layer that sits on top of existing SPC data collection, ingests historical process measurements, equipment maintenance records, and material lot changes, and forecasts Cpk trajectory for each monitored characteristic. It alerts the process engineer when a characteristic is predicted to drop below threshold within 24-72 hours, with the probable cause (shift in mean suggesting equipment drift vs. increasing variance suggesting material lot variability). The engineer takes proactive corrective action before any defective product is made.

## Target Customer
Quality directors and process engineering managers at automotive-certified EMS providers monitoring 50+ critical characteristics across their program portfolio. Approximately 150-200 US automotive EMS providers. Average contract value: $50-100K/year.

## Impact If Built
Cpk excursion events decrease by 50-70% through proactive intervention. Containment costs (sorting, rework, customer chargebacks) decrease by $200K-1M per year at a typical automotive EMS provider. Customer scorecard quality ratings improve, directly affecting contract retention and new program awards.
