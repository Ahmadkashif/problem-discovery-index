# Telemetry Turned Into a Dispatched Part

**Niche:** [[niches/field-service-software/oem-installed-base-service/profile|OEM Service on Its Own Installed Base]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Manufacturers connected their installed base and built alerting on sensor thresholds, which tells a service organisation that something is out of range rather than which component to bring on Tuesday.
**Tags:** #survival-analysis #time-series-forecasting #change-point-detection #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in OEM service software is fighting to convert telemetry and engineering knowledge from the manufacturer's own installed base into a dispatched action before the customer notices a fault — and whoever converts most reliably takes the account.

## The Problem
A machine reports a vibration reading above threshold. An alert fires, a case is created, and a technician is scheduled to investigate — which is a diagnostic visit, not a repair, and consumes exactly what predictive maintenance was supposed to save. He arrives, finds a bearing beginning to fail, does not have the bearing, and returns. The telemetry contained enough signal to identify the component and the time horizon; it was used to fire a threshold. This is the typical state of connected-product service programmes across the industry, and it is why so many of them have failed to deliver the returns promised.

## Why Nobody Has Built This
Threshold alerting is what a connected-product platform ships, and moving beyond it requires labelled failures — telemetry paired with what was actually found and replaced — which lives in the service system, in a different organisation, in a form that does not join cleanly to a machine's serial number and a time window. Building the join is a cross-organisational project with no single owner, and it is unglamorous next to the connected-product programme's own roadmap. There is also a commercial hesitation: a prediction that leads to a proactive part replacement can look, to a customer paying for a contract, like the manufacturer replacing things that had not failed, which requires a conversation the service organisation would rather not open.

## What to Build
A component-level failure prediction trained on telemetry joined to confirmed field outcomes, returning a predicted component, a time horizon and a confidence rather than an anomaly. The horizon is the product requirement: a prediction with four hours of lead time is an alarm, and one with three weeks is a service plan — it lets the part ship, the visit combine with a scheduled one, and the customer be given a choice. Outputs feed the service platform directly as a proposed work order with the part attached, not as a case for someone to triage. Calibration is reported per model and per component, because a service organisation will extend trust only as far as the track record, and because the alternative failure — proactively replacing parts that had years left — is exactly the outcome that discredits these programmes.

## Target Customer
Equipment manufacturers with connected installed bases in industrial, medical, refrigeration, HVAC, packaging and agricultural equipment, and the service platform vendors positioned between the IoT stack and the dispatch system.

## Impact If Built
Converting reactive events into planned ones with the right part in hand is the whole promise of connected service and is rarely realised; the difference between a threshold alert and a component-level prediction is where that gap lives. For the manufacturer it also defends the service business against third-party maintainers, whose only structural disadvantage is precisely this data — which is why it is the sharpest competitive question in the sub-niche.
