# Order Routing Across the Partner Network

**Industry:** [[print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Routing engines that assign orders to facilities by distance and capacity are standard, and the variable that determines whether the customer is happy — which facility prints this kind of work well — is not in the routing decision.
**Tags:** #optimization-fundamentals #gradient-boosting #convex-optimization #confidence-intervals #time-series-forecasting #evaluation-metrics #hypothesis-testing

## The Problem
A print-on-demand platform fulfils through a network of owned and partner facilities differing in geography, equipment, decoration methods, product catalogue, capacity and quality.

Each order must be assigned to one. The routing engine considers distance to the customer, whether the facility stocks the product, whether it supports the decoration method, and current capacity or lead time.

It does not consider quality, because quality per facility per work type is not measured. A facility that produces excellent embroidery and mediocre direct-to-garment on dark garments is treated as uniformly capable. A facility whose colour reproduction drifts between calibrations is treated as stable.

Nor does it consider predicted difficulty. An artwork likely to be problematic could be routed to the facility with the best record on that kind of work, and instead goes to the nearest one with capacity.

Capacity is also handled reactively. Facilities report lead times, the platform routes accordingly, and a partner that has quietly fallen behind produces late orders before the lead time updates.

## What Already Exists
Routing and order management across distributed fulfilment is standard in the category and technically capable. Facilities report capability and capacity. Shipping cost and transit time calculation is mature. Lead time tracking exists. Some platforms allow merchants to select a preferred facility. Partner onboarding includes quality standards and periodic audits.

## The Customisation Gap
Quality is absent from routing because it is not measured at the granularity routing needs. Reprint rate, complaint rate and return rate by facility, product, decoration method and artwork type are computable from existing order data and are generally reported at facility level if at all — which is far too coarse, since the interesting variation is within a facility across work types.

Predicted difficulty is not used. Once outcome prediction exists, routing hard jobs to capable facilities is the obvious application and it changes the objective from cost minimisation to expected-cost minimisation including reprint risk.

Capacity is reported rather than predicted. A facility's realistic throughput is forecastable from its own history, seasonality and current queue, and reactive lead time updates mean the platform learns about a backlog after committing orders into it.

Calibration state is invisible. Print quality drifts with equipment maintenance cycles, and drift is detectable in outcome data before it becomes a complaint pattern — which is early warning the partner would also value.

## Impact If Solved
Routing determines both the cost and the quality of every order, and it currently optimises the half that is easy to measure. Adding measured quality by work type and predicted difficulty turns routing into expected-cost optimisation, and calibration drift detection catches a quality decline before customers do.
