# Cross-Border Delivery Estimation

**Industry:** [[dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Tracking aggregation is a mature service and merchants still promise delivery windows they invent, because nobody publishes a realistic distribution for a specific supplier, service and destination.
**Tags:** #time-series-forecasting #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #change-point-detection

## The Problem
A dropshipped order frequently crosses a border. It leaves an origin country on an economy service, transits, clears customs, and is handed to a domestic carrier for final delivery. Transit times range from days to many weeks and the variance is large.

The merchant must tell the customer something. What they have is the supplier's stated processing time and a shipping method name, and what they say is a range they largely invent. Customers who are given eight to fifteen days and receive the item in thirty-four are unhappy, leave a poor review, and file a marketplace claim — and the marketplace penalises the merchant's account metrics for late delivery.

Nobody publishes the real distribution. The platform routes millions of orders and holds the tracking history for all of them, which means it knows precisely how long this supplier's shipments on this service to this country actually take, and merchants are guessing.

Customs adds a step nobody models: duties, thresholds and clearance delays vary by destination and by declared value, and a shipment held in clearance is invisible in the tracking narrative until it moves.

## What Already Exists
Tracking aggregation services (AfterShip, 17TRACK and others) unify carrier events across the global network. Carriers publish estimated transit times, which are aspirational and generic. Some platforms display average delivery times by supplier. Marketplace policies define delivery expectations and penalise breaches. Duty and tax calculation services exist for cross-border commerce.

## The Customisation Gap
Published carrier estimates are national averages for a service and are not what a merchant needs, which is the distribution for a specific origin facility, service, destination country and time of year.

The platform can compute the real distribution and generally reports a mean if anything. A mean is the wrong statistic for a promise: the merchant needs a quantile they can commit to, because the cost of exceeding a promise is asymmetric and heavily weighted toward the late tail.

Customs clearance is unmodelled despite being a large and destination-specific component of the variance, and it is observable in the tracking event stream.

Seasonal and disruption effects are handled reactively. Peak season and known disruptions shift the distribution substantially, and a static estimate is wrong for weeks at a time when it matters most.

## Impact If Solved
Late delivery against a promised window drives marketplace penalties, refunds and poor reviews, and the promise is currently invented because the real distribution is unpublished. Quantile-based estimates from the platform's own tracking history would let merchants promise something they can keep, which is the single largest controllable factor in dropshipping customer satisfaction.
