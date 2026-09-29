# The Delivery Window Everyone Invents

**Niche:** [[niches/dropshipping-suppliers/delivery-time-prediction/profile|Delivery Time Prediction]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tracking aggregation is a mature service and merchants still promise delivery windows they invent, because nobody publishes a realistic distribution for a specific supplier, service and destination.
**Tags:** #survival-analysis #time-series-forecasting #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to publish a delivery distribution for a specific supplier, service and destination that holds up — and whoever does that lets merchants make a promise instead of a guess.

## The Problem
The merchant writes twelve to twenty-five days on the shipping page. They chose those numbers because a forum said so. The actual distribution for this supplier, this service and this destination has a median of nineteen days and a long tail reaching sixty, and it shifts with season, customs and carrier capacity. When an order lands in the tail, the customer opens a dispute, the merchant refunds, and the marketplace records a late shipment. The platform has millions of completed journeys with full tracking, which is the labelled dataset for exactly this prediction, and it displays a tracking page.

## Why Nobody Has Built This
Tracking vendors sell visibility rather than prediction and the category bought visibility. Publishing an honest distribution means telling merchants their delivery times are worse than they advertise, which nobody wants to be first to do. The prediction requires joining supplier, service, route, destination and seasonal effects, which crosses system boundaries. And the cost of a bad promise falls on the merchant.

## What to Build
Predict the distribution, not a number. Model the full delivery time distribution per supplier, service and destination rather than an average, since the tail is where every dispute lives and a median is silent about it — this is the core and it is what makes the output actionable. Decompose the journey into supplier handling, first-mile, international leg, customs and last-mile, because each behaves differently and the decomposition is what makes the model both accurate and explainable. Include seasonality and known disruptions, as holiday and regional peak effects are large, predictable and currently absorbed as bad luck. Update in flight — once a parcel clears customs the remaining distribution is much tighter, and a revised estimate is worth more than the original. Detect stalls, which is the fix note's subject and the biggest single source of avoidable disputes. Publish a stated confidence level so the merchant chooses their promise deliberately: the date nine orders in ten will beat is a different business decision from the median, and merchants currently cannot express that choice at all. Feed the prediction into the storefront and the marketplace promise directly, since a number in a report changes nothing. Give suppliers their own handling-time distribution, which is frequently the largest and most controllable component and is unknown to them. Quantify the conversion cost of a longer honest promise against the dispute cost of a short dishonest one, which is the trade merchants are making blindly. And measure calibration — of orders promised by a date, what share arrived — because that is the only honest test.

## Target Customer
Dropshipping platforms, merchants and aggregators making shipping promises, and the tracking aggregation vendors who hold the data.

## Impact If Built
Millions of completed journeys with full tracking is the labelled dataset for this exact prediction, and it renders a tracking page. Modelling the distribution rather than a point makes the tail visible, and in-flight revision after customs is worth more than the original estimate.
