# An Arrival Time Promised to a Stranded Customer and Never Scored

**Niche:** [[niches/towing-companies/roadside-assistance-network-analytics/profile|Roadside Assistance Network Analytics]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The network tells millions of stranded people when help will arrive, holds the actual arrival time for every one of them, and manages the promise as an operational average rather than as a forecast.
**Tags:** #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #time-series-forecasting

## The Problem
The moment that defines this business is a person on a shoulder being told a truck will arrive in a stated number of minutes. Everything downstream follows from it: whether the customer stays or calls someone else, whether the client insurer records a service failure, whether the driver arrives to find the car gone, and whether the network keeps the contract.

The estimate is generally produced by rules — the provider's stated coverage time, a distance calculation, an adjustment for conditions — and then managed against a service level agreement. Performance is reported as an average or as a percentage within a threshold.

That is a forecasting problem being treated as an operations metric. The network holds tens of millions of completed events with everything a model would need: origin and destination, time of day, day of week, weather, road type, service type, vehicle, provider identity, provider load at the moment of dispatch, and the actual arrival time. The label is exact and arrives within an hour.

Nothing about how the estimate is generated uses it. There is no per-event predicted distribution, so there is no way to say that this particular customer, at this location, on this night, in this weather, has an unusual amount of uncertainty — which is exactly when a promise most needs a range or a hedge. And there is generally no calibration reporting at all: a network can say what proportion of events met the SLA and cannot say whether the times it quoted were right.

The consequences are commercial and they compound. Under-promising loses customers to competitors and to direct calls. Over-promising produces the complaints and abandonment that dominate this category's customer experience. And the dispatch decision itself — which provider to send — is made on a rules-based estimate rather than on a predicted distribution of arrival times.

## Why Nobody Has Built This
Contracts are written against service levels, not against accuracy, so the metric everyone is measured on is the percentage of events inside a threshold. Nobody has ever been asked for calibration, and a metric nobody asks for does not get built.

There is also a defensive reflex about the estimate. A quoted time is heard as a commitment, so operations teams pad it. Padding degrades accuracy in a way that is invisible if accuracy is never measured, and it feels safe.

And the provider network is fragmented — tens of thousands of small operators, many with no telematics and no real-time position — so the inputs feel weaker than they are. In practice the historical record substitutes for live position better than most people assume, because the same provider covering the same area at the same time of day behaves consistently.

## What to Build
Arrival time as a predicted distribution, scored continuously.

**Model time to arrival as a hazard, not a point.** Arrival is a duration with real dispersion and occasional very long tails, and the tails are what generate complaints. A distributional model gives the median for the promise and the spread for the hedge.

**Use provider load at the moment of dispatch.** The strongest predictor of a late arrival is how many jobs the provider already holds, and the network knows this at dispatch time because it issued them.

**Predict acceptance and re-dispatch too.** A material share of events are declined or timed out and re-dispatched, and every re-dispatch resets the clock. Modelling acceptance probability jointly with arrival time is what turns a single-provider estimate into a real expectation for the customer.

**Make dispatch a decision, not a lookup.** Choosing between two providers is a comparison of predicted arrival distributions and acceptance probabilities, weighted by cost. That is an optimisation the network has every input for and does not run.

**Report calibration to clients.** Not just SLA attainment, but whether quoted times were accurate, by market and condition. In a category procured on service levels, the first network able to demonstrate calibrated promises has an argument no competitor can match with an average.

## Target Customer
Chief Data Officer or VP of Data Science at a roadside assistance network. The commercial case is direct: arrival time accuracy drives customer satisfaction, abandonment, and client retention, and it is currently produced by rules on top of one of the largest, cleanest, fastest-labelled prediction datasets in this entire index.

## Impact If Built
Tens of millions of roadside events a year are promised on a rules-based estimate whose accuracy nobody measures, in a business where the promise is the product. Calibrated arrival prediction improves the customer experience directly, reduces re-dispatch and abandonment cost, and makes dispatch an optimisation rather than a lookup.
